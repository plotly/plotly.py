/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/**
 * mergeLength: set trace length as the minimum of all dimension data lengths
 *     and propagates this length into each dimension
 *
 * @param {object} traceOut: the fullData trace
 * @param {Array(object)} dimensions: array of dimension objects
 * @param {string} dataAttr: the attribute of each dimension containing the data
 * @param {integer} len: an already-existing length from other attributes
 */
module.exports = function(traceOut, dimensions, dataAttr, len) {
    if(!len) len = Infinity;
    var i, dimi;
    for(i = 0; i < dimensions.length; i++) {
        dimi = dimensions[i];
        if(dimi.visible) len = Math.min(len, dimi[dataAttr].length);
    }
    if(len === Infinity) len = 0;

    traceOut._length = len;
    for(i = 0; i < dimensions.length; i++) {
        dimi = dimensions[i];
        if(dimi.visible) dimi._length = len;
    }

    return len;
};
