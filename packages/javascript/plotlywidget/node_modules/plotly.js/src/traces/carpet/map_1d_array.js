/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;

/*
 * Map an array of x or y coordinates (c) to screen-space pixel coordinates (p).
 * The output array is optional, but if provided, it will be reused without
 * reallocation to the extent possible.
 */
module.exports = function mapArray(out, data, func) {
    var i;

    if(!isArrayOrTypedArray(out)) {
        // If not an array, make it an array:
        out = [];
    } else if(out.length > data.length) {
        // If too long, truncate. (If too short, it will grow
        // automatically so we don't care about that case)
        out = out.slice(0, data.length);
    }

    for(i = 0; i < data.length; i++) {
        out[i] = func(data[i]);
    }

    return out;
};
