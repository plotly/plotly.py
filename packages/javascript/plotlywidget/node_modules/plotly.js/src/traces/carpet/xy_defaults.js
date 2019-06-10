/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isArray1D = require('../../lib').isArray1D;

module.exports = function handleXYDefaults(traceIn, traceOut, coerce) {
    var x = coerce('x');
    var hasX = x && x.length;
    var y = coerce('y');
    var hasY = y && y.length;
    if(!hasX && !hasY) return false;

    traceOut._cheater = !x;

    if((!hasX || isArray1D(x)) && (!hasY || isArray1D(y))) {
        var len = hasX ? x.length : Infinity;
        if(hasY) len = Math.min(len, y.length);
        if(traceOut.a && traceOut.a.length) len = Math.min(len, traceOut.a.length);
        if(traceOut.b && traceOut.b.length) len = Math.min(len, traceOut.b.length);
        traceOut._length = len;
    } else traceOut._length = null;

    return true;
};
