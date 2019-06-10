/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


/**
 * Error bar computing function generator
 *
 * N.B. The generated function does not clean the dataPt entries. Non-numeric
 * entries result in undefined error magnitudes.
 *
 * @param {object} opts error bar attributes
 *
 * @return {function} :
 *      @param {numeric} dataPt data point from where to compute the error magnitude
 *      @param {number} index index of dataPt in its corresponding data array
 *      @return {array}
 *        - error[0] : error magnitude in the negative direction
 *        - error[1] : " " " " positive "
 */
module.exports = function makeComputeError(opts) {
    var type = opts.type;
    var symmetric = opts.symmetric;

    if(type === 'data') {
        var array = opts.array || [];

        if(symmetric) {
            return function computeError(dataPt, index) {
                var val = +(array[index]);
                return [val, val];
            };
        } else {
            var arrayminus = opts.arrayminus || [];
            return function computeError(dataPt, index) {
                var val = +array[index];
                var valMinus = +arrayminus[index];
                // in case one is present and the other is missing, fill in 0
                // so we still see the present one. Mostly useful during manual
                // data entry.
                if(!isNaN(val) || !isNaN(valMinus)) {
                    return [valMinus || 0, val || 0];
                }
                return [NaN, NaN];
            };
        }
    } else {
        var computeErrorValue = makeComputeErrorValue(type, opts.value);
        var computeErrorValueMinus = makeComputeErrorValue(type, opts.valueminus);

        if(symmetric || opts.valueminus === undefined) {
            return function computeError(dataPt) {
                var val = computeErrorValue(dataPt);
                return [val, val];
            };
        } else {
            return function computeError(dataPt) {
                return [
                    computeErrorValueMinus(dataPt),
                    computeErrorValue(dataPt)
                ];
            };
        }
    }
};

/**
 * Compute error bar magnitude (for all types except data)
 *
 * @param {string} type error bar type
 * @param {numeric} value error bar value
 *
 * @return {function} :
 *      @param {numeric} dataPt
 */
function makeComputeErrorValue(type, value) {
    if(type === 'percent') {
        return function(dataPt) {
            return Math.abs(dataPt * value / 100);
        };
    }
    if(type === 'constant') {
        return function() {
            return Math.abs(value);
        };
    }
    if(type === 'sqrt') {
        return function(dataPt) {
            return Math.sqrt(Math.abs(dataPt));
        };
    }
}
