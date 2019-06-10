/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scatterAttrs = require('../scatter/attributes');
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var colorScaleAttrs = require('../../components/colorscale/attributes');
var fontAttrs = require('../../plots/font_attributes');
var constants = require('./constants.js');

var extendFlat = require('../../lib/extend').extendFlat;

var textFontAttrs = fontAttrs({
    editType: 'calc',
    arrayOk: true,
    colorEditType: 'style',
    description: ''
});

var scatterMarkerAttrs = scatterAttrs.marker;
var scatterMarkerLineAttrs = scatterMarkerAttrs.line;

var markerLineWidth = extendFlat({},
    scatterMarkerLineAttrs.width, { dflt: 0 });

var markerLine = extendFlat({
    width: markerLineWidth,
    editType: 'calc'
}, colorScaleAttrs('marker.line'));

var marker = extendFlat({
    line: markerLine,
    editType: 'calc'
}, colorScaleAttrs('marker'), {
    opacity: {
        valType: 'number',
        arrayOk: true,
        dflt: 1,
        min: 0,
        max: 1,
        role: 'style',
        editType: 'style',
        description: 'Sets the opacity of the bars.'
    }
});

module.exports = {
    x: scatterAttrs.x,
    x0: scatterAttrs.x0,
    dx: scatterAttrs.dx,
    y: scatterAttrs.y,
    y0: scatterAttrs.y0,
    dy: scatterAttrs.dy,

    text: scatterAttrs.text,
    hovertext: scatterAttrs.hovertext,
    hovertemplate: hovertemplateAttrs({}, {
        keys: constants.eventDataKeys
    }),

    textposition: {
        valType: 'enumerated',
        role: 'info',
        values: ['inside', 'outside', 'auto', 'none'],
        dflt: 'none',
        arrayOk: true,
        editType: 'calc',
        description: [
            'Specifies the location of the `text`.',
            '*inside* positions `text` inside, next to the bar end',
            '(rotated and scaled if needed).',
            '*outside* positions `text` outside, next to the bar end',
            '(scaled if needed), unless there is another bar stacked on',
            'this one, then the text gets pushed inside.',
            '*auto* tries to position `text` inside the bar, but if',
            'the bar is too small and no bar is stacked on this one',
            'the text is moved outside.'
        ].join(' ')
    },

    insidetextanchor: {
        valType: 'enumerated',
        values: ['end', 'middle', 'start'],
        dflt: 'end',
        role: 'info',
        editType: 'plot',
        description: [
            'Determines if texts are kept at center or start/end points in `textposition` *inside* mode.'
        ].join(' ')
    },

    textangle: {
        valType: 'angle',
        dflt: 'auto',
        role: 'info',
        editType: 'plot',
        description: [
            'Sets the angle of the tick labels with respect to the bar.',
            'For example, a `tickangle` of -90 draws the tick labels',
            'vertically. With *auto* the texts may automatically be',
            'rotated to fit with the maximum size in bars.'
        ].join(' ')
    },

    textfont: extendFlat({}, textFontAttrs, {
        description: 'Sets the font used for `text`.'
    }),

    insidetextfont: extendFlat({}, textFontAttrs, {
        description: 'Sets the font used for `text` lying inside the bar.'
    }),

    outsidetextfont: extendFlat({}, textFontAttrs, {
        description: 'Sets the font used for `text` lying outside the bar.'
    }),

    constraintext: {
        valType: 'enumerated',
        values: ['inside', 'outside', 'both', 'none'],
        role: 'info',
        dflt: 'both',
        editType: 'calc',
        description: [
            'Constrain the size of text inside or outside a bar to be no',
            'larger than the bar itself.'
        ].join(' ')
    },

    cliponaxis: extendFlat({}, scatterAttrs.cliponaxis, {
        description: [
            'Determines whether the text nodes',
            'are clipped about the subplot axes.',
            'To show the text nodes above axis lines and tick labels,',
            'make sure to set `xaxis.layer` and `yaxis.layer` to *below traces*.'
        ].join(' ')
    }),

    orientation: {
        valType: 'enumerated',
        role: 'info',
        values: ['v', 'h'],
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the orientation of the bars.',
            'With *v* (*h*), the value of the each bar spans',
            'along the vertical (horizontal).'
        ].join(' ')
    },

    base: {
        valType: 'any',
        dflt: null,
        arrayOk: true,
        role: 'info',
        editType: 'calc',
        description: [
            'Sets where the bar base is drawn (in position axis units).',
            'In *stack* or *relative* barmode,',
            'traces that set *base* will be excluded',
            'and drawn in *overlay* mode instead.'
        ].join(' ')
    },

    offset: {
        valType: 'number',
        dflt: null,
        arrayOk: true,
        role: 'info',
        editType: 'calc',
        description: [
            'Shifts the position where the bar is drawn',
            '(in position axis units).',
            'In *group* barmode,',
            'traces that set *offset* will be excluded',
            'and drawn in *overlay* mode instead.'
        ].join(' ')
    },

    width: {
        valType: 'number',
        dflt: null,
        min: 0,
        arrayOk: true,
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the bar width (in position axis units).'
        ].join(' ')
    },

    marker: marker,

    offsetgroup: {
        valType: 'string',
        role: 'info',
        dflt: '',
        editType: 'calc',
        description: [
            'Set several traces linked to the same position axis',
            'or matching axes to the same',
            'offsetgroup where bars of the same position coordinate will line up.'
        ].join(' ')
    },
    alignmentgroup: {
        valType: 'string',
        role: 'info',
        dflt: '',
        editType: 'calc',
        description: [
            'Set several traces linked to the same position axis',
            'or matching axes to the same',
            'alignmentgroup. This controls whether bars compute their positional',
            'range dependently or independently.'
        ].join(' ')
    },

    selected: {
        marker: {
            opacity: scatterAttrs.selected.marker.opacity,
            color: scatterAttrs.selected.marker.color,
            editType: 'style'
        },
        textfont: scatterAttrs.selected.textfont,
        editType: 'style'
    },
    unselected: {
        marker: {
            opacity: scatterAttrs.unselected.marker.opacity,
            color: scatterAttrs.unselected.marker.color,
            editType: 'style'
        },
        textfont: scatterAttrs.unselected.textfont,
        editType: 'style'
    },

    r: scatterAttrs.r,
    t: scatterAttrs.t,

    _deprecated: {
        bardir: {
            valType: 'enumerated',
            role: 'info',
            editType: 'calc',
            values: ['v', 'h'],
            description: 'Renamed to `orientation`.'
        }
    }
};
