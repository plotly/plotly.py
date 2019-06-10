/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var Drawing = require('../../components/drawing');
var Color = require('../../components/color');

module.exports = function style(gd, cd) {
    var s = cd ? cd[0].node3 : d3.select(gd).selectAll('g.ohlclayer').selectAll('g.trace');

    s.style('opacity', function(d) {
        return d[0].trace.opacity;
    });

    s.each(function(d) {
        var trace = d[0].trace;

        d3.select(this).selectAll('path').each(function(di) {
            if(di.empty) return;

            var dirLine = trace[di.dir].line;
            d3.select(this)
                .style('fill', 'none')
                .call(Color.stroke, dirLine.color)
                .call(Drawing.dashLine, dirLine.dash, dirLine.width)
                // TODO: custom selection style for OHLC
                .style('opacity', trace.selectedpoints && !di.selected ? 0.3 : 1);
        });
    });
};
