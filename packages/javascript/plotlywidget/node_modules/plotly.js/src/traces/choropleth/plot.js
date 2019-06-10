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
var polygon = require('../../lib/polygon');

var getTopojsonFeatures = require('../../lib/topojson_utils').getTopojsonFeatures;
var locationToFeature = require('../../lib/geo_location_utils').locationToFeature;
var style = require('./style').style;

module.exports = function plot(gd, geo, calcData) {
    for(var i = 0; i < calcData.length; i++) {
        calcGeoJSON(calcData[i], geo.topojson);
    }

    var choroplethLayer = geo.layers.backplot.select('.choroplethlayer');
    Lib.makeTraceGroups(choroplethLayer, calcData, 'trace choropleth').each(function(calcTrace) {
        var sel = calcTrace[0].node3 = d3.select(this);

        var paths = sel.selectAll('path.choroplethlocation')
            .data(Lib.identity);

        paths.enter().append('path')
            .classed('choroplethlocation', true);

        paths.exit().remove();

        // call style here within topojson request callback
        style(gd, calcTrace);
    });
};

function calcGeoJSON(calcTrace, topojson) {
    var trace = calcTrace[0].trace;
    var len = calcTrace.length;
    var features = getTopojsonFeatures(trace, topojson);

    for(var i = 0; i < len; i++) {
        var calcPt = calcTrace[i];
        var feature = locationToFeature(trace.locationmode, calcPt.loc, features);

        if(!feature) {
            calcPt.geojson = null;
            continue;
        }


        calcPt.geojson = feature;
        calcPt.ct = feature.properties.ct;
        calcPt.index = i;
        calcPt._polygons = feature2polygons(feature);
    }
}

function feature2polygons(feature) {
    var geometry = feature.geometry;
    var coords = geometry.coordinates;
    var loc = feature.id;

    var polygons = [];
    var appendPolygon, j, k, m;

    function doesCrossAntiMerdian(pts) {
        for(var l = 0; l < pts.length - 1; l++) {
            if(pts[l][0] > 0 && pts[l + 1][0] < 0) return l;
        }
        return null;
    }

    if(loc === 'RUS' || loc === 'FJI') {
        // Russia and Fiji have landmasses that cross the antimeridian,
        // we need to add +360 to their longitude coordinates, so that
        // polygon 'contains' doesn't get confused when crossing the antimeridian.
        //
        // Note that other countries have polygons on either side of the antimeridian
        // (e.g. some Aleutian island for the USA), but those don't confuse
        // the 'contains' method; these are skipped here.
        appendPolygon = function(_pts) {
            var pts;

            if(doesCrossAntiMerdian(_pts) === null) {
                pts = _pts;
            } else {
                pts = new Array(_pts.length);
                for(m = 0; m < _pts.length; m++) {
                    // do nut mutate calcdata[i][j].geojson !!
                    pts[m] = [
                        _pts[m][0] < 0 ? _pts[m][0] + 360 : _pts[m][0],
                        _pts[m][1]
                    ];
                }
            }

            polygons.push(polygon.tester(pts));
        };
    } else if(loc === 'ATA') {
        // Antarctica has a landmass that wraps around every longitudes which
        // confuses the 'contains' methods.
        appendPolygon = function(pts) {
            var crossAntiMeridianIndex = doesCrossAntiMerdian(pts);

            // polygon that do not cross anti-meridian need no special handling
            if(crossAntiMeridianIndex === null) {
                return polygons.push(polygon.tester(pts));
            }

            // stitch polygon by adding pt over South Pole,
            // so that it covers the projected region covers all latitudes
            //
            // Note that the algorithm below only works for polygons that
            // start and end on longitude -180 (like the ones built by
            // https://github.com/etpinard/sane-topojson).
            var stitch = new Array(pts.length + 1);
            var si = 0;

            for(m = 0; m < pts.length; m++) {
                if(m > crossAntiMeridianIndex) {
                    stitch[si++] = [pts[m][0] + 360, pts[m][1]];
                } else if(m === crossAntiMeridianIndex) {
                    stitch[si++] = pts[m];
                    stitch[si++] = [pts[m][0], -90];
                } else {
                    stitch[si++] = pts[m];
                }
            }

            // polygon.tester by default appends pt[0] to the points list,
            // we must remove it here, to avoid a jump in longitude from 180 to -180,
            // that would confuse the 'contains' method
            var tester = polygon.tester(stitch);
            tester.pts.pop();
            polygons.push(tester);
        };
    } else {
        // otherwise using same array ref is fine
        appendPolygon = function(pts) {
            polygons.push(polygon.tester(pts));
        };
    }

    switch(geometry.type) {
        case 'MultiPolygon':
            for(j = 0; j < coords.length; j++) {
                for(k = 0; k < coords[j].length; k++) {
                    appendPolygon(coords[j][k]);
                }
            }
            break;
        case 'Polygon':
            for(j = 0; j < coords.length; j++) {
                appendPolygon(coords[j]);
            }
            break;
    }

    return polygons;
}
