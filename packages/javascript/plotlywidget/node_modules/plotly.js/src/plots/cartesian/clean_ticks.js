/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');
var Lib = require('../../lib');
var ONEDAY = require('../../constants/numerical').ONEDAY;

/**
 * Return a validated dtick value for this axis
 *
 * @param {any} dtick: the candidate dtick. valid values are numbers and strings,
 *     and further constrained depending on the axis type.
 * @param {string} axType: the axis type
 */
exports.dtick = function(dtick, axType) {
    var isLog = axType === 'log';
    var isDate = axType === 'date';
    var isCat = axType === 'category';
    var dtickDflt = isDate ? ONEDAY : 1;

    if(!dtick) return dtickDflt;

    if(isNumeric(dtick)) {
        dtick = Number(dtick);
        if(dtick <= 0) return dtickDflt;
        if(isCat) {
            // category dtick must be positive integers
            return Math.max(1, Math.round(dtick));
        }
        if(isDate) {
            // date dtick must be at least 0.1ms (our current precision)
            return Math.max(0.1, dtick);
        }
        return dtick;
    }

    if(typeof dtick !== 'string' || !(isDate || isLog)) {
        return dtickDflt;
    }

    var prefix = dtick.charAt(0);
    var dtickNum = dtick.substr(1);
    dtickNum = isNumeric(dtickNum) ? Number(dtickNum) : 0;

    if((dtickNum <= 0) || !(
            // "M<n>" gives ticks every (integer) n months
            (isDate && prefix === 'M' && dtickNum === Math.round(dtickNum)) ||
            // "L<f>" gives ticks linearly spaced in data (not in position) every (float) f
            (isLog && prefix === 'L') ||
            // "D1" gives powers of 10 with all small digits between, "D2" gives only 2 and 5
            (isLog && prefix === 'D' && (dtickNum === 1 || dtickNum === 2))
        )) {
        return dtickDflt;
    }

    return dtick;
};

/**
 * Return a validated tick0 for this axis
 *
 * @param {any} tick0: the candidate tick0. Valid values are numbers and strings,
 *     further constrained depending on the axis type
 * @param {string} axType: the axis type
 * @param {string} calendar: for date axes, the calendar to validate/convert with
 * @param {any} dtick: an already valid dtick. Only used for D1 and D2 log dticks,
 *     which do not support tick0 at all.
 */
exports.tick0 = function(tick0, axType, calendar, dtick) {
    if(axType === 'date') {
        return Lib.cleanDate(tick0, Lib.dateTick0(calendar));
    }
    if(dtick === 'D1' || dtick === 'D2') {
        // D1 and D2 modes ignore tick0 entirely
        return undefined;
    }
    // Aside from date axes, tick0 must be numeric
    return isNumeric(tick0) ? Number(tick0) : 0;
};
