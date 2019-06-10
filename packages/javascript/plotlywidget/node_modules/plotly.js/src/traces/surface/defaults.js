/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');

var colorscaleDefaults = require('../../components/colorscale/defaults');
var attributes = require('./attributes');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    var i, j;

    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var x = coerce('x');
    var y = coerce('y');

    var z = coerce('z');
    if(!z || !z.length ||
       (x ? (x.length < 1) : false) ||
       (y ? (y.length < 1) : false)
    ) {
        traceOut.visible = false;
        return;
    }

    traceOut._xlength = (Array.isArray(x) && Lib.isArrayOrTypedArray(x[0])) ? z.length : z[0].length;
    traceOut._ylength = z.length;

    var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleTraceDefaults');
    handleCalendarDefaults(traceIn, traceOut, ['x', 'y', 'z'], layout);

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    // Coerce remaining properties
    [
        'lighting.ambient',
        'lighting.diffuse',
        'lighting.specular',
        'lighting.roughness',
        'lighting.fresnel',
        'lightposition.x',
        'lightposition.y',
        'lightposition.z',
        'hidesurface',
        'connectgaps',
        'opacity'
    ].forEach(function(x) { coerce(x); });

    var surfaceColor = coerce('surfacecolor');

    var dims = ['x', 'y', 'z'];
    for(i = 0; i < 3; ++i) {
        var contourDim = 'contours.' + dims[i];
        var show = coerce(contourDim + '.show');
        var highlight = coerce(contourDim + '.highlight');

        if(show || highlight) {
            for(j = 0; j < 3; ++j) {
                coerce(contourDim + '.project.' + dims[j]);
            }
        }

        if(show) {
            coerce(contourDim + '.color');
            coerce(contourDim + '.width');
            coerce(contourDim + '.usecolormap');
        }

        if(highlight) {
            coerce(contourDim + '.highlightcolor');
            coerce(contourDim + '.highlightwidth');
        }

        coerce(contourDim + '.start');
        coerce(contourDim + '.end');
        coerce(contourDim + '.size');
    }

    // backward compatibility block
    if(!surfaceColor) {
        mapLegacy(traceIn, 'zmin', 'cmin');
        mapLegacy(traceIn, 'zmax', 'cmax');
        mapLegacy(traceIn, 'zauto', 'cauto');
    }

    // TODO if contours.?.usecolormap are false and hidesurface is true
    // the colorbar shouldn't be shown by default

    colorscaleDefaults(
        traceIn, traceOut, layout, coerce, {prefix: '', cLetter: 'c'}
    );

    // disable 1D transforms - currently surface does NOT support column data like heatmap does
    // you can use mesh3d for this use case, but not surface
    traceOut._length = null;
};

function mapLegacy(traceIn, oldAttr, newAttr) {
    if(oldAttr in traceIn && !(newAttr in traceIn)) {
        traceIn[newAttr] = traceIn[oldAttr];
    }
}
