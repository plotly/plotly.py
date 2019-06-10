/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');

var binFunctions = require('../histogram/bin_functions');
var normFunctions = require('../histogram/norm_functions');
var doAvg = require('../histogram/average');
var getBinSpanLabelRound = require('../histogram/bin_label_vals');
var calcAllAutoBins = require('../histogram/calc').calcAllAutoBins;

module.exports = function calc(gd, trace) {
    var xa = Axes.getFromId(gd, trace.xaxis);
    var ya = Axes.getFromId(gd, trace.yaxis);

    var xcalendar = trace.xcalendar;
    var ycalendar = trace.ycalendar;
    var xr2c = function(v) { return xa.r2c(v, 0, xcalendar); };
    var yr2c = function(v) { return ya.r2c(v, 0, ycalendar); };
    var xc2r = function(v) { return xa.c2r(v, 0, xcalendar); };
    var yc2r = function(v) { return ya.c2r(v, 0, ycalendar); };

    var i, j, n, m;

    // calculate the bins
    var xBinsAndPos = calcAllAutoBins(gd, trace, xa, 'x');
    var xBinSpec = xBinsAndPos[0];
    var xPos0 = xBinsAndPos[1];
    var yBinsAndPos = calcAllAutoBins(gd, trace, ya, 'y');
    var yBinSpec = yBinsAndPos[0];
    var yPos0 = yBinsAndPos[1];

    var serieslen = trace._length;
    if(xPos0.length > serieslen) xPos0.splice(serieslen, xPos0.length - serieslen);
    if(yPos0.length > serieslen) yPos0.splice(serieslen, yPos0.length - serieslen);

    // make the empty bin array & scale the map
    var z = [];
    var onecol = [];
    var zerocol = [];
    var nonuniformBinsX = typeof xBinSpec.size === 'string';
    var nonuniformBinsY = typeof yBinSpec.size === 'string';
    var xEdges = [];
    var yEdges = [];
    var xbins = nonuniformBinsX ? xEdges : xBinSpec;
    var ybins = nonuniformBinsY ? yEdges : yBinSpec;
    var total = 0;
    var counts = [];
    var inputPoints = [];
    var norm = trace.histnorm;
    var func = trace.histfunc;
    var densitynorm = norm.indexOf('density') !== -1;
    var extremefunc = func === 'max' || func === 'min';
    var sizeinit = extremefunc ? null : 0;
    var binfunc = binFunctions.count;
    var normfunc = normFunctions[norm];
    var doavg = false;
    var xinc = [];
    var yinc = [];

    // set a binning function other than count?
    // for binning functions: check first for 'z',
    // then 'mc' in case we had a colored scatter plot
    // and want to transfer these colors to the 2D histo
    // TODO: axe this, make it the responsibility of the app changing type? or an impliedEdit?
    var rawCounterData = ('z' in trace) ?
        trace.z :
        (('marker' in trace && Array.isArray(trace.marker.color)) ?
            trace.marker.color : '');
    if(rawCounterData && func !== 'count') {
        doavg = func === 'avg';
        binfunc = binFunctions[func];
    }

    // decrease end a little in case of rounding errors
    var xBinSize = xBinSpec.size;
    var xBinStart = xr2c(xBinSpec.start);
    var xBinEnd = xr2c(xBinSpec.end) +
        (xBinStart - Axes.tickIncrement(xBinStart, xBinSize, false, xcalendar)) / 1e6;

    for(i = xBinStart; i < xBinEnd; i = Axes.tickIncrement(i, xBinSize, false, xcalendar)) {
        onecol.push(sizeinit);
        xEdges.push(i);
        if(doavg) zerocol.push(0);
    }
    xEdges.push(i);

    var nx = onecol.length;
    var dx = (i - xBinStart) / nx;
    var x0 = xc2r(xBinStart + dx / 2);

    var yBinSize = yBinSpec.size;
    var yBinStart = yr2c(yBinSpec.start);
    var yBinEnd = yr2c(yBinSpec.end) +
        (yBinStart - Axes.tickIncrement(yBinStart, yBinSize, false, ycalendar)) / 1e6;

    for(i = yBinStart; i < yBinEnd; i = Axes.tickIncrement(i, yBinSize, false, ycalendar)) {
        z.push(onecol.slice());
        yEdges.push(i);
        var ipCol = new Array(nx);
        for(j = 0; j < nx; j++) ipCol[j] = [];
        inputPoints.push(ipCol);
        if(doavg) counts.push(zerocol.slice());
    }
    yEdges.push(i);

    var ny = z.length;
    var dy = (i - yBinStart) / ny;
    var y0 = yc2r(yBinStart + dy / 2);

    if(densitynorm) {
        xinc = makeIncrements(onecol.length, xbins, dx, nonuniformBinsX);
        yinc = makeIncrements(z.length, ybins, dy, nonuniformBinsY);
    }

    // for date axes we need bin bounds to be calcdata. For nonuniform bins
    // we already have this, but uniform with start/end/size they're still strings.
    if(!nonuniformBinsX && xa.type === 'date') xbins = binsToCalc(xr2c, xbins);
    if(!nonuniformBinsY && ya.type === 'date') ybins = binsToCalc(yr2c, ybins);

    // put data into bins
    var uniqueValsPerX = true;
    var uniqueValsPerY = true;
    var xVals = new Array(nx);
    var yVals = new Array(ny);
    var xGapLow = Infinity;
    var xGapHigh = Infinity;
    var yGapLow = Infinity;
    var yGapHigh = Infinity;
    for(i = 0; i < serieslen; i++) {
        var xi = xPos0[i];
        var yi = yPos0[i];
        n = Lib.findBin(xi, xbins);
        m = Lib.findBin(yi, ybins);
        if(n >= 0 && n < nx && m >= 0 && m < ny) {
            total += binfunc(n, i, z[m], rawCounterData, counts[m]);
            inputPoints[m][n].push(i);

            if(uniqueValsPerX) {
                if(xVals[n] === undefined) xVals[n] = xi;
                else if(xVals[n] !== xi) uniqueValsPerX = false;
            }
            if(uniqueValsPerY) {
                if(yVals[m] === undefined) yVals[m] = yi;
                else if(yVals[m] !== yi) uniqueValsPerY = false;
            }

            xGapLow = Math.min(xGapLow, xi - xEdges[n]);
            xGapHigh = Math.min(xGapHigh, xEdges[n + 1] - xi);
            yGapLow = Math.min(yGapLow, yi - yEdges[m]);
            yGapHigh = Math.min(yGapHigh, yEdges[m + 1] - yi);
        }
    }
    // normalize, if needed
    if(doavg) {
        for(m = 0; m < ny; m++) total += doAvg(z[m], counts[m]);
    }
    if(normfunc) {
        for(m = 0; m < ny; m++) normfunc(z[m], total, xinc, yinc[m]);
    }

    return {
        x: xPos0,
        xRanges: getRanges(xEdges, uniqueValsPerX && xVals, xGapLow, xGapHigh, xa, xcalendar),
        x0: x0,
        dx: dx,
        y: yPos0,
        yRanges: getRanges(yEdges, uniqueValsPerY && yVals, yGapLow, yGapHigh, ya, ycalendar),
        y0: y0,
        dy: dy,
        z: z,
        pts: inputPoints
    };
};

function makeIncrements(len, bins, dv, nonuniform) {
    var out = new Array(len);
    var i;
    if(nonuniform) {
        for(i = 0; i < len; i++) out[i] = 1 / (bins[i + 1] - bins[i]);
    } else {
        var inc = 1 / dv;
        for(i = 0; i < len; i++) out[i] = inc;
    }
    return out;
}

function binsToCalc(r2c, bins) {
    return {
        start: r2c(bins.start),
        end: r2c(bins.end),
        size: bins.size
    };
}

function getRanges(edges, uniqueVals, gapLow, gapHigh, ax, calendar) {
    var i;
    var len = edges.length - 1;
    var out = new Array(len);
    var roundFn = getBinSpanLabelRound(gapLow, gapHigh, edges, ax, calendar);

    for(i = 0; i < len; i++) {
        var v = (uniqueVals || [])[i];
        out[i] = v === undefined ?
            [roundFn(edges[i]), roundFn(edges[i + 1], true)] :
            [v, v];
    }
    return out;
}
