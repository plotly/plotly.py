/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var Registry = require('../../registry');
var Lib = require('../../lib');
var Drawing = require('../drawing');
var Color = require('../color');

var subTypes = require('../../traces/scatter/subtypes');
var stylePie = require('../../traces/pie/style_one');
var pieCastOption = require('../../traces/pie/helpers').castOption;

var CST_MARKER_SIZE = 12;
var CST_LINE_WIDTH = 5;
var CST_MARKER_LINE_WIDTH = 2;
var MAX_LINE_WIDTH = 10;
var MAX_MARKER_LINE_WIDTH = 5;

module.exports = function style(s, gd) {
    var fullLayout = gd._fullLayout;
    var legend = fullLayout.legend;
    var constantItemSizing = legend.itemsizing === 'constant';

    function boundLineWidth(mlw, cont, max, cst) {
        var v;
        if(mlw + 1) {
            v = mlw;
        } else if(cont && cont.width > 0) {
            v = cont.width;
        } else {
            return 0;
        }
        return constantItemSizing ? cst : Math.min(v, max);
    }

    s.each(function(d) {
        var traceGroup = d3.select(this);

        var layers = Lib.ensureSingle(traceGroup, 'g', 'layers');
        layers.style('opacity', d[0].trace.opacity);

        var valign = legend.valign;
        var lineHeight = d[0].lineHeight;
        var height = d[0].height;

        if(valign === 'middle' || !lineHeight || !height) {
            layers.attr('transform', null);
        } else {
            var factor = {top: 1, bottom: -1}[valign];
            var markerOffsetY = factor * (0.5 * (lineHeight - height + 3));
            layers.attr('transform', 'translate(0,' + markerOffsetY + ')');
        }

        var fill = layers
            .selectAll('g.legendfill')
                .data([d]);
        fill.enter().append('g')
            .classed('legendfill', true);

        var line = layers
            .selectAll('g.legendlines')
                .data([d]);
        line.enter().append('g')
            .classed('legendlines', true);

        var symbol = layers
            .selectAll('g.legendsymbols')
                .data([d]);
        symbol.enter().append('g')
            .classed('legendsymbols', true);

        symbol.selectAll('g.legendpoints')
            .data([d])
          .enter().append('g')
            .classed('legendpoints', true);
    })
    .each(styleWaterfalls)
    .each(styleFunnels)
    .each(styleBars)
    .each(styleBoxes)
    .each(styleFunnelareas)
    .each(stylePies)
    .each(styleLines)
    .each(stylePoints)
    .each(styleCandles)
    .each(styleOHLC);

    function styleLines(d) {
        var d0 = d[0];
        var trace = d0.trace;
        var showFill = trace.visible && trace.fill && trace.fill !== 'none';
        var showLine = subTypes.hasLines(trace);
        var contours = trace.contours;
        var showGradientLine = false;
        var showGradientFill = false;
        var dMod, tMod;

        if(contours) {
            var coloring = contours.coloring;

            if(coloring === 'lines') {
                showGradientLine = true;
            } else {
                showLine = coloring === 'none' || coloring === 'heatmap' || contours.showlines;
            }

            if(contours.type === 'constraint') {
                showFill = contours._operation !== '=';
            } else if(coloring === 'fill' || coloring === 'heatmap') {
                showGradientFill = true;
            }
        }

        // with fill and no markers or text, move the line and fill up a bit
        // so it's more centered
        var markersOrText = subTypes.hasMarkers(trace) || subTypes.hasText(trace);
        var anyFill = showFill || showGradientFill;
        var anyLine = showLine || showGradientLine;
        var pathStart = (markersOrText || !anyFill) ? 'M5,0' :
            // with a line leave it slightly below center, to leave room for the
            // line thickness and because the line is usually more prominent
            anyLine ? 'M5,-2' : 'M5,-3';

        var this3 = d3.select(this);

        var fill = this3.select('.legendfill').selectAll('path')
            .data(showFill || showGradientFill ? [d] : []);
        fill.enter().append('path').classed('js-fill', true);
        fill.exit().remove();
        fill.attr('d', pathStart + 'h30v6h-30z')
            .call(showFill ? Drawing.fillGroupStyle : fillGradient);

        if(showLine || showGradientLine) {
            var lw = boundLineWidth(undefined, trace.line, MAX_LINE_WIDTH, CST_LINE_WIDTH);
            tMod = Lib.minExtend(trace, {line: {width: lw}});
            dMod = [Lib.minExtend(d0, {trace: tMod})];
        }

        var line = this3.select('.legendlines').selectAll('path')
            .data(showLine || showGradientLine ? [dMod] : []);
        line.enter().append('path').classed('js-line', true);
        line.exit().remove();

        // this is ugly... but you can't apply a gradient to a perfectly
        // horizontal or vertical line. Presumably because then
        // the system doesn't know how to scale vertical variation, even
        // though there *is* no vertical variation in this case.
        // so add an invisibly small angle to the line
        // This issue (and workaround) exist across (Mac) Chrome, FF, and Safari
        line.attr('d', pathStart + (showGradientLine ? 'l30,0.0001' : 'h30'))
            .call(showLine ? Drawing.lineGroupStyle : lineGradient);

        function fillGradient(s) {
            if(s.size()) {
                var gradientID = 'legendfill-' + trace.uid;
                Drawing.gradient(s, gd, gradientID, 'horizontalreversed',
                    trace.colorscale, 'fill');
            }
        }

        function lineGradient(s) {
            if(s.size()) {
                var gradientID = 'legendline-' + trace.uid;
                Drawing.lineGroupStyle(s);
                Drawing.gradient(s, gd, gradientID, 'horizontalreversed',
                    trace.colorscale, 'stroke');
            }
        }
    }

    function stylePoints(d) {
        var d0 = d[0];
        var trace = d0.trace;
        var showMarkers = subTypes.hasMarkers(trace);
        var showText = subTypes.hasText(trace);
        var showLines = subTypes.hasLines(trace);
        var dMod, tMod;

        // 'scatter3d' don't use gd.calcdata,
        // use d0.trace to infer arrayOk attributes

        function boundVal(attrIn, arrayToValFn, bounds, cst) {
            var valIn = Lib.nestedProperty(trace, attrIn).get();
            var valToBound = (Lib.isArrayOrTypedArray(valIn) && arrayToValFn) ?
                arrayToValFn(valIn) :
                valIn;

            if(constantItemSizing && valToBound && cst !== undefined) {
                valToBound = cst;
            }

            if(bounds) {
                if(valToBound < bounds[0]) return bounds[0];
                else if(valToBound > bounds[1]) return bounds[1];
            }
            return valToBound;
        }

        function pickFirst(array) { return array[0]; }

        // constrain text, markers, etc so they'll fit on the legend
        if(showMarkers || showText || showLines) {
            var dEdit = {};
            var tEdit = {};

            if(showMarkers) {
                dEdit.mc = boundVal('marker.color', pickFirst);
                dEdit.mx = boundVal('marker.symbol', pickFirst);
                dEdit.mo = boundVal('marker.opacity', Lib.mean, [0.2, 1]);
                dEdit.mlc = boundVal('marker.line.color', pickFirst);
                dEdit.mlw = boundVal('marker.line.width', Lib.mean, [0, 5], CST_MARKER_LINE_WIDTH);
                tEdit.marker = {
                    sizeref: 1,
                    sizemin: 1,
                    sizemode: 'diameter'
                };

                var ms = boundVal('marker.size', Lib.mean, [2, 16], CST_MARKER_SIZE);
                dEdit.ms = ms;
                tEdit.marker.size = ms;
            }

            if(showLines) {
                tEdit.line = {
                    width: boundVal('line.width', pickFirst, [0, 10], CST_LINE_WIDTH)
                };
            }

            if(showText) {
                dEdit.tx = 'Aa';
                dEdit.tp = boundVal('textposition', pickFirst);
                dEdit.ts = 10;
                dEdit.tc = boundVal('textfont.color', pickFirst);
                dEdit.tf = boundVal('textfont.family', pickFirst);
            }

            dMod = [Lib.minExtend(d0, dEdit)];
            tMod = Lib.minExtend(trace, tEdit);

            // always show legend items in base state
            tMod.selectedpoints = null;
        }

        var ptgroup = d3.select(this).select('g.legendpoints');

        var pts = ptgroup.selectAll('path.scatterpts')
            .data(showMarkers ? dMod : []);
        // make sure marker is on the bottom, in case it enters after text
        pts.enter().insert('path', ':first-child')
            .classed('scatterpts', true)
            .attr('transform', 'translate(20,0)');
        pts.exit().remove();
        pts.call(Drawing.pointStyle, tMod, gd);

        // 'mrc' is set in pointStyle and used in textPointStyle:
        // constrain it here
        if(showMarkers) dMod[0].mrc = 3;

        var txt = ptgroup.selectAll('g.pointtext')
            .data(showText ? dMod : []);
        txt.enter()
            .append('g').classed('pointtext', true)
                .append('text').attr('transform', 'translate(20,0)');
        txt.exit().remove();
        txt.selectAll('text').call(Drawing.textPointStyle, tMod, gd);
    }

    function styleWaterfalls(d) {
        var trace = d[0].trace;

        var ptsData = [];
        if(trace.type === 'waterfall' && trace.visible) {
            ptsData = d[0].hasTotals ?
                [['increasing', 'M-6,-6V6H0Z'], ['totals', 'M6,6H0L-6,-6H-0Z'], ['decreasing', 'M6,6V-6H0Z']] :
                [['increasing', 'M-6,-6V6H6Z'], ['decreasing', 'M6,6V-6H-6Z']];
        }

        var pts = d3.select(this).select('g.legendpoints')
            .selectAll('path.legendwaterfall')
            .data(ptsData);
        pts.enter().append('path').classed('legendwaterfall', true)
            .attr('transform', 'translate(20,0)')
            .style('stroke-miterlimit', 1);
        pts.exit().remove();

        pts.each(function(dd) {
            var pt = d3.select(this);
            var cont = trace[dd[0]].marker;
            var lw = boundLineWidth(undefined, cont.line, MAX_MARKER_LINE_WIDTH, CST_MARKER_LINE_WIDTH);

            pt.attr('d', dd[1])
                .style('stroke-width', lw + 'px')
                .call(Color.fill, cont.color);

            if(lw) {
                pt.call(Color.stroke, cont.line.color);
            }
        });
    }

    function styleBars(d) {
        styleBarLike(d, this);
    }

    function styleFunnels(d) {
        styleBarLike(d, this, 'funnel');
    }

    function styleBarLike(d, lThis, desiredType) {
        var trace = d[0].trace;
        var marker = trace.marker || {};
        var markerLine = marker.line || {};

        var isVisible = (!desiredType) ? Registry.traceIs(trace, 'bar') :
            (trace.type === desiredType && trace.visible);

        var barpath = d3.select(lThis).select('g.legendpoints')
            .selectAll('path.legend' + desiredType)
            .data(isVisible ? [d] : []);
        barpath.enter().append('path').classed('legend' + desiredType, true)
            .attr('d', 'M6,6H-6V-6H6Z')
            .attr('transform', 'translate(20,0)');
        barpath.exit().remove();

        barpath.each(function(d) {
            var p = d3.select(this);
            var d0 = d[0];
            var w = boundLineWidth(d0.mlw, marker.line, MAX_MARKER_LINE_WIDTH, CST_MARKER_LINE_WIDTH);

            p.style('stroke-width', w + 'px')
                .call(Color.fill, d0.mc || marker.color);

            if(w) Color.stroke(p, d0.mlc || markerLine.color);
        });
    }

    function styleBoxes(d) {
        var trace = d[0].trace;

        var pts = d3.select(this).select('g.legendpoints')
            .selectAll('path.legendbox')
            .data(Registry.traceIs(trace, 'box-violin') && trace.visible ? [d] : []);
        pts.enter().append('path').classed('legendbox', true)
            // if we want the median bar, prepend M6,0H-6
            .attr('d', 'M6,6H-6V-6H6Z')
            .attr('transform', 'translate(20,0)');
        pts.exit().remove();

        pts.each(function() {
            var p = d3.select(this);

            if((trace.boxpoints === 'all' || trace.points === 'all') &&
                Color.opacity(trace.fillcolor) === 0 && Color.opacity((trace.line || {}).color) === 0
            ) {
                var tMod = Lib.minExtend(trace, {
                    marker: {
                        size: constantItemSizing ? CST_MARKER_SIZE : Lib.constrain(trace.marker.size, 2, 16),
                        sizeref: 1,
                        sizemin: 1,
                        sizemode: 'diameter'
                    }
                });
                pts.call(Drawing.pointStyle, tMod, gd);
            } else {
                var w = boundLineWidth(undefined, trace.line, MAX_MARKER_LINE_WIDTH, CST_MARKER_LINE_WIDTH);

                p.style('stroke-width', w + 'px')
                    .call(Color.fill, trace.fillcolor);

                if(w) Color.stroke(p, trace.line.color);
            }
        });
    }

    function styleCandles(d) {
        var trace = d[0].trace;

        var pts = d3.select(this).select('g.legendpoints')
            .selectAll('path.legendcandle')
            .data(trace.type === 'candlestick' && trace.visible ? [d, d] : []);
        pts.enter().append('path').classed('legendcandle', true)
            .attr('d', function(_, i) {
                if(i) return 'M-15,0H-8M-8,6V-6H8Z'; // increasing
                return 'M15,0H8M8,-6V6H-8Z'; // decreasing
            })
            .attr('transform', 'translate(20,0)')
            .style('stroke-miterlimit', 1);
        pts.exit().remove();

        pts.each(function(_, i) {
            var p = d3.select(this);
            var cont = trace[i ? 'increasing' : 'decreasing'];
            var w = boundLineWidth(undefined, cont.line, MAX_MARKER_LINE_WIDTH, CST_MARKER_LINE_WIDTH);

            p.style('stroke-width', w + 'px')
                .call(Color.fill, cont.fillcolor);

            if(w) Color.stroke(p, cont.line.color);
        });
    }

    function styleOHLC(d) {
        var trace = d[0].trace;

        var pts = d3.select(this).select('g.legendpoints')
            .selectAll('path.legendohlc')
            .data(trace.type === 'ohlc' && trace.visible ? [d, d] : []);
        pts.enter().append('path').classed('legendohlc', true)
            .attr('d', function(_, i) {
                if(i) return 'M-15,0H0M-8,-6V0'; // increasing
                return 'M15,0H0M8,6V0'; // decreasing
            })
            .attr('transform', 'translate(20,0)')
            .style('stroke-miterlimit', 1);
        pts.exit().remove();

        pts.each(function(_, i) {
            var p = d3.select(this);
            var cont = trace[i ? 'increasing' : 'decreasing'];
            var w = boundLineWidth(undefined, cont.line, MAX_MARKER_LINE_WIDTH, CST_MARKER_LINE_WIDTH);

            p.style('fill', 'none')
                .call(Drawing.dashLine, cont.line.dash, w);

            if(w) Color.stroke(p, cont.line.color);
        });
    }

    function stylePies(d) {
        stylePieLike(d, this, 'pie');
    }

    function styleFunnelareas(d) {
        stylePieLike(d, this, 'funnelarea');
    }

    function stylePieLike(d, lThis, desiredType) {
        var d0 = d[0];
        var trace = d0.trace;

        var isVisible = (!desiredType) ? Registry.traceIs(trace, desiredType) :
            (trace.type === desiredType && trace.visible);

        var pts = d3.select(lThis).select('g.legendpoints')
            .selectAll('path.legend' + desiredType)
            .data(isVisible ? [d] : []);
        pts.enter().append('path').classed('legend' + desiredType, true)
            .attr('d', 'M6,6H-6V-6H6Z')
            .attr('transform', 'translate(20,0)');
        pts.exit().remove();

        if(pts.size()) {
            var cont = (trace.marker || {}).line;
            var lw = boundLineWidth(pieCastOption(cont.width, d0.pts), cont, MAX_MARKER_LINE_WIDTH, CST_MARKER_LINE_WIDTH);

            var tMod = Lib.minExtend(trace, {marker: {line: {width: lw}}});
            // since minExtend do not slice more than 3 items we need to patch line.color here
            tMod.marker.line.color = cont.color;

            var d0Mod = Lib.minExtend(d0, {trace: tMod});

            stylePie(pts, d0Mod, tMod);
        }
    }
};
