/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');
var Registry = require('../../registry');
var Axes = require('../../plots/cartesian/axes');

var arraysToCalcdata = require('../bar/arrays_to_calcdata');
var binFunctions = require('./bin_functions');
var normFunctions = require('./norm_functions');
var doAvg = require('./average');
var getBinSpanLabelRound = require('./bin_label_vals');

function calc(gd, trace) {
    var pos = [];
    var size = [];
    var pa = Axes.getFromId(gd, trace.orientation === 'h' ? trace.yaxis : trace.xaxis);
    var mainData = trace.orientation === 'h' ? 'y' : 'x';
    var counterData = {x: 'y', y: 'x'}[mainData];
    var calendar = trace[mainData + 'calendar'];
    var cumulativeSpec = trace.cumulative;
    var i;

    var binsAndPos = calcAllAutoBins(gd, trace, pa, mainData);
    var binSpec = binsAndPos[0];
    var pos0 = binsAndPos[1];

    var nonuniformBins = typeof binSpec.size === 'string';
    var binEdges = [];
    var bins = nonuniformBins ? binEdges : binSpec;
    // make the empty bin array
    var inc = [];
    var counts = [];
    var inputPoints = [];
    var total = 0;
    var norm = trace.histnorm;
    var func = trace.histfunc;
    var densityNorm = norm.indexOf('density') !== -1;
    var i2, binEnd, n;

    if(cumulativeSpec.enabled && densityNorm) {
        // we treat "cumulative" like it means "integral" if you use a density norm,
        // which in the end means it's the same as without "density"
        norm = norm.replace(/ ?density$/, '');
        densityNorm = false;
    }

    var extremeFunc = func === 'max' || func === 'min';
    var sizeInit = extremeFunc ? null : 0;
    var binFunc = binFunctions.count;
    var normFunc = normFunctions[norm];
    var isAvg = false;
    var pr2c = function(v) { return pa.r2c(v, 0, calendar); };
    var rawCounterData;

    if(Lib.isArrayOrTypedArray(trace[counterData]) && func !== 'count') {
        rawCounterData = trace[counterData];
        isAvg = func === 'avg';
        binFunc = binFunctions[func];
    }

    // create the bins (and any extra arrays needed)
    // assume more than 1e6 bins is an error, so we don't crash the browser
    i = pr2c(binSpec.start);

    // decrease end a little in case of rounding errors
    binEnd = pr2c(binSpec.end) + (i - Axes.tickIncrement(i, binSpec.size, false, calendar)) / 1e6;

    while(i < binEnd && pos.length < 1e6) {
        i2 = Axes.tickIncrement(i, binSpec.size, false, calendar);
        pos.push((i + i2) / 2);
        size.push(sizeInit);
        inputPoints.push([]);
        // nonuniform bins (like months) we need to search,
        // rather than straight calculate the bin we're in
        binEdges.push(i);
        // nonuniform bins also need nonuniform normalization factors
        if(densityNorm) inc.push(1 / (i2 - i));
        if(isAvg) counts.push(0);
        // break to avoid infinite loops
        if(i2 <= i) break;
        i = i2;
    }
    binEdges.push(i);

    // for date axes we need bin bounds to be calcdata. For nonuniform bins
    // we already have this, but uniform with start/end/size they're still strings.
    if(!nonuniformBins && pa.type === 'date') {
        bins = {
            start: pr2c(bins.start),
            end: pr2c(bins.end),
            size: bins.size
        };
    }

    // bin the data
    // and make histogram-specific pt-number-to-cd-index map object
    var nMax = size.length;
    var uniqueValsPerBin = true;
    var leftGap = Infinity;
    var rightGap = Infinity;
    var ptNumber2cdIndex = {};
    for(i = 0; i < pos0.length; i++) {
        var posi = pos0[i];
        n = Lib.findBin(posi, bins);
        if(n >= 0 && n < nMax) {
            total += binFunc(n, i, size, rawCounterData, counts);
            if(uniqueValsPerBin && inputPoints[n].length && posi !== pos0[inputPoints[n][0]]) {
                uniqueValsPerBin = false;
            }
            inputPoints[n].push(i);
            ptNumber2cdIndex[i] = n;

            leftGap = Math.min(leftGap, posi - binEdges[n]);
            rightGap = Math.min(rightGap, binEdges[n + 1] - posi);
        }
    }

    var roundFn;
    if(!uniqueValsPerBin) {
        roundFn = getBinSpanLabelRound(leftGap, rightGap, binEdges, pa, calendar);
    }

    // average and/or normalize the data, if needed
    if(isAvg) total = doAvg(size, counts);
    if(normFunc) normFunc(size, total, inc);

    // after all normalization etc, now we can accumulate if desired
    if(cumulativeSpec.enabled) cdf(size, cumulativeSpec.direction, cumulativeSpec.currentbin);

    var seriesLen = Math.min(pos.length, size.length);
    var cd = [];
    var firstNonzero = 0;
    var lastNonzero = seriesLen - 1;

    // look for empty bins at the ends to remove, so autoscale omits them
    for(i = 0; i < seriesLen; i++) {
        if(size[i]) {
            firstNonzero = i;
            break;
        }
    }
    for(i = seriesLen - 1; i >= firstNonzero; i--) {
        if(size[i]) {
            lastNonzero = i;
            break;
        }
    }

    // create the "calculated data" to plot
    for(i = firstNonzero; i <= lastNonzero; i++) {
        if((isNumeric(pos[i]) && isNumeric(size[i]))) {
            var cdi = {
                p: pos[i],
                s: size[i],
                b: 0
            };

            // setup hover and event data fields,
            // N.B. pts and "hover" positions ph0/ph1 don't seem to make much sense
            // for cumulative distributions
            if(!cumulativeSpec.enabled) {
                cdi.pts = inputPoints[i];
                if(uniqueValsPerBin) {
                    cdi.ph0 = cdi.ph1 = (inputPoints[i].length) ? pos0[inputPoints[i][0]] : pos[i];
                } else {
                    cdi.ph0 = roundFn(binEdges[i]);
                    cdi.ph1 = roundFn(binEdges[i + 1], true);
                }
            }
            cd.push(cdi);
        }
    }

    if(cd.length === 1) {
        // when we collapse to a single bin, calcdata no longer describes bin size
        // so we need to explicitly specify it
        cd[0].width1 = Axes.tickIncrement(cd[0].p, binSpec.size, false, calendar) - cd[0].p;
    }

    arraysToCalcdata(cd, trace);

    if(Lib.isArrayOrTypedArray(trace.selectedpoints)) {
        Lib.tagSelected(cd, trace, ptNumber2cdIndex);
    }

    return cd;
}

/*
 * calcAllAutoBins: we want all histograms inside the same bingroup
 * (see logic in Histogram.crossTraceDefaults) to share bin specs
 *
 * If the user has explicitly specified differing
 * bin specs, there's nothing we can do, but if possible we will try to use the
 * smallest bins of any of the auto values for all histograms inside the same
 * bingroup.
 */
function calcAllAutoBins(gd, trace, pa, mainData, _overlayEdgeCase) {
    var binAttr = mainData + 'bins';
    var fullLayout = gd._fullLayout;
    var groupName = trace['_' + mainData + 'bingroup'];
    var binOpts = fullLayout._histogramBinOpts[groupName];
    var isOverlay = fullLayout.barmode === 'overlay';
    var i, traces, tracei, calendar, pos0, autoVals, cumulativeSpec;

    var r2c = function(v) { return pa.r2c(v, 0, calendar); };
    var c2r = function(v) { return pa.c2r(v, 0, calendar); };

    var cleanBound = pa.type === 'date' ?
        function(v) { return (v || v === 0) ? Lib.cleanDate(v, null, calendar) : null; } :
        function(v) { return isNumeric(v) ? Number(v) : null; };

    function setBound(attr, bins, newBins) {
        if(bins[attr + 'Found']) {
            bins[attr] = cleanBound(bins[attr]);
            if(bins[attr] === null) bins[attr] = newBins[attr];
        } else {
            autoVals[attr] = bins[attr] = newBins[attr];
            Lib.nestedProperty(traces[0], binAttr + '.' + attr).set(newBins[attr]);
        }
    }

    // all but the first trace in this group has already been marked finished
    // clear this flag, so next time we run calc we will run autobin again
    if(trace['_' + mainData + 'autoBinFinished']) {
        delete trace['_' + mainData + 'autoBinFinished'];
    } else {
        traces = binOpts.traces;
        var allPos = [];

        // Note: we're including `legendonly` traces here for autobin purposes,
        // so that showing & hiding from the legend won't affect bins.
        // But this complicates things a bit since those traces don't `calc`,
        // hence `isFirstVisible`.
        var isFirstVisible = true;
        var has2dMap = false;
        var hasHist2dContour = false;
        for(i = 0; i < traces.length; i++) {
            tracei = traces[i];

            if(tracei.visible) {
                var mainDatai = binOpts.dirs[i];
                pos0 = tracei['_' + mainDatai + 'pos0'] = pa.makeCalcdata(tracei, mainDatai);

                allPos = Lib.concat(allPos, pos0);
                delete tracei['_' + mainData + 'autoBinFinished'];

                if(trace.visible === true) {
                    if(isFirstVisible) {
                        isFirstVisible = false;
                    } else {
                        delete tracei._autoBin;
                        tracei['_' + mainData + 'autoBinFinished'] = 1;
                    }
                    if(Registry.traceIs(tracei, '2dMap')) {
                        has2dMap = true;
                    }
                    if(tracei.type === 'histogram2dcontour') {
                        hasHist2dContour = true;
                    }
                }
            }
        }

        calendar = traces[0][mainData + 'calendar'];
        var newBinSpec = Axes.autoBin(allPos, pa, binOpts.nbins, has2dMap, calendar, binOpts.sizeFound && binOpts.size);

        var autoBin = traces[0]._autoBin = {};
        autoVals = autoBin[binOpts.dirs[0]] = {};

        if(hasHist2dContour) {
            // the "true" 2nd argument reverses the tick direction (which we can't
            // just do with a minus sign because of month bins)
            if(!binOpts.size) {
                newBinSpec.start = c2r(Axes.tickIncrement(
                    r2c(newBinSpec.start), newBinSpec.size, true, calendar));
            }
            if(binOpts.end === undefined) {
                newBinSpec.end = c2r(Axes.tickIncrement(
                    r2c(newBinSpec.end), newBinSpec.size, false, calendar));
            }
        }

        // TODO how does work with bingroup ????
        // - https://github.com/plotly/plotly.js/issues/3881
        //
        // Edge case: single-valued histogram overlaying others
        // Use them all together to calculate the bin size for the single-valued one
        if(isOverlay && !Registry.traceIs(trace, '2dMap') && newBinSpec._dataSpan === 0 &&
            pa.type !== 'category' && pa.type !== 'multicategory') {
            // Several single-valued histograms! Stop infinite recursion,
            // just return an extra flag that tells handleSingleValueOverlays
            // to sort out this trace too
            if(_overlayEdgeCase) return [newBinSpec, pos0, true];

            newBinSpec = handleSingleValueOverlays(gd, trace, pa, mainData, binAttr);
        }

        // adjust for CDF edge cases
        cumulativeSpec = tracei.cumulative || {};
        if(cumulativeSpec.enabled && (cumulativeSpec.currentbin !== 'include')) {
            if(cumulativeSpec.direction === 'decreasing') {
                newBinSpec.start = c2r(Axes.tickIncrement(
                    r2c(newBinSpec.start), newBinSpec.size, true, calendar));
            } else {
                newBinSpec.end = c2r(Axes.tickIncrement(
                    r2c(newBinSpec.end), newBinSpec.size, false, calendar));
            }
        }

        binOpts.size = newBinSpec.size;
        if(!binOpts.sizeFound) {
            autoVals.size = newBinSpec.size;
            Lib.nestedProperty(traces[0], binAttr + '.size').set(newBinSpec.size);
        }

        setBound('start', binOpts, newBinSpec);
        setBound('end', binOpts, newBinSpec);
    }

    pos0 = trace['_' + mainData + 'pos0'];
    delete trace['_' + mainData + 'pos0'];

    // Each trace can specify its own start/end, or if omitted
    // we ensure they're beyond the bounds of this trace's data,
    // and we need to make sure start is aligned with the main start
    var traceInputBins = trace._input[binAttr] || {};
    var traceBinOptsCalc = Lib.extendFlat({}, binOpts);
    var mainStart = binOpts.start;
    var startIn = pa.r2l(traceInputBins.start);
    var hasStart = startIn !== undefined;
    if((binOpts.startFound || hasStart) && startIn !== pa.r2l(mainStart)) {
        // We have an explicit start to reconcile across traces
        // if this trace has an explicit start, shift it down to a bin edge
        // if another trace had an explicit start, shift it down to a
        // bin edge past our data
        var traceStart = hasStart ?
            startIn :
            Lib.aggNums(Math.min, null, pos0);

        var dummyAx = {
            type: (pa.type === 'category' || pa.type === 'multicategory') ? 'linear' : pa.type,
            r2l: pa.r2l,
            dtick: binOpts.size,
            tick0: mainStart,
            calendar: calendar,
            range: ([traceStart, Axes.tickIncrement(traceStart, binOpts.size, false, calendar)]).map(pa.l2r)
        };
        var newStart = Axes.tickFirst(dummyAx);
        if(newStart > pa.r2l(traceStart)) {
            newStart = Axes.tickIncrement(newStart, binOpts.size, true, calendar);
        }
        traceBinOptsCalc.start = pa.l2r(newStart);
        if(!hasStart) Lib.nestedProperty(trace, binAttr + '.start').set(traceBinOptsCalc.start);
    }

    var mainEnd = binOpts.end;
    var endIn = pa.r2l(traceInputBins.end);
    var hasEnd = endIn !== undefined;
    if((binOpts.endFound || hasEnd) && endIn !== pa.r2l(mainEnd)) {
        // Reconciling an explicit end is easier, as it doesn't need to
        // match bin edges
        var traceEnd = hasEnd ?
            endIn :
            Lib.aggNums(Math.max, null, pos0);

        traceBinOptsCalc.end = pa.l2r(traceEnd);
        if(!hasEnd) Lib.nestedProperty(trace, binAttr + '.start').set(traceBinOptsCalc.end);
    }

    // Backward compatibility for one-time autobinning.
    // autobin: true is handled in cleanData, but autobin: false
    // needs to be here where we have determined the values.
    var autoBinAttr = 'autobin' + mainData;
    if(trace._input[autoBinAttr] === false) {
        trace._input[binAttr] = Lib.extendFlat({}, trace[binAttr] || {});
        delete trace._input[autoBinAttr];
        delete trace[autoBinAttr];
    }

    return [traceBinOptsCalc, pos0];
}

/*
 * Adjust single-value histograms in overlay mode to make as good a
 * guess as we can at autobin values the user would like.
 *
 * Returns the binSpec for the trace that sparked all this
 */
function handleSingleValueOverlays(gd, trace, pa, mainData, binAttr) {
    var overlaidTraceGroup = getConnectedHistograms(gd, trace);
    var pastThisTrace = false;
    var minSize = Infinity;
    var singleValuedTraces = [trace];
    var i, tracei;

    // first collect all the:
    // - min bin size from all multi-valued traces
    // - single-valued traces
    for(i = 0; i < overlaidTraceGroup.length; i++) {
        tracei = overlaidTraceGroup[i];
        if(tracei === trace) pastThisTrace = true;
        else if(!pastThisTrace) {
            // This trace has already had its autobins calculated
            // (so must not have been single-valued).
            minSize = Math.min(minSize, tracei[binAttr].size);
        } else {
            var resulti = calcAllAutoBins(gd, tracei, pa, mainData, true);
            var binSpeci = resulti[0];
            var isSingleValued = resulti[2];

            // so we can use this result when we get to tracei in the normal
            // course of events, mark it as done and put _pos0 back
            tracei['_' + mainData + 'autoBinFinished'] = 1;
            tracei['_' + mainData + 'pos0'] = resulti[1];

            if(isSingleValued) {
                singleValuedTraces.push(tracei);
            } else {
                minSize = Math.min(minSize, binSpeci.size);
            }
        }
    }

    // find the real data values for each single-valued trace
    // hunt through pos0 for the first valid value
    var dataVals = new Array(singleValuedTraces.length);
    for(i = 0; i < singleValuedTraces.length; i++) {
        var pos0 = singleValuedTraces[i]['_' + mainData + 'pos0'];
        for(var j = 0; j < pos0.length; j++) {
            if(pos0[j] !== undefined) {
                dataVals[i] = pos0[j];
                break;
            }
        }
    }

    // are ALL traces are single-valued? use the min difference between
    // all of their values (which defaults to 1 if there's still only one)
    if(!isFinite(minSize)) {
        minSize = Lib.distinctVals(dataVals).minDiff;
    }

    // now apply the min size we found to all single-valued traces
    for(i = 0; i < singleValuedTraces.length; i++) {
        tracei = singleValuedTraces[i];
        var calendar = tracei[mainData + 'calendar'];

        tracei._input[binAttr] = tracei[binAttr] = {
            start: pa.c2r(dataVals[i] - minSize / 2, 0, calendar),
            end: pa.c2r(dataVals[i] + minSize / 2, 0, calendar),
            size: minSize
        };
    }

    return trace[binAttr];
}

/*
 * Return an array of histograms that share axes and orientation.
 *
 * Only considers histograms. In principle we could include bars in a
 * similar way to how we do manually binned histograms, though this
 * would have tons of edge cases and value judgments to make.
 */
function getConnectedHistograms(gd, trace) {
    var xid = trace.xaxis;
    var yid = trace.yaxis;
    var orientation = trace.orientation;

    var out = [];
    var fullData = gd._fullData;
    for(var i = 0; i < fullData.length; i++) {
        var tracei = fullData[i];
        if(tracei.type === 'histogram' &&
            tracei.visible === true &&
            tracei.orientation === orientation &&
            tracei.xaxis === xid && tracei.yaxis === yid
        ) {
            out.push(tracei);
        }
    }

    return out;
}

function cdf(size, direction, currentBin) {
    var i, vi, prevSum;

    function firstHalfPoint(i) {
        prevSum = size[i];
        size[i] /= 2;
    }

    function nextHalfPoint(i) {
        vi = size[i];
        size[i] = prevSum + vi / 2;
        prevSum += vi;
    }

    if(currentBin === 'half') {
        if(direction === 'increasing') {
            firstHalfPoint(0);
            for(i = 1; i < size.length; i++) {
                nextHalfPoint(i);
            }
        } else {
            firstHalfPoint(size.length - 1);
            for(i = size.length - 2; i >= 0; i--) {
                nextHalfPoint(i);
            }
        }
    } else if(direction === 'increasing') {
        for(i = 1; i < size.length; i++) {
            size[i] += size[i - 1];
        }

        // 'exclude' is identical to 'include' just shifted one bin over
        if(currentBin === 'exclude') {
            size.unshift(0);
            size.pop();
        }
    } else {
        for(i = size.length - 2; i >= 0; i--) {
            size[i] += size[i + 1];
        }

        if(currentBin === 'exclude') {
            size.push(0);
            size.shift();
        }
    }
}

module.exports = {
    calc: calc,
    calcAllAutoBins: calcAllAutoBins
};
