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
var colorScaleAttrs = require('../../components/colorscale/attributes');
var dash = require('../../components/drawing/attributes').dash;

var extendFlat = require('../../lib/extend').extendFlat;

var scatterMarkerAttrs = scatterAttrs.marker;
var scatterLineAttrs = scatterAttrs.line;
var scatterMarkerLineAttrs = scatterMarkerAttrs.line;

module.exports = {
    a: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the quantity of component `a` in each data point.',
            'If `a`, `b`, and `c` are all provided, they need not be',
            'normalized, only the relative values matter. If only two',
            'arrays are provided they must be normalized to match',
            '`ternary<i>.sum`.'
        ].join(' ')
    },
    b: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the quantity of component `a` in each data point.',
            'If `a`, `b`, and `c` are all provided, they need not be',
            'normalized, only the relative values matter. If only two',
            'arrays are provided they must be normalized to match',
            '`ternary<i>.sum`.'
        ].join(' ')
    },
    c: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the quantity of component `a` in each data point.',
            'If `a`, `b`, and `c` are all provided, they need not be',
            'normalized, only the relative values matter. If only two',
            'arrays are provided they must be normalized to match',
            '`ternary<i>.sum`.'
        ].join(' ')
    },
    sum: {
        valType: 'number',
        role: 'info',
        dflt: 0,
        min: 0,
        editType: 'calc',
        description: [
            'The number each triplet should sum to,',
            'if only two of `a`, `b`, and `c` are provided.',
            'This overrides `ternary<i>.sum` to normalize this specific',
            'trace, but does not affect the values displayed on the axes.',
            '0 (or missing) means to use ternary<i>.sum'
        ].join(' ')
    },
    mode: extendFlat({}, scatterAttrs.mode, {dflt: 'markers'}),
    text: extendFlat({}, scatterAttrs.text, {
        description: [
            'Sets text elements associated with each (a,b,c) point.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of strings, the items are mapped in order to the',
            'the data points in (a,b,c).',
            'If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,',
            'these elements will be seen in the hover labels.'
        ].join(' ')
    }),
    hovertext: extendFlat({}, scatterAttrs.hovertext, {
        description: [
            'Sets hover text elements associated with each (a,b,c) point.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of strings, the items are mapped in order to the',
            'the data points in (a,b,c).',
            'To be seen, trace `hoverinfo` must contain a *text* flag.'
        ].join(' ')
    }),
    line: {
        color: scatterLineAttrs.color,
        width: scatterLineAttrs.width,
        dash: dash,
        shape: extendFlat({}, scatterLineAttrs.shape,
            {values: ['linear', 'spline']}),
        smoothing: scatterLineAttrs.smoothing,
        editType: 'calc'
    },
    connectgaps: scatterAttrs.connectgaps,
    cliponaxis: scatterAttrs.cliponaxis,
    fill: extendFlat({}, scatterAttrs.fill, {
        values: ['none', 'toself', 'tonext'],
        dflt: 'none',
        description: [
            'Sets the area to fill with a solid color.',
            'Use with `fillcolor` if not *none*.',
            'scatterternary has a subset of the options available to scatter.',
            '*toself* connects the endpoints of the trace (or each segment',
            'of the trace if it has gaps) into a closed shape.',
            '*tonext* fills the space between two traces if one completely',
            'encloses the other (eg consecutive contour lines), and behaves like',
            '*toself* if there is no trace before it. *tonext* should not be',
            'used if one trace does not enclose the other.'
        ].join(' ')
    }),
    fillcolor: scatterAttrs.fillcolor,
    marker: extendFlat({
        symbol: scatterMarkerAttrs.symbol,
        opacity: scatterMarkerAttrs.opacity,
        maxdisplayed: scatterMarkerAttrs.maxdisplayed,
        size: scatterMarkerAttrs.size,
        sizeref: scatterMarkerAttrs.sizeref,
        sizemin: scatterMarkerAttrs.sizemin,
        sizemode: scatterMarkerAttrs.sizemode,
        line: extendFlat({
            width: scatterMarkerLineAttrs.width,
            editType: 'calc'
        },
            colorScaleAttrs('marker.line')
        ),
        gradient: scatterMarkerAttrs.gradient,
        editType: 'calc'
    },
        colorScaleAttrs('marker')
    ),

    textfont: scatterAttrs.textfont,
    textposition: scatterAttrs.textposition,

    selected: scatterAttrs.selected,
    unselected: scatterAttrs.unselected,

    hoverinfo: extendFlat({}, plotAttrs.hoverinfo, {
        flags: ['a', 'b', 'c', 'text', 'name']
    }),
    hoveron: scatterAttrs.hoveron,
    hovertemplate: hovertemplateAttrs(),
};
