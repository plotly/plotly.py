/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Colorscale = require('../../components/colorscale');

var heatmapCalc = require('../heatmap/calc');
var setContours = require('./set_contours');
var endPlus = require('./end_plus');

// most is the same as heatmap calc, then adjust it
// though a few things inside heatmap calc still look for
// contour maps, because the makeBoundArray calls are too entangled
module.exports = function calc(gd, trace) {
    var cd = heatmapCalc(gd, trace);

    var zOut = cd[0].z;
    setContours(trace, zOut);

    var contours = trace.contours;
    var cOpts = Colorscale.extractOpts(trace);
    var cVals;

    if(contours.coloring === 'heatmap' && cOpts.auto && trace.autocontour === false) {
        var start = contours.start;
        var end = endPlus(contours);
        var cs = contours.size || 1;
        var nc = Math.floor((end - start) / cs) + 1;

        if(!isFinite(cs)) {
            cs = 1;
            nc = 1;
        }

        var min0 = start - cs / 2;
        var max0 = min0 + nc * cs;
        cVals = [min0, max0];
    } else {
        cVals = zOut;
    }

    Colorscale.calc(gd, trace, {vals: cVals, cLetter: 'z'});

    return cd;
};
