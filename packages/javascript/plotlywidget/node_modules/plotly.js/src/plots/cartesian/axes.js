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
var Plots = require('../../plots/plots');

var Registry = require('../../registry');
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');
var Titles = require('../../components/titles');
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');

var axAttrs = require('./layout_attributes');
var cleanTicks = require('./clean_ticks');

var constants = require('../../constants/numerical');
var ONEAVGYEAR = constants.ONEAVGYEAR;
var ONEAVGMONTH = constants.ONEAVGMONTH;
var ONEDAY = constants.ONEDAY;
var ONEHOUR = constants.ONEHOUR;
var ONEMIN = constants.ONEMIN;
var ONESEC = constants.ONESEC;
var MINUS_SIGN = constants.MINUS_SIGN;
var BADNUM = constants.BADNUM;

var MID_SHIFT = require('../../constants/alignment').MID_SHIFT;
var LINE_SPACING = require('../../constants/alignment').LINE_SPACING;

var axes = module.exports = {};

axes.setConvert = require('./set_convert');
var autoType = require('./axis_autotype');

var axisIds = require('./axis_ids');
axes.id2name = axisIds.id2name;
axes.name2id = axisIds.name2id;
axes.cleanId = axisIds.cleanId;
axes.list = axisIds.list;
axes.listIds = axisIds.listIds;
axes.getFromId = axisIds.getFromId;
axes.getFromTrace = axisIds.getFromTrace;

var autorange = require('./autorange');
axes.getAutoRange = autorange.getAutoRange;
axes.findExtremes = autorange.findExtremes;

/*
 * find the list of possible axes to reference with an xref or yref attribute
 * and coerce it to that list
 *
 * attr: the attribute we're generating a reference for. Should end in 'x' or 'y'
 *     but can be prefixed, like 'ax' for annotation's arrow x
 * dflt: the default to coerce to, or blank to use the first axis (falling back on
 *     extraOption if there is no axis)
 * extraOption: aside from existing axes with this letter, what non-axis value is allowed?
 *     Only required if it's different from `dflt`
 */
axes.coerceRef = function(containerIn, containerOut, gd, attr, dflt, extraOption) {
    var axLetter = attr.charAt(attr.length - 1);
    var axlist = gd._fullLayout._subplots[axLetter + 'axis'];
    var refAttr = attr + 'ref';
    var attrDef = {};

    if(!dflt) dflt = axlist[0] || extraOption;
    if(!extraOption) extraOption = dflt;

    // data-ref annotations are not supported in gl2d yet

    attrDef[refAttr] = {
        valType: 'enumerated',
        values: axlist.concat(extraOption ? [extraOption] : []),
        dflt: dflt
    };

    // xref, yref
    return Lib.coerce(containerIn, containerOut, attrDef, refAttr);
};

/*
 * coerce position attributes (range-type) that can be either on axes or absolute
 * (paper or pixel) referenced. The biggest complication here is that we don't know
 * before looking at the axis whether the value must be a number or not (it may be
 * a date string), so we can't use the regular valType='number' machinery
 *
 * axRef (string): the axis this position is referenced to, or:
 *     paper: fraction of the plot area
 *     pixel: pixels relative to some starting position
 * attr (string): the attribute in containerOut we are coercing
 * dflt (number): the default position, as a fraction or pixels. If the attribute
 *     is to be axis-referenced, this will be converted to an axis data value
 *
 * Also cleans the values, since the attribute definition itself has to say
 * valType: 'any' to handle date axes. This allows us to accept:
 * - for category axes: category names, and convert them here into serial numbers.
 *   Note that this will NOT work for axis range endpoints, because we don't know
 *   the category list yet (it's set by ax.makeCalcdata during calc)
 *   but it works for component (note, shape, images) positions.
 * - for date axes: JS Dates or milliseconds, and convert to date strings
 * - for other types: coerce them to numbers
 */
axes.coercePosition = function(containerOut, gd, coerce, axRef, attr, dflt) {
    var cleanPos, pos;

    if(axRef === 'paper' || axRef === 'pixel') {
        cleanPos = Lib.ensureNumber;
        pos = coerce(attr, dflt);
    } else {
        var ax = axes.getFromId(gd, axRef);
        dflt = ax.fraction2r(dflt);
        pos = coerce(attr, dflt);
        cleanPos = ax.cleanPos;
    }

    containerOut[attr] = cleanPos(pos);
};

axes.cleanPosition = function(pos, gd, axRef) {
    var cleanPos = (axRef === 'paper' || axRef === 'pixel') ?
        Lib.ensureNumber :
        axes.getFromId(gd, axRef).cleanPos;

    return cleanPos(pos);
};

axes.redrawComponents = function(gd, axIds) {
    axIds = axIds ? axIds : axes.listIds(gd);

    var fullLayout = gd._fullLayout;

    function _redrawOneComp(moduleName, methodName, stashName, shortCircuit) {
        var method = Registry.getComponentMethod(moduleName, methodName);
        var stash = {};

        for(var i = 0; i < axIds.length; i++) {
            var ax = fullLayout[axes.id2name(axIds[i])];
            var indices = ax[stashName];

            for(var j = 0; j < indices.length; j++) {
                var ind = indices[j];

                if(!stash[ind]) {
                    method(gd, ind);
                    stash[ind] = 1;
                    // once is enough for images (which doesn't use the `i` arg anyway)
                    if(shortCircuit) return;
                }
            }
        }
    }

    // annotations and shapes 'draw' method is slow,
    // use the finer-grained 'drawOne' method instead
    _redrawOneComp('annotations', 'drawOne', '_annIndices');
    _redrawOneComp('shapes', 'drawOne', '_shapeIndices');
    _redrawOneComp('images', 'draw', '_imgIndices', true);
};

var getDataConversions = axes.getDataConversions = function(gd, trace, target, targetArray) {
    var ax;

    // If target points to an axis, use the type we already have for that
    // axis to find the data type. Otherwise use the values to autotype.
    var d2cTarget = (target === 'x' || target === 'y' || target === 'z') ?
        target :
        targetArray;

    // In the case of an array target, make a mock data array
    // and call supplyDefaults to the data type and
    // setup the data-to-calc method.
    if(Array.isArray(d2cTarget)) {
        ax = {
            type: autoType(targetArray),
            _categories: []
        };
        axes.setConvert(ax);

        // build up ax._categories (usually done during ax.makeCalcdata()
        if(ax.type === 'category') {
            for(var i = 0; i < targetArray.length; i++) {
                ax.d2c(targetArray[i]);
            }
        }
        // TODO what to do for transforms?
    } else {
        ax = axes.getFromTrace(gd, trace, d2cTarget);
    }

    // if 'target' has corresponding axis
    // -> use setConvert method
    if(ax) return {d2c: ax.d2c, c2d: ax.c2d};

    // special case for 'ids'
    // -> cast to String
    if(d2cTarget === 'ids') return {d2c: toString, c2d: toString};

    // otherwise (e.g. numeric-array of 'marker.color' or 'marker.size')
    // -> cast to Number

    return {d2c: toNum, c2d: toNum};
};

function toNum(v) { return +v; }
function toString(v) { return String(v); }

axes.getDataToCoordFunc = function(gd, trace, target, targetArray) {
    return getDataConversions(gd, trace, target, targetArray).d2c;
};

// get counteraxis letter for this axis (name or id)
// this can also be used as the id for default counter axis
axes.counterLetter = function(id) {
    var axLetter = id.charAt(0);
    if(axLetter === 'x') return 'y';
    if(axLetter === 'y') return 'x';
};

// incorporate a new minimum difference and first tick into
// forced
// note that _forceTick0 is linearized, so needs to be turned into
// a range value for setting tick0
axes.minDtick = function(ax, newDiff, newFirst, allow) {
    // doesn't make sense to do forced min dTick on log or category axes,
    // and the plot itself may decide to cancel (ie non-grouped bars)
    if(['log', 'category', 'multicategory'].indexOf(ax.type) !== -1 || !allow) {
        ax._minDtick = 0;
    } else if(ax._minDtick === undefined) {
        // undefined means there's nothing there yet

        ax._minDtick = newDiff;
        ax._forceTick0 = newFirst;
    } else if(ax._minDtick) {
        if((ax._minDtick / newDiff + 1e-6) % 1 < 2e-6 &&
            // existing minDtick is an integer multiple of newDiff
            // (within rounding err)
            // and forceTick0 can be shifted to newFirst

                (((newFirst - ax._forceTick0) / newDiff % 1) +
                    1.000001) % 1 < 2e-6) {
            ax._minDtick = newDiff;
            ax._forceTick0 = newFirst;
        } else if((newDiff / ax._minDtick + 1e-6) % 1 > 2e-6 ||
            // if the converse is true (newDiff is a multiple of minDtick and
            // newFirst can be shifted to forceTick0) then do nothing - same
            // forcing stands. Otherwise, cancel forced minimum

                (((newFirst - ax._forceTick0) / ax._minDtick % 1) +
                    1.000001) % 1 > 2e-6) {
            ax._minDtick = 0;
        }
    }
};

// save a copy of the initial axis ranges in fullLayout
// use them in mode bar and dblclick events
axes.saveRangeInitial = function(gd, overwrite) {
    var axList = axes.list(gd, '', true);
    var hasOneAxisChanged = false;

    for(var i = 0; i < axList.length; i++) {
        var ax = axList[i];
        var isNew = (ax._rangeInitial === undefined);
        var hasChanged = isNew || !(
            ax.range[0] === ax._rangeInitial[0] &&
            ax.range[1] === ax._rangeInitial[1]
        );

        if((isNew && ax.autorange === false) || (overwrite && hasChanged)) {
            ax._rangeInitial = ax.range.slice();
            hasOneAxisChanged = true;
        }
    }

    return hasOneAxisChanged;
};

// save a copy of the initial spike visibility
axes.saveShowSpikeInitial = function(gd, overwrite) {
    var axList = axes.list(gd, '', true);
    var hasOneAxisChanged = false;
    var allSpikesEnabled = 'on';

    for(var i = 0; i < axList.length; i++) {
        var ax = axList[i];
        var isNew = (ax._showSpikeInitial === undefined);
        var hasChanged = isNew || !(ax.showspikes === ax._showspikes);

        if(isNew || (overwrite && hasChanged)) {
            ax._showSpikeInitial = ax.showspikes;
            hasOneAxisChanged = true;
        }

        if(allSpikesEnabled === 'on' && !ax.showspikes) {
            allSpikesEnabled = 'off';
        }
    }
    gd._fullLayout._cartesianSpikesEnabled = allSpikesEnabled;
    return hasOneAxisChanged;
};

axes.autoBin = function(data, ax, nbins, is2d, calendar, size) {
    var dataMin = Lib.aggNums(Math.min, null, data);
    var dataMax = Lib.aggNums(Math.max, null, data);

    if(ax.type === 'category' || ax.type === 'multicategory') {
        return {
            start: dataMin - 0.5,
            end: dataMax + 0.5,
            size: Math.max(1, Math.round(size) || 1),
            _dataSpan: dataMax - dataMin,
        };
    }

    if(!calendar) calendar = ax.calendar;

    // piggyback off tick code to make "nice" bin sizes and edges
    var dummyAx;
    if(ax.type === 'log') {
        dummyAx = {
            type: 'linear',
            range: [dataMin, dataMax]
        };
    } else {
        dummyAx = {
            type: ax.type,
            range: Lib.simpleMap([dataMin, dataMax], ax.c2r, 0, calendar),
            calendar: calendar
        };
    }
    axes.setConvert(dummyAx);

    size = size && cleanTicks.dtick(size, dummyAx.type);

    if(size) {
        dummyAx.dtick = size;
        dummyAx.tick0 = cleanTicks.tick0(undefined, dummyAx.type, calendar);
    } else {
        var size0;
        if(nbins) size0 = ((dataMax - dataMin) / nbins);
        else {
            // totally auto: scale off std deviation so the highest bin is
            // somewhat taller than the total number of bins, but don't let
            // the size get smaller than the 'nice' rounded down minimum
            // difference between values
            var distinctData = Lib.distinctVals(data);
            var msexp = Math.pow(10, Math.floor(
                Math.log(distinctData.minDiff) / Math.LN10));
            var minSize = msexp * Lib.roundUp(
                distinctData.minDiff / msexp, [0.9, 1.9, 4.9, 9.9], true);
            size0 = Math.max(minSize, 2 * Lib.stdev(data) /
                Math.pow(data.length, is2d ? 0.25 : 0.4));

            // fallback if ax.d2c output BADNUMs
            // e.g. when user try to plot categorical bins
            // on a layout.xaxis.type: 'linear'
            if(!isNumeric(size0)) size0 = 1;
        }

        axes.autoTicks(dummyAx, size0);
    }

    var finalSize = dummyAx.dtick;
    var binStart = axes.tickIncrement(
            axes.tickFirst(dummyAx), finalSize, 'reverse', calendar);
    var binEnd, bincount;

    // check for too many data points right at the edges of bins
    // (>50% within 1% of bin edges) or all data points integral
    // and offset the bins accordingly
    if(typeof finalSize === 'number') {
        binStart = autoShiftNumericBins(binStart, data, dummyAx, dataMin, dataMax);

        bincount = 1 + Math.floor((dataMax - binStart) / finalSize);
        binEnd = binStart + bincount * finalSize;
    } else {
        // month ticks - should be the only nonlinear kind we have at this point.
        // dtick (as supplied by axes.autoTick) only has nonlinear values on
        // date and log axes, but even if you display a histogram on a log axis
        // we bin it on a linear axis (which one could argue against, but that's
        // a separate issue)
        if(dummyAx.dtick.charAt(0) === 'M') {
            binStart = autoShiftMonthBins(binStart, data, finalSize, dataMin, calendar);
        }

        // calculate the endpoint for nonlinear ticks - you have to
        // just increment until you're done
        binEnd = binStart;
        bincount = 0;
        while(binEnd <= dataMax) {
            binEnd = axes.tickIncrement(binEnd, finalSize, false, calendar);
            bincount++;
        }
    }

    return {
        start: ax.c2r(binStart, 0, calendar),
        end: ax.c2r(binEnd, 0, calendar),
        size: finalSize,
        _dataSpan: dataMax - dataMin
    };
};


function autoShiftNumericBins(binStart, data, ax, dataMin, dataMax) {
    var edgecount = 0;
    var midcount = 0;
    var intcount = 0;
    var blankCount = 0;

    function nearEdge(v) {
        // is a value within 1% of a bin edge?
        return (1 + (v - binStart) * 100 / ax.dtick) % 100 < 2;
    }

    for(var i = 0; i < data.length; i++) {
        if(data[i] % 1 === 0) intcount++;
        else if(!isNumeric(data[i])) blankCount++;

        if(nearEdge(data[i])) edgecount++;
        if(nearEdge(data[i] + ax.dtick / 2)) midcount++;
    }
    var dataCount = data.length - blankCount;

    if(intcount === dataCount && ax.type !== 'date') {
        if(ax.dtick < 1) {
            // all integers: if bin size is <1, it's because
            // that was specifically requested (large nbins)
            // so respect that... but center the bins containing
            // integers on those integers

            binStart = dataMin - 0.5 * ax.dtick;
        } else {
            // otherwise start half an integer down regardless of
            // the bin size, just enough to clear up endpoint
            // ambiguity about which integers are in which bins.

            binStart -= 0.5;
            if(binStart + ax.dtick < dataMin) binStart += ax.dtick;
        }
    } else if(midcount < dataCount * 0.1) {
        if(edgecount > dataCount * 0.3 ||
                nearEdge(dataMin) || nearEdge(dataMax)) {
            // lots of points at the edge, not many in the middle
            // shift half a bin
            var binshift = ax.dtick / 2;
            binStart += (binStart + binshift < dataMin) ? binshift : -binshift;
        }
    }
    return binStart;
}


function autoShiftMonthBins(binStart, data, dtick, dataMin, calendar) {
    var stats = Lib.findExactDates(data, calendar);
    // number of data points that needs to be an exact value
    // to shift that increment to (near) the bin center
    var threshold = 0.8;

    if(stats.exactDays > threshold) {
        var numMonths = Number(dtick.substr(1));

        if((stats.exactYears > threshold) && (numMonths % 12 === 0)) {
            // The exact middle of a non-leap-year is 1.5 days into July
            // so if we start the bins here, all but leap years will
            // get hover-labeled as exact years.
            binStart = axes.tickIncrement(binStart, 'M6', 'reverse') + ONEDAY * 1.5;
        } else if(stats.exactMonths > threshold) {
            // Months are not as clean, but if we shift half the *longest*
            // month (31/2 days) then 31-day months will get labeled exactly
            // and shorter months will get labeled with the correct month
            // but shifted 12-36 hours into it.
            binStart = axes.tickIncrement(binStart, 'M1', 'reverse') + ONEDAY * 15.5;
        } else {
            // Shifting half a day is exact, but since these are month bins it
            // will always give a somewhat odd-looking label, until we do something
            // smarter like showing the bin boundaries (or the bounds of the actual
            // data in each bin)
            binStart -= ONEDAY / 2;
        }
        var nextBinStart = axes.tickIncrement(binStart, dtick);

        if(nextBinStart <= dataMin) return nextBinStart;
    }
    return binStart;
}

// ----------------------------------------------------
// Ticks and grids
// ----------------------------------------------------

// ensure we have tick0, dtick, and tick rounding calculated
axes.prepTicks = function(ax) {
    var rng = Lib.simpleMap(ax.range, ax.r2l);

    // calculate max number of (auto) ticks to display based on plot size
    if(ax.tickmode === 'auto' || !ax.dtick) {
        var nt = ax.nticks;
        var minPx;

        if(!nt) {
            if(ax.type === 'category' || ax.type === 'multicategory') {
                minPx = ax.tickfont ? (ax.tickfont.size || 12) * 1.2 : 15;
                nt = ax._length / minPx;
            } else {
                minPx = ax._id.charAt(0) === 'y' ? 40 : 80;
                nt = Lib.constrain(ax._length / minPx, 4, 9) + 1;
            }

            // radial axes span half their domain,
            // multiply nticks value by two to get correct number of auto ticks.
            if(ax._name === 'radialaxis') nt *= 2;
        }

        // add a couple of extra digits for filling in ticks when we
        // have explicit tickvals without tick text
        if(ax.tickmode === 'array') nt *= 100;

        axes.autoTicks(ax, Math.abs(rng[1] - rng[0]) / nt);
        // check for a forced minimum dtick
        if(ax._minDtick > 0 && ax.dtick < ax._minDtick * 2) {
            ax.dtick = ax._minDtick;
            ax.tick0 = ax.l2r(ax._forceTick0);
        }
    }

    // check for missing tick0
    if(!ax.tick0) {
        ax.tick0 = (ax.type === 'date') ? '2000-01-01' : 0;
    }

    // ensure we don't try to make ticks below our minimum precision
    // see https://github.com/plotly/plotly.js/issues/2892
    if(ax.type === 'date' && ax.dtick < 0.1) ax.dtick = 0.1;

    // now figure out rounding of tick values
    autoTickRound(ax);
};

// calculate the ticks: text, values, positioning
// if ticks are set to automatic, determine the right values (tick0,dtick)
// in any case, set tickround to # of digits to round tick labels to,
// or codes to this effect for log and date scales
axes.calcTicks = function calcTicks(ax) {
    axes.prepTicks(ax);
    var rng = Lib.simpleMap(ax.range, ax.r2l);

    // now that we've figured out the auto values for formatting
    // in case we're missing some ticktext, we can break out for array ticks
    if(ax.tickmode === 'array') return arrayTicks(ax);

    // find the first tick
    ax._tmin = axes.tickFirst(ax);

    // add a tiny bit so we get ticks which may have rounded out
    var startTick = rng[0] * 1.0001 - rng[1] * 0.0001;
    var endTick = rng[1] * 1.0001 - rng[0] * 0.0001;
    // check for reversed axis
    var axrev = (rng[1] < rng[0]);

    // No visible ticks? Quit.
    // I've only seen this on category axes with all categories off the edge.
    if((ax._tmin < startTick) !== axrev) return [];

    // return the full set of tick vals
    var vals = [];
    if(ax.type === 'category' || ax.type === 'multicategory') {
        endTick = (axrev) ? Math.max(-0.5, endTick) :
            Math.min(ax._categories.length - 0.5, endTick);
    }

    var xPrevious = null;
    var maxTicks = Math.max(1000, ax._length || 0);
    for(var x = ax._tmin;
            (axrev) ? (x >= endTick) : (x <= endTick);
            x = axes.tickIncrement(x, ax.dtick, axrev, ax.calendar)) {
        // prevent infinite loops - no more than one tick per pixel,
        // and make sure each value is different from the previous
        if(vals.length > maxTicks || x === xPrevious) break;
        xPrevious = x;

        vals.push(x);
    }

    // If same angle over a full circle, the last tick vals is a duplicate.
    // TODO must do something similar for angular date axes.
    if(isAngular(ax) && Math.abs(rng[1] - rng[0]) === 360) {
        vals.pop();
    }

    // save the last tick as well as first, so we can
    // show the exponent only on the last one
    ax._tmax = vals[vals.length - 1];

    // for showing the rest of a date when the main tick label is only the
    // latter part: ax._prevDateHead holds what we showed most recently.
    // Start with it cleared and mark that we're in calcTicks (ie calculating a
    // whole string of these so we should care what the previous date head was!)
    ax._prevDateHead = '';
    ax._inCalcTicks = true;

    var ticksOut = new Array(vals.length);
    for(var i = 0; i < vals.length; i++) ticksOut[i] = axes.tickText(ax, vals[i]);

    ax._inCalcTicks = false;

    return ticksOut;
};

function arrayTicks(ax) {
    var vals = ax.tickvals;
    var text = ax.ticktext;
    var ticksOut = new Array(vals.length);
    var rng = Lib.simpleMap(ax.range, ax.r2l);
    var r0expanded = rng[0] * 1.0001 - rng[1] * 0.0001;
    var r1expanded = rng[1] * 1.0001 - rng[0] * 0.0001;
    var tickMin = Math.min(r0expanded, r1expanded);
    var tickMax = Math.max(r0expanded, r1expanded);
    var j = 0;

    // without a text array, just format the given values as any other ticks
    // except with more precision to the numbers
    if(!Array.isArray(text)) text = [];

    // make sure showing ticks doesn't accidentally add new categories
    // TODO multicategory, if we allow ticktext / tickvals
    var tickVal2l = ax.type === 'category' ? ax.d2l_noadd : ax.d2l;

    // array ticks on log axes always show the full number
    // (if no explicit ticktext overrides it)
    if(ax.type === 'log' && String(ax.dtick).charAt(0) !== 'L') {
        ax.dtick = 'L' + Math.pow(10, Math.floor(Math.min(ax.range[0], ax.range[1])) - 1);
    }

    for(var i = 0; i < vals.length; i++) {
        var vali = tickVal2l(vals[i]);
        if(vali > tickMin && vali < tickMax) {
            if(text[i] === undefined) ticksOut[j] = axes.tickText(ax, vali);
            else ticksOut[j] = tickTextObj(ax, vali, String(text[i]));
            j++;
        }
    }

    if(j < vals.length) ticksOut.splice(j, vals.length - j);

    return ticksOut;
}

var roundBase10 = [2, 5, 10];
var roundBase24 = [1, 2, 3, 6, 12];
var roundBase60 = [1, 2, 5, 10, 15, 30];
// 2&3 day ticks are weird, but need something btwn 1&7
var roundDays = [1, 2, 3, 7, 14];
// approx. tick positions for log axes, showing all (1) and just 1, 2, 5 (2)
// these don't have to be exact, just close enough to round to the right value
var roundLog1 = [-0.046, 0, 0.301, 0.477, 0.602, 0.699, 0.778, 0.845, 0.903, 0.954, 1];
var roundLog2 = [-0.301, 0, 0.301, 0.699, 1];
// N.B. `thetaunit; 'radians' angular axes must be converted to degrees
var roundAngles = [15, 30, 45, 90, 180];

function roundDTick(roughDTick, base, roundingSet) {
    return base * Lib.roundUp(roughDTick / base, roundingSet);
}

// autoTicks: calculate best guess at pleasant ticks for this axis
// inputs:
//      ax - an axis object
//      roughDTick - rough tick spacing (to be turned into a nice round number)
// outputs (into ax):
//   tick0: starting point for ticks (not necessarily on the graph)
//      usually 0 for numeric (=10^0=1 for log) or jan 1, 2000 for dates
//   dtick: the actual, nice round tick spacing, usually a little larger than roughDTick
//      if the ticks are spaced linearly (linear scale, categories,
//          log with only full powers, date ticks < month),
//          this will just be a number
//      months: M#
//      years: M# where # is 12*number of years
//      log with linear ticks: L# where # is the linear tick spacing
//      log showing powers plus some intermediates:
//          D1 shows all digits, D2 shows 2 and 5
axes.autoTicks = function(ax, roughDTick) {
    var base;

    function getBase(v) {
        return Math.pow(v, Math.floor(Math.log(roughDTick) / Math.LN10));
    }

    if(ax.type === 'date') {
        ax.tick0 = Lib.dateTick0(ax.calendar);
        // the criteria below are all based on the rough spacing we calculate
        // being > half of the final unit - so precalculate twice the rough val
        var roughX2 = 2 * roughDTick;

        if(roughX2 > ONEAVGYEAR) {
            roughDTick /= ONEAVGYEAR;
            base = getBase(10);
            ax.dtick = 'M' + (12 * roundDTick(roughDTick, base, roundBase10));
        } else if(roughX2 > ONEAVGMONTH) {
            roughDTick /= ONEAVGMONTH;
            ax.dtick = 'M' + roundDTick(roughDTick, 1, roundBase24);
        } else if(roughX2 > ONEDAY) {
            ax.dtick = roundDTick(roughDTick, ONEDAY, roundDays);
            // get week ticks on sunday
            // this will also move the base tick off 2000-01-01 if dtick is
            // 2 or 3 days... but that's a weird enough case that we'll ignore it.
            ax.tick0 = Lib.dateTick0(ax.calendar, true);
        } else if(roughX2 > ONEHOUR) {
            ax.dtick = roundDTick(roughDTick, ONEHOUR, roundBase24);
        } else if(roughX2 > ONEMIN) {
            ax.dtick = roundDTick(roughDTick, ONEMIN, roundBase60);
        } else if(roughX2 > ONESEC) {
            ax.dtick = roundDTick(roughDTick, ONESEC, roundBase60);
        } else {
            // milliseconds
            base = getBase(10);
            ax.dtick = roundDTick(roughDTick, base, roundBase10);
        }
    } else if(ax.type === 'log') {
        ax.tick0 = 0;
        var rng = Lib.simpleMap(ax.range, ax.r2l);

        if(roughDTick > 0.7) {
            // only show powers of 10
            ax.dtick = Math.ceil(roughDTick);
        } else if(Math.abs(rng[1] - rng[0]) < 1) {
            // span is less than one power of 10
            var nt = 1.5 * Math.abs((rng[1] - rng[0]) / roughDTick);

            // ticks on a linear scale, labeled fully
            roughDTick = Math.abs(Math.pow(10, rng[1]) -
                Math.pow(10, rng[0])) / nt;
            base = getBase(10);
            ax.dtick = 'L' + roundDTick(roughDTick, base, roundBase10);
        } else {
            // include intermediates between powers of 10,
            // labeled with small digits
            // ax.dtick = "D2" (show 2 and 5) or "D1" (show all digits)
            ax.dtick = (roughDTick > 0.3) ? 'D2' : 'D1';
        }
    } else if(ax.type === 'category' || ax.type === 'multicategory') {
        ax.tick0 = 0;
        ax.dtick = Math.ceil(Math.max(roughDTick, 1));
    } else if(isAngular(ax)) {
        ax.tick0 = 0;
        base = 1;
        ax.dtick = roundDTick(roughDTick, base, roundAngles);
    } else {
        // auto ticks always start at 0
        ax.tick0 = 0;
        base = getBase(10);
        ax.dtick = roundDTick(roughDTick, base, roundBase10);
    }

    // prevent infinite loops
    if(ax.dtick === 0) ax.dtick = 1;

    // TODO: this is from log axis histograms with autorange off
    if(!isNumeric(ax.dtick) && typeof ax.dtick !== 'string') {
        var olddtick = ax.dtick;
        ax.dtick = 1;
        throw 'ax.dtick error: ' + String(olddtick);
    }
};

// after dtick is already known, find tickround = precision
// to display in tick labels
//   for numeric ticks, integer # digits after . to round to
//   for date ticks, the last date part to show (y,m,d,H,M,S)
//      or an integer # digits past seconds
function autoTickRound(ax) {
    var dtick = ax.dtick;

    ax._tickexponent = 0;
    if(!isNumeric(dtick) && typeof dtick !== 'string') {
        dtick = 1;
    }

    if(ax.type === 'category' || ax.type === 'multicategory') {
        ax._tickround = null;
    }
    if(ax.type === 'date') {
        // If tick0 is unusual, give tickround a bit more information
        // not necessarily *all* the information in tick0 though, if it's really odd
        // minimal string length for tick0: 'd' is 10, 'M' is 16, 'S' is 19
        // take off a leading minus (year < 0) and i (intercalary month) so length is consistent
        var tick0ms = ax.r2l(ax.tick0);
        var tick0str = ax.l2r(tick0ms).replace(/(^-|i)/g, '');
        var tick0len = tick0str.length;

        if(String(dtick).charAt(0) === 'M') {
            // any tick0 more specific than a year: alway show the full date
            if(tick0len > 10 || tick0str.substr(5) !== '01-01') ax._tickround = 'd';
            // show the month unless ticks are full multiples of a year
            else ax._tickround = (+(dtick.substr(1)) % 12 === 0) ? 'y' : 'm';
        } else if((dtick >= ONEDAY && tick0len <= 10) || (dtick >= ONEDAY * 15)) ax._tickround = 'd';
        else if((dtick >= ONEMIN && tick0len <= 16) || (dtick >= ONEHOUR)) ax._tickround = 'M';
        else if((dtick >= ONESEC && tick0len <= 19) || (dtick >= ONEMIN)) ax._tickround = 'S';
        else {
            // tickround is a number of digits of fractional seconds
            // of any two adjacent ticks, at least one will have the maximum fractional digits
            // of all possible ticks - so take the max. length of tick0 and the next one
            var tick1len = ax.l2r(tick0ms + dtick).replace(/^-/, '').length;
            ax._tickround = Math.max(tick0len, tick1len) - 20;

            // We shouldn't get here... but in case there's a situation I'm
            // not thinking of where tick0str and tick1str are identical or
            // something, fall back on maximum precision
            if(ax._tickround < 0) ax._tickround = 4;
        }
    } else if(isNumeric(dtick) || dtick.charAt(0) === 'L') {
        // linear or log (except D1, D2)
        var rng = ax.range.map(ax.r2d || Number);
        if(!isNumeric(dtick)) dtick = Number(dtick.substr(1));
        // 2 digits past largest digit of dtick
        ax._tickround = 2 - Math.floor(Math.log(dtick) / Math.LN10 + 0.01);

        var maxend = Math.max(Math.abs(rng[0]), Math.abs(rng[1]));

        var rangeexp = Math.floor(Math.log(maxend) / Math.LN10 + 0.01);
        if(Math.abs(rangeexp) > 3) {
            if(isSIFormat(ax.exponentformat) && !beyondSI(rangeexp)) {
                ax._tickexponent = 3 * Math.round((rangeexp - 1) / 3);
            } else ax._tickexponent = rangeexp;
        }
    } else {
        // D1 or D2 (log)
        ax._tickround = null;
    }
}

// months and years don't have constant millisecond values
// (but a year is always 12 months so we only need months)
// log-scale ticks are also not consistently spaced, except
// for pure powers of 10
// numeric ticks always have constant differences, other datetime ticks
// can all be calculated as constant number of milliseconds
axes.tickIncrement = function(x, dtick, axrev, calendar) {
    var axSign = axrev ? -1 : 1;

    // includes linear, all dates smaller than month, and pure 10^n in log
    if(isNumeric(dtick)) return x + axSign * dtick;

    // everything else is a string, one character plus a number
    var tType = dtick.charAt(0);
    var dtSigned = axSign * Number(dtick.substr(1));

    // Dates: months (or years - see Lib.incrementMonth)
    if(tType === 'M') return Lib.incrementMonth(x, dtSigned, calendar);

    // Log scales: Linear, Digits
    else if(tType === 'L') return Math.log(Math.pow(10, x) + dtSigned) / Math.LN10;

    // log10 of 2,5,10, or all digits (logs just have to be
    // close enough to round)
    else if(tType === 'D') {
        var tickset = (dtick === 'D2') ? roundLog2 : roundLog1;
        var x2 = x + axSign * 0.01;
        var frac = Lib.roundUp(Lib.mod(x2, 1), tickset, axrev);

        return Math.floor(x2) +
            Math.log(d3.round(Math.pow(10, frac), 1)) / Math.LN10;
    } else throw 'unrecognized dtick ' + String(dtick);
};

// calculate the first tick on an axis
axes.tickFirst = function(ax) {
    var r2l = ax.r2l || Number;
    var rng = Lib.simpleMap(ax.range, r2l);
    var axrev = rng[1] < rng[0];
    var sRound = axrev ? Math.floor : Math.ceil;
    // add a tiny extra bit to make sure we get ticks
    // that may have been rounded out
    var r0 = rng[0] * 1.0001 - rng[1] * 0.0001;
    var dtick = ax.dtick;
    var tick0 = r2l(ax.tick0);

    if(isNumeric(dtick)) {
        var tmin = sRound((r0 - tick0) / dtick) * dtick + tick0;

        // make sure no ticks outside the category list
        if(ax.type === 'category' || ax.type === 'multicategory') {
            tmin = Lib.constrain(tmin, 0, ax._categories.length - 1);
        }
        return tmin;
    }

    var tType = dtick.charAt(0);
    var dtNum = Number(dtick.substr(1));

    // Dates: months (or years)
    if(tType === 'M') {
        var cnt = 0;
        var t0 = tick0;
        var t1, mult, newDTick;

        // This algorithm should work for *any* nonlinear (but close to linear!)
        // tick spacing. Limit to 10 iterations, for gregorian months it's normally <=3.
        while(cnt < 10) {
            t1 = axes.tickIncrement(t0, dtick, axrev, ax.calendar);
            if((t1 - r0) * (t0 - r0) <= 0) {
                // t1 and t0 are on opposite sides of r0! we've succeeded!
                if(axrev) return Math.min(t0, t1);
                return Math.max(t0, t1);
            }
            mult = (r0 - ((t0 + t1) / 2)) / (t1 - t0);
            newDTick = tType + ((Math.abs(Math.round(mult)) || 1) * dtNum);
            t0 = axes.tickIncrement(t0, newDTick, mult < 0 ? !axrev : axrev, ax.calendar);
            cnt++;
        }
        Lib.error('tickFirst did not converge', ax);
        return t0;
    } else if(tType === 'L') {
        // Log scales: Linear, Digits

        return Math.log(sRound(
            (Math.pow(10, r0) - tick0) / dtNum) * dtNum + tick0) / Math.LN10;
    } else if(tType === 'D') {
        var tickset = (dtick === 'D2') ? roundLog2 : roundLog1;
        var frac = Lib.roundUp(Lib.mod(r0, 1), tickset, axrev);

        return Math.floor(r0) +
            Math.log(d3.round(Math.pow(10, frac), 1)) / Math.LN10;
    } else throw 'unrecognized dtick ' + String(dtick);
};

// draw the text for one tick.
// px,py are the location on gd.paper
// prefix is there so the x axis ticks can be dropped a line
// ax is the axis layout, x is the tick value
// hover is a (truthy) flag for whether to show numbers with a bit
// more precision for hovertext
axes.tickText = function(ax, x, hover) {
    var out = tickTextObj(ax, x);
    var arrayMode = ax.tickmode === 'array';
    var extraPrecision = hover || arrayMode;
    var axType = ax.type;
    // TODO multicategory, if we allow ticktext / tickvals
    var tickVal2l = axType === 'category' ? ax.d2l_noadd : ax.d2l;
    var i;

    if(arrayMode && Array.isArray(ax.ticktext)) {
        var rng = Lib.simpleMap(ax.range, ax.r2l);
        var minDiff = Math.abs(rng[1] - rng[0]) / 10000;

        for(i = 0; i < ax.ticktext.length; i++) {
            if(Math.abs(x - tickVal2l(ax.tickvals[i])) < minDiff) break;
        }
        if(i < ax.ticktext.length) {
            out.text = String(ax.ticktext[i]);
            return out;
        }
    }

    function isHidden(showAttr) {
        if(showAttr === undefined) return true;
        if(hover) return showAttr === 'none';

        var firstOrLast = {
            first: ax._tmin,
            last: ax._tmax
        }[showAttr];

        return showAttr !== 'all' && x !== firstOrLast;
    }

    var hideexp = hover ?
        'never' :
        ax.exponentformat !== 'none' && isHidden(ax.showexponent) ? 'hide' : '';

    if(axType === 'date') formatDate(ax, out, hover, extraPrecision);
    else if(axType === 'log') formatLog(ax, out, hover, extraPrecision, hideexp);
    else if(axType === 'category') formatCategory(ax, out);
    else if(axType === 'multicategory') formatMultiCategory(ax, out, hover);
    else if(isAngular(ax)) formatAngle(ax, out, hover, extraPrecision, hideexp);
    else formatLinear(ax, out, hover, extraPrecision, hideexp);

    // add prefix and suffix
    if(ax.tickprefix && !isHidden(ax.showtickprefix)) out.text = ax.tickprefix + out.text;
    if(ax.ticksuffix && !isHidden(ax.showticksuffix)) out.text += ax.ticksuffix;

    // Setup ticks and grid lines boundaries
    // at 1/2 a 'category' to the left/bottom
    if(ax.tickson === 'boundaries' || ax.showdividers) {
        var inbounds = function(v) {
            var p = ax.l2p(v);
            return p >= 0 && p <= ax._length ? v : null;
        };

        out.xbnd = [
            inbounds(out.x - 0.5),
            inbounds(out.x + ax.dtick - 0.5)
        ];
    }

    return out;
};

/**
 * create text for a hover label on this axis, with special handling of
 * log axes (where negative values can't be displayed but can appear in hover text)
 *
 * @param {object} ax: the axis to format text for
 * @param {number} val: calcdata value to format
 * @param {Optional(number)} val2: a second value to display
 *
 * @returns {string} `val` formatted as a string appropriate to this axis, or
 *     `val` and `val2` as a range (ie '<val> - <val2>') if `val2` is provided and
 *     it's different from `val`.
 */
axes.hoverLabelText = function(ax, val, val2) {
    if(val2 !== BADNUM && val2 !== val) {
        return axes.hoverLabelText(ax, val) + ' - ' + axes.hoverLabelText(ax, val2);
    }

    var logOffScale = (ax.type === 'log' && val <= 0);
    var tx = axes.tickText(ax, ax.c2l(logOffScale ? -val : val), 'hover').text;

    if(logOffScale) {
        return val === 0 ? '0' : MINUS_SIGN + tx;
    }

    // TODO: should we do something special if the axis calendar and
    // the data calendar are different? Somehow display both dates with
    // their system names? Right now it will just display in the axis calendar
    // but users could add the other one as text.
    return tx;
};

function tickTextObj(ax, x, text) {
    var tf = ax.tickfont || {};

    return {
        x: x,
        dx: 0,
        dy: 0,
        text: text || '',
        fontSize: tf.size,
        font: tf.family,
        fontColor: tf.color
    };
}

function formatDate(ax, out, hover, extraPrecision) {
    var tr = ax._tickround;
    var fmt = (hover && ax.hoverformat) || axes.getTickFormat(ax);

    if(extraPrecision) {
        // second or sub-second precision: extra always shows max digits.
        // for other fields, extra precision just adds one field.
        if(isNumeric(tr)) tr = 4;
        else tr = {y: 'm', m: 'd', d: 'M', M: 'S', S: 4}[tr];
    }

    var dateStr = Lib.formatDate(out.x, fmt, tr, ax._dateFormat, ax.calendar, ax._extraFormat);
    var headStr;

    var splitIndex = dateStr.indexOf('\n');
    if(splitIndex !== -1) {
        headStr = dateStr.substr(splitIndex + 1);
        dateStr = dateStr.substr(0, splitIndex);
    }

    if(extraPrecision) {
        // if extraPrecision led to trailing zeros, strip them off
        // actually, this can lead to removing even more zeros than
        // in the original rounding, but that's fine because in these
        // contexts uniformity is not so important (if there's even
        // anything to be uniform with!)

        // can we remove the whole time part?
        if(dateStr === '00:00:00' || dateStr === '00:00') {
            dateStr = headStr;
            headStr = '';
        } else if(dateStr.length === 8) {
            // strip off seconds if they're zero (zero fractional seconds
            // are already omitted)
            // but we never remove minutes and leave just hours
            dateStr = dateStr.replace(/:00$/, '');
        }
    }

    if(headStr) {
        if(hover) {
            // hover puts it all on one line, so headPart works best up front
            // except for year headPart: turn this into "Jan 1, 2000" etc.
            if(tr === 'd') dateStr += ', ' + headStr;
            else dateStr = headStr + (dateStr ? ', ' + dateStr : '');
        } else if(!ax._inCalcTicks || (headStr !== ax._prevDateHead)) {
            dateStr += '<br>' + headStr;
            ax._prevDateHead = headStr;
        }
    }

    out.text = dateStr;
}

function formatLog(ax, out, hover, extraPrecision, hideexp) {
    var dtick = ax.dtick;
    var x = out.x;
    var tickformat = ax.tickformat;
    var dtChar0 = typeof dtick === 'string' && dtick.charAt(0);

    if(hideexp === 'never') {
        // If this is a hover label, then we must *never* hide the exponent
        // for the sake of display, which could give the wrong value by
        // potentially many orders of magnitude. If hideexp was 'never', then
        // it's now succeeded by preventing the other condition from automating
        // this choice. Thus we can unset it so that the axis formatting takes
        // precedence.
        hideexp = '';
    }

    if(extraPrecision && (dtChar0 !== 'L')) {
        dtick = 'L3';
        dtChar0 = 'L';
    }

    if(tickformat || (dtChar0 === 'L')) {
        out.text = numFormat(Math.pow(10, x), ax, hideexp, extraPrecision);
    } else if(isNumeric(dtick) || ((dtChar0 === 'D') && (Lib.mod(x + 0.01, 1) < 0.1))) {
        var p = Math.round(x);
        var absP = Math.abs(p);
        var exponentFormat = ax.exponentformat;
        if(exponentFormat === 'power' || (isSIFormat(exponentFormat) && beyondSI(p))) {
            if(p === 0) out.text = 1;
            else if(p === 1) out.text = '10';
            else out.text = '10<sup>' + (p > 1 ? '' : MINUS_SIGN) + absP + '</sup>';

            out.fontSize *= 1.25;
        } else if((exponentFormat === 'e' || exponentFormat === 'E') && absP > 2) {
            out.text = '1' + exponentFormat + (p > 0 ? '+' : MINUS_SIGN) + absP;
        } else {
            out.text = numFormat(Math.pow(10, x), ax, '', 'fakehover');
            if(dtick === 'D1' && ax._id.charAt(0) === 'y') {
                out.dy -= out.fontSize / 6;
            }
        }
    } else if(dtChar0 === 'D') {
        out.text = String(Math.round(Math.pow(10, Lib.mod(x, 1))));
        out.fontSize *= 0.75;
    } else throw 'unrecognized dtick ' + String(dtick);

    // if 9's are printed on log scale, move the 10's away a bit
    if(ax.dtick === 'D1') {
        var firstChar = String(out.text).charAt(0);
        if(firstChar === '0' || firstChar === '1') {
            if(ax._id.charAt(0) === 'y') {
                out.dx -= out.fontSize / 4;
            } else {
                out.dy += out.fontSize / 2;
                out.dx += (ax.range[1] > ax.range[0] ? 1 : -1) *
                    out.fontSize * (x < 0 ? 0.5 : 0.25);
            }
        }
    }
}

function formatCategory(ax, out) {
    var tt = ax._categories[Math.round(out.x)];
    if(tt === undefined) tt = '';
    out.text = String(tt);
}

function formatMultiCategory(ax, out, hover) {
    var v = Math.round(out.x);
    var cats = ax._categories[v] || [];
    var tt = cats[1] === undefined ? '' : String(cats[1]);
    var tt2 = cats[0] === undefined ? '' : String(cats[0]);

    if(hover) {
        // TODO is this what we want?
        out.text = tt2 + ' - ' + tt;
    } else {
        // setup for secondary labels
        out.text = tt;
        out.text2 = tt2;
    }
}

function formatLinear(ax, out, hover, extraPrecision, hideexp) {
    if(hideexp === 'never') {
        // If this is a hover label, then we must *never* hide the exponent
        // for the sake of display, which could give the wrong value by
        // potentially many orders of magnitude. If hideexp was 'never', then
        // it's now succeeded by preventing the other condition from automating
        // this choice. Thus we can unset it so that the axis formatting takes
        // precedence.
        hideexp = '';
    } else if(ax.showexponent === 'all' && Math.abs(out.x / ax.dtick) < 1e-6) {
        // don't add an exponent to zero if we're showing all exponents
        // so the only reason you'd show an exponent on zero is if it's the
        // ONLY tick to get an exponent (first or last)
        hideexp = 'hide';
    }
    out.text = numFormat(out.x, ax, hideexp, extraPrecision);
}

function formatAngle(ax, out, hover, extraPrecision, hideexp) {
    if(ax.thetaunit === 'radians' && !hover) {
        var num = out.x / 180;

        if(num === 0) {
            out.text = '0';
        } else {
            var frac = num2frac(num);

            if(frac[1] >= 100) {
                out.text = numFormat(Lib.deg2rad(out.x), ax, hideexp, extraPrecision);
            } else {
                var isNeg = out.x < 0;

                if(frac[1] === 1) {
                    if(frac[0] === 1) out.text = 'π';
                    else out.text = frac[0] + 'π';
                } else {
                    out.text = [
                        '<sup>', frac[0], '</sup>',
                        '⁄',
                        '<sub>', frac[1], '</sub>',
                        'π'
                    ].join('');
                }

                if(isNeg) out.text = MINUS_SIGN + out.text;
            }
        }
    } else {
        out.text = numFormat(out.x, ax, hideexp, extraPrecision);
    }
}

// inspired by
// https://github.com/yisibl/num2fraction/blob/master/index.js
function num2frac(num) {
    function almostEq(a, b) {
        return Math.abs(a - b) <= 1e-6;
    }

    function findGCD(a, b) {
        return almostEq(b, 0) ? a : findGCD(b, a % b);
    }

    function findPrecision(n) {
        var e = 1;
        while(!almostEq(Math.round(n * e) / e, n)) {
            e *= 10;
        }
        return e;
    }

    var precision = findPrecision(num);
    var number = num * precision;
    var gcd = Math.abs(findGCD(number, precision));

    return [
        // numerator
        Math.round(number / gcd),
        // denominator
        Math.round(precision / gcd)
    ];
}

// format a number (tick value) according to the axis settings
// new, more reliable procedure than d3.round or similar:
// add half the rounding increment, then stringify and truncate
// also automatically switch to sci. notation
var SIPREFIXES = ['f', 'p', 'n', 'μ', 'm', '', 'k', 'M', 'G', 'T'];

function isSIFormat(exponentFormat) {
    return exponentFormat === 'SI' || exponentFormat === 'B';
}

// are we beyond the range of common SI prefixes?
// 10^-16 -> 1x10^-16
// 10^-15 -> 1f
// ...
// 10^14 -> 100T
// 10^15 -> 1x10^15
// 10^16 -> 1x10^16
function beyondSI(exponent) {
    return exponent > 14 || exponent < -15;
}

function numFormat(v, ax, fmtoverride, hover) {
    var isNeg = v < 0;
    // max number of digits past decimal point to show
    var tickRound = ax._tickround;
    var exponentFormat = fmtoverride || ax.exponentformat || 'B';
    var exponent = ax._tickexponent;
    var tickformat = axes.getTickFormat(ax);
    var separatethousands = ax.separatethousands;

    // special case for hover: set exponent just for this value, and
    // add a couple more digits of precision over tick labels
    if(hover) {
        // make a dummy axis obj to get the auto rounding and exponent
        var ah = {
            exponentformat: exponentFormat,
            dtick: ax.showexponent === 'none' ? ax.dtick :
                (isNumeric(v) ? Math.abs(v) || 1 : 1),
            // if not showing any exponents, don't change the exponent
            // from what we calculate
            range: ax.showexponent === 'none' ? ax.range.map(ax.r2d) : [0, v || 1]
        };
        autoTickRound(ah);
        tickRound = (Number(ah._tickround) || 0) + 4;
        exponent = ah._tickexponent;
        if(ax.hoverformat) tickformat = ax.hoverformat;
    }

    if(tickformat) return ax._numFormat(tickformat)(v).replace(/-/g, MINUS_SIGN);

    // 'epsilon' - rounding increment
    var e = Math.pow(10, -tickRound) / 2;

    // exponentFormat codes:
    // 'e' (1.2e+6, default)
    // 'E' (1.2E+6)
    // 'SI' (1.2M)
    // 'B' (same as SI except 10^9=B not G)
    // 'none' (1200000)
    // 'power' (1.2x10^6)
    // 'hide' (1.2, use 3rd argument=='hide' to eg
    //      only show exponent on last tick)
    if(exponentFormat === 'none') exponent = 0;

    // take the sign out, put it back manually at the end
    // - makes cases easier
    v = Math.abs(v);
    if(v < e) {
        // 0 is just 0, but may get exponent if it's the last tick
        v = '0';
        isNeg = false;
    } else {
        v += e;
        // take out a common exponent, if any
        if(exponent) {
            v *= Math.pow(10, -exponent);
            tickRound += exponent;
        }
        // round the mantissa
        if(tickRound === 0) v = String(Math.floor(v));
        else if(tickRound < 0) {
            v = String(Math.round(v));
            v = v.substr(0, v.length + tickRound);
            for(var i = tickRound; i < 0; i++) v += '0';
        } else {
            v = String(v);
            var dp = v.indexOf('.') + 1;
            if(dp) v = v.substr(0, dp + tickRound).replace(/\.?0+$/, '');
        }
        // insert appropriate decimal point and thousands separator
        v = Lib.numSeparate(v, ax._separators, separatethousands);
    }

    // add exponent
    if(exponent && exponentFormat !== 'hide') {
        if(isSIFormat(exponentFormat) && beyondSI(exponent)) exponentFormat = 'power';

        var signedExponent;
        if(exponent < 0) signedExponent = MINUS_SIGN + -exponent;
        else if(exponentFormat !== 'power') signedExponent = '+' + exponent;
        else signedExponent = String(exponent);

        if(exponentFormat === 'e' || exponentFormat === 'E') {
            v += exponentFormat + signedExponent;
        } else if(exponentFormat === 'power') {
            v += '×10<sup>' + signedExponent + '</sup>';
        } else if(exponentFormat === 'B' && exponent === 9) {
            v += 'B';
        } else if(isSIFormat(exponentFormat)) {
            v += SIPREFIXES[exponent / 3 + 5];
        }
    }

    // put sign back in and return
    // replace standard minus character (which is technically a hyphen)
    // with a true minus sign
    if(isNeg) return MINUS_SIGN + v;
    return v;
}

axes.getTickFormat = function(ax) {
    var i;

    function convertToMs(dtick) {
        return typeof dtick !== 'string' ? dtick : Number(dtick.replace('M', '')) * ONEAVGMONTH;
    }

    function compareLogTicks(left, right) {
        var priority = ['L', 'D'];
        if(typeof left === typeof right) {
            if(typeof left === 'number') {
                return left - right;
            } else {
                var leftPriority = priority.indexOf(left.charAt(0));
                var rightPriority = priority.indexOf(right.charAt(0));
                if(leftPriority === rightPriority) {
                    return Number(left.replace(/(L|D)/g, '')) - Number(right.replace(/(L|D)/g, ''));
                } else {
                    return leftPriority - rightPriority;
                }
            }
        } else {
            return typeof left === 'number' ? 1 : -1;
        }
    }

    function isProperStop(dtick, range, convert) {
        var convertFn = convert || function(x) { return x;};
        var leftDtick = range[0];
        var rightDtick = range[1];
        return ((!leftDtick && typeof leftDtick !== 'number') || convertFn(leftDtick) <= convertFn(dtick)) &&
               ((!rightDtick && typeof rightDtick !== 'number') || convertFn(rightDtick) >= convertFn(dtick));
    }

    function isProperLogStop(dtick, range) {
        var isLeftDtickNull = range[0] === null;
        var isRightDtickNull = range[1] === null;
        var isDtickInRangeLeft = compareLogTicks(dtick, range[0]) >= 0;
        var isDtickInRangeRight = compareLogTicks(dtick, range[1]) <= 0;
        return (isLeftDtickNull || isDtickInRangeLeft) && (isRightDtickNull || isDtickInRangeRight);
    }

    var tickstop, stopi;
    if(ax.tickformatstops && ax.tickformatstops.length > 0) {
        switch(ax.type) {
            case 'date':
            case 'linear': {
                for(i = 0; i < ax.tickformatstops.length; i++) {
                    stopi = ax.tickformatstops[i];
                    if(stopi.enabled && isProperStop(ax.dtick, stopi.dtickrange, convertToMs)) {
                        tickstop = stopi;
                        break;
                    }
                }
                break;
            }
            case 'log': {
                for(i = 0; i < ax.tickformatstops.length; i++) {
                    stopi = ax.tickformatstops[i];
                    if(stopi.enabled && isProperLogStop(ax.dtick, stopi.dtickrange)) {
                        tickstop = stopi;
                        break;
                    }
                }
                break;
            }
            default:
        }
    }
    return tickstop ? tickstop.value : ax.tickformat;
};

// getSubplots - extract all subplot IDs we need
// as an array of items like 'xy', 'x2y', 'x2y2'...
// sorted by x (x,x2,x3...) then y
// optionally restrict to only subplots containing axis object ax
//
// NOTE: this is currently only used OUTSIDE plotly.js (toolpanel, webapp)
// ideally we get rid of it there (or just copy this there) and remove it here
axes.getSubplots = function(gd, ax) {
    var subplotObj = gd._fullLayout._subplots;
    var allSubplots = subplotObj.cartesian.concat(subplotObj.gl2d || []);

    var out = ax ? axes.findSubplotsWithAxis(allSubplots, ax) : allSubplots;

    out.sort(function(a, b) {
        var aParts = a.substr(1).split('y');
        var bParts = b.substr(1).split('y');

        if(aParts[0] === bParts[0]) return +aParts[1] - +bParts[1];
        return +aParts[0] - +bParts[0];
    });

    return out;
};

// find all subplots with axis 'ax'
// NOTE: this is only used in axes.getSubplots (only used outside plotly.js) and
// gl2d/convert (where it restricts axis subplots to only those with gl2d)
axes.findSubplotsWithAxis = function(subplots, ax) {
    var axMatch = new RegExp(
        (ax._id.charAt(0) === 'x') ? ('^' + ax._id + 'y') : (ax._id + '$')
    );
    var subplotsWithAx = [];

    for(var i = 0; i < subplots.length; i++) {
        var sp = subplots[i];
        if(axMatch.test(sp)) subplotsWithAx.push(sp);
    }

    return subplotsWithAx;
};

// makeClipPaths: prepare clipPaths for all single axes and all possible xy pairings
axes.makeClipPaths = function(gd) {
    var fullLayout = gd._fullLayout;

    // for more info: https://github.com/plotly/plotly.js/issues/2595
    if(fullLayout._hasOnlyLargeSploms) return;

    var fullWidth = {_offset: 0, _length: fullLayout.width, _id: ''};
    var fullHeight = {_offset: 0, _length: fullLayout.height, _id: ''};
    var xaList = axes.list(gd, 'x', true);
    var yaList = axes.list(gd, 'y', true);
    var clipList = [];
    var i, j;

    for(i = 0; i < xaList.length; i++) {
        clipList.push({x: xaList[i], y: fullHeight});
        for(j = 0; j < yaList.length; j++) {
            if(i === 0) clipList.push({x: fullWidth, y: yaList[j]});
            clipList.push({x: xaList[i], y: yaList[j]});
        }
    }

    // selectors don't work right with camelCase tags,
    // have to use class instead
    // https://groups.google.com/forum/#!topic/d3-js/6EpAzQ2gU9I
    var axClips = fullLayout._clips.selectAll('.axesclip')
        .data(clipList, function(d) { return d.x._id + d.y._id; });

    axClips.enter().append('clipPath')
        .classed('axesclip', true)
        .attr('id', function(d) { return 'clip' + fullLayout._uid + d.x._id + d.y._id; })
      .append('rect');

    axClips.exit().remove();

    axClips.each(function(d) {
        d3.select(this).select('rect').attr({
            x: d.x._offset || 0,
            y: d.y._offset || 0,
            width: d.x._length || 1,
            height: d.y._length || 1
        });
    });
};

/**
 * Main multi-axis drawing routine!
 *
 * @param {DOM element} gd : graph div
 * @param {string or array of strings} arg : polymorphic argument
 * @param {object} opts:
 * - @param {boolean} skipTitle : optional flag to skip axis title draw/update
 *
 * Signature 1: Axes.draw(gd, 'redraw')
 *   use this to clear and redraw all axes on graph
 *
 * Signature 2: Axes.draw(gd, '')
 *   use this to draw all axes on graph w/o the selectAll().remove()
 *   of the 'redraw' signature
 *
 * Signature 3: Axes.draw(gd, [axId, axId2, ...])
 *   where the items are axis id string,
 *   use this to update multiple axes in one call
 *
 * N.B draw updates:
 * - ax._r (stored range for use by zoom/pan)
 * - ax._rl (stored linearized range for use by zoom/pan)
 */
axes.draw = function(gd, arg, opts) {
    var fullLayout = gd._fullLayout;

    if(arg === 'redraw') {
        fullLayout._paper.selectAll('g.subplot').each(function(d) {
            var id = d[0];
            var plotinfo = fullLayout._plots[id];
            var xa = plotinfo.xaxis;
            var ya = plotinfo.yaxis;

            plotinfo.xaxislayer.selectAll('.' + xa._id + 'tick').remove();
            plotinfo.yaxislayer.selectAll('.' + ya._id + 'tick').remove();
            plotinfo.xaxislayer.selectAll('.' + xa._id + 'tick2').remove();
            plotinfo.yaxislayer.selectAll('.' + ya._id + 'tick2').remove();
            plotinfo.xaxislayer.selectAll('.' + xa._id + 'divider').remove();
            plotinfo.yaxislayer.selectAll('.' + ya._id + 'divider').remove();

            if(plotinfo.gridlayer) plotinfo.gridlayer.selectAll('path').remove();
            if(plotinfo.zerolinelayer) plotinfo.zerolinelayer.selectAll('path').remove();

            fullLayout._infolayer.select('.g-' + xa._id + 'title').remove();
            fullLayout._infolayer.select('.g-' + ya._id + 'title').remove();
        });
    }

    var axList = (!arg || arg === 'redraw') ? axes.listIds(gd) : arg;

    return Lib.syncOrAsync(axList.map(function(axId) {
        return function() {
            if(!axId) return;

            var ax = axes.getFromId(gd, axId);
            var axDone = axes.drawOne(gd, ax, opts);

            ax._r = ax.range.slice();
            ax._rl = Lib.simpleMap(ax._r, ax.r2l);

            return axDone;
        };
    }));
};

/**
 * Draw one cartesian axis
 *
 * @param {DOM element} gd
 * @param {object} ax (full) axis object
 * @param {object} opts
 * - @param {boolean} skipTitle (set to true to skip axis title draw call)
 */
axes.drawOne = function(gd, ax, opts) {
    opts = opts || {};

    var i, sp, plotinfo;

    ax.setScale();

    var fullLayout = gd._fullLayout;
    var axId = ax._id;
    var axLetter = axId.charAt(0);
    var counterLetter = axes.counterLetter(axId);
    var mainSubplot = ax._mainSubplot;
    var mainLinePosition = ax._mainLinePosition;
    var mainMirrorPosition = ax._mainMirrorPosition;
    var mainPlotinfo = fullLayout._plots[mainSubplot];
    var mainAxLayer = mainPlotinfo[axLetter + 'axislayer'];
    var subplotsWithAx = ax._subplotsWith;

    var vals = ax._vals = axes.calcTicks(ax);

    // Add a couple of axis properties that should cause us to recreate
    // elements. Used in d3 data function.
    var axInfo = [ax.mirror, mainLinePosition, mainMirrorPosition].join('_');
    for(i = 0; i < vals.length; i++) {
        vals[i].axInfo = axInfo;
    }

    if(!ax.visible) return;

    // stash selections to avoid DOM queries e.g.
    // - stash tickLabels selection, so that drawTitle can use it to scoot title
    ax._selections = {};
    // stash tick angle (including the computed 'auto' values) per tick-label class
    ax._tickAngles = {};

    var transFn = axes.makeTransFn(ax);
    var tickVals;
    // We remove zero lines, grid lines, and inside ticks if they're within 1px of the end
    // The key case here is removing zero lines when the axis bound is zero
    var valsClipped;

    if(ax.tickson === 'boundaries') {
        var boundaryVals = getBoundaryVals(ax, vals);
        valsClipped = axes.clipEnds(ax, boundaryVals);
        tickVals = ax.ticks === 'inside' ? valsClipped : boundaryVals;
    } else {
        valsClipped = axes.clipEnds(ax, vals);
        tickVals = ax.ticks === 'inside' ? valsClipped : vals;
    }

    var gridVals = ax._gridVals = valsClipped;
    var dividerVals = getDividerVals(ax, vals);

    if(!fullLayout._hasOnlyLargeSploms) {
        // keep track of which subplots (by main conteraxis) we've already
        // drawn grids for, so we don't overdraw overlaying subplots
        var finishedGrids = {};

        for(i = 0; i < subplotsWithAx.length; i++) {
            sp = subplotsWithAx[i];
            plotinfo = fullLayout._plots[sp];

            var counterAxis = plotinfo[counterLetter + 'axis'];
            var mainCounterID = counterAxis._mainAxis._id;
            if(finishedGrids[mainCounterID]) continue;
            finishedGrids[mainCounterID] = 1;

            var gridPath = axLetter === 'x' ?
                'M0,' + counterAxis._offset + 'v' + counterAxis._length :
                'M' + counterAxis._offset + ',0h' + counterAxis._length;

            axes.drawGrid(gd, ax, {
                vals: gridVals,
                counterAxis: counterAxis,
                layer: plotinfo.gridlayer.select('.' + axId),
                path: gridPath,
                transFn: transFn
            });
            axes.drawZeroLine(gd, ax, {
                counterAxis: counterAxis,
                layer: plotinfo.zerolinelayer,
                path: gridPath,
                transFn: transFn
            });
        }
    }

    var tickSigns = axes.getTickSigns(ax);
    var tickSubplots = [];

    if(ax.ticks) {
        var mainTickPath = axes.makeTickPath(ax, mainLinePosition, tickSigns[2]);
        var mirrorTickPath;
        var fullTickPath;
        if(ax._anchorAxis && ax.mirror && ax.mirror !== true) {
            mirrorTickPath = axes.makeTickPath(ax, mainMirrorPosition, tickSigns[3]);
            fullTickPath = mainTickPath + mirrorTickPath;
        } else {
            mirrorTickPath = '';
            fullTickPath = mainTickPath;
        }

        var tickPath;
        if(ax.showdividers && ax.ticks === 'outside' && ax.tickson === 'boundaries') {
            var dividerLookup = {};
            for(i = 0; i < dividerVals.length; i++) {
                dividerLookup[dividerVals[i].x] = 1;
            }
            tickPath = function(d) {
                return dividerLookup[d.x] ? mirrorTickPath : fullTickPath;
            };
        } else {
            tickPath = fullTickPath;
        }

        axes.drawTicks(gd, ax, {
            vals: tickVals,
            layer: mainAxLayer,
            path: tickPath,
            transFn: transFn
        });

        tickSubplots = Object.keys(ax._linepositions || {});
    }

    for(i = 0; i < tickSubplots.length; i++) {
        sp = tickSubplots[i];
        plotinfo = fullLayout._plots[sp];
        // [bottom or left, top or right], free and main are handled above
        var linepositions = ax._linepositions[sp] || [];
        var spTickPath = axes.makeTickPath(ax, linepositions[0], tickSigns[0]) +
            axes.makeTickPath(ax, linepositions[1], tickSigns[1]);

        axes.drawTicks(gd, ax, {
            vals: tickVals,
            layer: plotinfo[axLetter + 'axislayer'],
            path: spTickPath,
            transFn: transFn
        });
    }

    var seq = [];

    // tick labels - for now just the main labels.
    // TODO: mirror labels, esp for subplots

    seq.push(function() {
        return axes.drawLabels(gd, ax, {
            vals: vals,
            layer: mainAxLayer,
            transFn: transFn,
            labelFns: axes.makeLabelFns(ax, mainLinePosition)
        });
    });

    if(ax.type === 'multicategory') {
        var labelLength = 0;
        var pad = {x: 2, y: 10}[axLetter];
        var sgn = tickSigns[2] * (ax.ticks === 'inside' ? -1 : 1);

        seq.push(function() {
            labelLength += getLabelLevelSpan(ax, axId + 'tick') + pad;
            labelLength += ax._tickAngles[axId + 'tick'] ? ax.tickfont.size * LINE_SPACING : 0;

            return axes.drawLabels(gd, ax, {
                vals: getSecondaryLabelVals(ax, vals),
                layer: mainAxLayer,
                cls: axId + 'tick2',
                repositionOnUpdate: true,
                secondary: true,
                transFn: transFn,
                labelFns: axes.makeLabelFns(ax, mainLinePosition + labelLength * sgn)
            });
        });

        seq.push(function() {
            labelLength += getLabelLevelSpan(ax, axId + 'tick2');
            ax._labelLength = labelLength;

            return drawDividers(gd, ax, {
                vals: dividerVals,
                layer: mainAxLayer,
                path: axes.makeTickPath(ax, mainLinePosition, sgn, labelLength),
                transFn: transFn
            });
        });
    }

    function extendRange(range, newRange) {
        range[0] = Math.min(range[0], newRange[0]);
        range[1] = Math.max(range[1], newRange[1]);
    }

    function calcBoundingBox() {
        if(ax.showticklabels) {
            var gdBB = gd.getBoundingClientRect();
            var bBox = mainAxLayer.node().getBoundingClientRect();

            /*
             * the way we're going to use this, the positioning that matters
             * is relative to the origin of gd. This is important particularly
             * if gd is scrollable, and may have been scrolled between the time
             * we calculate this and the time we use it
             */

            ax._boundingBox = {
                width: bBox.width,
                height: bBox.height,
                left: bBox.left - gdBB.left,
                right: bBox.right - gdBB.left,
                top: bBox.top - gdBB.top,
                bottom: bBox.bottom - gdBB.top
            };
        } else {
            var gs = fullLayout._size;
            var pos;

            // set dummy bbox for ticklabel-less axes

            if(axLetter === 'x') {
                pos = ax.anchor === 'free' ?
                    gs.t + gs.h * (1 - ax.position) :
                    gs.t + gs.h * (1 - ax._anchorAxis.domain[{bottom: 0, top: 1}[ax.side]]);

                ax._boundingBox = {
                    top: pos,
                    bottom: pos,
                    left: ax._offset,
                    right: ax._offset + ax._length,
                    width: ax._length,
                    height: 0
                };
            } else {
                pos = ax.anchor === 'free' ?
                    gs.l + gs.w * ax.position :
                    gs.l + gs.w * ax._anchorAxis.domain[{left: 0, right: 1}[ax.side]];

                ax._boundingBox = {
                    left: pos,
                    right: pos,
                    bottom: ax._offset + ax._length,
                    top: ax._offset,
                    height: ax._length,
                    width: 0
                };
            }
        }

        /*
         * for spikelines: what's the full domain of positions in the
         * opposite direction that are associated with this axis?
         * This means any axes that we make a subplot with, plus the
         * position of the axis itself if it's free.
         */
        if(subplotsWithAx) {
            var fullRange = ax._counterSpan = [Infinity, -Infinity];

            for(var i = 0; i < subplotsWithAx.length; i++) {
                var plotinfo = fullLayout._plots[subplotsWithAx[i]];
                var counterAxis = plotinfo[(axLetter === 'x') ? 'yaxis' : 'xaxis'];

                extendRange(fullRange, [
                    counterAxis._offset,
                    counterAxis._offset + counterAxis._length
                ]);
            }

            if(ax.anchor === 'free') {
                extendRange(fullRange, (axLetter === 'x') ?
                    [ax._boundingBox.bottom, ax._boundingBox.top] :
                    [ax._boundingBox.right, ax._boundingBox.left]);
            }
        }
    }

    var hasRangeSlider = Registry.getComponentMethod('rangeslider', 'isVisible')(ax);

    function doAutoMargins() {
        var s = ax.side.charAt(0);
        var push;
        var rangeSliderPush;

        if(hasRangeSlider) {
            rangeSliderPush = Registry.getComponentMethod('rangeslider', 'autoMarginOpts')(gd, ax);
        }
        Plots.autoMargin(gd, rangeSliderAutoMarginID(ax), rangeSliderPush);

        if(ax.automargin && (!hasRangeSlider || s !== 'b')) {
            push = {x: 0, y: 0, r: 0, l: 0, t: 0, b: 0};

            var bbox = ax._boundingBox;
            var titleOffset = getTitleOffset(gd, ax);
            var anchorAxDomainIndex;
            var offset;

            switch(axLetter + s) {
                case 'xb':
                    anchorAxDomainIndex = 0;
                    offset = bbox.top - titleOffset;
                    push[s] = bbox.height;
                    break;
                case 'xt':
                    anchorAxDomainIndex = 1;
                    offset = titleOffset - bbox.bottom;
                    push[s] = bbox.height;
                    break;
                case 'yl':
                    anchorAxDomainIndex = 0;
                    offset = titleOffset - bbox.right;
                    push[s] = bbox.width;
                    break;
                case 'yr':
                    anchorAxDomainIndex = 1;
                    offset = bbox.left - titleOffset;
                    push[s] = bbox.width;
                    break;
            }

            push[counterLetter] = ax.anchor === 'free' ?
                ax.position :
                ax._anchorAxis.domain[anchorAxDomainIndex];

            if(push[s] > 0) {
                push[s] += offset;
            }

            if(ax.title.text !== fullLayout._dfltTitle[axLetter]) {
                push[s] += ax.title.font.size;
            }

            if(axLetter === 'x' && bbox.width > 0) {
                var rExtra = bbox.right - (ax._offset + ax._length);
                if(rExtra > 0) {
                    push.x = 1;
                    push.r = rExtra;
                }
                var lExtra = ax._offset - bbox.left;
                if(lExtra > 0) {
                    push.x = 0;
                    push.l = lExtra;
                }
            } else if(axLetter === 'y' && bbox.height > 0) {
                var bExtra = bbox.bottom - (ax._offset + ax._length);
                if(bExtra > 0) {
                    push.y = 0;
                    push.b = bExtra;
                }
                var tExtra = ax._offset - bbox.top;
                if(tExtra > 0) {
                    push.y = 1;
                    push.t = tExtra;
                }
            }
        }

        Plots.autoMargin(gd, axAutoMarginID(ax), push);
    }

    seq.push(calcBoundingBox, doAutoMargins);

    if(!opts.skipTitle &&
        !(hasRangeSlider && ax._boundingBox && ax.side === 'bottom')
    ) {
        seq.push(function() { return drawTitle(gd, ax); });
    }

    return Lib.syncOrAsync(seq);
};

function getBoundaryVals(ax, vals) {
    var out = [];
    var i;

    // boundaryVals are never used for labels;
    // no need to worry about the other tickTextObj keys
    var _push = function(d, bndIndex) {
        var xb = d.xbnd[bndIndex];
        if(xb !== null) {
            out.push(Lib.extendFlat({}, d, {x: xb}));
        }
    };

    if(vals.length) {
        for(i = 0; i < vals.length; i++) {
            _push(vals[i], 0);
        }
        _push(vals[i - 1], 1);
    }

    return out;
}

function getSecondaryLabelVals(ax, vals) {
    var out = [];
    var lookup = {};

    for(var i = 0; i < vals.length; i++) {
        var d = vals[i];
        if(lookup[d.text2]) {
            lookup[d.text2].push(d.x);
        } else {
            lookup[d.text2] = [d.x];
        }
    }

    for(var k in lookup) {
        out.push(tickTextObj(ax, Lib.interp(lookup[k], 0.5), k));
    }

    return out;
}

function getDividerVals(ax, vals) {
    var out = [];
    var i, current;

    // never used for labels;
    // no need to worry about the other tickTextObj keys
    var _push = function(d, bndIndex) {
        var xb = d.xbnd[bndIndex];
        if(xb !== null) {
            out.push(Lib.extendFlat({}, d, {x: xb}));
        }
    };

    if(ax.showdividers && vals.length) {
        for(i = 0; i < vals.length; i++) {
            var d = vals[i];
            if(d.text2 !== current) {
                _push(d, 0);
            }
            current = d.text2;
        }
        _push(vals[i - 1], 1);
    }

    return out;
}

function getLabelLevelSpan(ax, cls) {
    var axLetter = ax._id.charAt(0);
    var angle = ax._tickAngles[cls] || 0;
    var rad = Lib.deg2rad(angle);
    var sinA = Math.sin(rad);
    var cosA = Math.cos(rad);
    var maxX = 0;
    var maxY = 0;

    // N.B. Drawing.bBox does not take into account rotate transforms

    ax._selections[cls].each(function() {
        var thisLabel = selectTickLabel(this);
        var bb = Drawing.bBox(thisLabel.node());
        var w = bb.width;
        var h = bb.height;
        maxX = Math.max(maxX, cosA * w, sinA * h);
        maxY = Math.max(maxY, sinA * w, cosA * h);
    });

    return {x: maxY, y: maxX}[axLetter];
}

/**
 * Which direction do the 'ax.side' values, and free ticks go?
 *
 * @param {object} ax (full) axis object
 *  - {string} _id (starting with 'x' or 'y')
 *  - {string} side
 *  - {string} ticks
 * @return {array} all entries are either -1 or 1
 *  - [0]: sign for top/right ticks (i.e. negative SVG direction)
 *  - [1]: sign for bottom/left ticks (i.e. positive SVG direction)
 *  - [2]: sign for ticks corresponding to 'ax.side'
 *  - [3]: sign for ticks mirroring 'ax.side'
 */
axes.getTickSigns = function(ax) {
    var axLetter = ax._id.charAt(0);
    var sideOpposite = {x: 'top', y: 'right'}[axLetter];
    var main = ax.side === sideOpposite ? 1 : -1;
    var out = [-1, 1, main, -main];
    // then we flip if outside XOR y axis
    if((ax.ticks !== 'inside') === (axLetter === 'x')) {
        out = out.map(function(v) { return -v; });
    }
    return out;
};

/**
 * Make axis translate transform function
 *
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {number} _offset
 *  - {fn} l2p
 * @return {fn} function of calcTicks items
 */
axes.makeTransFn = function(ax) {
    var axLetter = ax._id.charAt(0);
    var offset = ax._offset;
    return axLetter === 'x' ?
        function(d) { return 'translate(' + (offset + ax.l2p(d.x)) + ',0)'; } :
        function(d) { return 'translate(0,' + (offset + ax.l2p(d.x)) + ')'; };
};

/**
 * Make axis tick path string
 *
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {number} ticklen
 *  - {number} linewidth
 * @param {number} shift along direction of ticklen
 * @param {1 or -1} sng tick sign
 * @param {number (optional)} len tick length
 * @return {string}
 */
axes.makeTickPath = function(ax, shift, sgn, len) {
    len = len !== undefined ? len : ax.ticklen;

    var axLetter = ax._id.charAt(0);
    var pad = (ax.linewidth || 1) / 2;

    return axLetter === 'x' ?
        'M0,' + (shift + pad * sgn) + 'v' + (len * sgn) :
        'M' + (shift + pad * sgn) + ',0h' + (len * sgn);
};

/**
 * Make axis tick label x, y and anchor functions
 *
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {string} ticks
 *  - {number} ticklen
 *  - {string} side
 *  - {number} linewidth
 *  - {number} tickfont.size
 *  - {boolean} showline
 * @param {number} shift
 * @param {number} angle [in degrees] ...
 * @return {object}
 *  - {fn} xFn
 *  - {fn} yFn
 *  - {fn} anchorFn
 *  - {fn} heightFn
 *  - {number} labelStandoff (gap parallel to ticks)
 *  - {number} labelShift (gap perpendicular to ticks)
 */
axes.makeLabelFns = function(ax, shift, angle) {
    var axLetter = ax._id.charAt(0);
    var ticksOnOutsideLabels = ax.tickson !== 'boundaries' && ax.ticks === 'outside';

    var labelStandoff = 0;
    var labelShift = 0;

    if(ticksOnOutsideLabels) {
        labelStandoff += ax.ticklen;
    }
    if(angle && ax.ticks === 'outside') {
        var rad = Lib.deg2rad(angle);
        labelStandoff = ax.ticklen * Math.cos(rad) + 1;
        labelShift = ax.ticklen * Math.sin(rad);
    }
    if(ax.showticklabels && (ticksOnOutsideLabels || ax.showline)) {
        labelStandoff += 0.2 * ax.tickfont.size;
    }
    labelStandoff += (ax.linewidth || 1) / 2;

    var out = {
        labelStandoff: labelStandoff,
        labelShift: labelShift
    };

    var x0, y0, ff, flipIt;

    if(axLetter === 'x') {
        flipIt = ax.side === 'bottom' ? 1 : -1;
        x0 = labelShift * flipIt;
        y0 = shift + labelStandoff * flipIt;
        ff = ax.side === 'bottom' ? 1 : -0.2;

        out.xFn = function(d) { return d.dx + x0; };
        out.yFn = function(d) { return d.dy + y0 + d.fontSize * ff; };
        out.anchorFn = function(d, a) {
            if(!isNumeric(a) || a === 0 || a === 180) {
                return 'middle';
            }
            return (a * flipIt < 0) ? 'end' : 'start';
        };
        out.heightFn = function(d, a, h) {
            return (a < -60 || a > 60) ? -0.5 * h :
                ax.side === 'top' ? -h :
                0;
        };
    } else if(axLetter === 'y') {
        flipIt = ax.side === 'right' ? 1 : -1;
        x0 = labelStandoff;
        y0 = -labelShift * flipIt;
        ff = Math.abs(ax.tickangle) === 90 ? 0.5 : 0;

        out.xFn = function(d) { return d.dx + shift + (x0 + d.fontSize * ff) * flipIt; };
        out.yFn = function(d) { return d.dy + y0 + d.fontSize * MID_SHIFT; };
        out.anchorFn = function(d, a) {
            if(isNumeric(a) && Math.abs(a) === 90) {
                return 'middle';
            }
            return ax.side === 'right' ? 'start' : 'end';
        };
        out.heightFn = function(d, a, h) {
            a *= ax.side === 'left' ? 1 : -1;
            return a < -30 ? -h :
                a < 30 ? -0.5 * h :
                0;
        };
    }

    return out;
};

function tickDataFn(d) {
    return [d.text, d.x, d.axInfo, d.font, d.fontSize, d.fontColor].join('_');
}

/**
 * Draw axis ticks
 *
 * @param {DOM element} gd
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {string} ticks
 *  - {number} linewidth
 *  - {string} tickcolor
 * @param {object} opts
 * - {array of object} vals (calcTicks output-like)
 * - {d3 selection} layer
 * - {string or fn} path
 * - {fn} transFn
 * - {boolean} crisp (set to false to unset crisp-edge SVG rendering)
 */
axes.drawTicks = function(gd, ax, opts) {
    opts = opts || {};

    var cls = ax._id + 'tick';

    var ticks = opts.layer.selectAll('path.' + cls)
        .data(ax.ticks ? opts.vals : [], tickDataFn);

    ticks.exit().remove();

    ticks.enter().append('path')
        .classed(cls, 1)
        .classed('ticks', 1)
        .classed('crisp', opts.crisp !== false)
        .call(Color.stroke, ax.tickcolor)
        .style('stroke-width', Drawing.crispRound(gd, ax.tickwidth, 1) + 'px')
        .attr('d', opts.path);

    ticks.attr('transform', opts.transFn);
};

/**
 * Draw axis grid
 *
 * @param {DOM element} gd
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {boolean} showgrid
 *  - {string} gridcolor
 *  - {string} gridwidth
 *  - {boolean} zeroline
 *  - {string} type
 *  - {string} dtick
 * @param {object} opts
 * - {array of object} vals (calcTicks output-like)
 * - {d3 selection} layer
 * - {object} counterAxis (full axis object corresponding to counter axis)
 *     optional - only required if this axis supports zero lines
 * - {string or fn} path
 * - {fn} transFn
 * - {boolean} crisp (set to false to unset crisp-edge SVG rendering)
 */
axes.drawGrid = function(gd, ax, opts) {
    opts = opts || {};

    var cls = ax._id + 'grid';
    var vals = opts.vals;
    var counterAx = opts.counterAxis;
    if(ax.showgrid === false) {
        vals = [];
    } else if(counterAx && axes.shouldShowZeroLine(gd, ax, counterAx)) {
        var isArrayMode = ax.tickmode === 'array';
        for(var i = 0; i < vals.length; i++) {
            var xi = vals[i].x;
            if(isArrayMode ? !xi : (Math.abs(xi) < ax.dtick / 100)) {
                vals = vals.slice(0, i).concat(vals.slice(i + 1));
                // In array mode you can in principle have multiple
                // ticks at 0, so test them all. Otherwise once we found
                // one we can stop.
                if(isArrayMode) i--;
                else break;
            }
        }
    }

    var grid = opts.layer.selectAll('path.' + cls)
        .data(vals, tickDataFn);

    grid.exit().remove();

    grid.enter().append('path')
        .classed(cls, 1)
        .classed('crisp', opts.crisp !== false);

    ax._gw = Drawing.crispRound(gd, ax.gridwidth, 1);

    grid.attr('transform', opts.transFn)
        .attr('d', opts.path)
        .call(Color.stroke, ax.gridcolor || '#ddd')
        .style('stroke-width', ax._gw + 'px');

    if(typeof opts.path === 'function') grid.attr('d', opts.path);
};

/**
 * Draw axis zero-line
 *
 * @param {DOM element} gd
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {boolean} zeroline
 *  - {number} zerolinewidth
 *  - {string} zerolinecolor
 *  - {number (optional)} _gridWidthCrispRound
 * @param {object} opts
 * - {d3 selection} layer
 * - {object} counterAxis (full axis object corresponding to counter axis)
 * - {string or fn} path
 * - {fn} transFn
 * - {boolean} crisp (set to false to unset crisp-edge SVG rendering)
 */
axes.drawZeroLine = function(gd, ax, opts) {
    opts = opts || opts;

    var cls = ax._id + 'zl';
    var show = axes.shouldShowZeroLine(gd, ax, opts.counterAxis);

    var zl = opts.layer.selectAll('path.' + cls)
        .data(show ? [{x: 0, id: ax._id}] : []);

    zl.exit().remove();

    zl.enter().append('path')
        .classed(cls, 1)
        .classed('zl', 1)
        .classed('crisp', opts.crisp !== false)
        .each(function() {
            // use the fact that only one element can enter to trigger a sort.
            // If several zerolines enter at the same time we will sort once per,
            // but generally this should be a minimal overhead.
            opts.layer.selectAll('path').sort(function(da, db) {
                return axisIds.idSort(da.id, db.id);
            });
        });

    zl.attr('transform', opts.transFn)
        .attr('d', opts.path)
        .call(Color.stroke, ax.zerolinecolor || Color.defaultLine)
        .style('stroke-width', Drawing.crispRound(gd, ax.zerolinewidth, ax._gw || 1) + 'px');
};

/**
 * Draw axis tick labels
 *
 * @param {DOM element} gd
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {boolean} showticklabels
 *  - {number} tickangle
 *  - {object (optional)} _selections
 *  - {object} (optional)} _tickAngles
 * @param {object} opts
 * - {array of object} vals (calcTicks output-like)
 * - {d3 selection} layer
 * - {string (optional)} cls (node className)
 * - {boolean} repositionOnUpdate (set to true to reposition update selection)
 * - {boolean} secondary
 * - {fn} transFn
 * - {object} labelFns
 *  + {fn} xFn
 *  + {fn} yFn
 *  + {fn} anchorFn
 *  + {fn} heightFn
 */
axes.drawLabels = function(gd, ax, opts) {
    opts = opts || {};

    var axId = ax._id;
    var axLetter = axId.charAt(0);
    var cls = opts.cls || axId + 'tick';
    var vals = opts.vals;
    var labelFns = opts.labelFns;
    var tickAngle = opts.secondary ? 0 : ax.tickangle;
    var lastAngle = (ax._tickAngles || {})[cls];

    var tickLabels = opts.layer.selectAll('g.' + cls)
        .data(ax.showticklabels ? vals : [], tickDataFn);

    var labelsReady = [];

    tickLabels.enter().append('g')
        .classed(cls, 1)
        .append('text')
            // only so tex has predictable alignment that we can
            // alter later
            .attr('text-anchor', 'middle')
            .each(function(d) {
                var thisLabel = d3.select(this);
                var newPromise = gd._promises.length;

                thisLabel
                    .call(svgTextUtils.positionText, labelFns.xFn(d), labelFns.yFn(d))
                    .call(Drawing.font, d.font, d.fontSize, d.fontColor)
                    .text(d.text)
                    .call(svgTextUtils.convertToTspans, gd);

                if(gd._promises[newPromise]) {
                    // if we have an async label, we'll deal with that
                    // all here so take it out of gd._promises and
                    // instead position the label and promise this in
                    // labelsReady
                    labelsReady.push(gd._promises.pop().then(function() {
                        positionLabels(thisLabel, tickAngle);
                    }));
                } else {
                    // sync label: just position it now.
                    positionLabels(thisLabel, tickAngle);
                }
            });

    tickLabels.exit().remove();

    if(opts.repositionOnUpdate) {
        tickLabels.each(function(d) {
            d3.select(this).select('text')
                .call(svgTextUtils.positionText, labelFns.xFn(d), labelFns.yFn(d));
        });
    }

    function positionLabels(s, angle) {
        s.each(function(d) {
            var thisLabel = d3.select(this);
            var mathjaxGroup = thisLabel.select('.text-math-group');
            var anchor = labelFns.anchorFn(d, angle);

            var transform = opts.transFn.call(thisLabel.node(), d) +
                ((isNumeric(angle) && +angle !== 0) ?
                (' rotate(' + angle + ',' + labelFns.xFn(d) + ',' +
                    (labelFns.yFn(d) - d.fontSize / 2) + ')') :
                '');

            // how much to shift a multi-line label to center it vertically.
            var nLines = svgTextUtils.lineCount(thisLabel);
            var lineHeight = LINE_SPACING * d.fontSize;
            var anchorHeight = labelFns.heightFn(d, isNumeric(angle) ? +angle : 0, (nLines - 1) * lineHeight);

            if(anchorHeight) {
                transform += ' translate(0, ' + anchorHeight + ')';
            }

            if(mathjaxGroup.empty()) {
                thisLabel.select('text').attr({
                    transform: transform,
                    'text-anchor': anchor
                });
            } else {
                var mjWidth = Drawing.bBox(mathjaxGroup.node()).width;
                var mjShift = mjWidth * {end: -0.5, start: 0.5}[anchor];
                mathjaxGroup.attr('transform', transform + (mjShift ? 'translate(' + mjShift + ',0)' : ''));
            }
        });
    }

    // make sure all labels are correctly positioned at their base angle
    // the positionLabels call above is only for newly drawn labels.
    // do this without waiting, using the last calculated angle to
    // minimize flicker, then do it again when we know all labels are
    // there, putting back the prescribed angle to check for overlaps.
    positionLabels(tickLabels, lastAngle || tickAngle);

    function allLabelsReady() {
        return labelsReady.length && Promise.all(labelsReady);
    }

    function fixLabelOverlaps() {
        positionLabels(tickLabels, tickAngle);

        var autoangle = null;

        // check for auto-angling if x labels overlap
        // don't auto-angle at all for log axes with
        // base and digit format
        if(vals.length && axLetter === 'x' && !isNumeric(tickAngle) &&
            (ax.type !== 'log' || String(ax.dtick).charAt(0) !== 'D')
        ) {
            autoangle = 0;

            var maxFontSize = 0;
            var lbbArray = [];
            var i;

            tickLabels.each(function(d) {
                maxFontSize = Math.max(maxFontSize, d.fontSize);

                var x = ax.l2p(d.x);
                var thisLabel = selectTickLabel(this);
                var bb = Drawing.bBox(thisLabel.node());

                lbbArray.push({
                    // ignore about y, just deal with x overlaps
                    top: 0,
                    bottom: 10,
                    height: 10,
                    left: x - bb.width / 2,
                    // impose a 2px gap
                    right: x + bb.width / 2 + 2,
                    width: bb.width + 2
                });
            });

            if((ax.tickson === 'boundaries' || ax.showdividers) && !opts.secondary) {
                var gap = 2;
                if(ax.ticks) gap += ax.tickwidth / 2;

                // TODO should secondary labels also fall into this fix-overlap regime?

                for(i = 0; i < lbbArray.length; i++) {
                    var xbnd = vals[i].xbnd;
                    var lbb = lbbArray[i];
                    if(
                        (xbnd[0] !== null && (lbb.left - ax.l2p(xbnd[0])) < gap) ||
                        (xbnd[1] !== null && (ax.l2p(xbnd[1]) - lbb.right) < gap)
                    ) {
                        autoangle = 90;
                        break;
                    }
                }
            } else {
                var vLen = vals.length;
                var tickSpacing = Math.abs((vals[vLen - 1].x - vals[0].x) * ax._m) / (vLen - 1);
                var rotate90 = (tickSpacing < maxFontSize * 2.5) || ax.type === 'multicategory';

                // any overlap at all - set 30 degrees or 90 degrees
                for(i = 0; i < lbbArray.length - 1; i++) {
                    if(Lib.bBoxIntersect(lbbArray[i], lbbArray[i + 1])) {
                        autoangle = rotate90 ? 90 : 30;
                        break;
                    }
                }
            }

            if(autoangle) {
                positionLabels(tickLabels, autoangle);
            }
        }

        if(ax._tickAngles) {
            ax._tickAngles[cls] = autoangle === null ?
                (isNumeric(tickAngle) ? tickAngle : 0) :
                autoangle;
        }
    }

    if(ax._selections) {
        ax._selections[cls] = tickLabels;
    }

    var done = Lib.syncOrAsync([allLabelsReady, fixLabelOverlaps]);
    if(done && done.then) gd._promises.push(done);
    return done;
};

/**
 * Draw axis dividers
 *
 * @param {DOM element} gd
 * @param {object} ax (full) axis object
 *  - {string} _id
 *  - {string} showdividers
 *  - {number} dividerwidth
 *  - {string} dividercolor
 * @param {object} opts
 * - {array of object} vals (calcTicks output-like)
 * - {d3 selection} layer
 * - {fn} path
 * - {fn} transFn
 */
function drawDividers(gd, ax, opts) {
    var cls = ax._id + 'divider';
    var vals = opts.vals;

    var dividers = opts.layer.selectAll('path.' + cls)
        .data(vals, tickDataFn);

    dividers.exit().remove();

    dividers.enter().insert('path', ':first-child')
        .classed(cls, 1)
        .classed('crisp', 1)
        .call(Color.stroke, ax.dividercolor)
        .style('stroke-width', Drawing.crispRound(gd, ax.dividerwidth, 1) + 'px');

    dividers
        .attr('transform', opts.transFn)
        .attr('d', opts.path);
}

function getTitleOffset(gd, ax) {
    var gs = gd._fullLayout._size;
    var axLetter = ax._id.charAt(0);
    var side = ax.side;
    var anchorAxis;

    if(ax.anchor !== 'free') {
        anchorAxis = axisIds.getFromId(gd, ax.anchor);
    } else if(axLetter === 'x') {
        anchorAxis = {
            _offset: gs.t + (1 - (ax.position || 0)) * gs.h,
            _length: 0
        };
    } else if(axLetter === 'y') {
        anchorAxis = {
            _offset: gs.l + (ax.position || 0) * gs.w,
            _length: 0
        };
    }

    if(side === 'top' || side === 'left') {
        return anchorAxis._offset;
    } else if(side === 'bottom' || side === 'right') {
        return anchorAxis._offset + anchorAxis._length;
    }
}

function drawTitle(gd, ax) {
    var fullLayout = gd._fullLayout;
    var axId = ax._id;
    var axLetter = axId.charAt(0);
    var fontSize = ax.title.font.size;

    var titleStandoff;
    if(ax.type === 'multicategory') {
        titleStandoff = ax._labelLength;
    } else {
        var offsetBase = 1.5;
        titleStandoff = 10 + fontSize * offsetBase + (ax.linewidth ? ax.linewidth - 1 : 0);
    }

    var titleOffset = getTitleOffset(gd, ax);

    var transform, x, y;

    if(axLetter === 'x') {
        x = ax._offset + ax._length / 2;

        if(ax.side === 'top') {
            y = -titleStandoff - fontSize * (ax.showticklabels ? 1 : 0);
        } else {
            y = titleStandoff + fontSize * (ax.showticklabels ? 1.5 : 0.5);
        }
        y += titleOffset;
    } else {
        y = ax._offset + ax._length / 2;

        if(ax.side === 'right') {
            x = titleStandoff + fontSize * (ax.showticklabels ? 1 : 0.5);
        } else {
            x = -titleStandoff - fontSize * (ax.showticklabels ? 0.5 : 0);
        }
        x += titleOffset;

        transform = {rotate: '-90', offset: 0};
    }

    var avoid;

    if(ax.type !== 'multicategory') {
        var tickLabels = ax._selections[ax._id + 'tick'];

        avoid = {
            selection: tickLabels,
            side: ax.side
        };

        if(tickLabels && tickLabels.node() && tickLabels.node().parentNode) {
            var translation = Drawing.getTranslate(tickLabels.node().parentNode);
            avoid.offsetLeft = translation.x;
            avoid.offsetTop = translation.y;
        }
    }

    return Titles.draw(gd, axId + 'title', {
        propContainer: ax,
        propName: ax._name + '.title.text',
        placeholder: fullLayout._dfltTitle[axLetter],
        avoid: avoid,
        transform: transform,
        attributes: {x: x, y: y, 'text-anchor': 'middle'}
    });
}

axes.shouldShowZeroLine = function(gd, ax, counterAxis) {
    var rng = Lib.simpleMap(ax.range, ax.r2l);
    return (
        (rng[0] * rng[1] <= 0) &&
        ax.zeroline &&
        (ax.type === 'linear' || ax.type === '-') &&
        ax._gridVals.length &&
        (
            clipEnds(ax, 0) ||
            !anyCounterAxLineAtZero(gd, ax, counterAxis, rng) ||
            hasBarsOrFill(gd, ax)
        )
    );
};

axes.clipEnds = function(ax, vals) {
    return vals.filter(function(d) { return clipEnds(ax, d.x); });
};

function clipEnds(ax, l) {
    var p = ax.l2p(l);
    return (p > 1 && p < ax._length - 1);
}

function anyCounterAxLineAtZero(gd, ax, counterAxis, rng) {
    var mainCounterAxis = counterAxis._mainAxis;
    if(!mainCounterAxis) return;

    var fullLayout = gd._fullLayout;
    var axLetter = ax._id.charAt(0);
    var counterLetter = axes.counterLetter(ax._id);

    var zeroPosition = ax._offset + (
        ((Math.abs(rng[0]) < Math.abs(rng[1])) === (axLetter === 'x')) ?
        0 : ax._length
    );

    function lineNearZero(ax2) {
        if(!ax2.showline || !ax2.linewidth) return false;
        var tolerance = Math.max((ax2.linewidth + ax.zerolinewidth) / 2, 1);

        function closeEnough(pos2) {
            return typeof pos2 === 'number' && Math.abs(pos2 - zeroPosition) < tolerance;
        }

        if(closeEnough(ax2._mainLinePosition) || closeEnough(ax2._mainMirrorPosition)) {
            return true;
        }
        var linePositions = ax2._linepositions || {};
        for(var k in linePositions) {
            if(closeEnough(linePositions[k][0]) || closeEnough(linePositions[k][1])) {
                return true;
            }
        }
    }

    var plotinfo = fullLayout._plots[counterAxis._mainSubplot];
    if(!(plotinfo.mainplotinfo || plotinfo).overlays.length) {
        return lineNearZero(counterAxis, zeroPosition);
    }

    var counterLetterAxes = axes.list(gd, counterLetter);
    for(var i = 0; i < counterLetterAxes.length; i++) {
        var counterAxis2 = counterLetterAxes[i];
        if(
            counterAxis2._mainAxis === mainCounterAxis &&
            lineNearZero(counterAxis2, zeroPosition)
        ) {
            return true;
        }
    }
}

function hasBarsOrFill(gd, ax) {
    var fullData = gd._fullData;
    var subplot = ax._mainSubplot;
    var axLetter = ax._id.charAt(0);

    for(var i = 0; i < fullData.length; i++) {
        var trace = fullData[i];

        if(trace.visible === true && (trace.xaxis + trace.yaxis) === subplot) {
            if(
                Registry.traceIs(trace, 'bar-like') &&
                trace.orientation === {x: 'h', y: 'v'}[axLetter]
            ) return true;

            if(
                trace.fill &&
                trace.fill.charAt(trace.fill.length - 1) === axLetter
            ) return true;
        }
    }
    return false;
}

function selectTickLabel(gTick) {
    var s = d3.select(gTick);
    var mj = s.select('.text-math-group');
    return mj.empty() ? s.select('text') : mj;
}

/**
 * Find all margin pushers for 2D axes and reserve them for later use
 * Both label and rangeslider automargin calculations happen later so
 * we need to explicitly allow their ids in order to not delete them.
 *
 * TODO: can we pull the actual automargin calls forward to avoid this hack?
 * We're probably also doing multiple redraws in this case, would be faster
 * if we can just do the whole calculation ahead of time and draw once.
 */
axes.allowAutoMargin = function(gd) {
    var axList = axes.list(gd, '', true);
    for(var i = 0; i < axList.length; i++) {
        var ax = axList[i];
        if(ax.automargin) {
            Plots.allowAutoMargin(gd, axAutoMarginID(ax));
        }
        if(Registry.getComponentMethod('rangeslider', 'isVisible')(ax)) {
            Plots.allowAutoMargin(gd, rangeSliderAutoMarginID(ax));
        }
    }
};

function axAutoMarginID(ax) { return ax._id + '.automargin'; }
function rangeSliderAutoMarginID(ax) { return ax._id + '.rangeslider'; }

// swap all the presentation attributes of the axes showing these traces
axes.swap = function(gd, traces) {
    var axGroups = makeAxisGroups(gd, traces);

    for(var i = 0; i < axGroups.length; i++) {
        swapAxisGroup(gd, axGroups[i].x, axGroups[i].y);
    }
};

function makeAxisGroups(gd, traces) {
    var groups = [];
    var i, j;

    for(i = 0; i < traces.length; i++) {
        var groupsi = [];
        var xi = gd._fullData[traces[i]].xaxis;
        var yi = gd._fullData[traces[i]].yaxis;
        if(!xi || !yi) continue; // not a 2D cartesian trace?

        for(j = 0; j < groups.length; j++) {
            if(groups[j].x.indexOf(xi) !== -1 || groups[j].y.indexOf(yi) !== -1) {
                groupsi.push(j);
            }
        }

        if(!groupsi.length) {
            groups.push({x: [xi], y: [yi]});
            continue;
        }

        var group0 = groups[groupsi[0]];
        var groupj;

        if(groupsi.length > 1) {
            for(j = 1; j < groupsi.length; j++) {
                groupj = groups[groupsi[j]];
                mergeAxisGroups(group0.x, groupj.x);
                mergeAxisGroups(group0.y, groupj.y);
            }
        }
        mergeAxisGroups(group0.x, [xi]);
        mergeAxisGroups(group0.y, [yi]);
    }

    return groups;
}

function mergeAxisGroups(intoSet, fromSet) {
    for(var i = 0; i < fromSet.length; i++) {
        if(intoSet.indexOf(fromSet[i]) === -1) intoSet.push(fromSet[i]);
    }
}

function swapAxisGroup(gd, xIds, yIds) {
    var xFullAxes = [];
    var yFullAxes = [];
    var layout = gd.layout;
    var i, j;

    for(i = 0; i < xIds.length; i++) xFullAxes.push(axes.getFromId(gd, xIds[i]));
    for(i = 0; i < yIds.length; i++) yFullAxes.push(axes.getFromId(gd, yIds[i]));

    var allAxKeys = Object.keys(axAttrs);

    var noSwapAttrs = [
        'anchor', 'domain', 'overlaying', 'position', 'side', 'tickangle', 'editType'
    ];
    var numericTypes = ['linear', 'log'];

    for(i = 0; i < allAxKeys.length; i++) {
        var keyi = allAxKeys[i];
        var xVal = xFullAxes[0][keyi];
        var yVal = yFullAxes[0][keyi];
        var allEqual = true;
        var coerceLinearX = false;
        var coerceLinearY = false;
        if(keyi.charAt(0) === '_' || typeof xVal === 'function' ||
                noSwapAttrs.indexOf(keyi) !== -1) {
            continue;
        }
        for(j = 1; j < xFullAxes.length && allEqual; j++) {
            var xVali = xFullAxes[j][keyi];
            if(keyi === 'type' && numericTypes.indexOf(xVal) !== -1 &&
                    numericTypes.indexOf(xVali) !== -1 && xVal !== xVali) {
                // type is special - if we find a mixture of linear and log,
                // coerce them all to linear on flipping
                coerceLinearX = true;
            } else if(xVali !== xVal) allEqual = false;
        }
        for(j = 1; j < yFullAxes.length && allEqual; j++) {
            var yVali = yFullAxes[j][keyi];
            if(keyi === 'type' && numericTypes.indexOf(yVal) !== -1 &&
                    numericTypes.indexOf(yVali) !== -1 && yVal !== yVali) {
                // type is special - if we find a mixture of linear and log,
                // coerce them all to linear on flipping
                coerceLinearY = true;
            } else if(yFullAxes[j][keyi] !== yVal) allEqual = false;
        }
        if(allEqual) {
            if(coerceLinearX) layout[xFullAxes[0]._name].type = 'linear';
            if(coerceLinearY) layout[yFullAxes[0]._name].type = 'linear';
            swapAxisAttrs(layout, keyi, xFullAxes, yFullAxes, gd._fullLayout._dfltTitle);
        }
    }

    // now swap x&y for any annotations anchored to these x & y
    for(i = 0; i < gd._fullLayout.annotations.length; i++) {
        var ann = gd._fullLayout.annotations[i];
        if(xIds.indexOf(ann.xref) !== -1 &&
                yIds.indexOf(ann.yref) !== -1) {
            Lib.swapAttrs(layout.annotations[i], ['?']);
        }
    }
}

function swapAxisAttrs(layout, key, xFullAxes, yFullAxes, dfltTitle) {
    // in case the value is the default for either axis,
    // look at the first axis in each list and see if
    // this key's value is undefined
    var np = Lib.nestedProperty;
    var xVal = np(layout[xFullAxes[0]._name], key).get();
    var yVal = np(layout[yFullAxes[0]._name], key).get();
    var i;

    if(key === 'title') {
        // special handling of placeholder titles
        if(xVal && xVal.text === dfltTitle.x) {
            xVal.text = dfltTitle.y;
        }
        if(yVal && yVal.text === dfltTitle.y) {
            yVal.text = dfltTitle.x;
        }
    }

    for(i = 0; i < xFullAxes.length; i++) {
        np(layout, xFullAxes[i]._name + '.' + key).set(yVal);
    }
    for(i = 0; i < yFullAxes.length; i++) {
        np(layout, yFullAxes[i]._name + '.' + key).set(xVal);
    }
}

function isAngular(ax) {
    return ax._id === 'angularaxis';
}
