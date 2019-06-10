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
    if(trace.intensity) {
        colorscaleCalc(gd, trace, {
            vals: trace.intensity,
            containerStr: '',
            cLetter: 'c'
        });
    }
};
