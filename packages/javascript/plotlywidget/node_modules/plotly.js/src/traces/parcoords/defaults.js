/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var hasColorscale = require('../../components/colorscale/helpers').hasColorscale;
var colorscaleDefaults = require('../../components/colorscale/defaults');
var handleDomainDefaults = require('../../plots/domain').defaults;
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');

var attributes = require('./attributes');
var axisBrush = require('./axisbrush');
var maxDimensionCount = require('./constants').maxDimensionCount;
var mergeLength = require('./merge_length');

function handleLineDefaults(traceIn, traceOut, defaultColor, layout, coerce) {
    var lineColor = coerce('line.color', defaultColor);

    if(hasColorscale(traceIn, 'line') && Lib.isArrayOrTypedArray(lineColor)) {
        if(lineColor.length) {
            coerce('line.colorscale');
            colorscaleDefaults(traceIn, traceOut, layout, coerce, {prefix: 'line.', cLetter: 'c'});
            // TODO: I think it would be better to keep showing lines beyond the last line color
            // but I'm not sure what color to give these lines - probably black or white
            // depending on the background color?
            return lineColor.length;
        } else {
            traceOut.line.color = defaultColor;
        }
    }
    return Infinity;
}

function dimensionDefaults(dimensionIn, dimensionOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(dimensionIn, dimensionOut, attributes.dimensions, attr, dflt);
    }

    var values = coerce('values');
    var visible = coerce('visible');
    if(!(values && values.length)) {
        visible = dimensionOut.visible = false;
    }

    if(visible) {
        coerce('label');
        coerce('tickvals');
        coerce('ticktext');
        coerce('tickformat');
        coerce('range');

        coerce('multiselect');
        var constraintRange = coerce('constraintrange');
        if(constraintRange) {
            dimensionOut.constraintrange = axisBrush.cleanRanges(constraintRange, dimensionOut);
        }
    }
}

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var dimensionsIn = traceIn.dimensions;
    if(Array.isArray(dimensionsIn) && dimensionsIn.length > maxDimensionCount) {
        Lib.log('parcoords traces support up to ' + maxDimensionCount + ' dimensions at the moment');
        dimensionsIn.splice(maxDimensionCount);
    }

    var dimensions = handleArrayContainerDefaults(traceIn, traceOut, {
        name: 'dimensions',
        handleItemDefaults: dimensionDefaults
    });

    var len = handleLineDefaults(traceIn, traceOut, defaultColor, layout, coerce);

    handleDomainDefaults(traceOut, layout, coerce);

    if(!Array.isArray(dimensions) || !dimensions.length) {
        traceOut.visible = false;
    }

    mergeLength(traceOut, dimensions, 'values', len);

    // make default font size 10px (default is 12),
    // scale linearly with global font size
    var fontDflt = {
        family: layout.font.family,
        size: Math.round(layout.font.size / 1.2),
        color: layout.font.color
    };

    Lib.coerceFont(coerce, 'labelfont', fontDflt);
    Lib.coerceFont(coerce, 'tickfont', fontDflt);
    Lib.coerceFont(coerce, 'rangefont', fontDflt);
};
