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
var mergeLength = require('../parcoords/merge_length');

function handleLineDefaults(traceIn, traceOut, defaultColor, layout, coerce) {
    coerce('line.shape');
    coerce('line.hovertemplate');

    var lineColor = coerce('line.color', layout.colorway[0]);
    if(hasColorscale(traceIn, 'line') && Lib.isArrayOrTypedArray(lineColor)) {
        if(lineColor.length) {
            coerce('line.colorscale');
            colorscaleDefaults(traceIn, traceOut, layout, coerce, {prefix: 'line.', cLetter: 'c'});
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
        // Dimension level
        coerce('label');
        coerce('displayindex', dimensionOut._index);

        // Category level
        var arrayIn = dimensionIn.categoryarray;
        var isValidArray = (Array.isArray(arrayIn) && arrayIn.length > 0);

        var orderDefault;
        if(isValidArray) orderDefault = 'array';
        var order = coerce('categoryorder', orderDefault);

        // coerce 'categoryarray' only in array order case
        if(order === 'array') {
            coerce('categoryarray');
            coerce('ticktext');
        } else {
            delete dimensionIn.categoryarray;
            delete dimensionIn.ticktext;
        }

        // cannot set 'categoryorder' to 'array' with an invalid 'categoryarray'
        if(!isValidArray && order === 'array') {
            dimensionOut.categoryorder = 'trace';
        }
    }
}

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
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

    coerce('hoveron');
    coerce('hovertemplate');
    coerce('arrangement');
    coerce('bundlecolors');
    coerce('sortpaths');
    coerce('counts');

    var labelfontDflt = {
        family: layout.font.family,
        size: Math.round(layout.font.size),
        color: layout.font.color
    };

    Lib.coerceFont(coerce, 'labelfont', labelfontDflt);

    var categoryfontDefault = {
        family: layout.font.family,
        size: Math.round(layout.font.size / 1.2),
        color: layout.font.color
    };

    Lib.coerceFont(coerce, 'tickfont', categoryfontDefault);
};
