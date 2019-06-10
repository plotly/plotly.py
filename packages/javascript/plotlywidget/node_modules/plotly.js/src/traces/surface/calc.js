/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var colorscaleCalc = require('../../components/colorscale/calc');


// Compute auto-z and autocolorscale if applicable
module.exports = function calc(gd, trace) {
    if(trace.surfacecolor) {
        colorscaleCalc(gd, trace, {
            vals: trace.surfacecolor,
            containerStr: '',
            cLetter: 'c'
        });
    } else {
        colorscaleCalc(gd, trace, {
            vals: trace.z,
            containerStr: '',
            cLetter: 'c'
        });
    }
};
