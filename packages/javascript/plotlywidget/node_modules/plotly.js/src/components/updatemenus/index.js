/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var constants = require('./constants');

module.exports = {
    moduleType: 'component',
    name: constants.name,

    layoutAttributes: require('./attributes'),
    supplyLayoutDefaults: require('./defaults'),

    draw: require('./draw')
};
