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
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');

var barPlot = require('../bar/plot');
var getTransformToMoveInsideBar = barPlot.getTransformToMoveInsideBar;

var pieHelpers = require('../pie/helpers');
var piePlot = require('../pie/plot');

var attachFxHandlers = piePlot.attachFxHandlers;
var determineInsideTextFont = piePlot.determineInsideTextFont;

var layoutAreas = piePlot.layoutAreas;
var prerenderTitles = piePlot.prerenderTitles;
var positionTitleOutside = piePlot.positionTitleOutside;

module.exports = function plot(gd, cdModule) {
    var fullLayout = gd._fullLayout;

    prerenderTitles(cdModule, gd);
    layoutAreas(cdModule, fullLayout._size);

    Lib.makeTraceGroups(fullLayout._funnelarealayer, cdModule, 'trace').each(function(cd) {
        var plotGroup = d3.select(this);
        var cd0 = cd[0];
        var trace = cd0.trace;

        setCoords(cd);

        plotGroup.each(function() {
            var slices = d3.select(this).selectAll('g.slice').data(cd);

            slices.enter().append('g')
                .classed('slice', true);
            slices.exit().remove();

            slices.each(function(pt) {
                if(pt.hidden) {
                    d3.select(this).selectAll('path,g').remove();
                    return;
                }

                // to have consistent event data compared to other traces
                pt.pointNumber = pt.i;
                pt.curveNumber = trace.index;

                var cx = cd0.cx;
                var cy = cd0.cy;
                var sliceTop = d3.select(this);
                var slicePath = sliceTop.selectAll('path.surface').data([pt]);

                slicePath.enter().append('path')
                    .classed('surface', true)
                    .style({'pointer-events': 'all'});

                sliceTop.call(attachFxHandlers, gd, cd);

                var shape =
                    'M' + (cx + pt.TR[0]) + ',' + (cy + pt.TR[1]) +
                    line(pt.TR, pt.BR) +
                    line(pt.BR, pt.BL) +
                    line(pt.BL, pt.TL) +
                    'Z';

                slicePath.attr('d', shape);

                // add text
                var textPosition = pieHelpers.castOption(trace.textposition, pt.pts);
                var sliceTextGroup = sliceTop.selectAll('g.slicetext')
                    .data(pt.text && (textPosition !== 'none') ? [0] : []);

                sliceTextGroup.enter().append('g')
                    .classed('slicetext', true);
                sliceTextGroup.exit().remove();

                sliceTextGroup.each(function() {
                    var sliceText = Lib.ensureSingle(d3.select(this), 'text', '', function(s) {
                        // prohibit tex interpretation until we can handle
                        // tex and regular text together
                        s.attr('data-notex', 1);
                    });

                    sliceText.text(pt.text)
                        .attr({
                            'class': 'slicetext',
                            transform: '',
                            'text-anchor': 'middle'
                        })
                        .call(Drawing.font, determineInsideTextFont(trace, pt, gd._fullLayout.font))
                        .call(svgTextUtils.convertToTspans, gd);

                    // position the text relative to the slice
                    var textBB = Drawing.bBox(sliceText.node());
                    var transform;

                    var x0, x1;
                    var y0 = Math.min(pt.BL[1], pt.BR[1]);
                    var y1 = Math.max(pt.TL[1], pt.TR[1]);

                    x0 = Math.max(pt.TL[0], pt.BL[0]);
                    x1 = Math.min(pt.TR[0], pt.BR[0]);

                    transform = getTransformToMoveInsideBar(x0, x1, y0, y1, textBB, {
                        isHorizontal: true,
                        constrained: true,
                        angle: 0,
                        anchor: 'middle'
                    });

                    sliceText.attr('transform',
                        'translate(' + cx + ',' + cy + ')' + transform
                    );
                });
            });

            // add the title
            var titleTextGroup = d3.select(this).selectAll('g.titletext')
                .data(trace.title.text ? [0] : []);

            titleTextGroup.enter().append('g')
                .classed('titletext', true);
            titleTextGroup.exit().remove();

            titleTextGroup.each(function() {
                var titleText = Lib.ensureSingle(d3.select(this), 'text', '', function(s) {
                    // prohibit tex interpretation as above
                    s.attr('data-notex', 1);
                });

                var txt = trace.title.text;
                if(trace._meta) {
                    txt = Lib.templateString(txt, trace._meta);
                }

                titleText.text(txt)
                    .attr({
                        'class': 'titletext',
                        transform: '',
                        'text-anchor': 'middle',
                    })
                .call(Drawing.font, trace.title.font)
                .call(svgTextUtils.convertToTspans, gd);

                var transform = positionTitleOutside(cd0, fullLayout._size);

                titleText.attr('transform',
                    'translate(' + transform.x + ',' + transform.y + ')' +
                    (transform.scale < 1 ? ('scale(' + transform.scale + ')') : '') +
                    'translate(' + transform.tx + ',' + transform.ty + ')');
            });
        });
    });
};

function line(a, b) {
    var dx = b[0] - a[0];
    var dy = b[1] - a[1];

    return 'l' + dx + ',' + dy;
}

function getBetween(a, b) {
    return [
        0.5 * (a[0] + b[0]),
        0.5 * (a[1] + b[1])
    ];
}

function setCoords(cd) {
    if(!cd.length) return;

    var cd0 = cd[0];
    var trace = cd0.trace;

    var aspectratio = trace.aspectratio;

    var h = trace.baseratio;
    if(h > 0.999) h = 0.999; // TODO: may handle this case separately
    var h2 = Math.pow(h, 2);

    var v1 = cd0.vTotal;
    var v0 = v1 * h2 / (1 - h2);

    var totalValues = v1;
    var sumSteps = v0 / v1;

    function calcPos() {
        var q = Math.sqrt(sumSteps);
        return {
            x: q,
            y: -q
        };
    }

    function getPoint() {
        var pos = calcPos();
        return [pos.x, pos.y];
    }

    var p;
    var allPoints = [];
    allPoints.push(getPoint());

    var i, cdi;
    for(i = cd.length - 1; i > -1; i--) {
        cdi = cd[i];
        if(cdi.hidden) continue;

        var step = cdi.v / totalValues;
        sumSteps += step;

        allPoints.push(getPoint());
    }

    var minY = Infinity;
    var maxY = -Infinity;
    for(i = 0; i < allPoints.length; i++) {
        p = allPoints[i];
        minY = Math.min(minY, p[1]);
        maxY = Math.max(maxY, p[1]);
    }

    // center the shape
    for(i = 0; i < allPoints.length; i++) {
        allPoints[i][1] -= (maxY + minY) / 2;
    }

    var lastX = allPoints[allPoints.length - 1][0];

    // get pie r
    var r = cd0.r;

    var rY = (maxY - minY) / 2;
    var scaleX = r / lastX;
    var scaleY = r / rY * aspectratio;

    // set funnelarea r
    cd0.r = scaleY * rY;

    // scale the shape
    for(i = 0; i < allPoints.length; i++) {
        allPoints[i][0] *= scaleX;
        allPoints[i][1] *= scaleY;
    }

    // record first position
    p = allPoints[0];
    var prevLeft = [-p[0], p[1]];
    var prevRight = [p[0], p[1]];

    var n = 0; // note we skip the very first point.
    for(i = cd.length - 1; i > -1; i--) {
        cdi = cd[i];
        if(cdi.hidden) continue;

        n += 1;
        var x = allPoints[n][0];
        var y = allPoints[n][1];

        cdi.TL = [-x, y];
        cdi.TR = [x, y];

        cdi.BL = prevLeft;
        cdi.BR = prevRight;

        cdi.pxmid = getBetween(cdi.TR, cdi.BR);

        prevLeft = cdi.TL;
        prevRight = cdi.TR;
    }
}
