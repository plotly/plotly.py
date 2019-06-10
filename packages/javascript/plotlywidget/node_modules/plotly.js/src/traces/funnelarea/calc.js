/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var pieCalc = require('../pie/calc');

function calc(gd, trace) {
    return pieCalc.calc(gd, trace);
}

function crossTraceCalc(gd) {
    pieCalc.crossTraceCalc(gd, { type: 'funnelarea' });
}

module.exports = {
    calc: calc,
    crossTraceCalc: crossTraceCalc
};
