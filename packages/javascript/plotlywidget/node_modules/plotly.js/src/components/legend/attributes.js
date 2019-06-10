/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var fontAttrs = require('../../plots/font_attributes');
var colorAttrs = require('../color/attributes');


module.exports = {
    bgcolor: {
        valType: 'color',
        role: 'style',
        editType: 'legend',
        description: 'Sets the legend background color.'
    },
    bordercolor: {
        valType: 'color',
        dflt: colorAttrs.defaultLine,
        role: 'style',
        editType: 'legend',
        description: 'Sets the color of the border enclosing the legend.'
    },
    borderwidth: {
        valType: 'number',
        min: 0,
        dflt: 0,
        role: 'style',
        editType: 'legend',
        description: 'Sets the width (in px) of the border enclosing the legend.'
    },
    font: fontAttrs({
        editType: 'legend',
        description: 'Sets the font used to text the legend items.'
    }),
    orientation: {
        valType: 'enumerated',
        values: ['v', 'h'],
        dflt: 'v',
        role: 'info',
        editType: 'legend',
        description: 'Sets the orientation of the legend.'
    },
    traceorder: {
        valType: 'flaglist',
        flags: ['reversed', 'grouped'],
        extras: ['normal'],
        role: 'style',
        editType: 'legend',
        description: [
            'Determines the order at which the legend items are displayed.',

            'If *normal*, the items are displayed top-to-bottom in the same',
            'order as the input data.',

            'If *reversed*, the items are displayed in the opposite order',
            'as *normal*.',

            'If *grouped*, the items are displayed in groups',
            '(when a trace `legendgroup` is provided).',

            'if *grouped+reversed*, the items are displayed in the opposite order',
            'as *grouped*.'
        ].join(' ')
    },
    tracegroupgap: {
        valType: 'number',
        min: 0,
        dflt: 10,
        role: 'style',
        editType: 'legend',
        description: [
            'Sets the amount of vertical space (in px) between legend groups.'
        ].join(' ')
    },
    itemsizing: {
        valType: 'enumerated',
        values: ['trace', 'constant'],
        dflt: 'trace',
        role: 'style',
        editType: 'legend',
        description: [
            'Determines if the legend items symbols scale with their corresponding *trace* attributes',
            'or remain *constant* independent of the symbol size on the graph.'
        ].join(' ')
    },

    itemclick: {
        valType: 'enumerated',
        values: ['toggle', 'toggleothers', false],
        dflt: 'toggle',
        role: 'info',
        editType: 'legend',
        description: [
            'Determines the behavior on legend item click.',
            '*toggle* toggles the visibility of the item clicked on the graph.',
            '*toggleothers* makes the clicked item the sole visible item on the graph.',
            '*false* disable legend item click interactions.'
        ].join(' ')
    },
    itemdoubleclick: {
        valType: 'enumerated',
        values: ['toggle', 'toggleothers', false],
        dflt: 'toggleothers',
        role: 'info',
        editType: 'legend',
        description: [
            'Determines the behavior on legend item double-click.',
            '*toggle* toggles the visibility of the item clicked on the graph.',
            '*toggleothers* makes the clicked item the sole visible item on the graph.',
            '*false* disable legend item double-click interactions.'
        ].join(' ')
    },

    x: {
        valType: 'number',
        min: -2,
        max: 3,
        dflt: 1.02,
        role: 'style',
        editType: 'legend',
        description: 'Sets the x position (in normalized coordinates) of the legend.'
    },
    xanchor: {
        valType: 'enumerated',
        values: ['auto', 'left', 'center', 'right'],
        dflt: 'left',
        role: 'info',
        editType: 'legend',
        description: [
            'Sets the legend\'s horizontal position anchor.',
            'This anchor binds the `x` position to the *left*, *center*',
            'or *right* of the legend.'
        ].join(' ')
    },
    y: {
        valType: 'number',
        min: -2,
        max: 3,
        dflt: 1,
        role: 'style',
        editType: 'legend',
        description: 'Sets the y position (in normalized coordinates) of the legend.'
    },
    yanchor: {
        valType: 'enumerated',
        values: ['auto', 'top', 'middle', 'bottom'],
        dflt: 'auto',
        role: 'info',
        editType: 'legend',
        description: [
            'Sets the legend\'s vertical position anchor',
            'This anchor binds the `y` position to the *top*, *middle*',
            'or *bottom* of the legend.'
        ].join(' ')
    },
    uirevision: {
        valType: 'any',
        role: 'info',
        editType: 'none',
        description: [
            'Controls persistence of legend-driven changes in trace and pie label',
            'visibility. Defaults to `layout.uirevision`.'
        ].join(' ')
    },
    valign: {
        valType: 'enumerated',
        values: ['top', 'middle', 'bottom'],
        dflt: 'middle',
        role: 'style',
        editType: 'legend',
        description: [
            'Sets the vertical alignment of the symbols with respect to their associated text.',
        ].join(' ')
    },
    editType: 'legend'
};
