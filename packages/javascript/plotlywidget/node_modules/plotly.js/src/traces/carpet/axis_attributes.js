/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var fontAttrs = require('../../plots/font_attributes');
var colorAttrs = require('../../components/color/attributes');
var axesAttrs = require('../../plots/cartesian/layout_attributes');
var overrideAll = require('../../plot_api/edit_types').overrideAll;

module.exports = {
    color: {
        valType: 'color',
        role: 'style',
        editType: 'calc',
        description: [
            'Sets default for all colors associated with this axis',
            'all at once: line, font, tick, and grid colors.',
            'Grid color is lightened by blending this with the plot background',
            'Individual pieces can override this.'
        ].join(' ')
    },
    smoothing: {
        valType: 'number',
        dflt: 1,
        min: 0,
        max: 1.3,
        role: 'info',
        editType: 'calc'
    },
    title: {
        text: {
            valType: 'string',
            dflt: '',
            role: 'info',
            editType: 'calc',
            description: [
                'Sets the title of this axis.',
                'Note that before the existence of `title.text`, the title\'s',
                'contents used to be defined as the `title` attribute itself.',
                'This behavior has been deprecated.'
            ].join(' ')
        },
        font: fontAttrs({
            editType: 'calc',
            description: [
                'Sets this axis\' title font.',
                'Note that the title\'s font used to be set',
                'by the now deprecated `titlefont` attribute.'
            ].join(' ')
        }),
        offset: {
            valType: 'number',
            role: 'info',
            dflt: 10,
            editType: 'calc',
            description: [
                'An additional amount by which to offset the title from the tick',
                'labels, given in pixels.',
                'Note that this used to be set',
                'by the now deprecated `titleoffset` attribute.'
            ].join(' '),
        },
        editType: 'calc',
    },
    type: {
        valType: 'enumerated',
        // '-' means we haven't yet run autotype or couldn't find any data
        // it gets turned into linear in gd._fullLayout but not copied back
        // to gd.data like the others are.
        values: ['-', 'linear', 'date', 'category'],
        dflt: '-',
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the axis type.',
            'By default, plotly attempts to determined the axis type',
            'by looking into the data of the traces that referenced',
            'the axis in question.'
        ].join(' ')
    },
    autorange: {
        valType: 'enumerated',
        values: [true, false, 'reversed'],
        dflt: true,
        role: 'style',
        editType: 'calc',
        description: [
            'Determines whether or not the range of this axis is',
            'computed in relation to the input data.',
            'See `rangemode` for more info.',
            'If `range` is provided, then `autorange` is set to *false*.'
        ].join(' ')
    },
    rangemode: {
        valType: 'enumerated',
        values: ['normal', 'tozero', 'nonnegative'],
        dflt: 'normal',
        role: 'style',
        editType: 'calc',
        description: [
            'If *normal*, the range is computed in relation to the extrema',
            'of the input data.',
            'If *tozero*`, the range extends to 0,',
            'regardless of the input data',
            'If *nonnegative*, the range is non-negative,',
            'regardless of the input data.'
        ].join(' ')
    },
    range: {
        valType: 'info_array',
        role: 'info',
        editType: 'calc',
        items: [
            {valType: 'any', editType: 'calc'},
            {valType: 'any', editType: 'calc'}
        ],
        description: [
            'Sets the range of this axis.',
            'If the axis `type` is *log*, then you must take the log of your',
            'desired range (e.g. to set the range from 1 to 100,',
            'set the range from 0 to 2).',
            'If the axis `type` is *date*, it should be date strings,',
            'like date data, though Date objects and unix milliseconds',
            'will be accepted and converted to strings.',
            'If the axis `type` is *category*, it should be numbers,',
            'using the scale where each category is assigned a serial',
            'number from zero in the order it appears.'
        ].join(' ')
    },

    fixedrange: {
        valType: 'boolean',
        dflt: false,
        role: 'info',
        editType: 'calc',
        description: [
            'Determines whether or not this axis is zoom-able.',
            'If true, then zoom is disabled.'
        ].join(' ')
    },
    cheatertype: {
        valType: 'enumerated',
        values: ['index', 'value'],
        dflt: 'value',
        role: 'info',
        editType: 'calc'
    },
    tickmode: {
        valType: 'enumerated',
        values: ['linear', 'array'],
        dflt: 'array',
        role: 'info',
        editType: 'calc'
    },
    nticks: {
        valType: 'integer',
        min: 0,
        dflt: 0,
        role: 'style',
        editType: 'calc',
        description: [
            'Specifies the maximum number of ticks for the particular axis.',
            'The actual number of ticks will be chosen automatically to be',
            'less than or equal to `nticks`.',
            'Has an effect only if `tickmode` is set to *auto*.'
        ].join(' ')
    },
    tickvals: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the values at which ticks on this axis appear.',
            'Only has an effect if `tickmode` is set to *array*.',
            'Used with `ticktext`.'
        ].join(' ')
    },
    ticktext: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the text displayed at the ticks position via `tickvals`.',
            'Only has an effect if `tickmode` is set to *array*.',
            'Used with `tickvals`.'
        ].join(' ')
    },
    showticklabels: {
        valType: 'enumerated',
        values: ['start', 'end', 'both', 'none'],
        dflt: 'start',
        role: 'style',
        editType: 'calc',
        description: [
            'Determines whether axis labels are drawn on the low side,',
            'the high side, both, or neither side of the axis.'
        ].join(' ')
    },
    tickfont: fontAttrs({
        editType: 'calc',
        description: 'Sets the tick font.'
    }),
    tickangle: {
        valType: 'angle',
        dflt: 'auto',
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the angle of the tick labels with respect to the horizontal.',
            'For example, a `tickangle` of -90 draws the tick labels',
            'vertically.'
        ].join(' ')
    },
    tickprefix: {
        valType: 'string',
        dflt: '',
        role: 'style',
        editType: 'calc',
        description: 'Sets a tick label prefix.'
    },
    showtickprefix: {
        valType: 'enumerated',
        values: ['all', 'first', 'last', 'none'],
        dflt: 'all',
        role: 'style',
        editType: 'calc',
        description: [
            'If *all*, all tick labels are displayed with a prefix.',
            'If *first*, only the first tick is displayed with a prefix.',
            'If *last*, only the last tick is displayed with a suffix.',
            'If *none*, tick prefixes are hidden.'
        ].join(' ')
    },
    ticksuffix: {
        valType: 'string',
        dflt: '',
        role: 'style',
        editType: 'calc',
        description: 'Sets a tick label suffix.'
    },
    showticksuffix: {
        valType: 'enumerated',
        values: ['all', 'first', 'last', 'none'],
        dflt: 'all',
        role: 'style',
        editType: 'calc',
        description: 'Same as `showtickprefix` but for tick suffixes.'
    },
    showexponent: {
        valType: 'enumerated',
        values: ['all', 'first', 'last', 'none'],
        dflt: 'all',
        role: 'style',
        editType: 'calc',
        description: [
            'If *all*, all exponents are shown besides their significands.',
            'If *first*, only the exponent of the first tick is shown.',
            'If *last*, only the exponent of the last tick is shown.',
            'If *none*, no exponents appear.'
        ].join(' ')
    },
    exponentformat: {
        valType: 'enumerated',
        values: ['none', 'e', 'E', 'power', 'SI', 'B'],
        dflt: 'B',
        role: 'style',
        editType: 'calc',
        description: [
            'Determines a formatting rule for the tick exponents.',
            'For example, consider the number 1,000,000,000.',
            'If *none*, it appears as 1,000,000,000.',
            'If *e*, 1e+9.',
            'If *E*, 1E+9.',
            'If *power*, 1x10^9 (with 9 in a super script).',
            'If *SI*, 1G.',
            'If *B*, 1B.'
        ].join(' ')
    },
    separatethousands: {
        valType: 'boolean',
        dflt: false,
        role: 'style',
        editType: 'calc',
        description: [
            'If "true", even 4-digit integers are separated'
        ].join(' ')
    },
    tickformat: {
        valType: 'string',
        dflt: '',
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the tick label formatting rule using d3 formatting mini-languages',
            'which are very similar to those in Python. For numbers, see:',
            'https://github.com/d3/d3-format/blob/master/README.md#locale_format',
            'And for dates see:',
            'https://github.com/d3/d3-time-format/blob/master/README.md#locale_format',
            'We add one item to d3\'s date formatter: *%{n}f* for fractional seconds',
            'with n digits. For example, *2016-10-13 09:15:23.456* with tickformat',
            '*%H~%M~%S.%2f* would display *09~15~23.46*'
        ].join(' ')
    },
    tickformatstops: overrideAll(axesAttrs.tickformatstops, 'calc', 'from-root'),
    categoryorder: {
        valType: 'enumerated',
        values: [
            'trace', 'category ascending', 'category descending', 'array'
            /* , 'value ascending', 'value descending'*/ // value ascending / descending to be implemented later
        ],
        dflt: 'trace',
        role: 'info',
        editType: 'calc',
        description: [
            'Specifies the ordering logic for the case of categorical variables.',
            'By default, plotly uses *trace*, which specifies the order that is present in the data supplied.',
            'Set `categoryorder` to *category ascending* or *category descending* if order should be determined by',
            'the alphanumerical order of the category names.',
            /* 'Set `categoryorder` to *value ascending* or *value descending* if order should be determined by the',
            'numerical order of the values.',*/ // // value ascending / descending to be implemented later
            'Set `categoryorder` to *array* to derive the ordering from the attribute `categoryarray`. If a category',
            'is not found in the `categoryarray` array, the sorting behavior for that attribute will be identical to',
            'the *trace* mode. The unspecified categories will follow the categories in `categoryarray`.'
        ].join(' ')
    },
    categoryarray: {
        valType: 'data_array',
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the order in which categories on this axis appear.',
            'Only has an effect if `categoryorder` is set to *array*.',
            'Used with `categoryorder`.'
        ].join(' ')
    },
    labelpadding: {
        valType: 'integer',
        role: 'style',
        dflt: 10,
        editType: 'calc',
        description: 'Extra padding between label and the axis'
    },
    labelprefix: {
        valType: 'string',
        role: 'style',
        editType: 'calc',
        description: 'Sets a axis label prefix.'
    },
    labelsuffix: {
        valType: 'string',
        dflt: '',
        role: 'style',
        editType: 'calc',
        description: 'Sets a axis label suffix.'
    },
    // lines and grids
    showline: {
        valType: 'boolean',
        dflt: false,
        role: 'style',
        editType: 'calc',
        description: [
            'Determines whether or not a line bounding this axis is drawn.'
        ].join(' ')
    },
    linecolor: {
        valType: 'color',
        dflt: colorAttrs.defaultLine,
        role: 'style',
        editType: 'calc',
        description: 'Sets the axis line color.'
    },
    linewidth: {
        valType: 'number',
        min: 0,
        dflt: 1,
        role: 'style',
        editType: 'calc',
        description: 'Sets the width (in px) of the axis line.'
    },
    gridcolor: {
        valType: 'color',
        role: 'style',
        editType: 'calc',
        description: 'Sets the axis line color.'
    },
    gridwidth: {
        valType: 'number',
        min: 0,
        dflt: 1,
        role: 'style',
        editType: 'calc',
        description: 'Sets the width (in px) of the axis line.'
    },
    showgrid: {
        valType: 'boolean',
        role: 'style',
        dflt: true,
        editType: 'calc',
        description: [
            'Determines whether or not grid lines are drawn.',
            'If *true*, the grid lines are drawn at every tick mark.'
        ].join(' ')
    },
    minorgridcount: {
        valType: 'integer',
        min: 0,
        dflt: 0,
        role: 'info',
        editType: 'calc',
        description: 'Sets the number of minor grid ticks per major grid tick'
    },
    minorgridwidth: {
        valType: 'number',
        min: 0,
        dflt: 1,
        role: 'style',
        editType: 'calc',
        description: 'Sets the width (in px) of the grid lines.'
    },
    minorgridcolor: {
        valType: 'color',
        dflt: colorAttrs.lightLine,
        role: 'style',
        editType: 'calc',
        description: 'Sets the color of the grid lines.'
    },
    startline: {
        valType: 'boolean',
        role: 'style',
        editType: 'calc',
        description: [
            'Determines whether or not a line is drawn at along the starting value',
            'of this axis.',
            'If *true*, the start line is drawn on top of the grid lines.'
        ].join(' ')
    },
    startlinecolor: {
        valType: 'color',
        role: 'style',
        editType: 'calc',
        description: 'Sets the line color of the start line.'
    },
    startlinewidth: {
        valType: 'number',
        dflt: 1,
        role: 'style',
        editType: 'calc',
        description: 'Sets the width (in px) of the start line.'
    },
    endline: {
        valType: 'boolean',
        role: 'style',
        editType: 'calc',
        description: [
            'Determines whether or not a line is drawn at along the final value',
            'of this axis.',
            'If *true*, the end line is drawn on top of the grid lines.'
        ].join(' ')
    },
    endlinewidth: {
        valType: 'number',
        dflt: 1,
        role: 'style',
        editType: 'calc',
        description: 'Sets the width (in px) of the end line.'
    },
    endlinecolor: {
        valType: 'color',
        role: 'style',
        editType: 'calc',
        description: 'Sets the line color of the end line.'
    },
    tick0: {
        valType: 'number',
        min: 0,
        dflt: 0,
        role: 'info',
        editType: 'calc',
        description: 'The starting index of grid lines along the axis'
    },
    dtick: {
        valType: 'number',
        min: 0,
        dflt: 1,
        role: 'info',
        editType: 'calc',
        description: 'The stride between grid lines along the axis'
    },
    arraytick0: {
        valType: 'integer',
        min: 0,
        dflt: 0,
        role: 'info',
        editType: 'calc',
        description: 'The starting index of grid lines along the axis'
    },
    arraydtick: {
        valType: 'integer',
        min: 1,
        dflt: 1,
        role: 'info',
        editType: 'calc',
        description: 'The stride between grid lines along the axis'
    },

    _deprecated: {
        title: {
            valType: 'string',
            role: 'info',
            editType: 'calc',
            description: [
                'Deprecated in favor of `title.text`.',
                'Note that value of `title` is no longer a simple',
                '*string* but a set of sub-attributes.'
            ].join(' ')
        },
        titlefont: fontAttrs({
            editType: 'calc',
            description: 'Deprecated in favor of `title.font`.'
        }),
        titleoffset: {
            valType: 'number',
            role: 'info',
            dflt: 10,
            editType: 'calc',
            description: 'Deprecated in favor of `title.offset`.'
        }
    },

    editType: 'calc'
};
