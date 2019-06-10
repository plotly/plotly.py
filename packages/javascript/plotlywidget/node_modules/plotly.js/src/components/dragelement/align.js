/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


// for automatic alignment on dragging, <1/3 means left align,
// >2/3 means right, and between is center. Pick the right fraction
// based on where you are, and return the fraction corresponding to
// that position on the object
module.exports = function align(v, dv, v0, v1, anchor) {
    var vmin = (v - v0) / (v1 - v0);
    var vmax = vmin + dv / (v1 - v0);
    var vc = (vmin + vmax) / 2;

    // explicitly specified anchor
    if(anchor === 'left' || anchor === 'bottom') return vmin;
    if(anchor === 'center' || anchor === 'middle') return vc;
    if(anchor === 'right' || anchor === 'top') return vmax;

    // automatic based on position
    if(vmin < (2 / 3) - vc) return vmin;
    if(vmax > (4 / 3) - vc) return vmax;
    return vc;
};
