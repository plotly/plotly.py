/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var getModuleCalcData = require('../../plots/get_data').getModuleCalcData;
var parcatsPlot = require('./plot');

var PARCATS = 'parcats';
exports.name = PARCATS;

exports.plot = function(gd, traces, transitionOpts, makeOnCompleteCallback) {
    var cdModuleAndOthers = getModuleCalcData(gd.calcdata, PARCATS);

    if(cdModuleAndOthers.length) {
        var calcData = cdModuleAndOthers[0];
        parcatsPlot(gd, calcData, transitionOpts, makeOnCompleteCallback);
    }
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var hadTable = (oldFullLayout._has && oldFullLayout._has('parcats'));
    var hasTable = (newFullLayout._has && newFullLayout._has('parcats'));

    if(hadTable && !hasTable) {
        oldFullLayout._paperdiv.selectAll('.parcats').remove();
    }
};
