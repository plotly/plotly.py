/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorscaleCalc = require('../../components/colorscale/calc');

module.exports = function calc(gd, trace) {
    trace._len = Math.min(trace.x.length, trace.y.length, trace.z.length, trace.value.length);

    var min = Infinity;
    var max = -Infinity;
    var len = trace.value.length;
    for(var i = 0; i < len; i++) {
        var v = trace.value[i];
        min = Math.min(min, v);
        max = Math.max(max, v);
    }

    trace._minValues = min;
    trace._maxValues = max;

    trace._vMin = (trace.isomin === undefined || trace.isomin === null) ? min : trace.isomin;
    trace._vMax = (trace.isomax === undefined || trace.isomin === null) ? max : trace.isomax;

    colorscaleCalc(gd, trace, {
        vals: [trace._vMin, trace._vMax],
        containerStr: '',
        cLetter: 'c'
    });
};
