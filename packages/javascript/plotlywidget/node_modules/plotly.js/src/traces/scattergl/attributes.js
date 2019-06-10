/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var plotAttrs = require('../../plots/attributes');
var scatterAttrs = require('../scatter/attributes');
var colorScaleAttrs = require('../../components/colorscale/attributes');

var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;
var DASHES = require('./constants').DASHES;

var scatterLineAttrs = scatterAttrs.line;
var scatterMarkerAttrs = scatterAttrs.marker;
var scatterMarkerLineAttrs = scatterMarkerAttrs.line;

var attrs = module.exports = overrideAll({
    x: scatterAttrs.x,
    x0: scatterAttrs.x0,
    dx: scatterAttrs.dx,
    y: scatterAttrs.y,
    y0: scatterAttrs.y0,
    dy: scatterAttrs.dy,

    text: scatterAttrs.text,
    hovertext: scatterAttrs.hovertext,

    textposition: scatterAttrs.textposition,
    textfont: scatterAttrs.textfont,

    mode: {
        valType: 'flaglist',
        flags: ['lines', 'markers', 'text'],
        extras: ['none'],
        role: 'info',
        description: [
            'Determines the drawing mode for this scatter trace.'
        ].join(' ')
    },
    line: {
        color: scatterLineAttrs.color,
        width: scatterLineAttrs.width,
        shape: {
            valType: 'enumerated',
            values: ['linear', 'hv', 'vh', 'hvh', 'vhv'],
            dflt: 'linear',
            role: 'style',
            editType: 'plot',
            description: [
                'Determines the line shape.',
                'The values correspond to step-wise line shapes.'
            ].join(' ')
        },
        dash: {
            valType: 'enumerated',
            values: Object.keys(DASHES),
            dflt: 'solid',
            role: 'style',
            description: 'Sets the style of the lines.'
        }
    },
    marker: extendFlat({}, colorScaleAttrs('marker'), {
        symbol: scatterMarkerAttrs.symbol,
        size: scatterMarkerAttrs.size,
        sizeref: scatterMarkerAttrs.sizeref,
        sizemin: scatterMarkerAttrs.sizemin,
        sizemode: scatterMarkerAttrs.sizemode,
        opacity: scatterMarkerAttrs.opacity,
        colorbar: scatterMarkerAttrs.colorbar,
        line: extendFlat({}, colorScaleAttrs('marker.line'), {
            width: scatterMarkerLineAttrs.width
        })
    }),
    connectgaps: scatterAttrs.connectgaps,
    fill: extendFlat({}, scatterAttrs.fill, {dflt: 'none'}),
    fillcolor: scatterAttrs.fillcolor,

    // no hoveron

    selected: {
        marker: scatterAttrs.selected.marker,
        textfont: scatterAttrs.selected.textfont
    },
    unselected: {
        marker: scatterAttrs.unselected.marker,
        textfont: scatterAttrs.unselected.textfont
    },

    opacity: plotAttrs.opacity

}, 'calc', 'nested');

attrs.x.editType = attrs.y.editType = attrs.x0.editType = attrs.y0.editType = 'calc+clearAxisTypes';
attrs.hovertemplate = scatterAttrs.hovertemplate;
