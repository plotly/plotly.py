/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var filterOps = require('../../constants/filter_ops');
var isNumeric = require('fast-isnumeric');

// This syntax conforms to the existing filter transform syntax, but we don't care
// about open vs. closed intervals for simply drawing contours constraints:
module.exports = {
    '[]': makeRangeSettings('[]'),
    '][': makeRangeSettings(']['),
    '>': makeInequalitySettings('>'),
    '<': makeInequalitySettings('<'),
    '=': makeInequalitySettings('=')
};

// This does not in any way shape or form support calendars. It's adapted from
// transforms/filter.js.
function coerceValue(operation, value) {
    var hasArrayValue = Array.isArray(value);

    var coercedValue;

    function coerce(value) {
        return isNumeric(value) ? (+value) : null;
    }

    if(filterOps.COMPARISON_OPS2.indexOf(operation) !== -1) {
        coercedValue = hasArrayValue ? coerce(value[0]) : coerce(value);
    } else if(filterOps.INTERVAL_OPS.indexOf(operation) !== -1) {
        coercedValue = hasArrayValue ?
            [coerce(value[0]), coerce(value[1])] :
            [coerce(value), coerce(value)];
    } else if(filterOps.SET_OPS.indexOf(operation) !== -1) {
        coercedValue = hasArrayValue ? value.map(coerce) : [coerce(value)];
    }

    return coercedValue;
}

// Returns a parabola scaled so that the min/max is either +/- 1 and zero at the two values
// provided. The data is mapped by this function when constructing intervals so that it's
// very easy to construct contours as normal.
function makeRangeSettings(operation) {
    return function(value) {
        value = coerceValue(operation, value);

        // Ensure proper ordering:
        var min = Math.min(value[0], value[1]);
        var max = Math.max(value[0], value[1]);

        return {
            start: min,
            end: max,
            size: max - min
        };
    };
}

function makeInequalitySettings(operation) {
    return function(value) {
        value = coerceValue(operation, value);

        return {
            start: value,
            end: Infinity,
            size: Infinity
        };
    };
}
