/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/*
 * make a regex for matching counter ids/names ie xaxis, xaxis2, xaxis10...
 *
 * @param {string} head: the head of the pattern, eg 'x' matches 'x', 'x2', 'x10' etc.
 *      'xy' is a special case for cartesian subplots: it matches 'x2y3' etc
 * @param {Optional(string)} tail: a fixed piece after the id
 *      eg counterRegex('scene', '.annotations') for scene2.annotations etc.
 * @param {boolean} openEnded: if true, the string may continue past the match.
 * @param {boolean} matchBeginning: if false, the string may start before the match.
 */
exports.counter = function(head, tail, openEnded, matchBeginning) {
    var fullTail = (tail || '') + (openEnded ? '' : '$');
    var startWithPrefix = matchBeginning === false ? '' : '^';
    if(head === 'xy') {
        return new RegExp(startWithPrefix + 'x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?' + fullTail);
    }
    return new RegExp(startWithPrefix + head + '([2-9]|[1-9][0-9]+)?' + fullTail);
};
