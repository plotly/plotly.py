/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scatterHover = require('../scatter/hover');
var Axes = require('../../plots/cartesian/axes');
var Lib = require('../../lib');

function hoverPoints(pointData, xval, yval, hovermode) {
    var scatterPointData = scatterHover(pointData, xval, yval, hovermode);
    if(!scatterPointData || scatterPointData[0].index === false) return;

    var newPointData = scatterPointData[0];

    // hovering on fill case
    if(newPointData.index === undefined) {
        return scatterPointData;
    }

    var subplot = pointData.subplot;
    var cdi = newPointData.cd[newPointData.index];
    var trace = newPointData.trace;

    if(!subplot.isPtInside(cdi)) return;

    newPointData.xLabelVal = undefined;
    newPointData.yLabelVal = undefined;
    makeHoverPointText(cdi, trace, subplot, newPointData);
    newPointData.hovertemplate = trace.hovertemplate;
    return scatterPointData;
}

function makeHoverPointText(cdi, trace, subplot, pointData) {
    var radialAxis = subplot.radialAxis;
    var angularAxis = subplot.angularAxis;
    radialAxis._hovertitle = 'r';
    angularAxis._hovertitle = 'θ';

    var hoverinfo = cdi.hi || trace.hoverinfo;
    var text = [];
    function textPart(ax, val) {
        text.push(ax._hovertitle + ': ' + Axes.tickText(ax, val, 'hover').text);
    }

    if(!trace.hovertemplate) {
        var parts = hoverinfo.split('+');

        if(parts.indexOf('all') !== -1) parts = ['r', 'theta', 'text'];
        if(parts.indexOf('r') !== -1) {
            textPart(radialAxis, radialAxis.c2l(cdi.r));
        }
        if(parts.indexOf('theta') !== -1) {
            var theta = cdi.theta;
            textPart(
                angularAxis,
                angularAxis.thetaunit === 'degrees' ? Lib.rad2deg(theta) : theta
            );
        }
        if(parts.indexOf('text') !== -1 && pointData.text) {
            text.push(pointData.text);
            delete pointData.text;
        }

        pointData.extraText = text.join('<br>');
    }
}

module.exports = {
    hoverPoints: hoverPoints,
    makeHoverPointText: makeHoverPointText
};
