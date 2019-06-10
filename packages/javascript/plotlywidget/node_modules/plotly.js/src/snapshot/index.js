/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var helpers = require('./helpers');

var Snapshot = {
    getDelay: helpers.getDelay,
    getRedrawFunc: helpers.getRedrawFunc,
    clone: require('./cloneplot'),
    toSVG: require('./tosvg'),
    svgToImg: require('./svgtoimg'),
    toImage: require('./toimage'),
    downloadImage: require('./download')
};

module.exports = Snapshot;
