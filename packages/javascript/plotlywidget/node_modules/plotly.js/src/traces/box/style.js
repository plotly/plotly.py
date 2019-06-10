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
var Drawing = require('../../components/drawing');

function style(gd, cd) {
    var s = cd ? cd[0].node3 : d3.select(gd).selectAll('g.trace.boxes');

    s.style('opacity', function(d) { return d[0].trace.opacity; });

    s.each(function(d) {
        var el = d3.select(this);
        var trace = d[0].trace;
        var lineWidth = trace.line.width;

        function styleBox(boxSel, lineWidth, lineColor, fillColor) {
            boxSel.style('stroke-width', lineWidth + 'px')
                .call(Color.stroke, lineColor)
                .call(Color.fill, fillColor);
        }

        var allBoxes = el.selectAll('path.box');

        if(trace.type === 'candlestick') {
            allBoxes.each(function(boxData) {
                if(boxData.empty) return;

                var thisBox = d3.select(this);
                var container = trace[boxData.dir]; // dir = 'increasing' or 'decreasing'
                styleBox(thisBox, container.line.width, container.line.color, container.fillcolor);
                // TODO: custom selection style for candlesticks
                thisBox.style('opacity', trace.selectedpoints && !boxData.selected ? 0.3 : 1);
            });
        } else {
            styleBox(allBoxes, lineWidth, trace.line.color, trace.fillcolor);
            el.selectAll('path.mean')
                .style({
                    'stroke-width': lineWidth,
                    'stroke-dasharray': (2 * lineWidth) + 'px,' + lineWidth + 'px'
                })
                .call(Color.stroke, trace.line.color);

            var pts = el.selectAll('path.point');
            Drawing.pointStyle(pts, trace, gd);
        }
    });
}

function styleOnSelect(gd, cd) {
    var s = cd[0].node3;
    var trace = cd[0].trace;
    var pts = s.selectAll('path.point');

    if(trace.selectedpoints) {
        Drawing.selectedPointStyle(pts, trace);
    } else {
        Drawing.pointStyle(pts, trace, gd);
    }
}

module.exports = {
    style: style,
    styleOnSelect: styleOnSelect
};
