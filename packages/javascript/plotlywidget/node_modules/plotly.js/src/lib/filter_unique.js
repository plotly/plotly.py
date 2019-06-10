/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


/**
 * Return news array containing only the unique items
 * found in input array.
 *
 * IMPORTANT: Note that items are considered unique
 * if `String({})` is unique. For example;
 *
 *  Lib.filterUnique([ { a: 1 }, { b: 2 } ])
 *
 *  returns [{ a: 1 }]
 *
 * and
 *
 *  Lib.filterUnique([ '1', 1 ])
 *
 *  returns ['1']
 *
 *
 * @param {array} array base array
 * @return {array} new filtered array
 */
module.exports = function filterUnique(array) {
    var seen = {};
    var out = [];
    var j = 0;

    for(var i = 0; i < array.length; i++) {
        var item = array[i];

        if(seen[item] !== 1) {
            seen[item] = 1;
            out[j++] = item;
        }
    }

    return out;
};
