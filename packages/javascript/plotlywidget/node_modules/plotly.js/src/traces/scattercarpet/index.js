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
    name: 'scattercarpet',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['svg', 'carpet', 'symbols', 'showLegend', 'carpetDependent', 'zoomScale'],
    meta: {
        hrName: 'scatter_carpet',
        description: [
            'Plots a scatter trace on either the first carpet axis or the',
            'carpet axis with a matching `carpet` attribute.'
        ].join(' ')
    }
};
