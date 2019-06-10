/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorScaleAttrs = require('../../components/colorscale/attributes');
var axesAttrs = require('../../plots/cartesian/layout_attributes');
var fontAttrs = require('../../plots/font_attributes');
var domainAttrs = require('../../plots/domain').attributes;

var extendFlat = require('../../lib/extend').extendFlat;
var templatedArray = require('../../plot_api/plot_template').templatedArray;

module.exports = {
    domain: domainAttrs({name: 'parcoords', trace: true, editType: 'calc'}),

    labelfont: fontAttrs({
        editType: 'calc',
        description: 'Sets the font for the `dimension` labels.'
    }),
    tickfont: fontAttrs({
        editType: 'calc',
        description: 'Sets the font for the `dimension` tick values.'
    }),
    rangefont: fontAttrs({
        editType: 'calc',
        description: 'Sets the font for the `dimension` range values.'
    }),

    dimensions: templatedArray('dimension', {
        label: {
            valType: 'string',
            role: 'info',
            editType: 'calc',
            description: 'The shown name of the dimension.'
        },
        // TODO: better way to determine ordinal vs continuous axes,
        // so users can use tickvals/ticktext with a continuous axis.
        tickvals: extendFlat({}, axesAttrs.tickvals, {editType: 'calc'}),
        ticktext: extendFlat({}, axesAttrs.ticktext, {editType: 'calc'}),
        tickformat: {
            valType: 'string',
            dflt: '3s',
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the tick label formatting rule using d3 formatting mini-language',
                'which is similar to those of Python. See',
                'https://github.com/d3/d3-format/blob/master/README.md#locale_format'
            ].join(' ')
        },
        visible: {
            valType: 'boolean',
            dflt: true,
            role: 'info',
            editType: 'calc',
            description: 'Shows the dimension when set to `true` (the default). Hides the dimension for `false`.'
        },
        range: {
            valType: 'info_array',
            role: 'info',
            items: [
                {valType: 'number', editType: 'calc'},
                {valType: 'number', editType: 'calc'}
            ],
            editType: 'calc',
            description: [
                'The domain range that represents the full, shown axis extent. Defaults to the `values` extent.',
                'Must be an array of `[fromValue, toValue]` with finite numbers as elements.'
            ].join(' ')
        },
        constraintrange: {
            valType: 'info_array',
            role: 'info',
            freeLength: true,
            dimensions: '1-2',
            items: [
                {valType: 'number', editType: 'calc'},
                {valType: 'number', editType: 'calc'}
            ],
            editType: 'calc',
            description: [
                'The domain range to which the filter on the dimension is constrained. Must be an array',
                'of `[fromValue, toValue]` with `fromValue <= toValue`, or if `multiselect` is not',
                'disabled, you may give an array of arrays, where each inner array is `[fromValue, toValue]`.'
            ].join(' ')
        },
        multiselect: {
            valType: 'boolean',
            dflt: true,
            role: 'info',
            editType: 'calc',
            description: 'Do we allow multiple selection ranges or just a single range?'
        },
        values: {
            valType: 'data_array',
            role: 'info',
            editType: 'calc',
            description: [
                'Dimension values. `values[n]` represents the value of the `n`th point in the dataset,',
                'therefore the `values` vector for all dimensions must be the same (longer vectors',
                'will be truncated). Each value must be a finite number.'
            ].join(' ')
        },
        editType: 'calc',
        description: 'The dimensions (variables) of the parallel coordinates chart. 2..60 dimensions are supported.'
    }),

    line: extendFlat({editType: 'calc'},
        colorScaleAttrs('line', {
            // the default autocolorscale isn't quite usable for parcoords due to context ambiguity around 0 (grey, off-white)
            // autocolorscale therefore defaults to false too, to avoid being overridden by the blue-white-red autocolor palette
            colorscaleDflt: 'Viridis',
            autoColorDflt: false,
            editTypeOverride: 'calc'
        })
    )
};
