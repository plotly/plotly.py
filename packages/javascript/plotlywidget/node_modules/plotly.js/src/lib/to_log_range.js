/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');

/**
 * convert a linear value into a logged value, folding negative numbers into
 * the given range
 */
module.exports = function toLogRange(val, range) {
    if(val > 0) return Math.log(val) / Math.LN10;

    // move a negative value reference to a log axis - just put the
    // result at the lowest range value on the plot (or if the range also went negative,
    // one millionth of the top of the range)
    var newVal = Math.log(Math.min(range[0], range[1])) / Math.LN10;
    if(!isNumeric(newVal)) newVal = Math.log(Math.max(range[0], range[1])) / Math.LN10 - 6;
    return newVal;
};
