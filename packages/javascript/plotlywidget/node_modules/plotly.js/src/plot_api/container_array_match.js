/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Registry = require('../registry');

/*
 * containerArrayMatch: does this attribute string point into a
 * layout container array?
 *
 * @param {String} astr: an attribute string, like *annotations[2].text*
 *
 * @returns {Object | false} Returns false if `astr` doesn't match a container
 *  array. If it does, returns:
 *     {array: {String}, index: {Number}, property: {String}}
 *  ie the attribute string for the array, the index within the array (or ''
 *  if the whole array) and the property within that (or '' if the whole array
 *  or the whole object)
 */
module.exports = function containerArrayMatch(astr) {
    var rootContainers = Registry.layoutArrayContainers;
    var regexpContainers = Registry.layoutArrayRegexes;
    var rootPart = astr.split('[')[0];
    var arrayStr;
    var match;

    // look for regexp matches first, because they may be nested inside root matches
    // eg updatemenus[i].buttons is nested inside updatemenus
    for(var i = 0; i < regexpContainers.length; i++) {
        match = astr.match(regexpContainers[i]);
        if(match && match.index === 0) {
            arrayStr = match[0];
            break;
        }
    }

    // now look for root matches
    if(!arrayStr) arrayStr = rootContainers[rootContainers.indexOf(rootPart)];

    if(!arrayStr) return false;

    var tail = astr.substr(arrayStr.length);
    if(!tail) return {array: arrayStr, index: '', property: ''};

    match = tail.match(/^\[(0|[1-9][0-9]*)\](\.(.+))?$/);
    if(!match) return false;

    return {array: arrayStr, index: Number(match[1]), property: match[3] || ''};
};
