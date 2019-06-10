/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var conePlot = require('gl-cone3d');
var createConeMesh = require('gl-cone3d').createConeMesh;

var simpleMap = require('../../lib').simpleMap;
var parseColorScale = require('../../lib/gl_format_color').parseColorScale;
var extractOpts = require('../../components/colorscale').extractOpts;
var zip3 = require('../../plots/gl3d/zip3');

function Cone(scene, uid) {
    this.scene = scene;
    this.uid = uid;
    this.mesh = null;
    this.data = null;
}

var proto = Cone.prototype;

proto.handlePick = function(selection) {
    if(selection.object === this.mesh) {
        var selectIndex = selection.index = selection.data.index;
        var xx = this.data.x[selectIndex];
        var yy = this.data.y[selectIndex];
        var zz = this.data.z[selectIndex];
        var uu = this.data.u[selectIndex];
        var vv = this.data.v[selectIndex];
        var ww = this.data.w[selectIndex];

        selection.traceCoordinate = [
            xx, yy, zz,
            uu, vv, ww,
            Math.sqrt(uu * uu + vv * vv + ww * ww)
        ];

        var text = this.data.hovertext || this.data.text;
        if(Array.isArray(text) && text[selectIndex] !== undefined) {
            selection.textLabel = text[selectIndex];
        } else if(text) {
            selection.textLabel = text;
        }

        return true;
    }
};

var axisName2scaleIndex = {xaxis: 0, yaxis: 1, zaxis: 2};
var anchor2coneOffset = {tip: 1, tail: 0, cm: 0.25, center: 0.5};
var anchor2coneSpan = {tip: 1, tail: 1, cm: 0.75, center: 0.5};

function convert(scene, trace) {
    var sceneLayout = scene.fullSceneLayout;
    var dataScale = scene.dataScale;
    var coneOpts = {};

    function toDataCoords(arr, axisName) {
        var ax = sceneLayout[axisName];
        var scale = dataScale[axisName2scaleIndex[axisName]];
        return simpleMap(arr, function(v) { return ax.d2l(v) * scale; });
    }

    coneOpts.vectors = zip3(
        toDataCoords(trace.u, 'xaxis'),
        toDataCoords(trace.v, 'yaxis'),
        toDataCoords(trace.w, 'zaxis'),
        trace._len
    );

    coneOpts.positions = zip3(
        toDataCoords(trace.x, 'xaxis'),
        toDataCoords(trace.y, 'yaxis'),
        toDataCoords(trace.z, 'zaxis'),
        trace._len
    );

    var cOpts = extractOpts(trace);
    coneOpts.colormap = parseColorScale(trace);
    coneOpts.vertexIntensityBounds = [cOpts.min / trace._normMax, cOpts.max / trace._normMax];
    coneOpts.coneOffset = anchor2coneOffset[trace.anchor];

    if(trace.sizemode === 'scaled') {
        // unitless sizeref
        coneOpts.coneSize = trace.sizeref || 0.5;
    } else {
        // sizeref here has unit of velocity
        coneOpts.coneSize = trace.sizeref && trace._normMax ?
            trace.sizeref / trace._normMax :
            0.5;
    }

    var meshData = conePlot(coneOpts);

    // pass gl-mesh3d lighting attributes
    var lp = trace.lightposition;
    meshData.lightPosition = [lp.x, lp.y, lp.z];
    meshData.ambient = trace.lighting.ambient;
    meshData.diffuse = trace.lighting.diffuse;
    meshData.specular = trace.lighting.specular;
    meshData.roughness = trace.lighting.roughness;
    meshData.fresnel = trace.lighting.fresnel;
    meshData.opacity = trace.opacity;

    // stash autorange pad value
    trace._pad = anchor2coneSpan[trace.anchor] * meshData.vectorScale * meshData.coneScale * trace._normMax;

    return meshData;
}

proto.update = function(data) {
    this.data = data;

    var meshData = convert(this.scene, data);
    this.mesh.update(meshData);
};

proto.dispose = function() {
    this.scene.glplot.remove(this.mesh);
    this.mesh.dispose();
};

function createConeTrace(scene, data) {
    var gl = scene.glplot.gl;

    var meshData = convert(scene, data);
    var mesh = createConeMesh(gl, meshData);

    var cone = new Cone(scene, data.uid);
    cone.mesh = mesh;
    cone.data = data;
    mesh._trace = cone;

    scene.glplot.add(mesh);

    return cone;
}

module.exports = createConeTrace;
