/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorAttrs = require('../../components/color/attributes');
var domainAttrs = require('../domain').attributes;
var constants = require('./constants');
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var geoAxesAttrs = {
    range: {
        valType: 'info_array',
        role: 'info',
        items: [
            {valType: 'number'},
            {valType: 'number'}
        ],
        description: [
            'Sets the range of this axis (in degrees),',
            'sets the map\'s clipped coordinates.'
        ].join(' ')
    },
    showgrid: {
        valType: 'boolean',
        role: 'info',
        dflt: false,
        description: 'Sets whether or not graticule are shown on the map.'
    },
    tick0: {
        valType: 'number',
        role: 'info',
        dflt: 0,
        description: [
            'Sets the graticule\'s starting tick longitude/latitude.'
        ].join(' ')
    },
    dtick: {
        valType: 'number',
        role: 'info',
        description: [
            'Sets the graticule\'s longitude/latitude tick step.'
        ].join(' ')
    },
    gridcolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.lightLine,
        description: [
            'Sets the graticule\'s stroke color.'
        ].join(' ')
    },
    gridwidth: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 1,
        description: [
            'Sets the graticule\'s stroke width (in px).'
        ].join(' ')
    }
};

var attrs = module.exports = overrideAll({
    domain: domainAttrs({name: 'geo'}, {
        description: [
            'Note that geo subplots are constrained by domain.',
            'In general, when `projection.scale` is set to 1.',
            'a map will fit either its x or y domain, but not both.'
        ].join(' ')
    }),

    resolution: {
        valType: 'enumerated',
        values: [110, 50],
        role: 'info',
        dflt: 110,
        coerceNumber: true,
        description: [
            'Sets the resolution of the base layers.',
            'The values have units of km/mm',
            'e.g. 110 corresponds to a scale ratio of 1:110,000,000.'
        ].join(' ')
    },
    scope: {
        valType: 'enumerated',
        role: 'info',
        values: Object.keys(constants.scopeDefaults),
        dflt: 'world',
        description: 'Set the scope of the map.'
    },
    projection: {
        type: {
            valType: 'enumerated',
            role: 'info',
            values: Object.keys(constants.projNames),
            description: 'Sets the projection type.'
        },
        rotation: {
            lon: {
                valType: 'number',
                role: 'info',
                description: [
                    'Rotates the map along parallels',
                    '(in degrees East).',
                    'Defaults to the center of the `lonaxis.range` values.'
                ].join(' ')
            },
            lat: {
                valType: 'number',
                role: 'info',
                description: [
                    'Rotates the map along meridians',
                    '(in degrees North).'
                ].join(' ')
            },
            roll: {
                valType: 'number',
                role: 'info',
                description: [
                    'Roll the map (in degrees)',
                    'For example, a roll of *180* makes the map appear upside down.'
                ].join(' ')
            }
        },
        parallels: {
            valType: 'info_array',
            role: 'info',
            items: [
                {valType: 'number'},
                {valType: 'number'}
            ],
            description: [
                'For conic projection types only.',
                'Sets the parallels (tangent, secant)',
                'where the cone intersects the sphere.'
            ].join(' ')
        },
        scale: {
            valType: 'number',
            role: 'info',
            min: 0,
            dflt: 1,
            description: [
                'Zooms in or out on the map view.',
                'A scale of *1* corresponds to the largest zoom level',
                'that fits the map\'s lon and lat ranges. '
            ].join(' ')
        },
    },
    center: {
        lon: {
            valType: 'number',
            role: 'info',
            description: [
                'Sets the longitude of the map\'s center.',
                'By default, the map\'s longitude center lies at the middle of the longitude range',
                'for scoped projection and above `projection.rotation.lon` otherwise.'
            ].join(' ')
        },
        lat: {
            valType: 'number',
            role: 'info',
            description: [
                'Sets the latitude of the map\'s center.',
                'For all projection types, the map\'s latitude center lies',
                'at the middle of the latitude range by default.'
            ].join(' ')
        }
    },
    showcoastlines: {
        valType: 'boolean',
        role: 'info',
        description: 'Sets whether or not the coastlines are drawn.'
    },
    coastlinecolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.defaultLine,
        description: 'Sets the coastline color.'
    },
    coastlinewidth: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 1,
        description: 'Sets the coastline stroke width (in px).'
    },
    showland: {
        valType: 'boolean',
        role: 'info',
        dflt: false,
        description: 'Sets whether or not land masses are filled in color.'
    },
    landcolor: {
        valType: 'color',
        role: 'style',
        dflt: constants.landColor,
        description: 'Sets the land mass color.'
    },
    showocean: {
        valType: 'boolean',
        role: 'info',
        dflt: false,
        description: 'Sets whether or not oceans are filled in color.'
    },
    oceancolor: {
        valType: 'color',
        role: 'style',
        dflt: constants.waterColor,
        description: 'Sets the ocean color'
    },
    showlakes: {
        valType: 'boolean',
        role: 'info',
        dflt: false,
        description: 'Sets whether or not lakes are drawn.'
    },
    lakecolor: {
        valType: 'color',
        role: 'style',
        dflt: constants.waterColor,
        description: 'Sets the color of the lakes.'
    },
    showrivers: {
        valType: 'boolean',
        role: 'info',
        dflt: false,
        description: 'Sets whether or not rivers are drawn.'
    },
    rivercolor: {
        valType: 'color',
        role: 'style',
        dflt: constants.waterColor,
        description: 'Sets color of the rivers.'
    },
    riverwidth: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 1,
        description: 'Sets the stroke width (in px) of the rivers.'
    },
    showcountries: {
        valType: 'boolean',
        role: 'info',
        description: 'Sets whether or not country boundaries are drawn.'
    },
    countrycolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.defaultLine,
        description: 'Sets line color of the country boundaries.'
    },
    countrywidth: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 1,
        description: 'Sets line width (in px) of the country boundaries.'
    },
    showsubunits: {
        valType: 'boolean',
        role: 'info',
        description: [
            'Sets whether or not boundaries of subunits within countries',
            '(e.g. states, provinces) are drawn.'
        ].join(' ')
    },
    subunitcolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.defaultLine,
        description: 'Sets the color of the subunits boundaries.'
    },
    subunitwidth: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 1,
        description: 'Sets the stroke width (in px) of the subunits boundaries.'
    },
    showframe: {
        valType: 'boolean',
        role: 'info',
        description: 'Sets whether or not a frame is drawn around the map.'
    },
    framecolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.defaultLine,
        description: 'Sets the color the frame.'
    },
    framewidth: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 1,
        description: 'Sets the stroke width (in px) of the frame.'
    },
    bgcolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.background,
        description: 'Set the background color of the map'
    },
    lonaxis: geoAxesAttrs,
    lataxis: geoAxesAttrs
}, 'plot', 'from-root');

// set uirevision outside of overrideAll so it can be `editType: 'none'`
attrs.uirevision = {
    valType: 'any',
    role: 'info',
    editType: 'none',
    description: [
        'Controls persistence of user-driven changes in the view',
        '(projection and center). Defaults to `layout.uirevision`.'
    ].join(' ')
};
