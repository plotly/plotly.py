/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var rgba = require('color-normalize');

function str2RgbaArray(color) {
    if(!color) return [0, 0, 0, 1];
    return rgba(color);
}

module.exports = str2RgbaArray;
