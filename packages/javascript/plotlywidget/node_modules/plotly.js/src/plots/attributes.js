/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var fxAttrs = require('../components/fx/attributes');

module.exports = {
    type: {
        valType: 'enumerated',
        role: 'info',
        values: [],     // listed dynamically
        dflt: 'scatter',
        editType: 'calc+clearAxisTypes',
        _noTemplating: true // we handle this at a higher level
    },
    visible: {
        valType: 'enumerated',
        values: [true, false, 'legendonly'],
        role: 'info',
        dflt: true,
        editType: 'calc',
        description: [
            'Determines whether or not this trace is visible.',
            'If *legendonly*, the trace is not drawn,',
            'but can appear as a legend item',
            '(provided that the legend itself is visible).'
        ].join(' ')
    },
    showlegend: {
        valType: 'boolean',
        role: 'info',
        dflt: true,
        editType: 'style',
        description: [
            'Determines whether or not an item corresponding to this',
            'trace is shown in the legend.'
        ].join(' ')
    },
    legendgroup: {
        valType: 'string',
        role: 'info',
        dflt: '',
        editType: 'style',
        description: [
            'Sets the legend group for this trace.',
            'Traces part of the same legend group hide/show at the same time',
            'when toggling legend items.'
        ].join(' ')
    },
    opacity: {
        valType: 'number',
        role: 'style',
        min: 0,
        max: 1,
        dflt: 1,
        editType: 'style',
        description: 'Sets the opacity of the trace.'
    },
    name: {
        valType: 'string',
        role: 'info',
        editType: 'style',
        description: [
            'Sets the trace name.',
            'The trace name appear as the legend item and on hover.'
        ].join(' ')
    },
    uid: {
        valType: 'string',
        role: 'info',
        editType: 'plot',
        anim: true,
        description: [
            'Assign an id to this trace,',
            'Use this to provide object constancy between traces during animations',
            'and transitions.'
        ].join(' ')
    },
    ids: {
        valType: 'data_array',
        editType: 'calc',
        anim: true,
        description: [
            'Assigns id labels to each datum.',
            'These ids for object constancy of data points during animation.',
            'Should be an array of strings, not numbers or any other type.'
        ].join(' ')
    },
    customdata: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Assigns extra data each datum.',
            'This may be useful when listening to hover, click and selection events.',
            'Note that, *scatter* traces also appends customdata items in the markers',
            'DOM elements'
        ].join(' ')
    },
    meta: {
        valType: 'any',
        arrayOk: true,
        role: 'info',
        editType: 'plot',
        description: [
            'Assigns extra meta information associated with this trace',
            'that can be used in various text attributes.',
            'Attributes such as trace `name`, graph, axis and colorbar `title.text`, annotation `text`',
            '`rangeselector`, `updatemenues` and `sliders` `label` text',
            'all support `meta`.',
            'To access the trace `meta` values in an attribute in the same trace, simply use',
            '`%{meta[i]}` where `i` is the index or key of the `meta`',
            'item in question.',
            'To access trace `meta` in layout attributes, use',
            '`%{data[n[.meta[i]}` where `i` is the index or key of the `meta`',
            'and `n` is the trace index.'
        ].join(' ')
    },

    // N.B. these cannot be 'data_array' as they do not have the same length as
    // other data arrays and arrayOk attributes in general
    //
    // Maybe add another valType:
    // https://github.com/plotly/plotly.js/issues/1894
    selectedpoints: {
        valType: 'any',
        role: 'info',
        editType: 'calc',
        description: [
            'Array containing integer indices of selected points.',
            'Has an effect only for traces that support selections.',
            'Note that an empty array means an empty selection where the `unselected`',
            'are turned on for all points, whereas, any other non-array values means no',
            'selection all where the `selected` and `unselected` styles have no effect.'
        ].join(' ')
    },

    hoverinfo: {
        valType: 'flaglist',
        role: 'info',
        flags: ['x', 'y', 'z', 'text', 'name'],
        extras: ['all', 'none', 'skip'],
        arrayOk: true,
        dflt: 'all',
        editType: 'none',
        description: [
            'Determines which trace information appear on hover.',
            'If `none` or `skip` are set, no information is displayed upon hovering.',
            'But, if `none` is set, click and hover events are still fired.'
        ].join(' ')
    },
    hoverlabel: fxAttrs.hoverlabel,
    stream: {
        token: {
            valType: 'string',
            noBlank: true,
            strict: true,
            role: 'info',
            editType: 'calc',
            description: [
                'The stream id number links a data trace on a plot with a stream.',
                'See https://plot.ly/settings for more details.'
            ].join(' ')
        },
        maxpoints: {
            valType: 'number',
            min: 0,
            max: 10000,
            dflt: 500,
            role: 'info',
            editType: 'calc',
            description: [
                'Sets the maximum number of points to keep on the plots from an',
                'incoming stream.',
                'If `maxpoints` is set to *50*, only the newest 50 points will',
                'be displayed on the plot.'
            ].join(' ')
        },
        editType: 'calc'
    },
    transforms: {
        _isLinkedToArray: 'transform',
        editType: 'calc',
        description: [
            'An array of operations that manipulate the trace data,',
            'for example filtering or sorting the data arrays.'
        ].join(' ')
    },
    uirevision: {
        valType: 'any',
        role: 'info',
        editType: 'none',
        description: [
            'Controls persistence of some user-driven changes to the trace:',
            '`constraintrange` in `parcoords` traces, as well as some',
            '`editable: true` modifications such as `name` and `colorbar.title`.',
            'Defaults to `layout.uirevision`.',
            'Note that other user-driven trace attribute changes are controlled',
            'by `layout` attributes:',
            '`trace.visible` is controlled by `layout.legend.uirevision`,',
            '`selectedpoints` is controlled by `layout.selectionrevision`,',
            'and `colorbar.(x|y)` (accessible with `config: {editable: true}`)',
            'is controlled by `layout.editrevision`.',
            'Trace changes are tracked by `uid`, which only falls back on trace',
            'index if no `uid` is provided. So if your app can add/remove traces',
            'before the end of the `data` array, such that the same trace has a',
            'different index, you can still preserve user-driven changes if you',
            'give each trace a `uid` that stays with it as it moves.'
        ].join(' ')
    }
};
