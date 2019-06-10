/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var Registry = require('../registry');
var Plots = require('../plots/plots');

var Lib = require('../lib');
var clearGlCanvases = require('../lib/clear_gl_canvases');

var Color = require('../components/color');
var Drawing = require('../components/drawing');
var Titles = require('../components/titles');
var ModeBar = require('../components/modebar');

var Axes = require('../plots/cartesian/axes');
var alignmentConstants = require('../constants/alignment');
var axisConstraints = require('../plots/cartesian/constraints');
var enforceAxisConstraints = axisConstraints.enforce;
var cleanAxisConstraints = axisConstraints.clean;
var doAutoRange = require('../plots/cartesian/autorange').doAutoRange;

var SVG_TEXT_ANCHOR_START = 'start';
var SVG_TEXT_ANCHOR_MIDDLE = 'middle';
var SVG_TEXT_ANCHOR_END = 'end';

exports.layoutStyles = function(gd) {
    return Lib.syncOrAsync([Plots.doAutoMargin, lsInner], gd);
};

function overlappingDomain(xDomain, yDomain, domains) {
    for(var i = 0; i < domains.length; i++) {
        var existingX = domains[i][0];
        var existingY = domains[i][1];

        if(existingX[0] >= xDomain[1] || existingX[1] <= xDomain[0]) {
            continue;
        }
        if(existingY[0] < yDomain[1] && existingY[1] > yDomain[0]) {
            return true;
        }
    }
    return false;
}

function lsInner(gd) {
    var fullLayout = gd._fullLayout;
    var gs = fullLayout._size;
    var pad = gs.p;
    var axList = Axes.list(gd, '', true);
    var i, subplot, plotinfo, ax, xa, ya;

    fullLayout._paperdiv.style({
        width: (gd._context.responsive && fullLayout.autosize && !gd._context._hasZeroWidth && !gd.layout.width) ? '100%' : fullLayout.width + 'px',
        height: (gd._context.responsive && fullLayout.autosize && !gd._context._hasZeroHeight && !gd.layout.height) ? '100%' : fullLayout.height + 'px'
    })
    .selectAll('.main-svg')
    .call(Drawing.setSize, fullLayout.width, fullLayout.height);
    gd._context.setBackground(gd, fullLayout.paper_bgcolor);

    exports.drawMainTitle(gd);
    ModeBar.manage(gd);

    // _has('cartesian') means SVG specifically, not GL2D - but GL2D
    // can still get here because it makes some of the SVG structure
    // for shared features like selections.
    if(!fullLayout._has('cartesian')) {
        return gd._promises.length && Promise.all(gd._promises);
    }

    function getLinePosition(ax, counterAx, side) {
        var lwHalf = ax._lw / 2;

        if(ax._id.charAt(0) === 'x') {
            if(!counterAx) return gs.t + gs.h * (1 - (ax.position || 0)) + (lwHalf % 1);
            else if(side === 'top') return counterAx._offset - pad - lwHalf;
            return counterAx._offset + counterAx._length + pad + lwHalf;
        }

        if(!counterAx) return gs.l + gs.w * (ax.position || 0) + (lwHalf % 1);
        else if(side === 'right') return counterAx._offset + counterAx._length + pad + lwHalf;
        return counterAx._offset - pad - lwHalf;
    }

    // some preparation of axis position info
    for(i = 0; i < axList.length; i++) {
        ax = axList[i];

        var counterAx = ax._anchorAxis;

        // clear axis line positions, to be set in the subplot loop below
        ax._linepositions = {};

        // stash crispRounded linewidth so we don't need to pass gd all over the place
        ax._lw = Drawing.crispRound(gd, ax.linewidth, 1);

        // figure out the main axis line and main mirror line position.
        // it's easier to follow the logic if we handle these separately from
        // ax._linepositions, which are only used by mirror=allticks
        // for non-main-subplot ticks, and mirror=all(ticks)? for zero line
        // hiding logic
        ax._mainLinePosition = getLinePosition(ax, counterAx, ax.side);
        ax._mainMirrorPosition = (ax.mirror && counterAx) ?
            getLinePosition(ax, counterAx,
                alignmentConstants.OPPOSITE_SIDE[ax.side]) : null;
    }

    // figure out which backgrounds we need to draw,
    // and in which layers to put them
    var lowerBackgroundIDs = [];
    var backgroundIds = [];
    var lowerDomains = [];
    // no need to draw background when paper and plot color are the same color,
    // activate mode just for large splom (which benefit the most from this
    // optimization), but this could apply to all cartesian subplots.
    var noNeedForBg = (
        Color.opacity(fullLayout.paper_bgcolor) === 1 &&
        Color.opacity(fullLayout.plot_bgcolor) === 1 &&
        fullLayout.paper_bgcolor === fullLayout.plot_bgcolor
    );

    for(subplot in fullLayout._plots) {
        plotinfo = fullLayout._plots[subplot];

        if(plotinfo.mainplot) {
            // mainplot is a reference to the main plot this one is overlaid on
            // so if it exists, this is an overlaid plot and we don't need to
            // give it its own background
            if(plotinfo.bg) {
                plotinfo.bg.remove();
            }
            plotinfo.bg = undefined;
        } else {
            var xDomain = plotinfo.xaxis.domain;
            var yDomain = plotinfo.yaxis.domain;
            var plotgroup = plotinfo.plotgroup;

            if(overlappingDomain(xDomain, yDomain, lowerDomains)) {
                var pgNode = plotgroup.node();
                var plotgroupBg = plotinfo.bg = Lib.ensureSingle(plotgroup, 'rect', 'bg');
                pgNode.insertBefore(plotgroupBg.node(), pgNode.childNodes[0]);
                backgroundIds.push(subplot);
            } else {
                plotgroup.select('rect.bg').remove();
                lowerDomains.push([xDomain, yDomain]);
                if(!noNeedForBg) {
                    lowerBackgroundIDs.push(subplot);
                    backgroundIds.push(subplot);
                }
            }
        }
    }

    // now create all the lower-layer backgrounds at once now that
    // we have the list of subplots that need them
    var lowerBackgrounds = fullLayout._bgLayer.selectAll('.bg')
        .data(lowerBackgroundIDs);

    lowerBackgrounds.enter().append('rect')
        .classed('bg', true);

    lowerBackgrounds.exit().remove();

    lowerBackgrounds.each(function(subplot) {
        fullLayout._plots[subplot].bg = d3.select(this);
    });

    // style all backgrounds
    for(i = 0; i < backgroundIds.length; i++) {
        plotinfo = fullLayout._plots[backgroundIds[i]];
        xa = plotinfo.xaxis;
        ya = plotinfo.yaxis;

        if(plotinfo.bg) {
            plotinfo.bg
                .call(Drawing.setRect,
                    xa._offset - pad, ya._offset - pad,
                    xa._length + 2 * pad, ya._length + 2 * pad)
                .call(Color.fill, fullLayout.plot_bgcolor)
                .style('stroke-width', 0);
        }
    }

    if(!fullLayout._hasOnlyLargeSploms) {
        for(subplot in fullLayout._plots) {
            plotinfo = fullLayout._plots[subplot];
            xa = plotinfo.xaxis;
            ya = plotinfo.yaxis;

            // Clip so that data only shows up on the plot area.
            var clipId = plotinfo.clipId = 'clip' + fullLayout._uid + subplot + 'plot';

            var plotClip = Lib.ensureSingleById(fullLayout._clips, 'clipPath', clipId, function(s) {
                s.classed('plotclip', true)
                    .append('rect');
            });

            plotinfo.clipRect = plotClip.select('rect').attr({
                width: xa._length,
                height: ya._length
            });

            Drawing.setTranslate(plotinfo.plot, xa._offset, ya._offset);

            var plotClipId;
            var layerClipId;

            if(plotinfo._hasClipOnAxisFalse) {
                plotClipId = null;
                layerClipId = clipId;
            } else {
                plotClipId = clipId;
                layerClipId = null;
            }

            Drawing.setClipUrl(plotinfo.plot, plotClipId, gd);

            // stash layer clipId value (null or same as clipId)
            // to DRY up Drawing.setClipUrl calls on trace-module and trace layers
            // downstream
            plotinfo.layerClipId = layerClipId;
        }
    }

    var xLinesXLeft, xLinesXRight, xLinesYBottom, xLinesYTop,
        leftYLineWidth, rightYLineWidth;
    var yLinesYBottom, yLinesYTop, yLinesXLeft, yLinesXRight,
        connectYBottom, connectYTop;
    var extraSubplot;

    function xLinePath(y) {
        return 'M' + xLinesXLeft + ',' + y + 'H' + xLinesXRight;
    }

    function xLinePathFree(y) {
        return 'M' + xa._offset + ',' + y + 'h' + xa._length;
    }

    function yLinePath(x) {
        return 'M' + x + ',' + yLinesYTop + 'V' + yLinesYBottom;
    }

    function yLinePathFree(x) {
        return 'M' + x + ',' + ya._offset + 'v' + ya._length;
    }

    function mainPath(ax, pathFn, pathFnFree) {
        if(!ax.showline || subplot !== ax._mainSubplot) return '';
        if(!ax._anchorAxis) return pathFnFree(ax._mainLinePosition);
        var out = pathFn(ax._mainLinePosition);
        if(ax.mirror) out += pathFn(ax._mainMirrorPosition);
        return out;
    }

    for(subplot in fullLayout._plots) {
        plotinfo = fullLayout._plots[subplot];
        xa = plotinfo.xaxis;
        ya = plotinfo.yaxis;

        /*
         * x lines get longer where they meet y lines, to make a crisp corner.
         * The x lines get the padding (margin.pad) plus the y line width to
         * fill up the corner nicely. Free x lines are excluded - they always
         * span exactly the data area of the plot
         *
         *  | XXXXX
         *  | XXXXX
         *  |
         *  +------
         *     x1
         *    -----
         *     x2
         */
        var xPath = 'M0,0';
        if(shouldShowLinesOrTicks(xa, subplot)) {
            leftYLineWidth = findCounterAxisLineWidth(xa, 'left', ya, axList);
            xLinesXLeft = xa._offset - (leftYLineWidth ? (pad + leftYLineWidth) : 0);
            rightYLineWidth = findCounterAxisLineWidth(xa, 'right', ya, axList);
            xLinesXRight = xa._offset + xa._length + (rightYLineWidth ? (pad + rightYLineWidth) : 0);
            xLinesYBottom = getLinePosition(xa, ya, 'bottom');
            xLinesYTop = getLinePosition(xa, ya, 'top');

            // save axis line positions for extra ticks to reference
            // each subplot that gets ticks from "allticks" gets an entry:
            //    [left or bottom, right or top]
            extraSubplot = (!xa._anchorAxis || subplot !== xa._mainSubplot);
            if(extraSubplot && (xa.mirror === 'allticks' || xa.mirror === 'all')) {
                xa._linepositions[subplot] = [xLinesYBottom, xLinesYTop];
            }

            xPath = mainPath(xa, xLinePath, xLinePathFree);
            if(extraSubplot && xa.showline && (xa.mirror === 'all' || xa.mirror === 'allticks')) {
                xPath += xLinePath(xLinesYBottom) + xLinePath(xLinesYTop);
            }

            plotinfo.xlines
                .style('stroke-width', xa._lw + 'px')
                .call(Color.stroke, xa.showline ?
                    xa.linecolor : 'rgba(0,0,0,0)');
        }
        plotinfo.xlines.attr('d', xPath);

        /*
         * y lines that meet x axes get longer only by margin.pad, because
         * the x axes fill in the corner space. Free y axes, like free x axes,
         * always span exactly the data area of the plot
         *
         *   |   | XXXX
         * y2| y1| XXXX
         *   |   | XXXX
         *       |
         *       +-----
         */
        var yPath = 'M0,0';
        if(shouldShowLinesOrTicks(ya, subplot)) {
            connectYBottom = findCounterAxisLineWidth(ya, 'bottom', xa, axList);
            yLinesYBottom = ya._offset + ya._length + (connectYBottom ? pad : 0);
            connectYTop = findCounterAxisLineWidth(ya, 'top', xa, axList);
            yLinesYTop = ya._offset - (connectYTop ? pad : 0);
            yLinesXLeft = getLinePosition(ya, xa, 'left');
            yLinesXRight = getLinePosition(ya, xa, 'right');

            extraSubplot = (!ya._anchorAxis || subplot !== ya._mainSubplot);
            if(extraSubplot && (ya.mirror === 'allticks' || ya.mirror === 'all')) {
                ya._linepositions[subplot] = [yLinesXLeft, yLinesXRight];
            }

            yPath = mainPath(ya, yLinePath, yLinePathFree);
            if(extraSubplot && ya.showline && (ya.mirror === 'all' || ya.mirror === 'allticks')) {
                yPath += yLinePath(yLinesXLeft) + yLinePath(yLinesXRight);
            }

            plotinfo.ylines
                .style('stroke-width', ya._lw + 'px')
                .call(Color.stroke, ya.showline ?
                    ya.linecolor : 'rgba(0,0,0,0)');
        }
        plotinfo.ylines.attr('d', yPath);
    }

    Axes.makeClipPaths(gd);

    return gd._promises.length && Promise.all(gd._promises);
}

function shouldShowLinesOrTicks(ax, subplot) {
    return (ax.ticks || ax.showline) &&
        (subplot === ax._mainSubplot || ax.mirror === 'all' || ax.mirror === 'allticks');
}

/*
 * should we draw a line on counterAx at this side of ax?
 * It's assumed that counterAx is known to overlay the subplot we're working on
 * but it may not be its main axis.
 */
function shouldShowLineThisSide(ax, side, counterAx) {
    // does counterAx get a line at all?
    if(!counterAx.showline || !counterAx._lw) return false;

    // are we drawing *all* lines for counterAx?
    if(counterAx.mirror === 'all' || counterAx.mirror === 'allticks') return true;

    var anchorAx = counterAx._anchorAxis;

    // is this a free axis? free axes can only have a subplot side-line with all(ticks)? mirroring
    if(!anchorAx) return false;

    // in order to handle cases where the user forgot to anchor this axis correctly
    // (because its default anchor has the same domain on the relevant end)
    // check whether the relevant position is the same.
    var sideIndex = alignmentConstants.FROM_BL[side];
    if(counterAx.side === side) {
        return anchorAx.domain[sideIndex] === ax.domain[sideIndex];
    }
    return counterAx.mirror && anchorAx.domain[1 - sideIndex] === ax.domain[1 - sideIndex];
}

/*
 * Is there another axis intersecting `side` end of `ax`?
 * First look at `counterAx` (the axis for this subplot),
 * then at all other potential counteraxes on or overlaying this subplot.
 * Take the line width from the first one that has a line.
 */
function findCounterAxisLineWidth(ax, side, counterAx, axList) {
    if(shouldShowLineThisSide(ax, side, counterAx)) {
        return counterAx._lw;
    }
    for(var i = 0; i < axList.length; i++) {
        var axi = axList[i];
        if(axi._mainAxis === counterAx._mainAxis && shouldShowLineThisSide(ax, side, axi)) {
            return axi._lw;
        }
    }
    return 0;
}

exports.drawMainTitle = function(gd) {
    var fullLayout = gd._fullLayout;

    var textAnchor = getMainTitleTextAnchor(fullLayout);
    var dy = getMainTitleDy(fullLayout);

    Titles.draw(gd, 'gtitle', {
        propContainer: fullLayout,
        propName: 'title.text',
        placeholder: fullLayout._dfltTitle.plot,
        attributes: {
            x: getMainTitleX(fullLayout, textAnchor),
            y: getMainTitleY(fullLayout, dy),
            'text-anchor': textAnchor,
            dy: dy
        }
    });
};

function getMainTitleX(fullLayout, textAnchor) {
    var title = fullLayout.title;
    var gs = fullLayout._size;
    var hPadShift = 0;

    if(textAnchor === SVG_TEXT_ANCHOR_START) {
        hPadShift = title.pad.l;
    } else if(textAnchor === SVG_TEXT_ANCHOR_END) {
        hPadShift = -title.pad.r;
    }

    switch(title.xref) {
        case 'paper':
            return gs.l + gs.w * title.x + hPadShift;
        case 'container':
        default:
            return fullLayout.width * title.x + hPadShift;
    }
}

function getMainTitleY(fullLayout, dy) {
    var title = fullLayout.title;
    var gs = fullLayout._size;
    var vPadShift = 0;

    if(dy === '0em' || !dy) {
        vPadShift = -title.pad.b;
    } else if(dy === alignmentConstants.CAP_SHIFT + 'em') {
        vPadShift = title.pad.t;
    }

    if(title.y === 'auto') {
        return gs.t / 2;
    } else {
        switch(title.yref) {
            case 'paper':
                return gs.t + gs.h - gs.h * title.y + vPadShift;
            case 'container':
            default:
                return fullLayout.height - fullLayout.height * title.y + vPadShift;
        }
    }
}

function getMainTitleTextAnchor(fullLayout) {
    var title = fullLayout.title;

    var textAnchor = SVG_TEXT_ANCHOR_MIDDLE;
    if(Lib.isRightAnchor(title)) {
        textAnchor = SVG_TEXT_ANCHOR_END;
    } else if(Lib.isLeftAnchor(title)) {
        textAnchor = SVG_TEXT_ANCHOR_START;
    }

    return textAnchor;
}

function getMainTitleDy(fullLayout) {
    var title = fullLayout.title;

    var dy = '0em';
    if(Lib.isTopAnchor(title)) {
        dy = alignmentConstants.CAP_SHIFT + 'em';
    } else if(Lib.isMiddleAnchor(title)) {
        dy = alignmentConstants.MID_SHIFT + 'em';
    }

    return dy;
}

exports.doTraceStyle = function(gd) {
    var calcdata = gd.calcdata;
    var editStyleCalls = [];
    var i;

    for(i = 0; i < calcdata.length; i++) {
        var cd = calcdata[i];
        var cd0 = cd[0] || {};
        var trace = cd0.trace || {};
        var _module = trace._module || {};

        // See if we need to do arraysToCalcdata
        // call it regardless of what change we made, in case
        // supplyDefaults brought in an array that was already
        // in gd.data but not in gd._fullData previously
        var arraysToCalcdata = _module.arraysToCalcdata;
        if(arraysToCalcdata) arraysToCalcdata(cd, trace);

        var editStyle = _module.editStyle;
        if(editStyle) editStyleCalls.push({fn: editStyle, cd0: cd0});
    }

    if(editStyleCalls.length) {
        for(i = 0; i < editStyleCalls.length; i++) {
            var edit = editStyleCalls[i];
            edit.fn(gd, edit.cd0);
        }
        clearGlCanvases(gd);
        exports.redrawReglTraces(gd);
    }

    Plots.style(gd);
    Registry.getComponentMethod('legend', 'draw')(gd);

    return Plots.previousPromises(gd);
};

exports.doColorBars = function(gd) {
    Registry.getComponentMethod('colorbar', 'draw')(gd);
    return Plots.previousPromises(gd);
};

// force plot() to redo the layout and replot with the modified layout
exports.layoutReplot = function(gd) {
    var layout = gd.layout;
    gd.layout = undefined;
    return Registry.call('plot', gd, '', layout);
};

exports.doLegend = function(gd) {
    Registry.getComponentMethod('legend', 'draw')(gd);
    return Plots.previousPromises(gd);
};

exports.doTicksRelayout = function(gd) {
    Axes.draw(gd, 'redraw');

    if(gd._fullLayout._hasOnlyLargeSploms) {
        Registry.subplotsRegistry.splom.updateGrid(gd);
        clearGlCanvases(gd);
        exports.redrawReglTraces(gd);
    }

    exports.drawMainTitle(gd);
    return Plots.previousPromises(gd);
};

exports.doModeBar = function(gd) {
    var fullLayout = gd._fullLayout;

    ModeBar.manage(gd);

    for(var i = 0; i < fullLayout._basePlotModules.length; i++) {
        var updateFx = fullLayout._basePlotModules[i].updateFx;
        if(updateFx) updateFx(gd);
    }

    return Plots.previousPromises(gd);
};

exports.doCamera = function(gd) {
    var fullLayout = gd._fullLayout;
    var sceneIds = fullLayout._subplots.gl3d;

    for(var i = 0; i < sceneIds.length; i++) {
        var sceneLayout = fullLayout[sceneIds[i]];
        var scene = sceneLayout._scene;

        var cameraData = sceneLayout.camera;
        scene.setCamera(cameraData);
    }
};

exports.drawData = function(gd) {
    var fullLayout = gd._fullLayout;

    clearGlCanvases(gd);

    // loop over the base plot modules present on graph
    var basePlotModules = fullLayout._basePlotModules;
    for(var i = 0; i < basePlotModules.length; i++) {
        basePlotModules[i].plot(gd);
    }

    exports.redrawReglTraces(gd);

    // styling separate from drawing
    Plots.style(gd);

    // show annotations and shapes
    Registry.getComponentMethod('shapes', 'draw')(gd);
    Registry.getComponentMethod('annotations', 'draw')(gd);

    // Mark the first render as complete
    fullLayout._replotting = false;

    return Plots.previousPromises(gd);
};

// Draw (or redraw) all regl-based traces in one go,
// useful during drag and selection where buffers of targeted traces are updated,
// but all traces need to be redrawn following clearGlCanvases.
//
// Note that _module.plot for regl trace does NOT draw things
// on the canvas, they only update the buffers.
// Drawing is perform here.
//
// TODO try adding per-subplot option using gl.SCISSOR_TEST for
// non-overlaying, disjoint subplots.
//
// TODO try to include parcoords in here.
// https://github.com/plotly/plotly.js/issues/3069
exports.redrawReglTraces = function(gd) {
    var fullLayout = gd._fullLayout;

    if(fullLayout._has('regl')) {
        var fullData = gd._fullData;
        var cartesianIds = [];
        var polarIds = [];
        var i, sp;

        if(fullLayout._hasOnlyLargeSploms) {
            fullLayout._splomGrid.draw();
        }

        // N.B.
        // - Loop over fullData (not _splomScenes) to preserve splom trace-to-trace ordering
        // - Fill list if subplot ids (instead of fullLayout._subplots) to handle cases where all traces
        //   of a given module are `visible !== true`
        for(i = 0; i < fullData.length; i++) {
            var trace = fullData[i];

            if(trace.visible === true && trace._length !== 0) {
                if(trace.type === 'splom') {
                    fullLayout._splomScenes[trace.uid].draw();
                } else if(trace.type === 'scattergl') {
                    Lib.pushUnique(cartesianIds, trace.xaxis + trace.yaxis);
                } else if(trace.type === 'scatterpolargl') {
                    Lib.pushUnique(polarIds, trace.subplot);
                }
            }
        }

        for(i = 0; i < cartesianIds.length; i++) {
            sp = fullLayout._plots[cartesianIds[i]];
            if(sp._scene) sp._scene.draw();
        }

        for(i = 0; i < polarIds.length; i++) {
            sp = fullLayout[polarIds[i]]._subplot;
            if(sp._scene) sp._scene.draw();
        }
    }
};

exports.doAutoRangeAndConstraints = function(gd) {
    var fullLayout = gd._fullLayout;
    var axList = Axes.list(gd, '', true);
    var matchGroups = fullLayout._axisMatchGroups || [];
    var ax;
    var axRng;

    for(var i = 0; i < axList.length; i++) {
        ax = axList[i];
        cleanAxisConstraints(gd, ax);
        doAutoRange(gd, ax);
    }

    enforceAxisConstraints(gd);

    groupLoop:
    for(var j = 0; j < matchGroups.length; j++) {
        var group = matchGroups[j];
        var rng = null;
        var id;

        for(id in group) {
            ax = Axes.getFromId(gd, id);
            if(ax.autorange === false) continue groupLoop;

            axRng = Lib.simpleMap(ax.range, ax.r2l);
            if(rng) {
                if(rng[0] < rng[1]) {
                    rng[0] = Math.min(rng[0], axRng[0]);
                    rng[1] = Math.max(rng[1], axRng[1]);
                } else {
                    rng[0] = Math.max(rng[0], axRng[0]);
                    rng[1] = Math.min(rng[1], axRng[1]);
                }
            } else {
                rng = axRng;
            }
        }

        for(id in group) {
            ax = Axes.getFromId(gd, id);
            ax.range = Lib.simpleMap(rng, ax.l2r);
            ax._input.range = ax.range.slice();
            ax.setScale();
        }
    }
};

// An initial paint must be completed before these components can be
// correctly sized and the whole plot re-margined. fullLayout._replotting must
// be set to false before these will work properly.
exports.finalDraw = function(gd) {
    Registry.getComponentMethod('shapes', 'draw')(gd);
    Registry.getComponentMethod('images', 'draw')(gd);
    Registry.getComponentMethod('annotations', 'draw')(gd);
    // TODO: rangesliders really belong in marginPushers but they need to be
    // drawn after data - can we at least get the margin pushing part separated
    // out and done earlier?
    Registry.getComponentMethod('rangeslider', 'draw')(gd);
    // TODO: rangeselector only needs to be here (in addition to drawMarginPushers)
    // because the margins need to be fully determined before we can call
    // autorange and update axis ranges (which rangeselector needs to know which
    // button is active). Can we break out its automargin step from its draw step?
    Registry.getComponentMethod('rangeselector', 'draw')(gd);
};

exports.drawMarginPushers = function(gd) {
    Registry.getComponentMethod('legend', 'draw')(gd);
    Registry.getComponentMethod('rangeselector', 'draw')(gd);
    Registry.getComponentMethod('sliders', 'draw')(gd);
    Registry.getComponentMethod('updatemenus', 'draw')(gd);
    Registry.getComponentMethod('colorbar', 'draw')(gd);
};
