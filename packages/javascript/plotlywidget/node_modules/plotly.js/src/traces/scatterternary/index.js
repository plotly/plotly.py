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
    colorbar: require('../scatter/marker_colorbar'),
    calc: require('./calc'),
    plot: require('./plot'),
    style: require('../scatter/style').style,
    styleOnSelect: require('../scatter/style').styleOnSelect,
    hoverPoints: require('./hover'),
    selectPoints: require('../scatter/select'),
    eventData: require('./event_data'),

    moduleType: 'trace',
    name: 'scatterternary',
    basePlotModule: require('../../plots/ternary'),
    categories: ['ternary', 'symbols', 'showLegend', 'scatter-like'],
    meta: {
        hrName: 'scatter_ternary',
        description: [
            'Provides similar functionality to the *scatter* type but on a ternary phase diagram.',
            'The data is provided by at least two arrays out of `a`, `b`, `c` triplets.'
        ].join(' ')
    }
};
