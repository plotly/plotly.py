/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var scatterPlot = require('../scatter/plot');

module.exports = function plot(gd, ternary, moduleCalcData) {
    var plotContainer = ternary.plotContainer;

    // remove all nodes inside the scatter layer
    plotContainer.select('.scatterlayer').selectAll('*').remove();

    // mimic cartesian plotinfo
    var plotinfo = {
        xaxis: ternary.xaxis,
        yaxis: ternary.yaxis,
        plot: plotContainer,
        layerClipId: ternary._hasClipOnAxisFalse ? ternary.clipIdRelative : null
    };

    var scatterLayer = ternary.layers.frontplot.select('g.scatterlayer');

    scatterPlot(gd, plotinfo, moduleCalcData, scatterLayer);
};
