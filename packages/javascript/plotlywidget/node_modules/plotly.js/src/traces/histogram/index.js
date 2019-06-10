/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/**
 * Histogram has its own attribute, defaults and calc steps,
 * but uses bar's plot to display
 * and bar's crossTraceCalc (formerly known as setPositions) for stacking and grouping
 */

/**
 * histogram errorBarsOK is debatable, but it's put in for backward compat.
 * there are use cases for it - sqrt for a simple histogram works right now,
 * constant and % work but they're not so meaningful. I guess it could be cool
 * to allow quadrature combination of errors in summed histograms...
 */

module.exports = {
    attributes: require('./attributes'),
    layoutAttributes: require('../bar/layout_attributes'),
    supplyDefaults: require('./defaults'),
    crossTraceDefaults: require('./cross_trace_defaults'),
    supplyLayoutDefaults: require('../bar/layout_defaults'),
    calc: require('./calc').calc,
    crossTraceCalc: require('../bar/cross_trace_calc').crossTraceCalc,
    plot: require('../bar/plot').plot,
    layerName: 'barlayer',
    style: require('../bar/style').style,
    styleOnSelect: require('../bar/style').styleOnSelect,
    colorbar: require('../scatter/marker_colorbar'),
    hoverPoints: require('./hover'),
    selectPoints: require('../bar/select'),
    eventData: require('./event_data'),

    moduleType: 'trace',
    name: 'histogram',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['bar-like', 'cartesian', 'svg', 'bar', 'histogram', 'oriented', 'errorBarsOK', 'showLegend'],
    meta: {
        description: [
            'The sample data from which statistics are computed is set in `x`',
            'for vertically spanning histograms and',
            'in `y` for horizontally spanning histograms.',
            'Binning options are set `xbins` and `ybins` respectively',
            'if no aggregation data is provided.'
        ].join(' ')
    }
};
