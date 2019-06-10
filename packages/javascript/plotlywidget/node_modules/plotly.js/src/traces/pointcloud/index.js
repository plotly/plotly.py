/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),

    // reuse the Scatter3D 'dummy' calc step so that legends know what to do
    calc: require('../scatter3d/calc'),
    plot: require('./convert'),

    moduleType: 'trace',
    name: 'pointcloud',
    basePlotModule: require('../../plots/gl2d'),
    categories: ['gl', 'gl2d', 'showLegend'],
    meta: {
        description: [
            'The data visualized as a point cloud set in `x` and `y`',
            'using the WebGl plotting engine.'
        ].join(' ')
    }
};
