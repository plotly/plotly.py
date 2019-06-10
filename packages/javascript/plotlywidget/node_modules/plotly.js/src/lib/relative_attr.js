/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

// ASCEND: chop off the last nesting level - either [<n>] or .<key> - to ascend
// the attribute tree. the remaining attrString is in match[1]
var ASCEND = /^(.*)(\.[^\.\[\]]+|\[\d\])$/;

// SIMPLEATTR: is this an un-nested attribute? (no dots or brackets)
var SIMPLEATTR = /^[^\.\[\]]+$/;

/*
 * calculate a relative attribute string, similar to a relative path
 *
 * @param {string} baseAttr:
 *   an attribute string, such as 'annotations[3].x'. The "current location"
 *   is the attribute string minus the last component ('annotations[3]')
 * @param {string} relativeAttr:
 *   a route to the desired attribute string, using '^' to ascend
 *
 * @return {string} attrString:
 *   for example:
 *     relativeAttr('annotations[3].x', 'y') = 'annotations[3].y'
 *     relativeAttr('annotations[3].x', '^[2].z') = 'annotations[2].z'
 *     relativeAttr('annotations[3].x', '^^margin') = 'margin'
 *     relativeAttr('annotations[3].x', '^^margin.r') = 'margin.r'
 */
module.exports = function(baseAttr, relativeAttr) {
    while(relativeAttr) {
        var match = baseAttr.match(ASCEND);

        if(match) baseAttr = match[1];
        else if(baseAttr.match(SIMPLEATTR)) baseAttr = '';
        else throw new Error('bad relativeAttr call:' + [baseAttr, relativeAttr]);

        if(relativeAttr.charAt(0) === '^') relativeAttr = relativeAttr.slice(1);
        else break;
    }

    if(baseAttr && relativeAttr.charAt(0) !== '[') {
        return baseAttr + '.' + relativeAttr;
    }
    return baseAttr + relativeAttr;
};
