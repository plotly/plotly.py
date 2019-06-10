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
    calc: require('../scattergeo/calc'),
    plot: require('./plot'),
    hoverPoints: require('./hover'),
    eventData: require('./event_data'),
    selectPoints: require('./select'),

    style: function(_, cd) {
        if(cd) {
            var trace = cd[0].trace;
            trace._glTrace.update(cd);
        }
    },

    moduleType: 'trace',
    name: 'scattermapbox',
    basePlotModule: require('../../plots/mapbox'),
    categories: ['mapbox', 'gl', 'symbols', 'showLegend', 'scatterlike'],
    meta: {
        hrName: 'scatter_mapbox',
        description: [
            'The data visualized as scatter point, lines or marker symbols',
            'on a Mapbox GL geographic map',
            'is provided by longitude/latitude pairs in `lon` and `lat`.'
        ].join(' ')
    }
};
