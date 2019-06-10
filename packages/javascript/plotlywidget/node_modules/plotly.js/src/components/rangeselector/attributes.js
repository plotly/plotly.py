/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var fontAttrs = require('../../plots/font_attributes');
var colorAttrs = require('../color/attributes');
var templatedArray = require('../../plot_api/plot_template').templatedArray;

var buttonAttrs = templatedArray('button', {
    visible: {
        valType: 'boolean',
        role: 'info',
        dflt: true,
        editType: 'plot',
        description: 'Determines whether or not this button is visible.'
    },
    step: {
        valType: 'enumerated',
        role: 'info',
        values: ['month', 'year', 'day', 'hour', 'minute', 'second', 'all'],
        dflt: 'month',
        editType: 'plot',
        description: [
            'The unit of measurement that the `count` value will set the range by.'
        ].join(' ')
    },
    stepmode: {
        valType: 'enumerated',
        role: 'info',
        values: ['backward', 'todate'],
        dflt: 'backward',
        editType: 'plot',
        description: [
            'Sets the range update mode.',
            'If *backward*, the range update shifts the start of range',
            'back *count* times *step* milliseconds.',
            'If *todate*, the range update shifts the start of range',
            'back to the first timestamp from *count* times',
            '*step* milliseconds back.',
            'For example, with `step` set to *year* and `count` set to *1*',
            'the range update shifts the start of the range back to',
            'January 01 of the current year.',
            'Month and year *todate* are currently available only',
            'for the built-in (Gregorian) calendar.'
        ].join(' ')
    },
    count: {
        valType: 'number',
        role: 'info',
        min: 0,
        dflt: 1,
        editType: 'plot',
        description: [
            'Sets the number of steps to take to update the range.',
            'Use with `step` to specify the update interval.'
        ].join(' ')
    },
    label: {
        valType: 'string',
        role: 'info',
        editType: 'plot',
        description: 'Sets the text label to appear on the button.'
    },
    editType: 'plot',
    description: [
        'Sets the specifications for each buttons.',
        'By default, a range selector comes with no buttons.'
    ].join(' ')
});

module.exports = {
    visible: {
        valType: 'boolean',
        role: 'info',
        editType: 'plot',
        description: [
            'Determines whether or not this range selector is visible.',
            'Note that range selectors are only available for x axes of',
            '`type` set to or auto-typed to *date*.'
        ].join(' ')
    },

    buttons: buttonAttrs,

    x: {
        valType: 'number',
        min: -2,
        max: 3,
        role: 'style',
        editType: 'plot',
        description: 'Sets the x position (in normalized coordinates) of the range selector.'
    },
    xanchor: {
        valType: 'enumerated',
        values: ['auto', 'left', 'center', 'right'],
        dflt: 'left',
        role: 'info',
        editType: 'plot',
        description: [
            'Sets the range selector\'s horizontal position anchor.',
            'This anchor binds the `x` position to the *left*, *center*',
            'or *right* of the range selector.'
        ].join(' ')
    },
    y: {
        valType: 'number',
        min: -2,
        max: 3,
        role: 'style',
        editType: 'plot',
        description: 'Sets the y position (in normalized coordinates) of the range selector.'
    },
    yanchor: {
        valType: 'enumerated',
        values: ['auto', 'top', 'middle', 'bottom'],
        dflt: 'bottom',
        role: 'info',
        editType: 'plot',
        description: [
            'Sets the range selector\'s vertical position anchor',
            'This anchor binds the `y` position to the *top*, *middle*',
            'or *bottom* of the range selector.'
        ].join(' ')
    },

    font: fontAttrs({
        editType: 'plot',
        description: 'Sets the font of the range selector button text.'
    }),

    bgcolor: {
        valType: 'color',
        dflt: colorAttrs.lightLine,
        role: 'style',
        editType: 'plot',
        description: 'Sets the background color of the range selector buttons.'
    },
    activecolor: {
        valType: 'color',
        role: 'style',
        editType: 'plot',
        description: 'Sets the background color of the active range selector button.'
    },
    bordercolor: {
        valType: 'color',
        dflt: colorAttrs.defaultLine,
        role: 'style',
        editType: 'plot',
        description: 'Sets the color of the border enclosing the range selector.'
    },
    borderwidth: {
        valType: 'number',
        min: 0,
        dflt: 0,
        role: 'style',
        editType: 'plot',
        description: 'Sets the width (in px) of the border enclosing the range selector.'
    },
    editType: 'plot'
};
