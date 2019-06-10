/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var attributes = require('./attributes');

var xyAttrs = {
    error_x: Lib.extendFlat({}, attributes),
    error_y: Lib.extendFlat({}, attributes)
};
delete xyAttrs.error_x.copy_zstyle;
delete xyAttrs.error_y.copy_zstyle;
delete xyAttrs.error_y.copy_ystyle;

var xyzAttrs = {
    error_x: Lib.extendFlat({}, attributes),
    error_y: Lib.extendFlat({}, attributes),
    error_z: Lib.extendFlat({}, attributes)
};
delete xyzAttrs.error_x.copy_ystyle;
delete xyzAttrs.error_y.copy_ystyle;
delete xyzAttrs.error_z.copy_ystyle;
delete xyzAttrs.error_z.copy_zstyle;

module.exports = {
    moduleType: 'component',
    name: 'errorbars',

    schema: {
        traces: {
            scatter: xyAttrs,
            bar: xyAttrs,
            histogram: xyAttrs,
            scatter3d: overrideAll(xyzAttrs, 'calc', 'nested'),
            scattergl: overrideAll(xyAttrs, 'calc', 'nested')
        }
    },

    supplyDefaults: require('./defaults'),

    calc: require('./calc'),
    makeComputeError: require('./compute_error'),

    plot: require('./plot'),
    style: require('./style'),
    hoverInfo: hoverInfo
};

function hoverInfo(calcPoint, trace, hoverPoint) {
    if((trace.error_y || {}).visible) {
        hoverPoint.yerr = calcPoint.yh - calcPoint.y;
        if(!trace.error_y.symmetric) hoverPoint.yerrneg = calcPoint.y - calcPoint.ys;
    }
    if((trace.error_x || {}).visible) {
        hoverPoint.xerr = calcPoint.xh - calcPoint.x;
        if(!trace.error_x.symmetric) hoverPoint.xerrneg = calcPoint.x - calcPoint.xs;
    }
}
