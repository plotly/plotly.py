/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var listAxes = require('../../plots/cartesian/axis_ids').list;
var getAutoRange = require('../../plots/cartesian/autorange').getAutoRange;
var constants = require('./constants');

module.exports = function calcAutorange(gd) {
    var axes = listAxes(gd, 'x', true);

    // Compute new slider range using axis autorange if necessary.
    //
    // Copy back range to input range slider container to skip
    // this step in subsequent draw calls.

    for(var i = 0; i < axes.length; i++) {
        var ax = axes[i];
        var opts = ax[constants.name];

        if(opts && opts.visible && opts.autorange) {
            opts._input.autorange = true;
            opts._input.range = opts.range = getAutoRange(gd, ax);
        }
    }
};
