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

exports.name = 'funnelarea';

exports.plot = function(gd) {
    var Funnelarea = Registry.getModule('funnelarea');
    var cdFunnelarea = getModuleCalcData(gd.calcdata, Funnelarea)[0];
    Funnelarea.plot(gd, cdFunnelarea);
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var hadFunnelarea = (oldFullLayout._has && oldFullLayout._has('funnelarea'));
    var hasFunnelarea = (newFullLayout._has && newFullLayout._has('funnelarea'));

    if(hadFunnelarea && !hasFunnelarea) {
        oldFullLayout._funnelarealayer.selectAll('g.trace').remove();
    }
};
