/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var annAttrs = require('../../components/annotations/attributes');
var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;
var fontAttrs = require('../../plots/font_attributes');
var domainAttrs = require('../../plots/domain').attributes;

var attrs = module.exports = overrideAll({
    domain: domainAttrs({name: 'table', trace: true}),

    columnwidth: {
        valType: 'number',
        arrayOk: true,
        dflt: null,
        role: 'style',
        description: [
            'The width of columns expressed as a ratio. Columns fill the available width',
            'in proportion of their specified column widths.'
        ].join(' ')
    },

    columnorder: {
        valType: 'data_array',
        role: 'info',
        description: [
            'Specifies the rendered order of the data columns; for example, a value `2` at position `0`',
            'means that column index `0` in the data will be rendered as the',
            'third column, as columns have an index base of zero.'
        ].join(' ')
    },

    header: {

        values: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            description: [
                'Header cell values. `values[m][n]` represents the value of the `n`th point in column `m`,',
                'therefore the `values[m]` vector length for all columns must be the same (longer vectors',
                'will be truncated). Each value must be a finite number or a string.'
            ].join(' ')
        },

        format: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            description: [
                'Sets the cell value formatting rule using d3 formatting mini-language',
                'which is similar to those of Python. See',
                'https://github.com/d3/d3-format/blob/master/README.md#locale_format'
            ].join(' ')
        },

        prefix: {
            valType: 'string',
            arrayOk: true,
            dflt: null,
            role: 'style',
            description: 'Prefix for cell values.'
        },

        suffix: {
            valType: 'string',
            arrayOk: true,
            dflt: null,
            role: 'style',
            description: 'Suffix for cell values.'
        },

        height: {
            valType: 'number',
            dflt: 28,
            role: 'style',
            description: 'The height of cells.'
        },

        align: extendFlat({}, annAttrs.align, {arrayOk: true}),

        line: {
            width: {
                valType: 'number',
                arrayOk: true,
                dflt: 1,
                role: 'style'
            },
            color: {
                valType: 'color',
                arrayOk: true,
                dflt: 'grey',
                role: 'style'
            }
        },

        fill: {
            color: {
                valType: 'color',
                arrayOk: true,
                dflt: 'white',
                role: 'style',
                description: [
                    'Sets the cell fill color. It accepts either a specific color',
                    ' or an array of colors or a 2D array of colors.'
                ].join('')
            }
        },

        font: extendFlat({}, fontAttrs({arrayOk: true}))
    },

    cells: {

        values: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            description: [
                'Cell values. `values[m][n]` represents the value of the `n`th point in column `m`,',
                'therefore the `values[m]` vector length for all columns must be the same (longer vectors',
                'will be truncated). Each value must be a finite number or a string.'
            ].join(' ')
        },

        format: {
            valType: 'data_array',
            role: 'info',
            dflt: [],
            description: [
                'Sets the cell value formatting rule using d3 formatting mini-language',
                'which is similar to those of Python. See',
                'https://github.com/d3/d3-format/blob/master/README.md#locale_format'
            ].join(' ')
        },

        prefix: {
            valType: 'string',
            arrayOk: true,
            dflt: null,
            role: 'style',
            description: 'Prefix for cell values.'
        },

        suffix: {
            valType: 'string',
            arrayOk: true,
            dflt: null,
            role: 'style',
            description: 'Suffix for cell values.'
        },

        height: {
            valType: 'number',
            dflt: 20,
            role: 'style',
            description: 'The height of cells.'
        },

        align: extendFlat({}, annAttrs.align, {arrayOk: true}),

        line: {
            width: {
                valType: 'number',
                arrayOk: true,
                dflt: 1,
                role: 'style'
            },
            color: {
                valType: 'color',
                arrayOk: true,
                dflt: 'grey',
                role: 'style'
            }
        },

        fill: {
            color: {
                valType: 'color',
                arrayOk: true,
                role: 'style',
                dflt: 'white',
                description: [
                    'Sets the cell fill color. It accepts either a specific color',
                    ' or an array of colors or a 2D array of colors.'
                ].join('')
            }
        },

        font: extendFlat({}, fontAttrs({arrayOk: true}))
    }
}, 'calc', 'from-root');
attrs.transforms = undefined;
