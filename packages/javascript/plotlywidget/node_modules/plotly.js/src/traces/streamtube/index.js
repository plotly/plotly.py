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
    name: 'streamtube',
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
        out.tubex = out.x;
        out.tubey = out.y;
        out.tubez = out.z;

        out.tubeu = pt.traceCoordinate[3];
        out.tubev = pt.traceCoordinate[4];
        out.tubew = pt.traceCoordinate[5];

        out.norm = pt.traceCoordinate[6];
        out.divergence = pt.traceCoordinate[7];

        // Does not correspond to input x/y/z, so delete them
        delete out.x;
        delete out.y;
        delete out.z;

        return out;
    },

    meta: {
        description: [
            'Use a streamtube trace to visualize flow in a vector field.',
            '',
            'Specify a vector field using 6 1D arrays of equal length,',
            '3 position arrays `x`, `y` and `z`',
            'and 3 vector component arrays `u`, `v`, and `w`.',
            '',
            'By default, the tubes\' starting positions will be cut from the vector field\'s',
            'x-z plane at its minimum y value.',
            'To specify your own starting position, use attributes `starts.x`, `starts.y`',
            'and `starts.z`.'
        ].join(' ')
    }
};
