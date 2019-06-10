/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Axes = require('../cartesian/axes');

var str2RGBArray = require('../../lib/str2rgbarray');

function Axes2DOptions(scene) {
    this.scene = scene;
    this.gl = scene.gl;
    this.pixelRatio = scene.pixelRatio;

    this.screenBox = [0, 0, 1, 1];
    this.viewBox = [0, 0, 1, 1];
    this.dataBox = [-1, -1, 1, 1];

    this.borderLineEnable = [false, false, false, false];
    this.borderLineWidth = [1, 1, 1, 1];
    this.borderLineColor = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ];

    this.ticks = [[], []];
    this.tickEnable = [true, true, false, false];
    this.tickPad = [15, 15, 15, 15];
    this.tickAngle = [0, 0, 0, 0];
    this.tickColor = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ];
    this.tickMarkLength = [0, 0, 0, 0];
    this.tickMarkWidth = [0, 0, 0, 0];
    this.tickMarkColor = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ];

    this.labels = ['x', 'y'];
    this.labelEnable = [true, true, false, false];
    this.labelAngle = [0, Math.PI / 2, 0, 3.0 * Math.PI / 2];
    this.labelPad = [15, 15, 15, 15];
    this.labelSize = [12, 12];
    this.labelFont = ['sans-serif', 'sans-serif'];
    this.labelColor = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ];

    this.title = '';
    this.titleEnable = true;
    this.titleCenter = [0, 0, 0, 0];
    this.titleAngle = 0;
    this.titleColor = [0, 0, 0, 1];
    this.titleFont = 'sans-serif';
    this.titleSize = 18;

    this.gridLineEnable = [true, true];
    this.gridLineColor = [
        [0, 0, 0, 0.5],
        [0, 0, 0, 0.5]
    ];
    this.gridLineWidth = [1, 1];

    this.zeroLineEnable = [true, true];
    this.zeroLineWidth = [1, 1];
    this.zeroLineColor = [
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ];

    this.borderColor = [0, 0, 0, 0];
    this.backgroundColor = [0, 0, 0, 0];

    this.static = this.scene.staticPlot;
}

var proto = Axes2DOptions.prototype;

var AXES = ['xaxis', 'yaxis'];

proto.merge = function(options) {
    // titles are rendered in SVG
    this.titleEnable = false;
    this.backgroundColor = str2RGBArray(options.plot_bgcolor);

    var axisName, ax, axTitle, axMirror;
    var hasAxisInDfltPos, hasAxisInAltrPos, hasSharedAxis, mirrorLines, mirrorTicks;
    var i, j;

    for(i = 0; i < 2; ++i) {
        axisName = AXES[i];
        var axisLetter = axisName.charAt(0);

        // get options relevant to this subplot,
        // '_name' is e.g. xaxis, xaxis2, yaxis, yaxis4 ...
        ax = options[this.scene[axisName]._name];

        axTitle = ax.title.text === this.scene.fullLayout._dfltTitle[axisLetter] ? '' : ax.title.text;

        for(j = 0; j <= 2; j += 2) {
            this.labelEnable[i + j] = false;
            this.labels[i + j] = axTitle;
            this.labelColor[i + j] = str2RGBArray(ax.title.font.color);
            this.labelFont[i + j] = ax.title.font.family;
            this.labelSize[i + j] = ax.title.font.size;
            this.labelPad[i + j] = this.getLabelPad(axisName, ax);

            this.tickEnable[i + j] = false;
            this.tickColor[i + j] = str2RGBArray((ax.tickfont || {}).color);
            this.tickAngle[i + j] = (ax.tickangle === 'auto') ?
                0 :
                Math.PI * -ax.tickangle / 180;
            this.tickPad[i + j] = this.getTickPad(ax);

            this.tickMarkLength[i + j] = 0;
            this.tickMarkWidth[i + j] = ax.tickwidth || 0;
            this.tickMarkColor[i + j] = str2RGBArray(ax.tickcolor);

            this.borderLineEnable[i + j] = false;
            this.borderLineColor[i + j] = str2RGBArray(ax.linecolor);
            this.borderLineWidth[i + j] = ax.linewidth || 0;
        }

        hasSharedAxis = this.hasSharedAxis(ax);
        hasAxisInDfltPos = this.hasAxisInDfltPos(axisName, ax) && !hasSharedAxis;
        hasAxisInAltrPos = this.hasAxisInAltrPos(axisName, ax) && !hasSharedAxis;

        axMirror = ax.mirror || false;
        mirrorLines = hasSharedAxis ?
            (String(axMirror).indexOf('all') !== -1) :  // 'all' or 'allticks'
            !!axMirror;                                 // all but false
        mirrorTicks = hasSharedAxis ?
            (axMirror === 'allticks') :
            (String(axMirror).indexOf('ticks') !== -1); // 'ticks' or 'allticks'

        // Axis titles and tick labels can only appear of one side of the scene
        //  and are never show on subplots that share existing axes.

        if(hasAxisInDfltPos) this.labelEnable[i] = true;
        else if(hasAxisInAltrPos) this.labelEnable[i + 2] = true;

        if(hasAxisInDfltPos) this.tickEnable[i] = ax.showticklabels;
        else if(hasAxisInAltrPos) this.tickEnable[i + 2] = ax.showticklabels;

        // Grid lines and ticks can appear on both sides of the scene
        //  and can appear on subplot that share existing axes via `ax.mirror`.

        if(hasAxisInDfltPos || mirrorLines) this.borderLineEnable[i] = ax.showline;
        if(hasAxisInAltrPos || mirrorLines) this.borderLineEnable[i + 2] = ax.showline;

        if(hasAxisInDfltPos || mirrorTicks) this.tickMarkLength[i] = this.getTickMarkLength(ax);
        if(hasAxisInAltrPos || mirrorTicks) this.tickMarkLength[i + 2] = this.getTickMarkLength(ax);

        this.gridLineEnable[i] = ax.showgrid;
        this.gridLineColor[i] = str2RGBArray(ax.gridcolor);
        this.gridLineWidth[i] = ax.gridwidth;

        this.zeroLineEnable[i] = ax.zeroline;
        this.zeroLineColor[i] = str2RGBArray(ax.zerolinecolor);
        this.zeroLineWidth[i] = ax.zerolinewidth;
    }
};

// is an axis shared with an already-drawn subplot ?
proto.hasSharedAxis = function(ax) {
    var scene = this.scene;
    var subplotIds = scene.fullLayout._subplots.gl2d;
    var list = Axes.findSubplotsWithAxis(subplotIds, ax);

    // if index === 0, then the subplot is already drawn as subplots
    // are drawn in order.
    return (list.indexOf(scene.id) !== 0);
};

// has an axis in default position (i.e. bottom/left) ?
proto.hasAxisInDfltPos = function(axisName, ax) {
    var axSide = ax.side;

    if(axisName === 'xaxis') return (axSide === 'bottom');
    else if(axisName === 'yaxis') return (axSide === 'left');
};

// has an axis in alternate position (i.e. top/right) ?
proto.hasAxisInAltrPos = function(axisName, ax) {
    var axSide = ax.side;

    if(axisName === 'xaxis') return (axSide === 'top');
    else if(axisName === 'yaxis') return (axSide === 'right');
};

proto.getLabelPad = function(axisName, ax) {
    var offsetBase = 1.5;
    var fontSize = ax.title.font.size;
    var showticklabels = ax.showticklabels;

    if(axisName === 'xaxis') {
        return (ax.side === 'top') ?
            -10 + fontSize * (offsetBase + (showticklabels ? 1 : 0)) :
            -10 + fontSize * (offsetBase + (showticklabels ? 0.5 : 0));
    } else if(axisName === 'yaxis') {
        return (ax.side === 'right') ?
            10 + fontSize * (offsetBase + (showticklabels ? 1 : 0.5)) :
            10 + fontSize * (offsetBase + (showticklabels ? 0.5 : 0));
    }
};

proto.getTickPad = function(ax) {
    return (ax.ticks === 'outside') ? 10 + ax.ticklen : 15;
};

proto.getTickMarkLength = function(ax) {
    if(!ax.ticks) return 0;

    var ticklen = ax.ticklen;

    return (ax.ticks === 'inside') ? -ticklen : ticklen;
};


function createAxes2D(scene) {
    return new Axes2DOptions(scene);
}

module.exports = createAxes2D;
