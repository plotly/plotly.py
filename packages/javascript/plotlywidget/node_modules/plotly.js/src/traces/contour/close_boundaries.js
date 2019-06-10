/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function(pathinfo, operation, perimeter, trace) {
    // Abandon all hope, ye who enter here.
    var i, v1, v2;
    var pi0 = pathinfo[0];
    var na = pi0.x.length;
    var nb = pi0.y.length;
    var z = pi0.z;
    var contours = trace.contours;

    var boundaryMax = -Infinity;
    var boundaryMin = Infinity;

    for(i = 0; i < nb; i++) {
        boundaryMin = Math.min(boundaryMin, z[i][0]);
        boundaryMin = Math.min(boundaryMin, z[i][na - 1]);
        boundaryMax = Math.max(boundaryMax, z[i][0]);
        boundaryMax = Math.max(boundaryMax, z[i][na - 1]);
    }

    for(i = 1; i < na - 1; i++) {
        boundaryMin = Math.min(boundaryMin, z[0][i]);
        boundaryMin = Math.min(boundaryMin, z[nb - 1][i]);
        boundaryMax = Math.max(boundaryMax, z[0][i]);
        boundaryMax = Math.max(boundaryMax, z[nb - 1][i]);
    }

    pi0.prefixBoundary = false;

    switch(operation) {
        case '>':
            if(contours.value > boundaryMax) {
                pi0.prefixBoundary = true;
            }
            break;
        case '<':
            if(contours.value < boundaryMin) {
                pi0.prefixBoundary = true;
            }
            break;
        case '[]':
            v1 = Math.min.apply(null, contours.value);
            v2 = Math.max.apply(null, contours.value);
            if(v2 < boundaryMin || v1 > boundaryMax) {
                pi0.prefixBoundary = true;
            }
            break;
        case '][':
            v1 = Math.min.apply(null, contours.value);
            v2 = Math.max.apply(null, contours.value);
            if(v1 < boundaryMin && v2 > boundaryMax) {
                pi0.prefixBoundary = true;
            }
            break;
    }
};
