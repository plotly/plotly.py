/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var opacity = require('../../components/color').opacity;
var hoverOnBars = require('../bar/hover').hoverOnBars;
var formatPercent = require('../../lib').formatPercent;

module.exports = function hoverPoints(pointData, xval, yval, hovermode) {
    var point = hoverOnBars(pointData, xval, yval, hovermode);
    if(!point) return;

    var cd = point.cd;
    var trace = cd[0].trace;
    var isHorizontal = (trace.orientation === 'h');

    // the closest data point
    var index = point.index;
    var di = cd[index];

    var sizeLetter = isHorizontal ? 'x' : 'y';

    point[sizeLetter + 'LabelVal'] = di.s;

    // display ratio to initial value
    point.extraText = [
        formatPercent(di.begR, 1) + ' of initial',
        formatPercent(di.difR, 1) + ' of previous',
        formatPercent(di.sumR, 1) + ' of total'
    ].join('<br>');
    // TODO: Should we use pieHelpers.formatPieValue instead ?

    point.color = getTraceColor(trace, di);

    return [point];
};

function getTraceColor(trace, di) {
    var cont = trace.marker;
    var mc = di.mc || cont.color;
    var mlc = di.mlc || cont.line.color;
    var mlw = di.mlw || cont.line.width;
    if(opacity(mc)) return mc;
    else if(opacity(mlc) && mlw) return mlc;
}
