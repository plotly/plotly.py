/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

// Maybe add kernels more down the road,
// but note that the default `spanmode: 'soft'` bounds might have
// to become kernel-dependent
var kernels = {
    gaussian: function(v) {
        return (1 / Math.sqrt(2 * Math.PI)) * Math.exp(-0.5 * v * v);
    }
};

exports.makeKDE = function(calcItem, trace, vals) {
    var len = vals.length;
    var kernel = kernels.gaussian;
    var bandwidth = calcItem.bandwidth;
    var factor = 1 / (len * bandwidth);

    // don't use Lib.aggNums to skip isNumeric checks
    return function(x) {
        var sum = 0;
        for(var i = 0; i < len; i++) {
            sum += kernel((x - vals[i]) / bandwidth);
        }
        return factor * sum;
    };
};

exports.getPositionOnKdePath = function(calcItem, trace, valuePx) {
    var posLetter, valLetter;

    if(trace.orientation === 'h') {
        posLetter = 'y';
        valLetter = 'x';
    } else {
        posLetter = 'x';
        valLetter = 'y';
    }

    var pointOnPath = Lib.findPointOnPath(
        calcItem.path,
        valuePx,
        valLetter,
        {pathLength: calcItem.pathLength}
    );

    var posCenterPx = calcItem.posCenterPx;
    var posOnPath0 = pointOnPath[posLetter];
    var posOnPath1 = trace.side === 'both' ?
        2 * posCenterPx - posOnPath0 :
        posCenterPx;

    return [posOnPath0, posOnPath1];
};

exports.getKdeValue = function(calcItem, trace, valueDist) {
    var vals = calcItem.pts.map(exports.extractVal);
    var kde = exports.makeKDE(calcItem, trace, vals);
    return kde(valueDist) / calcItem.posDensityScale;
};

exports.extractVal = function(o) { return o.v; };
