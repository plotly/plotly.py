/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');
var isArrayOrTypedArray = require('./array').isArrayOrTypedArray;

/**
 * aggNums() returns the result of an aggregate function applied to an array of
 * values, where non-numerical values have been tossed out.
 *
 * @param {function} f - aggregation function (e.g., Math.min)
 * @param {Number} v - initial value (continuing from previous calls)
 *      if there's no continuing value, use null for selector-type
 *      functions (max,min), or 0 for summations
 * @param {Array} a - array to aggregate (may be nested, we will recurse,
 *                    but all elements must have the same dimension)
 * @param {Number} len - maximum length of a to aggregate
 * @return {Number} - result of f applied to a starting from v
 */
exports.aggNums = function(f, v, a, len) {
    var i,
        b;
    if(!len || len > a.length) len = a.length;
    if(!isNumeric(v)) v = false;
    if(isArrayOrTypedArray(a[0])) {
        b = new Array(len);
        for(i = 0; i < len; i++) b[i] = exports.aggNums(f, v, a[i]);
        a = b;
    }

    for(i = 0; i < len; i++) {
        if(!isNumeric(v)) v = a[i];
        else if(isNumeric(a[i])) v = f(+v, +a[i]);
    }
    return v;
};

/**
 * mean & std dev functions using aggNums, so it handles non-numerics nicely
 * even need to use aggNums instead of .length, to toss out non-numerics
 */
exports.len = function(data) {
    return exports.aggNums(function(a) { return a + 1; }, 0, data);
};

exports.mean = function(data, len) {
    if(!len) len = exports.len(data);
    return exports.aggNums(function(a, b) { return a + b; }, 0, data) / len;
};

exports.midRange = function(numArr) {
    if(numArr === undefined || numArr.length === 0) return undefined;
    return (exports.aggNums(Math.max, null, numArr) + exports.aggNums(Math.min, null, numArr)) / 2;
};

exports.variance = function(data, len, mean) {
    if(!len) len = exports.len(data);
    if(!isNumeric(mean)) mean = exports.mean(data, len);

    return exports.aggNums(function(a, b) {
        return a + Math.pow(b - mean, 2);
    }, 0, data) / len;
};

exports.stdev = function(data, len, mean) {
    return Math.sqrt(exports.variance(data, len, mean));
};

/**
 * median of a finite set of numbers
 * reference page: https://en.wikipedia.org/wiki/Median#Finite_set_of_numbers
**/
exports.median = function(data) {
    var b = data.slice().sort();
    return exports.interp(b, 0.5);
};

/**
 * interp() computes a percentile (quantile) for a given distribution.
 * We interpolate the distribution (to compute quantiles, we follow method #10 here:
 * http://www.amstat.org/publications/jse/v14n3/langford.html).
 * Typically the index or rank (n * arr.length) may be non-integer.
 * For reference: ends are clipped to the extreme values in the array;
 * For box plots: index you get is half a point too high (see
 * http://en.wikipedia.org/wiki/Percentile#Nearest_rank) but note that this definition
 * indexes from 1 rather than 0, so we subtract 1/2 (instead of add).
 *
 * @param {Array} arr - This array contains the values that make up the distribution.
 * @param {Number} n - Between 0 and 1, n = p/100 is such that we compute the p^th percentile.
 * For example, the 50th percentile (or median) corresponds to n = 0.5
 * @return {Number} - percentile
 */
exports.interp = function(arr, n) {
    if(!isNumeric(n)) throw 'n should be a finite number';
    n = n * arr.length - 0.5;
    if(n < 0) return arr[0];
    if(n > arr.length - 1) return arr[arr.length - 1];
    var frac = n % 1;
    return frac * arr[Math.ceil(n)] + (1 - frac) * arr[Math.floor(n)];
};
