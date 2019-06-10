/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var styleOne = require('./style_one');

module.exports = function style(gd) {
    gd._fullLayout._pielayer.selectAll('.trace').each(function(cd) {
        var cd0 = cd[0];
        var trace = cd0.trace;
        var traceSelection = d3.select(this);

        traceSelection.style({opacity: trace.opacity});

        traceSelection.selectAll('path.surface').each(function(pt) {
            d3.select(this).call(styleOne, pt, trace);
        });
    });
};
