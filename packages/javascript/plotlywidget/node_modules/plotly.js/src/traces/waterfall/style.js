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

var styleTextPoints = require('../bar/style').styleTextPoints;

function style(gd, cd) {
    var s = cd ? cd[0].node3 : d3.select(gd).selectAll('g.waterfalllayer').selectAll('g.trace');

    s.style('opacity', function(d) { return d[0].trace.opacity; });

    s.each(function(d) {
        var gTrace = d3.select(this);
        var trace = d[0].trace;

        gTrace.selectAll('.point > path').each(function(di) {
            if(!di.isBlank) {
                var cont = trace[di.dir].marker;

                d3.select(this)
                    .call(Color.fill, cont.color)
                    .call(Color.stroke, cont.line.color)
                    .call(Drawing.dashLine, cont.line.dash, cont.line.width)
                    .style('opacity', trace.selectedpoints && !di.selected ? 0.3 : 1);
            }
        });

        styleTextPoints(gTrace, trace, gd);

        gTrace.selectAll('.lines').each(function() {
            var cont = trace.connector.line;

            Drawing.lineGroupStyle(
                d3.select(this).selectAll('path'),
                cont.width,
                cont.color,
                cont.dash
            );
        });
    });
}

module.exports = {
    style: style
};
