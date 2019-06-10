/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var fontAttrs = require('../../plots/font_attributes');
var plotAttrs = require('../../plots/attributes');
var colorAttrs = require('../../components/color/attributes');
var fxAttrs = require('../../components/fx/attributes');
var domainAttrs = require('../../plots/domain').attributes;
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var colorAttributes = require('../../components/colorscale/attributes');
var templatedArray = require('../../plot_api/plot_template').templatedArray;

var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var attrs = module.exports = overrideAll({
    hoverinfo: extendFlat({}, plotAttrs.hoverinfo, {
        flags: [],
        arrayOk: false,
        description: [
            'Determines which trace information appear on hover.',
            'If `none` or `skip` are set, no information is displayed upon hovering.',
            'But, if `none` is set, click and hover events are still fired.',
            'Note that this attribute is superseded by `node.hoverinfo` and `node.hoverinfo`',
            'for nodes and links respectively.'
        ].join(' ')
    }),
    hoverlabel: fxAttrs.hoverlabel,
    domain: domainAttrs({name: 'sankey', trace: true}),

    orientation: {
        valType: 'enumerated',
        values: ['v', 'h'],
        dflt: 'h',
        role: 'style',
        description: 'Sets the orientation of the Sankey diagram.'
    },

    valueformat: {
        valType: 'string',
        dflt: '.3s',
        role: 'style',
        description: [
            'Sets the value formatting rule using d3 formatting mini-language',
            'which is similar to those of Python. See',
            'https://github.com/d3/d3-format/blob/master/README.md#locale_format'
        ].join(' ')
    },

    valuesuffix: {
        valType: 'string',
        dflt: '',
        role: 'style',
        description: [
            'Adds a unit to follow the value in the hover tooltip. Add a space if a separation',
            'is necessary from the value.'
        ].join(' ')
    },

    arrangement: {
        valType: 'enumerated',
        values: ['snap', 'perpendicular', 'freeform', 'fixed'],
        dflt: 'snap',
        role: 'style',
        description: [
            'If value is `snap` (the default), the node arrangement is assisted by automatic snapping of elements to',
            'preserve space between nodes specified via `nodepad`.',
            'If value is `perpendicular`, the nodes can only move along a line perpendicular to the flow.',
            'If value is `freeform`, the nodes can freely move on the plane.',
            'If value is `fixed`, the nodes are stationary.'
        ].join(' ')
    },

    textfont: fontAttrs({
        description: 'Sets the font for node labels'
    }),

    node: {
        label: {
            valType: 'data_array',
            dflt: [],
            role: 'info',
            description: 'The shown name of the node.'
        },
        groups: {
            valType: 'info_array',
            impliedEdits: {'x': [], 'y': []},
            dimensions: 2,
            freeLength: true,
            dflt: [],
            items: {valType: 'number', editType: 'calc'},
            role: 'info',
            description: [
                'Groups of nodes.',
                'Each group is defined by an array with the indices of the nodes it contains.',
                'Multiple groups can be specified.'
            ].join(' ')
        },
        x: {
            valType: 'data_array',
            dflt: [],
            role: 'info',
            description: 'The normalized horizontal position of the node.'
        },
        y: {
            valType: 'data_array',
            dflt: [],
            role: 'info',
            description: 'The normalized vertical position of the node.'
        },
        color: {
            valType: 'color',
            role: 'style',
            arrayOk: true,
            description: [
                'Sets the `node` color. It can be a single value, or an array for specifying color for each `node`.',
                'If `node.color` is omitted, then the default `Plotly` color palette will be cycled through',
                'to have a variety of colors. These defaults are not fully opaque, to allow some visibility of',
                'what is beneath the node.'
            ].join(' ')
        },
        line: {
            color: {
                valType: 'color',
                role: 'style',
                dflt: colorAttrs.defaultLine,
                arrayOk: true,
                description: [
                    'Sets the color of the `line` around each `node`.'
                ].join(' ')
            },
            width: {
                valType: 'number',
                role: 'style',
                min: 0,
                dflt: 0.5,
                arrayOk: true,
                description: [
                    'Sets the width (in px) of the `line` around each `node`.'
                ].join(' ')
            }
        },
        pad: {
            valType: 'number',
            arrayOk: false,
            min: 0,
            dflt: 20,
            role: 'style',
            description: 'Sets the padding (in px) between the `nodes`.'
        },
        thickness: {
            valType: 'number',
            arrayOk: false,
            min: 1,
            dflt: 20,
            role: 'style',
            description: 'Sets the thickness (in px) of the `nodes`.'
        },
        hoverinfo: {
            valType: 'enumerated',
            values: ['all', 'none', 'skip'],
            dflt: 'all',
            role: 'info',
            description: [
                'Determines which trace information appear when hovering nodes.',
                'If `none` or `skip` are set, no information is displayed upon hovering.',
                'But, if `none` is set, click and hover events are still fired.'
            ].join(' ')
        },
        hoverlabel: fxAttrs.hoverlabel, // needs editType override,
        hovertemplate: hovertemplateAttrs({}, {
            description: 'Variables `sourceLinks` and `targetLinks` are arrays of link objects.',
            keys: ['value', 'label']
        }),
        description: 'The nodes of the Sankey plot.'
    },

    link: {
        label: {
            valType: 'data_array',
            dflt: [],
            role: 'info',
            description: 'The shown name of the link.'
        },
        color: {
            valType: 'color',
            role: 'style',
            arrayOk: true,
            description: [
                'Sets the `link` color. It can be a single value, or an array for specifying color for each `link`.',
                'If `link.color` is omitted, then by default, a translucent grey link will be used.'
            ].join(' ')
        },
        line: {
            color: {
                valType: 'color',
                role: 'style',
                dflt: colorAttrs.defaultLine,
                arrayOk: true,
                description: [
                    'Sets the color of the `line` around each `link`.'
                ].join(' ')
            },
            width: {
                valType: 'number',
                role: 'style',
                min: 0,
                dflt: 0,
                arrayOk: true,
                description: [
                    'Sets the width (in px) of the `line` around each `link`.'
                ].join(' ')
            }
        },
        source: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            description: 'An integer number `[0..nodes.length - 1]` that represents the source node.'
        },
        target: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            description: 'An integer number `[0..nodes.length - 1]` that represents the target node.'
        },
        value: {
            valType: 'data_array',
            dflt: [],
            role: 'info',
            description: 'A numeric value representing the flow volume value.'
        },
        hoverinfo: {
            valType: 'enumerated',
            values: ['all', 'none', 'skip'],
            dflt: 'all',
            role: 'info',
            description: [
                'Determines which trace information appear when hovering links.',
                'If `none` or `skip` are set, no information is displayed upon hovering.',
                'But, if `none` is set, click and hover events are still fired.'
            ].join(' ')
        },
        hoverlabel: fxAttrs.hoverlabel, // needs editType override,
        hovertemplate: hovertemplateAttrs({}, {
            description: 'Variables `source` and `target` are node objects.',
            keys: ['value', 'label']
        }),
        colorscales: templatedArray('concentrationscales', {
            editType: 'calc',
            label: {
                valType: 'string',
                role: 'info',
                editType: 'calc',
                description: 'The label of the links to color based on their concentration within a flow.',
                dflt: ''
            },
            cmax: {
                valType: 'number',
                role: 'info',
                editType: 'calc',
                dflt: 1,
                description: [
                    'Sets the upper bound of the color domain.'
                ].join('')
            },
            cmin: {
                valType: 'number',
                role: 'info',
                editType: 'calc',
                dflt: 0,
                description: [
                    'Sets the lower bound of the color domain.'
                ].join('')
            },
            colorscale: extendFlat(colorAttributes().colorscale, {dflt: [[0, 'white'], [1, 'black']]})
        }),
        description: 'The links of the Sankey plot.',
        role: 'info'
    }
}, 'calc', 'nested');
attrs.transforms = undefined;
