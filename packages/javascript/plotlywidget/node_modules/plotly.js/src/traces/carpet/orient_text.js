/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

module.exports = function orientText(trace, xaxis, yaxis, xy, dxy, refDxy) {
    var dx = dxy[0] * trace.dpdx(xaxis);
    var dy = dxy[1] * trace.dpdy(yaxis);
    var flip = 1;

    var offsetMultiplier = 1.0;
    if(refDxy) {
        var l1 = Math.sqrt(dxy[0] * dxy[0] + dxy[1] * dxy[1]);
        var l2 = Math.sqrt(refDxy[0] * refDxy[0] + refDxy[1] * refDxy[1]);
        var dot = (dxy[0] * refDxy[0] + dxy[1] * refDxy[1]) / l1 / l2;
        offsetMultiplier = Math.max(0.0, dot);
    }

    var angle = Math.atan2(dy, dx) * 180 / Math.PI;
    if(angle < -90) {
        angle += 180;
        flip = -flip;
    } else if(angle > 90) {
        angle -= 180;
        flip = -flip;
    }

    return {
        angle: angle,
        flip: flip,
        p: trace.c2p(xy, xaxis, yaxis),
        offsetMultplier: offsetMultiplier
    };
};
