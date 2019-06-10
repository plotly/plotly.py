/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var extendFlat = require('../../lib/extend').extendFlat;
var plotAttrs = require('../../plots/attributes');
var fontAttrs = require('../../plots/font_attributes');
var colorScaleAttrs = require('../../components/colorscale/attributes');
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var domainAttrs = require('../../plots/domain').attributes;

var line = extendFlat(
    {editType: 'calc'},
    colorScaleAttrs('line', {editTypeOverride: 'calc'}),
    {
        shape: {
            valType: 'enumerated',
            values: ['linear', 'hspline'],
            dflt: 'linear',
            role: 'info',
            editType: 'plot',
            description: [
                'Sets the shape of the paths.',
                'If `linear`, paths are composed of straight lines.',
                'If `hspline`, paths are composed of horizontal curved splines'
            ].join(' ')
        },

        hovertemplate: hovertemplateAttrs({
            editType: 'plot',
            arrayOk: false
        }, {
            keys: ['count', 'probability'],
            description: [
                'This value here applies when hovering over lines.'
            ].join(' ')
        })
    }
);

module.exports = {
    domain: domainAttrs({name: 'parcats', trace: true, editType: 'calc'}),

    hoverinfo: extendFlat({}, plotAttrs.hoverinfo, {
        flags: ['count', 'probability'],
        editType: 'plot',
        arrayOk: false
    }),
    hoveron: {
        valType: 'enumerated',
        values: ['category', 'color', 'dimension'],
        dflt: 'category',
        role: 'info',
        editType: 'plot',
        description: [
            'Sets the hover interaction mode for the parcats diagram.',
            'If `category`, hover interaction take place per category.',
            'If `color`, hover interactions take place per color per category.',
            'If `dimension`, hover interactions take place across all categories per dimension.'
        ].join(' ')
    },
    hovertemplate: hovertemplateAttrs({
        editType: 'plot',
        arrayOk: false
    }, {
        keys: [
            'count', 'probability', 'category',
            'categorycount', 'colorcount', 'bandcolorcount'
        ],
        description: [
            'This value here applies when hovering over dimensions.',
            'Note tath `*categorycount`, *colorcount* and *bandcolorcount*',
            'are only available when `hoveron` contains the *color* flag'
        ].join(' ')
    }),

    arrangement: {
        valType: 'enumerated',
        values: ['perpendicular', 'freeform', 'fixed'],
        dflt: 'perpendicular',
        role: 'style',
        editType: 'plot',
        description: [
            'Sets the drag interaction mode for categories and dimensions.',
            'If `perpendicular`, the categories can only move along a line perpendicular to the paths.',
            'If `freeform`, the categories can freely move on the plane.',
            'If `fixed`, the categories and dimensions are stationary.'
        ].join(' ')
    },
    bundlecolors: {
        valType: 'boolean',
        dflt: true,
        role: 'info',
        editType: 'plot',
        description: 'Sort paths so that like colors are bundled together within each category.'
    },
    sortpaths: {
        valType: 'enumerated',
        values: ['forward', 'backward'],
        dflt: 'forward',
        role: 'info',
        editType: 'plot',
        description: [
            'Sets the path sorting algorithm.',
            'If `forward`, sort paths based on dimension categories from left to right.',
            'If `backward`, sort paths based on dimensions categories from right to left.'
        ].join(' ')
    },
    labelfont: fontAttrs({
        editType: 'calc',
        description: 'Sets the font for the `dimension` labels.'
    }),

    tickfont: fontAttrs({
        editType: 'calc',
        description: 'Sets the font for the `category` labels.'
    }),

    dimensions: {
        _isLinkedToArray: 'dimension',
        label: {
            valType: 'string',
            role: 'info',
            editType: 'calc',
            description: 'The shown name of the dimension.'
        },
        categoryorder: {
            valType: 'enumerated',
            values: [
                'trace', 'category ascending', 'category descending', 'array'
            ],
            dflt: 'trace',
            role: 'info',
            editType: 'calc',
            description: [
                'Specifies the ordering logic for the categories in the dimension.',
                'By default, plotly uses *trace*, which specifies the order that is present in the data supplied.',
                'Set `categoryorder` to *category ascending* or *category descending* if order should be determined by',
                'the alphanumerical order of the category names.',
                'Set `categoryorder` to *array* to derive the ordering from the attribute `categoryarray`. If a category',
                'is not found in the `categoryarray` array, the sorting behavior for that attribute will be identical to',
                'the *trace* mode. The unspecified categories will follow the categories in `categoryarray`.'
            ].join(' ')
        },
        categoryarray: {
            valType: 'data_array',
            role: 'info',
            editType: 'calc',
            description: [
                'Sets the order in which categories in this dimension appear.',
                'Only has an effect if `categoryorder` is set to *array*.',
                'Used with `categoryorder`.'
            ].join(' ')
        },
        ticktext: {
            valType: 'data_array',
            role: 'info',
            editType: 'calc',
            description: [
                'Sets alternative tick labels for the categories in this dimension.',
                'Only has an effect if `categoryorder` is set to *array*.',
                'Should be an array the same length as `categoryarray`',
                'Used with `categoryorder`.'
            ].join(' ')
        },
        values: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            editType: 'calc',
            description: [
                'Dimension values. `values[n]` represents the category value of the `n`th point in the dataset,',
                'therefore the `values` vector for all dimensions must be the same (longer vectors',
                'will be truncated).'
            ].join(' ')
        },
        displayindex: {
            valType: 'integer',
            role: 'info',
            editType: 'calc',
            description: [
                'The display index of dimension, from left to right, zero indexed, defaults to dimension',
                'index.'
            ].join(' ')
        },
        editType: 'calc',
        description: 'The dimensions (variables) of the parallel categories diagram.',
        visible: {
            valType: 'boolean',
            dflt: true,
            role: 'info',
            editType: 'calc',
            description: 'Shows the dimension when set to `true` (the default). Hides the dimension for `false`.'
        }
    },

    line: line,
    counts: {
        valType: 'number',
        min: 0,
        dflt: 1,
        arrayOk: true,
        role: 'info',
        editType: 'calc',
        description: [
            'The number of observations represented by each state. Defaults to 1 so that each state represents',
            'one observation'
        ].join(' ')
    },

    // Hide unsupported top-level properties from plot-schema
    customdata: undefined,
    hoverlabel: undefined,
    ids: undefined,
    legendgroup: undefined,
    opacity: undefined,
    selectedpoints: undefined,
    showlegend: undefined
};
