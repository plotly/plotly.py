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
    plot: require('./plot'),
    calc: require('./calc'),
    animatable: true,
    isContainer: true, // so carpet traces get `calc` before other traces

    moduleType: 'trace',
    name: 'carpet',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['cartesian', 'svg', 'carpet', 'carpetAxis', 'notLegendIsolatable', 'noMultiCategory'],
    meta: {
        description: [
            'The data describing carpet axis layout is set in `y` and (optionally)',
            'also `x`. If only `y` is present, `x` the plot is interpreted as a',
            'cheater plot and is filled in using the `y` values.',

            '`x` and `y` may either be 2D arrays matching with each dimension matching',
            'that of `a` and `b`, or they may be 1D arrays with total length equal to',
            'that of `a` and `b`.'
        ].join(' ')
    }
};
