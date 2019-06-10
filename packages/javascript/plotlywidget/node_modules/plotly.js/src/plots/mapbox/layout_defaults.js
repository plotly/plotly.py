/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');

var handleSubplotDefaults = require('../subplot_defaults');
var handleArrayContainerDefaults = require('../array_container_defaults');
var layoutAttributes = require('./layout_attributes');


module.exports = function supplyLayoutDefaults(layoutIn, layoutOut, fullData) {
    handleSubplotDefaults(layoutIn, layoutOut, fullData, {
        type: 'mapbox',
        attributes: layoutAttributes,
        handleDefaults: handleDefaults,
        partition: 'y',
        accessToken: layoutOut._mapboxAccessToken
    });
};

function handleDefaults(containerIn, containerOut, coerce, opts) {
    coerce('accesstoken', opts.accessToken);
    coerce('style');
    coerce('center.lon');
    coerce('center.lat');
    coerce('zoom');
    coerce('bearing');
    coerce('pitch');

    handleArrayContainerDefaults(containerIn, containerOut, {
        name: 'layers',
        handleItemDefaults: handleLayerDefaults
    });

    // copy ref to input container to update 'center' and 'zoom' on map move
    containerOut._input = containerIn;
}

function handleLayerDefaults(layerIn, layerOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(layerIn, layerOut, layoutAttributes.layers, attr, dflt);
    }

    var visible = coerce('visible');
    if(visible) {
        var sourceType = coerce('sourcetype');
        coerce('source');

        if(sourceType === 'vector') coerce('sourcelayer');

        // maybe add smart default based off GeoJSON geometry?
        var type = coerce('type');

        coerce('below');
        coerce('color');
        coerce('opacity');
        coerce('minzoom');
        coerce('maxzoom');

        if(type === 'circle') {
            coerce('circle.radius');
        }

        if(type === 'line') {
            coerce('line.width');
            coerce('line.dash');
        }

        if(type === 'fill') {
            coerce('fill.outlinecolor');
        }

        if(type === 'symbol') {
            coerce('symbol.icon');
            coerce('symbol.iconsize');

            coerce('symbol.text');
            Lib.coerceFont(coerce, 'symbol.textfont');
            coerce('symbol.textposition');
            coerce('symbol.placement');
        }
    }
}
