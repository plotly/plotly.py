/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var hoverLabelText = require('../../plots/cartesian/axes').hoverLabelText;
var opacity = require('../../components/color').opacity;
var hoverOnBars = require('../bar/hover').hoverOnBars;

var DIRSYMBOL = {
    increasing: '▲',
    decreasing: '▼'
};

module.exports = function hoverPoints(pointData, xval, yval, hovermode) {
    var point = hoverOnBars(pointData, xval, yval, hovermode);
    if(!point) return;

    var cd = point.cd;
    var trace = cd[0].trace;
    var isHorizontal = (trace.orientation === 'h');

    var vAxis = isHorizontal ? pointData.xa : pointData.ya;

    function formatNumber(a) {
        return hoverLabelText(vAxis, a);
    }

    // the closest data point
    var index = point.index;
    var di = cd[index];

    var size = (di.isSum) ? di.b + di.s : di.rawS;

    if(!di.isSum) {
        // format delta numbers:
        if(size > 0) {
            point.extraText = formatNumber(size) + ' ' + DIRSYMBOL.increasing;
        } else if(size < 0) {
            point.extraText = '(' + (formatNumber(-size)) + ') ' + DIRSYMBOL.decreasing;
        } else {
            return;
        }
        // display initial value
        point.extraText += '<br>Initial: ' + formatNumber(di.b + di.s - size);
    }

    point.color = getTraceColor(trace, di);

    return [point];
};

function getTraceColor(trace, di) {
    var cont = trace[di.dir].marker;
    var mc = cont.color;
    var mlc = cont.line.color;
    var mlw = cont.line.width;
    if(opacity(mc)) return mc;
    else if(opacity(mlc) && mlw) return mlc;
}
