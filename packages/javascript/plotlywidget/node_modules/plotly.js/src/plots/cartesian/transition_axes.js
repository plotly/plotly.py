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
var Drawing = require('../../components/drawing');
var Axes = require('./axes');

/**
 * transitionAxes
 *
 * transition axes from one set of ranges to another, using a svg
 * transformations, similar to during panning.
 *
 * @param {DOM element | object} gd
 * @param {array} edits : array of 'edits', each item with
 * - plotinfo {object} subplot object
 * - xr0 {array} initial x-range
 * - xr1 {array} end x-range
 * - yr0 {array} initial y-range
 * - yr1 {array} end y-range
 * @param {object} transitionOpts
 * @param {function} makeOnCompleteCallback
 */
module.exports = function transitionAxes(gd, edits, transitionOpts, makeOnCompleteCallback) {
    var fullLayout = gd._fullLayout;

    // special case for redraw:false Plotly.animate that relies on this
    // to update axis-referenced layout components
    if(edits.length === 0) {
        Axes.redrawComponents(gd);
        return;
    }

    function unsetSubplotTransform(subplot) {
        var xa = subplot.xaxis;
        var ya = subplot.yaxis;

        fullLayout._defs.select('#' + subplot.clipId + '> rect')
            .call(Drawing.setTranslate, 0, 0)
            .call(Drawing.setScale, 1, 1);

        subplot.plot
            .call(Drawing.setTranslate, xa._offset, ya._offset)
            .call(Drawing.setScale, 1, 1);

        var traceGroups = subplot.plot.selectAll('.scatterlayer .trace');

        // This is specifically directed at scatter traces, applying an inverse
        // scale to individual points to counteract the scale of the trace
        // as a whole:
        traceGroups.selectAll('.point')
            .call(Drawing.setPointGroupScale, 1, 1);
        traceGroups.selectAll('.textpoint')
            .call(Drawing.setTextPointsScale, 1, 1);
        traceGroups
            .call(Drawing.hideOutsideRangePoints, subplot);
    }

    function updateSubplot(edit, progress) {
        var plotinfo = edit.plotinfo;
        var xa = plotinfo.xaxis;
        var ya = plotinfo.yaxis;

        var xr0 = edit.xr0;
        var xr1 = edit.xr1;
        var xlen = xa._length;
        var yr0 = edit.yr0;
        var yr1 = edit.yr1;
        var ylen = ya._length;

        var editX = !!xr1;
        var editY = !!yr1;
        var viewBox = [];

        if(editX) {
            var dx0 = xr0[1] - xr0[0];
            var dx1 = xr1[1] - xr1[0];
            viewBox[0] = (xr0[0] * (1 - progress) + progress * xr1[0] - xr0[0]) / (xr0[1] - xr0[0]) * xlen;
            viewBox[2] = xlen * ((1 - progress) + progress * dx1 / dx0);
            xa.range[0] = xr0[0] * (1 - progress) + progress * xr1[0];
            xa.range[1] = xr0[1] * (1 - progress) + progress * xr1[1];
        } else {
            viewBox[0] = 0;
            viewBox[2] = xlen;
        }

        if(editY) {
            var dy0 = yr0[1] - yr0[0];
            var dy1 = yr1[1] - yr1[0];
            viewBox[1] = (yr0[1] * (1 - progress) + progress * yr1[1] - yr0[1]) / (yr0[0] - yr0[1]) * ylen;
            viewBox[3] = ylen * ((1 - progress) + progress * dy1 / dy0);
            ya.range[0] = yr0[0] * (1 - progress) + progress * yr1[0];
            ya.range[1] = yr0[1] * (1 - progress) + progress * yr1[1];
        } else {
            viewBox[1] = 0;
            viewBox[3] = ylen;
        }

        Axes.drawOne(gd, xa, {skipTitle: true});
        Axes.drawOne(gd, ya, {skipTitle: true});
        Axes.redrawComponents(gd, [xa._id, ya._id]);

        var xScaleFactor = editX ? xlen / viewBox[2] : 1;
        var yScaleFactor = editY ? ylen / viewBox[3] : 1;
        var clipDx = editX ? viewBox[0] : 0;
        var clipDy = editY ? viewBox[1] : 0;
        var fracDx = editX ? (viewBox[0] / viewBox[2] * xlen) : 0;
        var fracDy = editY ? (viewBox[1] / viewBox[3] * ylen) : 0;
        var plotDx = xa._offset - fracDx;
        var plotDy = ya._offset - fracDy;

        plotinfo.clipRect
            .call(Drawing.setTranslate, clipDx, clipDy)
            .call(Drawing.setScale, 1 / xScaleFactor, 1 / yScaleFactor);

        plotinfo.plot
            .call(Drawing.setTranslate, plotDx, plotDy)
            .call(Drawing.setScale, xScaleFactor, yScaleFactor);

        // apply an inverse scale to individual points to counteract
        // the scale of the trace group.
        Drawing.setPointGroupScale(plotinfo.zoomScalePts, 1 / xScaleFactor, 1 / yScaleFactor);
        Drawing.setTextPointsScale(plotinfo.zoomScaleTxt, 1 / xScaleFactor, 1 / yScaleFactor);
    }

    var onComplete;
    if(makeOnCompleteCallback) {
        // This module makes the choice whether or not it notifies Plotly.transition
        // about completion:
        onComplete = makeOnCompleteCallback();
    }

    function transitionComplete() {
        var aobj = {};

        for(var i = 0; i < edits.length; i++) {
            var edit = edits[i];
            if(edit.xr1) aobj[edit.plotinfo.xaxis._name + '.range'] = edit.xr1.slice();
            if(edit.yr1) aobj[edit.plotinfo.yaxis._name + '.range'] = edit.yr1.slice();
        }

        // Signal that this transition has completed:
        onComplete && onComplete();

        return Registry.call('relayout', gd, aobj).then(function() {
            for(var i = 0; i < edits.length; i++) {
                unsetSubplotTransform(edits[i].plotinfo);
            }
        });
    }

    function transitionInterrupt() {
        var aobj = {};

        for(var i = 0; i < edits.length; i++) {
            var edit = edits[i];
            if(edit.xr0) aobj[edit.plotinfo.xaxis._name + '.range'] = edit.xr0.slice();
            if(edit.yr0) aobj[edit.plotinfo.yaxis._name + '.range'] = edit.yr0.slice();
        }

        return Registry.call('relayout', gd, aobj).then(function() {
            for(var i = 0; i < edits.length; i++) {
                unsetSubplotTransform(edits[i].plotinfo);
            }
        });
    }

    var t1, t2, raf;
    var easeFn = d3.ease(transitionOpts.easing);

    gd._transitionData._interruptCallbacks.push(function() {
        window.cancelAnimationFrame(raf);
        raf = null;
        return transitionInterrupt();
    });

    function doFrame() {
        t2 = Date.now();

        var tInterp = Math.min(1, (t2 - t1) / transitionOpts.duration);
        var progress = easeFn(tInterp);

        for(var i = 0; i < edits.length; i++) {
            updateSubplot(edits[i], progress);
        }

        if(t2 - t1 > transitionOpts.duration) {
            transitionComplete();
            raf = window.cancelAnimationFrame(doFrame);
        } else {
            raf = window.requestAnimationFrame(doFrame);
        }
    }

    t1 = Date.now();
    raf = window.requestAnimationFrame(doFrame);

    return Promise.resolve();
};
