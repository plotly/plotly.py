/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/*
 * Return a function that evaluates a set of linear or bicubic control points.
 * This will get evaluated a lot, so we'll at least do a bit of extra work to
 * flatten some of the choices. In particular, we'll unroll the linear/bicubic
 * combinations and we'll allow computing results in parallel to cut down
 * on repeated arithmetic.
 *
 * Take note that we don't search for the correct range in this function. The
 * reason is for consistency due to the corrresponding derivative function. In
 * particular, the derivatives aren't continuous across cells, so it's important
 * to be able control whether the derivative at a cell boundary is approached
 * from one side or the other.
 */
module.exports = function(arrays, na, nb, asmoothing, bsmoothing) {
    var imax = na - 2;
    var jmax = nb - 2;

    if(asmoothing && bsmoothing) {
        return function(out, i, j) {
            if(!out) out = [];
            var f0, f1, f2, f3, ak, k;

            var i0 = Math.max(0, Math.min(Math.floor(i), imax));
            var j0 = Math.max(0, Math.min(Math.floor(j), jmax));
            var u = Math.max(0, Math.min(1, i - i0));
            var v = Math.max(0, Math.min(1, j - j0));

            // Since it's a grid of control points, the actual indices are * 3:
            i0 *= 3;
            j0 *= 3;

            // Precompute some numbers:
            var u2 = u * u;
            var u3 = u2 * u;
            var ou = 1 - u;
            var ou2 = ou * ou;
            var ou3 = ou2 * ou;

            var v2 = v * v;
            var v3 = v2 * v;
            var ov = 1 - v;
            var ov2 = ov * ov;
            var ov3 = ov2 * ov;

            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];
                f0 = ou3 * ak[j0][i0] + 3 * (ou2 * u * ak[j0][i0 + 1] + ou * u2 * ak[j0][i0 + 2]) + u3 * ak[j0][i0 + 3];
                f1 = ou3 * ak[j0 + 1][i0] + 3 * (ou2 * u * ak[j0 + 1][i0 + 1] + ou * u2 * ak[j0 + 1][i0 + 2]) + u3 * ak[j0 + 1][i0 + 3];
                f2 = ou3 * ak[j0 + 2][i0] + 3 * (ou2 * u * ak[j0 + 2][i0 + 1] + ou * u2 * ak[j0 + 2][i0 + 2]) + u3 * ak[j0 + 2][i0 + 3];
                f3 = ou3 * ak[j0 + 3][i0] + 3 * (ou2 * u * ak[j0 + 3][i0 + 1] + ou * u2 * ak[j0 + 3][i0 + 2]) + u3 * ak[j0 + 3][i0 + 3];
                out[k] = ov3 * f0 + 3 * (ov2 * v * f1 + ov * v2 * f2) + v3 * f3;
            }

            return out;
        };
    } else if(asmoothing) {
        // Handle smooth in the a-direction but linear in the b-direction by performing four
        // linear interpolations followed by one cubic interpolation of the result
        return function(out, i, j) {
            if(!out) out = [];

            var i0 = Math.max(0, Math.min(Math.floor(i), imax));
            var j0 = Math.max(0, Math.min(Math.floor(j), jmax));
            var u = Math.max(0, Math.min(1, i - i0));
            var v = Math.max(0, Math.min(1, j - j0));

            var f0, f1, f2, f3, k, ak;
            i0 *= 3;
            var u2 = u * u;
            var u3 = u2 * u;
            var ou = 1 - u;
            var ou2 = ou * ou;
            var ou3 = ou2 * ou;
            var ov = 1 - v;
            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];
                f0 = ov * ak[j0][i0] + v * ak[j0 + 1][i0];
                f1 = ov * ak[j0][i0 + 1] + v * ak[j0 + 1][i0 + 1];
                f2 = ov * ak[j0][i0 + 2] + v * ak[j0 + 1][i0 + 1];
                f3 = ov * ak[j0][i0 + 3] + v * ak[j0 + 1][i0 + 1];

                out[k] = ou3 * f0 + 3 * (ou2 * u * f1 + ou * u2 * f2) + u3 * f3;
            }
            return out;
        };
    } else if(bsmoothing) {
        // Same as the above case, except reversed:
        return function(out, i, j) {
            if(!out) out = [];

            var i0 = Math.max(0, Math.min(Math.floor(i), imax));
            var j0 = Math.max(0, Math.min(Math.floor(j), jmax));
            var u = Math.max(0, Math.min(1, i - i0));
            var v = Math.max(0, Math.min(1, j - j0));

            var f0, f1, f2, f3, k, ak;
            j0 *= 3;
            var v2 = v * v;
            var v3 = v2 * v;
            var ov = 1 - v;
            var ov2 = ov * ov;
            var ov3 = ov2 * ov;
            var ou = 1 - u;
            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];
                f0 = ou * ak[j0][i0] + u * ak[j0][i0 + 1];
                f1 = ou * ak[j0 + 1][i0] + u * ak[j0 + 1][i0 + 1];
                f2 = ou * ak[j0 + 2][i0] + u * ak[j0 + 2][i0 + 1];
                f3 = ou * ak[j0 + 3][i0] + u * ak[j0 + 3][i0 + 1];

                out[k] = ov3 * f0 + 3 * (ov2 * v * f1 + ov * v2 * f2) + v3 * f3;
            }
            return out;
        };
    } else {
        // Finally, both directions are linear:
        return function(out, i, j) {
            if(!out) out = [];

            var i0 = Math.max(0, Math.min(Math.floor(i), imax));
            var j0 = Math.max(0, Math.min(Math.floor(j), jmax));
            var u = Math.max(0, Math.min(1, i - i0));
            var v = Math.max(0, Math.min(1, j - j0));

            var f0, f1, k, ak;
            var ov = 1 - v;
            var ou = 1 - u;
            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];
                f0 = ou * ak[j0][i0] + u * ak[j0][i0 + 1];
                f1 = ou * ak[j0 + 1][i0] + u * ak[j0 + 1][i0 + 1];

                out[k] = ov * f0 + v * f1;
            }
            return out;
        };
    }
};
