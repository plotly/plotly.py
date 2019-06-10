/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function zip3(x, y, z, len) {
    len = len || x.length;

    var result = new Array(len);
    for(var i = 0; i < len; i++) {
        result[i] = [x[i], y[i], z[i]];
    }
    return result;
};
