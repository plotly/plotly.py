/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');
var loggers = require('./loggers');
var identity = require('./identity');

// don't trust floating point equality - fraction of bin size to call
// "on the line" and ensure that they go the right way specified by
// linelow
var roundingError = 1e-9;


/**
 * findBin - find the bin for val - note that it can return outside the
 * bin range any pos. or neg. integer for linear bins, or -1 or
 * bins.length-1 for explicit.
 * bins is either an object {start,size,end} or an array length #bins+1
 * bins can be either increasing or decreasing but must be monotonic
 * for linear bins, we can just calculate. For listed bins, run a binary
 * search linelow (truthy) says the bin boundary should be attributed to
 * the lower bin rather than the default upper bin
 */
exports.findBin = function(val, bins, linelow) {
    if(isNumeric(bins.start)) {
        return linelow ?
            Math.ceil((val - bins.start) / bins.size - roundingError) - 1 :
            Math.floor((val - bins.start) / bins.size + roundingError);
    } else {
        var n1 = 0;
        var n2 = bins.length;
        var c = 0;
        var binSize = (n2 > 1) ? (bins[n2 - 1] - bins[0]) / (n2 - 1) : 1;
        var n, test;
        if(binSize >= 0) {
            test = linelow ? lessThan : lessOrEqual;
        } else {
            test = linelow ? greaterOrEqual : greaterThan;
        }
        val += binSize * roundingError * (linelow ? -1 : 1) * (binSize >= 0 ? 1 : -1);
        // c is just to avoid infinite loops if there's an error
        while(n1 < n2 && c++ < 100) {
            n = Math.floor((n1 + n2) / 2);
            if(test(bins[n], val)) n1 = n + 1;
            else n2 = n;
        }
        if(c > 90) loggers.log('Long binary search...');
        return n1 - 1;
    }
};

function lessThan(a, b) { return a < b; }
function lessOrEqual(a, b) { return a <= b; }
function greaterThan(a, b) { return a > b; }
function greaterOrEqual(a, b) { return a >= b; }

exports.sorterAsc = function(a, b) { return a - b; };
exports.sorterDes = function(a, b) { return b - a; };

/**
 * find distinct values in an array, lumping together ones that appear to
 * just be off by a rounding error
 * return the distinct values and the minimum difference between any two
 */
exports.distinctVals = function(valsIn) {
    var vals = valsIn.slice();  // otherwise we sort the original array...
    vals.sort(exports.sorterAsc);

    var l = vals.length - 1;
    var minDiff = (vals[l] - vals[0]) || 1;
    var errDiff = minDiff / (l || 1) / 10000;
    var v2 = [vals[0]];

    for(var i = 0; i < l; i++) {
        // make sure values aren't just off by a rounding error
        if(vals[i + 1] > vals[i] + errDiff) {
            minDiff = Math.min(minDiff, vals[i + 1] - vals[i]);
            v2.push(vals[i + 1]);
        }
    }

    return {vals: v2, minDiff: minDiff};
};

/**
 * return the smallest element from (sorted) array arrayIn that's bigger than val,
 * or (reverse) the largest element smaller than val
 * used to find the best tick given the minimum (non-rounded) tick
 * particularly useful for date/time where things are not powers of 10
 * binary search is probably overkill here...
 */
exports.roundUp = function(val, arrayIn, reverse) {
    var low = 0;
    var high = arrayIn.length - 1;
    var mid;
    var c = 0;
    var dlow = reverse ? 0 : 1;
    var dhigh = reverse ? 1 : 0;
    var rounded = reverse ? Math.ceil : Math.floor;
    // c is just to avoid infinite loops if there's an error
    while(low < high && c++ < 100) {
        mid = rounded((low + high) / 2);
        if(arrayIn[mid] <= val) low = mid + dlow;
        else high = mid - dhigh;
    }
    return arrayIn[low];
};

/**
 * Tweak to Array.sort(sortFn) that improves performance for pre-sorted arrays
 *
 * Note that newer browsers (such as Chrome v70+) are starting to pick up
 * on pre-sorted arrays which may render the following optimization unnecessary
 * in the future.
 *
 * Motivation: sometimes we need to sort arrays but the input is likely to
 * already be sorted. Browsers don't seem to pick up on pre-sorted arrays,
 * and in fact Chrome is actually *slower* sorting pre-sorted arrays than purely
 * random arrays. FF is at least faster if the array is pre-sorted, but still
 * not as fast as it could be.
 * Here's how this plays out sorting a length-1e6 array:
 *
 * Calls to Sort FN  |  Chrome bare  |  FF bare  |  Chrome tweak  |  FF tweak
 *                   |  v68.0 Mac    |  v61.0 Mac|                |
 * ------------------+---------------+-----------+----------------+------------
 * ordered           |  30.4e6       |  10.1e6   |  1e6           |  1e6
 * reversed          |  29.4e6       |  9.9e6    |  1e6 + reverse |  1e6 + reverse
 * random            |  ~21e6        |  ~18.7e6  |  ~21e6         |  ~18.7e6
 *
 * So this is a substantial win for pre-sorted (ordered or exactly reversed)
 * arrays. Including this wrapper on an unsorted array adds a penalty that will
 * in general be only a few calls to the sort function. The only case this
 * penalty will be significant is if the array is mostly sorted but there are
 * a few unsorted items near the end, but the penalty is still at most N calls
 * out of (for N=1e6) ~20N total calls
 *
 * @param {Array} array: the array, to be sorted in place
 * @param {function} sortFn: As in Array.sort, function(a, b) that puts
 *     item a before item b if the return is negative, a after b if positive,
 *     and no change if zero.
 * @return {Array}: the original array, sorted in place.
 */
exports.sort = function(array, sortFn) {
    var notOrdered = 0;
    var notReversed = 0;
    for(var i = 1; i < array.length; i++) {
        var pairOrder = sortFn(array[i], array[i - 1]);
        if(pairOrder < 0) notOrdered = 1;
        else if(pairOrder > 0) notReversed = 1;
        if(notOrdered && notReversed) return array.sort(sortFn);
    }
    return notReversed ? array : array.reverse();
};

/**
 * find index in array 'arr' that minimizes 'fn'
 *
 * @param {array} arr : array where to search
 * @param {fn (optional)} fn : function to minimize,
 *   if not given, fn is the identity function
 * @return {integer}
 */
exports.findIndexOfMin = function(arr, fn) {
    fn = fn || identity;

    var min = Infinity;
    var ind;

    for(var i = 0; i < arr.length; i++) {
        var v = fn(arr[i]);
        if(v < min) {
            min = v;
            ind = i;
        }
    }
    return ind;
};
