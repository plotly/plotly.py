/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var BADNUM = require('../constants/numerical').BADNUM;

/**
 * Convert calcTrace to GeoJSON 'MultiLineString' coordinate arrays
 *
 * @param {object} calcTrace
 *  gd.calcdata item.
 *  Note that calcTrace[i].lonlat is assumed to be defined
 *
 * @return {array}
 *  return line coords array (or array of arrays)
 *
 */
exports.calcTraceToLineCoords = function(calcTrace) {
    var trace = calcTrace[0].trace;
    var connectgaps = trace.connectgaps;

    var coords = [];
    var lineString = [];

    for(var i = 0; i < calcTrace.length; i++) {
        var calcPt = calcTrace[i];
        var lonlat = calcPt.lonlat;

        if(lonlat[0] !== BADNUM) {
            lineString.push(lonlat);
        } else if(!connectgaps && lineString.length > 0) {
            coords.push(lineString);
            lineString = [];
        }
    }

    if(lineString.length > 0) {
        coords.push(lineString);
    }

    return coords;
};


/**
 * Make line ('LineString' or 'MultiLineString') GeoJSON
 *
 * @param {array} coords
 *  results form calcTraceToLineCoords
 * @return {object} out
 *  GeoJSON object
 *
 */
exports.makeLine = function(coords) {
    if(coords.length === 1) {
        return {
            type: 'LineString',
            coordinates: coords[0]
        };
    } else {
        return {
            type: 'MultiLineString',
            coordinates: coords
        };
    }
};

/**
 * Make polygon ('Polygon' or 'MultiPolygon') GeoJSON
 *
 * @param {array} coords
 *  results form calcTraceToLineCoords
 * @return {object} out
 *  GeoJSON object
 */
exports.makePolygon = function(coords) {
    if(coords.length === 1) {
        return {
            type: 'Polygon',
            coordinates: coords
        };
    } else {
        var _coords = new Array(coords.length);

        for(var i = 0; i < coords.length; i++) {
            _coords[i] = [coords[i]];
        }

        return {
            type: 'MultiPolygon',
            coordinates: _coords
        };
    }
};

/**
 * Make blank GeoJSON
 *
 * @return {object}
 *  Blank GeoJSON object
 *
 */
exports.makeBlank = function() {
    return {
        type: 'Point',
        coordinates: []
    };
};
