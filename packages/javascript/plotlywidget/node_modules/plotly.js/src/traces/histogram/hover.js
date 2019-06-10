/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var barHover = require('../bar/hover').hoverPoints;
var hoverLabelText = require('../../plots/cartesian/axes').hoverLabelText;

module.exports = function hoverPoints(pointData, xval, yval, hovermode) {
    var pts = barHover(pointData, xval, yval, hovermode);

    if(!pts) return;

    pointData = pts[0];
    var di = pointData.cd[pointData.index];
    var trace = pointData.cd[0].trace;

    if(!trace.cumulative.enabled) {
        var posLetter = trace.orientation === 'h' ? 'y' : 'x';

        pointData[posLetter + 'Label'] = hoverLabelText(pointData[posLetter + 'a'], di.ph0, di.ph1);
    }

    if(trace.hovermplate) pointData.hovertemplate = trace.hovertemplate;

    return pts;
};
