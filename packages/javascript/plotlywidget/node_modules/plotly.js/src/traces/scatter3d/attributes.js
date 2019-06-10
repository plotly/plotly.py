/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scatterAttrs = require('../scatter/attributes');
var colorAttributes = require('../../components/colorscale/attributes');
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var baseAttrs = require('../../plots/attributes');
var DASHES = require('../../constants/gl3d_dashes');

var MARKER_SYMBOLS = require('../../constants/gl3d_markers');
var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var scatterLineAttrs = scatterAttrs.line;
var scatterMarkerAttrs = scatterAttrs.marker;
var scatterMarkerLineAttrs = scatterMarkerAttrs.line;

var lineAttrs = extendFlat({
    width: scatterLineAttrs.width,
    dash: {
        valType: 'enumerated',
        values: Object.keys(DASHES),
        dflt: 'solid',
        role: 'style',
        description: 'Sets the dash style of the lines.'
    }
}, colorAttributes('line'));

function makeProjectionAttr(axLetter) {
    return {
        show: {
            valType: 'boolean',
            role: 'info',
            dflt: false,
            description: [
                'Sets whether or not projections are shown along the',
                axLetter, 'axis.'
            ].join(' ')
        },
        opacity: {
            valType: 'number',
            role: 'style',
            min: 0,
            max: 1,
            dflt: 1,
            description: 'Sets the projection color.'
        },
        scale: {
            valType: 'number',
            role: 'style',
            min: 0,
            max: 10,
            dflt: 2 / 3,
            description: [
                'Sets the scale factor determining the size of the',
                'projection marker points.'
            ].join(' ')
        }
    };
}

var attrs = module.exports = overrideAll({
    x: scatterAttrs.x,
    y: scatterAttrs.y,
    z: {
        valType: 'data_array',
        description: 'Sets the z coordinates.'
    },

    text: extendFlat({}, scatterAttrs.text, {
        description: [
            'Sets text elements associated with each (x,y,z) triplet.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of string, the items are mapped in order to the',
            'this trace\'s (x,y,z) coordinates.',
            'If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,',
            'these elements will be seen in the hover labels.'
        ].join(' ')
    }),
    hovertext: extendFlat({}, scatterAttrs.hovertext, {
        description: [
            'Sets text elements associated with each (x,y,z) triplet.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of string, the items are mapped in order to the',
            'this trace\'s (x,y,z) coordinates.',
            'To be seen, trace `hoverinfo` must contain a *text* flag.'
        ].join(' ')
    }),
    hovertemplate: hovertemplateAttrs(),

    mode: extendFlat({}, scatterAttrs.mode,  // shouldn't this be on-par with 2D?
        {dflt: 'lines+markers'}),
    surfaceaxis: {
        valType: 'enumerated',
        role: 'info',
        values: [-1, 0, 1, 2],
        dflt: -1,
        description: [
            'If *-1*, the scatter points are not fill with a surface',
            'If *0*, *1*, *2*, the scatter points are filled with',
            'a Delaunay surface about the x, y, z respectively.'
        ].join(' ')
    },
    surfacecolor: {
        valType: 'color',
        role: 'style',
        description: 'Sets the surface fill color.'
    },
    projection: {
        x: makeProjectionAttr('x'),
        y: makeProjectionAttr('y'),
        z: makeProjectionAttr('z')
    },

    connectgaps: scatterAttrs.connectgaps,
    line: lineAttrs,

    marker: extendFlat({  // Parity with scatter.js?
        symbol: {
            valType: 'enumerated',
            values: Object.keys(MARKER_SYMBOLS),
            role: 'style',
            dflt: 'circle',
            arrayOk: true,
            description: 'Sets the marker symbol type.'
        },
        size: extendFlat({}, scatterMarkerAttrs.size, {dflt: 8}),
        sizeref: scatterMarkerAttrs.sizeref,
        sizemin: scatterMarkerAttrs.sizemin,
        sizemode: scatterMarkerAttrs.sizemode,
        opacity: extendFlat({}, scatterMarkerAttrs.opacity, {
            arrayOk: false,
            description: [
                'Sets the marker opacity.',
                'Note that the marker opacity for scatter3d traces',
                'must be a scalar value for performance reasons.',
                'To set a blending opacity value',
                '(i.e. which is not transparent), set *marker.color*',
                'to an rgba color and use its alpha channel.'
            ].join(' ')
        }),
        colorbar: scatterMarkerAttrs.colorbar,

        line: extendFlat({
            width: extendFlat({}, scatterMarkerLineAttrs.width, {arrayOk: false})
        },
            colorAttributes('marker.line')
        )
    },
        colorAttributes('marker')
    ),

    textposition: extendFlat({}, scatterAttrs.textposition, {dflt: 'top center'}),
    textfont: {
        color: scatterAttrs.textfont.color,
        size: scatterAttrs.textfont.size,
        family: extendFlat({}, scatterAttrs.textfont.family, {arrayOk: false})
    },

    hoverinfo: extendFlat({}, baseAttrs.hoverinfo)
}, 'calc', 'nested');

attrs.x.editType = attrs.y.editType = attrs.z.editType = 'calc+clearAxisTypes';
