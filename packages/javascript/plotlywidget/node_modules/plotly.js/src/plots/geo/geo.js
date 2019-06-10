/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/* global PlotlyGeoAssets:false */

var d3 = require('d3');

var Registry = require('../../registry');
var Lib = require('../../lib');
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');
var Fx = require('../../components/fx');
var Plots = require('../plots');
var Axes = require('../cartesian/axes');
var dragElement = require('../../components/dragelement');
var prepSelect = require('../cartesian/select').prepSelect;
var selectOnClick = require('../cartesian/select').selectOnClick;

var createGeoZoom = require('./zoom');
var constants = require('./constants');

var topojsonUtils = require('../../lib/topojson_utils');
var topojsonFeature = require('topojson-client').feature;

require('./projections')(d3);

function Geo(opts) {
    this.id = opts.id;
    this.graphDiv = opts.graphDiv;
    this.container = opts.container;
    this.topojsonURL = opts.topojsonURL;
    this.isStatic = opts.staticPlot;

    this.topojsonName = null;
    this.topojson = null;

    this.projection = null;
    this.scope = null;
    this.viewInitial = null;
    this.fitScale = null;
    this.bounds = null;
    this.midPt = null;

    this.hasChoropleth = false;
    this.traceHash = {};

    this.layers = {};
    this.basePaths = {};
    this.dataPaths = {};
    this.dataPoints = {};

    this.clipDef = null;
    this.clipRect = null;
    this.bgRect = null;

    this.makeFramework();
}

var proto = Geo.prototype;

module.exports = function createGeo(opts) {
    return new Geo(opts);
};

proto.plot = function(geoCalcData, fullLayout, promises) {
    var _this = this;
    var geoLayout = fullLayout[this.id];

    var needsTopojson = false;
    for(var k in constants.layerNameToAdjective) {
        if(k !== 'frame' && geoLayout['show' + k]) {
            needsTopojson = true;
            break;
        }
    }
    if(!needsTopojson) {
        return _this.update(geoCalcData, fullLayout);
    }

    var topojsonNameNew = topojsonUtils.getTopojsonName(geoLayout);

    if(_this.topojson === null || topojsonNameNew !== _this.topojsonName) {
        _this.topojsonName = topojsonNameNew;

        if(PlotlyGeoAssets.topojson[_this.topojsonName] === undefined) {
            promises.push(_this.fetchTopojson().then(function(topojson) {
                PlotlyGeoAssets.topojson[_this.topojsonName] = topojson;
                _this.topojson = topojson;
                _this.update(geoCalcData, fullLayout);
            }));
        } else {
            _this.topojson = PlotlyGeoAssets.topojson[_this.topojsonName];
            _this.update(geoCalcData, fullLayout);
        }
    } else {
        _this.update(geoCalcData, fullLayout);
    }
};

proto.fetchTopojson = function() {
    var topojsonPath = topojsonUtils.getTopojsonPath(
        this.topojsonURL,
        this.topojsonName
    );
    return new Promise(function(resolve, reject) {
        d3.json(topojsonPath, function(err, topojson) {
            if(err) {
                if(err.status === 404) {
                    return reject(new Error([
                        'plotly.js could not find topojson file at',
                        topojsonPath, '.',
                        'Make sure the *topojsonURL* plot config option',
                        'is set properly.'
                    ].join(' ')));
                } else {
                    return reject(new Error([
                        'unexpected error while fetching topojson file at',
                        topojsonPath
                    ].join(' ')));
                }
            }
            resolve(topojson);
        });
    });
};

proto.update = function(geoCalcData, fullLayout) {
    var geoLayout = fullLayout[this.id];

    var hasInvalidBounds = this.updateProjection(fullLayout, geoLayout);
    if(hasInvalidBounds) return;

    // important: maps with choropleth traces have a different layer order
    this.hasChoropleth = false;
    for(var i = 0; i < geoCalcData.length; i++) {
        if(geoCalcData[i][0].trace.type === 'choropleth') {
            this.hasChoropleth = true;
            break;
        }
    }

    if(!this.viewInitial || this.scope !== geoLayout.scope) {
        this.saveViewInitial(geoLayout);
    }
    this.scope = geoLayout.scope;

    this.updateBaseLayers(fullLayout, geoLayout);
    this.updateDims(fullLayout, geoLayout);
    this.updateFx(fullLayout, geoLayout);

    Plots.generalUpdatePerTraceModule(this.graphDiv, this, geoCalcData, geoLayout);

    var scatterLayer = this.layers.frontplot.select('.scatterlayer');
    this.dataPoints.point = scatterLayer.selectAll('.point');
    this.dataPoints.text = scatterLayer.selectAll('text');
    this.dataPaths.line = scatterLayer.selectAll('.js-line');

    var choroplethLayer = this.layers.backplot.select('.choroplethlayer');
    this.dataPaths.choropleth = choroplethLayer.selectAll('path');

    this.render();
};

proto.updateProjection = function(fullLayout, geoLayout) {
    var gs = fullLayout._size;
    var domain = geoLayout.domain;
    var projLayout = geoLayout.projection;
    var rotation = projLayout.rotation || {};
    var center = geoLayout.center || {};

    var projection = this.projection = getProjection(geoLayout);

    // set 'pre-fit' projection
    projection
        .center([center.lon - rotation.lon, center.lat - rotation.lat])
        .rotate([-rotation.lon, -rotation.lat, rotation.roll])
        .parallels(projLayout.parallels);

    // setup subplot extent [[x0,y0], [x1,y1]]
    var extent = [[
        gs.l + gs.w * domain.x[0],
        gs.t + gs.h * (1 - domain.y[1])
    ], [
        gs.l + gs.w * domain.x[1],
        gs.t + gs.h * (1 - domain.y[0])
    ]];

    var lonaxis = geoLayout.lonaxis;
    var lataxis = geoLayout.lataxis;
    var rangeBox = makeRangeBox(lonaxis.range, lataxis.range);

    // fit projection 'scale' and 'translate' to set lon/lat ranges
    projection.fitExtent(extent, rangeBox);

    var b = this.bounds = projection.getBounds(rangeBox);
    var s = this.fitScale = projection.scale();
    var t = projection.translate();

    if(
        !isFinite(b[0][0]) || !isFinite(b[0][1]) ||
        !isFinite(b[1][0]) || !isFinite(b[1][1]) ||
        isNaN(t[0]) || isNaN(t[0])
    ) {
        var gd = this.graphDiv;
        var attrToUnset = ['projection.rotation', 'center', 'lonaxis.range', 'lataxis.range'];
        var msg = 'Invalid geo settings, relayout\'ing to default view.';
        var updateObj = {};

        // clear all attribute that could cause invalid bounds,
        // clear viewInitial to update reset-view behavior

        for(var i = 0; i < attrToUnset.length; i++) {
            updateObj[this.id + '.' + attrToUnset[i]] = null;
        }

        this.viewInitial = null;

        Lib.warn(msg);
        gd._promises.push(Registry.call('relayout', gd, updateObj));
        return msg;
    }

    // px coordinates of view mid-point,
    // useful to update `geo.center` after interactions
    var midPt = this.midPt = [
        (b[0][0] + b[1][0]) / 2,
        (b[0][1] + b[1][1]) / 2
    ];

    // adjust projection to user setting
    projection
        .scale(projLayout.scale * s)
        .translate([t[0] + (midPt[0] - t[0]), t[1] + (midPt[1] - t[1])])
        .clipExtent(b);

    // the 'albers usa' projection does not expose a 'center' method
    // so here's this hack to make it respond to 'geoLayout.center'
    if(geoLayout._isAlbersUsa) {
        var centerPx = projection([center.lon, center.lat]);
        var tt = projection.translate();

        projection.translate([
            tt[0] - (centerPx[0] - tt[0]),
            tt[1] - (centerPx[1] - tt[1])
        ]);
    }
};

proto.updateBaseLayers = function(fullLayout, geoLayout) {
    var _this = this;
    var topojson = _this.topojson;
    var layers = _this.layers;
    var basePaths = _this.basePaths;

    function isAxisLayer(d) {
        return (d === 'lonaxis' || d === 'lataxis');
    }

    function isLineLayer(d) {
        return Boolean(constants.lineLayers[d]);
    }

    function isFillLayer(d) {
        return Boolean(constants.fillLayers[d]);
    }

    var allLayers = this.hasChoropleth ?
        constants.layersForChoropleth :
        constants.layers;

    var layerData = allLayers.filter(function(d) {
        return (isLineLayer(d) || isFillLayer(d)) ? geoLayout['show' + d] :
            isAxisLayer(d) ? geoLayout[d].showgrid :
            true;
    });

    var join = _this.framework.selectAll('.layer')
        .data(layerData, String);

    join.exit().each(function(d) {
        delete layers[d];
        delete basePaths[d];
        d3.select(this).remove();
    });

    join.enter().append('g')
        .attr('class', function(d) { return 'layer ' + d; })
        .each(function(d) {
            var layer = layers[d] = d3.select(this);

            if(d === 'bg') {
                _this.bgRect = layer.append('rect')
                    .style('pointer-events', 'all');
            } else if(isAxisLayer(d)) {
                basePaths[d] = layer.append('path')
                    .style('fill', 'none');
            } else if(d === 'backplot') {
                layer.append('g')
                    .classed('choroplethlayer', true);
            } else if(d === 'frontplot') {
                layer.append('g')
                    .classed('scatterlayer', true);
            } else if(isLineLayer(d)) {
                basePaths[d] = layer.append('path')
                    .style('fill', 'none')
                    .style('stroke-miterlimit', 2);
            } else if(isFillLayer(d)) {
                basePaths[d] = layer.append('path')
                    .style('stroke', 'none');
            }
        });

    join.order();

    join.each(function(d) {
        var path = basePaths[d];
        var adj = constants.layerNameToAdjective[d];

        if(d === 'frame') {
            path.datum(constants.sphereSVG);
        } else if(isLineLayer(d) || isFillLayer(d)) {
            path.datum(topojsonFeature(topojson, topojson.objects[d]));
        } else if(isAxisLayer(d)) {
            path.datum(makeGraticule(d, geoLayout, fullLayout))
                .call(Color.stroke, geoLayout[d].gridcolor)
                .call(Drawing.dashLine, '', geoLayout[d].gridwidth);
        }

        if(isLineLayer(d)) {
            path.call(Color.stroke, geoLayout[adj + 'color'])
                .call(Drawing.dashLine, '', geoLayout[adj + 'width']);
        } else if(isFillLayer(d)) {
            path.call(Color.fill, geoLayout[adj + 'color']);
        }
    });
};

proto.updateDims = function(fullLayout, geoLayout) {
    var b = this.bounds;
    var hFrameWidth = (geoLayout.framewidth || 0) / 2;

    var l = b[0][0] - hFrameWidth;
    var t = b[0][1] - hFrameWidth;
    var w = b[1][0] - l + hFrameWidth;
    var h = b[1][1] - t + hFrameWidth;

    Drawing.setRect(this.clipRect, l, t, w, h);

    this.bgRect
        .call(Drawing.setRect, l, t, w, h)
        .call(Color.fill, geoLayout.bgcolor);

    this.xaxis._offset = l;
    this.xaxis._length = w;

    this.yaxis._offset = t;
    this.yaxis._length = h;
};

proto.updateFx = function(fullLayout, geoLayout) {
    var _this = this;
    var gd = _this.graphDiv;
    var bgRect = _this.bgRect;
    var dragMode = fullLayout.dragmode;
    var clickMode = fullLayout.clickmode;

    if(_this.isStatic) return;

    function zoomReset() {
        var viewInitial = _this.viewInitial;
        var updateObj = {};

        for(var k in viewInitial) {
            updateObj[_this.id + '.' + k] = viewInitial[k];
        }

        Registry.call('_guiRelayout', gd, updateObj);
        gd.emit('plotly_doubleclick', null);
    }

    function invert(lonlat) {
        return _this.projection.invert([
            lonlat[0] + _this.xaxis._offset,
            lonlat[1] + _this.yaxis._offset
        ]);
    }

    var fillRangeItems;

    if(dragMode === 'select') {
        fillRangeItems = function(eventData, poly) {
            var ranges = eventData.range = {};
            ranges[_this.id] = [
                invert([poly.xmin, poly.ymin]),
                invert([poly.xmax, poly.ymax])
            ];
        };
    } else if(dragMode === 'lasso') {
        fillRangeItems = function(eventData, poly, pts) {
            var dataPts = eventData.lassoPoints = {};
            dataPts[_this.id] = pts.filtered.map(invert);
        };
    }

    // Note: dragOptions is needed to be declared for all dragmodes because
    // it's the object that holds persistent selection state.
    var dragOptions = {
        element: _this.bgRect.node(),
        gd: gd,
        plotinfo: {
            id: _this.id,
            xaxis: _this.xaxis,
            yaxis: _this.yaxis,
            fillRangeItems: fillRangeItems
        },
        xaxes: [_this.xaxis],
        yaxes: [_this.yaxis],
        subplot: _this.id,
        clickFn: function(numClicks) {
            if(numClicks === 2) {
                fullLayout._zoomlayer.selectAll('.select-outline').remove();
            }
        }
    };

    if(dragMode === 'pan') {
        bgRect.node().onmousedown = null;
        bgRect.call(createGeoZoom(_this, geoLayout));
        bgRect.on('dblclick.zoom', zoomReset);
        if(!gd._context._scrollZoom.geo) {
            bgRect.on('wheel.zoom', null);
        }
    } else if(dragMode === 'select' || dragMode === 'lasso') {
        bgRect.on('.zoom', null);

        dragOptions.prepFn = function(e, startX, startY) {
            prepSelect(e, startX, startY, dragOptions, dragMode);
        };

        dragElement.init(dragOptions);
    }

    bgRect.on('mousemove', function() {
        var lonlat = _this.projection.invert(d3.mouse(this));

        if(!lonlat || isNaN(lonlat[0]) || isNaN(lonlat[1])) {
            return dragElement.unhover(gd, d3.event);
        }

        _this.xaxis.p2c = function() { return lonlat[0]; };
        _this.yaxis.p2c = function() { return lonlat[1]; };

        Fx.hover(gd, d3.event, _this.id);
    });

    bgRect.on('mouseout', function() {
        if(gd._dragging) return;
        dragElement.unhover(gd, d3.event);
    });

    bgRect.on('click', function() {
        // For select and lasso the dragElement is handling clicks
        if(dragMode !== 'select' && dragMode !== 'lasso') {
            if(clickMode.indexOf('select') > -1) {
                selectOnClick(d3.event, gd, [_this.xaxis], [_this.yaxis],
                  _this.id, dragOptions);
            }

            if(clickMode.indexOf('event') > -1) {
                // TODO: like pie and mapbox, this doesn't support right-click
                // actually this one is worse, as right-click starts a pan, or leaves
                // select in a weird state.
                // Also, only tangentially related, we should cancel hover during pan
                Fx.click(gd, d3.event);
            }
        }
    });
};

proto.makeFramework = function() {
    var _this = this;
    var gd = _this.graphDiv;
    var fullLayout = gd._fullLayout;
    var clipId = 'clip' + fullLayout._uid + _this.id;

    _this.clipDef = fullLayout._clips.append('clipPath')
        .attr('id', clipId);

    _this.clipRect = _this.clipDef.append('rect');

    _this.framework = d3.select(_this.container).append('g')
        .attr('class', 'geo ' + _this.id)
        .call(Drawing.setClipUrl, clipId, gd);

    // sane lonlat to px
    _this.project = function(v) {
        var px = _this.projection(v);
        return px ?
            [px[0] - _this.xaxis._offset, px[1] - _this.yaxis._offset] :
            [null, null];
    };

    _this.xaxis = {
        _id: 'x',
        c2p: function(v) { return _this.project(v)[0]; }
    };

    _this.yaxis = {
        _id: 'y',
        c2p: function(v) { return _this.project(v)[1]; }
    };

    // mock axis for hover formatting
    _this.mockAxis = {
        type: 'linear',
        showexponent: 'all',
        exponentformat: 'B'
    };
    Axes.setConvert(_this.mockAxis, fullLayout);
};

proto.saveViewInitial = function(geoLayout) {
    var center = geoLayout.center || {};
    var projLayout = geoLayout.projection;
    var rotation = projLayout.rotation || {};

    if(geoLayout._isScoped) {
        this.viewInitial = {
            'center.lon': center.lon,
            'center.lat': center.lat,
            'projection.scale': projLayout.scale
        };
    } else if(geoLayout._isClipped) {
        this.viewInitial = {
            'projection.scale': projLayout.scale,
            'projection.rotation.lon': rotation.lon,
            'projection.rotation.lat': rotation.lat
        };
    } else {
        this.viewInitial = {
            'center.lon': center.lon,
            'center.lat': center.lat,
            'projection.scale': projLayout.scale,
            'projection.rotation.lon': rotation.lon
        };
    }
};

// [hot code path] (re)draw all paths which depend on the projection
proto.render = function() {
    var projection = this.projection;
    var pathFn = projection.getPath();
    var k;

    function translatePoints(d) {
        var lonlatPx = projection(d.lonlat);
        return lonlatPx ?
            'translate(' + lonlatPx[0] + ',' + lonlatPx[1] + ')' :
             null;
    }

    function hideShowPoints(d) {
        return projection.isLonLatOverEdges(d.lonlat) ? 'none' : null;
    }

    for(k in this.basePaths) {
        this.basePaths[k].attr('d', pathFn);
    }

    for(k in this.dataPaths) {
        this.dataPaths[k].attr('d', function(d) { return pathFn(d.geojson); });
    }

    for(k in this.dataPoints) {
        this.dataPoints[k]
            .attr('display', hideShowPoints)
            .attr('transform', translatePoints);
    }
};

// Helper that wraps d3.geo[/* projection name /*]() which:
//
// - adds 'fitExtent' (available in d3 v4)
// - adds 'getPath', 'getBounds' convenience methods
// - scopes logic related to 'clipAngle'
// - adds 'isLonLatOverEdges' method
// - sets projection precision
// - sets methods that aren't always defined depending
//   on the projection type to a dummy 'd3-esque' function,
//
// This wrapper alleviates subsequent code of (many) annoying if-statements.
function getProjection(geoLayout) {
    var projLayout = geoLayout.projection;
    var projType = projLayout.type;

    var projection = d3.geo[constants.projNames[projType]]();

    var clipAngle = geoLayout._isClipped ?
        constants.lonaxisSpan[projType] / 2 :
        null;

    var methods = ['center', 'rotate', 'parallels', 'clipExtent'];
    var dummyFn = function(_) { return _ ? projection : []; };

    for(var i = 0; i < methods.length; i++) {
        var m = methods[i];
        if(typeof projection[m] !== 'function') {
            projection[m] = dummyFn;
        }
    }

    projection.isLonLatOverEdges = function(lonlat) {
        if(projection(lonlat) === null) {
            return true;
        }

        if(clipAngle) {
            var r = projection.rotate();
            var angle = d3.geo.distance(lonlat, [-r[0], -r[1]]);
            var maxAngle = clipAngle * Math.PI / 180;
            return angle > maxAngle;
        } else {
            return false;
        }
    };

    projection.getPath = function() {
        return d3.geo.path().projection(projection);
    };

    projection.getBounds = function(object) {
        return projection.getPath().bounds(object);
    };

    // adapted from d3 v4:
    // https://github.com/d3/d3-geo/blob/master/src/projection/fit.js
    projection.fitExtent = function(extent, object) {
        var w = extent[1][0] - extent[0][0];
        var h = extent[1][1] - extent[0][1];
        var clip = projection.clipExtent && projection.clipExtent();

        projection
            .scale(150)
            .translate([0, 0]);

        if(clip) projection.clipExtent(null);

        var b = projection.getBounds(object);
        var k = Math.min(w / (b[1][0] - b[0][0]), h / (b[1][1] - b[0][1]));
        var x = +extent[0][0] + (w - k * (b[1][0] + b[0][0])) / 2;
        var y = +extent[0][1] + (h - k * (b[1][1] + b[0][1])) / 2;

        if(clip) projection.clipExtent(clip);

        return projection
            .scale(k * 150)
            .translate([x, y]);
    };

    projection.precision(constants.precision);

    if(clipAngle) {
        projection.clipAngle(clipAngle - constants.clipPad);
    }

    return projection;
}

function makeGraticule(axisName, geoLayout, fullLayout) {
    // equivalent to the d3 "ε"
    var epsilon = 1e-6;
    // same as the geoGraticule default
    var precision = 2.5;

    var axLayout = geoLayout[axisName];
    var scopeDefaults = constants.scopeDefaults[geoLayout.scope];
    var rng;
    var oppRng;
    var coordFn;

    if(axisName === 'lonaxis') {
        rng = scopeDefaults.lonaxisRange;
        oppRng = scopeDefaults.lataxisRange;
        coordFn = function(v, l) { return [v, l]; };
    } else if(axisName === 'lataxis') {
        rng = scopeDefaults.lataxisRange;
        oppRng = scopeDefaults.lonaxisRange;
        coordFn = function(v, l) { return [l, v]; };
    }

    var dummyAx = {
        type: 'linear',
        range: [rng[0], rng[1] - epsilon],
        tick0: axLayout.tick0,
        dtick: axLayout.dtick
    };

    Axes.setConvert(dummyAx, fullLayout);
    var vals = Axes.calcTicks(dummyAx);

    // remove duplicate on antimeridian
    if(!geoLayout.isScoped && axisName === 'lonaxis') {
        vals.pop();
    }

    var len = vals.length;
    var coords = new Array(len);

    for(var i = 0; i < len; i++) {
        var v = vals[i].x;
        var line = coords[i] = [];
        for(var l = oppRng[0]; l < oppRng[1] + precision; l += precision) {
            line.push(coordFn(v, l));
        }
    }

    return {
        type: 'MultiLineString',
        coordinates: coords
    };
}

// Returns polygon GeoJSON corresponding to lon/lat range box
// with well-defined direction
//
// Note that clipPad padding is added around range to avoid aliasing.
function makeRangeBox(lon, lat) {
    var clipPad = constants.clipPad;
    var lon0 = lon[0] + clipPad;
    var lon1 = lon[1] - clipPad;
    var lat0 = lat[0] + clipPad;
    var lat1 = lat[1] - clipPad;

    // to cross antimeridian w/o ambiguity
    if(lon0 > 0 && lon1 < 0) lon1 += 360;

    var dlon4 = (lon1 - lon0) / 4;

    return {
        type: 'Polygon',
        coordinates: [[
            [lon0, lat0],
            [lon0, lat1],
            [lon0 + dlon4, lat1],
            [lon0 + 2 * dlon4, lat1],
            [lon0 + 3 * dlon4, lat1],
            [lon1, lat1],
            [lon1, lat0],
            [lon1 - dlon4, lat0],
            [lon1 - 2 * dlon4, lat0],
            [lon1 - 3 * dlon4, lat0],
            [lon0, lat0]
        ]]
    };
}
