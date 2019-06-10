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
    colorbar: {
        min: 'cmin',
        max: 'cmax'
    },
    calc: require('./calc'),
    plot: require('./convert'),

    moduleType: 'trace',
    name: 'surface',
    basePlotModule: require('../../plots/gl3d'),
    categories: ['gl3d', '2dMap', 'noOpacity'],
    meta: {
        description: [
            'The data the describes the coordinates of the surface is set in `z`.',
            'Data in `z` should be a {2D array}.',

            'Coordinates in `x` and `y` can either be 1D {arrays}',
            'or {2D arrays} (e.g. to graph parametric surfaces).',

            'If not provided in `x` and `y`, the x and y coordinates are assumed',
            'to be linear starting at 0 with a unit step.',

            'The color scale corresponds to the `z` values by default.',
            'For custom color scales, use `surfacecolor` which should be a {2D array},',
            'where its bounds can be controlled using `cmin` and `cmax`.'
        ].join(' ')
    }
};
