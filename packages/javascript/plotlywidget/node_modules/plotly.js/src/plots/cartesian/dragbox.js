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
var supportsPassive = require('has-passive-events');

var Registry = require('../../registry');
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');
var Fx = require('../../components/fx');
var Axes = require('./axes');
var setCursor = require('../../lib/setcursor');
var dragElement = require('../../components/dragelement');
var FROM_TL = require('../../constants/alignment').FROM_TL;
var clearGlCanvases = require('../../lib/clear_gl_canvases');
var redrawReglTraces = require('../../plot_api/subroutines').redrawReglTraces;

var Plots = require('../plots');

var getFromId = require('./axis_ids').getFromId;
var prepSelect = require('./select').prepSelect;
var clearSelect = require('./select').clearSelect;
var selectOnClick = require('./select').selectOnClick;
var scaleZoom = require('./scale_zoom');

var constants = require('./constants');
var MINDRAG = constants.MINDRAG;
var MINZOOM = constants.MINZOOM;

// flag for showing "doubleclick to zoom out" only at the beginning
var SHOWZOOMOUTTIP = true;

// dragBox: create an element to drag one or more axis ends
// inputs:
//      plotinfo - which subplot are we making dragboxes on?
//      x,y,w,h - left, top, width, height of the box
//      ns - how does this drag the vertical axis?
//          'n' - top only
//          's' - bottom only
//          'ns' - top and bottom together, difference unchanged
//      ew - same for horizontal axis
function makeDragBox(gd, plotinfo, x, y, w, h, ns, ew) {
    // mouseDown stores ms of first mousedown event in the last
    // DBLCLICKDELAY ms on the drag bars
    // numClicks stores how many mousedowns have been seen
    // within DBLCLICKDELAY so we can check for click or doubleclick events
    // dragged stores whether a drag has occurred, so we don't have to
    // redraw unnecessarily, ie if no move bigger than MINDRAG or MINZOOM px
    var zoomlayer = gd._fullLayout._zoomlayer;
    var isMainDrag = (ns + ew === 'nsew');
    var singleEnd = (ns + ew).length === 1;

    // main subplot x and y (i.e. found in plotinfo - the main ones)
    var xa0, ya0;
    // {ax._id: ax} hash objects
    var xaHash, yaHash;
    // xaHash/yaHash values (arrays)
    var xaxes, yaxes;
    // main axis offsets
    var xs, ys;
    // main axis lengths
    var pw, ph;
    // contains keys 'xaHash', 'yaHash', 'xaxes', and 'yaxes'
    // which are the x/y {ax._id: ax} hash objects and their values
    // for linked axis relative to this subplot
    var links;
    // similar to `links` but for matching axes
    var matches;
    // set to ew/ns val when active, set to '' when inactive
    var xActive, yActive;
    // are all axes in this subplot are fixed?
    var allFixedRanges;
    // do we need to edit x/y ranges?
    var editX, editY;
    // graph-wide optimization flags
    var hasScatterGl, hasSplom, hasSVG;
    // collected changes to be made to the plot by relayout at the end
    var updates = {};

    function recomputeAxisLists() {
        xa0 = plotinfo.xaxis;
        ya0 = plotinfo.yaxis;
        pw = xa0._length;
        ph = ya0._length;
        xs = xa0._offset;
        ys = ya0._offset;

        xaHash = {};
        xaHash[xa0._id] = xa0;
        yaHash = {};
        yaHash[ya0._id] = ya0;

        // if we're dragging two axes at once, also drag overlays
        if(ns && ew) {
            var overlays = plotinfo.overlays;
            for(var i = 0; i < overlays.length; i++) {
                var xa = overlays[i].xaxis;
                xaHash[xa._id] = xa;
                var ya = overlays[i].yaxis;
                yaHash[ya._id] = ya;
            }
        }

        xaxes = hashValues(xaHash);
        yaxes = hashValues(yaHash);
        xActive = isDirectionActive(xaxes, ew);
        yActive = isDirectionActive(yaxes, ns);
        allFixedRanges = !yActive && !xActive;

        links = calcLinks(gd, gd._fullLayout._axisConstraintGroups, xaHash, yaHash);
        matches = calcLinks(gd, gd._fullLayout._axisMatchGroups, xaHash, yaHash);
        editX = ew || links.isSubplotConstrained || matches.isSubplotConstrained;
        editY = ns || links.isSubplotConstrained || matches.isSubplotConstrained;

        var fullLayout = gd._fullLayout;
        hasScatterGl = fullLayout._has('scattergl');
        hasSplom = fullLayout._has('splom');
        hasSVG = fullLayout._has('svg');
    }

    recomputeAxisLists();

    var cursor = getDragCursor(yActive + xActive, gd._fullLayout.dragmode, isMainDrag);
    var dragger = makeRectDragger(plotinfo, ns + ew + 'drag', cursor, x, y, w, h);

    // still need to make the element if the axes are disabled
    // but nuke its events (except for maindrag which needs them for hover)
    // and stop there
    if(allFixedRanges && !isMainDrag) {
        dragger.onmousedown = null;
        dragger.style.pointerEvents = 'none';
        return dragger;
    }

    var dragOptions = {
        element: dragger,
        gd: gd,
        plotinfo: plotinfo
    };

    dragOptions.prepFn = function(e, startX, startY) {
        var dragModePrev = dragOptions.dragmode;
        var dragModeNow = gd._fullLayout.dragmode;
        if(dragModeNow !== dragModePrev) {
            dragOptions.dragmode = dragModeNow;
        }

        recomputeAxisLists();

        if(!allFixedRanges) {
            if(isMainDrag) {
                // main dragger handles all drag modes, and changes
                // to pan (or to zoom if it already is pan) on shift
                if(e.shiftKey) {
                    if(dragModeNow === 'pan') dragModeNow = 'zoom';
                    else if(!isSelectOrLasso(dragModeNow)) dragModeNow = 'pan';
                } else if(e.ctrlKey) {
                    dragModeNow = 'pan';
                }
            } else {
                // all other draggers just pan
                dragModeNow = 'pan';
            }
        }

        if(dragModeNow === 'lasso') dragOptions.minDrag = 1;
        else dragOptions.minDrag = undefined;

        if(isSelectOrLasso(dragModeNow)) {
            dragOptions.xaxes = xaxes;
            dragOptions.yaxes = yaxes;
            // this attaches moveFn, clickFn, doneFn on dragOptions
            prepSelect(e, startX, startY, dragOptions, dragModeNow);
        } else {
            dragOptions.clickFn = clickFn;
            if(isSelectOrLasso(dragModePrev)) {
                // TODO Fix potential bug
                // Note: clearing / resetting selection state only happens, when user
                // triggers at least one interaction in pan/zoom mode. Otherwise, the
                // select/lasso outlines are deleted (in plots.js.cleanPlot) but the selection
                // cache isn't cleared. So when the user switches back to select/lasso and
                // 'adds to a selection' with Shift, the "old", seemingly removed outlines
                // are redrawn again because the selection cache still holds their coordinates.
                // However, this isn't easily solved, since plots.js would need
                // to have a reference to the dragOptions object (which holds the
                // selection cache).
                clearAndResetSelect();
            }

            if(!allFixedRanges) {
                if(dragModeNow === 'zoom') {
                    dragOptions.moveFn = zoomMove;
                    dragOptions.doneFn = zoomDone;

                    // zoomMove takes care of the threshold, but we need to
                    // minimize this so that constrained zoom boxes will flip
                    // orientation at the right place
                    dragOptions.minDrag = 1;

                    zoomPrep(e, startX, startY);
                } else if(dragModeNow === 'pan') {
                    dragOptions.moveFn = plotDrag;
                    dragOptions.doneFn = dragTail;
                }
            }
        }

        gd._fullLayout._redrag = function() {
            var dragDataNow = gd._dragdata;

            if(dragDataNow && dragDataNow.element === dragger) {
                var dragModeNow = gd._fullLayout.dragmode;

                if(!isSelectOrLasso(dragModeNow)) {
                    recomputeAxisLists();
                    updateSubplots([0, 0, pw, ph]);
                    dragOptions.moveFn(dragDataNow.dx, dragDataNow.dy);
                }

                // TODO should we try to "re-select" under select/lasso modes?
                // probably best to wait for https://github.com/plotly/plotly.js/issues/1851
            }
        };
    };

    function clearAndResetSelect() {
        // clear selection polygon cache (if any)
        dragOptions.plotinfo.selection = false;
        // clear selection outlines
        clearSelect(gd);
    }

    function clickFn(numClicks, evt) {
        var clickmode = gd._fullLayout.clickmode;

        removeZoombox(gd);

        if(numClicks === 2 && !singleEnd) doubleClick();

        if(isMainDrag) {
            if(clickmode.indexOf('select') > -1) {
                selectOnClick(evt, gd, xaxes, yaxes, plotinfo.id, dragOptions);
            }

            if(clickmode.indexOf('event') > -1) {
                Fx.click(gd, evt, plotinfo.id);
            }
        } else if(numClicks === 1 && singleEnd) {
            var ax = ns ? ya0 : xa0;
            var end = (ns === 's' || ew === 'w') ? 0 : 1;
            var attrStr = ax._name + '.range[' + end + ']';
            var initialText = getEndText(ax, end);
            var hAlign = 'left';
            var vAlign = 'middle';

            if(ax.fixedrange) return;

            if(ns) {
                vAlign = (ns === 'n') ? 'top' : 'bottom';
                if(ax.side === 'right') hAlign = 'right';
            } else if(ew === 'e') hAlign = 'right';

            if(gd._context.showAxisRangeEntryBoxes) {
                d3.select(dragger)
                    .call(svgTextUtils.makeEditable, {
                        gd: gd,
                        immediate: true,
                        background: gd._fullLayout.paper_bgcolor,
                        text: String(initialText),
                        fill: ax.tickfont ? ax.tickfont.color : '#444',
                        horizontalAlign: hAlign,
                        verticalAlign: vAlign
                    })
                    .on('edit', function(text) {
                        var v = ax.d2r(text);
                        if(v !== undefined) {
                            Registry.call('_guiRelayout', gd, attrStr, v);
                        }
                    });
            }
        }
    }

    dragElement.init(dragOptions);

    // x/y px position at start of drag
    var x0, y0;
    // bbox object of the zoombox
    var box;
    // luminance of bg behind zoombox
    var lum;
    // zoombox path outline
    var path0;
    // is zoombox dimmed (during drag)
    var dimmed;
    // 'x'-only, 'y' or 'xy' zooming
    var zoomMode;
    // zoombox d3 selection
    var zb;
    // zoombox corner d3 selection
    var corners;
    // zoom takes over minDrag, so it also has to take over gd._dragged
    var zoomDragged;

    function zoomPrep(e, startX, startY) {
        var dragBBox = dragger.getBoundingClientRect();
        x0 = startX - dragBBox.left;
        y0 = startY - dragBBox.top;
        box = {l: x0, r: x0, w: 0, t: y0, b: y0, h: 0};
        lum = gd._hmpixcount ?
            (gd._hmlumcount / gd._hmpixcount) :
            tinycolor(gd._fullLayout.plot_bgcolor).getLuminance();
        path0 = 'M0,0H' + pw + 'V' + ph + 'H0V0';
        dimmed = false;
        zoomMode = 'xy';
        zoomDragged = false;
        zb = makeZoombox(zoomlayer, lum, xs, ys, path0);
        corners = makeCorners(zoomlayer, xs, ys);
    }

    function zoomMove(dx0, dy0) {
        if(gd._transitioningWithDuration) {
            return false;
        }

        var x1 = Math.max(0, Math.min(pw, dx0 + x0));
        var y1 = Math.max(0, Math.min(ph, dy0 + y0));
        var dx = Math.abs(x1 - x0);
        var dy = Math.abs(y1 - y0);

        box.l = Math.min(x0, x1);
        box.r = Math.max(x0, x1);
        box.t = Math.min(y0, y1);
        box.b = Math.max(y0, y1);

        function noZoom() {
            zoomMode = '';
            box.r = box.l;
            box.t = box.b;
            corners.attr('d', 'M0,0Z');
        }

        if(links.isSubplotConstrained) {
            if(dx > MINZOOM || dy > MINZOOM) {
                zoomMode = 'xy';
                if(dx / pw > dy / ph) {
                    dy = dx * ph / pw;
                    if(y0 > y1) box.t = y0 - dy;
                    else box.b = y0 + dy;
                } else {
                    dx = dy * pw / ph;
                    if(x0 > x1) box.l = x0 - dx;
                    else box.r = x0 + dx;
                }
                corners.attr('d', xyCorners(box));
            } else {
                noZoom();
            }
        } else if(matches.isSubplotConstrained) {
            if(dx > MINZOOM || dy > MINZOOM) {
                zoomMode = 'xy';

                var r0 = Math.min(box.l / pw, (ph - box.b) / ph);
                var r1 = Math.max(box.r / pw, (ph - box.t) / ph);

                box.l = r0 * pw;
                box.r = r1 * pw;
                box.b = (1 - r0) * ph;
                box.t = (1 - r1) * ph;
                corners.attr('d', xyCorners(box));
            } else {
                noZoom();
            }
        } else if(!yActive || dy < Math.min(Math.max(dx * 0.6, MINDRAG), MINZOOM)) {
            // look for small drags in one direction or the other,
            // and only drag the other axis

            if(dx < MINDRAG || !xActive) {
                noZoom();
            } else {
                box.t = 0;
                box.b = ph;
                zoomMode = 'x';
                corners.attr('d', xCorners(box, y0));
            }
        } else if(!xActive || dx < Math.min(dy * 0.6, MINZOOM)) {
            box.l = 0;
            box.r = pw;
            zoomMode = 'y';
            corners.attr('d', yCorners(box, x0));
        } else {
            zoomMode = 'xy';
            corners.attr('d', xyCorners(box));
        }
        box.w = box.r - box.l;
        box.h = box.b - box.t;

        if(zoomMode) zoomDragged = true;
        gd._dragged = zoomDragged;

        updateZoombox(zb, corners, box, path0, dimmed, lum);
        computeZoomUpdates();
        gd.emit('plotly_relayouting', updates);
        dimmed = true;
    }

    function computeZoomUpdates() {
        // TODO: edit linked axes in zoomAxRanges and in dragTail
        if(zoomMode === 'xy' || zoomMode === 'x') {
            zoomAxRanges(xaxes, box.l / pw, box.r / pw, updates, links.xaxes);
            updateMatchedAxRange('x', updates);
        }
        if(zoomMode === 'xy' || zoomMode === 'y') {
            zoomAxRanges(yaxes, (ph - box.b) / ph, (ph - box.t) / ph, updates, links.yaxes);
            updateMatchedAxRange('y', updates);
        }
    }

    function zoomDone() {
        updates = {};

        // more strict than dragged, which allows you to come back to where you started
        // and still count as dragged
        if(Math.min(box.h, box.w) < MINDRAG * 2) {
            return removeZoombox(gd);
        }

        computeZoomUpdates();

        removeZoombox(gd);
        dragTail();
        showDoubleClickNotifier(gd);
    }

    // scroll zoom, on all draggers except corners
    var scrollViewBox = [0, 0, pw, ph];
    // wait a little after scrolling before redrawing
    var redrawTimer = null;
    var REDRAWDELAY = constants.REDRAWDELAY;
    var mainplot = plotinfo.mainplot ? gd._fullLayout._plots[plotinfo.mainplot] : plotinfo;

    function zoomWheel(e) {
        // deactivate mousewheel scrolling on embedded graphs
        // devs can override this with layout._enablescrollzoom,
        // but _ ensures this setting won't leave their page
        if(!gd._context._scrollZoom.cartesian && !gd._fullLayout._enablescrollzoom) {
            return;
        }

        clearAndResetSelect();

        // If a transition is in progress, then disable any behavior:
        if(gd._transitioningWithDuration) {
            e.preventDefault();
            e.stopPropagation();
            return;
        }

        recomputeAxisLists();

        clearTimeout(redrawTimer);

        var wheelDelta = -e.deltaY;
        if(!isFinite(wheelDelta)) wheelDelta = e.wheelDelta / 10;
        if(!isFinite(wheelDelta)) {
            Lib.log('Did not find wheel motion attributes: ', e);
            return;
        }

        var zoom = Math.exp(-Math.min(Math.max(wheelDelta, -20), 20) / 200);
        var gbb = mainplot.draglayer.select('.nsewdrag').node().getBoundingClientRect();
        var xfrac = (e.clientX - gbb.left) / gbb.width;
        var yfrac = (gbb.bottom - e.clientY) / gbb.height;
        var i;

        function zoomWheelOneAxis(ax, centerFraction, zoom) {
            if(ax.fixedrange) return;

            var axRange = Lib.simpleMap(ax.range, ax.r2l);
            var v0 = axRange[0] + (axRange[1] - axRange[0]) * centerFraction;
            function doZoom(v) { return ax.l2r(v0 + (v - v0) * zoom); }
            ax.range = axRange.map(doZoom);
        }

        if(editX) {
            // if we're only zooming this axis because of constraints,
            // zoom it about the center
            if(!ew) xfrac = 0.5;

            for(i = 0; i < xaxes.length; i++) {
                zoomWheelOneAxis(xaxes[i], xfrac, zoom);
            }
            updateMatchedAxRange('x');

            scrollViewBox[2] *= zoom;
            scrollViewBox[0] += scrollViewBox[2] * xfrac * (1 / zoom - 1);
        }
        if(editY) {
            if(!ns) yfrac = 0.5;

            for(i = 0; i < yaxes.length; i++) {
                zoomWheelOneAxis(yaxes[i], yfrac, zoom);
            }
            updateMatchedAxRange('y');

            scrollViewBox[3] *= zoom;
            scrollViewBox[1] += scrollViewBox[3] * (1 - yfrac) * (1 / zoom - 1);
        }

        // viewbox redraw at first
        updateSubplots(scrollViewBox);
        ticksAndAnnotations();

        gd.emit('plotly_relayouting', updates);

        // then replot after a delay to make sure
        // no more scrolling is coming
        redrawTimer = setTimeout(function() {
            scrollViewBox = [0, 0, pw, ph];
            dragTail();
        }, REDRAWDELAY);

        e.preventDefault();
        return;
    }

    // everything but the corners gets wheel zoom
    if(ns.length * ew.length !== 1) {
        attachWheelEventHandler(dragger, zoomWheel);
    }

    // plotDrag: move the plot in response to a drag
    function plotDrag(dx, dy) {
        // If a transition is in progress, then disable any behavior:
        if(gd._transitioningWithDuration) {
            return;
        }

        // prevent axis drawing from monkeying with margins until we're done
        gd._fullLayout._replotting = true;

        if(xActive === 'ew' || yActive === 'ns') {
            if(xActive) {
                dragAxList(xaxes, dx);
                updateMatchedAxRange('x');
            }
            if(yActive) {
                dragAxList(yaxes, dy);
                updateMatchedAxRange('y');
            }
            updateSubplots([xActive ? -dx : 0, yActive ? -dy : 0, pw, ph]);
            ticksAndAnnotations();
            gd.emit('plotly_relayouting', updates);
            return;
        }

        // dz: set a new value for one end (0 or 1) of an axis array axArray,
        // and return a pixel shift for that end for the viewbox
        // based on pixel drag distance d
        // TODO: this makes (generally non-fatal) errors when you get
        // near floating point limits
        function dz(axArray, end, d) {
            var otherEnd = 1 - end;
            var movedAx;
            var newLinearizedEnd;
            for(var i = 0; i < axArray.length; i++) {
                var axi = axArray[i];
                if(axi.fixedrange) continue;
                movedAx = axi;
                newLinearizedEnd = axi._rl[otherEnd] +
                    (axi._rl[end] - axi._rl[otherEnd]) / dZoom(d / axi._length);
                var newEnd = axi.l2r(newLinearizedEnd);

                // if l2r comes back false or undefined, it means we've dragged off
                // the end of valid ranges - so stop.
                if(newEnd !== false && newEnd !== undefined) axi.range[end] = newEnd;
            }
            return movedAx._length * (movedAx._rl[end] - newLinearizedEnd) /
                (movedAx._rl[end] - movedAx._rl[otherEnd]);
        }

        if(links.isSubplotConstrained && xActive && yActive) {
            // dragging a corner of a constrained subplot:
            // respect the fixed corner, but harmonize dx and dy
            var dxySign = ((xActive === 'w') === (yActive === 'n')) ? 1 : -1;
            var dxyFraction = (dx / pw + dxySign * dy / ph) / 2;
            dx = dxyFraction * pw;
            dy = dxySign * dxyFraction * ph;
        }

        if(xActive === 'w') dx = dz(xaxes, 0, dx);
        else if(xActive === 'e') dx = dz(xaxes, 1, -dx);
        else if(!xActive) dx = 0;

        if(yActive === 'n') dy = dz(yaxes, 1, dy);
        else if(yActive === 's') dy = dz(yaxes, 0, -dy);
        else if(!yActive) dy = 0;

        var xStart = (xActive === 'w') ? dx : 0;
        var yStart = (yActive === 'n') ? dy : 0;

        if(links.isSubplotConstrained) {
            var i;
            if(!xActive && yActive.length === 1) {
                // dragging one end of the y axis of a constrained subplot
                // scale the other axis the same about its middle
                for(i = 0; i < xaxes.length; i++) {
                    xaxes[i].range = xaxes[i]._r.slice();
                    scaleZoom(xaxes[i], 1 - dy / ph);
                }
                dx = dy * pw / ph;
                xStart = dx / 2;
            }
            if(!yActive && xActive.length === 1) {
                for(i = 0; i < yaxes.length; i++) {
                    yaxes[i].range = yaxes[i]._r.slice();
                    scaleZoom(yaxes[i], 1 - dx / pw);
                }
                dy = dx * ph / pw;
                yStart = dy / 2;
            }
        }

        updateMatchedAxRange('x');
        updateMatchedAxRange('y');
        updateSubplots([xStart, yStart, pw - dx, ph - dy]);
        ticksAndAnnotations();
        gd.emit('plotly_relayouting', updates);
    }

    function updateMatchedAxRange(axLetter, out) {
        var matchedAxes = matches.isSubplotConstrained ?
            {x: yaxes, y: xaxes}[axLetter] :
            matches[axLetter + 'axes'];

        var constrainedAxes = matches.isSubplotConstrained ?
            {x: xaxes, y: yaxes}[axLetter] :
            [];

        for(var i = 0; i < matchedAxes.length; i++) {
            var ax = matchedAxes[i];
            var axId = ax._id;
            var axId2 = matches.xLinks[axId] || matches.yLinks[axId];
            var ax2 = constrainedAxes[0] || xaHash[axId2] || yaHash[axId2];

            if(ax2) {
                var rng = ax2.range;
                if(out) {
                    out[ax._name + '.range[0]'] = rng[0];
                    out[ax._name + '.range[1]'] = rng[1];
                } else {
                    ax.range = rng;
                }
            }
        }
    }

    // Draw ticks and annotations (and other components) when ranges change.
    // Also records the ranges that have changed for use by update at the end.
    function ticksAndAnnotations() {
        var activeAxIds = [];
        var i;

        function pushActiveAxIds(axList) {
            for(i = 0; i < axList.length; i++) {
                if(!axList[i].fixedrange) activeAxIds.push(axList[i]._id);
            }
        }

        if(editX) {
            pushActiveAxIds(xaxes);
            pushActiveAxIds(links.xaxes);
            pushActiveAxIds(matches.xaxes);
        }
        if(editY) {
            pushActiveAxIds(yaxes);
            pushActiveAxIds(links.yaxes);
            pushActiveAxIds(matches.yaxes);
        }

        updates = {};
        for(i = 0; i < activeAxIds.length; i++) {
            var axId = activeAxIds[i];
            var ax = getFromId(gd, axId);
            Axes.drawOne(gd, ax, {skipTitle: true});
            updates[ax._name + '.range[0]'] = ax.range[0];
            updates[ax._name + '.range[1]'] = ax.range[1];
        }

        Axes.redrawComponents(gd, activeAxIds);
    }

    function doubleClick() {
        if(gd._transitioningWithDuration) return;

        var doubleClickConfig = gd._context.doubleClick;

        var axList = [];
        if(xActive) axList = axList.concat(xaxes);
        if(yActive) axList = axList.concat(yaxes);
        if(matches.xaxes) axList = axList.concat(matches.xaxes);
        if(matches.yaxes) axList = axList.concat(matches.yaxes);

        var attrs = {};
        var ax, i, rangeInitial;

        // For reset+autosize mode:
        // If *any* of the main axes is not at its initial range
        // (or autoranged, if we have no initial range, to match the logic in
        // doubleClickConfig === 'reset' below), we reset.
        // If they are *all* at their initial ranges, then we autosize.
        if(doubleClickConfig === 'reset+autosize') {
            doubleClickConfig = 'autosize';

            for(i = 0; i < axList.length; i++) {
                ax = axList[i];
                if((ax._rangeInitial && (
                        ax.range[0] !== ax._rangeInitial[0] ||
                        ax.range[1] !== ax._rangeInitial[1]
                    )) ||
                    (!ax._rangeInitial && !ax.autorange)
                ) {
                    doubleClickConfig = 'reset';
                    break;
                }
            }
        }

        if(doubleClickConfig === 'autosize') {
            // don't set the linked axes here, so relayout marks them as shrinkable
            // and we autosize just to the requested axis/axes
            for(i = 0; i < axList.length; i++) {
                ax = axList[i];
                if(!ax.fixedrange) attrs[ax._name + '.autorange'] = true;
            }
        } else if(doubleClickConfig === 'reset') {
            // when we're resetting, reset all linked axes too, so we get back
            // to the fully-auto-with-constraints situation
            if(xActive || links.isSubplotConstrained) axList = axList.concat(links.xaxes);
            if(yActive && !links.isSubplotConstrained) axList = axList.concat(links.yaxes);

            if(links.isSubplotConstrained) {
                if(!xActive) axList = axList.concat(xaxes);
                else if(!yActive) axList = axList.concat(yaxes);
            }

            for(i = 0; i < axList.length; i++) {
                ax = axList[i];

                if(!ax.fixedrange) {
                    if(!ax._rangeInitial) {
                        attrs[ax._name + '.autorange'] = true;
                    } else {
                        rangeInitial = ax._rangeInitial;
                        attrs[ax._name + '.range[0]'] = rangeInitial[0];
                        attrs[ax._name + '.range[1]'] = rangeInitial[1];
                    }
                }
            }
        }

        gd.emit('plotly_doubleclick', null);
        Registry.call('_guiRelayout', gd, attrs);
    }

    // dragTail - finish a drag event with a redraw
    function dragTail() {
        // put the subplot viewboxes back to default (Because we're going to)
        // be repositioning the data in the relayout. But DON'T call
        // ticksAndAnnotations again - it's unnecessary and would overwrite `updates`
        updateSubplots([0, 0, pw, ph]);

        // since we may have been redrawing some things during the drag, we may have
        // accumulated MathJax promises - wait for them before we relayout.
        Lib.syncOrAsync([
            Plots.previousPromises,
            function() {
                gd._fullLayout._replotting = false;
                Registry.call('_guiRelayout', gd, updates);
            }
        ], gd);
    }

    // updateSubplots - find all plot viewboxes that should be
    // affected by this drag, and update them. look for all plots
    // sharing an affected axis (including the one being dragged),
    // includes also scattergl and splom logic.
    function updateSubplots(viewBox) {
        var fullLayout = gd._fullLayout;
        var plotinfos = fullLayout._plots;
        var subplots = fullLayout._subplots.cartesian;
        var i, sp, xa, ya;

        if(hasSplom) {
            Registry.subplotsRegistry.splom.drag(gd);
        }

        if(hasScatterGl) {
            for(i = 0; i < subplots.length; i++) {
                sp = plotinfos[subplots[i]];
                xa = sp.xaxis;
                ya = sp.yaxis;

                if(sp._scene) {
                    var xrng = Lib.simpleMap(xa.range, xa.r2l);
                    var yrng = Lib.simpleMap(ya.range, ya.r2l);
                    sp._scene.update({range: [xrng[0], yrng[0], xrng[1], yrng[1]]});
                }
            }
        }

        if(hasSplom || hasScatterGl) {
            clearGlCanvases(gd);
            redrawReglTraces(gd);
        }

        if(hasSVG) {
            var xScaleFactor = viewBox[2] / xa0._length;
            var yScaleFactor = viewBox[3] / ya0._length;

            for(i = 0; i < subplots.length; i++) {
                sp = plotinfos[subplots[i]];
                xa = sp.xaxis;
                ya = sp.yaxis;

                var editX2 = editX && !xa.fixedrange && xaHash[xa._id];
                var editY2 = editY && !ya.fixedrange && yaHash[ya._id];

                var xScaleFactor2, yScaleFactor2;
                var clipDx, clipDy;

                if(editX2) {
                    xScaleFactor2 = xScaleFactor;
                    clipDx = ew ? viewBox[0] : getShift(xa, xScaleFactor2);
                } else if(matches.xaHash[xa._id]) {
                    xScaleFactor2 = xScaleFactor;
                    clipDx = viewBox[0] * xa._length / xa0._length;
                } else if(matches.yaHash[xa._id]) {
                    xScaleFactor2 = yScaleFactor;
                    clipDx = yActive === 'ns' ?
                        -viewBox[1] * xa._length / ya0._length :
                        getShift(xa, xScaleFactor2, {n: 'top', s: 'bottom'}[yActive]);
                } else {
                    xScaleFactor2 = getLinkedScaleFactor(xa, xScaleFactor, yScaleFactor);
                    clipDx = scaleAndGetShift(xa, xScaleFactor2);
                }

                if(editY2) {
                    yScaleFactor2 = yScaleFactor;
                    clipDy = ns ? viewBox[1] : getShift(ya, yScaleFactor2);
                } else if(matches.yaHash[ya._id]) {
                    yScaleFactor2 = yScaleFactor;
                    clipDy = viewBox[1] * ya._length / ya0._length;
                } else if(matches.xaHash[ya._id]) {
                    yScaleFactor2 = xScaleFactor;
                    clipDy = xActive === 'ew' ?
                        -viewBox[0] * ya._length / xa0._length :
                        getShift(ya, yScaleFactor2, {e: 'right', w: 'left'}[xActive]);
                } else {
                    yScaleFactor2 = getLinkedScaleFactor(ya, xScaleFactor, yScaleFactor);
                    clipDy = scaleAndGetShift(ya, yScaleFactor2);
                }

                // don't scale at all if neither axis is scalable here
                if(!xScaleFactor2 && !yScaleFactor2) {
                    continue;
                }

                // but if only one is, reset the other axis scaling
                if(!xScaleFactor2) xScaleFactor2 = 1;
                if(!yScaleFactor2) yScaleFactor2 = 1;

                var plotDx = xa._offset - clipDx / xScaleFactor2;
                var plotDy = ya._offset - clipDy / yScaleFactor2;

                // TODO could be more efficient here:
                // setTranslate and setScale do a lot of extra work
                // when working independently, should perhaps combine
                // them into a single routine.
                sp.clipRect
                    .call(Drawing.setTranslate, clipDx, clipDy)
                    .call(Drawing.setScale, xScaleFactor2, yScaleFactor2);

                sp.plot
                    .call(Drawing.setTranslate, plotDx, plotDy)
                    .call(Drawing.setScale, 1 / xScaleFactor2, 1 / yScaleFactor2);

                // apply an inverse scale to individual points to counteract
                // the scale of the trace group.
                // apply only when scale changes, as adjusting the scale of
                // all the points can be expansive.
                if(xScaleFactor2 !== sp.xScaleFactor || yScaleFactor2 !== sp.yScaleFactor) {
                    Drawing.setPointGroupScale(sp.zoomScalePts, xScaleFactor2, yScaleFactor2);
                    Drawing.setTextPointsScale(sp.zoomScaleTxt, xScaleFactor2, yScaleFactor2);
                }

                Drawing.hideOutsideRangePoints(sp.clipOnAxisFalseTraces, sp);

                // update x/y scaleFactor stash
                sp.xScaleFactor = xScaleFactor2;
                sp.yScaleFactor = yScaleFactor2;
            }
        }
    }

    // Find the appropriate scaling for this axis, if it's linked to the
    // dragged axes by constraints. 0 is special, it means this axis shouldn't
    // ever be scaled (will be converted to 1 if the other axis is scaled)
    function getLinkedScaleFactor(ax, xScaleFactor, yScaleFactor) {
        if(ax.fixedrange) return 0;

        if(editX && links.xaHash[ax._id]) {
            return xScaleFactor;
        }
        if(editY && (links.isSubplotConstrained ? links.xaHash : links.yaHash)[ax._id]) {
            return yScaleFactor;
        }
        return 0;
    }

    function scaleAndGetShift(ax, scaleFactor) {
        if(scaleFactor) {
            ax.range = ax._r.slice();
            scaleZoom(ax, scaleFactor);
            return getShift(ax, scaleFactor);
        }
        return 0;
    }

    function getShift(ax, scaleFactor, from) {
        return ax._length * (1 - scaleFactor) * FROM_TL[from || ax.constraintoward || 'middle'];
    }

    return dragger;
}

function makeDragger(plotinfo, nodeName, dragClass, cursor) {
    var dragger3 = Lib.ensureSingle(plotinfo.draglayer, nodeName, dragClass, function(s) {
        s.classed('drag', true)
            .style({fill: 'transparent', 'stroke-width': 0})
            .attr('data-subplot', plotinfo.id);
    });

    dragger3.call(setCursor, cursor);

    return dragger3.node();
}

function makeRectDragger(plotinfo, dragClass, cursor, x, y, w, h) {
    var dragger = makeDragger(plotinfo, 'rect', dragClass, cursor);
    d3.select(dragger).call(Drawing.setRect, x, y, w, h);
    return dragger;
}

function isDirectionActive(axList, activeVal) {
    for(var i = 0; i < axList.length; i++) {
        if(!axList[i].fixedrange) return activeVal;
    }
    return '';
}

function getEndText(ax, end) {
    var initialVal = ax.range[end];
    var diff = Math.abs(initialVal - ax.range[1 - end]);
    var dig;

    // TODO: this should basically be ax.r2d but we're doing extra
    // rounding here... can we clean up at all?
    if(ax.type === 'date') {
        return initialVal;
    } else if(ax.type === 'log') {
        dig = Math.ceil(Math.max(0, -Math.log(diff) / Math.LN10)) + 3;
        return d3.format('.' + dig + 'g')(Math.pow(10, initialVal));
    } else { // linear numeric (or category... but just show numbers here)
        dig = Math.floor(Math.log(Math.abs(initialVal)) / Math.LN10) -
            Math.floor(Math.log(diff) / Math.LN10) + 4;
        return d3.format('.' + String(dig) + 'g')(initialVal);
    }
}

function zoomAxRanges(axList, r0Fraction, r1Fraction, updates, linkedAxes) {
    for(var i = 0; i < axList.length; i++) {
        var axi = axList[i];
        if(axi.fixedrange) continue;

        var axRangeLinear0 = axi._rl[0];
        var axRangeLinearSpan = axi._rl[1] - axRangeLinear0;
        axi.range = [
            axi.l2r(axRangeLinear0 + axRangeLinearSpan * r0Fraction),
            axi.l2r(axRangeLinear0 + axRangeLinearSpan * r1Fraction)
        ];

        updates[axi._name + '.range[0]'] = axi.range[0];
        updates[axi._name + '.range[1]'] = axi.range[1];
    }

    // zoom linked axes about their centers
    if(linkedAxes && linkedAxes.length) {
        var linkedR0Fraction = (r0Fraction + (1 - r1Fraction)) / 2;
        zoomAxRanges(linkedAxes, linkedR0Fraction, 1 - linkedR0Fraction, updates, [], []);
    }
}

function dragAxList(axList, pix) {
    for(var i = 0; i < axList.length; i++) {
        var axi = axList[i];
        if(!axi.fixedrange) {
            axi.range = [
                axi.l2r(axi._rl[0] - pix / axi._m),
                axi.l2r(axi._rl[1] - pix / axi._m)
            ];
        }
    }
}

// common transform for dragging one end of an axis
// d>0 is compressing scale (cursor is over the plot,
//  the axis end should move with the cursor)
// d<0 is expanding (cursor is off the plot, axis end moves
//  nonlinearly so you can expand far)
function dZoom(d) {
    return 1 - ((d >= 0) ? Math.min(d, 0.9) :
        1 / (1 / Math.max(d, -0.3) + 3.222));
}

function getDragCursor(nsew, dragmode, isMainDrag) {
    if(!nsew) return 'pointer';
    if(nsew === 'nsew') {
        // in this case here, clear cursor and
        // use the cursor style set on <g .draglayer>
        if(isMainDrag) return '';
        if(dragmode === 'pan') return 'move';
        return 'crosshair';
    }
    return nsew.toLowerCase() + '-resize';
}

function makeZoombox(zoomlayer, lum, xs, ys, path0) {
    return zoomlayer.append('path')
        .attr('class', 'zoombox')
        .style({
            'fill': lum > 0.2 ? 'rgba(0,0,0,0)' : 'rgba(255,255,255,0)',
            'stroke-width': 0
        })
        .attr('transform', 'translate(' + xs + ', ' + ys + ')')
        .attr('d', path0 + 'Z');
}

function makeCorners(zoomlayer, xs, ys) {
    return zoomlayer.append('path')
        .attr('class', 'zoombox-corners')
        .style({
            fill: Color.background,
            stroke: Color.defaultLine,
            'stroke-width': 1,
            opacity: 0
        })
        .attr('transform', 'translate(' + xs + ', ' + ys + ')')
        .attr('d', 'M0,0Z');
}

function updateZoombox(zb, corners, box, path0, dimmed, lum) {
    zb.attr('d',
        path0 + 'M' + (box.l) + ',' + (box.t) + 'v' + (box.h) +
        'h' + (box.w) + 'v-' + (box.h) + 'h-' + (box.w) + 'Z');
    transitionZoombox(zb, corners, dimmed, lum);
}

function transitionZoombox(zb, corners, dimmed, lum) {
    if(!dimmed) {
        zb.transition()
            .style('fill', lum > 0.2 ? 'rgba(0,0,0,0.4)' :
                'rgba(255,255,255,0.3)')
            .duration(200);
        corners.transition()
            .style('opacity', 1)
            .duration(200);
    }
}

function removeZoombox(gd) {
    d3.select(gd)
        .selectAll('.zoombox,.js-zoombox-backdrop,.js-zoombox-menu,.zoombox-corners')
        .remove();
}

function showDoubleClickNotifier(gd) {
    if(SHOWZOOMOUTTIP && gd.data && gd._context.showTips) {
        Lib.notifier(Lib._(gd, 'Double-click to zoom back out'), 'long');
        SHOWZOOMOUTTIP = false;
    }
}

function isSelectOrLasso(dragmode) {
    return dragmode === 'lasso' || dragmode === 'select';
}

function xCorners(box, y0) {
    return 'M' +
        (box.l - 0.5) + ',' + (y0 - MINZOOM - 0.5) +
        'h-3v' + (2 * MINZOOM + 1) + 'h3ZM' +
        (box.r + 0.5) + ',' + (y0 - MINZOOM - 0.5) +
        'h3v' + (2 * MINZOOM + 1) + 'h-3Z';
}

function yCorners(box, x0) {
    return 'M' +
        (x0 - MINZOOM - 0.5) + ',' + (box.t - 0.5) +
        'v-3h' + (2 * MINZOOM + 1) + 'v3ZM' +
        (x0 - MINZOOM - 0.5) + ',' + (box.b + 0.5) +
        'v3h' + (2 * MINZOOM + 1) + 'v-3Z';
}

function xyCorners(box) {
    var clen = Math.floor(Math.min(box.b - box.t, box.r - box.l, MINZOOM) / 2);
    return 'M' +
        (box.l - 3.5) + ',' + (box.t - 0.5 + clen) + 'h3v' + (-clen) +
            'h' + clen + 'v-3h-' + (clen + 3) + 'ZM' +
        (box.r + 3.5) + ',' + (box.t - 0.5 + clen) + 'h-3v' + (-clen) +
            'h' + (-clen) + 'v-3h' + (clen + 3) + 'ZM' +
        (box.r + 3.5) + ',' + (box.b + 0.5 - clen) + 'h-3v' + clen +
            'h' + (-clen) + 'v3h' + (clen + 3) + 'ZM' +
        (box.l - 3.5) + ',' + (box.b + 0.5 - clen) + 'h3v' + clen +
            'h' + clen + 'v3h-' + (clen + 3) + 'Z';
}

function calcLinks(gd, groups, xaHash, yaHash) {
    var isSubplotConstrained = false;
    var xLinks = {};
    var yLinks = {};
    var xID, yID, xLinkID, yLinkID;

    for(var i = 0; i < groups.length; i++) {
        var group = groups[i];
        // check if any of the x axes we're dragging is in this constraint group
        for(xID in xaHash) {
            if(group[xID]) {
                // put the rest of these axes into xLinks, if we're not already
                // dragging them, so we know to scale these axes automatically too
                // to match the changes in the dragged x axes
                for(xLinkID in group) {
                    if(!(xLinkID.charAt(0) === 'x' ? xaHash : yaHash)[xLinkID]) {
                        xLinks[xLinkID] = xID;
                    }
                }

                // check if the x and y axes of THIS drag are linked
                for(yID in yaHash) {
                    if(group[yID]) isSubplotConstrained = true;
                }
            }
        }

        // now check if any of the y axes we're dragging is in this constraint group
        // only look for outside links, as we've already checked for links within the dragger
        for(yID in yaHash) {
            if(group[yID]) {
                for(yLinkID in group) {
                    if(!(yLinkID.charAt(0) === 'x' ? xaHash : yaHash)[yLinkID]) {
                        yLinks[yLinkID] = yID;
                    }
                }
            }
        }
    }

    if(isSubplotConstrained) {
        // merge xLinks and yLinks if the subplot is constrained,
        // since we'll always apply both anyway and the two will contain
        // duplicates
        Lib.extendFlat(xLinks, yLinks);
        yLinks = {};
    }

    var xaHashLinked = {};
    var xaxesLinked = [];
    for(xLinkID in xLinks) {
        var xa = getFromId(gd, xLinkID);
        xaxesLinked.push(xa);
        xaHashLinked[xa._id] = xa;
    }

    var yaHashLinked = {};
    var yaxesLinked = [];
    for(yLinkID in yLinks) {
        var ya = getFromId(gd, yLinkID);
        yaxesLinked.push(ya);
        yaHashLinked[ya._id] = ya;
    }

    return {
        xaHash: xaHashLinked,
        yaHash: yaHashLinked,
        xaxes: xaxesLinked,
        yaxes: yaxesLinked,
        xLinks: xLinks,
        yLinks: yLinks,
        isSubplotConstrained: isSubplotConstrained
    };
}

// still seems to be some confusion about onwheel vs onmousewheel...
function attachWheelEventHandler(element, handler) {
    if(!supportsPassive) {
        if(element.onwheel !== undefined) element.onwheel = handler;
        else if(element.onmousewheel !== undefined) element.onmousewheel = handler;
    } else {
        var wheelEventName = element.onwheel !== undefined ? 'wheel' : 'mousewheel';

        if(element._onwheel) {
            element.removeEventListener(wheelEventName, element._onwheel);
        }
        element._onwheel = handler;

        element.addEventListener(wheelEventName, handler, {passive: false});
    }
}

function hashValues(hash) {
    var out = [];
    for(var k in hash) out.push(hash[k]);
    return out;
}

module.exports = {
    makeDragBox: makeDragBox,

    makeDragger: makeDragger,
    makeRectDragger: makeRectDragger,
    makeZoombox: makeZoombox,
    makeCorners: makeCorners,

    updateZoombox: updateZoombox,
    xyCorners: xyCorners,
    transitionZoombox: transitionZoombox,
    removeZoombox: removeZoombox,
    showDoubleClickNotifier: showDoubleClickNotifier,

    attachWheelEventHandler: attachWheelEventHandler
};
