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
    crossTraceCalc: require('./cross_trace_calc').crossTraceCalc,
    colorbar: require('../scatter/marker_colorbar'),
    arraysToCalcdata: require('./arrays_to_calcdata'),
    plot: require('./plot').plot,
    style: require('./style').style,
    styleOnSelect: require('./style').styleOnSelect,
    hoverPoints: require('./hover').hoverPoints,
    selectPoints: require('./select'),

    moduleType: 'trace',
    name: 'bar',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['bar-like', 'cartesian', 'svg', 'bar', 'oriented', 'errorBarsOK', 'showLegend', 'zoomScale'],
    meta: {
        description: [
            'The data visualized by the span of the bars is set in `y`',
            'if `orientation` is set th *v* (the default)',
            'and the labels are set in `x`.',
            'By setting `orientation` to *h*, the roles are interchanged.'
        ].join(' ')
    }
};
