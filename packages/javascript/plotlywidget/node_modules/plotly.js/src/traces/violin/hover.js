/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');
var boxHoverPoints = require('../box/hover');
var helpers = require('./helpers');

module.exports = function hoverPoints(pointData, xval, yval, hovermode, hoverLayer) {
    var cd = pointData.cd;
    var trace = cd[0].trace;
    var hoveron = trace.hoveron;
    var hasHoveronViolins = hoveron.indexOf('violins') !== -1;
    var hasHoveronKDE = hoveron.indexOf('kde') !== -1;
    var closeData = [];
    var closePtData;
    var violinLineAttrs;

    if(hasHoveronViolins || hasHoveronKDE) {
        var closeBoxData = boxHoverPoints.hoverOnBoxes(pointData, xval, yval, hovermode);

        if(hasHoveronKDE && closeBoxData.length > 0) {
            var xa = pointData.xa;
            var ya = pointData.ya;
            var pLetter, vLetter, pAxis, vAxis, vVal;

            if(trace.orientation === 'h') {
                vVal = xval;
                pLetter = 'y';
                pAxis = ya;
                vLetter = 'x';
                vAxis = xa;
            } else {
                vVal = yval;
                pLetter = 'x';
                pAxis = xa;
                vLetter = 'y';
                vAxis = ya;
            }

            var di = cd[pointData.index];

            if(vVal >= di.span[0] && vVal <= di.span[1]) {
                var kdePointData = Lib.extendFlat({}, pointData);
                var vValPx = vAxis.c2p(vVal, true);
                var kdeVal = helpers.getKdeValue(di, trace, vVal);
                var pOnPath = helpers.getPositionOnKdePath(di, trace, vValPx);
                var paOffset = pAxis._offset;
                var paLength = pAxis._length;

                kdePointData[pLetter + '0'] = pOnPath[0];
                kdePointData[pLetter + '1'] = pOnPath[1];
                kdePointData[vLetter + '0'] = kdePointData[vLetter + '1'] = vValPx;
                kdePointData[vLetter + 'Label'] = vLetter + ': ' + Axes.hoverLabelText(vAxis, vVal) + ', ' + cd[0].t.labels.kde + ' ' + kdeVal.toFixed(3);

                // move the spike to the KDE point
                kdePointData.spikeDistance = closeBoxData[0].spikeDistance;
                var spikePosAttr = pLetter + 'Spike';
                kdePointData[spikePosAttr] = closeBoxData[0][spikePosAttr];
                closeBoxData[0].spikeDistance = undefined;
                closeBoxData[0][spikePosAttr] = undefined;

                // no hovertemplate support yet
                kdePointData.hovertemplate = false;

                closeData.push(kdePointData);

                violinLineAttrs = {stroke: pointData.color};
                violinLineAttrs[pLetter + '1'] = Lib.constrain(paOffset + pOnPath[0], paOffset, paOffset + paLength);
                violinLineAttrs[pLetter + '2'] = Lib.constrain(paOffset + pOnPath[1], paOffset, paOffset + paLength);
                violinLineAttrs[vLetter + '1'] = violinLineAttrs[vLetter + '2'] = vAxis._offset + vValPx;
            }
        }

        if(hasHoveronViolins) {
            closeData = closeData.concat(closeBoxData);
        }
    }

    if(hoveron.indexOf('points') !== -1) {
        closePtData = boxHoverPoints.hoverOnPoints(pointData, xval, yval);
    }

    // update violin line (if any)
    var violinLine = hoverLayer.selectAll('.violinline-' + trace.uid)
        .data(violinLineAttrs ? [0] : []);
    violinLine.enter().append('line')
        .classed('violinline-' + trace.uid, true)
        .attr('stroke-width', 1.5);
    violinLine.exit().remove();
    violinLine.attr(violinLineAttrs);

    // same combine logic as box hoverPoints
    if(hovermode === 'closest') {
        if(closePtData) return [closePtData];
        return closeData;
    }
    if(closePtData) {
        closeData.push(closePtData);
        return closeData;
    }
    return closeData;
};
