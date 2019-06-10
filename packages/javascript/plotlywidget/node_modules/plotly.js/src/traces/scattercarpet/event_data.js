/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function eventData(out, pt, trace, cd, pointNumber) {
    var cdi = cd[pointNumber];

    out.a = cdi.a;
    out.b = cdi.b;
    out.y = cdi.y;

    return out;
};
