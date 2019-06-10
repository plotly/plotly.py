/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../plots/cartesian/axes');
var Lib = require('../lib');
var PlotSchema = require('../plot_api/plot_schema');
var pointsAccessorFunction = require('./helpers').pointsAccessorFunction;
var BADNUM = require('../constants/numerical').BADNUM;

exports.moduleType = 'transform';

exports.name = 'aggregate';

var attrs = exports.attributes = {
    enabled: {
        valType: 'boolean',
        dflt: true,
        role: 'info',
        editType: 'calc',
        description: [
            'Determines whether this aggregate transform is enabled or disabled.'
        ].join(' ')
    },
    groups: {
        // TODO: groupby should support string or array grouping this way too
        // currently groupby only allows a grouping array
        valType: 'string',
        strict: true,
        noBlank: true,
        arrayOk: true,
        dflt: 'x',
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the grouping target to which the aggregation is applied.',
            'Data points with matching group values will be coalesced into',
            'one point, using the supplied aggregation functions to reduce data',
            'in other data arrays.',
            'If a string, `groups` is assumed to be a reference to a data array',
            'in the parent trace object.',
            'To aggregate by nested variables, use *.* to access them.',
            'For example, set `groups` to *marker.color* to aggregate',
            'about the marker color array.',
            'If an array, `groups` is itself the data array by which we aggregate.'
        ].join(' ')
    },
    aggregations: {
        _isLinkedToArray: 'aggregation',
        target: {
            valType: 'string',
            role: 'info',
            editType: 'calc',
            description: [
                'A reference to the data array in the parent trace to aggregate.',
                'To aggregate by nested variables, use *.* to access them.',
                'For example, set `groups` to *marker.color* to aggregate',
                'over the marker color array.',
                'The referenced array must already exist, unless `func` is *count*,',
                'and each array may only be referenced once.'
            ].join(' ')
        },
        func: {
            valType: 'enumerated',
            values: ['count', 'sum', 'avg', 'median', 'mode', 'rms', 'stddev', 'min', 'max', 'first', 'last', 'change', 'range'],
            dflt: 'first',
            role: 'info',
            editType: 'calc',
            description: [
                'Sets the aggregation function.',
                'All values from the linked `target`, corresponding to the same value',
                'in the `groups` array, are collected and reduced by this function.',
                '*count* is simply the number of values in the `groups` array, so does',
                'not even require the linked array to exist. *first* (*last*) is just',
                'the first (last) linked value.',
                'Invalid values are ignored, so for example in *avg* they do not',
                'contribute to either the numerator or the denominator.',
                'Any data type (numeric, date, category) may be aggregated with any',
                'function, even though in certain cases it is unlikely to make sense,',
                'for example a sum of dates or average of categories.',
                '*median* will return the average of the two central values if there is',
                'an even count. *mode* will return the first value to reach the maximum',
                'count, in case of a tie.',
                '*change* will return the difference between the first and last linked values.',
                '*range* will return the difference between the min and max linked values.'
            ].join(' ')
        },
        funcmode: {
            valType: 'enumerated',
            values: ['sample', 'population'],
            dflt: 'sample',
            role: 'info',
            editType: 'calc',
            description: [
                '*stddev* supports two formula variants: *sample* (normalize by N-1)',
                'and *population* (normalize by N).'
            ].join(' ')
        },
        enabled: {
            valType: 'boolean',
            dflt: true,
            role: 'info',
            editType: 'calc',
            description: [
                'Determines whether this aggregation function is enabled or disabled.'
            ].join(' ')
        },
        editType: 'calc'
    },
    editType: 'calc'
};

var aggAttrs = attrs.aggregations;

/**
 * Supply transform attributes defaults
 *
 * @param {object} transformIn
 *  object linked to trace.transforms[i] with 'func' set to exports.name
 * @param {object} traceOut
 *  the _fullData trace this transform applies to
 * @param {object} layout
 *  the plot's (not-so-full) layout
 * @param {object} traceIn
 *  the input data trace this transform applies to
 *
 * @return {object} transformOut
 *  copy of transformIn that contains attribute defaults
 */
exports.supplyDefaults = function(transformIn, traceOut) {
    var transformOut = {};
    var i;

    function coerce(attr, dflt) {
        return Lib.coerce(transformIn, transformOut, attrs, attr, dflt);
    }

    var enabled = coerce('enabled');

    if(!enabled) return transformOut;

    /*
     * Normally _arrayAttrs is calculated during doCalc, but that comes later.
     * Anyway this can change due to *count* aggregations (see below) so it's not
     * necessarily the same set.
     *
     * For performance we turn it into an object of truthy values
     * we'll use 1 for arrays we haven't aggregated yet, 0 for finished arrays,
     * as distinct from undefined which means this array isn't present in the input
     * missing arrays can still be aggregate outputs for *count* aggregations.
     */
    var arrayAttrArray = PlotSchema.findArrayAttributes(traceOut);
    var arrayAttrs = {};
    for(i = 0; i < arrayAttrArray.length; i++) arrayAttrs[arrayAttrArray[i]] = 1;

    var groups = coerce('groups');

    if(!Array.isArray(groups)) {
        if(!arrayAttrs[groups]) {
            transformOut.enabled = false;
            return transformOut;
        }
        arrayAttrs[groups] = 0;
    }

    var aggregationsIn = transformIn.aggregations || [];
    var aggregationsOut = transformOut.aggregations = new Array(aggregationsIn.length);
    var aggregationOut;

    function coercei(attr, dflt) {
        return Lib.coerce(aggregationsIn[i], aggregationOut, aggAttrs, attr, dflt);
    }

    for(i = 0; i < aggregationsIn.length; i++) {
        aggregationOut = {_index: i};
        var target = coercei('target');
        var func = coercei('func');
        var enabledi = coercei('enabled');

        // add this aggregation to the output only if it's the first instance
        // of a valid target attribute - or an unused target attribute with "count"
        if(enabledi && target && (arrayAttrs[target] || (func === 'count' && arrayAttrs[target] === undefined))) {
            if(func === 'stddev') coercei('funcmode');

            arrayAttrs[target] = 0;
            aggregationsOut[i] = aggregationOut;
        } else aggregationsOut[i] = {enabled: false, _index: i};
    }

    // any array attributes we haven't yet covered, fill them with the default aggregation
    for(i = 0; i < arrayAttrArray.length; i++) {
        if(arrayAttrs[arrayAttrArray[i]]) {
            aggregationsOut.push({
                target: arrayAttrArray[i],
                func: aggAttrs.func.dflt,
                enabled: true,
                _index: -1
            });
        }
    }

    return transformOut;
};


exports.calcTransform = function(gd, trace, opts) {
    if(!opts.enabled) return;

    var groups = opts.groups;

    var groupArray = Lib.getTargetArray(trace, {target: groups});
    if(!groupArray) return;

    var i, vi, groupIndex, newGrouping;

    var groupIndices = {};
    var indexToPoints = {};
    var groupings = [];

    var originalPointsAccessor = pointsAccessorFunction(trace.transforms, opts);

    var len = groupArray.length;
    if(trace._length) len = Math.min(len, trace._length);

    for(i = 0; i < len; i++) {
        vi = groupArray[i];
        groupIndex = groupIndices[vi];
        if(groupIndex === undefined) {
            groupIndices[vi] = groupings.length;
            newGrouping = [i];
            groupings.push(newGrouping);
            indexToPoints[groupIndices[vi]] = originalPointsAccessor(i);
        } else {
            groupings[groupIndex].push(i);
            indexToPoints[groupIndices[vi]] = (indexToPoints[groupIndices[vi]] || []).concat(originalPointsAccessor(i));
        }
    }

    opts._indexToPoints = indexToPoints;

    var aggregations = opts.aggregations;

    for(i = 0; i < aggregations.length; i++) {
        aggregateOneArray(gd, trace, groupings, aggregations[i]);
    }

    if(typeof groups === 'string') {
        aggregateOneArray(gd, trace, groupings, {
            target: groups,
            func: 'first',
            enabled: true
        });
    }

    trace._length = groupings.length;
};

function aggregateOneArray(gd, trace, groupings, aggregation) {
    if(!aggregation.enabled) return;

    var attr = aggregation.target;
    var targetNP = Lib.nestedProperty(trace, attr);
    var arrayIn = targetNP.get();
    var conversions = Axes.getDataConversions(gd, trace, attr, arrayIn);
    var func = getAggregateFunction(aggregation, conversions);

    var arrayOut = new Array(groupings.length);
    for(var i = 0; i < groupings.length; i++) {
        arrayOut[i] = func(arrayIn, groupings[i]);
    }
    targetNP.set(arrayOut);

    if(aggregation.func === 'count') {
        // count does not depend on an input array, so it's likely not part of _arrayAttrs yet
        // but after this transform it most definitely *is* an array attribute.
        Lib.pushUnique(trace._arrayAttrs, attr);
    }
}

function getAggregateFunction(opts, conversions) {
    var func = opts.func;
    var d2c = conversions.d2c;
    var c2d = conversions.c2d;

    switch(func) {
        // count, first, and last don't depend on anything about the data
        // point back to pure functions for performance
        case 'count':
            return count;
        case 'first':
            return first;
        case 'last':
            return last;

        case 'sum':
            // This will produce output in all cases even though it's nonsensical
            // for date or category data.
            return function(array, indices) {
                var total = 0;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) total += vi;
                }
                return c2d(total);
            };

        case 'avg':
            // Generally meaningless for category data but it still does something.
            return function(array, indices) {
                var total = 0;
                var cnt = 0;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) {
                        total += vi;
                        cnt++;
                    }
                }
                return cnt ? c2d(total / cnt) : BADNUM;
            };

        case 'min':
            return function(array, indices) {
                var out = Infinity;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) out = Math.min(out, vi);
                }
                return (out === Infinity) ? BADNUM : c2d(out);
            };

        case 'max':
            return function(array, indices) {
                var out = -Infinity;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) out = Math.max(out, vi);
                }
                return (out === -Infinity) ? BADNUM : c2d(out);
            };

        case 'range':
            return function(array, indices) {
                var min = Infinity;
                var max = -Infinity;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) {
                        min = Math.min(min, vi);
                        max = Math.max(max, vi);
                    }
                }
                return (max === -Infinity || min === Infinity) ? BADNUM : c2d(max - min);
            };

        case 'change':
            return function(array, indices) {
                var first = d2c(array[indices[0]]);
                var last = d2c(array[indices[indices.length - 1]]);
                return (first === BADNUM || last === BADNUM) ? BADNUM : c2d(last - first);
            };

        case 'median':
            return function(array, indices) {
                var sortCalc = [];
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) sortCalc.push(vi);
                }
                if(!sortCalc.length) return BADNUM;
                sortCalc.sort();
                var mid = (sortCalc.length - 1) / 2;
                return c2d((sortCalc[Math.floor(mid)] + sortCalc[Math.ceil(mid)]) / 2);
            };

        case 'mode':
            return function(array, indices) {
                var counts = {};
                var maxCnt = 0;
                var out = BADNUM;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) {
                        var counti = counts[vi] = (counts[vi] || 0) + 1;
                        if(counti > maxCnt) {
                            maxCnt = counti;
                            out = vi;
                        }
                    }
                }
                return maxCnt ? c2d(out) : BADNUM;
            };

        case 'rms':
            return function(array, indices) {
                var total = 0;
                var cnt = 0;
                for(var i = 0; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) {
                        total += vi * vi;
                        cnt++;
                    }
                }
                return cnt ? c2d(Math.sqrt(total / cnt)) : BADNUM;
            };

        case 'stddev':
            return function(array, indices) {
                // balance numerical stability with performance:
                // so that we call d2c once per element but don't need to
                // store them, reference all to the first element
                var total = 0;
                var total2 = 0;
                var cnt = 1;
                var v0 = BADNUM;
                var i;
                for(i = 0; i < indices.length && v0 === BADNUM; i++) {
                    v0 = d2c(array[indices[i]]);
                }
                if(v0 === BADNUM) return BADNUM;

                for(; i < indices.length; i++) {
                    var vi = d2c(array[indices[i]]);
                    if(vi !== BADNUM) {
                        var dv = vi - v0;
                        total += dv;
                        total2 += dv * dv;
                        cnt++;
                    }
                }

                // This is population std dev, if we want sample std dev
                // we would need (...) / (cnt - 1)
                // Also note there's no c2d here - that means for dates the result
                // is a number of milliseconds, and for categories it's a number
                // of category differences, which is not generically meaningful but
                // as in other cases we don't forbid it.
                var norm = (opts.funcmode === 'sample') ? (cnt - 1) : cnt;
                // this is debatable: should a count of 1 return sample stddev of
                // 0 or undefined?
                if(!norm) return 0;
                return Math.sqrt((total2 - (total * total / cnt)) / norm);
            };
    }
}

function count(array, indices) {
    return indices.length;
}

function first(array, indices) {
    return array[indices[0]];
}

function last(array, indices) {
    return array[indices[indices.length - 1]];
}
