/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var wrap = require('../../lib/gup').wrap;

module.exports = function calc() {
    // we don't actually need to include the trace here, since that will be added
    // by Plots.doCalcdata, and that's all we actually need later.
    return wrap({});
};
