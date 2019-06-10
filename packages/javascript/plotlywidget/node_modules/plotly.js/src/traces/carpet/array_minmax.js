/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;

module.exports = function(a) {
    return minMax(a, 0);
};

function minMax(a, depth) {
    // Limit to ten dimensional datasets. This seems *exceedingly* unlikely to
    // ever cause problems or even be a concern. It's include strictly so that
    // circular arrays could never cause this to loop.
    if(!isArrayOrTypedArray(a) || depth >= 10) {
        return null;
    }

    var min = Infinity;
    var max = -Infinity;
    var n = a.length;
    for(var i = 0; i < n; i++) {
        var datum = a[i];

        if(isArrayOrTypedArray(datum)) {
            var result = minMax(datum, depth + 1);

            if(result) {
                min = Math.min(result[0], min);
                max = Math.max(result[1], max);
            }
        } else {
            min = Math.min(datum, min);
            max = Math.max(datum, max);
        }
    }

    return [min, max];
}
