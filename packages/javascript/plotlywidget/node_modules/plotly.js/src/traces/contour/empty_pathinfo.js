/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var constraintMapping = require('./constraint_mapping');
var endPlus = require('./end_plus');

module.exports = function emptyPathinfo(contours, plotinfo, cd0) {
    var contoursFinal = (contours.type === 'constraint') ?
        constraintMapping[contours._operation](contours.value) :
        contours;

    var cs = contoursFinal.size;
    var pathinfo = [];
    var end = endPlus(contoursFinal);

    var carpet = cd0.trace._carpetTrace;

    var basePathinfo = carpet ? {
        // store axes so we can convert to px
        xaxis: carpet.aaxis,
        yaxis: carpet.baxis,
        // full data arrays to use for interpolation
        x: cd0.a,
        y: cd0.b
    } : {
        xaxis: plotinfo.xaxis,
        yaxis: plotinfo.yaxis,
        x: cd0.x,
        y: cd0.y
    };

    for(var ci = contoursFinal.start; ci < end; ci += cs) {
        pathinfo.push(Lib.extendFlat({
            level: ci,
            // all the cells with nontrivial marching index
            crossings: {},
            // starting points on the edges of the lattice for each contour
            starts: [],
            // all unclosed paths (may have less items than starts,
            // if a path is closed by rounding)
            edgepaths: [],
            // all closed paths
            paths: [],
            z: cd0.z,
            smoothing: cd0.trace.line.smoothing
        }, basePathinfo));

        if(pathinfo.length > 1000) {
            Lib.warn('Too many contours, clipping at 1000', contours);
            break;
        }
    }
    return pathinfo;
};
