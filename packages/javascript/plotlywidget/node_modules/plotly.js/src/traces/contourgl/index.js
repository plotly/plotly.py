/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var overrideAll = require('../../plot_api/edit_types').overrideAll;

module.exports = {
    attributes: overrideAll(require('../contour/attributes'), 'calc', 'nested'),
    supplyDefaults: require('../contour/defaults'),
    colorbar: require('../contour/colorbar'),

    calc: require('../contour/calc'),
    plot: require('./convert'),

    moduleType: 'trace',
    name: 'contourgl',
    basePlotModule: require('../../plots/gl2d'),
    categories: ['gl', 'gl2d', '2dMap'],
    meta: {
        description: [
            'WebGL contour (beta)'
        ].join(' ')
    }
};
