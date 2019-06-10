/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var c = require('./constants');
var d3 = require('d3');
var gup = require('../../lib/gup');
var Drawing = require('../../components/drawing');
var svgUtil = require('../../lib/svg_text_utils');
var raiseToTop = require('../../lib').raiseToTop;
var cancelEeaseColumn = require('../../lib').cancelTransition;
var prepareData = require('./data_preparation_helper');
var splitData = require('./data_split_helpers');
var Color = require('../../components/color');

module.exports = function plot(gd, wrappedTraceHolders) {
    var dynamic = !gd._context.staticPlot;

    var table = gd._fullLayout._paper.selectAll('.' + c.cn.table)
        .data(wrappedTraceHolders.map(function(wrappedTraceHolder) {
            var traceHolder = gup.unwrap(wrappedTraceHolder);
            var trace = traceHolder.trace;
            return prepareData(gd, trace);
        }), gup.keyFun);

    table.exit().remove();

    table.enter()
        .append('g')
        .classed(c.cn.table, true)
        .attr('overflow', 'visible')
        .style('box-sizing', 'content-box')
        .style('position', 'absolute')
        .style('left', 0)
        .style('overflow', 'visible')
        .style('shape-rendering', 'crispEdges')
        .style('pointer-events', 'all');

    table
        .attr('width', function(d) {return d.width + d.size.l + d.size.r;})
        .attr('height', function(d) {return d.height + d.size.t + d.size.b;})
        .attr('transform', function(d) {
            return 'translate(' + d.translateX + ',' + d.translateY + ')';
        });

    var tableControlView = table.selectAll('.' + c.cn.tableControlView)
        .data(gup.repeat, gup.keyFun);

    var cvEnter = tableControlView.enter()
        .append('g')
        .classed(c.cn.tableControlView, true)
        .style('box-sizing', 'content-box');
    if(dynamic) {
        cvEnter
            .on('mousemove', function(d) {
                tableControlView
                    .filter(function(dd) {return d === dd;})
                    .call(renderScrollbarKit, gd);
            })
            .on('mousewheel', function(d) {
                if(d.scrollbarState.wheeling) return;
                d.scrollbarState.wheeling = true;
                var newY = d.scrollY + d3.event.deltaY;
                var noChange = makeDragRow(gd, tableControlView, null, newY)(d);
                if(!noChange) {
                    d3.event.stopPropagation();
                    d3.event.preventDefault();
                }
                d.scrollbarState.wheeling = false;
            })
            .call(renderScrollbarKit, gd, true);
    }

    tableControlView
        .attr('transform', function(d) {return 'translate(' + d.size.l + ' ' + d.size.t + ')';});

    // scrollBackground merely ensures that mouse events are captured even on crazy fast scrollwheeling
    // otherwise rendering glitches may occur
    var scrollBackground = tableControlView.selectAll('.' + c.cn.scrollBackground)
        .data(gup.repeat, gup.keyFun);

    scrollBackground.enter()
        .append('rect')
        .classed(c.cn.scrollBackground, true)
        .attr('fill', 'none');

    scrollBackground
        .attr('width', function(d) {return d.width;})
        .attr('height', function(d) {return d.height;});

    tableControlView.each(function(d) {
        Drawing.setClipUrl(d3.select(this), scrollAreaBottomClipKey(gd, d), gd);
    });

    var yColumn = tableControlView.selectAll('.' + c.cn.yColumn)
        .data(function(vm) {return vm.columns;}, gup.keyFun);

    yColumn.enter()
        .append('g')
        .classed(c.cn.yColumn, true);

    yColumn.exit().remove();

    yColumn.attr('transform', function(d) {return 'translate(' + d.x + ' 0)';});

    if(dynamic) {
        yColumn.call(d3.behavior.drag()
            .origin(function(d) {
                var movedColumn = d3.select(this);
                easeColumn(movedColumn, d, -c.uplift);
                raiseToTop(this);
                d.calcdata.columnDragInProgress = true;
                renderScrollbarKit(tableControlView.filter(function(dd) {return d.calcdata.key === dd.key;}), gd);
                return d;
            })
            .on('drag', function(d) {
                var movedColumn = d3.select(this);
                var getter = function(dd) {return (d === dd ? d3.event.x : dd.x) + dd.columnWidth / 2;};
                d.x = Math.max(-c.overdrag, Math.min(d.calcdata.width + c.overdrag - d.columnWidth, d3.event.x));

                var sortableColumns = flatData(yColumn).filter(function(dd) {return dd.calcdata.key === d.calcdata.key;});
                var newOrder = sortableColumns.sort(function(a, b) {return getter(a) - getter(b);});
                newOrder.forEach(function(dd, i) {
                    dd.xIndex = i;
                    dd.x = d === dd ? dd.x : dd.xScale(dd);
                });

                yColumn.filter(function(dd) {return d !== dd;})
                    .transition()
                    .ease(c.transitionEase)
                    .duration(c.transitionDuration)
                    .attr('transform', function(d) {return 'translate(' + d.x + ' 0)';});
                movedColumn
                    .call(cancelEeaseColumn)
                    .attr('transform', 'translate(' + d.x + ' -' + c.uplift + ' )');
            })
            .on('dragend', function(d) {
                var movedColumn = d3.select(this);
                var p = d.calcdata;
                d.x = d.xScale(d);
                d.calcdata.columnDragInProgress = false;
                easeColumn(movedColumn, d, 0);
                columnMoved(gd, p, p.columns.map(function(dd) {return dd.xIndex;}));
            })
        );
    }

    yColumn.each(function(d) {
        Drawing.setClipUrl(d3.select(this), columnBoundaryClipKey(gd, d), gd);
    });

    var columnBlock = yColumn.selectAll('.' + c.cn.columnBlock)
        .data(splitData.splitToPanels, gup.keyFun);

    columnBlock.enter()
        .append('g')
        .classed(c.cn.columnBlock, true)
        .attr('id', function(d) {return d.key;});

    columnBlock
        .style('cursor', function(d) {
            return d.dragHandle ? 'ew-resize' : d.calcdata.scrollbarState.barWiggleRoom ? 'ns-resize' : 'default';
        });

    var headerColumnBlock = columnBlock.filter(headerBlock);
    var cellsColumnBlock = columnBlock.filter(cellsBlock);

    if(dynamic) {
        cellsColumnBlock.call(d3.behavior.drag()
            .origin(function(d) {
                d3.event.stopPropagation();
                return d;
            })
            .on('drag', makeDragRow(gd, tableControlView, -1))
            .on('dragend', function() {
                // fixme emit plotly notification
            })
        );
    }

    // initial rendering: header is rendered first, as it may may have async LaTeX (show header first)
    // but blocks are _entered_ the way they are due to painter's algo (header on top)
    renderColumnCellTree(gd, tableControlView, headerColumnBlock, columnBlock);
    renderColumnCellTree(gd, tableControlView, cellsColumnBlock, columnBlock);

    var scrollAreaClip = tableControlView.selectAll('.' + c.cn.scrollAreaClip)
        .data(gup.repeat, gup.keyFun);

    scrollAreaClip.enter()
        .append('clipPath')
        .classed(c.cn.scrollAreaClip, true)
        .attr('id', function(d) {return scrollAreaBottomClipKey(gd, d);});

    var scrollAreaClipRect = scrollAreaClip.selectAll('.' + c.cn.scrollAreaClipRect)
        .data(gup.repeat, gup.keyFun);

    scrollAreaClipRect.enter()
        .append('rect')
        .classed(c.cn.scrollAreaClipRect, true)
        .attr('x', -c.overdrag)
        .attr('y', -c.uplift)
        .attr('fill', 'none');

    scrollAreaClipRect
        .attr('width', function(d) {return d.width + 2 * c.overdrag;})
        .attr('height', function(d) {return d.height + c.uplift;});

    var columnBoundary = yColumn.selectAll('.' + c.cn.columnBoundary)
        .data(gup.repeat, gup.keyFun);

    columnBoundary.enter()
        .append('g')
        .classed(c.cn.columnBoundary, true);

    var columnBoundaryClippath = yColumn.selectAll('.' + c.cn.columnBoundaryClippath)
        .data(gup.repeat, gup.keyFun);

    // SVG spec doesn't mandate wrapping into a <defs> and doesn't seem to cause a speed difference
    columnBoundaryClippath.enter()
        .append('clipPath')
        .classed(c.cn.columnBoundaryClippath, true);

    columnBoundaryClippath
        .attr('id', function(d) {return columnBoundaryClipKey(gd, d);});

    var columnBoundaryRect = columnBoundaryClippath.selectAll('.' + c.cn.columnBoundaryRect)
        .data(gup.repeat, gup.keyFun);

    columnBoundaryRect.enter()
        .append('rect')
        .classed(c.cn.columnBoundaryRect, true)
        .attr('fill', 'none');

    columnBoundaryRect
        .attr('width', function(d) { return d.columnWidth + 2 * roundHalfWidth(d); })
        .attr('height', function(d) {return d.calcdata.height + 2 * roundHalfWidth(d) + c.uplift;})
        .attr('x', function(d) { return -roundHalfWidth(d); })
        .attr('y', function(d) { return -roundHalfWidth(d); });

    updateBlockYPosition(null, cellsColumnBlock, tableControlView);
};

function roundHalfWidth(d) {
    return Math.ceil(d.calcdata.maxLineWidth / 2);
}

function scrollAreaBottomClipKey(gd, d) {
    return 'clip' + gd._fullLayout._uid + '_scrollAreaBottomClip_' + d.key;
}

function columnBoundaryClipKey(gd, d) {
    return 'clip' + gd._fullLayout._uid + '_columnBoundaryClippath_' + d.calcdata.key + '_' + d.specIndex;
}

function flatData(selection) {
    return [].concat.apply([], selection.map(function(g) {return g;}))
        .map(function(g) {return g.__data__;});
}

function renderScrollbarKit(tableControlView, gd, bypassVisibleBar) {
    function calcTotalHeight(d) {
        var blocks = d.rowBlocks;
        return firstRowAnchor(blocks, blocks.length - 1) + (blocks.length ? rowsHeight(blocks[blocks.length - 1], Infinity) : 1);
    }

    var scrollbarKit = tableControlView.selectAll('.' + c.cn.scrollbarKit)
        .data(gup.repeat, gup.keyFun);

    scrollbarKit.enter()
        .append('g')
        .classed(c.cn.scrollbarKit, true)
        .style('shape-rendering', 'geometricPrecision');

    scrollbarKit
        .each(function(d) {
            var s = d.scrollbarState;
            s.totalHeight = calcTotalHeight(d);
            s.scrollableAreaHeight = d.groupHeight - headerHeight(d);
            s.currentlyVisibleHeight = Math.min(s.totalHeight, s.scrollableAreaHeight);
            s.ratio = s.currentlyVisibleHeight / s.totalHeight;
            s.barLength = Math.max(s.ratio * s.currentlyVisibleHeight, c.goldenRatio * c.scrollbarWidth);
            s.barWiggleRoom = s.currentlyVisibleHeight - s.barLength;
            s.wiggleRoom = Math.max(0, s.totalHeight - s.scrollableAreaHeight);
            s.topY = s.barWiggleRoom === 0 ? 0 : (d.scrollY / s.wiggleRoom) * s.barWiggleRoom;
            s.bottomY = s.topY + s.barLength;
            s.dragMultiplier = s.wiggleRoom / s.barWiggleRoom;
        })
        .attr('transform', function(d) {
            var xPosition = d.width + c.scrollbarWidth / 2 + c.scrollbarOffset;
            return 'translate(' + xPosition + ' ' + headerHeight(d) + ')';
        });

    var scrollbar = scrollbarKit.selectAll('.' + c.cn.scrollbar)
        .data(gup.repeat, gup.keyFun);

    scrollbar.enter()
        .append('g')
        .classed(c.cn.scrollbar, true);

    var scrollbarSlider = scrollbar.selectAll('.' + c.cn.scrollbarSlider)
        .data(gup.repeat, gup.keyFun);

    scrollbarSlider.enter()
        .append('g')
        .classed(c.cn.scrollbarSlider, true);

    scrollbarSlider
        .attr('transform', function(d) {
            return 'translate(0 ' + (d.scrollbarState.topY || 0) + ')';
        });

    var scrollbarGlyph = scrollbarSlider.selectAll('.' + c.cn.scrollbarGlyph)
        .data(gup.repeat, gup.keyFun);

    scrollbarGlyph.enter()
        .append('line')
        .classed(c.cn.scrollbarGlyph, true)
        .attr('stroke', 'black')
        .attr('stroke-width', c.scrollbarWidth)
        .attr('stroke-linecap', 'round')
        .attr('y1', c.scrollbarWidth / 2);

    scrollbarGlyph
        .attr('y2', function(d) {
            return d.scrollbarState.barLength - c.scrollbarWidth / 2;
        })
        .attr('stroke-opacity', function(d) {
            return d.columnDragInProgress || !d.scrollbarState.barWiggleRoom || bypassVisibleBar ? 0 : 0.4;
        });

    // cancel transition: possible pending (also, delayed) transition
    scrollbarGlyph
        .transition().delay(0).duration(0);

    scrollbarGlyph
        .transition().delay(c.scrollbarHideDelay).duration(c.scrollbarHideDuration)
        .attr('stroke-opacity', 0);

    var scrollbarCaptureZone = scrollbar.selectAll('.' + c.cn.scrollbarCaptureZone)
        .data(gup.repeat, gup.keyFun);

    scrollbarCaptureZone.enter()
        .append('line')
        .classed(c.cn.scrollbarCaptureZone, true)
        .attr('stroke', 'white')
        .attr('stroke-opacity', 0.01) // some browser might get rid of a 0 opacity element
        .attr('stroke-width', c.scrollbarCaptureWidth)
        .attr('stroke-linecap', 'butt')
        .attr('y1', 0)
        .on('mousedown', function(d) {
            var y = d3.event.y;
            var bbox = this.getBoundingClientRect();
            var s = d.scrollbarState;
            var pixelVal = y - bbox.top;
            var inverseScale = d3.scale.linear().domain([0, s.scrollableAreaHeight]).range([0, s.totalHeight]).clamp(true);
            if(!(s.topY <= pixelVal && pixelVal <= s.bottomY)) {
                makeDragRow(gd, tableControlView, null, inverseScale(pixelVal - s.barLength / 2))(d);
            }
        })
        .call(d3.behavior.drag()
            .origin(function(d) {
                d3.event.stopPropagation();
                d.scrollbarState.scrollbarScrollInProgress = true;
                return d;
            })
            .on('drag', makeDragRow(gd, tableControlView))
            .on('dragend', function() {
                // fixme emit Plotly event
            })
        );

    scrollbarCaptureZone
        .attr('y2', function(d) {
            return d.scrollbarState.scrollableAreaHeight;
        });

    // Remove scroll glyph and capture zone on static plots
    // as they don't render properly when converted to PDF
    // in the Chrome PDF viewer
    // https://github.com/plotly/streambed/issues/11618
    if(gd._context.staticPlot) {
        scrollbarGlyph.remove();
        scrollbarCaptureZone.remove();
    }
}

function renderColumnCellTree(gd, tableControlView, columnBlock, allColumnBlock) {
    // fixme this perf hotspot
    // this is performance critical code as scrolling calls it on every revolver switch
    // it appears sufficiently fast but there are plenty of low-hanging fruits for performance optimization

    var columnCells = renderColumnCells(columnBlock);

    var columnCell = renderColumnCell(columnCells);

    supplyStylingValues(columnCell);

    var cellRect = renderCellRect(columnCell);

    sizeAndStyleRect(cellRect);

    var cellTextHolder = renderCellTextHolder(columnCell);

    var cellText = renderCellText(cellTextHolder);

    setFont(cellText);
    populateCellText(cellText, tableControlView, allColumnBlock, gd);

    // doing this at the end when text, and text stlying are set
    setCellHeightAndPositionY(columnCell);
}

function renderColumnCells(columnBlock) {
    var columnCells = columnBlock.selectAll('.' + c.cn.columnCells)
        .data(gup.repeat, gup.keyFun);

    columnCells.enter()
        .append('g')
        .classed(c.cn.columnCells, true);

    columnCells.exit()
        .remove();

    return columnCells;
}

function renderColumnCell(columnCells) {
    var columnCell = columnCells.selectAll('.' + c.cn.columnCell)
        .data(splitData.splitToCells, function(d) {return d.keyWithinBlock;});

    columnCell.enter()
        .append('g')
        .classed(c.cn.columnCell, true);

    columnCell.exit()
        .remove();

    return columnCell;
}

function renderCellRect(columnCell) {
    var cellRect = columnCell.selectAll('.' + c.cn.cellRect)
        .data(gup.repeat, function(d) {return d.keyWithinBlock;});

    cellRect.enter()
        .append('rect')
        .classed(c.cn.cellRect, true);

    return cellRect;
}

function renderCellText(cellTextHolder) {
    var cellText = cellTextHolder.selectAll('.' + c.cn.cellText)
        .data(gup.repeat, function(d) {return d.keyWithinBlock;});

    cellText.enter()
        .append('text')
        .classed(c.cn.cellText, true)
        .style('cursor', function() {return 'auto';})
        .on('mousedown', function() {d3.event.stopPropagation();});

    return cellText;
}

function renderCellTextHolder(columnCell) {
    var cellTextHolder = columnCell.selectAll('.' + c.cn.cellTextHolder)
        .data(gup.repeat, function(d) {return d.keyWithinBlock;});

    cellTextHolder.enter()
        .append('g')
        .classed(c.cn.cellTextHolder, true)
        .style('shape-rendering', 'geometricPrecision');

    return cellTextHolder;
}

function supplyStylingValues(columnCell) {
    columnCell
        .each(function(d, i) {
            var spec = d.calcdata.cells.font;
            var col = d.column.specIndex;
            var font = {
                size: gridPick(spec.size, col, i),
                color: gridPick(spec.color, col, i),
                family: gridPick(spec.family, col, i)
            };
            d.rowNumber = d.key;
            d.align = gridPick(d.calcdata.cells.align, col, i);
            d.cellBorderWidth = gridPick(d.calcdata.cells.line.width, col, i);
            d.font = font;
        });
}

function setFont(cellText) {
    cellText
        .each(function(d) {
            Drawing.font(d3.select(this), d.font);
        });
}

function sizeAndStyleRect(cellRect) {
    cellRect
        .attr('width', function(d) {return d.column.columnWidth;})
        .attr('stroke-width', function(d) {return d.cellBorderWidth;})
        .each(function(d) {
            var atomicSelection = d3.select(this);
            Color.stroke(atomicSelection, gridPick(d.calcdata.cells.line.color, d.column.specIndex, d.rowNumber));
            Color.fill(atomicSelection, gridPick(d.calcdata.cells.fill.color, d.column.specIndex, d.rowNumber));
        });
}

function populateCellText(cellText, tableControlView, allColumnBlock, gd) {
    cellText
        .text(function(d) {
            var col = d.column.specIndex;
            var row = d.rowNumber;

            var userSuppliedContent = d.value;
            var stringSupplied = (typeof userSuppliedContent === 'string');
            var hasBreaks = stringSupplied && userSuppliedContent.match(/<br>/i);
            var userBrokenText = !stringSupplied || hasBreaks;
            d.mayHaveMarkup = stringSupplied && userSuppliedContent.match(/[<&>]/);

            var latex = isLatex(userSuppliedContent);
            d.latex = latex;

            var prefix = latex ? '' : gridPick(d.calcdata.cells.prefix, col, row) || '';
            var suffix = latex ? '' : gridPick(d.calcdata.cells.suffix, col, row) || '';
            var format = latex ? null : gridPick(d.calcdata.cells.format, col, row) || null;

            var prefixSuffixedText = prefix + (format ? d3.format(format)(d.value) : d.value) + suffix;

            var hasWrapSplitCharacter;
            d.wrappingNeeded = !d.wrapped && !userBrokenText && !latex && (hasWrapSplitCharacter = hasWrapCharacter(prefixSuffixedText));
            d.cellHeightMayIncrease = hasBreaks || latex || d.mayHaveMarkup || (hasWrapSplitCharacter === void(0) ? hasWrapCharacter(prefixSuffixedText) : hasWrapSplitCharacter);
            d.needsConvertToTspans = d.mayHaveMarkup || d.wrappingNeeded || d.latex;

            var textToRender;
            if(d.wrappingNeeded) {
                var hrefPreservedText = c.wrapSplitCharacter === ' ' ? prefixSuffixedText.replace(/<a href=/ig, '<a_href=') : prefixSuffixedText;
                var fragments = hrefPreservedText.split(c.wrapSplitCharacter);
                var hrefRestoredFragments = c.wrapSplitCharacter === ' ' ? fragments.map(function(frag) {return frag.replace(/<a_href=/ig, '<a href=');}) : fragments;
                d.fragments = hrefRestoredFragments.map(function(f) {return {text: f, width: null};});
                d.fragments.push({fragment: c.wrapSpacer, width: null});
                textToRender = hrefRestoredFragments.join(c.lineBreaker) + c.lineBreaker + c.wrapSpacer;
            } else {
                delete d.fragments;
                textToRender = prefixSuffixedText;
            }

            return textToRender;
        })
        .attr('dy', function(d) {
            return d.needsConvertToTspans ? 0 : '0.75em';
        })
        .each(function(d) {
            var element = this;
            var selection = d3.select(element);

            // finalize what's in the DOM

            var renderCallback = d.wrappingNeeded ? wrapTextMaker : updateYPositionMaker;
            if(d.needsConvertToTspans) {
                svgUtil.convertToTspans(selection, gd, renderCallback(allColumnBlock, element, tableControlView, gd, d));
            } else {
                d3.select(element.parentNode)
                    // basic cell adjustment - compliance with `cellPad`
                    .attr('transform', function(d) {return 'translate(' + xPosition(d) + ' ' + c.cellPad + ')';})
                    .attr('text-anchor', function(d) {
                        return ({
                            left: 'start',
                            center: 'middle',
                            right: 'end'
                        })[d.align];
                    });
            }
        });
}

function isLatex(content) {
    return typeof content === 'string' && content.match(c.latexCheck);
}

function hasWrapCharacter(text) {return text.indexOf(c.wrapSplitCharacter) !== -1;}

function columnMoved(gd, calcdata, indices) {
    var o = calcdata.gdColumnsOriginalOrder;
    calcdata.gdColumns.sort(function(a, b) {
        return indices[o.indexOf(a)] - indices[o.indexOf(b)];
    });

    calcdata.columnorder = indices;

    // TODO: there's no data here, but also this reordering is not reflected
    // in gd.data or even gd._fullData.
    // For now I will not attempt to persist this in _preGUI
    gd.emit('plotly_restyle');
}

function gridPick(spec, col, row) {
    if(Array.isArray(spec)) {
        var column = spec[Math.min(col, spec.length - 1)];
        if(Array.isArray(column)) {
            return column[Math.min(row, column.length - 1)];
        } else {
            return column;
        }
    } else {
        return spec;
    }
}

function easeColumn(selection, d, y) {
    selection
        .transition()
        .ease(c.releaseTransitionEase)
        .duration(c.releaseTransitionDuration)
        .attr('transform', 'translate(' + d.x + ' ' + y + ')');
}

function cellsBlock(d) {return d.type === 'cells';}
function headerBlock(d) {return d.type === 'header';}

/**
 * Revolver panel and cell contents layouting
 */

function headerHeight(d) {
    var headerBlocks = d.rowBlocks.length ? d.rowBlocks[0].auxiliaryBlocks : [];
    return headerBlocks.reduce(function(p, n) {return p + rowsHeight(n, Infinity);}, 0);
}

function findPagesAndCacheHeights(blocks, scrollY, scrollHeight) {
    var pages = [];
    var pTop = 0;

    for(var blockIndex = 0; blockIndex < blocks.length; blockIndex++) {
        var block = blocks[blockIndex];
        var blockRows = block.rows;
        var rowsHeight = 0;
        for(var i = 0; i < blockRows.length; i++) {
            rowsHeight += blockRows[i].rowHeight;
        }

        // caching allRowsHeight on the block - it's safe as this function is always called from within the code part
        // that handles increases to row heights
        block.allRowsHeight = rowsHeight;

        var pBottom = pTop + rowsHeight;
        var windowTop = scrollY;
        var windowBottom = windowTop + scrollHeight;
        if(windowTop < pBottom && windowBottom > pTop) {
            pages.push(blockIndex);
        }
        pTop += rowsHeight;

        // consider this nice final optimization; put it in `for` condition - caveat, currently the
        // block.allRowsHeight relies on being invalidated, so enabling this opt may not be safe
        // if(pages.length > 1) break;
    }

    return pages;
}

function updateBlockYPosition(gd, cellsColumnBlock, tableControlView) {
    var d = flatData(cellsColumnBlock)[0];
    if(d === undefined) return;
    var blocks = d.rowBlocks;
    var calcdata = d.calcdata;

    var bottom = firstRowAnchor(blocks, blocks.length);
    var scrollHeight = d.calcdata.groupHeight - headerHeight(d);
    var scrollY = calcdata.scrollY = Math.max(0, Math.min(bottom - scrollHeight, calcdata.scrollY));

    var pages = findPagesAndCacheHeights(blocks, scrollY, scrollHeight);
    if(pages.length === 1) {
        if(pages[0] === blocks.length - 1) {
            pages.unshift(pages[0] - 1);
        } else {
            pages.push(pages[0] + 1);
        }
    }

    // make phased out page jump by 2 while leaving stationary page intact
    if(pages[0] % 2) {
        pages.reverse();
    }

    cellsColumnBlock
        .each(function(d, i) {
            // these values will also be needed when a block is translated again due to growing cell height
            d.page = pages[i];
            d.scrollY = scrollY;
        });

    cellsColumnBlock
        .attr('transform', function(d) {
            var yTranslate = firstRowAnchor(d.rowBlocks, d.page) - d.scrollY;
            return 'translate(0 ' + yTranslate + ')';
        });

    // conditionally rerendering panel 0 and 1
    if(gd) {
        conditionalPanelRerender(gd, tableControlView, cellsColumnBlock, pages, d.prevPages, d, 0);
        conditionalPanelRerender(gd, tableControlView, cellsColumnBlock, pages, d.prevPages, d, 1);
        renderScrollbarKit(tableControlView, gd);
    }
}

function makeDragRow(gd, allTableControlView, optionalMultiplier, optionalPosition) {
    return function dragRow(eventD) {
        // may come from whichever DOM event target: drag, wheel, bar... eventD corresponds to event target
        var d = eventD.calcdata ? eventD.calcdata : eventD;
        var tableControlView = allTableControlView.filter(function(dd) {return d.key === dd.key;});
        var multiplier = optionalMultiplier || d.scrollbarState.dragMultiplier;

        var initialScrollY = d.scrollY;

        d.scrollY = optionalPosition === void(0) ? d.scrollY + multiplier * d3.event.dy : optionalPosition;
        var cellsColumnBlock = tableControlView.selectAll('.' + c.cn.yColumn).selectAll('.' + c.cn.columnBlock).filter(cellsBlock);
        updateBlockYPosition(gd, cellsColumnBlock, tableControlView);

        // return false if we've "used" the scroll, ie it did something,
        // so the event shouldn't bubble (if appropriate)
        return d.scrollY === initialScrollY;
    };
}

function conditionalPanelRerender(gd, tableControlView, cellsColumnBlock, pages, prevPages, d, revolverIndex) {
    var shouldComponentUpdate = pages[revolverIndex] !== prevPages[revolverIndex];
    if(shouldComponentUpdate) {
        clearTimeout(d.currentRepaint[revolverIndex]);
        d.currentRepaint[revolverIndex] = setTimeout(function() {
            // setTimeout might lag rendering but yields a smoother scroll, because fast scrolling makes
            // some repaints invisible ie. wasteful (DOM work blocks the main thread)
            var toRerender = cellsColumnBlock.filter(function(d, i) {return i === revolverIndex && pages[i] !== prevPages[i];});
            renderColumnCellTree(gd, tableControlView, toRerender, cellsColumnBlock);
            prevPages[revolverIndex] = pages[revolverIndex];
        });
    }
}

function wrapTextMaker(columnBlock, element, tableControlView, gd) {
    return function wrapText() {
        var cellTextHolder = d3.select(element.parentNode);
        cellTextHolder
            .each(function(d) {
                var fragments = d.fragments;
                cellTextHolder.selectAll('tspan.line').each(function(dd, i) {
                    fragments[i].width = this.getComputedTextLength();
                });
                // last element is only for measuring the separator character, so it's ignored:
                var separatorLength = fragments[fragments.length - 1].width;
                var rest = fragments.slice(0, -1);
                var currentRow = [];
                var currentAddition, currentAdditionLength;
                var currentRowLength = 0;
                var rowLengthLimit = d.column.columnWidth - 2 * c.cellPad;
                d.value = '';
                while(rest.length) {
                    currentAddition = rest.shift();
                    currentAdditionLength = currentAddition.width + separatorLength;
                    if(currentRowLength + currentAdditionLength > rowLengthLimit) {
                        d.value += currentRow.join(c.wrapSpacer) + c.lineBreaker;
                        currentRow = [];
                        currentRowLength = 0;
                    }
                    currentRow.push(currentAddition.text);
                    currentRowLength += currentAdditionLength;
                }
                if(currentRowLength) {
                    d.value += currentRow.join(c.wrapSpacer);
                }
                d.wrapped = true;
            });

        // the pre-wrapped text was rendered only for the text measurements
        cellTextHolder.selectAll('tspan.line').remove();

        // resupply text, now wrapped
        populateCellText(cellTextHolder.select('.' + c.cn.cellText), tableControlView, columnBlock, gd);
        d3.select(element.parentNode.parentNode).call(setCellHeightAndPositionY);
    };
}

function updateYPositionMaker(columnBlock, element, tableControlView, gd, d) {
    return function updateYPosition() {
        if(d.settledY) return;
        var cellTextHolder = d3.select(element.parentNode);
        var l = getBlock(d);
        var rowIndex = d.key - l.firstRowIndex;

        var declaredRowHeight = l.rows[rowIndex].rowHeight;

        var requiredHeight = d.cellHeightMayIncrease ? element.parentNode.getBoundingClientRect().height + 2 * c.cellPad : declaredRowHeight;

        var finalHeight = Math.max(requiredHeight, declaredRowHeight);
        var increase = finalHeight - l.rows[rowIndex].rowHeight;

        if(increase) {
            // current row height increased
            l.rows[rowIndex].rowHeight = finalHeight;

            columnBlock
                .selectAll('.' + c.cn.columnCell)
                .call(setCellHeightAndPositionY);

            updateBlockYPosition(null, columnBlock.filter(cellsBlock), 0);

            // if d.column.type === 'header', then the scrollbar has to be pushed downward to the scrollable area
            // if d.column.type === 'cells', it can still be relevant if total scrolling content height is less than the
            //                               scrollable window, as increases to row heights may need scrollbar updates
            renderScrollbarKit(tableControlView, gd, true);
        }

        cellTextHolder
            .attr('transform', function() {
                // this code block is only invoked for items where d.cellHeightMayIncrease is truthy
                var element = this;
                var columnCellElement = element.parentNode;
                var box = columnCellElement.getBoundingClientRect();
                var rectBox = d3.select(element.parentNode).select('.' + c.cn.cellRect).node().getBoundingClientRect();
                var currentTransform = element.transform.baseVal.consolidate();
                var yPosition = rectBox.top - box.top + (currentTransform ? currentTransform.matrix.f : c.cellPad);
                return 'translate(' + xPosition(d, d3.select(element.parentNode).select('.' + c.cn.cellTextHolder).node().getBoundingClientRect().width) + ' ' + yPosition + ')';
            });

        d.settledY = true;
    };
}

function xPosition(d, optionalWidth) {
    switch(d.align) {
        case 'left': return c.cellPad;
        case 'right': return d.column.columnWidth - (optionalWidth || 0) - c.cellPad;
        case 'center': return (d.column.columnWidth - (optionalWidth || 0)) / 2;
        default: return c.cellPad;
    }
}

function setCellHeightAndPositionY(columnCell) {
    columnCell
        .attr('transform', function(d) {
            var headerHeight = d.rowBlocks[0].auxiliaryBlocks.reduce(function(p, n) {return p + rowsHeight(n, Infinity);}, 0);
            var l = getBlock(d);
            var rowAnchor = rowsHeight(l, d.key);
            var yOffset = rowAnchor + headerHeight;
            return 'translate(0 ' + yOffset + ')';
        })
        .selectAll('.' + c.cn.cellRect)
        .attr('height', function(d) {return getRow(getBlock(d), d.key).rowHeight;});
}

function firstRowAnchor(blocks, page) {
    var total = 0;
    for(var i = page - 1; i >= 0; i--) {
        total += allRowsHeight(blocks[i]);
    }
    return total;
}

function rowsHeight(rowBlock, key) {
    var total = 0;
    for(var i = 0; i < rowBlock.rows.length && rowBlock.rows[i].rowIndex < key; i++) {
        total += rowBlock.rows[i].rowHeight;
    }
    return total;
}

function allRowsHeight(rowBlock) {
    var cached = rowBlock.allRowsHeight;

    if(cached !== void(0)) {
        return cached;
    }

    var total = 0;
    for(var i = 0; i < rowBlock.rows.length; i++) {
        total += rowBlock.rows[i].rowHeight;
    }
    rowBlock.allRowsHeight = total;

    return total;
}

function getBlock(d) {return d.rowBlocks[d.page];}
function getRow(l, i) {return l.rows[i - l.firstRowIndex];}
