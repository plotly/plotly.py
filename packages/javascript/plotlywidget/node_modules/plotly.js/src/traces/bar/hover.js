/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Fx = require('../../components/fx');
var Registry = require('../../registry');
var Color = require('../../components/color');

var fillText = require('../../lib').fillText;

function hoverPoints(pointData, xval, yval, hovermode) {
    var barPointData = hoverOnBars(pointData, xval, yval, hovermode);

    if(barPointData) {
        var cd = barPointData.cd;
        var trace = cd[0].trace;
        var di = cd[barPointData.index];

        barPointData.color = getTraceColor(trace, di);
        Registry.getComponentMethod('errorbars', 'hoverInfo')(di, trace, barPointData);

        return [barPointData];
    }
}

function hoverOnBars(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var trace = cd[0].trace;
    var t = cd[0].t;
    var isClosest = (hovermode === 'closest');
    var isWaterfall = (trace.type === 'waterfall');
    var maxHoverDistance = pointData.maxHoverDistance;
    var maxSpikeDistance = pointData.maxSpikeDistance;

    var posVal, sizeVal, posLetter, sizeLetter, dx, dy, pRangeCalc;

    function thisBarMinPos(di) { return di[posLetter] - di.w / 2; }
    function thisBarMaxPos(di) { return di[posLetter] + di.w / 2; }

    var minPos = isClosest ?
        thisBarMinPos :
        function(di) {
            /*
             * In compare mode, accept a bar if you're on it *or* its group.
             * Nearly always it's the group that matters, but in case the bar
             * was explicitly set wider than its group we'd better accept the
             * whole bar.
             *
             * use `bardelta` instead of `bargroupwidth` so we accept hover
             * in the gap. That way hover doesn't flash on and off as you
             * mouse over the plot in compare modes.
             * In 'closest' mode though the flashing seems inevitable,
             * without far more complex logic
             */
            return Math.min(thisBarMinPos(di), di.p - t.bardelta / 2);
        };

    var maxPos = isClosest ?
        thisBarMaxPos :
        function(di) {
            return Math.max(thisBarMaxPos(di), di.p + t.bardelta / 2);
        };

    function _positionFn(_minPos, _maxPos) {
        // add a little to the pseudo-distance for wider bars, so that like scatter,
        // if you are over two overlapping bars, the narrower one wins.
        return Fx.inbox(_minPos - posVal, _maxPos - posVal,
            maxHoverDistance + Math.min(1, Math.abs(_maxPos - _minPos) / pRangeCalc) - 1);
    }

    function positionFn(di) {
        return _positionFn(minPos(di), maxPos(di));
    }

    function thisBarPositionFn(di) {
        return _positionFn(thisBarMinPos(di), thisBarMaxPos(di));
    }

    function sizeFn(di) {
        var v = sizeVal;
        var b = di.b;
        var s = di[sizeLetter];

        if(isWaterfall) {
            s += Math.abs(di.rawS || 0);
        }

        // add a gradient so hovering near the end of a
        // bar makes it a little closer match
        return Fx.inbox(b - v, s - v, maxHoverDistance + (s - v) / (s - b) - 1);
    }

    if(trace.orientation === 'h') {
        posVal = yval;
        sizeVal = xval;
        posLetter = 'y';
        sizeLetter = 'x';
        dx = sizeFn;
        dy = positionFn;
    } else {
        posVal = xval;
        sizeVal = yval;
        posLetter = 'x';
        sizeLetter = 'y';
        dy = sizeFn;
        dx = positionFn;
    }

    var pa = pointData[posLetter + 'a'];
    var sa = pointData[sizeLetter + 'a'];

    pRangeCalc = Math.abs(pa.r2c(pa.range[1]) - pa.r2c(pa.range[0]));

    function dxy(di) { return (dx(di) + dy(di)) / 2; }
    var distfn = Fx.getDistanceFunction(hovermode, dx, dy, dxy);
    Fx.getClosest(cd, distfn, pointData);

    // skip the rest (for this trace) if we didn't find a close point
    if(pointData.index === false) return;

    // if we get here and we're not in 'closest' mode, push min/max pos back
    // onto the group - even though that means occasionally the mouse will be
    // over the hover label.
    if(!isClosest) {
        minPos = function(di) {
            return Math.min(thisBarMinPos(di), di.p - t.bargroupwidth / 2);
        };
        maxPos = function(di) {
            return Math.max(thisBarMaxPos(di), di.p + t.bargroupwidth / 2);
        };
    }

    // the closest data point
    var index = pointData.index;
    var di = cd[index];

    var size = (trace.base) ? di.b + di.s : di.s;
    pointData[sizeLetter + '0'] = pointData[sizeLetter + '1'] = sa.c2p(di[sizeLetter], true);
    pointData[sizeLetter + 'LabelVal'] = size;

    var extent = t.extents[t.extents.round(di.p)];
    pointData[posLetter + '0'] = pa.c2p(isClosest ? minPos(di) : extent[0], true);
    pointData[posLetter + '1'] = pa.c2p(isClosest ? maxPos(di) : extent[1], true);
    pointData[posLetter + 'LabelVal'] = di.p;

    // spikelines always want "closest" distance regardless of hovermode
    pointData.spikeDistance = (sizeFn(di) + thisBarPositionFn(di)) / 2 + maxSpikeDistance - maxHoverDistance;
    // they also want to point to the data value, regardless of where the label goes
    // in case of bars shifted within groups
    pointData[posLetter + 'Spike'] = pa.c2p(di.p, true);

    fillText(di, trace, pointData);
    pointData.hovertemplate = trace.hovertemplate;

    return pointData;
}

function getTraceColor(trace, di) {
    var mc = di.mcc || trace.marker.color;
    var mlc = di.mlcc || trace.marker.line.color;
    var mlw = di.mlw || trace.marker.line.width;

    if(Color.opacity(mc)) return mc;
    else if(Color.opacity(mlc) && mlw) return mlc;
}

module.exports = {
    hoverPoints: hoverPoints,
    hoverOnBars: hoverOnBars,
    getTraceColor: getTraceColor
};
