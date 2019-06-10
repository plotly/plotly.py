/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

function findCategories(ax, opts) {
    var dataAttr = opts.dataAttr || ax._id.charAt(0);
    var lookup = {};
    var axData;
    var i, j;

    if(opts.axData) {
        // non-x/y case
        axData = opts.axData;
    } else {
        // x/y case
        axData = [];
        for(i = 0; i < opts.data.length; i++) {
            var trace = opts.data[i];
            if(trace[dataAttr + 'axis'] === ax._id) {
                axData.push(trace);
            }
        }
    }

    for(i = 0; i < axData.length; i++) {
        var vals = axData[i][dataAttr];
        for(j = 0; j < vals.length; j++) {
            var v = vals[j];
            if(v !== null && v !== undefined) {
                lookup[v] = 1;
            }
        }
    }

    return Object.keys(lookup);
}

/**
 * Fills in category* default and initial categories.
 *
 * @param {object} containerIn : input axis object
 * @param {object} containerOut : full axis object
 * @param {function} coerce : Lib.coerce fn wrapper
 * @param {object} opts :
 *   - data {array} : (full) data trace
 * OR
 *   - axData {array} : (full) data associated with axis being coerced here
 *   - dataAttr {string} : attribute name corresponding to coordinate array
 */
module.exports = function handleCategoryOrderDefaults(containerIn, containerOut, coerce, opts) {
    if(containerOut.type !== 'category') return;

    var arrayIn = containerIn.categoryarray;
    var isValidArray = (Array.isArray(arrayIn) && arrayIn.length > 0);

    // override default 'categoryorder' value when non-empty array is supplied
    var orderDefault;
    if(isValidArray) orderDefault = 'array';

    var order = coerce('categoryorder', orderDefault);
    var array;

    // coerce 'categoryarray' only in array order case
    if(order === 'array') {
        array = coerce('categoryarray');
    }

    // cannot set 'categoryorder' to 'array' with an invalid 'categoryarray'
    if(!isValidArray && order === 'array') {
        order = containerOut.categoryorder = 'trace';
    }

    // set up things for makeCalcdata
    if(order === 'trace') {
        containerOut._initialCategories = [];
    } else if(order === 'array') {
        containerOut._initialCategories = array.slice();
    } else {
        array = findCategories(containerOut, opts).sort();
        if(order === 'category ascending') {
            containerOut._initialCategories = array;
        } else if(order === 'category descending') {
            containerOut._initialCategories = array.reverse();
        }
    }
};
