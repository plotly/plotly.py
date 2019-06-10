/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/** Filter out object items with visible !== true
 *  insider array container.
 *
 *  @param {array of objects} container
 *  @return {array of objects} of length <= container
 *
 */
module.exports = function filterVisible(container) {
    var filterFn = isCalcData(container) ? calcDataFilter : baseFilter;
    var out = [];

    for(var i = 0; i < container.length; i++) {
        var item = container[i];
        if(filterFn(item)) out.push(item);
    }

    return out;
};

function baseFilter(item) {
    return item.visible === true;
}

function calcDataFilter(item) {
    var trace = item[0].trace;
    return trace.visible === true && trace._length !== 0;
}

function isCalcData(cont) {
    return (
        Array.isArray(cont) &&
        Array.isArray(cont[0]) &&
        cont[0][0] &&
        cont[0][0].trace
    );
}
