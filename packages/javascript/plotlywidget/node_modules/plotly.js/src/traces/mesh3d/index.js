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
    calc: require('./calc'),
    colorbar: {
        min: 'cmin',
        max: 'cmax'
    },
    plot: require('./convert'),

    moduleType: 'trace',
    name: 'mesh3d',
    basePlotModule: require('../../plots/gl3d'),
    categories: ['gl3d'],
    meta: {
        description: [
            'Draws sets of triangles with coordinates given by',
            'three 1-dimensional arrays in `x`, `y`, `z` and',
            '(1) a sets of `i`, `j`, `k` indices',
            '(2) Delaunay triangulation or',
            '(3) the Alpha-shape algorithm or',
            '(4) the Convex-hull algorithm'
        ].join(' ')
    }
};
