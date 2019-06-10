/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../../plots/cartesian/axes');
var mergeArray = require('../../lib').mergeArray;
var calcSelection = require('../scatter/calc_selection');
var BADNUM = require('../../constants/numerical').BADNUM;

function isAbsolute(a) {
    return (a === 'a' || a === 'absolute');
}

function isTotal(a) {
    return (a === 't' || a === 'total');
}

module.exports = function calc(gd, trace) {
    var xa = Axes.getFromId(gd, trace.xaxis || 'x');
    var ya = Axes.getFromId(gd, trace.yaxis || 'y');
    var size, pos;

    if(trace.orientation === 'h') {
        size = xa.makeCalcdata(trace, 'x');
        pos = ya.makeCalcdata(trace, 'y');
    } else {
        size = ya.makeCalcdata(trace, 'y');
        pos = xa.makeCalcdata(trace, 'x');
    }

    // create the "calculated data" to plot
    var serieslen = Math.min(pos.length, size.length);
    var cd = new Array(serieslen);

    // set position and size (as well as for waterfall total size)
    var previousSum = 0;
    var newSize;
    // trace-wide flags
    var hasTotals = false;

    for(var i = 0; i < serieslen; i++) {
        var amount = size[i] || 0;

        var connectToNext = false;
        if(size[i] !== BADNUM || isTotal(trace.measure[i]) || isAbsolute(trace.measure[i])) {
            if(i + 1 < serieslen && (size[i + 1] !== BADNUM || isTotal(trace.measure[i + 1]) || isAbsolute(trace.measure[i + 1]))) {
                connectToNext = true;
            }
        }

        var cdi = cd[i] = {
            i: i,
            p: pos[i],
            s: amount,
            rawS: amount,
            cNext: connectToNext
        };

        if(isAbsolute(trace.measure[i])) {
            previousSum = cdi.s;

            cdi.isSum = true;
            cdi.dir = 'totals';
            cdi.s = previousSum;
        } else if(isTotal(trace.measure[i])) {
            cdi.isSum = true;
            cdi.dir = 'totals';
            cdi.s = previousSum;
        } else {
            // default: relative
            cdi.isSum = false;
            cdi.dir = cdi.rawS < 0 ? 'decreasing' : 'increasing';
            newSize = cdi.s;
            cdi.s = previousSum + newSize;
            previousSum += newSize;
        }

        if(cdi.dir === 'totals') {
            hasTotals = true;
        }

        if(trace.ids) {
            cdi.id = String(trace.ids[i]);
        }

        cdi.v = (trace.base || 0) + previousSum;
    }

    if(cd.length) cd[0].hasTotals = hasTotals;

    mergeArray(trace.text, cd, 'tx');
    mergeArray(trace.hovertext, cd, 'htx');
    calcSelection(cd, trace);

    return cd;
};
