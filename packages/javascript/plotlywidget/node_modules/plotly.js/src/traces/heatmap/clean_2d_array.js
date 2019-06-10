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

module.exports = function clean2dArray(zOld, trace, xa, ya) {
    var rowlen, collen, getCollen, old2new, i, j;

    function cleanZvalue(v) {
        if(!isNumeric(v)) return undefined;
        return +v;
    }

    if(trace && trace.transpose) {
        rowlen = 0;
        for(i = 0; i < zOld.length; i++) rowlen = Math.max(rowlen, zOld[i].length);
        if(rowlen === 0) return false;
        getCollen = function(zOld) { return zOld.length; };
        old2new = function(zOld, i, j) { return zOld[j][i]; };
    } else {
        rowlen = zOld.length;
        getCollen = function(zOld, i) { return zOld[i].length; };
        old2new = function(zOld, i, j) { return zOld[i][j]; };
    }

    var padOld2new = function(zOld, i, j) {
        if(i === BADNUM || j === BADNUM) return BADNUM;
        return old2new(zOld, i, j);
    };

    function axisMapping(ax) {
        if(trace && trace.type !== 'carpet' && trace.type !== 'contourcarpet' &&
            ax && ax.type === 'category' && trace['_' + ax._id.charAt(0)].length) {
            var axLetter = ax._id.charAt(0);
            var axMapping = {};
            var traceCategories = trace['_' + axLetter + 'CategoryMap'] || trace[axLetter];
            for(i = 0; i < traceCategories.length; i++) {
                axMapping[traceCategories[i]] = i;
            }
            return function(i) {
                var ind = axMapping[ax._categories[i]];
                return ind + 1 ? ind : BADNUM;
            };
        } else {
            return Lib.identity;
        }
    }

    var xMap = axisMapping(xa);
    var yMap = axisMapping(ya);

    var zNew = new Array(rowlen);

    if(ya && ya.type === 'category') rowlen = ya._categories.length;
    for(i = 0; i < rowlen; i++) {
        if(xa && xa.type === 'category') {
            collen = xa._categories.length;
        } else {
            collen = getCollen(zOld, i);
        }
        zNew[i] = new Array(collen);
        for(j = 0; j < collen; j++) zNew[i][j] = cleanZvalue(padOld2new(zOld, yMap(i), xMap(j)));
    }

    return zNew;
};
