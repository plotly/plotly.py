/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var tinycolor = require('tinycolor2');

var Plots = require('../../plots/plots');
var Registry = require('../../registry');
var Axes = require('../../plots/cartesian/axes');
var dragElement = require('../dragelement');
var Lib = require('../../lib');
var extendFlat = require('../../lib/extend').extendFlat;
var setCursor = require('../../lib/setcursor');
var Drawing = require('../drawing');
var Color = require('../color');
var Titles = require('../titles');
var svgTextUtils = require('../../lib/svg_text_utils');
var flipScale = require('../colorscale/helpers').flipScale;

var handleAxisDefaults = require('../../plots/cartesian/axis_defaults');
var handleAxisPositionDefaults = require('../../plots/cartesian/position_defaults');
var axisLayoutAttrs = require('../../plots/cartesian/layout_attributes');

var alignmentConstants = require('../../constants/alignment');
var LINE_SPACING = alignmentConstants.LINE_SPACING;
var FROM_TL = alignmentConstants.FROM_TL;
var FROM_BR = alignmentConstants.FROM_BR;

var cn = require('./constants').cn;

function draw(gd) {
    var fullLayout = gd._fullLayout;

    var colorBars = fullLayout._infolayer
        .selectAll('g.' + cn.colorbar)
        .data(makeColorBarData(gd), function(opts) { return opts._id; });

    colorBars.enter().append('g')
        .attr('class', function(opts) { return opts._id; })
        .classed(cn.colorbar, true);

    colorBars.each(function(opts) {
        var g = d3.select(this);

        Lib.ensureSingle(g, 'rect', cn.cbbg);
        Lib.ensureSingle(g, 'g', cn.cbfills);
        Lib.ensureSingle(g, 'g', cn.cblines);
        Lib.ensureSingle(g, 'g', cn.cbaxis, function(s) { s.classed(cn.crisp, true); });
        Lib.ensureSingle(g, 'g', cn.cbtitleunshift, function(s) { s.append('g').classed(cn.cbtitle, true); });
        Lib.ensureSingle(g, 'rect', cn.cboutline);

        var done = drawColorBar(g, opts, gd);
        if(done && done.then) (gd._promises || []).push(done);

        if(gd._context.edits.colorbarPosition) {
            makeEditable(g, opts, gd);
        }
    });

    colorBars.exit()
        .each(function(opts) { Plots.autoMargin(gd, opts._id); })
        .remove();

    colorBars.order();
}

function makeColorBarData(gd) {
    var fullLayout = gd._fullLayout;
    var calcdata = gd.calcdata;
    var out = [];

    // single out item
    var opts;
    // colorbar attr parent container
    var cont;
    // trace attr container
    var trace;
    // colorbar options
    var cbOpt;

    function initOpts(opts) {
        return extendFlat(opts, {
            // fillcolor can be a d3 scale, domain is z values, range is colors
            // or leave it out for no fill,
            // or set to a string constant for single-color fill
            _fillcolor: null,
            // line.color has the same options as fillcolor
            _line: {color: null, width: null, dash: null},
            // levels of lines to draw.
            // note that this DOES NOT determine the extent of the bar
            // that's given by the domain of fillcolor
            // (or line.color if no fillcolor domain)
            _levels: {start: null, end: null, size: null},
            // separate fill levels (for example, heatmap coloring of a
            // contour map) if this is omitted, fillcolors will be
            // evaluated halfway between levels
            _filllevels: null,
            // for continuous colorscales: fill with a gradient instead of explicit levels
            // value should be the colorscale [[0, c0], [v1, c1], ..., [1, cEnd]]
            _fillgradient: null,
            // when using a gradient, we need the data range specified separately
            _zrange: null
        });
    }

    function calcOpts() {
        if(typeof cbOpt.calc === 'function') {
            cbOpt.calc(gd, trace, opts);
        } else {
            opts._fillgradient = cont.reversescale ?
                flipScale(cont.colorscale) :
                cont.colorscale;
            opts._zrange = [cont[cbOpt.min], cont[cbOpt.max]];
        }
    }

    for(var i = 0; i < calcdata.length; i++) {
        var cd = calcdata[i];
        trace = cd[0].trace;
        var moduleOpts = trace._module.colorbar;

        if(trace.visible === true && moduleOpts) {
            var allowsMultiplotCbs = Array.isArray(moduleOpts);
            var cbOpts = allowsMultiplotCbs ? moduleOpts : [moduleOpts];

            for(var j = 0; j < cbOpts.length; j++) {
                cbOpt = cbOpts[j];
                var contName = cbOpt.container;
                cont = contName ? trace[contName] : trace;

                if(cont && cont.showscale) {
                    opts = initOpts(cont.colorbar);
                    opts._id = 'cb' + trace.uid + (allowsMultiplotCbs && contName ? '-' + contName : '');
                    opts._traceIndex = trace.index;
                    opts._propPrefix = (contName ? contName + '.' : '') + 'colorbar.';
                    opts._meta = trace._meta;
                    calcOpts();
                    out.push(opts);
                }
            }
        }
    }

    for(var k in fullLayout._colorAxes) {
        cont = fullLayout[k];

        if(cont.showscale) {
            var colorAxOpts = fullLayout._colorAxes[k];

            opts = initOpts(cont.colorbar);
            opts._id = 'cb' + k;
            opts._propPrefix = k + '.colorbar.';
            opts._meta = fullLayout._meta;

            cbOpt = {min: 'cmin', max: 'cmax'};
            if(colorAxOpts[0] !== 'heatmap') {
                trace = colorAxOpts[1];
                cbOpt.calc = trace._module.colorbar.calc;
            }

            calcOpts();
            out.push(opts);
        }
    }

    return out;
}

function drawColorBar(g, opts, gd) {
    var fullLayout = gd._fullLayout;
    var gs = fullLayout._size;

    var fillColor = opts._fillcolor;
    var line = opts._line;
    var title = opts.title;
    var titleSide = title.side;

    var zrange = opts._zrange ||
        d3.extent((typeof fillColor === 'function' ? fillColor : line.color).domain());

    var lineColormap = typeof line.color === 'function' ?
        line.color :
        function() { return line.color; };
    var fillColormap = typeof fillColor === 'function' ?
        fillColor :
        function() { return fillColor; };

    var levelsIn = opts._levels;
    var levelsOut = calcLevels(gd, opts, zrange);
    var fillLevels = levelsOut.fill;
    var lineLevels = levelsOut.line;

    // we calculate pixel sizes based on the specified graph size,
    // not the actual (in case something pushed the margins around)
    // which is a little odd but avoids an odd iterative effect
    // when the colorbar itself is pushing the margins.
    // but then the fractional size is calculated based on the
    // actual graph size, so that the axes will size correctly.
    var thickPx = Math.round(opts.thickness * (opts.thicknessmode === 'fraction' ? gs.w : 1));
    var thickFrac = thickPx / gs.w;
    var lenPx = Math.round(opts.len * (opts.lenmode === 'fraction' ? gs.h : 1));
    var lenFrac = lenPx / gs.h;
    var xpadFrac = opts.xpad / gs.w;
    var yExtraPx = (opts.borderwidth + opts.outlinewidth) / 2;
    var ypadFrac = opts.ypad / gs.h;

    // x positioning: do it initially just for left anchor,
    // then fix at the end (since we don't know the width yet)
    var xLeft = Math.round(opts.x * gs.w + opts.xpad);
    // for dragging... this is getting a little muddled...
    var xLeftFrac = opts.x - thickFrac * ({middle: 0.5, right: 1}[opts.xanchor] || 0);

    // y positioning we can do correctly from the start
    var yBottomFrac = opts.y + lenFrac * (({top: -0.5, bottom: 0.5}[opts.yanchor] || 0) - 0.5);
    var yBottomPx = Math.round(gs.h * (1 - yBottomFrac));
    var yTopPx = yBottomPx - lenPx;

    // stash a few things for makeEditable
    opts._lenFrac = lenFrac;
    opts._thickFrac = thickFrac;
    opts._xLeftFrac = xLeftFrac;
    opts._yBottomFrac = yBottomFrac;

    var ax = mockColorBarAxis(gd, opts, zrange);

    // position can't go in through supplyDefaults
    // because that restricts it to [0,1]
    ax.position = opts.x + xpadFrac + thickFrac;

    if(['top', 'bottom'].indexOf(titleSide) !== -1) {
        ax.title.side = titleSide;
        ax.titlex = opts.x + xpadFrac;
        ax.titley = yBottomFrac + (title.side === 'top' ? lenFrac - ypadFrac : ypadFrac);
    }

    if(line.color && opts.tickmode === 'auto') {
        ax.tickmode = 'linear';
        ax.tick0 = levelsIn.start;
        var dtick = levelsIn.size;
        // expand if too many contours, so we don't get too many ticks
        var autoNtick = Lib.constrain((yBottomPx - yTopPx) / 50, 4, 15) + 1;
        var dtFactor = (zrange[1] - zrange[0]) / ((opts.nticks || autoNtick) * dtick);
        if(dtFactor > 1) {
            var dtexp = Math.pow(10, Math.floor(Math.log(dtFactor) / Math.LN10));
            dtick *= dtexp * Lib.roundUp(dtFactor / dtexp, [2, 5, 10]);
            // if the contours are at round multiples, reset tick0
            // so they're still at round multiples. Otherwise,
            // keep the first label on the first contour level
            if((Math.abs(levelsIn.start) / levelsIn.size + 1e-6) % 1 < 2e-6) {
                ax.tick0 = 0;
            }
        }
        ax.dtick = dtick;
    }

    // set domain after init, because we may want to
    // allow it outside [0,1]
    ax.domain = [
        yBottomFrac + ypadFrac,
        yBottomFrac + lenFrac - ypadFrac
    ];

    ax.setScale();

    g.attr('transform', 'translate(' + Math.round(gs.l) + ',' + Math.round(gs.t) + ')');

    var titleCont = g.select('.' + cn.cbtitleunshift)
        .attr('transform', 'translate(-' + Math.round(gs.l) + ',-' + Math.round(gs.t) + ')');

    var axLayer = g.select('.' + cn.cbaxis);
    var titleEl;
    var titleHeight = 0;

    function drawTitle(titleClass, titleOpts) {
        var dfltTitleOpts = {
            propContainer: ax,
            propName: opts._propPrefix + 'title',
            traceIndex: opts._traceIndex,
            _meta: opts._meta,
            placeholder: fullLayout._dfltTitle.colorbar,
            containerGroup: g.select('.' + cn.cbtitle)
        };

        // this class-to-rotate thing with convertToTspans is
        // getting hackier and hackier... delete groups with the
        // wrong class (in case earlier the colorbar was drawn on
        // a different side, I think?)
        var otherClass = titleClass.charAt(0) === 'h' ?
            titleClass.substr(1) :
            'h' + titleClass;
        g.selectAll('.' + otherClass + ',.' + otherClass + '-math-group').remove();

        Titles.draw(gd, titleClass, extendFlat(dfltTitleOpts, titleOpts || {}));
    }

    function drawDummyTitle() {
        if(['top', 'bottom'].indexOf(titleSide) !== -1) {
            // draw the title so we know how much room it needs
            // when we squish the axis. This one only applies to
            // top or bottom titles, not right side.
            var x = gs.l + (opts.x + xpadFrac) * gs.w;
            var fontSize = ax.title.font.size;
            var y;

            if(titleSide === 'top') {
                y = (1 - (yBottomFrac + lenFrac - ypadFrac)) * gs.h +
                    gs.t + 3 + fontSize * 0.75;
            } else {
                y = (1 - (yBottomFrac + ypadFrac)) * gs.h +
                    gs.t - 3 - fontSize * 0.25;
            }
            drawTitle(ax._id + 'title', {
                attributes: {x: x, y: y, 'text-anchor': 'start'}
            });
        }
    }

    function drawCbTitle() {
        if(['top', 'bottom'].indexOf(titleSide) === -1) {
            var fontSize = ax.title.font.size;
            var y = ax._offset + ax._length / 2;
            var x = gs.l + (ax.position || 0) * gs.w + ((ax.side === 'right') ?
                10 + fontSize * ((ax.showticklabels ? 1 : 0.5)) :
                -10 - fontSize * ((ax.showticklabels ? 0.5 : 0)));

            // the 'h' + is a hack to get around the fact that
            // convertToTspans rotates any 'y...' class by 90 degrees.
            // TODO: find a better way to control this.
            drawTitle('h' + ax._id + 'title', {
                avoid: {
                    selection: d3.select(gd).selectAll('g.' + ax._id + 'tick'),
                    side: titleSide,
                    offsetLeft: gs.l,
                    offsetTop: 0,
                    maxShift: fullLayout.width
                },
                attributes: {x: x, y: y, 'text-anchor': 'middle'},
                transform: {rotate: '-90', offset: 0}
            });
        }
    }

    function drawAxis() {
        if(['top', 'bottom'].indexOf(titleSide) !== -1) {
            // squish the axis top to make room for the title
            var titleGroup = g.select('.' + cn.cbtitle);
            var titleText = titleGroup.select('text');
            var titleTrans = [-opts.outlinewidth / 2, opts.outlinewidth / 2];
            var mathJaxNode = titleGroup
                .select('.h' + ax._id + 'title-math-group')
                .node();
            var lineSize = 15.6;
            if(titleText.node()) {
                lineSize = parseInt(titleText.node().style.fontSize, 10) * LINE_SPACING;
            }
            if(mathJaxNode) {
                titleHeight = Drawing.bBox(mathJaxNode).height;
                if(titleHeight > lineSize) {
                    // not entirely sure how mathjax is doing
                    // vertical alignment, but this seems to work.
                    titleTrans[1] -= (titleHeight - lineSize) / 2;
                }
            } else if(titleText.node() && !titleText.classed(cn.jsPlaceholder)) {
                titleHeight = Drawing.bBox(titleText.node()).height;
            }
            if(titleHeight) {
                // buffer btwn colorbar and title
                // TODO: configurable
                titleHeight += 5;

                if(titleSide === 'top') {
                    ax.domain[1] -= titleHeight / gs.h;
                    titleTrans[1] *= -1;
                } else {
                    ax.domain[0] += titleHeight / gs.h;
                    var nlines = svgTextUtils.lineCount(titleText);
                    titleTrans[1] += (1 - nlines) * lineSize;
                }

                titleGroup.attr('transform', 'translate(' + titleTrans + ')');
                ax.setScale();
            }
        }

        g.selectAll('.' + cn.cbfills + ',.' + cn.cblines)
            .attr('transform', 'translate(0,' + Math.round(gs.h * (1 - ax.domain[1])) + ')');

        axLayer.attr('transform', 'translate(0,' + Math.round(-gs.t) + ')');

        var fills = g.select('.' + cn.cbfills)
            .selectAll('rect.' + cn.cbfill)
            .data(fillLevels);
        fills.enter().append('rect')
            .classed(cn.cbfill, true)
            .style('stroke', 'none');
        fills.exit().remove();

        var zBounds = zrange
            .map(ax.c2p)
            .map(Math.round)
            .sort(function(a, b) { return a - b; });

        fills.each(function(d, i) {
            var z = [
                (i === 0) ? zrange[0] : (fillLevels[i] + fillLevels[i - 1]) / 2,
                (i === fillLevels.length - 1) ? zrange[1] : (fillLevels[i] + fillLevels[i + 1]) / 2
            ]
            .map(ax.c2p)
            .map(Math.round);

            // offset the side adjoining the next rectangle so they
            // overlap, to prevent antialiasing gaps
            z[1] = Lib.constrain(z[1] + (z[1] > z[0]) ? 1 : -1, zBounds[0], zBounds[1]);


            // Colorbar cannot currently support opacities so we
            // use an opaque fill even when alpha channels present
            var fillEl = d3.select(this).attr({
                x: xLeft,
                width: Math.max(thickPx, 2),
                y: d3.min(z),
                height: Math.max(d3.max(z) - d3.min(z), 2),
            });

            if(opts._fillgradient) {
                Drawing.gradient(fillEl, gd, opts._id, 'vertical', opts._fillgradient, 'fill');
            } else {
                // tinycolor can't handle exponents and
                // at this scale, removing it makes no difference.
                var colorString = fillColormap(d).replace('e-', '');
                fillEl.attr('fill', tinycolor(colorString).toHexString());
            }
        });

        var lines = g.select('.' + cn.cblines)
            .selectAll('path.' + cn.cbline)
            .data(line.color && line.width ? lineLevels : []);
        lines.enter().append('path')
            .classed(cn.cbline, true);
        lines.exit().remove();
        lines.each(function(d) {
            d3.select(this)
                .attr('d', 'M' + xLeft + ',' +
                    (Math.round(ax.c2p(d)) + (line.width / 2) % 1) + 'h' + thickPx)
                .call(Drawing.lineGroupStyle, line.width, lineColormap(d), line.dash);
        });

        // force full redraw of labels and ticks
        axLayer.selectAll('g.' + ax._id + 'tick,path').remove();

        var shift = xLeft + thickPx +
            (opts.outlinewidth || 0) / 2 - (opts.ticks === 'outside' ? 1 : 0);

        var vals = Axes.calcTicks(ax);
        var transFn = Axes.makeTransFn(ax);
        var tickSign = Axes.getTickSigns(ax)[2];

        Axes.drawTicks(gd, ax, {
            vals: ax.ticks === 'inside' ? Axes.clipEnds(ax, vals) : vals,
            layer: axLayer,
            path: Axes.makeTickPath(ax, shift, tickSign),
            transFn: transFn
        });

        return Axes.drawLabels(gd, ax, {
            vals: vals,
            layer: axLayer,
            transFn: transFn,
            labelFns: Axes.makeLabelFns(ax, shift)
        });
    }

    // wait for the axis & title to finish rendering before
    // continuing positioning
    // TODO: why are we redrawing multiple times now with this?
    // I guess autoMargin doesn't like being post-promise?
    function positionCB() {
        var innerWidth = thickPx + opts.outlinewidth / 2 + Drawing.bBox(axLayer.node()).width;
        titleEl = titleCont.select('text');

        if(titleEl.node() && !titleEl.classed(cn.jsPlaceholder)) {
            var mathJaxNode = titleCont.select('.h' + ax._id + 'title-math-group').node();
            var titleWidth;
            if(mathJaxNode && ['top', 'bottom'].indexOf(titleSide) !== -1) {
                titleWidth = Drawing.bBox(mathJaxNode).width;
            } else {
                // note: the formula below works for all title sides,
                // (except for top/bottom mathjax, above)
                // but the weird gs.l is because the titleunshift
                // transform gets removed by Drawing.bBox
                titleWidth = Drawing.bBox(titleCont.node()).right - xLeft - gs.l;
            }
            innerWidth = Math.max(innerWidth, titleWidth);
        }

        var outerwidth = 2 * opts.xpad + innerWidth + opts.borderwidth + opts.outlinewidth / 2;
        var outerheight = yBottomPx - yTopPx;

        g.select('.' + cn.cbbg).attr({
            x: xLeft - opts.xpad - (opts.borderwidth + opts.outlinewidth) / 2,
            y: yTopPx - yExtraPx,
            width: Math.max(outerwidth, 2),
            height: Math.max(outerheight + 2 * yExtraPx, 2)
        })
        .call(Color.fill, opts.bgcolor)
        .call(Color.stroke, opts.bordercolor)
        .style('stroke-width', opts.borderwidth);

        g.selectAll('.' + cn.cboutline).attr({
            x: xLeft,
            y: yTopPx + opts.ypad + (titleSide === 'top' ? titleHeight : 0),
            width: Math.max(thickPx, 2),
            height: Math.max(outerheight - 2 * opts.ypad - titleHeight, 2)
        })
        .call(Color.stroke, opts.outlinecolor)
        .style({
            fill: 'none',
            'stroke-width': opts.outlinewidth
        });

        // fix positioning for xanchor!='left'
        var xoffset = ({center: 0.5, right: 1}[opts.xanchor] || 0) * outerwidth;
        g.attr('transform', 'translate(' + (gs.l - xoffset) + ',' + gs.t + ')');

        // auto margin adjustment
        var marginOpts = {};
        var tFrac = FROM_TL[opts.yanchor];
        var bFrac = FROM_BR[opts.yanchor];
        if(opts.lenmode === 'pixels') {
            marginOpts.y = opts.y;
            marginOpts.t = outerheight * tFrac;
            marginOpts.b = outerheight * bFrac;
        } else {
            marginOpts.t = marginOpts.b = 0;
            marginOpts.yt = opts.y + opts.len * tFrac;
            marginOpts.yb = opts.y - opts.len * bFrac;
        }

        var lFrac = FROM_TL[opts.xanchor];
        var rFrac = FROM_BR[opts.xanchor];
        if(opts.thicknessmode === 'pixels') {
            marginOpts.x = opts.x;
            marginOpts.l = outerwidth * lFrac;
            marginOpts.r = outerwidth * rFrac;
        } else {
            var extraThickness = outerwidth - thickPx;
            marginOpts.l = extraThickness * lFrac;
            marginOpts.r = extraThickness * rFrac;
            marginOpts.xl = opts.x - opts.thickness * lFrac;
            marginOpts.xr = opts.x + opts.thickness * rFrac;
        }

        Plots.autoMargin(gd, opts._id, marginOpts);
    }

    return Lib.syncOrAsync([
        Plots.previousPromises,
        drawDummyTitle,
        drawAxis,
        drawCbTitle,
        Plots.previousPromises,
        positionCB
    ], gd);
}

function makeEditable(g, opts, gd) {
    var fullLayout = gd._fullLayout;
    var gs = fullLayout._size;
    var t0, xf, yf;

    dragElement.init({
        element: g.node(),
        gd: gd,
        prepFn: function() {
            t0 = g.attr('transform');
            setCursor(g);
        },
        moveFn: function(dx, dy) {
            g.attr('transform', t0 + ' ' + 'translate(' + dx + ',' + dy + ')');

            xf = dragElement.align(opts._xLeftFrac + (dx / gs.w), opts._thickFrac,
                0, 1, opts.xanchor);
            yf = dragElement.align(opts._yBottomFrac - (dy / gs.h), opts._lenFrac,
                0, 1, opts.yanchor);

            var csr = dragElement.getCursor(xf, yf, opts.xanchor, opts.yanchor);
            setCursor(g, csr);
        },
        doneFn: function() {
            setCursor(g);

            if(xf !== undefined && yf !== undefined) {
                var update = {};
                update[opts._propPrefix + 'x'] = xf;
                update[opts._propPrefix + 'y'] = yf;
                if(opts._traceIndex !== undefined) {
                    Registry.call('_guiRestyle', gd, update, opts._traceIndex);
                } else {
                    Registry.call('_guiRelayout', gd, update);
                }
            }
        }
    });
}

function calcLevels(gd, opts, zrange) {
    var levelsIn = opts._levels;
    var lineLevels = [];
    var fillLevels = [];
    var l;
    var i;

    var l0 = levelsIn.end + levelsIn.size / 100;
    var ls = levelsIn.size;
    var zr0 = (1.001 * zrange[0] - 0.001 * zrange[1]);
    var zr1 = (1.001 * zrange[1] - 0.001 * zrange[0]);

    for(i = 0; i < 1e5; i++) {
        l = levelsIn.start + i * ls;
        if(ls > 0 ? (l >= l0) : (l <= l0)) break;
        if(l > zr0 && l < zr1) lineLevels.push(l);
    }

    if(opts._fillgradient) {
        fillLevels = [0];
    } else if(typeof opts._fillcolor === 'function') {
        var fillLevelsIn = opts._filllevels;

        if(fillLevelsIn) {
            l0 = fillLevelsIn.end + fillLevelsIn.size / 100;
            ls = fillLevelsIn.size;
            for(i = 0; i < 1e5; i++) {
                l = fillLevelsIn.start + i * ls;
                if(ls > 0 ? (l >= l0) : (l <= l0)) break;
                if(l > zrange[0] && l < zrange[1]) fillLevels.push(l);
            }
        } else {
            fillLevels = lineLevels.map(function(v) {
                return v - levelsIn.size / 2;
            });
            fillLevels.push(fillLevels[fillLevels.length - 1] + levelsIn.size);
        }
    } else if(opts._fillcolor && typeof opts._fillcolor === 'string') {
        // doesn't matter what this value is, with a single value
        // we'll make a single fill rect covering the whole bar
        fillLevels = [0];
    }

    if(levelsIn.size < 0) {
        lineLevels.reverse();
        fillLevels.reverse();
    }

    return {line: lineLevels, fill: fillLevels};
}

function mockColorBarAxis(gd, opts, zrange) {
    var fullLayout = gd._fullLayout;

    var cbAxisIn = {
        type: 'linear',
        range: zrange,
        tickmode: opts.tickmode,
        nticks: opts.nticks,
        tick0: opts.tick0,
        dtick: opts.dtick,
        tickvals: opts.tickvals,
        ticktext: opts.ticktext,
        ticks: opts.ticks,
        ticklen: opts.ticklen,
        tickwidth: opts.tickwidth,
        tickcolor: opts.tickcolor,
        showticklabels: opts.showticklabels,
        tickfont: opts.tickfont,
        tickangle: opts.tickangle,
        tickformat: opts.tickformat,
        exponentformat: opts.exponentformat,
        separatethousands: opts.separatethousands,
        showexponent: opts.showexponent,
        showtickprefix: opts.showtickprefix,
        tickprefix: opts.tickprefix,
        showticksuffix: opts.showticksuffix,
        ticksuffix: opts.ticksuffix,
        title: opts.title,
        showline: true,
        anchor: 'free',
        side: 'right',
        position: 1
    };

    var cbAxisOut = {
        type: 'linear',
        _id: 'y' + opts._id
    };

    var axisOptions = {
        letter: 'y',
        font: fullLayout.font,
        noHover: true,
        noTickson: true,
        calendar: fullLayout.calendar  // not really necessary (yet?)
    };

    function coerce(attr, dflt) {
        return Lib.coerce(cbAxisIn, cbAxisOut, axisLayoutAttrs, attr, dflt);
    }

    handleAxisDefaults(cbAxisIn, cbAxisOut, coerce, axisOptions, fullLayout);
    handleAxisPositionDefaults(cbAxisIn, cbAxisOut, coerce, axisOptions);

    return cbAxisOut;
}

module.exports = {
    draw: draw
};
