/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');

var BADNUM = require('../constants/numerical').BADNUM;

// precompile for speed
var JUNK = /^['"%,$#\s']+|[, ]|['"%,$#\s']+$/g;

/**
 * cleanNumber: remove common leading and trailing cruft
 * Always returns either a number or BADNUM.
 */
module.exports = function cleanNumber(v) {
    if(typeof v === 'string') {
        v = v.replace(JUNK, '');
    }

    if(isNumeric(v)) return Number(v);

    return BADNUM;
};
