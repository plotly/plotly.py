/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


module.exports = {

    // layout attribute name
    name: 'sliders',

    // class names
    containerClassName: 'slider-container',
    groupClassName: 'slider-group',
    inputAreaClass: 'slider-input-area',
    railRectClass: 'slider-rail-rect',
    railTouchRectClass: 'slider-rail-touch-rect',
    gripRectClass: 'slider-grip-rect',
    tickRectClass: 'slider-tick-rect',
    inputProxyClass: 'slider-input-proxy',
    labelsClass: 'slider-labels',
    labelGroupClass: 'slider-label-group',
    labelClass: 'slider-label',
    currentValueClass: 'slider-current-value',

    railHeight: 5,

    // DOM attribute name in button group keeping track
    // of active update menu
    menuIndexAttrName: 'slider-active-index',

    // id root pass to Plots.autoMargin
    autoMarginIdRoot: 'slider-',

    // min item width / height
    minWidth: 30,
    minHeight: 30,

    // padding around item text
    textPadX: 40,

    // arrow offset off right edge
    arrowOffsetX: 4,

    railRadius: 2,
    railWidth: 5,
    railBorder: 4,
    railBorderWidth: 1,
    railBorderColor: '#bec8d9',
    railBgColor: '#f8fafc',

    // The distance of the rail from the edge of the touchable area
    // Slightly less than the step inset because of the curved edges
    // of the rail
    railInset: 8,

    // The distance from the extremal tick marks to the edge of the
    // touchable area. This is basically the same as the grip radius,
    // but for other styles it wouldn't really need to be.
    stepInset: 10,

    gripRadius: 10,
    gripWidth: 20,
    gripHeight: 20,
    gripBorder: 20,
    gripBorderWidth: 1,
    gripBorderColor: '#bec8d9',
    gripBgColor: '#f6f8fa',
    gripBgActiveColor: '#dbdde0',

    labelPadding: 8,
    labelOffset: 0,

    tickWidth: 1,
    tickColor: '#333',
    tickOffset: 25,
    tickLength: 7,

    minorTickOffset: 25,
    minorTickColor: '#333',
    minorTickLength: 4,

    // Extra space below the current value label:
    currentValuePadding: 8,
    currentValueInset: 0,
};
