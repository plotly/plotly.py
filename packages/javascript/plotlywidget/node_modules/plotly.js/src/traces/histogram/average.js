/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


module.exports = function doAvg(size, counts) {
    var nMax = size.length;
    var total = 0;
    for(var i = 0; i < nMax; i++) {
        if(counts[i]) {
            size[i] /= counts[i];
            total += size[i];
        } else size[i] = null;
    }
    return total;
};
