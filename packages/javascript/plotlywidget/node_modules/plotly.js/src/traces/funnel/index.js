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
    layoutAttributes: require('./layout_attributes'),
    supplyDefaults: require('./defaults').supplyDefaults,
    crossTraceDefaults: require('./defaults').crossTraceDefaults,
    supplyLayoutDefaults: require('./layout_defaults'),
    calc: require('./calc'),
    crossTraceCalc: require('./cross_trace_calc'),
    plot: require('./plot'),
    style: require('./style').style,
    hoverPoints: require('./hover'),
    selectPoints: require('../bar/select'),

    moduleType: 'trace',
    name: 'funnel',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['bar-like', 'cartesian', 'svg', 'oriented', 'showLegend', 'zoomScale'],
    meta: {
        description: [
            'Visualize stages in a process using length-encoded bars. This trace can be used',
            'to show data in either a part-to-whole representation wherein each item appears',
            'in a single stage, or in a "drop-off" representation wherein each item appears in',
            'each stage it traversed. See also the "funnelarea" trace type for a different',
            'approach to visualizing funnel data.'
        ].join(' ')
    }
};
