/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');
var BADNUM = require('../../constants/numerical').BADNUM;

var colorscaleCalc = require('../../components/colorscale/calc');
var arraysToCalcdata = require('../scatter/arrays_to_calcdata');
var calcSelection = require('../scatter/calc_selection');

module.exports = function calc(gd, trace) {
    var len = trace._length;
    var calcTrace = new Array(len);

    for(var i = 0; i < len; i++) {
        var calcPt = calcTrace[i] = {};
        var loc = trace.locations[i];
        var z = trace.z[i];

        calcPt.loc = typeof loc === 'string' ? loc : null;
        calcPt.z = isNumeric(z) ? z : BADNUM;
    }

    arraysToCalcdata(calcTrace, trace);
    colorscaleCalc(gd, trace, {
        vals: trace.z,
        containerStr: '',
        cLetter: 'z'
    });
    calcSelection(calcTrace, trace);

    return calcTrace;
};
