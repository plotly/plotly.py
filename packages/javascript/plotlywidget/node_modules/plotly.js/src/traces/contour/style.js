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
var heatmapStyle = require('../heatmap/style');

var makeColorMap = require('./make_color_map');


module.exports = function style(gd) {
    var contours = d3.select(gd).selectAll('g.contour');

    contours.style('opacity', function(d) {
        return d[0].trace.opacity;
    });

    contours.each(function(d) {
        var c = d3.select(this);
        var trace = d[0].trace;
        var contours = trace.contours;
        var line = trace.line;
        var cs = contours.size || 1;
        var start = contours.start;

        // for contourcarpet only - is this a constraint-type contour trace?
        var isConstraintType = contours.type === 'constraint';
        var colorLines = !isConstraintType && contours.coloring === 'lines';
        var colorFills = !isConstraintType && contours.coloring === 'fill';

        var colorMap = (colorLines || colorFills) ? makeColorMap(trace) : null;

        c.selectAll('g.contourlevel').each(function(d) {
            d3.select(this).selectAll('path')
                .call(Drawing.lineGroupStyle,
                    line.width,
                    colorLines ? colorMap(d.level) : line.color,
                    line.dash);
        });

        var labelFont = contours.labelfont;
        c.selectAll('g.contourlabels text').each(function(d) {
            Drawing.font(d3.select(this), {
                family: labelFont.family,
                size: labelFont.size,
                color: labelFont.color || (colorLines ? colorMap(d.level) : line.color)
            });
        });

        if(isConstraintType) {
            c.selectAll('g.contourfill path')
                .style('fill', trace.fillcolor);
        } else if(colorFills) {
            var firstFill;

            c.selectAll('g.contourfill path')
                .style('fill', function(d) {
                    if(firstFill === undefined) firstFill = d.level;
                    return colorMap(d.level + 0.5 * cs);
                });

            if(firstFill === undefined) firstFill = start;

            c.selectAll('g.contourbg path')
                .style('fill', colorMap(firstFill - 0.5 * cs));
        }
    });

    heatmapStyle(gd);
};
