/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');

var calcColorscale = require('../scatter/colorscale_calc');
var arraysToCalcdata = require('../scatter/arrays_to_calcdata');
var calcSelection = require('../scatter/calc_selection');
var calcMarkerSize = require('../scatter/calc').calcMarkerSize;

var dataArrays = ['a', 'b', 'c'];
var arraysToFill = {a: ['b', 'c'], b: ['a', 'c'], c: ['a', 'b']};

module.exports = function calc(gd, trace) {
    var ternary = gd._fullLayout[trace.subplot];
    var displaySum = ternary.sum;
    var normSum = trace.sum || displaySum;
    var arrays = {a: trace.a, b: trace.b, c: trace.c};

    var i, j, dataArray, newArray, fillArray1, fillArray2;

    // fill in one missing component
    for(i = 0; i < dataArrays.length; i++) {
        dataArray = dataArrays[i];
        if(arrays[dataArray]) continue;

        fillArray1 = arrays[arraysToFill[dataArray][0]];
        fillArray2 = arrays[arraysToFill[dataArray][1]];
        newArray = new Array(fillArray1.length);
        for(j = 0; j < fillArray1.length; j++) {
            newArray[j] = normSum - fillArray1[j] - fillArray2[j];
        }
        arrays[dataArray] = newArray;
    }

    // make the calcdata array
    var serieslen = trace._length;
    var cd = new Array(serieslen);
    var a, b, c, norm, x, y;
    for(i = 0; i < serieslen; i++) {
        a = arrays.a[i];
        b = arrays.b[i];
        c = arrays.c[i];
        if(isNumeric(a) && isNumeric(b) && isNumeric(c)) {
            a = +a;
            b = +b;
            c = +c;
            norm = displaySum / (a + b + c);
            if(norm !== 1) {
                a *= norm;
                b *= norm;
                c *= norm;
            }
            // map a, b, c onto x and y where the full scale of y
            // is [0, sum], and x is [-sum, sum]
            // TODO: this makes `a` always the top, `b` the bottom left,
            // and `c` the bottom right. Do we want options to rearrange
            // these?
            y = a;
            x = c - b;
            cd[i] = {x: x, y: y, a: a, b: b, c: c};
        } else cd[i] = {x: false, y: false};
    }

    calcMarkerSize(trace, serieslen);
    calcColorscale(gd, trace);
    arraysToCalcdata(cd, trace);
    calcSelection(cd, trace);

    return cd;
};
