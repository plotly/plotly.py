/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var createLinePlot = require('gl-line3d');
var createScatterPlot = require('gl-scatter3d');
var createErrorBars = require('gl-error3d');
var createMesh = require('gl-mesh3d');
var triangulate = require('delaunay-triangulate');

var Lib = require('../../lib');
var str2RgbaArray = require('../../lib/str2rgbarray');
var formatColor = require('../../lib/gl_format_color').formatColor;
var makeBubbleSizeFn = require('../scatter/make_bubble_size_func');
var DASH_PATTERNS = require('../../constants/gl3d_dashes');
var MARKER_SYMBOLS = require('../../constants/gl3d_markers');

var calculateError = require('./calc_errors');

function LineWithMarkers(scene, uid) {
    this.scene = scene;
    this.uid = uid;
    this.linePlot = null;
    this.scatterPlot = null;
    this.errorBars = null;
    this.textMarkers = null;
    this.delaunayMesh = null;
    this.color = null;
    this.mode = '';
    this.dataPoints = [];
    this.axesBounds = [
        [-Infinity, -Infinity, -Infinity],
        [Infinity, Infinity, Infinity]
    ];
    this.textLabels = null;
    this.data = null;
}

var proto = LineWithMarkers.prototype;

proto.handlePick = function(selection) {
    if(selection.object &&
        (selection.object === this.linePlot ||
         selection.object === this.delaunayMesh ||
         selection.object === this.textMarkers ||
         selection.object === this.scatterPlot)
    ) {
        var ind = selection.index = selection.data.index;

        if(selection.object.highlight) {
            selection.object.highlight(null);
        }
        if(this.scatterPlot) {
            selection.object = this.scatterPlot;
            this.scatterPlot.highlight(selection.data);
        }

        selection.textLabel = '';
        if(this.textLabels) {
            if(Array.isArray(this.textLabels)) {
                if(this.textLabels[ind] || this.textLabels[ind] === 0) {
                    selection.textLabel = this.textLabels[ind];
                }
            } else {
                selection.textLabel = this.textLabels;
            }
        }

        selection.traceCoordinate = [
            this.data.x[ind],
            this.data.y[ind],
            this.data.z[ind]
        ];

        return true;
    }
};

function constructDelaunay(points, color, axis) {
    var u = (axis + 1) % 3;
    var v = (axis + 2) % 3;
    var filteredPoints = [];
    var filteredIds = [];
    var i;

    for(i = 0; i < points.length; ++i) {
        var p = points[i];
        if(isNaN(p[u]) || !isFinite(p[u]) ||
           isNaN(p[v]) || !isFinite(p[v])) {
            continue;
        }
        filteredPoints.push([p[u], p[v]]);
        filteredIds.push(i);
    }
    var cells = triangulate(filteredPoints);
    for(i = 0; i < cells.length; ++i) {
        var c = cells[i];
        for(var j = 0; j < c.length; ++j) {
            c[j] = filteredIds[c[j]];
        }
    }
    return {
        positions: points,
        cells: cells,
        meshColor: color
    };
}

function calculateErrorParams(errors) {
    var capSize = [0.0, 0.0, 0.0];
    var color = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
    var lineWidth = [1.0, 1.0, 1.0];

    for(var i = 0; i < 3; i++) {
        var e = errors[i];

        if(e && e.copy_zstyle !== false && errors[2].visible !== false) e = errors[2];
        if(!e || !e.visible) continue;

        capSize[i] = e.width / 2;  // ballpark rescaling
        color[i] = str2RgbaArray(e.color);
        lineWidth[i] = e.thickness;
    }

    return {capSize: capSize, color: color, lineWidth: lineWidth};
}

function parseAlignmentX(a) {
    if(a === null || a === undefined) return 0;

    return (a.indexOf('left') > -1) ? -1 :
           (a.indexOf('right') > -1) ? 1 : 0;
}

function parseAlignmentY(a) {
    if(a === null || a === undefined) return 0;

    return (a.indexOf('top') > -1) ? -1 :
           (a.indexOf('bottom') > -1) ? 1 : 0;
}

function calculateTextOffset(tp) {
    // Read out text properties

    var defaultAlignmentX = 0;
    var defaultAlignmentY = 0;

    var textOffset = [
        defaultAlignmentX,
        defaultAlignmentY
    ];

    if(Array.isArray(tp)) {
        for(var i = 0; i < tp.length; i++) {
            textOffset[i] = [
                defaultAlignmentX,
                defaultAlignmentY
            ];
            if(tp[i]) {
                textOffset[i][0] = parseAlignmentX(tp[i]);
                textOffset[i][1] = parseAlignmentY(tp[i]);
            }
        }
    } else {
        textOffset[0] = parseAlignmentX(tp);
        textOffset[1] = parseAlignmentY(tp);
    }

    return textOffset;
}


function calculateSize(sizeIn, sizeFn) {
    // rough parity with Plotly 2D markers
    return sizeFn(sizeIn * 4);
}

function calculateSymbol(symbolIn) {
    return MARKER_SYMBOLS[symbolIn];
}

function formatParam(paramIn, len, calculate, dflt, extraFn) {
    var paramOut = null;

    if(Lib.isArrayOrTypedArray(paramIn)) {
        paramOut = [];

        for(var i = 0; i < len; i++) {
            if(paramIn[i] === undefined) paramOut[i] = dflt;
            else paramOut[i] = calculate(paramIn[i], extraFn);
        }
    } else paramOut = calculate(paramIn, Lib.identity);

    return paramOut;
}


function convertPlotlyOptions(scene, data) {
    var points = [];
    var sceneLayout = scene.fullSceneLayout;
    var scaleFactor = scene.dataScale;
    var xaxis = sceneLayout.xaxis;
    var yaxis = sceneLayout.yaxis;
    var zaxis = sceneLayout.zaxis;
    var marker = data.marker;
    var line = data.line;
    var x = data.x || [];
    var y = data.y || [];
    var z = data.z || [];
    var len = x.length;
    var xcalendar = data.xcalendar;
    var ycalendar = data.ycalendar;
    var zcalendar = data.zcalendar;
    var xc, yc, zc;
    var params, i;
    var text;

    // Convert points
    for(i = 0; i < len; i++) {
        // sanitize numbers and apply transforms based on axes.type
        xc = xaxis.d2l(x[i], 0, xcalendar) * scaleFactor[0];
        yc = yaxis.d2l(y[i], 0, ycalendar) * scaleFactor[1];
        zc = zaxis.d2l(z[i], 0, zcalendar) * scaleFactor[2];

        points[i] = [xc, yc, zc];
    }

    // convert text
    if(Array.isArray(data.text)) text = data.text;
    else if(data.text !== undefined) {
        text = new Array(len);
        for(i = 0; i < len; i++) text[i] = data.text;
    }

    // Build object parameters
    params = {
        position: points,
        mode: data.mode,
        text: text
    };

    if('line' in data) {
        params.lineColor = formatColor(line, 1, len);
        params.lineWidth = line.width;
        params.lineDashes = line.dash;
    }

    if('marker' in data) {
        var sizeFn = makeBubbleSizeFn(data);

        params.scatterColor = formatColor(marker, 1, len);
        params.scatterSize = formatParam(marker.size, len, calculateSize, 20, sizeFn);
        params.scatterMarker = formatParam(marker.symbol, len, calculateSymbol, '●');
        params.scatterLineWidth = marker.line.width;  // arrayOk === false
        params.scatterLineColor = formatColor(marker.line, 1, len);
        params.scatterAngle = 0;
    }

    if('textposition' in data) {
        params.textOffset = calculateTextOffset(data.textposition);
        params.textColor = formatColor(data.textfont, 1, len);
        params.textSize = formatParam(data.textfont.size, len, Lib.identity, 12);
        params.textFont = data.textfont.family;  // arrayOk === false
        params.textAngle = 0;
    }

    var dims = ['x', 'y', 'z'];
    params.project = [false, false, false];
    params.projectScale = [1, 1, 1];
    params.projectOpacity = [1, 1, 1];
    for(i = 0; i < 3; ++i) {
        var projection = data.projection[dims[i]];
        if((params.project[i] = projection.show)) {
            params.projectOpacity[i] = projection.opacity;
            params.projectScale[i] = projection.scale;
        }
    }

    params.errorBounds = calculateError(data, scaleFactor, sceneLayout);

    var errorParams = calculateErrorParams([data.error_x, data.error_y, data.error_z]);
    params.errorColor = errorParams.color;
    params.errorLineWidth = errorParams.lineWidth;
    params.errorCapSize = errorParams.capSize;

    params.delaunayAxis = data.surfaceaxis;
    params.delaunayColor = str2RgbaArray(data.surfacecolor);

    return params;
}

function arrayToColor(color) {
    if(Array.isArray(color)) {
        var c = color[0];

        if(Array.isArray(c)) color = c;

        return 'rgb(' + color.slice(0, 3).map(function(x) {
            return Math.round(x * 255);
        }) + ')';
    }

    return null;
}

proto.update = function(data) {
    var gl = this.scene.glplot.gl;
    var lineOptions;
    var scatterOptions;
    var errorOptions;
    var textOptions;
    var dashPattern = DASH_PATTERNS.solid;

    // Save data
    this.data = data;

    // Run data conversion
    var options = convertPlotlyOptions(this.scene, data);

    if('mode' in options) {
        this.mode = options.mode;
    }
    if('lineDashes' in options) {
        if(options.lineDashes in DASH_PATTERNS) {
            dashPattern = DASH_PATTERNS[options.lineDashes];
        }
    }

    this.color = arrayToColor(options.scatterColor) ||
                 arrayToColor(options.lineColor);

    // Save data points
    this.dataPoints = options.position;

    lineOptions = {
        gl: this.scene.glplot.gl,
        position: options.position,
        color: options.lineColor,
        lineWidth: options.lineWidth || 1,
        dashes: dashPattern[0],
        dashScale: dashPattern[1],
        opacity: data.opacity,
        connectGaps: data.connectgaps
    };

    if(this.mode.indexOf('lines') !== -1) {
        if(this.linePlot) this.linePlot.update(lineOptions);
        else {
            this.linePlot = createLinePlot(lineOptions);
            this.linePlot._trace = this;
            this.scene.glplot.add(this.linePlot);
        }
    } else if(this.linePlot) {
        this.scene.glplot.remove(this.linePlot);
        this.linePlot.dispose();
        this.linePlot = null;
    }

    // N.B. marker.opacity must be a scalar for performance
    var scatterOpacity = data.opacity;
    if(data.marker && data.marker.opacity) scatterOpacity *= data.marker.opacity;

    scatterOptions = {
        gl: this.scene.glplot.gl,
        position: options.position,
        color: options.scatterColor,
        size: options.scatterSize,
        glyph: options.scatterMarker,
        opacity: scatterOpacity,
        orthographic: true,
        lineWidth: options.scatterLineWidth,
        lineColor: options.scatterLineColor,
        project: options.project,
        projectScale: options.projectScale,
        projectOpacity: options.projectOpacity
    };

    if(this.mode.indexOf('markers') !== -1) {
        if(this.scatterPlot) this.scatterPlot.update(scatterOptions);
        else {
            this.scatterPlot = createScatterPlot(scatterOptions);
            this.scatterPlot._trace = this;
            this.scatterPlot.highlightScale = 1;
            this.scene.glplot.add(this.scatterPlot);
        }
    } else if(this.scatterPlot) {
        this.scene.glplot.remove(this.scatterPlot);
        this.scatterPlot.dispose();
        this.scatterPlot = null;
    }

    textOptions = {
        gl: this.scene.glplot.gl,
        position: options.position,
        glyph: options.text,
        color: options.textColor,
        size: options.textSize,
        angle: options.textAngle,
        alignment: options.textOffset,
        font: options.textFont,
        orthographic: true,
        lineWidth: 0,
        project: false,
        opacity: data.opacity
    };

    this.textLabels = data.hovertext || data.text;

    if(this.mode.indexOf('text') !== -1) {
        if(this.textMarkers) this.textMarkers.update(textOptions);
        else {
            this.textMarkers = createScatterPlot(textOptions);
            this.textMarkers._trace = this;
            this.textMarkers.highlightScale = 1;
            this.scene.glplot.add(this.textMarkers);
        }
    } else if(this.textMarkers) {
        this.scene.glplot.remove(this.textMarkers);
        this.textMarkers.dispose();
        this.textMarkers = null;
    }

    errorOptions = {
        gl: this.scene.glplot.gl,
        position: options.position,
        color: options.errorColor,
        error: options.errorBounds,
        lineWidth: options.errorLineWidth,
        capSize: options.errorCapSize,
        opacity: data.opacity
    };
    if(this.errorBars) {
        if(options.errorBounds) {
            this.errorBars.update(errorOptions);
        } else {
            this.scene.glplot.remove(this.errorBars);
            this.errorBars.dispose();
            this.errorBars = null;
        }
    } else if(options.errorBounds) {
        this.errorBars = createErrorBars(errorOptions);
        this.errorBars._trace = this;
        this.scene.glplot.add(this.errorBars);
    }

    if(options.delaunayAxis >= 0) {
        var delaunayOptions = constructDelaunay(
            options.position,
            options.delaunayColor,
            options.delaunayAxis
        );
        delaunayOptions.opacity = data.opacity;

        if(this.delaunayMesh) {
            this.delaunayMesh.update(delaunayOptions);
        } else {
            delaunayOptions.gl = gl;
            this.delaunayMesh = createMesh(delaunayOptions);
            this.delaunayMesh._trace = this;
            this.scene.glplot.add(this.delaunayMesh);
        }
    } else if(this.delaunayMesh) {
        this.scene.glplot.remove(this.delaunayMesh);
        this.delaunayMesh.dispose();
        this.delaunayMesh = null;
    }
};

proto.dispose = function() {
    if(this.linePlot) {
        this.scene.glplot.remove(this.linePlot);
        this.linePlot.dispose();
    }
    if(this.scatterPlot) {
        this.scene.glplot.remove(this.scatterPlot);
        this.scatterPlot.dispose();
    }
    if(this.errorBars) {
        this.scene.glplot.remove(this.errorBars);
        this.errorBars.dispose();
    }
    if(this.textMarkers) {
        this.scene.glplot.remove(this.textMarkers);
        this.textMarkers.dispose();
    }
    if(this.delaunayMesh) {
        this.scene.glplot.remove(this.delaunayMesh);
        this.delaunayMesh.dispose();
    }
};

function createLineWithMarkers(scene, data) {
    var plot = new LineWithMarkers(scene, data.uid);
    plot.update(data);
    return plot;
}

module.exports = createLineWithMarkers;
