/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../../plots/cartesian/axes');
var Lib = require('../../lib');
var Fx = require('../../components/fx');
var Color = require('../../components/color');
var fillText = require('../../lib').fillText;

var DIRSYMBOL = {
    increasing: '▲',
    decreasing: '▼'
};

function hoverPoints(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var trace = cd[0].trace;

    if(trace.hoverlabel.split) {
        return hoverSplit(pointData, xval, yval, hovermode);
    }

    return hoverOnPoints(pointData, xval, yval, hovermode);
}

function getClosestPoint(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var xa = pointData.xa;
    var trace = cd[0].trace;
    var t = cd[0].t;

    var type = trace.type;
    var minAttr = type === 'ohlc' ? 'l' : 'min';
    var maxAttr = type === 'ohlc' ? 'h' : 'max';

    var hoverPseudoDistance, spikePseudoDistance;

    // potentially shift xval for grouped candlesticks
    var centerShift = t.bPos || 0;
    var shiftPos = function(di) { return di.pos + centerShift - xval; };

    // ohlc and candlestick call displayHalfWidth different things...
    var displayHalfWidth = t.bdPos || t.tickLen;
    var hoverHalfWidth = t.wHover;

    // if two figures are overlaying, let the narrowest one win
    var pseudoDistance = Math.min(1, displayHalfWidth / Math.abs(xa.r2c(xa.range[1]) - xa.r2c(xa.range[0])));
    hoverPseudoDistance = pointData.maxHoverDistance - pseudoDistance;
    spikePseudoDistance = pointData.maxSpikeDistance - pseudoDistance;

    function dx(di) {
        var pos = shiftPos(di);
        return Fx.inbox(pos - hoverHalfWidth, pos + hoverHalfWidth, hoverPseudoDistance);
    }

    function dy(di) {
        var min = di[minAttr];
        var max = di[maxAttr];
        return min === max || Fx.inbox(min - yval, max - yval, hoverPseudoDistance);
    }

    function dxy(di) { return (dx(di) + dy(di)) / 2; }

    var distfn = Fx.getDistanceFunction(hovermode, dx, dy, dxy);
    Fx.getClosest(cd, distfn, pointData);

    if(pointData.index === false) return null;

    var di = cd[pointData.index];

    if(di.empty) return null;

    var dir = di.dir;
    var container = trace[dir];
    var lc = container.line.color;

    if(Color.opacity(lc) && container.line.width) pointData.color = lc;
    else pointData.color = container.fillcolor;

    pointData.x0 = xa.c2p(di.pos + centerShift - displayHalfWidth, true);
    pointData.x1 = xa.c2p(di.pos + centerShift + displayHalfWidth, true);

    pointData.xLabelVal = di.pos;

    pointData.spikeDistance = dxy(di) * spikePseudoDistance / hoverPseudoDistance;
    pointData.xSpike = xa.c2p(di.pos, true);

    return pointData;
}

function hoverSplit(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var ya = pointData.ya;
    var trace = cd[0].trace;
    var t = cd[0].t;
    var closeBoxData = [];

    var closestPoint = getClosestPoint(pointData, xval, yval, hovermode);
    // skip the rest (for this trace) if we didn't find a close point
    if(!closestPoint) return [];

    var cdIndex = closestPoint.index;
    var di = cd[cdIndex];
    var hoverinfo = di.hi || trace.hoverinfo;
    var hoverParts = hoverinfo.split('+');
    var isAll = hoverinfo === 'all';
    var hasY = isAll || hoverParts.indexOf('y') !== -1;

    // similar to hoverOnPoints, we return nothing
    // if all or y is not present.
    if(!hasY) return [];

    var attrs = ['high', 'open', 'close', 'low'];

    // several attributes can have the same y-coordinate. We will
    // bunch them together in a single text block. For this, we keep
    // a dictionary mapping y-coord -> point data.
    var usedVals = {};

    for(var i = 0; i < attrs.length; i++) {
        var attr = attrs[i];

        var val = trace[attr][closestPoint.index];
        var valPx = ya.c2p(val, true);
        var pointData2;
        if(val in usedVals) {
            pointData2 = usedVals[val];
            pointData2.yLabel += '<br>' + t.labels[attr] + Axes.hoverLabelText(ya, val);
        } else {
            // copy out to a new object for each new y-value to label
            pointData2 = Lib.extendFlat({}, closestPoint);

            pointData2.y0 = pointData2.y1 = valPx;
            pointData2.yLabelVal = val;
            pointData2.yLabel = t.labels[attr] + Axes.hoverLabelText(ya, val);

            pointData2.name = '';

            closeBoxData.push(pointData2);
            usedVals[val] = pointData2;
        }
    }

    return closeBoxData;
}

function hoverOnPoints(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var ya = pointData.ya;
    var trace = cd[0].trace;
    var t = cd[0].t;

    var closestPoint = getClosestPoint(pointData, xval, yval, hovermode);
    // skip the rest (for this trace) if we didn't find a close point
    if(!closestPoint) return [];

    // we don't make a calcdata point if we're missing any piece (x/o/h/l/c)
    // so we need to fix the index here to point to the data arrays
    var cdIndex = closestPoint.index;
    var di = cd[cdIndex];
    var i = closestPoint.index = di.i;
    var dir = di.dir;

    function getLabelLine(attr) {
        return t.labels[attr] + Axes.hoverLabelText(ya, trace[attr][i]);
    }

    var hoverinfo = di.hi || trace.hoverinfo;
    var hoverParts = hoverinfo.split('+');
    var isAll = hoverinfo === 'all';
    var hasY = isAll || hoverParts.indexOf('y') !== -1;
    var hasText = isAll || hoverParts.indexOf('text') !== -1;

    var textParts = hasY ? [
        getLabelLine('open'),
        getLabelLine('high'),
        getLabelLine('low'),
        getLabelLine('close') + '  ' + DIRSYMBOL[dir]
    ] : [];
    if(hasText) fillText(di, trace, textParts);

    // don't make .yLabelVal or .text, since we're managing hoverinfo
    // put it all in .extraText
    closestPoint.extraText = textParts.join('<br>');

    // this puts the label *and the spike* at the midpoint of the box, ie
    // halfway between open and close, not between high and low.
    closestPoint.y0 = closestPoint.y1 = ya.c2p(di.yc, true);

    return [closestPoint];
}

module.exports = {
    hoverPoints: hoverPoints,
    hoverSplit: hoverSplit,
    hoverOnPoints: hoverOnPoints
};
