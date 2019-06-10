/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');

var Lib = require('../../lib');
var BADNUM = require('../../constants/numerical').BADNUM;
var getTopojsonFeatures = require('../../lib/topojson_utils').getTopojsonFeatures;
var locationToFeature = require('../../lib/geo_location_utils').locationToFeature;
var geoJsonUtils = require('../../lib/geojson_utils');
var subTypes = require('../scatter/subtypes');
var style = require('./style');

module.exports = function plot(gd, geo, calcData) {
    for(var i = 0; i < calcData.length; i++) {
        calcGeoJSON(calcData[i], geo.topojson);
    }

    function removeBADNUM(d, node) {
        if(d.lonlat[0] === BADNUM) {
            d3.select(node).remove();
        }
    }

    var scatterLayer = geo.layers.frontplot.select('.scatterlayer');
    var gTraces = Lib.makeTraceGroups(scatterLayer, calcData, 'trace scattergeo');

    // TODO find a way to order the inner nodes on update
    gTraces.selectAll('*').remove();

    gTraces.each(function(calcTrace) {
        var s = calcTrace[0].node3 = d3.select(this);
        var trace = calcTrace[0].trace;

        if(subTypes.hasLines(trace) || trace.fill !== 'none') {
            var lineCoords = geoJsonUtils.calcTraceToLineCoords(calcTrace);

            var lineData = (trace.fill !== 'none') ?
                geoJsonUtils.makePolygon(lineCoords) :
                geoJsonUtils.makeLine(lineCoords);

            s.selectAll('path.js-line')
                .data([{geojson: lineData, trace: trace}])
              .enter().append('path')
                .classed('js-line', true)
                .style('stroke-miterlimit', 2);
        }

        if(subTypes.hasMarkers(trace)) {
            s.selectAll('path.point')
                .data(Lib.identity)
             .enter().append('path')
                .classed('point', true)
                .each(function(calcPt) { removeBADNUM(calcPt, this); });
        }

        if(subTypes.hasText(trace)) {
            s.selectAll('g')
                .data(Lib.identity)
              .enter().append('g')
                .append('text')
                .each(function(calcPt) { removeBADNUM(calcPt, this); });
        }

        // call style here within topojson request callback
        style(gd, calcTrace);
    });
};

function calcGeoJSON(calcTrace, topojson) {
    var trace = calcTrace[0].trace;

    if(!Array.isArray(trace.locations)) return;

    var features = getTopojsonFeatures(trace, topojson);
    var locationmode = trace.locationmode;

    for(var i = 0; i < calcTrace.length; i++) {
        var calcPt = calcTrace[i];
        var feature = locationToFeature(locationmode, calcPt.loc, features);

        calcPt.lonlat = feature ? feature.properties.ct : [BADNUM, BADNUM];
    }
}
