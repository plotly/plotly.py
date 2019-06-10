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

var extendFlat = require('../../lib/extend').extendFlat;

module.exports = extendFlat({
    z: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the z data.'
    },
    x: extendFlat({}, scatterAttrs.x, {impliedEdits: {xtype: 'array'}}),
    x0: extendFlat({}, scatterAttrs.x0, {impliedEdits: {xtype: 'scaled'}}),
    dx: extendFlat({}, scatterAttrs.dx, {impliedEdits: {xtype: 'scaled'}}),
    y: extendFlat({}, scatterAttrs.y, {impliedEdits: {ytype: 'array'}}),
    y0: extendFlat({}, scatterAttrs.y0, {impliedEdits: {ytype: 'scaled'}}),
    dy: extendFlat({}, scatterAttrs.dy, {impliedEdits: {ytype: 'scaled'}}),

    text: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the text elements associated with each z value.'
    },
    hovertext: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Same as `text`.'
    },
    transpose: {
        valType: 'boolean',
        dflt: false,
        role: 'info',
        editType: 'calc',
        description: 'Transposes the z data.'
    },
    xtype: {
        valType: 'enumerated',
        values: ['array', 'scaled'],
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: [
            'If *array*, the heatmap\'s x coordinates are given by *x*',
            '(the default behavior when `x` is provided).',
            'If *scaled*, the heatmap\'s x coordinates are given by *x0* and *dx*',
            '(the default behavior when `x` is not provided).'
        ].join(' ')
    },
    ytype: {
        valType: 'enumerated',
        values: ['array', 'scaled'],
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: [
            'If *array*, the heatmap\'s y coordinates are given by *y*',
            '(the default behavior when `y` is provided)',
            'If *scaled*, the heatmap\'s y coordinates are given by *y0* and *dy*',
            '(the default behavior when `y` is not provided)'
        ].join(' ')
    },
    zsmooth: {
        valType: 'enumerated',
        values: ['fast', 'best', false],
        dflt: false,
        role: 'style',
        editType: 'calc',
        description: [
            'Picks a smoothing algorithm use to smooth `z` data.'
        ].join(' ')
    },
    connectgaps: {
        valType: 'boolean',
        dflt: false,
        role: 'info',
        editType: 'calc',
        description: [
            'Determines whether or not gaps',
            '(i.e. {nan} or missing values)',
            'in the `z` data are filled in.'
        ].join(' ')
    },
    xgap: {
        valType: 'number',
        dflt: 0,
        min: 0,
        role: 'style',
        editType: 'plot',
        description: 'Sets the horizontal gap (in pixels) between bricks.'
    },
    ygap: {
        valType: 'number',
        dflt: 0,
        min: 0,
        role: 'style',
        editType: 'plot',
        description: 'Sets the vertical gap (in pixels) between bricks.'
    },
    zhoverformat: {
        valType: 'string',
        dflt: '',
        role: 'style',
        editType: 'none',
        description: [
            'Sets the hover text formatting rule using d3 formatting mini-languages',
            'which are very similar to those in Python. See:',
            'https://github.com/d3/d3-format/blob/master/README.md#locale_format'
        ].join(' ')
    },
    hovertemplate: hovertemplateAttrs()
}, {
    transforms: undefined
},
    colorScaleAttrs('', {cLetter: 'z', autoColorDflt: false})
);
