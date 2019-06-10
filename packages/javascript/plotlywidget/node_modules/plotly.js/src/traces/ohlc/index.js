/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    moduleType: 'trace',
    name: 'ohlc',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['cartesian', 'svg', 'showLegend'],
    meta: {
        description: [
            'The ohlc (short for Open-High-Low-Close) is a style of financial chart describing',
            'open, high, low and close for a given `x` coordinate (most likely time).',

            'The tip of the lines represent the `low` and `high` values and',
            'the horizontal segments represent the `open` and `close` values.',

            'Sample points where the close value is higher (lower) then the open',
            'value are called increasing (decreasing).',

            'By default, increasing items are drawn in green whereas',
            'decreasing are drawn in red.'
        ].join(' ')
    },

    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),
    calc: require('./calc').calc,
    plot: require('./plot'),
    style: require('./style'),
    hoverPoints: require('./hover').hoverPoints,
    selectPoints: require('./select')
};
