/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    moduleType: 'component',
    name: 'colorbar',

    attributes: require('./attributes'),
    supplyDefaults: require('./defaults'),

    draw: require('./draw').draw,
    hasColorbar: require('./has_colorbar')
};
