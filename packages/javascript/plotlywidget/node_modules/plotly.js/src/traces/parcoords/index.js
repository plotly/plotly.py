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
    plot: require('./plot'),
    colorbar: {
        container: 'line',
        min: 'cmin',
        max: 'cmax'
    },

    moduleType: 'trace',
    name: 'parcoords',
    basePlotModule: require('./base_plot'),
    categories: ['gl', 'regl', 'noOpacity', 'noHover'],
    meta: {
        description: [
            'Parallel coordinates for multidimensional exploratory data analysis.',
            'The samples are specified in `dimensions`.',
            'The colors are set in `line.color`.'
        ].join(' ')
    }
};
