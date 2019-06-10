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
    supplyDefaults: require('./defaults').supplyDefaults,
    calc: require('./calc'),
    colorbar: {
        min: 'cmin',
        max: 'cmax'
    },
    plot: require('./convert').createIsosurfaceTrace,

    moduleType: 'trace',
    name: 'isosurface',
    basePlotModule: require('../../plots/gl3d'),
    categories: ['gl3d'],
    meta: {
        description: [
            'Draws isosurfaces between iso-min and iso-max values with coordinates given by',
            'four 1-dimensional arrays containing the `value`, `x`, `y` and `z` of every vertex',
            'of a uniform or non-uniform 3-D grid. Horizontal or vertical slices, caps as well as',
            'spaceframe between iso-min and iso-max values could also be drawn using this trace.'
        ].join(' ')
    }
};
