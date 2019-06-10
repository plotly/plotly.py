/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function eventData(out, pt, trace, cd, pointNumber) {
    if(pt.xa) out.xaxis = pt.xa;
    if(pt.ya) out.yaxis = pt.ya;

    if(cd[pointNumber]) {
        var cdi = cd[pointNumber];

        // N.B. These are the normalized coordinates.
        out.a = cdi.a;
        out.b = cdi.b;
        out.c = cdi.c;
    } else {
        // for fill-hover only
        out.a = pt.a;
        out.b = pt.b;
        out.c = pt.c;
    }

    return out;
};
