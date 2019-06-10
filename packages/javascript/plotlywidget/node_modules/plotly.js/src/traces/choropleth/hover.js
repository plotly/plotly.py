/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Axes = require('../../plots/cartesian/axes');
var attributes = require('./attributes');
var fillText = require('../../lib').fillText;

module.exports = function hoverPoints(pointData, xval, yval) {
    var cd = pointData.cd;
    var trace = cd[0].trace;
    var geo = pointData.subplot;

    var pt, i, j, isInside;

    for(i = 0; i < cd.length; i++) {
        pt = cd[i];
        isInside = false;

        if(pt._polygons) {
            for(j = 0; j < pt._polygons.length; j++) {
                if(pt._polygons[j].contains([xval, yval])) {
                    isInside = !isInside;
                }
                // for polygons that cross antimeridian as xval is in [-180, 180]
                if(pt._polygons[j].contains([xval + 360, yval])) {
                    isInside = !isInside;
                }
            }

            if(isInside) break;
        }
    }

    if(!isInside || !pt) return;

    pointData.x0 = pointData.x1 = pointData.xa.c2p(pt.ct);
    pointData.y0 = pointData.y1 = pointData.ya.c2p(pt.ct);

    pointData.index = pt.index;
    pointData.location = pt.loc;
    pointData.z = pt.z;
    pointData.hovertemplate = pt.hovertemplate;

    makeHoverInfo(pointData, trace, pt, geo.mockAxis);

    return [pointData];
};

function makeHoverInfo(pointData, trace, pt, axis) {
    if(trace.hovertemplate) {
        return;
    }

    var hoverinfo = pt.hi || trace.hoverinfo;

    var parts = (hoverinfo === 'all') ?
        attributes.hoverinfo.flags :
        hoverinfo.split('+');

    var hasName = (parts.indexOf('name') !== -1);
    var hasLocation = (parts.indexOf('location') !== -1);
    var hasZ = (parts.indexOf('z') !== -1);
    var hasText = (parts.indexOf('text') !== -1);
    var hasIdAsNameLabel = !hasName && hasLocation;

    var text = [];

    function formatter(val) {
        return Axes.tickText(axis, axis.c2l(val), 'hover').text;
    }

    if(hasIdAsNameLabel) {
        pointData.nameOverride = pt.loc;
    } else {
        if(hasName) pointData.nameOverride = trace.name;
        if(hasLocation) text.push(pt.loc);
    }

    if(hasZ) text.push(formatter(pt.z));
    if(hasText) {
        fillText(pt, trace, text);
    }

    pointData.extraText = text.join('<br>');
}
