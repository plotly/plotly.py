/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var getModuleCalcData = require('../../plots/get_data').getModuleCalcData;

var name = exports.name = 'sunburst';

exports.plot = function(gd, traces, transitionOpts, makeOnCompleteCallback) {
    var _module = Registry.getModule(name);
    var cdmodule = getModuleCalcData(gd.calcdata, _module)[0];
    _module.plot(gd, cdmodule, transitionOpts, makeOnCompleteCallback);
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var had = (oldFullLayout._has && oldFullLayout._has(name));
    var has = (newFullLayout._has && newFullLayout._has(name));

    if(had && !has) {
        oldFullLayout._sunburstlayer.selectAll('g.trace').remove();
    }
};
