/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var Lib = require('../../lib');
var Plots = require('../../plots/plots');
var Registry = require('../../registry');
var Events = require('../../lib/events');
var dragElement = require('../dragelement');
var Drawing = require('../drawing');
var Color = require('../color');
var svgTextUtils = require('../../lib/svg_text_utils');
var handleClick = require('./handle_click');

var constants = require('./constants');
var interactConstants = require('../../constants/interactions');
var alignmentConstants = require('../../constants/alignment');
var LINE_SPACING = alignmentConstants.LINE_SPACING;
var FROM_TL = alignmentConstants.FROM_TL;
var FROM_BR = alignmentConstants.FROM_BR;

var getLegendData = require('./get_legend_data');
var style = require('./style');
var helpers = require('./helpers');

var DBLCLICKDELAY = interactConstants.DBLCLICKDELAY;

module.exports = function draw(gd) {
    var fullLayout = gd._fullLayout;
    var clipId = 'legend' + fullLayout._uid;

    if(!fullLayout._infolayer || !gd.calcdata) return;

    if(!gd._legendMouseDownTime) gd._legendMouseDownTime = 0;

    var opts = fullLayout.legend;
    var legendData = fullLayout.showlegend && getLegendData(gd.calcdata, opts);
    var hiddenSlices = fullLayout.hiddenlabels || [];

    if(!fullLayout.showlegend || !legendData.length) {
        fullLayout._infolayer.selectAll('.legend').remove();
        fullLayout._topdefs.select('#' + clipId).remove();

        Plots.autoMargin(gd, 'legend');
        return;
    }

    var maxLength = 0;
    for(var i = 0; i < legendData.length; i++) {
        for(var j = 0; j < legendData[i].length; j++) {
            var item = legendData[i][j][0];
            var trace = item.trace;
            var isPieLike = Registry.traceIs(trace, 'pie-like');
            var name = isPieLike ? item.label : trace.name;
            maxLength = Math.max(maxLength, name && name.length || 0);
        }
    }

    var firstRender = false;
    var legend = Lib.ensureSingle(fullLayout._infolayer, 'g', 'legend', function(s) {
        s.attr('pointer-events', 'all');
        firstRender = true;
    });

    var clipPath = Lib.ensureSingleById(fullLayout._topdefs, 'clipPath', clipId, function(s) {
        s.append('rect');
    });

    var bg = Lib.ensureSingle(legend, 'rect', 'bg', function(s) {
        s.attr('shape-rendering', 'crispEdges');
    });

    bg.call(Color.stroke, opts.bordercolor)
        .call(Color.fill, opts.bgcolor)
        .style('stroke-width', opts.borderwidth + 'px');

    var scrollBox = Lib.ensureSingle(legend, 'g', 'scrollbox');

    var scrollBar = Lib.ensureSingle(legend, 'rect', 'scrollbar', function(s) {
        s.attr({
            rx: 20,
            ry: 3,
            width: 0,
            height: 0
        })
        .call(Color.fill, '#808BA4');
    });

    var groups = scrollBox.selectAll('g.groups')
        .data(legendData);

    groups.enter().append('g')
        .attr('class', 'groups');

    groups.exit().remove();

    var traces = groups.selectAll('g.traces')
        .data(Lib.identity);

    traces.enter().append('g').attr('class', 'traces');
    traces.exit().remove();

    traces.style('opacity', function(d) {
        var trace = d[0].trace;
        if(Registry.traceIs(trace, 'pie-like')) {
            return hiddenSlices.indexOf(d[0].label) !== -1 ? 0.5 : 1;
        } else {
            return trace.visible === 'legendonly' ? 0.5 : 1;
        }
    })
    .each(function() {
        d3.select(this)
            .call(drawTexts, gd, maxLength);
    })
    .call(style, gd)
    .each(function() {
        d3.select(this)
            .call(setupTraceToggle, gd);
    });

    Lib.syncOrAsync([Plots.previousPromises,
        function() {
            if(firstRender) {
                computeLegendDimensions(gd, groups, traces);
                expandMargin(gd);
            }

            // Position and size the legend
            var lxMin = 0;
            var lxMax = fullLayout.width;
            var lyMin = 0;
            var lyMax = fullLayout.height;

            computeLegendDimensions(gd, groups, traces);

            if(opts._height > lyMax) {
                // If the legend doesn't fit in the plot area,
                // do not expand the vertical margins.
                expandHorizontalMargin(gd);
            } else {
                expandMargin(gd);
            }

            // Scroll section must be executed after repositionLegend.
            // It requires the legend width, height, x and y to position the scrollbox
            // and these values are mutated in repositionLegend.
            var gs = fullLayout._size;
            var lx = gs.l + gs.w * opts.x;
            var ly = gs.t + gs.h * (1 - opts.y);

            if(Lib.isRightAnchor(opts)) {
                lx -= opts._width;
            } else if(Lib.isCenterAnchor(opts)) {
                lx -= opts._width / 2;
            }

            if(Lib.isBottomAnchor(opts)) {
                ly -= opts._height;
            } else if(Lib.isMiddleAnchor(opts)) {
                ly -= opts._height / 2;
            }

            // Make sure the legend left and right sides are visible
            var legendWidth = opts._width;
            var legendWidthMax = gs.w;

            if(legendWidth > legendWidthMax) {
                lx = gs.l;
                legendWidth = legendWidthMax;
            } else {
                if(lx + legendWidth > lxMax) lx = lxMax - legendWidth;
                if(lx < lxMin) lx = lxMin;
                legendWidth = Math.min(lxMax - lx, opts._width);
            }

            // Make sure the legend top and bottom are visible
            // (legends with a scroll bar are not allowed to stretch beyond the extended
            // margins)
            var legendHeight = opts._height;
            var legendHeightMax = gs.h;

            if(legendHeight > legendHeightMax) {
                ly = gs.t;
                legendHeight = legendHeightMax;
            } else {
                if(ly + legendHeight > lyMax) ly = lyMax - legendHeight;
                if(ly < lyMin) ly = lyMin;
                legendHeight = Math.min(lyMax - ly, opts._height);
            }

            // Set size and position of all the elements that make up a legend:
            // legend, background and border, scroll box and scroll bar
            Drawing.setTranslate(legend, lx, ly);

            // to be safe, remove previous listeners
            scrollBar.on('.drag', null);
            legend.on('wheel', null);

            if(opts._height <= legendHeight || gd._context.staticPlot) {
                // if scrollbar should not be shown.
                bg.attr({
                    width: legendWidth - opts.borderwidth,
                    height: legendHeight - opts.borderwidth,
                    x: opts.borderwidth / 2,
                    y: opts.borderwidth / 2
                });

                Drawing.setTranslate(scrollBox, 0, 0);

                clipPath.select('rect').attr({
                    width: legendWidth - 2 * opts.borderwidth,
                    height: legendHeight - 2 * opts.borderwidth,
                    x: opts.borderwidth,
                    y: opts.borderwidth
                });

                Drawing.setClipUrl(scrollBox, clipId, gd);

                Drawing.setRect(scrollBar, 0, 0, 0, 0);
                delete opts._scrollY;
            } else {
                var scrollBarHeight = Math.max(constants.scrollBarMinHeight,
                    legendHeight * legendHeight / opts._height);
                var scrollBarYMax = legendHeight -
                    scrollBarHeight -
                    2 * constants.scrollBarMargin;
                var scrollBoxYMax = opts._height - legendHeight;
                var scrollRatio = scrollBarYMax / scrollBoxYMax;

                var scrollBoxY = Math.min(opts._scrollY || 0, scrollBoxYMax);

                // increase the background and clip-path width
                // by the scrollbar width and margin
                bg.attr({
                    width: legendWidth -
                        2 * opts.borderwidth +
                        constants.scrollBarWidth +
                        constants.scrollBarMargin,
                    height: legendHeight - opts.borderwidth,
                    x: opts.borderwidth / 2,
                    y: opts.borderwidth / 2
                });

                clipPath.select('rect').attr({
                    width: legendWidth -
                        2 * opts.borderwidth +
                        constants.scrollBarWidth +
                        constants.scrollBarMargin,
                    height: legendHeight - 2 * opts.borderwidth,
                    x: opts.borderwidth,
                    y: opts.borderwidth + scrollBoxY
                });

                Drawing.setClipUrl(scrollBox, clipId, gd);

                scrollHandler(scrollBoxY, scrollBarHeight, scrollRatio);

                legend.on('wheel', function() {
                    scrollBoxY = Lib.constrain(
                        opts._scrollY +
                            d3.event.deltaY / scrollBarYMax * scrollBoxYMax,
                        0, scrollBoxYMax);
                    scrollHandler(scrollBoxY, scrollBarHeight, scrollRatio);
                    if(scrollBoxY !== 0 && scrollBoxY !== scrollBoxYMax) {
                        d3.event.preventDefault();
                    }
                });

                var eventY0, scrollBoxY0;

                var drag = d3.behavior.drag()
                .on('dragstart', function() {
                    eventY0 = d3.event.sourceEvent.clientY;
                    scrollBoxY0 = scrollBoxY;
                })
                .on('drag', function() {
                    var e = d3.event.sourceEvent;
                    if(e.buttons === 2 || e.ctrlKey) return;

                    scrollBoxY = Lib.constrain(
                        (e.clientY - eventY0) / scrollRatio + scrollBoxY0,
                        0, scrollBoxYMax);
                    scrollHandler(scrollBoxY, scrollBarHeight, scrollRatio);
                });

                scrollBar.call(drag);
            }


            function scrollHandler(scrollBoxY, scrollBarHeight, scrollRatio) {
                opts._scrollY = gd._fullLayout.legend._scrollY = scrollBoxY;
                Drawing.setTranslate(scrollBox, 0, -scrollBoxY);

                Drawing.setRect(
                    scrollBar,
                    legendWidth,
                    constants.scrollBarMargin + scrollBoxY * scrollRatio,
                    constants.scrollBarWidth,
                    scrollBarHeight
                );
                clipPath.select('rect').attr({
                    y: opts.borderwidth + scrollBoxY
                });
            }

            if(gd._context.edits.legendPosition) {
                var xf, yf, x0, y0;

                legend.classed('cursor-move', true);

                dragElement.init({
                    element: legend.node(),
                    gd: gd,
                    prepFn: function() {
                        var transform = Drawing.getTranslate(legend);

                        x0 = transform.x;
                        y0 = transform.y;
                    },
                    moveFn: function(dx, dy) {
                        var newX = x0 + dx;
                        var newY = y0 + dy;

                        Drawing.setTranslate(legend, newX, newY);

                        xf = dragElement.align(newX, 0, gs.l, gs.l + gs.w, opts.xanchor);
                        yf = dragElement.align(newY, 0, gs.t + gs.h, gs.t, opts.yanchor);
                    },
                    doneFn: function() {
                        if(xf !== undefined && yf !== undefined) {
                            Registry.call('_guiRelayout', gd, {'legend.x': xf, 'legend.y': yf});
                        }
                    },
                    clickFn: function(numClicks, e) {
                        var clickedTrace = fullLayout._infolayer.selectAll('g.traces').filter(function() {
                            var bbox = this.getBoundingClientRect();
                            return (
                                e.clientX >= bbox.left && e.clientX <= bbox.right &&
                                e.clientY >= bbox.top && e.clientY <= bbox.bottom
                            );
                        });
                        if(clickedTrace.size() > 0) {
                            clickOrDoubleClick(gd, legend, clickedTrace, numClicks, e);
                        }
                    }
                });
            }
        }], gd);
};

function clickOrDoubleClick(gd, legend, legendItem, numClicks, evt) {
    var trace = legendItem.data()[0][0].trace;

    var evtData = {
        event: evt,
        node: legendItem.node(),
        curveNumber: trace.index,
        expandedIndex: trace._expandedIndex,
        data: gd.data,
        layout: gd.layout,
        frames: gd._transitionData._frames,
        config: gd._context,
        fullData: gd._fullData,
        fullLayout: gd._fullLayout
    };

    if(trace._group) {
        evtData.group = trace._group;
    }
    if(Registry.traceIs(trace, 'pie-like')) {
        evtData.label = legendItem.datum()[0].label;
    }

    var clickVal = Events.triggerHandler(gd, 'plotly_legendclick', evtData);
    if(clickVal === false) return;

    if(numClicks === 1) {
        legend._clickTimeout = setTimeout(function() {
            handleClick(legendItem, gd, numClicks);
        }, DBLCLICKDELAY);
    } else if(numClicks === 2) {
        if(legend._clickTimeout) clearTimeout(legend._clickTimeout);
        gd._legendMouseDownTime = 0;

        var dblClickVal = Events.triggerHandler(gd, 'plotly_legenddoubleclick', evtData);
        if(dblClickVal !== false) handleClick(legendItem, gd, numClicks);
    }
}

function drawTexts(g, gd, maxLength) {
    var legendItem = g.data()[0][0];
    var fullLayout = gd._fullLayout;
    var trace = legendItem.trace;
    var isPieLike = Registry.traceIs(trace, 'pie-like');
    var traceIndex = trace.index;
    var isEditable = gd._context.edits.legendText && !isPieLike;

    var name = isPieLike ? legendItem.label : trace.name;
    if(trace._meta) {
        name = Lib.templateString(name, trace._meta);
    }

    var textEl = Lib.ensureSingle(g, 'text', 'legendtext');

    textEl.attr('text-anchor', 'start')
        .classed('user-select-none', true)
        .call(Drawing.font, fullLayout.legend.font)
        .text(isEditable ? ensureLength(name, maxLength) : name);

    svgTextUtils.positionText(textEl, constants.textOffsetX, 0);

    function textLayout(s) {
        svgTextUtils.convertToTspans(s, gd, function() {
            computeTextDimensions(g, gd);
        });
    }

    if(isEditable) {
        textEl.call(svgTextUtils.makeEditable, {gd: gd, text: name})
            .call(textLayout)
            .on('edit', function(newName) {
                this.text(ensureLength(newName, maxLength))
                    .call(textLayout);

                var fullInput = legendItem.trace._fullInput || {};
                var update = {};

                if(Registry.hasTransform(fullInput, 'groupby')) {
                    var groupbyIndices = Registry.getTransformIndices(fullInput, 'groupby');
                    var index = groupbyIndices[groupbyIndices.length - 1];

                    var kcont = Lib.keyedContainer(fullInput, 'transforms[' + index + '].styles', 'target', 'value.name');

                    kcont.set(legendItem.trace._group, newName);

                    update = kcont.constructUpdate();
                } else {
                    update.name = newName;
                }

                return Registry.call('_guiRestyle', gd, update, traceIndex);
            });
    } else {
        textLayout(textEl);
    }
}

/*
 * Make sure we have a reasonably clickable region.
 * If this string is missing or very short, pad it with spaces out to at least
 * 4 characters, up to the max length of other labels, on the assumption that
 * most characters are wider than spaces so a string of spaces will usually be
 * no wider than the real labels.
 */
function ensureLength(str, maxLength) {
    var targetLength = Math.max(4, maxLength);
    if(str && str.trim().length >= targetLength / 2) return str;
    str = str || '';
    for(var i = targetLength - str.length; i > 0; i--) str += ' ';
    return str;
}

function setupTraceToggle(g, gd) {
    var newMouseDownTime;
    var numClicks = 1;

    var traceToggle = Lib.ensureSingle(g, 'rect', 'legendtoggle', function(s) {
        s.style('cursor', 'pointer')
            .attr('pointer-events', 'all')
            .call(Color.fill, 'rgba(0,0,0,0)');
    });

    traceToggle.on('mousedown', function() {
        newMouseDownTime = (new Date()).getTime();
        if(newMouseDownTime - gd._legendMouseDownTime < DBLCLICKDELAY) {
            // in a click train
            numClicks += 1;
        } else {
            // new click train
            numClicks = 1;
            gd._legendMouseDownTime = newMouseDownTime;
        }
    });
    traceToggle.on('mouseup', function() {
        if(gd._dragged || gd._editing) return;
        var legend = gd._fullLayout.legend;

        if((new Date()).getTime() - gd._legendMouseDownTime > DBLCLICKDELAY) {
            numClicks = Math.max(numClicks - 1, 1);
        }

        clickOrDoubleClick(gd, legend, g, numClicks, d3.event);
    });
}

function computeTextDimensions(g, gd) {
    var legendItem = g.data()[0][0];

    if(!legendItem.trace.showlegend) {
        g.remove();
        return;
    }

    var mathjaxGroup = g.select('g[class*=math-group]');
    var mathjaxNode = mathjaxGroup.node();
    var opts = gd._fullLayout.legend;
    var lineHeight = opts.font.size * LINE_SPACING;
    var height, width;

    if(mathjaxNode) {
        var mathjaxBB = Drawing.bBox(mathjaxNode);

        height = mathjaxBB.height;
        width = mathjaxBB.width;

        Drawing.setTranslate(mathjaxGroup, 0, (height / 4));
    } else {
        var text = g.select('.legendtext');
        var textLines = svgTextUtils.lineCount(text);
        var textNode = text.node();

        height = lineHeight * textLines;
        width = textNode ? Drawing.bBox(textNode).width : 0;

        // approximation to height offset to center the font
        // to avoid getBoundingClientRect
        var textY = lineHeight * (0.3 + (1 - textLines) / 2);
        svgTextUtils.positionText(text, constants.textOffsetX, textY);
    }

    legendItem.lineHeight = lineHeight;
    legendItem.height = Math.max(height, 16) + 3;
    legendItem.width = width;
}

function computeLegendDimensions(gd, groups, traces) {
    var fullLayout = gd._fullLayout;
    var opts = fullLayout.legend;
    var borderwidth = opts.borderwidth;
    var isGrouped = helpers.isGrouped(opts);

    var extraWidth = 0;

    var traceGap = 5;

    opts._width = 0;
    opts._height = 0;

    if(helpers.isVertical(opts)) {
        if(isGrouped) {
            groups.each(function(d, i) {
                Drawing.setTranslate(this, 0, i * opts.tracegroupgap);
            });
        }

        traces.each(function(d) {
            var legendItem = d[0];
            var textHeight = legendItem.height;
            var textWidth = legendItem.width;

            Drawing.setTranslate(this,
                borderwidth,
                (5 + borderwidth + opts._height + textHeight / 2));

            opts._height += textHeight;
            opts._width = Math.max(opts._width, textWidth);
        });

        opts._width += 45 + borderwidth * 2;
        opts._height += 10 + borderwidth * 2;

        if(isGrouped) {
            opts._height += (opts._lgroupsLength - 1) * opts.tracegroupgap;
        }

        extraWidth = 40;
    } else if(isGrouped) {
        var maxHeight = 0;
        var maxWidth = 0;
        var groupData = groups.data();

        var maxItems = 0;

        var i;
        for(i = 0; i < groupData.length; i++) {
            var group = groupData[i];
            var groupWidths = group.map(function(legendItemArray) {
                return legendItemArray[0].width;
            });

            var groupWidth = Lib.aggNums(Math.max, null, groupWidths);
            var groupHeight = group.reduce(function(a, b) {
                return a + b[0].height;
            }, 0);

            maxWidth = Math.max(maxWidth, groupWidth);
            maxHeight = Math.max(maxHeight, groupHeight);
            maxItems = Math.max(maxItems, group.length);
        }

        maxWidth += traceGap;
        maxWidth += 40;

        var groupXOffsets = [opts._width];
        var groupYOffsets = [];
        var rowNum = 0;
        for(i = 0; i < groupData.length; i++) {
            if(fullLayout._size.w < (borderwidth + opts._width + traceGap + maxWidth)) {
                groupXOffsets[groupXOffsets.length - 1] = groupXOffsets[0];
                opts._width = maxWidth;
                rowNum++;
            } else {
                opts._width += maxWidth + borderwidth;
            }

            var rowYOffset = (rowNum * maxHeight);
            rowYOffset += rowNum > 0 ? opts.tracegroupgap : 0;

            groupYOffsets.push(rowYOffset);
            groupXOffsets.push(opts._width);
        }

        groups.each(function(d, i) {
            Drawing.setTranslate(this, groupXOffsets[i], groupYOffsets[i]);
        });

        groups.each(function() {
            var group = d3.select(this);
            var groupTraces = group.selectAll('g.traces');
            var groupHeight = 0;

            groupTraces.each(function(d) {
                var legendItem = d[0];
                var textHeight = legendItem.height;

                Drawing.setTranslate(this,
                    0,
                    (5 + borderwidth + groupHeight + textHeight / 2));

                groupHeight += textHeight;
            });
        });

        var maxYLegend = groupYOffsets[groupYOffsets.length - 1] + maxHeight;
        opts._height = 10 + (borderwidth * 2) + maxYLegend;

        var maxOffset = Math.max.apply(null, groupXOffsets);
        opts._width = maxOffset + maxWidth + 40;
        opts._width += borderwidth * 2;
    } else {
        var rowHeight = 0;
        var maxTraceHeight = 0;
        var maxTraceWidth = 0;
        var offsetX = 0;
        var fullTracesWidth = 0;

        // calculate largest width for traces and use for width of all legend items
        traces.each(function(d) {
            maxTraceWidth = Math.max(40 + d[0].width, maxTraceWidth);
            fullTracesWidth += 40 + d[0].width + traceGap;
        });

        // check if legend fits in one row
        var oneRowLegend = fullLayout._size.w > borderwidth + fullTracesWidth - traceGap;

        traces.each(function(d) {
            var legendItem = d[0];
            var traceWidth = oneRowLegend ? 40 + d[0].width : maxTraceWidth;

            if((borderwidth + offsetX + traceGap + traceWidth) > fullLayout._size.w) {
                offsetX = 0;
                rowHeight += maxTraceHeight;
                opts._height += maxTraceHeight;
                // reset for next row
                maxTraceHeight = 0;
            }

            Drawing.setTranslate(this,
                (borderwidth + offsetX),
                (5 + borderwidth + legendItem.height / 2) + rowHeight);

            opts._width += traceGap + traceWidth;

            // keep track of tallest trace in group
            offsetX += traceGap + traceWidth;
            maxTraceHeight = Math.max(legendItem.height, maxTraceHeight);
        });

        if(oneRowLegend) {
            opts._height = maxTraceHeight;
        } else {
            opts._height += maxTraceHeight;
        }

        opts._width += borderwidth * 2;
        opts._height += 10 + borderwidth * 2;
    }

    // make sure we're only getting full pixels
    opts._width = Math.ceil(opts._width);
    opts._height = Math.ceil(opts._height);

    var isEditable = (
        gd._context.edits.legendText ||
        gd._context.edits.legendPosition
    );

    traces.each(function(d) {
        var legendItem = d[0];
        var bg = d3.select(this).select('.legendtoggle');

        Drawing.setRect(bg,
            0,
            -legendItem.height / 2,
            (isEditable ? 0 : opts._width) + extraWidth,
            legendItem.height
        );
    });
}

function expandMargin(gd) {
    var fullLayout = gd._fullLayout;
    var opts = fullLayout.legend;

    var xanchor = 'left';
    if(Lib.isRightAnchor(opts)) {
        xanchor = 'right';
    } else if(Lib.isCenterAnchor(opts)) {
        xanchor = 'center';
    }

    var yanchor = 'top';
    if(Lib.isBottomAnchor(opts)) {
        yanchor = 'bottom';
    } else if(Lib.isMiddleAnchor(opts)) {
        yanchor = 'middle';
    }

    // lastly check if the margin auto-expand has changed
    Plots.autoMargin(gd, 'legend', {
        x: opts.x,
        y: opts.y,
        l: opts._width * (FROM_TL[xanchor]),
        r: opts._width * (FROM_BR[xanchor]),
        b: opts._height * (FROM_BR[yanchor]),
        t: opts._height * (FROM_TL[yanchor])
    });
}

function expandHorizontalMargin(gd) {
    var fullLayout = gd._fullLayout;
    var opts = fullLayout.legend;

    var xanchor = 'left';
    if(Lib.isRightAnchor(opts)) {
        xanchor = 'right';
    } else if(Lib.isCenterAnchor(opts)) {
        xanchor = 'center';
    }

    // lastly check if the margin auto-expand has changed
    Plots.autoMargin(gd, 'legend', {
        x: opts.x,
        y: 0.5,
        l: opts._width * (FROM_TL[xanchor]),
        r: opts._width * (FROM_BR[xanchor]),
        b: 0,
        t: 0
    });
}
