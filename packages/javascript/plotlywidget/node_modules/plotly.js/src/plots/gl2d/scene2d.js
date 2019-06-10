/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Registry = require('../../registry');
var Axes = require('../../plots/cartesian/axes');
var Fx = require('../../components/fx');

var createPlot2D = require('gl-plot2d');
var createSpikes = require('gl-spikes2d');
var createSelectBox = require('gl-select-box');
var getContext = require('webgl-context');

var createOptions = require('./convert');
var createCamera = require('./camera');
var showNoWebGlMsg = require('../../lib/show_no_webgl_msg');
var axisConstraints = require('../cartesian/constraints');
var enforceAxisConstraints = axisConstraints.enforce;
var cleanAxisConstraints = axisConstraints.clean;
var doAutoRange = require('../cartesian/autorange').doAutoRange;

var AXES = ['xaxis', 'yaxis'];
var STATIC_CANVAS, STATIC_CONTEXT;

var SUBPLOT_PATTERN = require('../cartesian/constants').SUBPLOT_PATTERN;


function Scene2D(options, fullLayout) {
    this.container = options.container;
    this.graphDiv = options.graphDiv;
    this.pixelRatio = options.plotGlPixelRatio || window.devicePixelRatio;
    this.id = options.id;
    this.staticPlot = !!options.staticPlot;
    this.scrollZoom = this.graphDiv._context._scrollZoom.cartesian;

    this.fullData = null;
    this.updateRefs(fullLayout);

    this.makeFramework();
    if(this.stopped) return;

    // update options
    this.glplotOptions = createOptions(this);
    this.glplotOptions.merge(fullLayout);

    // create the plot
    this.glplot = createPlot2D(this.glplotOptions);

    // create camera
    this.camera = createCamera(this);

    // trace set
    this.traces = {};

    // create axes spikes
    this.spikes = createSpikes(this.glplot);

    this.selectBox = createSelectBox(this.glplot, {
        innerFill: false,
        outerFill: true
    });

    // last button state
    this.lastButtonState = 0;

    // last pick result
    this.pickResult = null;

    // is the mouse over the plot?
    // it's OK if this says true when it's not, so long as
    // when we get a mouseout we set it to false before handling
    this.isMouseOver = true;

    // flag to stop render loop
    this.stopped = false;

    // redraw the plot
    this.redraw = this.draw.bind(this);
    this.redraw();
}

module.exports = Scene2D;

var proto = Scene2D.prototype;

proto.makeFramework = function() {
    // create canvas and gl context
    if(this.staticPlot) {
        if(!STATIC_CONTEXT) {
            STATIC_CANVAS = document.createElement('canvas');

            STATIC_CONTEXT = getContext({
                canvas: STATIC_CANVAS,
                preserveDrawingBuffer: false,
                premultipliedAlpha: true,
                antialias: true
            });

            if(!STATIC_CONTEXT) {
                throw new Error('Error creating static canvas/context for image server');
            }
        }

        this.canvas = STATIC_CANVAS;
        this.gl = STATIC_CONTEXT;
    } else {
        var liveCanvas = this.container.querySelector('.gl-canvas-focus');

        var gl = getContext({
            canvas: liveCanvas,
            preserveDrawingBuffer: true,
            premultipliedAlpha: true
        });

        if(!gl) {
            showNoWebGlMsg(this);
            this.stopped = true;
            return;
        }

        this.canvas = liveCanvas;
        this.gl = gl;
    }

    // position the canvas
    var canvas = this.canvas;

    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.position = 'absolute';
    canvas.style.top = '0px';
    canvas.style.left = '0px';
    canvas.style['pointer-events'] = 'none';

    this.updateSize(canvas);

    // disabling user select on the canvas
    // sanitizes double-clicks interactions
    // ref: https://github.com/plotly/plotly.js/issues/744
    canvas.className += ' user-select-none';

    // create SVG container for hover text
    var svgContainer = this.svgContainer = document.createElementNS(
        'http://www.w3.org/2000/svg',
        'svg');
    svgContainer.style.position = 'absolute';
    svgContainer.style.top = svgContainer.style.left = '0px';
    svgContainer.style.width = svgContainer.style.height = '100%';
    svgContainer.style['z-index'] = 20;
    svgContainer.style['pointer-events'] = 'none';

    // create div to catch the mouse event
    var mouseContainer = this.mouseContainer = document.createElement('div');
    mouseContainer.style.position = 'absolute';
    mouseContainer.style['pointer-events'] = 'auto';

    this.pickCanvas = this.container.querySelector('.gl-canvas-pick');


    // append canvas, hover svg and mouse div to container
    var container = this.container;
    container.appendChild(svgContainer);
    container.appendChild(mouseContainer);

    var self = this;
    mouseContainer.addEventListener('mouseout', function() {
        self.isMouseOver = false;
        self.unhover();
    });
    mouseContainer.addEventListener('mouseover', function() {
        self.isMouseOver = true;
    });
};

proto.toImage = function(format) {
    if(!format) format = 'png';

    this.stopped = true;

    if(this.staticPlot) this.container.appendChild(STATIC_CANVAS);

    // update canvas size
    this.updateSize(this.canvas);


    // grab context and yank out pixels
    var gl = this.glplot.gl;
    var w = gl.drawingBufferWidth;
    var h = gl.drawingBufferHeight;

    // force redraw
    gl.clearColor(1, 1, 1, 0);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    this.glplot.setDirty();
    this.glplot.draw();

    gl.bindFramebuffer(gl.FRAMEBUFFER, null);

    var pixels = new Uint8Array(w * h * 4);
    gl.readPixels(0, 0, w, h, gl.RGBA, gl.UNSIGNED_BYTE, pixels);

    // flip pixels
    for(var j = 0, k = h - 1; j < k; ++j, --k) {
        for(var i = 0; i < w; ++i) {
            for(var l = 0; l < 4; ++l) {
                var tmp = pixels[4 * (w * j + i) + l];
                pixels[4 * (w * j + i) + l] = pixels[4 * (w * k + i) + l];
                pixels[4 * (w * k + i) + l] = tmp;
            }
        }
    }

    var canvas = document.createElement('canvas');
    canvas.width = w;
    canvas.height = h;

    var context = canvas.getContext('2d');
    var imageData = context.createImageData(w, h);
    imageData.data.set(pixels);
    context.putImageData(imageData, 0, 0);

    var dataURL;

    switch(format) {
        case 'jpeg':
            dataURL = canvas.toDataURL('image/jpeg');
            break;
        case 'webp':
            dataURL = canvas.toDataURL('image/webp');
            break;
        default:
            dataURL = canvas.toDataURL('image/png');
    }

    if(this.staticPlot) this.container.removeChild(STATIC_CANVAS);

    return dataURL;
};

proto.updateSize = function(canvas) {
    if(!canvas) canvas = this.canvas;

    var pixelRatio = this.pixelRatio;
    var fullLayout = this.fullLayout;

    var width = fullLayout.width;
    var height = fullLayout.height;
    var pixelWidth = Math.ceil(pixelRatio * width) |0;
    var pixelHeight = Math.ceil(pixelRatio * height) |0;

    // check for resize
    if(canvas.width !== pixelWidth || canvas.height !== pixelHeight) {
        canvas.width = pixelWidth;
        canvas.height = pixelHeight;
    }

    return canvas;
};

proto.computeTickMarks = function() {
    this.xaxis.setScale();
    this.yaxis.setScale();

    var nextTicks = [
        Axes.calcTicks(this.xaxis),
        Axes.calcTicks(this.yaxis)
    ];

    for(var j = 0; j < 2; ++j) {
        for(var i = 0; i < nextTicks[j].length; ++i) {
            // coercing tick value (may not be a string) to a string
            nextTicks[j][i].text = nextTicks[j][i].text + '';
        }
    }

    return nextTicks;
};

function compareTicks(a, b) {
    for(var i = 0; i < 2; ++i) {
        var aticks = a[i];
        var bticks = b[i];

        if(aticks.length !== bticks.length) return true;

        for(var j = 0; j < aticks.length; ++j) {
            if(aticks[j].x !== bticks[j].x) return true;
        }
    }

    return false;
}

proto.updateRefs = function(newFullLayout) {
    this.fullLayout = newFullLayout;

    var spmatch = this.id.match(SUBPLOT_PATTERN);
    var xaxisName = 'xaxis' + spmatch[1];
    var yaxisName = 'yaxis' + spmatch[2];

    this.xaxis = this.fullLayout[xaxisName];
    this.yaxis = this.fullLayout[yaxisName];
};

proto.relayoutCallback = function() {
    var graphDiv = this.graphDiv;
    var xaxis = this.xaxis;
    var yaxis = this.yaxis;
    var layout = graphDiv.layout;

    // make a meaningful value to be passed on to possible 'plotly_relayout' subscriber(s)
    var update = {};
    var xrange = update[xaxis._name + '.range'] = xaxis.range.slice();
    var yrange = update[yaxis._name + '.range'] = yaxis.range.slice();
    update[xaxis._name + '.autorange'] = xaxis.autorange;
    update[yaxis._name + '.autorange'] = yaxis.autorange;

    Registry.call('_storeDirectGUIEdit', graphDiv.layout, graphDiv._fullLayout._preGUI, update);

    // update the input layout
    var xaIn = layout[xaxis._name];
    xaIn.range = xrange;
    xaIn.autorange = xaxis.autorange;

    var yaIn = layout[yaxis._name];
    yaIn.range = yrange;
    yaIn.autorange = yaxis.autorange;

    // lastInputTime helps determine which one is the latest input (if async)
    update.lastInputTime = this.camera.lastInputTime;
    graphDiv.emit('plotly_relayout', update);
};

proto.cameraChanged = function() {
    var camera = this.camera;

    this.glplot.setDataBox(this.calcDataBox());

    var nextTicks = this.computeTickMarks();
    var curTicks = this.glplotOptions.ticks;

    if(compareTicks(nextTicks, curTicks)) {
        this.glplotOptions.ticks = nextTicks;
        this.glplotOptions.dataBox = camera.dataBox;
        this.glplot.update(this.glplotOptions);
        this.handleAnnotations();
    }
};

proto.handleAnnotations = function() {
    var gd = this.graphDiv;
    var annotations = this.fullLayout.annotations;

    for(var i = 0; i < annotations.length; i++) {
        var ann = annotations[i];

        if(ann.xref === this.xaxis._id && ann.yref === this.yaxis._id) {
            Registry.getComponentMethod('annotations', 'drawOne')(gd, i);
        }
    }
};

proto.destroy = function() {
    if(!this.glplot) return;

    var traces = this.traces;

    if(traces) {
        Object.keys(traces).map(function(key) {
            traces[key].dispose();
            delete traces[key];
        });
    }

    this.glplot.dispose();

    this.container.removeChild(this.svgContainer);
    this.container.removeChild(this.mouseContainer);

    this.fullData = null;
    this.glplot = null;
    this.stopped = true;
    this.camera.mouseListener.enabled = false;
    this.mouseContainer.removeEventListener('wheel', this.camera.wheelListener);
    this.camera = null;
};

proto.plot = function(fullData, calcData, fullLayout) {
    var glplot = this.glplot;

    this.updateRefs(fullLayout);
    this.xaxis.clearCalc();
    this.yaxis.clearCalc();
    this.updateTraces(fullData, calcData);
    this.updateFx(fullLayout.dragmode);

    var width = fullLayout.width;
    var height = fullLayout.height;

    this.updateSize(this.canvas);

    var options = this.glplotOptions;
    options.merge(fullLayout);
    options.screenBox = [0, 0, width, height];

    var mockGraphDiv = {_fullLayout: {
        _axisConstraintGroups: this.graphDiv._fullLayout._axisConstraintGroups,
        xaxis: this.xaxis,
        yaxis: this.yaxis
    }};

    cleanAxisConstraints(mockGraphDiv, this.xaxis);
    cleanAxisConstraints(mockGraphDiv, this.yaxis);

    var size = fullLayout._size;
    var domainX = this.xaxis.domain;
    var domainY = this.yaxis.domain;

    options.viewBox = [
        size.l + domainX[0] * size.w,
        size.b + domainY[0] * size.h,
        (width - size.r) - (1 - domainX[1]) * size.w,
        (height - size.t) - (1 - domainY[1]) * size.h
    ];

    this.mouseContainer.style.width = size.w * (domainX[1] - domainX[0]) + 'px';
    this.mouseContainer.style.height = size.h * (domainY[1] - domainY[0]) + 'px';
    this.mouseContainer.height = size.h * (domainY[1] - domainY[0]);
    this.mouseContainer.style.left = size.l + domainX[0] * size.w + 'px';
    this.mouseContainer.style.top = size.t + (1 - domainY[1]) * size.h + 'px';

    var ax, i;

    for(i = 0; i < 2; ++i) {
        ax = this[AXES[i]];
        ax._length = options.viewBox[i + 2] - options.viewBox[i];

        doAutoRange(this.graphDiv, ax);
        ax.setScale();
    }

    enforceAxisConstraints(mockGraphDiv);

    options.ticks = this.computeTickMarks();

    options.dataBox = this.calcDataBox();

    options.merge(fullLayout);
    glplot.update(options);

    // force redraw so that promise is returned when rendering is completed
    this.glplot.draw();
};

proto.calcDataBox = function() {
    var xaxis = this.xaxis;
    var yaxis = this.yaxis;
    var xrange = xaxis.range;
    var yrange = yaxis.range;
    var xr2l = xaxis.r2l;
    var yr2l = yaxis.r2l;

    return [xr2l(xrange[0]), yr2l(yrange[0]), xr2l(xrange[1]), yr2l(yrange[1])];
};

proto.setRanges = function(dataBox) {
    var xaxis = this.xaxis;
    var yaxis = this.yaxis;
    var xl2r = xaxis.l2r;
    var yl2r = yaxis.l2r;

    xaxis.range = [xl2r(dataBox[0]), xl2r(dataBox[2])];
    yaxis.range = [yl2r(dataBox[1]), yl2r(dataBox[3])];
};

proto.updateTraces = function(fullData, calcData) {
    var traceIds = Object.keys(this.traces);
    var i, j, fullTrace;

    this.fullData = fullData;

    // remove empty traces
    traceIdLoop:
    for(i = 0; i < traceIds.length; i++) {
        var oldUid = traceIds[i];
        var oldTrace = this.traces[oldUid];

        for(j = 0; j < fullData.length; j++) {
            fullTrace = fullData[j];

            if(fullTrace.uid === oldUid && fullTrace.type === oldTrace.type) {
                continue traceIdLoop;
            }
        }

        oldTrace.dispose();
        delete this.traces[oldUid];
    }

    // update / create trace objects
    for(i = 0; i < fullData.length; i++) {
        fullTrace = fullData[i];
        var calcTrace = calcData[i];
        var traceObj = this.traces[fullTrace.uid];

        if(traceObj) traceObj.update(fullTrace, calcTrace);
        else {
            traceObj = fullTrace._module.plot(this, fullTrace, calcTrace);
            this.traces[fullTrace.uid] = traceObj;
        }
    }

    // order object per traces
    this.glplot.objects.sort(function(a, b) {
        return a._trace.index - b._trace.index;
    });
};

proto.updateFx = function(dragmode) {
    // switch to svg interactions in lasso/select mode
    if(dragmode === 'lasso' || dragmode === 'select') {
        this.pickCanvas.style['pointer-events'] = 'none';
        this.mouseContainer.style['pointer-events'] = 'none';
    } else {
        this.pickCanvas.style['pointer-events'] = 'auto';
        this.mouseContainer.style['pointer-events'] = 'auto';
    }

    // set proper cursor
    if(dragmode === 'pan') {
        this.mouseContainer.style.cursor = 'move';
    } else if(dragmode === 'zoom') {
        this.mouseContainer.style.cursor = 'crosshair';
    } else {
        this.mouseContainer.style.cursor = null;
    }
};

proto.emitPointAction = function(nextSelection, eventType) {
    var uid = nextSelection.trace.uid;
    var ptNumber = nextSelection.pointIndex;
    var trace;

    for(var i = 0; i < this.fullData.length; i++) {
        if(this.fullData[i].uid === uid) {
            trace = this.fullData[i];
        }
    }

    var pointData = {
        x: nextSelection.traceCoord[0],
        y: nextSelection.traceCoord[1],
        curveNumber: trace.index,
        pointNumber: ptNumber,
        data: trace._input,
        fullData: this.fullData,
        xaxis: this.xaxis,
        yaxis: this.yaxis
    };

    Fx.appendArrayPointValue(pointData, trace, ptNumber);

    this.graphDiv.emit(eventType, {points: [pointData]});
};

proto.draw = function() {
    if(this.stopped) return;

    requestAnimationFrame(this.redraw);

    var glplot = this.glplot;
    var camera = this.camera;
    var mouseListener = camera.mouseListener;
    var mouseUp = this.lastButtonState === 1 && mouseListener.buttons === 0;
    var fullLayout = this.fullLayout;

    this.lastButtonState = mouseListener.buttons;

    this.cameraChanged();

    var x = mouseListener.x * glplot.pixelRatio;
    var y = this.canvas.height - glplot.pixelRatio * mouseListener.y;

    var result;

    if(camera.boxEnabled && fullLayout.dragmode === 'zoom') {
        this.selectBox.enabled = true;

        var selectBox = this.selectBox.selectBox = [
            Math.min(camera.boxStart[0], camera.boxEnd[0]),
            Math.min(camera.boxStart[1], camera.boxEnd[1]),
            Math.max(camera.boxStart[0], camera.boxEnd[0]),
            Math.max(camera.boxStart[1], camera.boxEnd[1])
        ];

        // 1D zoom
        for(var i = 0; i < 2; i++) {
            if(camera.boxStart[i] === camera.boxEnd[i]) {
                selectBox[i] = glplot.dataBox[i];
                selectBox[i + 2] = glplot.dataBox[i + 2];
            }
        }

        glplot.setDirty();
    } else if(!camera.panning && this.isMouseOver) {
        this.selectBox.enabled = false;

        var size = fullLayout._size;
        var domainX = this.xaxis.domain;
        var domainY = this.yaxis.domain;

        result = glplot.pick(
            (x / glplot.pixelRatio) + size.l + domainX[0] * size.w,
            (y / glplot.pixelRatio) - (size.t + (1 - domainY[1]) * size.h)
        );

        var nextSelection = result && result.object._trace.handlePick(result);

        if(nextSelection && mouseUp) {
            this.emitPointAction(nextSelection, 'plotly_click');
        }

        if(result && result.object._trace.hoverinfo !== 'skip' && fullLayout.hovermode) {
            if(nextSelection && (
                !this.lastPickResult ||
                this.lastPickResult.traceUid !== nextSelection.trace.uid ||
                this.lastPickResult.dataCoord[0] !== nextSelection.dataCoord[0] ||
                this.lastPickResult.dataCoord[1] !== nextSelection.dataCoord[1])
            ) {
                var selection = nextSelection;

                this.lastPickResult = {
                    traceUid: nextSelection.trace ? nextSelection.trace.uid : null,
                    dataCoord: nextSelection.dataCoord.slice()
                };
                this.spikes.update({ center: result.dataCoord });

                selection.screenCoord = [
                    ((glplot.viewBox[2] - glplot.viewBox[0]) *
                    (result.dataCoord[0] - glplot.dataBox[0]) /
                        (glplot.dataBox[2] - glplot.dataBox[0]) + glplot.viewBox[0]) /
                            glplot.pixelRatio,
                    (this.canvas.height - (glplot.viewBox[3] - glplot.viewBox[1]) *
                    (result.dataCoord[1] - glplot.dataBox[1]) /
                        (glplot.dataBox[3] - glplot.dataBox[1]) - glplot.viewBox[1]) /
                            glplot.pixelRatio
                ];

                // this needs to happen before the next block that deletes traceCoord data
                // also it's important to copy, otherwise data is lost by the time event data is read
                this.emitPointAction(nextSelection, 'plotly_hover');

                var trace = this.fullData[selection.trace.index] || {};
                var ptNumber = selection.pointIndex;
                var hoverinfo = Fx.castHoverinfo(trace, fullLayout, ptNumber);

                if(hoverinfo && hoverinfo !== 'all') {
                    var parts = hoverinfo.split('+');
                    if(parts.indexOf('x') === -1) selection.traceCoord[0] = undefined;
                    if(parts.indexOf('y') === -1) selection.traceCoord[1] = undefined;
                    if(parts.indexOf('z') === -1) selection.traceCoord[2] = undefined;
                    if(parts.indexOf('text') === -1) selection.textLabel = undefined;
                    if(parts.indexOf('name') === -1) selection.name = undefined;
                }

                Fx.loneHover({
                    x: selection.screenCoord[0],
                    y: selection.screenCoord[1],
                    xLabel: this.hoverFormatter('xaxis', selection.traceCoord[0]),
                    yLabel: this.hoverFormatter('yaxis', selection.traceCoord[1]),
                    zLabel: selection.traceCoord[2],
                    text: selection.textLabel,
                    name: selection.name,
                    color: Fx.castHoverOption(trace, ptNumber, 'bgcolor') || selection.color,
                    borderColor: Fx.castHoverOption(trace, ptNumber, 'bordercolor'),
                    fontFamily: Fx.castHoverOption(trace, ptNumber, 'font.family'),
                    fontSize: Fx.castHoverOption(trace, ptNumber, 'font.size'),
                    fontColor: Fx.castHoverOption(trace, ptNumber, 'font.color'),
                    nameLength: Fx.castHoverOption(trace, ptNumber, 'namelength'),
                    textAlign: Fx.castHoverOption(trace, ptNumber, 'align')
                }, {
                    container: this.svgContainer,
                    gd: this.graphDiv
                });
            }
        }
    }

    // Remove hover effects if we're not over a point OR
    // if we're zooming or panning (in which case result is not set)
    if(!result) {
        this.unhover();
    }

    glplot.draw();
};

proto.unhover = function() {
    if(this.lastPickResult) {
        this.spikes.update({});
        this.lastPickResult = null;
        this.graphDiv.emit('plotly_unhover');
        Fx.loneUnhover(this.svgContainer);
    }
};

proto.hoverFormatter = function(axisName, val) {
    if(val === undefined) return undefined;

    var axis = this[axisName];
    return Axes.tickText(axis, axis.c2l(val), 'hover').text;
};
