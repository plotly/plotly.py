/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Registry = require('../../registry');
var attributes = require('./attributes');
var colorscaleDefaults = require('../../components/colorscale/defaults');

function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    supplyIsoDefaults(traceIn, traceOut, defaultColor, layout, coerce);
}

function supplyIsoDefaults(traceIn, traceOut, defaultColor, layout, coerce) {
    var isomin = coerce('isomin');
    var isomax = coerce('isomax');

    if(isomax !== undefined && isomax !== null &&
        isomin !== undefined && isomin !== null &&
         isomin > isomax) {
        // applying default values in this case:
        traceOut.isomin = null;
        traceOut.isomax = null;
    }

    var x = coerce('x');
    var y = coerce('y');
    var z = coerce('z');
    var value = coerce('value');

    if(
        !x || !x.length ||
        !y || !y.length ||
        !z || !z.length ||
        !value || !value.length
    ) {
        traceOut.visible = false;
        return;
    }

    var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleTraceDefaults');
    handleCalendarDefaults(traceIn, traceOut, ['x', 'y', 'z'], layout);

    ['x', 'y', 'z'].forEach(function(dim) {
        var capDim = 'caps.' + dim;
        var showCap = coerce(capDim + '.show');
        if(showCap) {
            coerce(capDim + '.fill');
        }

        var sliceDim = 'slices.' + dim;
        var showSlice = coerce(sliceDim + '.show');
        if(showSlice) {
            coerce(sliceDim + '.fill');
            coerce(sliceDim + '.locations');
        }
    });

    var showSpaceframe = coerce('spaceframe.show');
    if(showSpaceframe) {
        coerce('spaceframe.fill');
    }

    var showSurface = coerce('surface.show');
    if(showSurface) {
        coerce('surface.count');
        coerce('surface.fill');
        coerce('surface.pattern');
    }

    var showContour = coerce('contour.show');
    if(showContour) {
        coerce('contour.color');
        coerce('contour.width');
    }

    // Coerce remaining properties
    [
        'text',
        'hovertext',
        'hovertemplate',
        'lighting.ambient',
        'lighting.diffuse',
        'lighting.specular',
        'lighting.roughness',
        'lighting.fresnel',
        'lighting.vertexnormalsepsilon',
        'lighting.facenormalsepsilon',
        'lightposition.x',
        'lightposition.y',
        'lightposition.z',
        'flatshading',
        'opacity'
    ].forEach(function(x) { coerce(x); });

    colorscaleDefaults(traceIn, traceOut, layout, coerce, {prefix: '', cLetter: 'c'});

    // disable 1D transforms (for now)
    traceOut._length = null;
}

module.exports = {
    supplyDefaults: supplyDefaults,
    supplyIsoDefaults: supplyIsoDefaults
};
