/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var subtypes = require('./subtypes');

module.exports = {
    hasLines: subtypes.hasLines,
    hasMarkers: subtypes.hasMarkers,
    hasText: subtypes.hasText,
    isBubble: subtypes.isBubble,

    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),
    crossTraceDefaults: require('./cross_trace_defaults'),
    calc: require('./calc').calc,
    crossTraceCalc: require('./cross_trace_calc'),
    arraysToCalcdata: require('./arrays_to_calcdata'),
    plot: require('./plot'),
    colorbar: require('./marker_colorbar'),
    style: require('./style').style,
    styleOnSelect: require('./style').styleOnSelect,
    hoverPoints: require('./hover'),
    selectPoints: require('./select'),
    animatable: true,

    moduleType: 'trace',
    name: 'scatter',
    basePlotModule: require('../../plots/cartesian'),
    categories: [
        'cartesian', 'svg', 'symbols', 'errorBarsOK', 'showLegend', 'scatter-like',
        'zoomScale'
    ],
    meta: {
        description: [
            'The scatter trace type encompasses line charts, scatter charts, text charts, and bubble charts.',
            'The data visualized as scatter point or lines is set in `x` and `y`.',
            'Text (appearing either on the chart or on hover only) is via `text`.',
            'Bubble charts are achieved by setting `marker.size` and/or `marker.color`',
            'to numerical arrays.'
        ].join(' ')
    }
};
