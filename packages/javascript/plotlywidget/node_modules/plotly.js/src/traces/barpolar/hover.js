/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Fx = require('../../components/fx');
var Lib = require('../../lib');
var getTraceColor = require('../bar/hover').getTraceColor;
var fillText = Lib.fillText;
var makeHoverPointText = require('../scatterpolar/hover').makeHoverPointText;
var isPtInsidePolygon = require('../../plots/polar/helpers').isPtInsidePolygon;

module.exports = function hoverPoints(pointData, xval, yval) {
    var cd = pointData.cd;
    var trace = cd[0].trace;

    var subplot = pointData.subplot;
    var radialAxis = subplot.radialAxis;
    var angularAxis = subplot.angularAxis;
    var vangles = subplot.vangles;
    var inboxFn = vangles ? isPtInsidePolygon : Lib.isPtInsideSector;
    var maxHoverDistance = pointData.maxHoverDistance;
    var period = angularAxis._period || 2 * Math.PI;

    var rVal = Math.abs(radialAxis.g2p(Math.sqrt(xval * xval + yval * yval)));
    var thetaVal = Math.atan2(yval, xval);

    // polar.(x|y)axis.p2c doesn't get the reversed radial axis range case right
    if(radialAxis.range[0] > radialAxis.range[1]) {
        thetaVal += Math.PI;
    }

    var distFn = function(di) {
        if(inboxFn(rVal, thetaVal, [di.rp0, di.rp1], [di.thetag0, di.thetag1], vangles)) {
            return maxHoverDistance +
                // add a little to the pseudo-distance for wider bars, so that like scatter,
                // if you are over two overlapping bars, the narrower one wins.
                Math.min(1, Math.abs(di.thetag1 - di.thetag0) / period) - 1 +
                // add a gradient so hovering near the end of a
                // bar makes it a little closer match
                (di.rp1 - rVal) / (di.rp1 - di.rp0) - 1;
        } else {
            return Infinity;
        }
    };

    Fx.getClosest(cd, distFn, pointData);
    if(pointData.index === false) return;

    var index = pointData.index;
    var cdi = cd[index];

    pointData.x0 = pointData.x1 = cdi.ct[0];
    pointData.y0 = pointData.y1 = cdi.ct[1];

    var _cdi = Lib.extendFlat({}, cdi, {r: cdi.s, theta: cdi.p});
    fillText(cdi, trace, pointData);
    makeHoverPointText(_cdi, trace, subplot, pointData);
    pointData.hovertemplate = trace.hovertemplate;
    pointData.color = getTraceColor(trace, cdi);
    pointData.xLabelVal = pointData.yLabelVal = undefined;

    if(cdi.s < 0) {
        pointData.idealAlign = 'left';
    }

    return [pointData];
};
