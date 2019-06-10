/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');
var defaultLine = require('../../components/color').defaultLine;
var domainAttrs = require('../domain').attributes;
var fontAttrs = require('../font_attributes');
var textposition = require('../../traces/scatter/attributes').textposition;
var overrideAll = require('../../plot_api/edit_types').overrideAll;
var templatedArray = require('../../plot_api/plot_template').templatedArray;

var fontAttr = fontAttrs({
    description: [
        'Sets the icon text font (color=mapbox.layer.paint.text-color, size=mapbox.layer.layout.text-size).',
        'Has an effect only when `type` is set to *symbol*.'
    ].join(' ')
});
fontAttr.family.dflt = 'Open Sans Regular, Arial Unicode MS Regular';

var attrs = module.exports = overrideAll({
    _arrayAttrRegexps: [Lib.counterRegex('mapbox', '.layers', true)],

    domain: domainAttrs({name: 'mapbox'}),

    accesstoken: {
        valType: 'string',
        noBlank: true,
        strict: true,
        role: 'info',
        description: [
            'Sets the mapbox access token to be used for this mapbox map.',
            'Alternatively, the mapbox access token can be set in the',
            'configuration options under `mapboxAccessToken`.'
        ].join(' ')
    },
    style: {
        valType: 'any',
        values: ['basic', 'streets', 'outdoors', 'light', 'dark', 'satellite', 'satellite-streets'],
        dflt: 'basic',
        role: 'style',
        description: [
            'Sets the Mapbox map style.',
            'Either input one of the default Mapbox style names or the URL to a custom style',
            'or a valid Mapbox style JSON.'
        ].join(' ')
    },

    center: {
        lon: {
            valType: 'number',
            dflt: 0,
            role: 'info',
            description: 'Sets the longitude of the center of the map (in degrees East).'
        },
        lat: {
            valType: 'number',
            dflt: 0,
            role: 'info',
            description: 'Sets the latitude of the center of the map (in degrees North).'
        }
    },
    zoom: {
        valType: 'number',
        dflt: 1,
        role: 'info',
        description: 'Sets the zoom level of the map (mapbox.zoom).'
    },
    bearing: {
        valType: 'number',
        dflt: 0,
        role: 'info',
        description: 'Sets the bearing angle of the map in degrees counter-clockwise from North (mapbox.bearing).'
    },
    pitch: {
        valType: 'number',
        dflt: 0,
        role: 'info',
        description: [
            'Sets the pitch angle of the map',
            '(in degrees, where *0* means perpendicular to the surface of the map) (mapbox.pitch).'
        ].join(' ')
    },

    layers: templatedArray('layer', {
        visible: {
            valType: 'boolean',
            role: 'info',
            dflt: true,
            description: [
                'Determines whether this layer is displayed'
            ].join(' ')
        },
        sourcetype: {
            valType: 'enumerated',
            values: ['geojson', 'vector'],
            dflt: 'geojson',
            role: 'info',
            description: [
                'Sets the source type for this layer.',
                'Support for *raster*, *image* and *video* source types is coming soon.'
            ].join(' ')
        },

        source: {
            valType: 'any',
            role: 'info',
            description: [
                'Sets the source data for this layer (mapbox.layer.source).',
                'Source can be either a URL,',
                'a geojson object (with `sourcetype` set to *geojson*)',
                'or an array of tile URLS (with `sourcetype` set to *vector*).'
            ].join(' ')
        },

        sourcelayer: {
            valType: 'string',
            dflt: '',
            role: 'info',
            description: [
                'Specifies the layer to use from a vector tile source (mapbox.layer.source-layer).',
                'Required for *vector* source type that supports multiple layers.'
            ].join(' ')
        },

        type: {
            valType: 'enumerated',
            values: ['circle', 'line', 'fill', 'symbol'],
            dflt: 'circle',
            role: 'info',
            description: [
                'Sets the layer type (mapbox.layer.type).',
                'Support for *raster*, *background* types is coming soon.',
                'Note that *line* and *fill* are not compatible with Point',
                'GeoJSON geometries.'
            ].join(' ')
        },

        // attributes shared between all types
        below: {
            valType: 'string',
            dflt: '',
            role: 'info',
            description: [
                'Determines if the layer will be inserted',
                'before the layer with the specified ID.',
                'If omitted or set to \'\',',
                'the layer will be inserted above every existing layer.'
            ].join(' ')
        },
        color: {
            valType: 'color',
            dflt: defaultLine,
            role: 'style',
            description: [
                'Sets the primary layer color.',
                'If `type` is *circle*, color corresponds to the circle color (mapbox.layer.paint.circle-color)',
                'If `type` is *line*, color corresponds to the line color (mapbox.layer.paint.line-color)',
                'If `type` is *fill*, color corresponds to the fill color (mapbox.layer.paint.fill-color)',
                'If `type` is *symbol*, color corresponds to the icon color (mapbox.layer.paint.icon-color)'
            ].join(' ')
        },
        opacity: {
            valType: 'number',
            min: 0,
            max: 1,
            dflt: 1,
            role: 'info',
            description: [
                'Sets the opacity of the layer.',
                'If `type` is *circle*, opacity corresponds to the circle opacity (mapbox.layer.paint.circle-opacity)',
                'If `type` is *line*, opacity corresponds to the line opacity (mapbox.layer.paint.line-opacity)',
                'If `type` is *fill*, opacity corresponds to the fill opacity (mapbox.layer.paint.fill-opacity)',
                'If `type` is *symbol*, opacity corresponds to the icon/text opacity (mapbox.layer.paint.text-opacity)'
            ].join(' ')
        },
        minzoom: {
            valType: 'number',
            min: 0,
            max: 24,
            dflt: 0,
            role: 'info',
            description: [
                'Sets the minimum zoom level (mapbox.layer.minzoom).',
                'At zoom levels less than the minzoom, the layer will be hidden.',
            ].join(' ')
        },
        maxzoom: {
            valType: 'number',
            min: 0,
            max: 24,
            dflt: 24,
            role: 'info',
            description: [
                'Sets the maximum zoom level (mapbox.layer.maxzoom).',
                'At zoom levels equal to or greater than the maxzoom, the layer will be hidden.'
            ].join(' ')
        },

        // type-specific style attributes
        circle: {
            radius: {
                valType: 'number',
                dflt: 15,
                role: 'style',
                description: [
                    'Sets the circle radius (mapbox.layer.paint.circle-radius).',
                    'Has an effect only when `type` is set to *circle*.'
                ].join(' ')
            }
        },

        line: {
            width: {
                valType: 'number',
                dflt: 2,
                role: 'style',
                description: [
                    'Sets the line width (mapbox.layer.paint.line-width).',
                    'Has an effect only when `type` is set to *line*.'
                ].join(' ')
            },
            dash: {
                valType: 'data_array',
                role: 'style',
                description: [
                    'Sets the length of dashes and gaps (mapbox.layer.paint.line-dasharray).',
                    'Has an effect only when `type` is set to *line*.'
                ].join(' ')
            }
        },

        fill: {
            outlinecolor: {
                valType: 'color',
                dflt: defaultLine,
                role: 'style',
                description: [
                    'Sets the fill outline color (mapbox.layer.paint.fill-outline-color).',
                    'Has an effect only when `type` is set to *fill*.'
                ].join(' ')
            }
        },

        symbol: {
            icon: {
                valType: 'string',
                dflt: 'marker',
                role: 'style',
                description: [
                    'Sets the symbol icon image (mapbox.layer.layout.icon-image).',
                    'Full list: https://www.mapbox.com/maki-icons/'
                ].join(' ')
            },
            iconsize: {
                valType: 'number',
                dflt: 10,
                role: 'style',
                description: [
                    'Sets the symbol icon size (mapbox.layer.layout.icon-size).',
                    'Has an effect only when `type` is set to *symbol*.'
                ].join(' ')
            },
            text: {
                valType: 'string',
                dflt: '',
                role: 'info',
                description: [
                    'Sets the symbol text (mapbox.layer.layout.text-field).'
                ].join(' ')
            },
            placement: {
                valType: 'enumerated',
                values: ['point', 'line', 'line-center'],
                dflt: 'point',
                role: 'info',
                description: [
                    'Sets the symbol and/or text placement (mapbox.layer.layout.symbol-placement).',
                    'If `placement` is *point*, the label is placed where the geometry is located',
                    'If `placement` is *line*, the label is placed along the line of the geometry',
                    'If `placement` is *line-center*, the label is placed on the center of the geometry',
                ].join(' ')
            },
            textfont: fontAttr,
            textposition: Lib.extendFlat({}, textposition, { arrayOk: false })
        }
    })
}, 'plot', 'from-root');

// set uirevision outside of overrideAll so it can be `editType: 'none'`
attrs.uirevision = {
    valType: 'any',
    role: 'info',
    editType: 'none',
    description: [
        'Controls persistence of user-driven changes in the view:',
        '`center`, `zoom`, `bearing`, `pitch`. Defaults to `layout.uirevision`.'
    ].join(' ')
};
