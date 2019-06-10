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

exports.name = 'pie';

exports.plot = function(gd) {
    var Pie = Registry.getModule('pie');
    var cdPie = getModuleCalcData(gd.calcdata, Pie)[0];
    Pie.plot(gd, cdPie);
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var hadPie = (oldFullLayout._has && oldFullLayout._has('pie'));
    var hasPie = (newFullLayout._has && newFullLayout._has('pie'));

    if(hadPie && !hasPie) {
        oldFullLayout._pielayer.selectAll('g.trace').remove();
    }
};
