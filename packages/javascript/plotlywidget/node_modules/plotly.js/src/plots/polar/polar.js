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

var Registry = require('../../registry');
var Lib = require('../../lib');
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');
var Plots = require('../plots');
var Axes = require('../../plots/cartesian/axes');
var setConvertCartesian = require('../cartesian/set_convert');
var setConvertPolar = require('./set_convert');
var doAutoRange = require('../cartesian/autorange').doAutoRange;
var dragBox = require('../cartesian/dragbox');
var dragElement = require('../../components/dragelement');
var Fx = require('../../components/fx');
var Titles = require('../../components/titles');
var prepSelect = require('../cartesian/select').prepSelect;
var selectOnClick = require('../cartesian/select').selectOnClick;
var clearSelect = require('../cartesian/select').clearSelect;
var setCursor = require('../../lib/setcursor');
var clearGlCanvases = require('../../lib/clear_gl_canvases');
var redrawReglTraces = require('../../plot_api/subroutines').redrawReglTraces;

var MID_SHIFT = require('../../constants/alignment').MID_SHIFT;
var constants = require('./constants');
var helpers = require('./helpers');

var _ = Lib._;
var mod = Lib.mod;
var deg2rad = Lib.deg2rad;
var rad2deg = Lib.rad2deg;

function Polar(gd, id) {
    this.id = id;
    this.gd = gd;

    this._hasClipOnAxisFalse = null;
    this.vangles = null;
    this.radialAxisAngle = null;
    this.traceHash = {};
    this.layers = {};
    this.clipPaths = {};
    this.clipIds = {};
    this.viewInitial = {};

    var fullLayout = gd._fullLayout;
    var clipIdBase = 'clip' + fullLayout._uid + id;

    this.clipIds.forTraces = clipIdBase + '-for-traces';
    this.clipPaths.forTraces = fullLayout._clips.append('clipPath')
        .attr('id', this.clipIds.forTraces);
    this.clipPaths.forTraces.append('path');

    this.framework = fullLayout._polarlayer.append('g')
        .attr('class', id);

    // unfortunately, we have to keep track of some axis tick settings
    // as polar subplots do not implement the 'ticks' editType
    this.radialTickLayout = null;
    this.angularTickLayout = null;
}

var proto = Polar.prototype;

module.exports = function createPolar(gd, id) {
    return new Polar(gd, id);
};

proto.plot = function(polarCalcData, fullLayout) {
    var _this = this;
    var polarLayout = fullLayout[_this.id];

    _this._hasClipOnAxisFalse = false;
    for(var i = 0; i < polarCalcData.length; i++) {
        var trace = polarCalcData[i][0].trace;
        if(trace.cliponaxis === false) {
            _this._hasClipOnAxisFalse = true;
            break;
        }
    }

    _this.updateLayers(fullLayout, polarLayout);
    _this.updateLayout(fullLayout, polarLayout);
    Plots.generalUpdatePerTraceModule(_this.gd, _this, polarCalcData, polarLayout);
    _this.updateFx(fullLayout, polarLayout);
};

proto.updateLayers = function(fullLayout, polarLayout) {
    var _this = this;
    var layers = _this.layers;
    var radialLayout = polarLayout.radialaxis;
    var angularLayout = polarLayout.angularaxis;
    var layerNames = constants.layerNames;

    var frontPlotIndex = layerNames.indexOf('frontplot');
    var layerData = layerNames.slice(0, frontPlotIndex);
    var isAngularAxisBelowTraces = angularLayout.layer === 'below traces';
    var isRadialAxisBelowTraces = radialLayout.layer === 'below traces';

    if(isAngularAxisBelowTraces) layerData.push('angular-line');
    if(isRadialAxisBelowTraces) layerData.push('radial-line');
    if(isAngularAxisBelowTraces) layerData.push('angular-axis');
    if(isRadialAxisBelowTraces) layerData.push('radial-axis');

    layerData.push('frontplot');

    if(!isAngularAxisBelowTraces) layerData.push('angular-line');
    if(!isRadialAxisBelowTraces) layerData.push('radial-line');
    if(!isAngularAxisBelowTraces) layerData.push('angular-axis');
    if(!isRadialAxisBelowTraces) layerData.push('radial-axis');

    var join = _this.framework.selectAll('.polarsublayer')
        .data(layerData, String);

    join.enter().append('g')
        .attr('class', function(d) { return 'polarsublayer ' + d;})
        .each(function(d) {
            var sel = layers[d] = d3.select(this);

            switch(d) {
                case 'frontplot':
                    // TODO add option to place in 'backplot' layer??
                    sel.append('g').classed('barlayer', true);
                    sel.append('g').classed('scatterlayer', true);
                    break;
                case 'backplot':
                    sel.append('g').classed('maplayer', true);
                    break;
                case 'plotbg':
                    layers.bg = sel.append('path');
                    break;
                case 'radial-grid':
                    sel.style('fill', 'none');
                    break;
                case 'angular-grid':
                    sel.style('fill', 'none');
                    break;
                case 'radial-line':
                    sel.append('line').style('fill', 'none');
                    break;
                case 'angular-line':
                    sel.append('path').style('fill', 'none');
                    break;
            }
        });

    join.order();
};

/* Polar subplots juggle with 6 'axis objects' (!), these are:
 *
 * - polarLayout.radialaxis (aka radialLayout in this file):
 * - polarLayout.angularaxis (aka angularLayout in this file):
 *   used for data -> calcdata conversions (aka d2c) during the calc step
 *
 * - this.radialAxis
 *   extends polarLayout.radialaxis, adds mocked 'domain' and
 *   few other keys in order to reuse Cartesian doAutoRange and the Axes
 *   drawing routines.
 *   used for calcdata -> geometric conversions (aka c2g) during the plot step
 *   + setGeometry setups ax.c2g for given ax.range
 *   + setScale setups ax._m,ax._b for given ax.range
 *
 * - this.angularAxis
 *   extends polarLayout.angularaxis, adds mocked 'range' and 'domain' and
 *   a few other keys in order to reuse the Axes drawing routines.
 *   used for calcdata -> geometric conversions (aka c2g) during the plot step
 *   + setGeometry setups ax.c2g given ax.rotation, ax.direction & ax._categories,
 *                 and mocks ax.range
 *   + setScale setups ax._m,ax._b with that mocked ax.range
 *
 * - this.xaxis
 * - this.yaxis
 *   setup so that polar traces can reuse plot methods of Cartesian traces
 *   which mostly rely on 2pixel methods (e.g ax.c2p)
 */
proto.updateLayout = function(fullLayout, polarLayout) {
    var _this = this;
    var layers = _this.layers;
    var gs = fullLayout._size;

    // axis attributes
    var radialLayout = polarLayout.radialaxis;
    var angularLayout = polarLayout.angularaxis;
    // layout domains
    var xDomain = polarLayout.domain.x;
    var yDomain = polarLayout.domain.y;
    // offsets from paper edge to layout domain box
    _this.xOffset = gs.l + gs.w * xDomain[0];
    _this.yOffset = gs.t + gs.h * (1 - yDomain[1]);
    // lengths of the layout domain box
    var xLength = _this.xLength = gs.w * (xDomain[1] - xDomain[0]);
    var yLength = _this.yLength = gs.h * (yDomain[1] - yDomain[0]);
    // sector to plot
    var sector = polarLayout.sector;
    _this.sectorInRad = sector.map(deg2rad);
    var sectorBBox = _this.sectorBBox = computeSectorBBox(sector);
    var dxSectorBBox = sectorBBox[2] - sectorBBox[0];
    var dySectorBBox = sectorBBox[3] - sectorBBox[1];
    // aspect ratios
    var arDomain = yLength / xLength;
    var arSector = Math.abs(dySectorBBox / dxSectorBBox);
    // actual lengths and domains of subplot box
    var xLength2, yLength2;
    var xDomain2, yDomain2;
    var gap;
    if(arDomain > arSector) {
        xLength2 = xLength;
        yLength2 = xLength * arSector;
        gap = (yLength - yLength2) / gs.h / 2;
        xDomain2 = [xDomain[0], xDomain[1]];
        yDomain2 = [yDomain[0] + gap, yDomain[1] - gap];
    } else {
        xLength2 = yLength / arSector;
        yLength2 = yLength;
        gap = (xLength - xLength2) / gs.w / 2;
        xDomain2 = [xDomain[0] + gap, xDomain[1] - gap];
        yDomain2 = [yDomain[0], yDomain[1]];
    }
    _this.xLength2 = xLength2;
    _this.yLength2 = yLength2;
    _this.xDomain2 = xDomain2;
    _this.yDomain2 = yDomain2;
    // actual offsets from paper edge to the subplot box top-left corner
    var xOffset2 = _this.xOffset2 = gs.l + gs.w * xDomain2[0];
    var yOffset2 = _this.yOffset2 = gs.t + gs.h * (1 - yDomain2[1]);
    // circle radius in px
    var radius = _this.radius = xLength2 / dxSectorBBox;
    // 'inner' radius in px (when polar.hole is set)
    var innerRadius = _this.innerRadius = polarLayout.hole * radius;
    // circle center position in px
    var cx = _this.cx = xOffset2 - radius * sectorBBox[0];
    var cy = _this.cy = yOffset2 + radius * sectorBBox[3];
    // circle center in the coordinate system of plot area
    var cxx = _this.cxx = cx - xOffset2;
    var cyy = _this.cyy = cy - yOffset2;

    _this.radialAxis = _this.mockAxis(fullLayout, polarLayout, radialLayout, {
        // make this an 'x' axis to make positioning (especially rotation) easier
        _id: 'x',
        // convert to 'x' axis equivalent
        side: {
            counterclockwise: 'top',
            clockwise: 'bottom'
        }[radialLayout.side],
        // spans length 1 radius
        domain: [innerRadius / gs.w, radius / gs.w]
    });

    _this.angularAxis = _this.mockAxis(fullLayout, polarLayout, angularLayout, {
        side: 'right',
        // to get auto nticks right
        domain: [0, Math.PI],
        // don't pass through autorange logic
        autorange: false
    });

    _this.doAutoRange(fullLayout, polarLayout);
    // N.B. this sets _this.vangles
    _this.updateAngularAxis(fullLayout, polarLayout);
    // N.B. this sets _this.radialAxisAngle
    _this.updateRadialAxis(fullLayout, polarLayout);
    _this.updateRadialAxisTitle(fullLayout, polarLayout);

    _this.xaxis = _this.mockCartesianAxis(fullLayout, polarLayout, {
        _id: 'x',
        domain: xDomain2
    });

    _this.yaxis = _this.mockCartesianAxis(fullLayout, polarLayout, {
        _id: 'y',
        domain: yDomain2
    });

    var dPath = _this.pathSubplot();

    _this.clipPaths.forTraces.select('path')
        .attr('d', dPath)
        .attr('transform', strTranslate(cxx, cyy));

    layers.frontplot
        .attr('transform', strTranslate(xOffset2, yOffset2))
        .call(Drawing.setClipUrl, _this._hasClipOnAxisFalse ? null : _this.clipIds.forTraces, _this.gd);

    layers.bg
        .attr('d', dPath)
        .attr('transform', strTranslate(cx, cy))
        .call(Color.fill, polarLayout.bgcolor);
};

proto.mockAxis = function(fullLayout, polarLayout, axLayout, opts) {
    var commonOpts = {
        // to get _boundingBox computation right when showticklabels is false
        anchor: 'free',
        position: 0
    };

    var ax = Lib.extendFlat(commonOpts, axLayout, opts);
    setConvertPolar(ax, polarLayout, fullLayout);
    return ax;
};

proto.mockCartesianAxis = function(fullLayout, polarLayout, opts) {
    var _this = this;
    var axId = opts._id;

    var ax = Lib.extendFlat({type: 'linear'}, opts);
    setConvertCartesian(ax, fullLayout);

    var bboxIndices = {
        x: [0, 2],
        y: [1, 3]
    };

    ax.setRange = function() {
        var sectorBBox = _this.sectorBBox;
        var ind = bboxIndices[axId];
        var rl = _this.radialAxis._rl;
        var drl = (rl[1] - rl[0]) / (1 - polarLayout.hole);
        ax.range = [sectorBBox[ind[0]] * drl, sectorBBox[ind[1]] * drl];
    };

    ax.isPtWithinRange = axId === 'x' ?
        function(d) { return _this.isPtInside(d); } :
        function() { return true; };

    ax.setRange();
    ax.setScale();
    return ax;
};

proto.doAutoRange = function(fullLayout, polarLayout) {
    var gd = this.gd;
    var radialAxis = this.radialAxis;
    var radialLayout = polarLayout.radialaxis;

    radialAxis.setScale();
    doAutoRange(gd, radialAxis);

    var rng = radialAxis.range;
    radialLayout.range = rng.slice();
    radialLayout._input.range = rng.slice();

    radialAxis._rl = [
        radialAxis.r2l(rng[0], null, 'gregorian'),
        radialAxis.r2l(rng[1], null, 'gregorian')
    ];
};

proto.updateRadialAxis = function(fullLayout, polarLayout) {
    var _this = this;
    var gd = _this.gd;
    var layers = _this.layers;
    var radius = _this.radius;
    var innerRadius = _this.innerRadius;
    var cx = _this.cx;
    var cy = _this.cy;
    var radialLayout = polarLayout.radialaxis;
    var a0 = mod(polarLayout.sector[0], 360);
    var ax = _this.radialAxis;
    var hasRoomForIt = innerRadius < radius;

    _this.fillViewInitialKey('radialaxis.angle', radialLayout.angle);
    _this.fillViewInitialKey('radialaxis.range', ax.range.slice());

    ax.setGeometry();

    // rotate auto tick labels by 180 if in quadrant II and III to make them
    // readable from left-to-right
    //
    // TODO try moving deeper in Axes.drawLabels for better results?
    if(ax.tickangle === 'auto' && (a0 > 90 && a0 <= 270)) {
        ax.tickangle = 180;
    }

    // easier to set rotate angle with custom translate function
    var transFn = function(d) {
        return 'translate(' + (ax.l2p(d.x) + innerRadius) + ',0)';
    };

    // set special grid path function
    var gridPathFn = function(d) {
        return _this.pathArc(ax.r2p(d.x) + innerRadius);
    };

    var newTickLayout = strTickLayout(radialLayout);
    if(_this.radialTickLayout !== newTickLayout) {
        layers['radial-axis'].selectAll('.xtick').remove();
        _this.radialTickLayout = newTickLayout;
    }

    if(hasRoomForIt) {
        ax.setScale();

        var vals = Axes.calcTicks(ax);
        var valsClipped = Axes.clipEnds(ax, vals);
        var tickSign = Axes.getTickSigns(ax)[2];

        Axes.drawTicks(gd, ax, {
            vals: vals,
            layer: layers['radial-axis'],
            path: Axes.makeTickPath(ax, 0, tickSign),
            transFn: transFn,
            crisp: false
        });

        Axes.drawGrid(gd, ax, {
            vals: valsClipped,
            layer: layers['radial-grid'],
            path: gridPathFn,
            transFn: Lib.noop,
            crisp: false
        });

        Axes.drawLabels(gd, ax, {
            vals: vals,
            layer: layers['radial-axis'],
            transFn: transFn,
            labelFns: Axes.makeLabelFns(ax, 0)
        });
    }

    // stash 'actual' radial axis angle for drag handlers (in degrees)
    var angle = _this.radialAxisAngle = _this.vangles ?
        rad2deg(snapToVertexAngle(deg2rad(radialLayout.angle), _this.vangles)) :
        radialLayout.angle;

    var tLayer = strTranslate(cx, cy);
    var tLayer2 = tLayer + strRotate(-angle);

    updateElement(
        layers['radial-axis'],
        hasRoomForIt && (radialLayout.showticklabels || radialLayout.ticks),
        {transform: tLayer2}
    );

    updateElement(
        layers['radial-grid'],
        hasRoomForIt && radialLayout.showgrid,
        {transform: tLayer}
    );

    updateElement(
        layers['radial-line'].select('line'),
        hasRoomForIt && radialLayout.showline,
        {
            x1: innerRadius,
            y1: 0,
            x2: radius,
            y2: 0,
            transform: tLayer2
        }
    )
    .attr('stroke-width', radialLayout.linewidth)
    .call(Color.stroke, radialLayout.linecolor);
};

proto.updateRadialAxisTitle = function(fullLayout, polarLayout, _angle) {
    var _this = this;
    var gd = _this.gd;
    var radius = _this.radius;
    var cx = _this.cx;
    var cy = _this.cy;
    var radialLayout = polarLayout.radialaxis;
    var titleClass = _this.id + 'title';

    var angle = _angle !== undefined ? _angle : _this.radialAxisAngle;
    var angleRad = deg2rad(angle);
    var cosa = Math.cos(angleRad);
    var sina = Math.sin(angleRad);

    var pad = 0;

    // Hint: no need to check if there is in fact a title.text set
    // because if plot is editable, pad needs to be calculated anyways
    // to properly show placeholder text when title is empty.
    if(radialLayout.title) {
        var h = Drawing.bBox(_this.layers['radial-axis'].node()).height;
        var ts = radialLayout.title.font.size;
        pad = radialLayout.side === 'counterclockwise' ?
            -h - ts * 0.4 :
            h + ts * 0.8;
    }

    _this.layers['radial-axis-title'] = Titles.draw(gd, titleClass, {
        propContainer: radialLayout,
        propName: _this.id + '.radialaxis.title',
        placeholder: _(gd, 'Click to enter radial axis title'),
        attributes: {
            x: cx + (radius / 2) * cosa + pad * sina,
            y: cy - (radius / 2) * sina + pad * cosa,
            'text-anchor': 'middle'
        },
        transform: {rotate: -angle}
    });
};

proto.updateAngularAxis = function(fullLayout, polarLayout) {
    var _this = this;
    var gd = _this.gd;
    var layers = _this.layers;
    var radius = _this.radius;
    var innerRadius = _this.innerRadius;
    var cx = _this.cx;
    var cy = _this.cy;
    var angularLayout = polarLayout.angularaxis;
    var ax = _this.angularAxis;

    _this.fillViewInitialKey('angularaxis.rotation', angularLayout.rotation);

    ax.setGeometry();
    ax.setScale();

    // 't'ick to 'g'eometric radians is used all over the place here
    var t2g = function(d) { return ax.t2g(d.x); };

    // run rad2deg on tick0 and ditck for thetaunit: 'radians' axes
    if(ax.type === 'linear' && ax.thetaunit === 'radians') {
        ax.tick0 = rad2deg(ax.tick0);
        ax.dtick = rad2deg(ax.dtick);
    }

    var _transFn = function(rad) {
        return strTranslate(cx + radius * Math.cos(rad), cy - radius * Math.sin(rad));
    };

    var transFn = function(d) {
        return _transFn(t2g(d));
    };

    var transFn2 = function(d) {
        var rad = t2g(d);
        return _transFn(rad) + strRotate(-rad2deg(rad));
    };

    var gridPathFn = function(d) {
        var rad = t2g(d);
        var cosRad = Math.cos(rad);
        var sinRad = Math.sin(rad);
        return 'M' + [cx + innerRadius * cosRad, cy - innerRadius * sinRad] +
            'L' + [cx + radius * cosRad, cy - radius * sinRad];
    };

    var out = Axes.makeLabelFns(ax, 0);
    var labelStandoff = out.labelStandoff;
    var labelFns = {};

    labelFns.xFn = function(d) {
        var rad = t2g(d);
        return Math.cos(rad) * labelStandoff;
    };

    labelFns.yFn = function(d) {
        var rad = t2g(d);
        var ff = Math.sin(rad) > 0 ? 0.2 : 1;
        return -Math.sin(rad) * (labelStandoff + d.fontSize * ff) +
            Math.abs(Math.cos(rad)) * (d.fontSize * MID_SHIFT);
    };

    labelFns.anchorFn = function(d) {
        var rad = t2g(d);
        var cos = Math.cos(rad);
        return Math.abs(cos) < 0.1 ?
            'middle' :
            (cos > 0 ? 'start' : 'end');
    };

    labelFns.heightFn = function(d, a, h) {
        var rad = t2g(d);
        return -0.5 * (1 + Math.sin(rad)) * h;
    };

    var newTickLayout = strTickLayout(angularLayout);
    if(_this.angularTickLayout !== newTickLayout) {
        layers['angular-axis'].selectAll('.' + ax._id + 'tick').remove();
        _this.angularTickLayout = newTickLayout;
    }

    var vals = Axes.calcTicks(ax);

    // angle of polygon vertices in geometric radians (null means circles)
    // TODO what to do when ax.period > ax._categories ??
    var vangles;
    if(polarLayout.gridshape === 'linear') {
        vangles = vals.map(t2g);

        // ax._vals should be always ordered, make them
        // always turn counterclockwise for convenience here
        if(Lib.angleDelta(vangles[0], vangles[1]) < 0) {
            vangles = vangles.slice().reverse();
        }
    } else {
        vangles = null;
    }
    _this.vangles = vangles;

    // Use tickval filter for category axes instead of tweaking
    // the range w.r.t sector, so that sectors that cross 360 can
    // show all their ticks.
    if(ax.type === 'category') {
        vals = vals.filter(function(d) {
            return Lib.isAngleInsideSector(t2g(d), _this.sectorInRad);
        });
    }

    if(ax.visible) {
        var tickSign = ax.ticks === 'inside' ? -1 : 1;
        var pad = (ax.linewidth || 1) / 2;

        Axes.drawTicks(gd, ax, {
            vals: vals,
            layer: layers['angular-axis'],
            path: 'M' + (tickSign * pad) + ',0h' + (tickSign * ax.ticklen),
            transFn: transFn2,
            crisp: false
        });

        Axes.drawGrid(gd, ax, {
            vals: vals,
            layer: layers['angular-grid'],
            path: gridPathFn,
            transFn: Lib.noop,
            crisp: false
        });

        Axes.drawLabels(gd, ax, {
            vals: vals,
            layer: layers['angular-axis'],
            repositionOnUpdate: true,
            transFn: transFn,
            labelFns: labelFns
        });
    }

    // TODO maybe two arcs is better here?
    // maybe split style attributes between inner and outer angular axes?

    updateElement(layers['angular-line'].select('path'), angularLayout.showline, {
        d: _this.pathSubplot(),
        transform: strTranslate(cx, cy)
    })
    .attr('stroke-width', angularLayout.linewidth)
    .call(Color.stroke, angularLayout.linecolor);
};

proto.updateFx = function(fullLayout, polarLayout) {
    if(!this.gd._context.staticPlot) {
        this.updateAngularDrag(fullLayout);
        this.updateRadialDrag(fullLayout, polarLayout, 0);
        this.updateRadialDrag(fullLayout, polarLayout, 1);
        this.updateMainDrag(fullLayout);
    }
};

proto.updateMainDrag = function(fullLayout) {
    var _this = this;
    var gd = _this.gd;
    var layers = _this.layers;
    var zoomlayer = fullLayout._zoomlayer;
    var MINZOOM = constants.MINZOOM;
    var OFFEDGE = constants.OFFEDGE;
    var radius = _this.radius;
    var innerRadius = _this.innerRadius;
    var cx = _this.cx;
    var cy = _this.cy;
    var cxx = _this.cxx;
    var cyy = _this.cyy;
    var sectorInRad = _this.sectorInRad;
    var vangles = _this.vangles;
    var radialAxis = _this.radialAxis;
    var clampTiny = helpers.clampTiny;
    var findXYatLength = helpers.findXYatLength;
    var findEnclosingVertexAngles = helpers.findEnclosingVertexAngles;
    var chw = constants.cornerHalfWidth;
    var chl = constants.cornerLen / 2;

    var mainDrag = dragBox.makeDragger(layers, 'path', 'maindrag', 'crosshair');

    d3.select(mainDrag)
        .attr('d', _this.pathSubplot())
        .attr('transform', strTranslate(cx, cy));

    var dragOpts = {
        element: mainDrag,
        gd: gd,
        subplot: _this.id,
        plotinfo: {
            id: _this.id,
            xaxis: _this.xaxis,
            yaxis: _this.yaxis
        },
        xaxes: [_this.xaxis],
        yaxes: [_this.yaxis]
    };

    // mouse px position at drag start (0), move (1)
    var x0, y0;
    // radial distance from circle center at drag start (0), move (1)
    var r0, r1;
    // zoombox persistent quantities
    var path0, dimmed, lum;
    // zoombox, corners elements
    var zb, corners;

    function norm(x, y) {
        return Math.sqrt(x * x + y * y);
    }

    function xy2r(x, y) {
        return norm(x - cxx, y - cyy);
    }

    function xy2a(x, y) {
        return Math.atan2(cyy - y, x - cxx);
    }

    function ra2xy(r, a) {
        return [r * Math.cos(a), r * Math.sin(-a)];
    }

    function pathCorner(r, a) {
        if(r === 0) return _this.pathSector(2 * chw);

        var da = chl / r;
        var am = a - da;
        var ap = a + da;
        var rb = Math.max(0, Math.min(r, radius));
        var rm = rb - chw;
        var rp = rb + chw;

        return 'M' + ra2xy(rm, am) +
            'A' + [rm, rm] + ' 0,0,0 ' + ra2xy(rm, ap) +
            'L' + ra2xy(rp, ap) +
            'A' + [rp, rp] + ' 0,0,1 ' + ra2xy(rp, am) +
            'Z';
    }

    // (x,y) is the pt at middle of the va0 <-> va1 edge
    //
    // ... we could eventually add another mode for cursor
    // angles 'close to' enough to a particular vertex.
    function pathCornerForPolygons(r, va0, va1) {
        if(r === 0) return _this.pathSector(2 * chw);

        var xy0 = ra2xy(r, va0);
        var xy1 = ra2xy(r, va1);
        var x = clampTiny((xy0[0] + xy1[0]) / 2);
        var y = clampTiny((xy0[1] + xy1[1]) / 2);
        var innerPts, outerPts;

        if(x && y) {
            var m = y / x;
            var mperp = -1 / m;
            var midPts = findXYatLength(chw, m, x, y);
            innerPts = findXYatLength(chl, mperp, midPts[0][0], midPts[0][1]);
            outerPts = findXYatLength(chl, mperp, midPts[1][0], midPts[1][1]);
        } else {
            var dx, dy;
            if(y) {
                // horizontal handles
                dx = chl;
                dy = chw;
            } else {
                // vertical handles
                dx = chw;
                dy = chl;
            }
            innerPts = [[x - dx, y - dy], [x + dx, y - dy]];
            outerPts = [[x - dx, y + dy], [x + dx, y + dy]];
        }

        return 'M' + innerPts.join('L') +
            'L' + outerPts.reverse().join('L') + 'Z';
    }

    function zoomPrep() {
        r0 = null;
        r1 = null;
        path0 = _this.pathSubplot();
        dimmed = false;

        var polarLayoutNow = gd._fullLayout[_this.id];
        lum = tinycolor(polarLayoutNow.bgcolor).getLuminance();

        zb = dragBox.makeZoombox(zoomlayer, lum, cx, cy, path0);
        zb.attr('fill-rule', 'evenodd');
        corners = dragBox.makeCorners(zoomlayer, cx, cy);
        clearSelect(gd);
    }

    // N.B. this sets scoped 'r0' and 'r1'
    // return true if 'valid' zoom distance, false otherwise
    function clampAndSetR0R1(rr0, rr1) {
        rr1 = Math.max(Math.min(rr1, radius), innerRadius);

        // starting or ending drag near center (outer edge),
        // clamps radial distance at origin (at r=radius)
        if(rr0 < OFFEDGE) rr0 = 0;
        else if((radius - rr0) < OFFEDGE) rr0 = radius;
        else if(rr1 < OFFEDGE) rr1 = 0;
        else if((radius - rr1) < OFFEDGE) rr1 = radius;

        // make sure r0 < r1,
        // to get correct fill pattern in path1 below
        if(Math.abs(rr1 - rr0) > MINZOOM) {
            if(rr0 < rr1) {
                r0 = rr0;
                r1 = rr1;
            } else {
                r0 = rr1;
                r1 = rr0;
            }
            return true;
        } else {
            r0 = null;
            r1 = null;
            return false;
        }
    }

    function applyZoomMove(path1, cpath) {
        path1 = path1 || path0;
        cpath = cpath || 'M0,0Z';

        zb.attr('d', path1);
        corners.attr('d', cpath);
        dragBox.transitionZoombox(zb, corners, dimmed, lum);
        dimmed = true;

        var updateObj = {};
        computeZoomUpdates(updateObj);
        gd.emit('plotly_relayouting', updateObj);
    }

    function zoomMove(dx, dy) {
        var x1 = x0 + dx;
        var y1 = y0 + dy;
        var rr0 = xy2r(x0, y0);
        var rr1 = Math.min(xy2r(x1, y1), radius);
        var a0 = xy2a(x0, y0);
        var path1;
        var cpath;

        if(clampAndSetR0R1(rr0, rr1)) {
            path1 = path0 + _this.pathSector(r1);
            if(r0) path1 += _this.pathSector(r0);
            // keep 'starting' angle
            cpath = pathCorner(r0, a0) + pathCorner(r1, a0);
        }
        applyZoomMove(path1, cpath);
    }

    function findPolygonRadius(x, y, va0, va1) {
        var xy = helpers.findIntersectionXY(va0, va1, va0, [x - cxx, cyy - y]);
        return norm(xy[0], xy[1]);
    }

    function zoomMoveForPolygons(dx, dy) {
        var x1 = x0 + dx;
        var y1 = y0 + dy;
        var a0 = xy2a(x0, y0);
        var a1 = xy2a(x1, y1);
        var vangles0 = findEnclosingVertexAngles(a0, vangles);
        var vangles1 = findEnclosingVertexAngles(a1, vangles);
        var rr0 = findPolygonRadius(x0, y0, vangles0[0], vangles0[1]);
        var rr1 = Math.min(findPolygonRadius(x1, y1, vangles1[0], vangles1[1]), radius);
        var path1;
        var cpath;

        if(clampAndSetR0R1(rr0, rr1)) {
            path1 = path0 + _this.pathSector(r1);
            if(r0) path1 += _this.pathSector(r0);
            // keep 'starting' angle here too
            cpath = [
                pathCornerForPolygons(r0, vangles0[0], vangles0[1]),
                pathCornerForPolygons(r1, vangles0[0], vangles0[1])
            ].join(' ');
        }
        applyZoomMove(path1, cpath);
    }

    function zoomDone() {
        dragBox.removeZoombox(gd);

        if(r0 === null || r1 === null) return;
        var updateObj = {};
        computeZoomUpdates(updateObj);

        dragBox.showDoubleClickNotifier(gd);

        Registry.call('_guiRelayout', gd, updateObj);
    }

    function computeZoomUpdates(update) {
        var rl = radialAxis._rl;
        var m = (rl[1] - rl[0]) / (1 - innerRadius / radius) / radius;
        var newRng = [
            rl[0] + (r0 - innerRadius) * m,
            rl[0] + (r1 - innerRadius) * m
        ];
        update[_this.id + '.radialaxis.range'] = newRng;
    }

    function zoomClick(numClicks, evt) {
        var clickMode = gd._fullLayout.clickmode;

        dragBox.removeZoombox(gd);

        // TODO double once vs twice logic (autorange vs fixed range)
        if(numClicks === 2) {
            var updateObj = {};
            for(var k in _this.viewInitial) {
                updateObj[_this.id + '.' + k] = _this.viewInitial[k];
            }

            gd.emit('plotly_doubleclick', null);
            Registry.call('_guiRelayout', gd, updateObj);
        }

        if(clickMode.indexOf('select') > -1 && numClicks === 1) {
            selectOnClick(evt, gd, [_this.xaxis], [_this.yaxis], _this.id, dragOpts);
        }

        if(clickMode.indexOf('event') > -1) {
            Fx.click(gd, evt, _this.id);
        }
    }

    dragOpts.prepFn = function(evt, startX, startY) {
        var dragModeNow = gd._fullLayout.dragmode;

        var bbox = mainDrag.getBoundingClientRect();
        x0 = startX - bbox.left;
        y0 = startY - bbox.top;

        // need to offset x/y as bbox center does not
        // match origin for asymmetric polygons
        if(vangles) {
            var offset = helpers.findPolygonOffset(radius, sectorInRad[0], sectorInRad[1], vangles);
            x0 += cxx + offset[0];
            y0 += cyy + offset[1];
        }

        switch(dragModeNow) {
            case 'zoom':
                if(vangles) {
                    dragOpts.moveFn = zoomMoveForPolygons;
                } else {
                    dragOpts.moveFn = zoomMove;
                }
                dragOpts.clickFn = zoomClick;
                dragOpts.doneFn = zoomDone;
                zoomPrep(evt, startX, startY);
                break;
            case 'select':
            case 'lasso':
                prepSelect(evt, startX, startY, dragOpts, dragModeNow);
                break;
        }
    };

    mainDrag.onmousemove = function(evt) {
        Fx.hover(gd, evt, _this.id);
        gd._fullLayout._lasthover = mainDrag;
        gd._fullLayout._hoversubplot = _this.id;
    };

    mainDrag.onmouseout = function(evt) {
        if(gd._dragging) return;
        dragElement.unhover(gd, evt);
    };

    dragElement.init(dragOpts);
};

proto.updateRadialDrag = function(fullLayout, polarLayout, rngIndex) {
    var _this = this;
    var gd = _this.gd;
    var layers = _this.layers;
    var radius = _this.radius;
    var innerRadius = _this.innerRadius;
    var cx = _this.cx;
    var cy = _this.cy;
    var radialAxis = _this.radialAxis;
    var bl = constants.radialDragBoxSize;
    var bl2 = bl / 2;

    if(!radialAxis.visible) return;

    var angle0 = deg2rad(_this.radialAxisAngle);
    var rl = radialAxis._rl;
    var rl0 = rl[0];
    var rl1 = rl[1];
    var rbase = rl[rngIndex];
    var m = 0.75 * (rl[1] - rl[0]) / (1 - polarLayout.hole) / radius;

    var tx, ty, className;
    if(rngIndex) {
        tx = cx + (radius + bl2) * Math.cos(angle0);
        ty = cy - (radius + bl2) * Math.sin(angle0);
        className = 'radialdrag';
    } else {
        // the 'inner' box can get called:
        // - when polar.hole>0
        // - when polar.sector isn't a full circle
        // otherwise it is hidden behind the main drag.
        tx = cx + (innerRadius - bl2) * Math.cos(angle0);
        ty = cy - (innerRadius - bl2) * Math.sin(angle0);
        className = 'radialdrag-inner';
    }

    var radialDrag = dragBox.makeRectDragger(layers, className, 'crosshair', -bl2, -bl2, bl, bl);
    var dragOpts = {element: radialDrag, gd: gd};

    updateElement(d3.select(radialDrag), radialAxis.visible && innerRadius < radius, {
        transform: strTranslate(tx, ty)
    });

    // move function (either rotate or re-range flavor)
    var moveFn2;
    // rotate angle on done
    var angle1;
    // re-range range[1] (or range[0]) on done
    var rprime;

    function moveFn(dx, dy) {
        if(moveFn2) {
            moveFn2(dx, dy);
        } else {
            var dvec = [dx, -dy];
            var rvec = [Math.cos(angle0), Math.sin(angle0)];
            var comp = Math.abs(Lib.dot(dvec, rvec) / Math.sqrt(Lib.dot(dvec, dvec)));

            // mostly perpendicular motions rotate,
            // mostly parallel motions re-range
            if(!isNaN(comp)) {
                moveFn2 = comp < 0.5 ? rotateMove : rerangeMove;
            }
        }

        var update = {};
        computeRadialAxisUpdates(update);
        gd.emit('plotly_relayouting', update);
    }

    function computeRadialAxisUpdates(update) {
        if(angle1 !== null) {
            update[_this.id + '.radialaxis.angle'] = angle1;
        } else if(rprime !== null) {
            update[_this.id + '.radialaxis.range[' + rngIndex + ']'] = rprime;
        }
    }

    function doneFn() {
        if(angle1 !== null) {
            Registry.call('_guiRelayout', gd, _this.id + '.radialaxis.angle', angle1);
        } else if(rprime !== null) {
            Registry.call('_guiRelayout', gd, _this.id + '.radialaxis.range[' + rngIndex + ']', rprime);
        }
    }

    function rotateMove(dx, dy) {
        // disable for inner drag boxes
        if(rngIndex === 0) return;

        var x1 = tx + dx;
        var y1 = ty + dy;

        angle1 = Math.atan2(cy - y1, x1 - cx);
        if(_this.vangles) angle1 = snapToVertexAngle(angle1, _this.vangles);
        angle1 = rad2deg(angle1);

        var transform = strTranslate(cx, cy) + strRotate(-angle1);
        layers['radial-axis'].attr('transform', transform);
        layers['radial-line'].select('line').attr('transform', transform);

        var fullLayoutNow = _this.gd._fullLayout;
        var polarLayoutNow = fullLayoutNow[_this.id];
        _this.updateRadialAxisTitle(fullLayoutNow, polarLayoutNow, angle1);
    }

    function rerangeMove(dx, dy) {
        // project (dx, dy) unto unit radial axis vector
        var dr = Lib.dot([dx, -dy], [Math.cos(angle0), Math.sin(angle0)]);
        rprime = rbase - m * dr;

        // make sure rprime does not change the range[0] -> range[1] sign
        if((m > 0) !== (rngIndex ? rprime > rl0 : rprime < rl1)) {
            rprime = null;
            return;
        }

        var fullLayoutNow = gd._fullLayout;
        var polarLayoutNow = fullLayoutNow[_this.id];

        // update radial range -> update c2g -> update _m,_b
        radialAxis.range[rngIndex] = rprime;
        radialAxis._rl[rngIndex] = rprime;
        _this.updateRadialAxis(fullLayoutNow, polarLayoutNow);

        _this.xaxis.setRange();
        _this.xaxis.setScale();
        _this.yaxis.setRange();
        _this.yaxis.setScale();

        var hasRegl = false;

        for(var traceType in _this.traceHash) {
            var moduleCalcData = _this.traceHash[traceType];
            var moduleCalcDataVisible = Lib.filterVisible(moduleCalcData);
            var _module = moduleCalcData[0][0].trace._module;
            _module.plot(gd, _this, moduleCalcDataVisible, polarLayoutNow);
            if(Registry.traceIs(traceType, 'gl') && moduleCalcDataVisible.length) hasRegl = true;
        }

        if(hasRegl) {
            clearGlCanvases(gd);
            redrawReglTraces(gd);
        }
    }

    dragOpts.prepFn = function() {
        moveFn2 = null;
        angle1 = null;
        rprime = null;

        dragOpts.moveFn = moveFn;
        dragOpts.doneFn = doneFn;

        clearSelect(gd);
    };

    dragOpts.clampFn = function(dx, dy) {
        if(Math.sqrt(dx * dx + dy * dy) < constants.MINDRAG) {
            dx = 0;
            dy = 0;
        }
        return [dx, dy];
    };

    dragElement.init(dragOpts);
};

proto.updateAngularDrag = function(fullLayout) {
    var _this = this;
    var gd = _this.gd;
    var layers = _this.layers;
    var radius = _this.radius;
    var angularAxis = _this.angularAxis;
    var cx = _this.cx;
    var cy = _this.cy;
    var cxx = _this.cxx;
    var cyy = _this.cyy;
    var dbs = constants.angularDragBoxSize;

    var angularDrag = dragBox.makeDragger(layers, 'path', 'angulardrag', 'move');
    var dragOpts = {element: angularDrag, gd: gd};

    d3.select(angularDrag)
        .attr('d', _this.pathAnnulus(radius, radius + dbs))
        .attr('transform', strTranslate(cx, cy))
        .call(setCursor, 'move');

    function xy2a(x, y) {
        return Math.atan2(cyy + dbs - y, x - cxx - dbs);
    }

    // scatter trace, points and textpoints selections
    var scatterTraces = layers.frontplot.select('.scatterlayer').selectAll('.trace');
    var scatterPoints = scatterTraces.selectAll('.point');
    var scatterTextPoints = scatterTraces.selectAll('.textpoint');

    // mouse px position at drag start (0), move (1)
    var x0, y0;
    // angular axis angle rotation at drag start (0), move (1)
    var rot0, rot1;
    // induced radial axis rotation (only used on polygon grids)
    var rrot1;
    // angle about circle center at drag start
    var a0;

    function moveFn(dx, dy) {
        var fullLayoutNow = _this.gd._fullLayout;
        var polarLayoutNow = fullLayoutNow[_this.id];

        var x1 = x0 + dx;
        var y1 = y0 + dy;
        var a1 = xy2a(x1, y1);
        var da = rad2deg(a1 - a0);
        rot1 = rot0 + da;

        layers.frontplot.attr('transform',
            strTranslate(_this.xOffset2, _this.yOffset2) + strRotate([-da, cxx, cyy])
        );

        if(_this.vangles) {
            rrot1 = _this.radialAxisAngle + da;

            var trans = strTranslate(cx, cy) + strRotate(-da);
            var trans2 = strTranslate(cx, cy) + strRotate(-rrot1);

            layers.bg.attr('transform', trans);
            layers['radial-grid'].attr('transform', trans);
            layers['radial-axis'].attr('transform', trans2);
            layers['radial-line'].select('line').attr('transform', trans2);
            _this.updateRadialAxisTitle(fullLayoutNow, polarLayoutNow, rrot1);
        } else {
            _this.clipPaths.forTraces.select('path').attr('transform',
                strTranslate(cxx, cyy) + strRotate(da)
            );
        }

        // 'un-rotate' marker and text points
        scatterPoints.each(function() {
            var sel = d3.select(this);
            var xy = Drawing.getTranslate(sel);
            sel.attr('transform', strTranslate(xy.x, xy.y) + strRotate([da]));
        });
        scatterTextPoints.each(function() {
            var sel = d3.select(this);
            var tx = sel.select('text');
            var xy = Drawing.getTranslate(sel);
            // N.B rotate -> translate ordering matters
            sel.attr('transform', strRotate([da, tx.attr('x'), tx.attr('y')]) + strTranslate(xy.x, xy.y));
        });

        // update rotation -> range -> _m,_b
        angularAxis.rotation = Lib.modHalf(rot1, 360);
        _this.updateAngularAxis(fullLayoutNow, polarLayoutNow);

        if(_this._hasClipOnAxisFalse && !Lib.isFullCircle(_this.sectorInRad)) {
            scatterTraces.call(Drawing.hideOutsideRangePoints, _this);
        }

        var hasRegl = false;

        for(var traceType in _this.traceHash) {
            if(Registry.traceIs(traceType, 'gl')) {
                var moduleCalcData = _this.traceHash[traceType];
                var moduleCalcDataVisible = Lib.filterVisible(moduleCalcData);
                var _module = moduleCalcData[0][0].trace._module;
                _module.plot(gd, _this, moduleCalcDataVisible, polarLayoutNow);
                if(moduleCalcDataVisible.length) hasRegl = true;
            }
        }

        if(hasRegl) {
            clearGlCanvases(gd);
            redrawReglTraces(gd);
        }

        var update = {};
        computeRotationUpdates(update);
        gd.emit('plotly_relayouting', update);
    }

    function computeRotationUpdates(updateObj) {
        updateObj[_this.id + '.angularaxis.rotation'] = rot1;

        if(_this.vangles) {
            updateObj[_this.id + '.radialaxis.angle'] = rrot1;
        }
    }

    function doneFn() {
        scatterTextPoints.select('text').attr('transform', null);

        var updateObj = {};
        computeRotationUpdates(updateObj);
        Registry.call('_guiRelayout', gd, updateObj);
    }

    dragOpts.prepFn = function(evt, startX, startY) {
        var polarLayoutNow = fullLayout[_this.id];
        rot0 = polarLayoutNow.angularaxis.rotation;

        var bbox = angularDrag.getBoundingClientRect();
        x0 = startX - bbox.left;
        y0 = startY - bbox.top;
        a0 = xy2a(x0, y0);

        dragOpts.moveFn = moveFn;
        dragOpts.doneFn = doneFn;

        clearSelect(gd);
    };

    // I don't what we should do in this case, skip we now
    if(_this.vangles && !Lib.isFullCircle(_this.sectorInRad)) {
        dragOpts.prepFn = Lib.noop;
        setCursor(d3.select(angularDrag), null);
    }

    dragElement.init(dragOpts);
};

proto.isPtInside = function(d) {
    var sectorInRad = this.sectorInRad;
    var vangles = this.vangles;
    var thetag = this.angularAxis.c2g(d.theta);
    var radialAxis = this.radialAxis;
    var r = radialAxis.c2l(d.r);
    var rl = radialAxis._rl;

    var fn = vangles ? helpers.isPtInsidePolygon : Lib.isPtInsideSector;
    return fn(r, thetag, rl, sectorInRad, vangles);
};

proto.pathArc = function(r) {
    var sectorInRad = this.sectorInRad;
    var vangles = this.vangles;
    var fn = vangles ? helpers.pathPolygon : Lib.pathArc;
    return fn(r, sectorInRad[0], sectorInRad[1], vangles);
};

proto.pathSector = function(r) {
    var sectorInRad = this.sectorInRad;
    var vangles = this.vangles;
    var fn = vangles ? helpers.pathPolygon : Lib.pathSector;
    return fn(r, sectorInRad[0], sectorInRad[1], vangles);
};

proto.pathAnnulus = function(r0, r1) {
    var sectorInRad = this.sectorInRad;
    var vangles = this.vangles;
    var fn = vangles ? helpers.pathPolygonAnnulus : Lib.pathAnnulus;
    return fn(r0, r1, sectorInRad[0], sectorInRad[1], vangles);
};

proto.pathSubplot = function() {
    var r0 = this.innerRadius;
    var r1 = this.radius;
    return r0 ? this.pathAnnulus(r0, r1) : this.pathSector(r1);
};

proto.fillViewInitialKey = function(key, val) {
    if(!(key in this.viewInitial)) {
        this.viewInitial[key] = val;
    }
};

function strTickLayout(axLayout) {
    var out = axLayout.ticks + String(axLayout.ticklen) + String(axLayout.showticklabels);
    if('side' in axLayout) out += axLayout.side;
    return out;
}

// Finds the bounding box of a given circle sector,
// inspired by https://math.stackexchange.com/q/1852703
//
// assumes:
// - sector[0] < sector[1]
// - counterclockwise rotation
function computeSectorBBox(sector) {
    var s0 = sector[0];
    var s1 = sector[1];
    var arc = s1 - s0;
    var a0 = mod(s0, 360);
    var a1 = a0 + arc;

    var ax0 = Math.cos(deg2rad(a0));
    var ay0 = Math.sin(deg2rad(a0));
    var ax1 = Math.cos(deg2rad(a1));
    var ay1 = Math.sin(deg2rad(a1));

    var x0, y0, x1, y1;

    if((a0 <= 90 && a1 >= 90) || (a0 > 90 && a1 >= 450)) {
        y1 = 1;
    } else if(ay0 <= 0 && ay1 <= 0) {
        y1 = 0;
    } else {
        y1 = Math.max(ay0, ay1);
    }

    if((a0 <= 180 && a1 >= 180) || (a0 > 180 && a1 >= 540)) {
        x0 = -1;
    } else if(ax0 >= 0 && ax1 >= 0) {
        x0 = 0;
    } else {
        x0 = Math.min(ax0, ax1);
    }

    if((a0 <= 270 && a1 >= 270) || (a0 > 270 && a1 >= 630)) {
        y0 = -1;
    } else if(ay0 >= 0 && ay1 >= 0) {
        y0 = 0;
    } else {
        y0 = Math.min(ay0, ay1);
    }

    if(a1 >= 360) {
        x1 = 1;
    } else if(ax0 <= 0 && ax1 <= 0) {
        x1 = 0;
    } else {
        x1 = Math.max(ax0, ax1);
    }

    return [x0, y0, x1, y1];
}

function snapToVertexAngle(a, vangles) {
    var fn = function(v) { return Lib.angleDist(a, v); };
    var ind = Lib.findIndexOfMin(vangles, fn);
    return vangles[ind];
}

function updateElement(sel, showAttr, attrs) {
    if(showAttr) {
        sel.attr('display', null);
        sel.attr(attrs);
    } else if(sel) {
        sel.attr('display', 'none');
    }
    return sel;
}

function strTranslate(x, y) {
    return 'translate(' + x + ',' + y + ')';
}

function strRotate(angle) {
    return 'rotate(' + angle + ')';
}
