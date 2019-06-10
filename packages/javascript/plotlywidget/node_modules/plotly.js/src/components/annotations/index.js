/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var drawModule = require('./draw');
var clickModule = require('./click');

module.exports = {
    moduleType: 'component',
    name: 'annotations',

    layoutAttributes: require('./attributes'),
    supplyLayoutDefaults: require('./defaults'),
    includeBasePlot: require('../../plots/cartesian/include_components')('annotations'),

    calcAutorange: require('./calc_autorange'),
    draw: drawModule.draw,
    drawOne: drawModule.drawOne,
    drawRaw: drawModule.drawRaw,

    hasClickToShow: clickModule.hasClickToShow,
    onClick: clickModule.onClick,

    convertCoords: require('./convert_coords')
};
