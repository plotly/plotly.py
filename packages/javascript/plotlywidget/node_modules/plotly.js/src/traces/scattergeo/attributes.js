/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var scatterAttrs = require('../scatter/attributes');
var plotAttrs = require('../../plots/attributes');
var colorAttributes = require('../../components/colorscale/attributes');
var dash = require('../../components/drawing/attributes').dash;

var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var scatterMarkerAttrs = scatterAttrs.marker;
var scatterLineAttrs = scatterAttrs.line;
var scatterMarkerLineAttrs = scatterMarkerAttrs.line;

module.exports = overrideAll({
    lon: {
        valType: 'data_array',
        description: 'Sets the longitude coordinates (in degrees East).'
    },
    lat: {
        valType: 'data_array',
        description: 'Sets the latitude coordinates (in degrees North).'
    },

    locations: {
        valType: 'data_array',
        description: [
            'Sets the coordinates via location IDs or names.',
            'Coordinates correspond to the centroid of each location given.',
            'See `locationmode` for more info.'
        ].join(' ')
    },
    locationmode: {
        valType: 'enumerated',
        values: ['ISO-3', 'USA-states', 'country names'],
        role: 'info',
        dflt: 'ISO-3',
        description: [
            'Determines the set of locations used to match entries in `locations`',
            'to regions on the map.'
        ].join(' ')
    },

    mode: extendFlat({}, scatterAttrs.mode, {dflt: 'markers'}),

    text: extendFlat({}, scatterAttrs.text, {
        description: [
            'Sets text elements associated with each (lon,lat) pair',
            'or item in `locations`.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of string, the items are mapped in order to the',
            'this trace\'s (lon,lat) or `locations` coordinates.',
            'If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,',
            'these elements will be seen in the hover labels.'
        ].join(' ')
    }),
    hovertext: extendFlat({}, scatterAttrs.hovertext, {
        description: [
            'Sets hover text elements associated with each (lon,lat) pair',
            'or item in `locations`.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of string, the items are mapped in order to the',
            'this trace\'s (lon,lat) or `locations` coordinates.',
            'To be seen, trace `hoverinfo` must contain a *text* flag.'
        ].join(' ')
    }),

    textfont: scatterAttrs.textfont,
    textposition: scatterAttrs.textposition,

    line: {
        color: scatterLineAttrs.color,
        width: scatterLineAttrs.width,
        dash: dash
    },
    connectgaps: scatterAttrs.connectgaps,

    marker: extendFlat({
        symbol: scatterMarkerAttrs.symbol,
        opacity: scatterMarkerAttrs.opacity,
        size: scatterMarkerAttrs.size,
        sizeref: scatterMarkerAttrs.sizeref,
        sizemin: scatterMarkerAttrs.sizemin,
        sizemode: scatterMarkerAttrs.sizemode,
        colorbar: scatterMarkerAttrs.colorbar,
        line: extendFlat({
            width: scatterMarkerLineAttrs.width
        },
            colorAttributes('marker.line')
        ),
        gradient: scatterMarkerAttrs.gradient
    },
        colorAttributes('marker')
    ),

    fill: {
        valType: 'enumerated',
        values: ['none', 'toself'],
        dflt: 'none',
        role: 'style',
        description: [
            'Sets the area to fill with a solid color.',
            'Use with `fillcolor` if not *none*.',
            '*toself* connects the endpoints of the trace (or each segment',
            'of the trace if it has gaps) into a closed shape.'
        ].join(' ')
    },
    fillcolor: scatterAttrs.fillcolor,

    selected: scatterAttrs.selected,
    unselected: scatterAttrs.unselected,

    hoverinfo: extendFlat({}, plotAttrs.hoverinfo, {
        flags: ['lon', 'lat', 'location', 'text', 'name']
    }),
    hovertemplate: hovertemplateAttrs(),
}, 'calc', 'nested');
