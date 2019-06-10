/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');
var BADNUM = require('../../constants/numerical').BADNUM;

module.exports = function autoType(array, calendar, opts) {
    opts = opts || {};

    if(!opts.noMultiCategory && multiCategory(array)) return 'multicategory';
    if(moreDates(array, calendar)) return 'date';
    if(category(array)) return 'category';
    if(linearOK(array)) return 'linear';
    else return '-';
};

// is there at least one number in array? If not, we should leave
// ax.type empty so it can be autoset later
function linearOK(array) {
    if(!array) return false;

    for(var i = 0; i < array.length; i++) {
        if(isNumeric(array[i])) return true;
    }

    return false;
}

// does the array a have mostly dates rather than numbers?
// note: some values can be neither (such as blanks, text)
// 2- or 4-digit integers can be both, so require twice as many
// dates as non-dates, to exclude cases with mostly 2 & 4 digit
// numbers and a few dates
// as with categories, consider DISTINCT values only.
function moreDates(a, calendar) {
    // test at most 1000 points, evenly spaced
    var inc = Math.max(1, (a.length - 1) / 1000);
    var dcnt = 0;
    var ncnt = 0;
    var seen = {};

    for(var i = 0; i < a.length; i += inc) {
        var ai = a[Math.round(i)];
        var stri = String(ai);
        if(seen[stri]) continue;
        seen[stri] = 1;

        if(Lib.isDateTime(ai, calendar)) dcnt += 1;
        if(isNumeric(ai)) ncnt += 1;
    }

    return (dcnt > ncnt * 2);
}

// are the (x,y)-values in gd.data mostly text?
// require twice as many DISTINCT categories as distinct numbers
function category(a) {
    // test at most 1000 points
    var inc = Math.max(1, (a.length - 1) / 1000);
    var curvenums = 0;
    var curvecats = 0;
    var seen = {};

    for(var i = 0; i < a.length; i += inc) {
        var ai = a[Math.round(i)];
        var stri = String(ai);
        if(seen[stri]) continue;
        seen[stri] = 1;

        if(typeof ai === 'boolean') curvecats++;
        else if(Lib.cleanNumber(ai) !== BADNUM) curvenums++;
        else if(typeof ai === 'string') curvecats++;
    }

    return curvecats > curvenums * 2;
}

// very-loose requirements for multicategory,
// trace modules that should never auto-type to multicategory
// should be declared with 'noMultiCategory'
function multiCategory(a) {
    return Lib.isArrayOrTypedArray(a[0]) && Lib.isArrayOrTypedArray(a[1]);
}
