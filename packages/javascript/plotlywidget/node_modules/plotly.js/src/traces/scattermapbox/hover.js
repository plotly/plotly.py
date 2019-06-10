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
var getTraceColor = require('../scatter/get_trace_color');
var fillText = Lib.fillText;
var BADNUM = require('../../constants/numerical').BADNUM;

module.exports = function hoverPoints(pointData, xval, yval) {
    var cd = pointData.cd;
    var trace = cd[0].trace;
    var xa = pointData.xa;
    var ya = pointData.ya;
    var subplot = pointData.subplot;

    // compute winding number about [-180, 180] globe
    var winding = (xval >= 0) ?
        Math.floor((xval + 180) / 360) :
        Math.ceil((xval - 180) / 360);

    // shift longitude to [-180, 180] to determine closest point
    var lonShift = winding * 360;
    var xval2 = xval - lonShift;

    function distFn(d) {
        var lonlat = d.lonlat;
        if(lonlat[0] === BADNUM) return Infinity;

        var lon = Lib.modHalf(lonlat[0], 360);
        var lat = lonlat[1];
        var pt = subplot.project([lon, lat]);
        var dx = pt.x - xa.c2p([xval2, lat]);
        var dy = pt.y - ya.c2p([lon, yval]);
        var rad = Math.max(3, d.mrc || 0);

        return Math.max(Math.sqrt(dx * dx + dy * dy) - rad, 1 - 3 / rad);
    }

    Fx.getClosest(cd, distFn, pointData);

    // skip the rest (for this trace) if we didn't find a close point
    if(pointData.index === false) return;

    var di = cd[pointData.index];
    var lonlat = di.lonlat;
    var lonlatShifted = [Lib.modHalf(lonlat[0], 360) + lonShift, lonlat[1]];

    // shift labels back to original winded globe
    var xc = xa.c2p(lonlatShifted);
    var yc = ya.c2p(lonlatShifted);
    var rad = di.mrc || 1;

    pointData.x0 = xc - rad;
    pointData.x1 = xc + rad;
    pointData.y0 = yc - rad;
    pointData.y1 = yc + rad;

    pointData.color = getTraceColor(trace, di);
    pointData.extraText = getExtraText(trace, di, cd[0].t.labels);
    pointData.hovertemplate = trace.hovertemplate;

    return [pointData];
};

function getExtraText(trace, di, labels) {
    if(trace.hovertemplate) {
        return;
    }

    var hoverinfo = di.hi || trace.hoverinfo;
    var parts = hoverinfo.split('+');
    var isAll = parts.indexOf('all') !== -1;
    var hasLon = parts.indexOf('lon') !== -1;
    var hasLat = parts.indexOf('lat') !== -1;
    var lonlat = di.lonlat;
    var text = [];

    // TODO should we use a mock axis to format hover?
    // If so, we'll need to make precision be zoom-level dependent
    function format(v) {
        return v + '\u00B0';
    }

    if(isAll || (hasLon && hasLat)) {
        text.push('(' + format(lonlat[0]) + ', ' + format(lonlat[1]) + ')');
    } else if(hasLon) {
        text.push(labels.lon + format(lonlat[0]));
    } else if(hasLat) {
        text.push(labels.lat + format(lonlat[1]));
    }

    if(isAll || parts.indexOf('text') !== -1) {
        fillText(di, trace, text);
    }

    return text.join('<br>');
}
