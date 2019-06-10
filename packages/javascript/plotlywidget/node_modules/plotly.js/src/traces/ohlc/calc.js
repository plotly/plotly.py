/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var _ = Lib._;
var Axes = require('../../plots/cartesian/axes');
var BADNUM = require('../../constants/numerical').BADNUM;

function calc(gd, trace) {
    var xa = Axes.getFromId(gd, trace.xaxis);
    var ya = Axes.getFromId(gd, trace.yaxis);

    var tickLen = convertTickWidth(gd, xa, trace);
    var minDiff = trace._minDiff;
    trace._minDiff = null;
    var x = trace._xcalc;
    trace._xcalc = null;

    var cd = calcCommon(gd, trace, x, ya, ptFunc);

    trace._extremes[xa._id] = Axes.findExtremes(xa, x, {vpad: minDiff / 2});
    if(cd.length) {
        Lib.extendFlat(cd[0].t, {
            wHover: minDiff / 2,
            tickLen: tickLen
        });
        return cd;
    } else {
        return [{t: {empty: true}}];
    }
}

function ptFunc(o, h, l, c) {
    return {
        o: o,
        h: h,
        l: l,
        c: c
    };
}


// shared between OHLC and candlestick
// ptFunc makes a calcdata point specific to each trace type, from oi, hi, li, ci
function calcCommon(gd, trace, x, ya, ptFunc) {
    var o = ya.makeCalcdata(trace, 'open');
    var h = ya.makeCalcdata(trace, 'high');
    var l = ya.makeCalcdata(trace, 'low');
    var c = ya.makeCalcdata(trace, 'close');

    var hasTextArray = Array.isArray(trace.text);
    var hasHovertextArray = Array.isArray(trace.hovertext);

    // we're optimists - before we have any changing data, assume increasing
    var increasing = true;
    var cPrev = null;

    var cd = [];
    for(var i = 0; i < x.length; i++) {
        var xi = x[i];
        var oi = o[i];
        var hi = h[i];
        var li = l[i];
        var ci = c[i];

        if(xi !== BADNUM && oi !== BADNUM && hi !== BADNUM && li !== BADNUM && ci !== BADNUM) {
            if(ci === oi) {
                // if open == close, look for a change from the previous close
                if(cPrev !== null && ci !== cPrev) increasing = ci > cPrev;
                // else (c === cPrev or cPrev is null) no change
            } else increasing = ci > oi;

            cPrev = ci;

            var pt = ptFunc(oi, hi, li, ci);

            pt.pos = xi;
            pt.yc = (oi + ci) / 2;
            pt.i = i;
            pt.dir = increasing ? 'increasing' : 'decreasing';

            // For categoryorder, store low and high
            pt.x = pt.pos;
            pt.y = [li, hi];

            if(hasTextArray) pt.tx = trace.text[i];
            if(hasHovertextArray) pt.htx = trace.hovertext[i];

            cd.push(pt);
        } else {
            cd.push({pos: xi, empty: true});
        }
    }

    trace._extremes[ya._id] = Axes.findExtremes(ya, Lib.concat(l, h), {padded: true});

    if(cd.length) {
        cd[0].t = {
            labels: {
                open: _(gd, 'open:') + ' ',
                high: _(gd, 'high:') + ' ',
                low: _(gd, 'low:') + ' ',
                close: _(gd, 'close:') + ' '
            }
        };
    }

    return cd;
}

/*
 * find min x-coordinates difference of all traces
 * attached to this x-axis and stash the result in _minDiff
 * in all traces; when a trace uses this in its
 * calc step it deletes _minDiff, so that next calc this is
 * done again in case the data changed.
 * also since we need it here, stash _xcalc on the trace
 */
function convertTickWidth(gd, xa, trace) {
    var minDiff = trace._minDiff;

    if(!minDiff) {
        var fullData = gd._fullData;
        var ohlcTracesOnThisXaxis = [];

        minDiff = Infinity;

        var i;

        for(i = 0; i < fullData.length; i++) {
            var tracei = fullData[i];

            if(tracei.type === 'ohlc' &&
                tracei.visible === true &&
                tracei.xaxis === xa._id
            ) {
                ohlcTracesOnThisXaxis.push(tracei);

                var xcalc = xa.makeCalcdata(tracei, 'x');
                tracei._xcalc = xcalc;

                var _minDiff = Lib.distinctVals(xcalc).minDiff;
                if(_minDiff && isFinite(_minDiff)) {
                    minDiff = Math.min(minDiff, _minDiff);
                }
            }
        }

        // if minDiff is still Infinity here, set it to 1
        if(minDiff === Infinity) minDiff = 1;

        for(i = 0; i < ohlcTracesOnThisXaxis.length; i++) {
            ohlcTracesOnThisXaxis[i]._minDiff = minDiff;
        }
    }

    return minDiff * trace.tickwidth;
}

module.exports = {
    calc: calc,
    calcCommon: calcCommon
};
