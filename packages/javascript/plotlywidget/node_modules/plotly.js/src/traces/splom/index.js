/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var createMatrix = require('regl-splom');

var Registry = require('../../registry');
var Grid = require('../../components/grid');
var Lib = require('../../lib');
var AxisIDs = require('../../plots/cartesian/axis_ids');

var subTypes = require('../scatter/subtypes');
var calcMarkerSize = require('../scatter/calc').calcMarkerSize;
var calcAxisExpansion = require('../scatter/calc').calcAxisExpansion;
var calcColorscale = require('../scatter/colorscale_calc');
var convertMarkerSelection = require('../scattergl/convert').markerSelection;
var convertMarkerStyle = require('../scattergl/convert').markerStyle;
var calcHover = require('../scattergl').calcHover;

var BADNUM = require('../../constants/numerical').BADNUM;
var TOO_MANY_POINTS = require('../scattergl/constants').TOO_MANY_POINTS;

function calc(gd, trace) {
    var dimensions = trace.dimensions;
    var commonLength = trace._length;
    var opts = {};
    // 'c' for calculated, 'l' for linear,
    // only differ here for log axes, pass ldata to createMatrix as 'data'
    var cdata = opts.cdata = [];
    var ldata = opts.data = [];
    // keep track of visible dimensions
    var visibleDims = trace._visibleDims = [];
    var i, k, dim, xa, ya;

    function makeCalcdata(ax, dim) {
        // call makeCalcdata with fake input
        var ccol = ax.makeCalcdata({
            v: dim.values,
            vcalendar: trace.calendar
        }, 'v');

        for(var j = 0; j < ccol.length; j++) {
            ccol[j] = ccol[j] === BADNUM ? NaN : ccol[j];
        }
        cdata.push(ccol);
        ldata.push(ax.type === 'log' ? Lib.simpleMap(ccol, ax.c2l) : ccol);
    }

    for(i = 0; i < dimensions.length; i++) {
        dim = dimensions[i];

        if(dim.visible) {
            xa = AxisIDs.getFromId(gd, trace._diag[i][0]);
            ya = AxisIDs.getFromId(gd, trace._diag[i][1]);

            // if corresponding x & y axes don't have matching types, skip dim
            if(xa && ya && xa.type !== ya.type) {
                Lib.log('Skipping splom dimension ' + i + ' with conflicting axis types');
                continue;
            }

            if(xa) {
                makeCalcdata(xa, dim);
                if(ya && ya.type === 'category') {
                    ya._categories = xa._categories.slice();
                }
            } else {
                // should not make it here, if both xa and ya undefined
                makeCalcdata(ya, dim);
            }

            visibleDims.push(i);
        }
    }

    calcColorscale(gd, trace);
    Lib.extendFlat(opts, convertMarkerStyle(trace));

    var visibleLength = cdata.length;
    var hasTooManyPoints = (visibleLength * commonLength) > TOO_MANY_POINTS;

    // Reuse SVG scatter axis expansion routine.
    // For graphs with very large number of points and array marker.size,
    // use average marker size instead to speed things up.
    var ppad;
    if(hasTooManyPoints) {
        ppad = 2 * (opts.sizeAvg || Math.max(opts.size, 3));
    } else {
        ppad = calcMarkerSize(trace, commonLength);
    }

    for(k = 0; k < visibleDims.length; k++) {
        i = visibleDims[k];
        dim = dimensions[i];
        xa = AxisIDs.getFromId(gd, trace._diag[i][0]) || {};
        ya = AxisIDs.getFromId(gd, trace._diag[i][1]) || {};
        calcAxisExpansion(gd, trace, xa, ya, cdata[k], cdata[k], ppad);
    }

    var scene = sceneUpdate(gd, trace);
    if(!scene.matrix) scene.matrix = true;
    scene.matrixOptions = opts;

    scene.selectedOptions = convertMarkerSelection(trace, trace.selected);
    scene.unselectedOptions = convertMarkerSelection(trace, trace.unselected);

    return [{x: false, y: false, t: {}, trace: trace}];
}

function sceneUpdate(gd, trace) {
    var fullLayout = gd._fullLayout;
    var uid = trace.uid;

    // must place ref to 'scene' in fullLayout, so that:
    // - it can be relinked properly on updates
    // - it can be destroyed properly when needed
    var splomScenes = fullLayout._splomScenes;
    if(!splomScenes) splomScenes = fullLayout._splomScenes = {};

    var reset = {dirty: true};

    var first = {
        matrix: false,
        selectBatch: [],
        unselectBatch: []
    };

    var scene = splomScenes[trace.uid];

    if(!scene) {
        scene = splomScenes[uid] = Lib.extendFlat({}, reset, first);

        scene.draw = function draw() {
            if(scene.matrix && scene.matrix.draw) {
                if(scene.selectBatch.length || scene.unselectBatch.length) {
                    scene.matrix.draw(scene.unselectBatch, scene.selectBatch);
                } else {
                    scene.matrix.draw();
                }
            }

            scene.dirty = false;
        };

        // remove scene resources
        scene.destroy = function destroy() {
            if(scene.matrix && scene.matrix.destroy) {
                scene.matrix.destroy();
            }
            scene.matrixOptions = null;
            scene.selectBatch = null;
            scene.unselectBatch = null;
            scene = null;
        };
    }

    // In case if we have scene from the last calc - reset data
    if(!scene.dirty) {
        Lib.extendFlat(scene, reset);
    }

    return scene;
}

function plot(gd, _, splomCalcData) {
    if(!splomCalcData.length) return;

    for(var i = 0; i < splomCalcData.length; i++) {
        plotOne(gd, splomCalcData[i][0]);
    }
}

function plotOne(gd, cd0) {
    var fullLayout = gd._fullLayout;
    var gs = fullLayout._size;
    var trace = cd0.trace;
    var stash = cd0.t;
    var scene = fullLayout._splomScenes[trace.uid];
    var matrixOpts = scene.matrixOptions;
    var cdata = matrixOpts.cdata;
    var regl = fullLayout._glcanvas.data()[0].regl;
    var dragmode = fullLayout.dragmode;
    var xa, ya;
    var i, j, k;

    if(cdata.length === 0) return;

    // augment options with proper upper/lower halves
    // regl-splom's default grid starts from bottom-left
    matrixOpts.lower = trace.showupperhalf;
    matrixOpts.upper = trace.showlowerhalf;
    matrixOpts.diagonal = trace.diagonal.visible;

    var visibleDims = trace._visibleDims;
    var visibleLength = cdata.length;
    var viewOpts = scene.viewOpts = {};
    viewOpts.ranges = new Array(visibleLength);
    viewOpts.domains = new Array(visibleLength);

    for(k = 0; k < visibleDims.length; k++) {
        i = visibleDims[k];

        var rng = viewOpts.ranges[k] = new Array(4);
        var dmn = viewOpts.domains[k] = new Array(4);

        xa = AxisIDs.getFromId(gd, trace._diag[i][0]);
        if(xa) {
            rng[0] = xa._rl[0];
            rng[2] = xa._rl[1];
            dmn[0] = xa.domain[0];
            dmn[2] = xa.domain[1];
        }

        ya = AxisIDs.getFromId(gd, trace._diag[i][1]);
        if(ya) {
            rng[1] = ya._rl[0];
            rng[3] = ya._rl[1];
            dmn[1] = ya.domain[0];
            dmn[3] = ya.domain[1];
        }
    }

    viewOpts.viewport = [gs.l, gs.b, gs.w + gs.l, gs.h + gs.b];

    if(scene.matrix === true) {
        scene.matrix = createMatrix(regl);
    }

    var clickSelectEnabled = fullLayout.clickmode.indexOf('select') > -1;
    var selectMode = dragmode === 'lasso' || dragmode === 'select' ||
      !!trace.selectedpoints || clickSelectEnabled;
    var needsBaseUpdate = true;

    if(selectMode) {
        var commonLength = trace._length;

        // regenerate scene batch, if traces number changed during selection
        if(trace.selectedpoints) {
            scene.selectBatch = trace.selectedpoints;

            var selPts = trace.selectedpoints;
            var selDict = {};
            for(i = 0; i < selPts.length; i++) {
                selDict[selPts[i]] = true;
            }
            var unselPts = [];
            for(i = 0; i < commonLength; i++) {
                if(!selDict[i]) unselPts.push(i);
            }
            scene.unselectBatch = unselPts;
        }

        // precalculate px coords since we are not going to pan during select
        var xpx = stash.xpx = new Array(visibleLength);
        var ypx = stash.ypx = new Array(visibleLength);

        for(k = 0; k < visibleDims.length; k++) {
            i = visibleDims[k];

            xa = AxisIDs.getFromId(gd, trace._diag[i][0]);
            if(xa) {
                xpx[k] = new Array(commonLength);
                for(j = 0; j < commonLength; j++) {
                    xpx[k][j] = xa.c2p(cdata[k][j]);
                }
            }

            ya = AxisIDs.getFromId(gd, trace._diag[i][1]);
            if(ya) {
                ypx[k] = new Array(commonLength);
                for(j = 0; j < commonLength; j++) {
                    ypx[k][j] = ya.c2p(cdata[k][j]);
                }
            }
        }

        if(scene.selectBatch.length || scene.unselectBatch.length) {
            var unselOpts = Lib.extendFlat({}, matrixOpts, scene.unselectedOptions, viewOpts);
            var selOpts = Lib.extendFlat({}, matrixOpts, scene.selectedOptions, viewOpts);
            scene.matrix.update(unselOpts, selOpts);
            needsBaseUpdate = false;
        }
    } else {
        stash.xpx = stash.ypx = null;
    }

    if(needsBaseUpdate) {
        var opts = Lib.extendFlat({}, matrixOpts, viewOpts);
        scene.matrix.update(opts, null);
    }
}

function editStyle(gd, cd0) {
    var trace = cd0.trace;
    var scene = gd._fullLayout._splomScenes[trace.uid];

    if(scene) {
        calcColorscale(gd, trace);

        Lib.extendFlat(scene.matrixOptions, convertMarkerStyle(trace));
        // TODO [un]selected styles?

        var opts = Lib.extendFlat({}, scene.matrixOptions, scene.viewOpts);

        // TODO this is too long for arrayOk attributes!
        scene.matrix.update(opts, null);
    }
}

function hoverPoints(pointData, xval, yval) {
    var cd = pointData.cd;
    var trace = cd[0].trace;
    var scene = pointData.scene;
    var cdata = scene.matrixOptions.cdata;
    var xa = pointData.xa;
    var ya = pointData.ya;
    var xpx = xa.c2p(xval);
    var ypx = ya.c2p(yval);
    var maxDistance = pointData.distance;

    var xi = getDimIndex(trace, xa);
    var yi = getDimIndex(trace, ya);
    if(xi === false || yi === false) return [pointData];

    var x = cdata[xi];
    var y = cdata[yi];

    var id, dxy;
    var minDist = maxDistance;

    for(var i = 0; i < x.length; i++) {
        var ptx = x[i];
        var pty = y[i];
        var dx = xa.c2p(ptx) - xpx;
        var dy = ya.c2p(pty) - ypx;
        var dist = Math.sqrt(dx * dx + dy * dy);

        if(dist < minDist) {
            minDist = dxy = dist;
            id = i;
        }
    }

    pointData.index = id;
    pointData.distance = minDist;
    pointData.dxy = dxy;

    if(id === undefined) return [pointData];

    calcHover(pointData, x, y, trace);

    return [pointData];
}

function selectPoints(searchInfo, selectionTester) {
    var cd = searchInfo.cd;
    var trace = cd[0].trace;
    var stash = cd[0].t;
    var scene = searchInfo.scene;
    var cdata = scene.matrixOptions.cdata;
    var xa = searchInfo.xaxis;
    var ya = searchInfo.yaxis;
    var selection = [];

    if(!scene) return selection;

    var hasOnlyLines = (!subTypes.hasMarkers(trace) && !subTypes.hasText(trace));
    if(trace.visible !== true || hasOnlyLines) return selection;

    var xi = getDimIndex(trace, xa);
    var yi = getDimIndex(trace, ya);
    if(xi === false || yi === false) return selection;

    var xpx = stash.xpx[xi];
    var ypx = stash.ypx[yi];
    var x = cdata[xi];
    var y = cdata[yi];
    var els = [];
    var unels = [];

    // degenerate polygon does not enable selection
    // filter out points by visible scatter ones
    if(selectionTester !== false && !selectionTester.degenerate) {
        for(var i = 0; i < x.length; i++) {
            if(selectionTester.contains([xpx[i], ypx[i]], null, i, searchInfo)) {
                els.push(i);
                selection.push({
                    pointNumber: i,
                    x: x[i],
                    y: y[i]
                });
            } else {
                unels.push(i);
            }
        }
    }

    var matrixOpts = scene.matrixOptions;

    if(!els.length && !unels.length) {
        scene.matrix.update(matrixOpts, null);
    } else if(!scene.selectBatch.length && !scene.unselectBatch.length) {
        scene.matrix.update(
            scene.unselectedOptions,
            Lib.extendFlat({}, matrixOpts, scene.selectedOptions, scene.viewOpts)
        );
    }

    scene.selectBatch = els;
    scene.unselectBatch = unels;

    return selection;
}

function getDimIndex(trace, ax) {
    var axId = ax._id;
    var axLetter = axId.charAt(0);
    var ind = {x: 0, y: 1}[axLetter];
    var visibleDims = trace._visibleDims;

    for(var k = 0; k < visibleDims.length; k++) {
        var i = visibleDims[k];
        if(trace._diag[i][ind] === axId) return k;
    }
    return false;
}

module.exports = {
    moduleType: 'trace',
    name: 'splom',

    basePlotModule: require('./base_plot'),
    categories: ['gl', 'regl', 'cartesian', 'symbols', 'showLegend', 'scatter-like'],

    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),
    colorbar: require('../scatter/marker_colorbar'),

    calc: calc,
    plot: plot,
    hoverPoints: hoverPoints,
    selectPoints: selectPoints,
    editStyle: editStyle,

    meta: {
        description: [
            'Splom traces generate scatter plot matrix visualizations.',
            'Each splom `dimensions` items correspond to a generated axis.',
            'Values for each of those dimensions are set in `dimensions[i].values`.',
            'Splom traces support all `scattergl` marker style attributes.',
            'Specify `layout.grid` attributes and/or layout x-axis and y-axis attributes',
            'for more control over the axis positioning and style. '
        ].join(' ')
    }
};

// splom traces use the 'grid' component to generate their axes,
// register it here
Registry.register(Grid);
