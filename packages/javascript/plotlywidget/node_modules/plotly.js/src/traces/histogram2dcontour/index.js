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
    crossTraceDefaults: require('../histogram/cross_trace_defaults'),
    calc: require('../contour/calc'),
    plot: require('../contour/plot').plot,
    layerName: 'contourlayer',
    style: require('../contour/style'),
    colorbar: require('../contour/colorbar'),
    hoverPoints: require('../contour/hover'),

    moduleType: 'trace',
    name: 'histogram2dcontour',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['cartesian', 'svg', '2dMap', 'contour', 'histogram', 'showLegend'],
    meta: {
        hrName: 'histogram_2d_contour',
        description: [
            'The sample data from which statistics are computed is set in `x`',
            'and `y` (where `x` and `y` represent marginal distributions,',
            'binning is set in `xbins` and `ybins` in this case)',
            'or `z` (where `z` represent the 2D distribution and binning set,',
            'binning is set by `x` and `y` in this case).',
            'The resulting distribution is visualized as a contour plot.'
        ].join(' ')
    }
};
