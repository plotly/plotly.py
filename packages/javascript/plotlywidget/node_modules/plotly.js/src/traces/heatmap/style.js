/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');

module.exports = function style(gd) {
    d3.select(gd).selectAll('.hm image')
        .style('opacity', function(d) {
            return d.trace.opacity;
        });
};
