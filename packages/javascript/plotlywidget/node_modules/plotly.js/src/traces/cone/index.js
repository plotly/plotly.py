/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    moduleType: 'trace',
    name: 'cone',
    basePlotModule: require('../../plots/gl3d'),
    categories: ['gl3d'],

    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),
    colorbar: {
        min: 'cmin',
        max: 'cmax'
    },
    calc: require('./calc'),
    plot: require('./convert'),
    eventData: function(out, pt) {
        out.norm = pt.traceCoordinate[6];
        return out;
    },

    meta: {
        description: [
            'Use cone traces to visualize vector fields.',
            '',
            'Specify a vector field using 6 1D arrays,',
            '3 position arrays `x`, `y` and `z`',
            'and 3 vector component arrays `u`, `v`, `w`.',
            'The cones are drawn exactly at the positions given',
            'by `x`, `y` and `z`.'
        ].join(' ')
    }
};
