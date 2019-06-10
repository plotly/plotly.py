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
    colorbar: require('../heatmap/colorbar'),
    calc: require('./calc'),
    plot: require('./plot'),
    style: require('./style').style,
    styleOnSelect: require('./style').styleOnSelect,
    hoverPoints: require('./hover'),
    eventData: require('./event_data'),
    selectPoints: require('./select'),

    moduleType: 'trace',
    name: 'choropleth',
    basePlotModule: require('../../plots/geo'),
    categories: ['geo', 'noOpacity'],
    meta: {
        description: [
            'The data that describes the choropleth value-to-color mapping',
            'is set in `z`.',
            'The geographic locations corresponding to each value in `z`',
            'are set in `locations`.'
        ].join(' ')
    }
};
