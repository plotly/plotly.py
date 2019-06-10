/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

module.exports = {
    PTS_LINESONLY: 20,

    // fixed parameters of clustering and clipping algorithms

    // fraction of clustering tolerance "so close we don't even consider it a new point"
    minTolerance: 0.2,
    // how fast does clustering tolerance increase as you get away from the visible region
    toleranceGrowth: 10,

    // number of viewport sizes away from the visible region
    // at which we clip all lines to the perimeter
    maxScreensAway: 20,

    eventDataKeys: []
};
