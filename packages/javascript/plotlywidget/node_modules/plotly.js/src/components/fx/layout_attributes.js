/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var constants = require('./constants');

var fontAttrs = require('../../plots/font_attributes')({
    editType: 'none',
    description: 'Sets the default hover label font used by all traces on the graph.'
});
fontAttrs.family.dflt = constants.HOVERFONT;
fontAttrs.size.dflt = constants.HOVERFONTSIZE;

module.exports = {
    clickmode: {
        valType: 'flaglist',
        role: 'info',
        flags: ['event', 'select'],
        dflt: 'event',
        editType: 'plot',
        extras: ['none'],
        description: [
            'Determines the mode of single click interactions.',
            '*event* is the default value and emits the `plotly_click`',
            'event. In addition this mode emits the `plotly_selected` event',
            'in drag modes *lasso* and *select*, but with no event data attached',
            '(kept for compatibility reasons).',
            'The *select* flag enables selecting single',
            'data points via click. This mode also supports persistent selections,',
            'meaning that pressing Shift while clicking, adds to / subtracts from an',
            'existing selection. *select* with `hovermode`: *x* can be confusing, consider',
            'explicitly setting `hovermode`: *closest* when using this feature.',
            'Selection events are sent accordingly as long as *event* flag is set as well.',
            'When the *event* flag is missing, `plotly_click` and `plotly_selected`',
            'events are not fired.'
        ].join(' ')
    },
    dragmode: {
        valType: 'enumerated',
        role: 'info',
        values: ['zoom', 'pan', 'select', 'lasso', 'orbit', 'turntable', false],
        dflt: 'zoom',
        editType: 'modebar',
        description: [
            'Determines the mode of drag interactions.',
            '*select* and *lasso* apply only to scatter traces with',
            'markers or text. *orbit* and *turntable* apply only to',
            '3D scenes.'
        ].join(' ')
    },
    hovermode: {
        valType: 'enumerated',
        role: 'info',
        values: ['x', 'y', 'closest', false],
        editType: 'modebar',
        description: [
            'Determines the mode of hover interactions.',
            'If `clickmode` includes the *select* flag,',
            '`hovermode` defaults to *closest*.',
            'If `clickmode` lacks the *select* flag,',
            'it defaults to *x* or *y* (depending on the trace\'s',
            '`orientation` value) for plots based on',
            'cartesian coordinates. For anything else the default',
            'value is *closest*.',
        ].join(' ')
    },
    hoverdistance: {
        valType: 'integer',
        min: -1,
        dflt: 20,
        role: 'info',
        editType: 'none',
        description: [
            'Sets the default distance (in pixels) to look for data',
            'to add hover labels (-1 means no cutoff, 0 means no looking for data).',
            'This is only a real distance for hovering on point-like objects,',
            'like scatter points. For area-like objects (bars, scatter fills, etc)',
            'hovering is on inside the area and off outside, but these objects',
            'will not supersede hover on point-like objects in case of conflict.'
        ].join(' ')
    },
    spikedistance: {
        valType: 'integer',
        min: -1,
        dflt: 20,
        role: 'info',
        editType: 'none',
        description: [
            'Sets the default distance (in pixels) to look for data to draw',
            'spikelines to (-1 means no cutoff, 0 means no looking for data).',
            'As with hoverdistance, distance does not apply to area-like objects.',
            'In addition, some objects can be hovered on but will not generate',
            'spikelines, such as scatter fills.'
        ].join(' ')
    },
    hoverlabel: {
        bgcolor: {
            valType: 'color',
            role: 'style',
            editType: 'none',
            description: [
                'Sets the background color of all hover labels on graph'
            ].join(' ')
        },
        bordercolor: {
            valType: 'color',
            role: 'style',
            editType: 'none',
            description: [
                'Sets the border color of all hover labels on graph.'
            ].join(' ')
        },
        font: fontAttrs,
        align: {
            valType: 'enumerated',
            values: ['left', 'right', 'auto'],
            dflt: 'auto',
            role: 'style',
            editType: 'none',
            description: [
                'Sets the horizontal alignment of the text content within hover label box.',
                'Has an effect only if the hover label text spans more two or more lines'
            ].join(' ')
        },
        namelength: {
            valType: 'integer',
            min: -1,
            dflt: 15,
            role: 'style',
            editType: 'none',
            description: [
                'Sets the default length (in number of characters) of the trace name in',
                'the hover labels for all traces. -1 shows the whole name',
                'regardless of length. 0-3 shows the first 0-3 characters, and',
                'an integer >3 will show the whole name if it is less than that',
                'many characters, but if it is longer, will truncate to',
                '`namelength - 3` characters and add an ellipsis.'
            ].join(' ')
        },
        editType: 'none'
    },
    selectdirection: {
        valType: 'enumerated',
        role: 'info',
        values: ['h', 'v', 'd', 'any'],
        dflt: 'any',
        description: [
            'When "dragmode" is set to "select", this limits the selection of the drag to',
            'horizontal, vertical or diagonal. "h" only allows horizontal selection,',
            '"v" only vertical, "d" only diagonal and "any" sets no limit.'
        ].join(' '),
        editType: 'none'
    }
};
