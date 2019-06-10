/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');
var BADNUM = require('../../constants/numerical').BADNUM;
var geoJsonUtils = require('../../lib/geojson_utils');

var Colorscale = require('../../components/colorscale');
var Drawing = require('../../components/drawing');
var makeBubbleSizeFn = require('../scatter/make_bubble_size_func');
var subTypes = require('../scatter/subtypes');
var convertTextOpts = require('../../plots/mapbox/convert_text_opts');

module.exports = function convert(calcTrace) {
    var trace = calcTrace[0].trace;

    var isVisible = (trace.visible === true && trace._length !== 0);
    var hasFill = (trace.fill !== 'none');
    var hasLines = subTypes.hasLines(trace);
    var hasMarkers = subTypes.hasMarkers(trace);
    var hasText = subTypes.hasText(trace);
    var hasCircles = (hasMarkers && trace.marker.symbol === 'circle');
    var hasSymbols = (hasMarkers && trace.marker.symbol !== 'circle');

    var fill = initContainer();
    var line = initContainer();
    var circle = initContainer();
    var symbol = initContainer();

    var opts = {
        fill: fill,
        line: line,
        circle: circle,
        symbol: symbol
    };

    // early return if not visible or placeholder
    if(!isVisible) return opts;

    // fill layer and line layer use the same coords
    var lineCoords;
    if(hasFill || hasLines) {
        lineCoords = geoJsonUtils.calcTraceToLineCoords(calcTrace);
    }

    if(hasFill) {
        fill.geojson = geoJsonUtils.makePolygon(lineCoords);
        fill.layout.visibility = 'visible';

        Lib.extendFlat(fill.paint, {
            'fill-color': trace.fillcolor
        });
    }

    if(hasLines) {
        line.geojson = geoJsonUtils.makeLine(lineCoords);
        line.layout.visibility = 'visible';

        Lib.extendFlat(line.paint, {
            'line-width': trace.line.width,
            'line-color': trace.line.color,
            'line-opacity': trace.opacity
        });

        // TODO convert line.dash into line-dasharray
    }

    if(hasCircles) {
        var circleOpts = makeCircleOpts(calcTrace);
        circle.geojson = circleOpts.geojson;
        circle.layout.visibility = 'visible';

        Lib.extendFlat(circle.paint, {
            'circle-color': circleOpts.mcc,
            'circle-radius': circleOpts.mrc,
            'circle-opacity': circleOpts.mo
        });
    }

    if(hasSymbols || hasText) {
        symbol.geojson = makeSymbolGeoJSON(calcTrace);

        Lib.extendFlat(symbol.layout, {
            visibility: 'visible',
            'icon-image': '{symbol}-15',
            'text-field': '{text}'
        });

        if(hasSymbols) {
            Lib.extendFlat(symbol.layout, {
                'icon-size': trace.marker.size / 10
            });

            Lib.extendFlat(symbol.paint, {
                'icon-opacity': trace.opacity * trace.marker.opacity,

                // TODO does not work ??
                'icon-color': trace.marker.color
            });
        }

        if(hasText) {
            var iconSize = (trace.marker || {}).size;
            var textOpts = convertTextOpts(trace.textposition, iconSize);

            // all data-driven below !!

            Lib.extendFlat(symbol.layout, {
                'text-size': trace.textfont.size,
                'text-anchor': textOpts.anchor,
                'text-offset': textOpts.offset

                // TODO font family
                // 'text-font': symbol.textfont.family.split(', '),
            });

            Lib.extendFlat(symbol.paint, {
                'text-color': trace.textfont.color,
                'text-opacity': trace.opacity
            });
        }
    }

    return opts;
};

function initContainer() {
    return {
        geojson: geoJsonUtils.makeBlank(),
        layout: { visibility: 'none' },
        paint: {}
    };
}

function makeCircleOpts(calcTrace) {
    var trace = calcTrace[0].trace;
    var marker = trace.marker;
    var selectedpoints = trace.selectedpoints;
    var arrayColor = Lib.isArrayOrTypedArray(marker.color);
    var arraySize = Lib.isArrayOrTypedArray(marker.size);
    var arrayOpacity = Lib.isArrayOrTypedArray(marker.opacity);
    var i;

    function addTraceOpacity(o) { return trace.opacity * o; }

    function size2radius(s) { return s / 2; }

    var colorFn;
    if(arrayColor) {
        if(Colorscale.hasColorscale(trace, 'marker')) {
            colorFn = Colorscale.makeColorScaleFuncFromTrace(marker);
        } else {
            colorFn = Lib.identity;
        }
    }

    var sizeFn;
    if(arraySize) {
        sizeFn = makeBubbleSizeFn(trace);
    }

    var opacityFn;
    if(arrayOpacity) {
        opacityFn = function(mo) {
            var mo2 = isNumeric(mo) ? +Lib.constrain(mo, 0, 1) : 0;
            return addTraceOpacity(mo2);
        };
    }

    var features = [];
    for(i = 0; i < calcTrace.length; i++) {
        var calcPt = calcTrace[i];
        var lonlat = calcPt.lonlat;

        if(isBADNUM(lonlat)) continue;

        var props = {};
        if(colorFn) props.mcc = calcPt.mcc = colorFn(calcPt.mc);
        if(sizeFn) props.mrc = calcPt.mrc = sizeFn(calcPt.ms);
        if(opacityFn) props.mo = opacityFn(calcPt.mo);
        if(selectedpoints) props.selected = calcPt.selected || 0;

        features.push({
            type: 'Feature',
            geometry: {type: 'Point', coordinates: lonlat},
            properties: props
        });
    }

    var fns;
    if(selectedpoints) {
        fns = Drawing.makeSelectedPointStyleFns(trace);

        for(i = 0; i < features.length; i++) {
            var d = features[i].properties;

            if(fns.selectedOpacityFn) {
                d.mo = addTraceOpacity(fns.selectedOpacityFn(d));
            }
            if(fns.selectedColorFn) {
                d.mcc = fns.selectedColorFn(d);
            }
            if(fns.selectedSizeFn) {
                d.mrc = fns.selectedSizeFn(d);
            }
        }
    }

    return {
        geojson: {type: 'FeatureCollection', features: features},
        mcc: arrayColor || (fns && fns.selectedColorFn) ?
            {type: 'identity', property: 'mcc'} :
            marker.color,
        mrc: arraySize || (fns && fns.selectedSizeFn) ?
            {type: 'identity', property: 'mrc'} :
            size2radius(marker.size),
        mo: arrayOpacity || (fns && fns.selectedOpacityFn) ?
            {type: 'identity', property: 'mo'} :
            addTraceOpacity(marker.opacity)
    };
}

function makeSymbolGeoJSON(calcTrace) {
    var trace = calcTrace[0].trace;

    var marker = trace.marker || {};
    var symbol = marker.symbol;
    var text = trace.text;

    var fillSymbol = (symbol !== 'circle') ?
        getFillFunc(symbol) :
        blankFillFunc;

    var fillText = subTypes.hasText(trace) ?
        getFillFunc(text) :
        blankFillFunc;

    var features = [];

    for(var i = 0; i < calcTrace.length; i++) {
        var calcPt = calcTrace[i];

        if(isBADNUM(calcPt.lonlat)) continue;

        features.push({
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: calcPt.lonlat
            },
            properties: {
                symbol: fillSymbol(calcPt.mx),
                text: fillText(calcPt.tx)
            }
        });
    }

    return {
        type: 'FeatureCollection',
        features: features
    };
}

function getFillFunc(attr) {
    if(Lib.isArrayOrTypedArray(attr)) {
        return function(v) { return v; };
    } else if(attr) {
        return function() { return attr; };
    } else {
        return blankFillFunc;
    }
}

function blankFillFunc() { return ''; }

// only need to check lon (OR lat)
function isBADNUM(lonlat) {
    return lonlat[0] === BADNUM;
}
