/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var Color = require('../../components/color');
var stylePoints = require('../scatter/style').stylePoints;

module.exports = function style(gd, cd) {
    var s = cd ? cd[0].node3 : d3.select(gd).selectAll('g.trace.violins');

    s.style('opacity', function(d) { return d[0].trace.opacity; });

    s.each(function(d) {
        var trace = d[0].trace;
        var sel = d3.select(this);
        var box = trace.box || {};
        var boxLine = box.line || {};
        var meanline = trace.meanline || {};
        var meanLineWidth = meanline.width;

        sel.selectAll('path.violin')
            .style('stroke-width', trace.line.width + 'px')
            .call(Color.stroke, trace.line.color)
            .call(Color.fill, trace.fillcolor);

        sel.selectAll('path.box')
            .style('stroke-width', boxLine.width + 'px')
            .call(Color.stroke, boxLine.color)
            .call(Color.fill, box.fillcolor);

        var meanLineStyle = {
            'stroke-width': meanLineWidth + 'px',
            'stroke-dasharray': (2 * meanLineWidth) + 'px,' + meanLineWidth + 'px'
        };

        sel.selectAll('path.mean')
            .style(meanLineStyle)
            .call(Color.stroke, meanline.color);

        sel.selectAll('path.meanline')
            .style(meanLineStyle)
            .call(Color.stroke, meanline.color);

        stylePoints(sel, trace, gd);
    });
};
