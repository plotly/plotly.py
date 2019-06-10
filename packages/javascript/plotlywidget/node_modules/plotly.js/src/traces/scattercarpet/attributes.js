/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scatterAttrs = require('../scatter/attributes');
var plotAttrs = require('../../plots/attributes');
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var colorScaleAttrs = require('../../components/colorscale/attributes');

var extendFlat = require('../../lib/extend').extendFlat;

var scatterMarkerAttrs = scatterAttrs.marker;
var scatterLineAttrs = scatterAttrs.line;
var scatterMarkerLineAttrs = scatterMarkerAttrs.line;

module.exports = {
    carpet: {
        valType: 'string',
        role: 'info',
        editType: 'calc',
        description: [
            'An identifier for this carpet, so that `scattercarpet` and',
            '`scattercontour` traces can specify a carpet plot on which',
            'they lie'
        ].join(' ')
    },
    a: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the a-axis coordinates.'
    },
    b: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the b-axis coordinates.'
    },
    mode: extendFlat({}, scatterAttrs.mode, {dflt: 'markers'}),
    text: extendFlat({}, scatterAttrs.text, {
        description: [
            'Sets text elements associated with each (a,b) point.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of strings, the items are mapped in order to the',
            'the data points in (a,b).',
            'If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,',
            'these elements will be seen in the hover labels.'
        ].join(' ')
    }),
    hovertext: extendFlat({}, scatterAttrs.hovertext, {
        description: [
            'Sets hover text elements associated with each (a,b) point.',
            'If a single string, the same string appears over',
            'all the data points.',
            'If an array of strings, the items are mapped in order to the',
            'the data points in (a,b).',
            'To be seen, trace `hoverinfo` must contain a *text* flag.'
        ].join(' ')
    }),
    line: {
        color: scatterLineAttrs.color,
        width: scatterLineAttrs.width,
        dash: scatterLineAttrs.dash,
        shape: extendFlat({}, scatterLineAttrs.shape,
            {values: ['linear', 'spline']}),
        smoothing: scatterLineAttrs.smoothing,
        editType: 'calc'
    },
    connectgaps: scatterAttrs.connectgaps,
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
        flags: ['a', 'b', 'text', 'name']
    }),
    hoveron: scatterAttrs.hoveron,
    hovertemplate: hovertemplateAttrs()
};
