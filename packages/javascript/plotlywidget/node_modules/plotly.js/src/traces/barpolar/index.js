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
    name: 'barpolar',
    basePlotModule: require('../../plots/polar'),
    categories: ['polar', 'bar', 'showLegend'],

    attributes: require('./attributes'),
    layoutAttributes: require('./layout_attributes'),
    supplyDefaults: require('./defaults'),
    supplyLayoutDefaults: require('./layout_defaults'),

    calc: require('./calc').calc,
    crossTraceCalc: require('./calc').crossTraceCalc,

    plot: require('./plot'),
    colorbar: require('../scatter/marker_colorbar'),
    style: require('../bar/style').style,

    hoverPoints: require('./hover'),
    selectPoints: require('../bar/select'),

    meta: {
        hrName: 'bar_polar',
        description: [
            'The data visualized by the radial span of the bars is set in `r`'
            // 'if `orientation` is set th *radial* (the default)',
            // 'and the labels are set in `theta`.',
            // 'By setting `orientation` to *angular*, the roles are interchanged.'
        ].join(' ')
    }
};
