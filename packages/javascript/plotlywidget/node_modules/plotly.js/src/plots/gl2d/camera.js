/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var mouseChange = require('mouse-change');
var mouseWheel = require('mouse-wheel');
var mouseOffset = require('mouse-event-offset');
var cartesianConstants = require('../cartesian/constants');
var hasPassive = require('has-passive-events');

module.exports = createCamera;

function Camera2D(element, plot) {
    this.element = element;
    this.plot = plot;
    this.mouseListener = null;
    this.wheelListener = null;
    this.lastInputTime = Date.now();
    this.lastPos = [0, 0];
    this.boxEnabled = false;
    this.boxInited = false;
    this.boxStart = [0, 0];
    this.boxEnd = [0, 0];
    this.dragStart = [0, 0];
}


function createCamera(scene) {
    var element = scene.mouseContainer;
    var plot = scene.glplot;
    var result = new Camera2D(element, plot);

    function unSetAutoRange() {
        scene.xaxis.autorange = false;
        scene.yaxis.autorange = false;
    }

    function getSubplotConstraint() {
        // note: this assumes we only have one x and one y axis on this subplot
        // when this constraint is lifted this block won't make sense
        var constraints = scene.graphDiv._fullLayout._axisConstraintGroups;
        var xaId = scene.xaxis._id;
        var yaId = scene.yaxis._id;
        for(var i = 0; i < constraints.length; i++) {
            if(constraints[i][xaId] !== -1) {
                if(constraints[i][yaId] !== -1) return true;
                break;
            }
        }
        return false;
    }

    result.mouseListener = mouseChange(element, handleInteraction);

    // enable simple touch interactions
    element.addEventListener('touchstart', function(ev) {
        var xy = mouseOffset(ev.changedTouches[0], element);
        handleInteraction(0, xy[0], xy[1]);
        handleInteraction(1, xy[0], xy[1]);

        ev.preventDefault();
    }, hasPassive ? {passive: false} : false);
    element.addEventListener('touchmove', function(ev) {
        ev.preventDefault();
        var xy = mouseOffset(ev.changedTouches[0], element);
        handleInteraction(1, xy[0], xy[1]);

        ev.preventDefault();
    }, hasPassive ? {passive: false} : false);
    element.addEventListener('touchend', function(ev) {
        handleInteraction(0, result.lastPos[0], result.lastPos[1]);

        ev.preventDefault();
    }, hasPassive ? {passive: false} : false);

    function handleInteraction(buttons, x, y) {
        var dataBox = scene.calcDataBox();
        var viewBox = plot.viewBox;

        var lastX = result.lastPos[0];
        var lastY = result.lastPos[1];

        var MINDRAG = cartesianConstants.MINDRAG * plot.pixelRatio;
        var MINZOOM = cartesianConstants.MINZOOM * plot.pixelRatio;

        var dx, dy;

        x *= plot.pixelRatio;
        y *= plot.pixelRatio;

        // mouseChange gives y about top; convert to about bottom
        y = (viewBox[3] - viewBox[1]) - y;

        function updateRange(i0, start, end) {
            var range0 = Math.min(start, end);
            var range1 = Math.max(start, end);

            if(range0 !== range1) {
                dataBox[i0] = range0;
                dataBox[i0 + 2] = range1;
                result.dataBox = dataBox;
                scene.setRanges(dataBox);
            } else {
                scene.selectBox.selectBox = [0, 0, 1, 1];
                scene.glplot.setDirty();
            }
        }

        switch(scene.fullLayout.dragmode) {
            case 'zoom':
                if(buttons) {
                    var dataX = x /
                            (viewBox[2] - viewBox[0]) * (dataBox[2] - dataBox[0]) +
                        dataBox[0];
                    var dataY = y /
                            (viewBox[3] - viewBox[1]) * (dataBox[3] - dataBox[1]) +
                        dataBox[1];

                    if(!result.boxInited) {
                        result.boxStart[0] = dataX;
                        result.boxStart[1] = dataY;
                        result.dragStart[0] = x;
                        result.dragStart[1] = y;
                    }

                    result.boxEnd[0] = dataX;
                    result.boxEnd[1] = dataY;

                    // we need to mark the box as initialized right away
                    // so that we can tell the start and end points apart
                    result.boxInited = true;

                    // but don't actually enable the box until the cursor moves
                    if(!result.boxEnabled && (
                        result.boxStart[0] !== result.boxEnd[0] ||
                        result.boxStart[1] !== result.boxEnd[1])
                    ) {
                        result.boxEnabled = true;
                    }

                    // constrain aspect ratio if the axes require it
                    var smallDx = Math.abs(result.dragStart[0] - x) < MINZOOM;
                    var smallDy = Math.abs(result.dragStart[1] - y) < MINZOOM;
                    if(getSubplotConstraint() && !(smallDx && smallDy)) {
                        dx = result.boxEnd[0] - result.boxStart[0];
                        dy = result.boxEnd[1] - result.boxStart[1];
                        var dydx = (dataBox[3] - dataBox[1]) / (dataBox[2] - dataBox[0]);

                        if(Math.abs(dx * dydx) > Math.abs(dy)) {
                            result.boxEnd[1] = result.boxStart[1] +
                                Math.abs(dx) * dydx * (dy >= 0 ? 1 : -1);

                            // gl-select-box clips to the plot area bounds,
                            // which breaks the axis constraint, so don't allow
                            // this box to go out of bounds
                            if(result.boxEnd[1] < dataBox[1]) {
                                result.boxEnd[1] = dataBox[1];
                                result.boxEnd[0] = result.boxStart[0] +
                                    (dataBox[1] - result.boxStart[1]) / Math.abs(dydx);
                            } else if(result.boxEnd[1] > dataBox[3]) {
                                result.boxEnd[1] = dataBox[3];
                                result.boxEnd[0] = result.boxStart[0] +
                                    (dataBox[3] - result.boxStart[1]) / Math.abs(dydx);
                            }
                        } else {
                            result.boxEnd[0] = result.boxStart[0] +
                                Math.abs(dy) / dydx * (dx >= 0 ? 1 : -1);

                            if(result.boxEnd[0] < dataBox[0]) {
                                result.boxEnd[0] = dataBox[0];
                                result.boxEnd[1] = result.boxStart[1] +
                                    (dataBox[0] - result.boxStart[0]) * Math.abs(dydx);
                            } else if(result.boxEnd[0] > dataBox[2]) {
                                result.boxEnd[0] = dataBox[2];
                                result.boxEnd[1] = result.boxStart[1] +
                                    (dataBox[2] - result.boxStart[0]) * Math.abs(dydx);
                            }
                        }
                    } else {
                        // otherwise clamp small changes to the origin so we get 1D zoom

                        if(smallDx) result.boxEnd[0] = result.boxStart[0];
                        if(smallDy) result.boxEnd[1] = result.boxStart[1];
                    }
                } else if(result.boxEnabled) {
                    dx = result.boxStart[0] !== result.boxEnd[0];
                    dy = result.boxStart[1] !== result.boxEnd[1];
                    if(dx || dy) {
                        if(dx) {
                            updateRange(0, result.boxStart[0], result.boxEnd[0]);
                            scene.xaxis.autorange = false;
                        }
                        if(dy) {
                            updateRange(1, result.boxStart[1], result.boxEnd[1]);
                            scene.yaxis.autorange = false;
                        }
                        scene.relayoutCallback();
                    } else {
                        scene.glplot.setDirty();
                    }
                    result.boxEnabled = false;
                    result.boxInited = false;
                } else if(result.boxInited) {
                    // if box was inited but button released then - reset the box

                    result.boxInited = false;
                }
                break;

            case 'pan':
                result.boxEnabled = false;
                result.boxInited = false;

                if(buttons) {
                    if(!result.panning) {
                        result.dragStart[0] = x;
                        result.dragStart[1] = y;
                    }

                    if(Math.abs(result.dragStart[0] - x) < MINDRAG) x = result.dragStart[0];
                    if(Math.abs(result.dragStart[1] - y) < MINDRAG) y = result.dragStart[1];

                    dx = (lastX - x) * (dataBox[2] - dataBox[0]) /
                        (plot.viewBox[2] - plot.viewBox[0]);
                    dy = (lastY - y) * (dataBox[3] - dataBox[1]) /
                        (plot.viewBox[3] - plot.viewBox[1]);

                    dataBox[0] += dx;
                    dataBox[2] += dx;
                    dataBox[1] += dy;
                    dataBox[3] += dy;

                    scene.setRanges(dataBox);

                    result.panning = true;
                    result.lastInputTime = Date.now();
                    unSetAutoRange();
                    scene.cameraChanged();
                    scene.handleAnnotations();
                } else if(result.panning) {
                    result.panning = false;
                    scene.relayoutCallback();
                }
                break;
        }

        result.lastPos[0] = x;
        result.lastPos[1] = y;
    }

    result.wheelListener = mouseWheel(element, function(dx, dy) {
        if(!scene.scrollZoom) return false;

        var dataBox = scene.calcDataBox();
        var viewBox = plot.viewBox;

        var lastX = result.lastPos[0];
        var lastY = result.lastPos[1];

        var scale = Math.exp(5.0 * dy / (viewBox[3] - viewBox[1]));

        var cx = lastX /
                (viewBox[2] - viewBox[0]) * (dataBox[2] - dataBox[0]) +
            dataBox[0];
        var cy = lastY /
                (viewBox[3] - viewBox[1]) * (dataBox[3] - dataBox[1]) +
            dataBox[1];

        dataBox[0] = (dataBox[0] - cx) * scale + cx;
        dataBox[2] = (dataBox[2] - cx) * scale + cx;
        dataBox[1] = (dataBox[1] - cy) * scale + cy;
        dataBox[3] = (dataBox[3] - cy) * scale + cy;

        scene.setRanges(dataBox);

        result.lastInputTime = Date.now();
        unSetAutoRange();
        scene.cameraChanged();
        scene.handleAnnotations();
        scene.relayoutCallback();

        return true;
    }, true);

    return result;
}
