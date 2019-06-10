/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var cluster = require('point-cluster');
var isNumeric = require('fast-isnumeric');

var ScatterGl = require('../scattergl');
var calcColorscale = require('../scatter/colorscale_calc');
var calcMarkerSize = require('../scatter/calc').calcMarkerSize;
var convert = require('../scattergl/convert');

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');
var makeHoverPointText = require('../scatterpolar/hover').makeHoverPointText;

var TOO_MANY_POINTS = require('../scattergl/constants').TOO_MANY_POINTS;

function calc(gd, trace) {
    var fullLayout = gd._fullLayout;
    var subplotId = trace.subplot;
    var radialAxis = fullLayout[subplotId].radialaxis;
    var angularAxis = fullLayout[subplotId].angularaxis;
    var rArray = radialAxis.makeCalcdata(trace, 'r');
    var thetaArray = angularAxis.makeCalcdata(trace, 'theta');
    var len = trace._length;
    var stash = {};

    if(len < rArray.length) rArray = rArray.slice(0, len);
    if(len < thetaArray.length) thetaArray = thetaArray.slice(0, len);

    stash.r = rArray;
    stash.theta = thetaArray;

    calcColorscale(gd, trace);

    // only compute 'style' options in calc, as position options
    // depend on the radial range and must be set in plot
    var opts = stash.opts = convert.style(gd, trace);

    // For graphs with very large number of points and array marker.size,
    // use average marker size instead to speed things up.
    var ppad;
    if(len < TOO_MANY_POINTS) {
        ppad = calcMarkerSize(trace, len);
    } else if(opts.marker) {
        ppad = 2 * (opts.marker.sizeAvg || Math.max(opts.marker.size, 3));
    }
    trace._extremes.x = Axes.findExtremes(radialAxis, rArray, {ppad: ppad});

    return [{x: false, y: false, t: stash, trace: trace}];
}

function plot(gd, subplot, cdata) {
    if(!cdata.length) return;

    var radialAxis = subplot.radialAxis;
    var angularAxis = subplot.angularAxis;
    var scene = ScatterGl.sceneUpdate(gd, subplot);

    cdata.forEach(function(cdscatter) {
        if(!cdscatter || !cdscatter[0] || !cdscatter[0].trace) return;
        var cd = cdscatter[0];
        var trace = cd.trace;
        var stash = cd.t;
        var len = trace._length;
        var rArray = stash.r;
        var thetaArray = stash.theta;
        var opts = stash.opts;
        var i;

        var subRArray = rArray.slice();
        var subThetaArray = thetaArray.slice();

        // filter out by range
        for(i = 0; i < rArray.length; i++) {
            if(!subplot.isPtInside({r: rArray[i], theta: thetaArray[i]})) {
                subRArray[i] = NaN;
                subThetaArray[i] = NaN;
            }
        }

        var positions = new Array(len * 2);
        var x = Array(len);
        var y = Array(len);

        for(i = 0; i < len; i++) {
            var r = subRArray[i];
            var xx, yy;

            if(isNumeric(r)) {
                var rg = radialAxis.c2g(r);
                var thetag = angularAxis.c2g(subThetaArray[i], trace.thetaunit);
                xx = rg * Math.cos(thetag);
                yy = rg * Math.sin(thetag);
            } else {
                xx = yy = NaN;
            }
            x[i] = positions[i * 2] = xx;
            y[i] = positions[i * 2 + 1] = yy;
        }

        stash.tree = cluster(positions);

        // FIXME: see scattergl.js#109
        if(opts.marker && len >= TOO_MANY_POINTS) {
            opts.marker.cluster = stash.tree;
        }

        if(opts.marker) {
            opts.markerSel.positions = opts.markerUnsel.positions = opts.marker.positions = positions;
        }

        if(opts.line && positions.length > 1) {
            Lib.extendFlat(
                opts.line,
                convert.linePositions(gd, trace, positions)
            );
        }

        if(opts.text) {
            Lib.extendFlat(
                opts.text,
                {positions: positions},
                convert.textPosition(gd, trace, opts.text, opts.marker)
            );
            Lib.extendFlat(
                opts.textSel,
                {positions: positions},
                convert.textPosition(gd, trace, opts.text, opts.markerSel)
            );
            Lib.extendFlat(
                opts.textUnsel,
                {positions: positions},
                convert.textPosition(gd, trace, opts.text, opts.markerUnsel)
            );
        }

        if(opts.fill && !scene.fill2d) scene.fill2d = true;
        if(opts.marker && !scene.scatter2d) scene.scatter2d = true;
        if(opts.line && !scene.line2d) scene.line2d = true;
        if(opts.text && !scene.glText) scene.glText = true;

        scene.lineOptions.push(opts.line);
        scene.fillOptions.push(opts.fill);
        scene.markerOptions.push(opts.marker);
        scene.markerSelectedOptions.push(opts.markerSel);
        scene.markerUnselectedOptions.push(opts.markerUnsel);
        scene.textOptions.push(opts.text);
        scene.textSelectedOptions.push(opts.textSel);
        scene.textUnselectedOptions.push(opts.textUnsel);
        scene.selectBatch.push([]);
        scene.unselectBatch.push([]);

        stash.x = x;
        stash.y = y;
        stash.rawx = x;
        stash.rawy = y;
        stash.r = rArray;
        stash.theta = thetaArray;
        stash.positions = positions;
        stash._scene = scene;
        stash.index = scene.count;
        scene.count++;
    });

    return ScatterGl.plot(gd, subplot, cdata);
}

function hoverPoints(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var stash = cd[0].t;
    var rArray = stash.r;
    var thetaArray = stash.theta;

    var scatterPointData = ScatterGl.hoverPoints(pointData, xval, yval, hovermode);
    if(!scatterPointData || scatterPointData[0].index === false) return;

    var newPointData = scatterPointData[0];

    if(newPointData.index === undefined) {
        return scatterPointData;
    }

    var subplot = pointData.subplot;
    var cdi = newPointData.cd[newPointData.index];
    var trace = newPointData.trace;

    // augment pointData with r/theta param
    cdi.r = rArray[newPointData.index];
    cdi.theta = thetaArray[newPointData.index];

    if(!subplot.isPtInside(cdi)) return;

    newPointData.xLabelVal = undefined;
    newPointData.yLabelVal = undefined;
    makeHoverPointText(cdi, trace, subplot, newPointData);

    return scatterPointData;
}

module.exports = {
    moduleType: 'trace',
    name: 'scatterpolargl',
    basePlotModule: require('../../plots/polar'),
    categories: ['gl', 'regl', 'polar', 'symbols', 'showLegend', 'scatter-like'],

    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),
    colorbar: require('../scatter/marker_colorbar'),

    calc: calc,
    plot: plot,
    hoverPoints: hoverPoints,
    selectPoints: ScatterGl.selectPoints,

    meta: {
        hrName: 'scatter_polar_gl',
        description: [
            'The scatterpolargl trace type encompasses line charts, scatter charts, and bubble charts',
            'in polar coordinates using the WebGL plotting engine.',
            'The data visualized as scatter point or lines is set in',
            '`r` (radial) and `theta` (angular) coordinates',
            'Bubble charts are achieved by setting `marker.size` and/or `marker.color`',
            'to numerical arrays.'
        ].join(' ')
    }
};
