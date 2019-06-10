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
    colorbar: require('../contour/colorbar'),
    calc: require('./calc'),
    plot: require('./plot'),
    style: require('../contour/style'),

    moduleType: 'trace',
    name: 'contourcarpet',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['cartesian', 'svg', 'carpet', 'contour', 'symbols', 'showLegend', 'hasLines', 'carpetDependent'],
    meta: {
        hrName: 'contour_carpet',
        description: [
            'Plots contours on either the first carpet axis or the',
            'carpet axis with a matching `carpet` attribute. Data `z`',
            'is interpreted as matching that of the corresponding carpet',
            'axis.'
        ].join(' ')
    }
};
