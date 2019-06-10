/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var plotAttrs = require('../../plots/attributes');
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var domainAttrs = require('../../plots/domain').attributes;
var pieAtts = require('../pie/attributes');

var extendFlat = require('../../lib/extend').extendFlat;

module.exports = {
    labels: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the labels of each of the sunburst sectors.'
        ].join(' ')
    },
    parents: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the parent sectors for each of the sunburst sectors.',
            'Empty string items \'\' are understood to reference',
            'the root node in the hierarchy.',
            'If `ids` is filled, `parents` items are understood to be "ids" themselves.',
            'When `ids` is not set, plotly attempts to find matching items in `labels`,',
            'but beware they must be unique.'
        ].join(' ')
    },

    values: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the values associated with each of the sunburst sectors.',
            'Use with `branchvalues` to determine how the values are summed.'
        ].join(' ')
    },
    branchvalues: {
        valType: 'enumerated',
        values: ['remainder', 'total'],
        dflt: 'remainder',
        editType: 'calc',
        role: 'info',
        description: [
            'Determines how the items in `values` are summed.',
            'When set to *total*, items in `values` are taken to be value of all its descendants.',
            'When set to *remainder*, items in `values` corresponding to the root and the branches sectors',
            'are taken to be the extra part not part of the sum of the values at their leaves.'
        ].join(' ')
    },

    level: {
        valType: 'any',
        editType: 'plot',
        anim: true,
        role: 'info',
        description: [
            'Sets the level from which this sunburst trace hierarchy is rendered.',
            'Set `level` to `\'\'` to start the sunburst from the root node in the hierarchy.',
            'Must be an "id" if `ids` is filled in, otherwise plotly attempts to find a matching',
            'item in `labels`.'
        ].join(' ')
    },
    maxdepth: {
        valType: 'integer',
        editType: 'plot',
        role: 'info',
        dflt: -1,
        description: [
            'Sets the number of rendered sunburst rings from any given `level`.',
            'Set `maxdepth` to *-1* to render all the levels in the hierarchy.'
        ].join(' ')
    },

    marker: {
        colors: {
            valType: 'data_array',
            editType: 'calc',
            description: [
                'Sets the color of each sector of this sunburst chart.',
                'If not specified, the default trace color set is used',
                'to pick the sector colors.'
            ].join(' ')
        },

        // colorinheritance: {
        //     valType: 'enumerated',
        //     values: ['per-branch', 'per-label', false]
        // },

        line: {
            color: extendFlat({}, pieAtts.marker.line.color, {
                dflt: null,
                description: [
                    'Sets the color of the line enclosing each sector.',
                    'Defaults to the `paper_bgcolor` value.'
                ].join(' ')
            }),
            width: extendFlat({}, pieAtts.marker.line.width, {dflt: 1}),
            editType: 'calc'
        },
        editType: 'calc'
    },

    leaf: {
        opacity: {
            valType: 'number',
            editType: 'style',
            role: 'style',
            min: 0,
            max: 1,
            dflt: 0.7,
            description: 'Sets the opacity of the leaves.'
        },
        editType: 'plot'
    },

    text: pieAtts.text,
    textinfo: extendFlat({}, pieAtts.textinfo, {
        editType: 'plot',
        flags: ['label', 'text', 'value']
    }),
    textfont: pieAtts.textfont,

    hovertext: pieAtts.hovertext,
    hoverinfo: extendFlat({}, plotAttrs.hoverinfo, {
        flags: ['label', 'text', 'value', 'name']
    }),
    hovertemplate: hovertemplateAttrs(),

    insidetextfont: pieAtts.insidetextfont,
    outsidetextfont: pieAtts.outsidetextfont,

    domain: domainAttrs({name: 'sunburst', trace: true, editType: 'calc'})
};
