/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorscaleCalc = require('../../components/colorscale/calc');

module.exports = function calc(gd, trace) {
    var i;

    var u = trace.u;
    var v = trace.v;
    var w = trace.w;
    var x = trace.x;
    var y = trace.y;
    var z = trace.z;
    var len = Math.min(x.length, y.length, z.length, u.length, v.length, w.length);

    var slen = 0;
    var startx, starty, startz;
    if(trace.starts) {
        startx = trace.starts.x || [];
        starty = trace.starts.y || [];
        startz = trace.starts.z || [];
        slen = Math.min(startx.length, starty.length, startz.length);
    }

    var normMax = 0;
    var normMin = Infinity;

    for(i = 0; i < len; i++) {
        var uu = u[i];
        var vv = v[i];
        var ww = w[i];
        var norm = Math.sqrt(uu * uu + vv * vv + ww * ww);

        normMax = Math.max(normMax, norm);
        normMin = Math.min(normMin, norm);
    }

    colorscaleCalc(gd, trace, {
        vals: [normMin, normMax],
        containerStr: '',
        cLetter: 'c'
    });

    var xMax = -Infinity;
    var xMin = Infinity;
    var yMax = -Infinity;
    var yMin = Infinity;
    var zMax = -Infinity;
    var zMin = Infinity;

    for(i = 0; i < len; i++) {
        var xx = x[i];
        xMax = Math.max(xMax, xx);
        xMin = Math.min(xMin, xx);

        var yy = y[i];
        yMax = Math.max(yMax, yy);
        yMin = Math.min(yMin, yy);

        var zz = z[i];
        zMax = Math.max(zMax, zz);
        zMin = Math.min(zMin, zz);
    }
    for(i = 0; i < slen; i++) {
        var sx = startx[i];
        xMax = Math.max(xMax, sx);
        xMin = Math.min(xMin, sx);

        var sy = starty[i];
        yMax = Math.max(yMax, sy);
        yMin = Math.min(yMin, sy);

        var sz = startz[i];
        zMax = Math.max(zMax, sz);
        zMin = Math.min(zMin, sz);
    }

    trace._len = len;
    trace._slen = slen;
    trace._normMax = normMax;
    trace._xbnds = [xMin, xMax];
    trace._ybnds = [yMin, yMax];
    trace._zbnds = [zMin, zMax];
};
