/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var createPointCloudRenderer = require('gl-pointcloud2d');

var str2RGBArray = require('../../lib/str2rgbarray');
var findExtremes = require('../../plots/cartesian/autorange').findExtremes;
var getTraceColor = require('../scatter/get_trace_color');

function Pointcloud(scene, uid) {
    this.scene = scene;
    this.uid = uid;
    this.type = 'pointcloud';

    this.pickXData = [];
    this.pickYData = [];
    this.xData = [];
    this.yData = [];
    this.textLabels = [];
    this.color = 'rgb(0, 0, 0)';
    this.name = '';
    this.hoverinfo = 'all';

    this.idToIndex = new Int32Array(0);
    this.bounds = [0, 0, 0, 0];

    this.pointcloudOptions = {
        positions: new Float32Array(0),
        idToIndex: this.idToIndex,
        sizemin: 0.5,
        sizemax: 12,
        color: [0, 0, 0, 1],
        areaRatio: 1,
        borderColor: [0, 0, 0, 1]
    };
    this.pointcloud = createPointCloudRenderer(scene.glplot, this.pointcloudOptions);
    this.pointcloud._trace = this; // scene2d requires this prop
}

var proto = Pointcloud.prototype;

proto.handlePick = function(pickResult) {
    var index = this.idToIndex[pickResult.pointId];

    // prefer the readout from XY, if present
    return {
        trace: this,
        dataCoord: pickResult.dataCoord,
        traceCoord: this.pickXYData ?
            [this.pickXYData[index * 2], this.pickXYData[index * 2 + 1]] :
            [this.pickXData[index], this.pickYData[index]],
        textLabel: Array.isArray(this.textLabels) ?
            this.textLabels[index] :
            this.textLabels,
        color: this.color,
        name: this.name,
        pointIndex: index,
        hoverinfo: this.hoverinfo
    };
};

proto.update = function(options) {
    this.index = options.index;
    this.textLabels = options.text;
    this.name = options.name;
    this.hoverinfo = options.hoverinfo;
    this.bounds = [Infinity, Infinity, -Infinity, -Infinity];

    this.updateFast(options);

    this.color = getTraceColor(options, {});
};

proto.updateFast = function(options) {
    var x = this.xData = this.pickXData = options.x;
    var y = this.yData = this.pickYData = options.y;
    var xy = this.pickXYData = options.xy;

    var userBounds = options.xbounds && options.ybounds;
    var index = options.indices;

    var len;
    var idToIndex;
    var positions;
    var bounds = this.bounds;

    var xx, yy, i;

    if(xy) {
        positions = xy;

        // dividing xy.length by 2 and truncating to integer if xy.length was not even
        len = xy.length >>> 1;

        if(userBounds) {
            bounds[0] = options.xbounds[0];
            bounds[2] = options.xbounds[1];
            bounds[1] = options.ybounds[0];
            bounds[3] = options.ybounds[1];
        } else {
            for(i = 0; i < len; i++) {
                xx = positions[i * 2];
                yy = positions[i * 2 + 1];

                if(xx < bounds[0]) bounds[0] = xx;
                if(xx > bounds[2]) bounds[2] = xx;
                if(yy < bounds[1]) bounds[1] = yy;
                if(yy > bounds[3]) bounds[3] = yy;
            }
        }

        if(index) {
            idToIndex = index;
        } else {
            idToIndex = new Int32Array(len);

            for(i = 0; i < len; i++) {
                idToIndex[i] = i;
            }
        }
    } else {
        len = x.length;

        positions = new Float32Array(2 * len);
        idToIndex = new Int32Array(len);

        for(i = 0; i < len; i++) {
            xx = x[i];
            yy = y[i];

            idToIndex[i] = i;

            positions[i * 2] = xx;
            positions[i * 2 + 1] = yy;

            if(xx < bounds[0]) bounds[0] = xx;
            if(xx > bounds[2]) bounds[2] = xx;
            if(yy < bounds[1]) bounds[1] = yy;
            if(yy > bounds[3]) bounds[3] = yy;
        }
    }

    this.idToIndex = idToIndex;
    this.pointcloudOptions.idToIndex = idToIndex;

    this.pointcloudOptions.positions = positions;

    var markerColor = str2RGBArray(options.marker.color);
    var borderColor = str2RGBArray(options.marker.border.color);
    var opacity = options.opacity * options.marker.opacity;

    markerColor[3] *= opacity;
    this.pointcloudOptions.color = markerColor;

    // detect blending from the number of points, if undefined
    // because large data with blending hits performance
    var blend = options.marker.blend;
    if(blend === null) {
        var maxPoints = 100;
        blend = x.length < maxPoints || y.length < maxPoints;
    }
    this.pointcloudOptions.blend = blend;

    borderColor[3] *= opacity;
    this.pointcloudOptions.borderColor = borderColor;

    var markerSizeMin = options.marker.sizemin;
    var markerSizeMax = Math.max(options.marker.sizemax, options.marker.sizemin);
    this.pointcloudOptions.sizeMin = markerSizeMin;
    this.pointcloudOptions.sizeMax = markerSizeMax;
    this.pointcloudOptions.areaRatio = options.marker.border.arearatio;

    this.pointcloud.update(this.pointcloudOptions);

    // add item for autorange routine
    var xa = this.scene.xaxis;
    var ya = this.scene.yaxis;
    var pad = markerSizeMax / 2 || 0.5;
    options._extremes[xa._id] = findExtremes(xa, [bounds[0], bounds[2]], {ppad: pad});
    options._extremes[ya._id] = findExtremes(ya, [bounds[1], bounds[3]], {ppad: pad});
};

proto.dispose = function() {
    this.pointcloud.dispose();
};

function createPointcloud(scene, data) {
    var plot = new Pointcloud(scene, data.uid);
    plot.update(data);
    return plot;
}

module.exports = createPointcloud;
