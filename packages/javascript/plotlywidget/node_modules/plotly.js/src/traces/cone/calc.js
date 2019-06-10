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
    var u = trace.u;
    var v = trace.v;
    var w = trace.w;
    var len = Math.min(
        trace.x.length, trace.y.length, trace.z.length,
        u.length, v.length, w.length
    );
    var normMax = -Infinity;
    var normMin = Infinity;

    for(var i = 0; i < len; i++) {
        var uu = u[i];
        var vv = v[i];
        var ww = w[i];
        var norm = Math.sqrt(uu * uu + vv * vv + ww * ww);

        normMax = Math.max(normMax, norm);
        normMin = Math.min(normMin, norm);
    }

    trace._len = len;
    trace._normMax = normMax;

    colorscaleCalc(gd, trace, {
        vals: [normMin, normMax],
        containerStr: '',
        cLetter: 'c'
    });
};
