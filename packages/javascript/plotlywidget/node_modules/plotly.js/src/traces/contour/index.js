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
    calc: require('./calc'),
    plot: require('./plot').plot,
    style: require('./style'),
    colorbar: require('./colorbar'),
    hoverPoints: require('./hover'),

    moduleType: 'trace',
    name: 'contour',
    basePlotModule: require('../../plots/cartesian'),
    categories: ['cartesian', 'svg', '2dMap', 'contour', 'showLegend'],
    meta: {
        description: [
            'The data from which contour lines are computed is set in `z`.',
            'Data in `z` must be a {2D array} of numbers.',

            'Say that `z` has N rows and M columns, then by default,',
            'these N rows correspond to N y coordinates',
            '(set in `y` or auto-generated) and the M columns',
            'correspond to M x coordinates (set in `x` or auto-generated).',
            'By setting `transpose` to *true*, the above behavior is flipped.'
        ].join(' ')
    }
};
