/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var pieAttrs = require('../pie/attributes');
var plotAttrs = require('../../plots/attributes');
var domainAttrs = require('../../plots/domain').attributes;
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');

var extendFlat = require('../../lib/extend').extendFlat;

module.exports = {
    labels: pieAttrs.labels,
    // equivalent of x0 and dx, if label is missing
    label0: pieAttrs.label0,
    dlabel: pieAttrs.dlabel,
    values: pieAttrs.values,

    marker: {
        colors: pieAttrs.marker.colors,
        line: {
            color: extendFlat({}, pieAttrs.marker.line.color, {
                dflt: null,
                description: [
                    'Sets the color of the line enclosing each sector.',
                    'Defaults to the `paper_bgcolor` value.'
                ].join(' ')
            }),
            width: extendFlat({}, pieAttrs.marker.line.width, {dflt: 1}),
            editType: 'calc'
        },
        editType: 'calc'
    },

    text: pieAttrs.text,
    hovertext: pieAttrs.hovertext,

    scalegroup: extendFlat({}, pieAttrs.scalegroup, {
        description: [
            'If there are multiple funnelareas that should be sized according to',
            'their totals, link them by providing a non-empty group id here',
            'shared by every trace in the same group.'
        ].join(' ')
    }),

    textinfo: extendFlat({}, pieAttrs.textinfo, {
        flags: ['label', 'text', 'value', 'percent']
    }),

    hoverinfo: extendFlat({}, plotAttrs.hoverinfo, {
        flags: ['label', 'text', 'value', 'percent', 'name']
    }),

    hovertemplate: hovertemplateAttrs({}, {
        keys: ['label', 'color', 'value', 'percent', 'text']
    }),

    textposition: extendFlat({}, pieAttrs.textposition, {
        values: ['inside', 'none'],
        dflt: 'inside'
    }),

    textfont: pieAttrs.textfont,
    insidetextfont: pieAttrs.insidetextfont,

    title: {
        text: pieAttrs.title.text,
        font: pieAttrs.title.font,
        position: extendFlat({}, pieAttrs.title.position, {
            values: ['top left', 'top center', 'top right'],
            dflt: 'top center'
        }),
        editType: 'plot'
    },

    domain: domainAttrs({name: 'funnelarea', trace: true, editType: 'calc'}),

    aspectratio: {
        valType: 'number',
        role: 'info',
        min: 0,
        dflt: 1,
        editType: 'plot',
        description: [
            'Sets the ratio between height and width'
        ].join(' ')
    },

    baseratio: {
        valType: 'number',
        role: 'info',
        min: 0,
        max: 1,
        dflt: 0.333,
        editType: 'plot',
        description: [
            'Sets the ratio between bottom length and maximum top length.'
        ].join(' ')
    }
};
