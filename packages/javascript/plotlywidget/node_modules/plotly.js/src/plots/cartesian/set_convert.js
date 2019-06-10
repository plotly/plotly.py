/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');
var cleanNumber = Lib.cleanNumber;
var ms2DateTime = Lib.ms2DateTime;
var dateTime2ms = Lib.dateTime2ms;
var ensureNumber = Lib.ensureNumber;
var isArrayOrTypedArray = Lib.isArrayOrTypedArray;

var numConstants = require('../../constants/numerical');
var FP_SAFE = numConstants.FP_SAFE;
var BADNUM = numConstants.BADNUM;
var LOG_CLIP = numConstants.LOG_CLIP;

var constants = require('./constants');
var axisIds = require('./axis_ids');

function fromLog(v) {
    return Math.pow(10, v);
}

function isValidCategory(v) {
    return v !== null && v !== undefined;
}

/**
 * Define the conversion functions for an axis data is used in 5 ways:
 *
 *  d: data, in whatever form it's provided
 *  c: calcdata: turned into numbers, but not linearized
 *  l: linearized - same as c except for log axes (and other nonlinear
 *      mappings later?) this is used when we need to know if it's
 *      *possible* to show some data on this axis, without caring about
 *      the current range
 *  p: pixel value - mapped to the screen with current size and zoom
 *  r: ranges, tick0, and annotation positions match one of the above
 *     but are handled differently for different types:
 *     - linear and date: data format (d)
 *     - category: calcdata format (c), and will stay that way because
 *       the data format has no continuous mapping
 *     - log: linearized (l) format
 *       TODO: in v2.0 we plan to change it to data format. At that point
 *       shapes will work the same way as ranges, tick0, and annotations
 *       so they can use this conversion too.
 *
 * Creates/updates these conversion functions, and a few more utilities
 * like cleanRange, and makeCalcdata
 *
 * also clears the autotick constraints ._minDtick, ._forceTick0
 */
module.exports = function setConvert(ax, fullLayout) {
    fullLayout = fullLayout || {};

    var axId = (ax._id || 'x');
    var axLetter = axId.charAt(0);

    function toLog(v, clip) {
        if(v > 0) return Math.log(v) / Math.LN10;

        else if(v <= 0 && clip && ax.range && ax.range.length === 2) {
            // clip NaN (ie past negative infinity) to LOG_CLIP axis
            // length past the negative edge
            var r0 = ax.range[0];
            var r1 = ax.range[1];
            return 0.5 * (r0 + r1 - 2 * LOG_CLIP * Math.abs(r0 - r1));
        } else return BADNUM;
    }

    /*
     * wrapped dateTime2ms that:
     * - accepts ms numbers for backward compatibility
     * - inserts a dummy arg so calendar is the 3rd arg (see notes below).
     * - defaults to ax.calendar
     */
    function dt2ms(v, _, calendar) {
        // NOTE: Changed this behavior: previously we took any numeric value
        // to be a ms, even if it was a string that could be a bare year.
        // Now we convert it as a date if at all possible, and only try
        // as (local) ms if that fails.
        var ms = dateTime2ms(v, calendar || ax.calendar);
        if(ms === BADNUM) {
            if(isNumeric(v)) {
                v = +v;
                // keep track of tenths of ms, that `new Date` will drop
                // same logic as in Lib.ms2DateTime
                var msecTenths = Math.floor(Lib.mod(v + 0.05, 1) * 10);
                var msRounded = Math.round(v - msecTenths / 10);
                ms = dateTime2ms(new Date(msRounded)) + msecTenths / 10;
            } else return BADNUM;
        }
        return ms;
    }

    // wrapped ms2DateTime to insert default ax.calendar
    function ms2dt(v, r, calendar) {
        return ms2DateTime(v, r, calendar || ax.calendar);
    }

    function getCategoryName(v) {
        return ax._categories[Math.round(v)];
    }

    /*
     * setCategoryIndex: return the index of category v,
     * inserting it in the list if it's not already there
     *
     * this will enter the categories in the order it
     * encounters them, ie all the categories from the
     * first data set, then all the ones from the second
     * that aren't in the first etc.
     *
     * it is assumed that this function is being invoked in the
     * already sorted category order; otherwise there would be
     * a disconnect between the array and the index returned
     */
    function setCategoryIndex(v) {
        if(isValidCategory(v)) {
            if(ax._categoriesMap === undefined) {
                ax._categoriesMap = {};
            }

            if(ax._categoriesMap[v] !== undefined) {
                return ax._categoriesMap[v];
            } else {
                ax._categories.push(typeof v === 'number' ? String(v) : v);

                var curLength = ax._categories.length - 1;
                ax._categoriesMap[v] = curLength;

                return curLength;
            }
        }
        return BADNUM;
    }

    function setMultiCategoryIndex(arrayIn, len) {
        var arrayOut = new Array(len);

        for(var i = 0; i < len; i++) {
            var v0 = (arrayIn[0] || [])[i];
            var v1 = (arrayIn[1] || [])[i];
            arrayOut[i] = getCategoryIndex([v0, v1]);
        }

        return arrayOut;
    }

    function getCategoryIndex(v) {
        if(ax._categoriesMap) {
            return ax._categoriesMap[v];
        }
    }

    function getCategoryPosition(v) {
        // d2l/d2c variant that that won't add categories but will also
        // allow numbers to be mapped to the linearized axis positions
        var index = getCategoryIndex(v);
        if(index !== undefined) return index;
        if(isNumeric(v)) return +v;
    }

    function l2p(v) {
        if(!isNumeric(v)) return BADNUM;

        // include 2 fractional digits on pixel, for PDF zooming etc
        return d3.round(ax._b + ax._m * v, 2);
    }

    function p2l(px) { return (px - ax._b) / ax._m; }

    // conversions among c/l/p are fairly simple - do them together for all axis types
    ax.c2l = (ax.type === 'log') ? toLog : ensureNumber;
    ax.l2c = (ax.type === 'log') ? fromLog : ensureNumber;

    ax.l2p = l2p;
    ax.p2l = p2l;

    ax.c2p = (ax.type === 'log') ? function(v, clip) { return l2p(toLog(v, clip)); } : l2p;
    ax.p2c = (ax.type === 'log') ? function(px) { return fromLog(p2l(px)); } : p2l;

    /*
     * now type-specific conversions for **ALL** other combinations
     * they're all written out, instead of being combinations of each other, for
     * both clarity and speed.
     */
    if(['linear', '-'].indexOf(ax.type) !== -1) {
        // all are data vals, but d and r need cleaning
        ax.d2r = ax.r2d = ax.d2c = ax.r2c = ax.d2l = ax.r2l = cleanNumber;
        ax.c2d = ax.c2r = ax.l2d = ax.l2r = ensureNumber;

        ax.d2p = ax.r2p = function(v) { return ax.l2p(cleanNumber(v)); };
        ax.p2d = ax.p2r = p2l;

        ax.cleanPos = ensureNumber;
    } else if(ax.type === 'log') {
        // d and c are data vals, r and l are logged (but d and r need cleaning)
        ax.d2r = ax.d2l = function(v, clip) { return toLog(cleanNumber(v), clip); };
        ax.r2d = ax.r2c = function(v) { return fromLog(cleanNumber(v)); };

        ax.d2c = ax.r2l = cleanNumber;
        ax.c2d = ax.l2r = ensureNumber;

        ax.c2r = toLog;
        ax.l2d = fromLog;

        ax.d2p = function(v, clip) { return ax.l2p(ax.d2r(v, clip)); };
        ax.p2d = function(px) { return fromLog(p2l(px)); };

        ax.r2p = function(v) { return ax.l2p(cleanNumber(v)); };
        ax.p2r = p2l;

        ax.cleanPos = ensureNumber;
    } else if(ax.type === 'date') {
        // r and d are date strings, l and c are ms

        /*
         * Any of these functions with r and d on either side, calendar is the
         * **3rd** argument. log has reserved the second argument.
         *
         * Unless you need the special behavior of the second arg (ms2DateTime
         * uses this to limit precision, toLog uses true to clip negatives
         * to offscreen low rather than undefined), it's safe to pass 0.
         */
        ax.d2r = ax.r2d = Lib.identity;

        ax.d2c = ax.r2c = ax.d2l = ax.r2l = dt2ms;
        ax.c2d = ax.c2r = ax.l2d = ax.l2r = ms2dt;

        ax.d2p = ax.r2p = function(v, _, calendar) { return ax.l2p(dt2ms(v, 0, calendar)); };
        ax.p2d = ax.p2r = function(px, r, calendar) { return ms2dt(p2l(px), r, calendar); };

        ax.cleanPos = function(v) { return Lib.cleanDate(v, BADNUM, ax.calendar); };
    } else if(ax.type === 'category') {
        // d is categories (string)
        // c and l are indices (numbers)
        // r is categories or numbers

        ax.d2c = ax.d2l = setCategoryIndex;
        ax.r2d = ax.c2d = ax.l2d = getCategoryName;

        ax.d2r = ax.d2l_noadd = getCategoryPosition;

        ax.r2c = function(v) {
            var index = getCategoryPosition(v);
            return index !== undefined ? index : ax.fraction2r(0.5);
        };

        ax.l2r = ax.c2r = ensureNumber;
        ax.r2l = getCategoryPosition;

        ax.d2p = function(v) { return ax.l2p(ax.r2c(v)); };
        ax.p2d = function(px) { return getCategoryName(p2l(px)); };
        ax.r2p = ax.d2p;
        ax.p2r = p2l;

        ax.cleanPos = function(v) {
            if(typeof v === 'string' && v !== '') return v;
            return ensureNumber(v);
        };
    } else if(ax.type === 'multicategory') {
        // N.B. multicategory axes don't define d2c and d2l,
        // as 'data-to-calcdata' conversion needs to take into
        // account all data array items as in ax.makeCalcdata.

        ax.r2d = ax.c2d = ax.l2d = getCategoryName;
        ax.d2r = ax.d2l_noadd = getCategoryPosition;

        ax.r2c = function(v) {
            var index = getCategoryPosition(v);
            return index !== undefined ? index : ax.fraction2r(0.5);
        };

        ax.r2c_just_indices = getCategoryIndex;

        ax.l2r = ax.c2r = ensureNumber;
        ax.r2l = getCategoryPosition;

        ax.d2p = function(v) { return ax.l2p(ax.r2c(v)); };
        ax.p2d = function(px) { return getCategoryName(p2l(px)); };
        ax.r2p = ax.d2p;
        ax.p2r = p2l;

        ax.cleanPos = function(v) {
            if(Array.isArray(v) || (typeof v === 'string' && v !== '')) return v;
            return ensureNumber(v);
        };

        ax.setupMultiCategory = function(fullData) {
            var traceIndices = ax._traceIndices;
            var i, j;

            var matchGroups = fullLayout._axisMatchGroups;
            if(matchGroups && matchGroups.length && ax._categories.length === 0) {
                for(i = 0; i < matchGroups.length; i++) {
                    var group = matchGroups[i];
                    if(group[axId]) {
                        for(var axId2 in group) {
                            if(axId2 !== axId) {
                                var ax2 = fullLayout[axisIds.id2name(axId2)];
                                traceIndices = traceIndices.concat(ax2._traceIndices);
                            }
                        }
                    }
                }
            }

            // [ [cnt, {$cat: index}], for 1,2 ]
            var seen = [[0, {}], [0, {}]];
            // [ [arrayIn[0][i], arrayIn[1][i]], for i .. N ]
            var list = [];

            for(i = 0; i < traceIndices.length; i++) {
                var trace = fullData[traceIndices[i]];

                if(axLetter in trace) {
                    var arrayIn = trace[axLetter];
                    var len = trace._length || Lib.minRowLength(arrayIn);

                    if(isArrayOrTypedArray(arrayIn[0]) && isArrayOrTypedArray(arrayIn[1])) {
                        for(j = 0; j < len; j++) {
                            var v0 = arrayIn[0][j];
                            var v1 = arrayIn[1][j];

                            if(isValidCategory(v0) && isValidCategory(v1)) {
                                list.push([v0, v1]);

                                if(!(v0 in seen[0][1])) {
                                    seen[0][1][v0] = seen[0][0]++;
                                }
                                if(!(v1 in seen[1][1])) {
                                    seen[1][1][v1] = seen[1][0]++;
                                }
                            }
                        }
                    }
                }
            }

            list.sort(function(a, b) {
                var ind0 = seen[0][1];
                var d = ind0[a[0]] - ind0[b[0]];
                if(d) return d;

                var ind1 = seen[1][1];
                return ind1[a[1]] - ind1[b[1]];
            });

            for(i = 0; i < list.length; i++) {
                setCategoryIndex(list[i]);
            }
        };
    }

    // find the range value at the specified (linear) fraction of the axis
    ax.fraction2r = function(v) {
        var rl0 = ax.r2l(ax.range[0]);
        var rl1 = ax.r2l(ax.range[1]);
        return ax.l2r(rl0 + v * (rl1 - rl0));
    };

    // find the fraction of the range at the specified range value
    ax.r2fraction = function(v) {
        var rl0 = ax.r2l(ax.range[0]);
        var rl1 = ax.r2l(ax.range[1]);
        return (ax.r2l(v) - rl0) / (rl1 - rl0);
    };

    /*
     * cleanRange: make sure range is a couplet of valid & distinct values
     * keep numbers away from the limits of floating point numbers,
     * and dates away from the ends of our date system (+/- 9999 years)
     *
     * optional param rangeAttr: operate on a different attribute, like
     * ax._r, rather than ax.range
     */
    ax.cleanRange = function(rangeAttr, opts) {
        if(!opts) opts = {};
        if(!rangeAttr) rangeAttr = 'range';

        var range = Lib.nestedProperty(ax, rangeAttr).get();
        var i, dflt;

        if(ax.type === 'date') dflt = Lib.dfltRange(ax.calendar);
        else if(axLetter === 'y') dflt = constants.DFLTRANGEY;
        else dflt = opts.dfltRange || constants.DFLTRANGEX;

        // make sure we don't later mutate the defaults
        dflt = dflt.slice();

        if(!range || range.length !== 2) {
            Lib.nestedProperty(ax, rangeAttr).set(dflt);
            return;
        }

        if(ax.type === 'date' && !ax.autorange) {
            // check if milliseconds or js date objects are provided for range
            // and convert to date strings
            range[0] = Lib.cleanDate(range[0], BADNUM, ax.calendar);
            range[1] = Lib.cleanDate(range[1], BADNUM, ax.calendar);
        }

        for(i = 0; i < 2; i++) {
            if(ax.type === 'date') {
                if(!Lib.isDateTime(range[i], ax.calendar)) {
                    ax[rangeAttr] = dflt;
                    break;
                }

                if(ax.r2l(range[0]) === ax.r2l(range[1])) {
                    // split by +/- 1 second
                    var linCenter = Lib.constrain(ax.r2l(range[0]),
                        Lib.MIN_MS + 1000, Lib.MAX_MS - 1000);
                    range[0] = ax.l2r(linCenter - 1000);
                    range[1] = ax.l2r(linCenter + 1000);
                    break;
                }
            } else {
                if(!isNumeric(range[i])) {
                    if(isNumeric(range[1 - i])) {
                        range[i] = range[1 - i] * (i ? 10 : 0.1);
                    } else {
                        ax[rangeAttr] = dflt;
                        break;
                    }
                }

                if(range[i] < -FP_SAFE) range[i] = -FP_SAFE;
                else if(range[i] > FP_SAFE) range[i] = FP_SAFE;

                if(range[0] === range[1]) {
                    // somewhat arbitrary: split by 1 or 1ppm, whichever is bigger
                    var inc = Math.max(1, Math.abs(range[0] * 1e-6));
                    range[0] -= inc;
                    range[1] += inc;
                }
            }
        }
    };

    // set scaling to pixels
    ax.setScale = function(usePrivateRange) {
        var gs = fullLayout._size;

        // make sure we have a domain (pull it in from the axis
        // this one is overlaying if necessary)
        if(ax.overlaying) {
            var ax2 = axisIds.getFromId({ _fullLayout: fullLayout }, ax.overlaying);
            ax.domain = ax2.domain;
        }

        // While transitions are occuring, occurring, we get a double-transform
        // issue if we transform the drawn layer *and* use the new axis range to
        // draw the data. This allows us to construct setConvert using the pre-
        // interaction values of the range:
        var rangeAttr = (usePrivateRange && ax._r) ? '_r' : 'range';
        var calendar = ax.calendar;
        ax.cleanRange(rangeAttr);

        var rl0 = ax.r2l(ax[rangeAttr][0], calendar);
        var rl1 = ax.r2l(ax[rangeAttr][1], calendar);

        if(axLetter === 'y') {
            ax._offset = gs.t + (1 - ax.domain[1]) * gs.h;
            ax._length = gs.h * (ax.domain[1] - ax.domain[0]);
            ax._m = ax._length / (rl0 - rl1);
            ax._b = -ax._m * rl1;
        } else {
            ax._offset = gs.l + ax.domain[0] * gs.w;
            ax._length = gs.w * (ax.domain[1] - ax.domain[0]);
            ax._m = ax._length / (rl1 - rl0);
            ax._b = -ax._m * rl0;
        }

        if(!isFinite(ax._m) || !isFinite(ax._b) || ax._length < 0) {
            fullLayout._replotting = false;
            throw new Error('Something went wrong with axis scaling');
        }
    };

    // makeCalcdata: takes an x or y array and converts it
    // to a position on the axis object "ax"
    // inputs:
    //      trace - a data object from gd.data
    //      axLetter - a string, either 'x' or 'y', for which item
    //          to convert (TODO: is this now always the same as
    //          the first letter of ax._id?)
    // in case the expected data isn't there, make a list of
    // integers based on the opposite data
    ax.makeCalcdata = function(trace, axLetter) {
        var arrayIn, arrayOut, i, len;

        var axType = ax.type;
        var cal = axType === 'date' && trace[axLetter + 'calendar'];

        if(axLetter in trace) {
            arrayIn = trace[axLetter];
            len = trace._length || Lib.minRowLength(arrayIn);

            if(Lib.isTypedArray(arrayIn) && (axType === 'linear' || axType === 'log')) {
                if(len === arrayIn.length) {
                    return arrayIn;
                } else if(arrayIn.subarray) {
                    return arrayIn.subarray(0, len);
                }
            }

            if(axType === 'multicategory') {
                return setMultiCategoryIndex(arrayIn, len);
            }

            arrayOut = new Array(len);
            for(i = 0; i < len; i++) {
                arrayOut[i] = ax.d2c(arrayIn[i], 0, cal);
            }
        } else {
            var v0 = ((axLetter + '0') in trace) ? ax.d2c(trace[axLetter + '0'], 0, cal) : 0;
            var dv = (trace['d' + axLetter]) ? Number(trace['d' + axLetter]) : 1;

            // the opposing data, for size if we have x and dx etc
            arrayIn = trace[{x: 'y', y: 'x'}[axLetter]];
            len = trace._length || arrayIn.length;
            arrayOut = new Array(len);

            for(i = 0; i < len; i++) {
                arrayOut[i] = v0 + i * dv;
            }
        }

        return arrayOut;
    };

    ax.isValidRange = function(range) {
        return (
            Array.isArray(range) &&
            range.length === 2 &&
            isNumeric(ax.r2l(range[0])) &&
            isNumeric(ax.r2l(range[1]))
        );
    };

    ax.isPtWithinRange = function(d, calendar) {
        var coord = ax.c2l(d[axLetter], null, calendar);
        var r0 = ax.r2l(ax.range[0]);
        var r1 = ax.r2l(ax.range[1]);

        if(r0 < r1) {
            return r0 <= coord && coord <= r1;
        } else {
            // Reversed axis case.
            return r1 <= coord && coord <= r0;
        }
    };

    // should skip if not category nor multicategory
    ax.clearCalc = function() {
        var emptyCategories = function() {
            ax._categories = [];
            ax._categoriesMap = {};
        };

        var matchGroups = fullLayout._axisMatchGroups;

        if(matchGroups && matchGroups.length) {
            var found = false;

            for(var i = 0; i < matchGroups.length; i++) {
                var group = matchGroups[i];

                if(group[axId]) {
                    found = true;
                    var categories = null;
                    var categoriesMap = null;

                    for(var axId2 in group) {
                        var ax2 = fullLayout[axisIds.id2name(axId2)];
                        if(ax2._categories) {
                            categories = ax2._categories;
                            categoriesMap = ax2._categoriesMap;
                            break;
                        }
                    }

                    if(categories && categoriesMap) {
                        ax._categories = categories;
                        ax._categoriesMap = categoriesMap;
                    } else {
                        emptyCategories();
                    }
                    break;
                }
            }
            if(!found) emptyCategories();
        } else {
            emptyCategories();
        }

        if(ax._initialCategories) {
            for(var j = 0; j < ax._initialCategories.length; j++) {
                setCategoryIndex(ax._initialCategories[j]);
            }
        }
    };

    // sort the axis (and all the matching ones) by _initialCategories
    // returns the indices of the traces affected by the reordering
    ax.sortByInitialCategories = function() {
        var affectedTraces = [];
        var emptyCategories = function() {
            ax._categories = [];
            ax._categoriesMap = {};
        };

        emptyCategories();

        if(ax._initialCategories) {
            for(var j = 0; j < ax._initialCategories.length; j++) {
                setCategoryIndex(ax._initialCategories[j]);
            }
        }

        affectedTraces = affectedTraces.concat(ax._traceIndices);

        // Propagate to matching axes
        var group = ax._matchGroup;
        for(var axId2 in group) {
            if(axId === axId2) continue;
            var ax2 = fullLayout[axisIds.id2name(axId2)];
            ax2._categories = ax._categories;
            ax2._categoriesMap = ax._categoriesMap;
            affectedTraces = affectedTraces.concat(ax2._traceIndices);
        }
        return affectedTraces;
    };

    // Propagate localization into the axis so that
    // methods in Axes can use it w/o having to pass fullLayout
    // Default (non-d3) number formatting uses separators directly
    // dates and d3-formatted numbers use the d3 locale
    // Fall back on default format for dummy axes that don't care about formatting
    var locale = fullLayout._d3locale;
    if(ax.type === 'date') {
        ax._dateFormat = locale ? locale.timeFormat.utc : d3.time.format.utc;
        ax._extraFormat = fullLayout._extraFormat;
    }
    // occasionally we need _numFormat to pass through
    // even though it won't be needed by this axis
    ax._separators = fullLayout.separators;
    ax._numFormat = locale ? locale.numberFormat : d3.format;

    // and for bar charts and box plots: reset forced minimum tick spacing
    delete ax._minDtick;
    delete ax._forceTick0;
};
