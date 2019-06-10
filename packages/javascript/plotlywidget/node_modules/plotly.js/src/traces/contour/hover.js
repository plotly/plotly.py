/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Color = require('../../components/color');

var heatmapHoverPoints = require('../heatmap/hover');

module.exports = function hoverPoints(pointData, xval, yval, hovermode, hoverLayer) {
    var hoverData = heatmapHoverPoints(pointData, xval, yval, hovermode, hoverLayer, true);

    if(hoverData) {
        hoverData.forEach(function(hoverPt) {
            var trace = hoverPt.trace;
            if(trace.contours.type === 'constraint') {
                if(trace.fillcolor && Color.opacity(trace.fillcolor)) {
                    hoverPt.color = Color.addOpacity(trace.fillcolor, 1);
                } else if(trace.contours.showlines && Color.opacity(trace.line.color)) {
                    hoverPt.color = Color.addOpacity(trace.line.color, 1);
                }
            }
        });
    }

    return hoverData;
};
