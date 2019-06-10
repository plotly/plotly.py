/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    attr: 'subplot',
    name: 'polar',

    axisNames: ['angularaxis', 'radialaxis'],
    axisName2dataArray: {angularaxis: 'theta', radialaxis: 'r'},

    layerNames: [
        'draglayer',
        'plotbg',
        'backplot',
        'angular-grid',
        'radial-grid',
        'frontplot',
        'angular-line',
        'radial-line',
        'angular-axis',
        'radial-axis'
    ],

    radialDragBoxSize: 50,
    angularDragBoxSize: 30,
    cornerLen: 25,
    cornerHalfWidth: 2,

    // pixels to move mouse before you stop clamping to starting point
    MINDRAG: 8,
    // smallest radial distance [px] allowed for a zoombox
    MINZOOM: 20,
    // distance [px] off (r=0) or (r=radius) where we transition
    // from single-sided to two-sided radial zoom
    OFFEDGE: 20
};
