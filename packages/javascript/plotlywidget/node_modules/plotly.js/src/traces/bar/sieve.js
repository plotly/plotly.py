/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = Sieve;

var distinctVals = require('../../lib').distinctVals;
var BADNUM = require('../../constants/numerical').BADNUM;

/**
 * Helper class to sieve data from traces into bins
 *
 * @class
 *
 * @param {Array} traces
*   Array of calculated traces
 * @param {object} opts
 *  - @param {boolean} [sepNegVal]
 *      If true, then split data at the same position into a bar
 *      for positive values and another for negative values
 *  - @param {boolean} [overlapNoMerge]
 *     If true, then don't merge overlapping bars into a single bar
 */
function Sieve(traces, opts) {
    this.traces = traces;
    this.sepNegVal = opts.sepNegVal;
    this.overlapNoMerge = opts.overlapNoMerge;

    // for single-bin histograms - see histogram/calc
    var width1 = Infinity;

    var positions = [];
    for(var i = 0; i < traces.length; i++) {
        var trace = traces[i];
        for(var j = 0; j < trace.length; j++) {
            var bar = trace[j];
            if(bar.p !== BADNUM) positions.push(bar.p);
        }
        if(trace[0] && trace[0].width1) {
            width1 = Math.min(trace[0].width1, width1);
        }
    }
    this.positions = positions;

    var dv = distinctVals(positions);
    this.distinctPositions = dv.vals;
    if(dv.vals.length === 1 && width1 !== Infinity) this.minDiff = width1;
    else this.minDiff = Math.min(dv.minDiff, width1);

    this.binWidth = this.minDiff;

    this.bins = {};
}

/**
 * Sieve datum
 *
 * @method
 * @param {number} position
 * @param {number} value
 * @returns {number} Previous bin value
 */
Sieve.prototype.put = function put(position, value) {
    var label = this.getLabel(position, value);
    var oldValue = this.bins[label] || 0;

    this.bins[label] = oldValue + value;

    return oldValue;
};

/**
 * Get current bin value for a given datum
 *
 * @method
 * @param {number} position  Position of datum
 * @param {number} [value]   Value of datum
 *                           (required if this.sepNegVal is true)
 * @returns {number} Current bin value
 */
Sieve.prototype.get = function get(position, value) {
    var label = this.getLabel(position, value);
    return this.bins[label] || 0;
};

/**
 * Get bin label for a given datum
 *
 * @method
 * @param {number} position  Position of datum
 * @param {number} [value]   Value of datum
 *                           (required if this.sepNegVal is true)
 * @returns {string} Bin label
 * (prefixed with a 'v' if value is negative and this.sepNegVal is
 * true; otherwise prefixed with '^')
 */
Sieve.prototype.getLabel = function getLabel(position, value) {
    var prefix = (value < 0 && this.sepNegVal) ? 'v' : '^';
    var label = (this.overlapNoMerge) ?
        position :
        Math.round(position / this.binWidth);
    return prefix + label;
};
