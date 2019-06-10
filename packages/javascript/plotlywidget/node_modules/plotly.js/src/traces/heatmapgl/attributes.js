/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var heatmapAttrs = require('../heatmap/attributes');
var colorScaleAttrs = require('../../components/colorscale/attributes');

var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var commonList = [
    'z',
    'x', 'x0', 'dx',
    'y', 'y0', 'dy',
    'text', 'transpose',
    'xtype', 'ytype'
];

var attrs = {};

for(var i = 0; i < commonList.length; i++) {
    var k = commonList[i];
    attrs[k] = heatmapAttrs[k];
}

extendFlat(
    attrs,
    colorScaleAttrs('', {cLetter: 'z', autoColorDflt: false})
);

module.exports = overrideAll(attrs, 'calc', 'nested');
