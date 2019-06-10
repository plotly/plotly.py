/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function(arrays, asmoothing, bsmoothing) {
    if(asmoothing && bsmoothing) {
        return function(out, i0, j0, u, v) {
            if(!out) out = [];
            var f0, f1, f2, f3, ak, k;

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
            var ov = 1 - v;
            var ov2 = ov * ov;
            var ovv2 = ov * v * 2;
            var a = -3 * ov2;
            var b = 3 * (ov2 - ovv2);
            var c = 3 * (ovv2 - v2);
            var d = 3 * v2;

            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];

                // Compute the derivatives in the v-direction:
                f0 = a * ak[j0][i0] + b * ak[j0 + 1][i0] + c * ak[j0 + 2][i0] + d * ak[j0 + 3][i0];
                f1 = a * ak[j0][i0 + 1] + b * ak[j0 + 1][i0 + 1] + c * ak[j0 + 2][i0 + 1] + d * ak[j0 + 3][i0 + 1];
                f2 = a * ak[j0][i0 + 2] + b * ak[j0 + 1][i0 + 2] + c * ak[j0 + 2][i0 + 2] + d * ak[j0 + 3][i0 + 2];
                f3 = a * ak[j0][i0 + 3] + b * ak[j0 + 1][i0 + 3] + c * ak[j0 + 2][i0 + 3] + d * ak[j0 + 3][i0 + 3];

                // Now just interpolate in the v-direction since it's all separable:
                out[k] = ou3 * f0 + 3 * (ou2 * u * f1 + ou * u2 * f2) + u3 * f3;
            }

            return out;
        };
    } else if(asmoothing) {
        // Handle smooth in the a-direction but linear in the b-direction by performing four
        // linear interpolations followed by one cubic interpolation of the result
        return function(out, i0, j0, v, u) {
            if(!out) out = [];
            var f0, f1, f2, f3, k, ak;
            i0 *= 3;
            var u2 = u * u;
            var u3 = u2 * u;
            var ou = 1 - u;
            var ou2 = ou * ou;
            var ou3 = ou2 * ou;
            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];

                f0 = ak[j0 + 1][i0] - ak[j0][i0];
                f1 = ak[j0 + 1][i0 + 1] - ak[j0][i0 + 1];
                f2 = ak[j0 + 1][i0 + 2] - ak[j0][i0 + 2];
                f3 = ak[j0 + 1][i0 + 3] - ak[j0][i0 + 3];

                out[k] = ou3 * f0 + 3 * (ou2 * u * f1 + ou * u2 * f2) + u3 * f3;

                // mathematically equivalent:
                // f0 = ou3 * ak[j0    ][i0] + 3 * (ou2 * u * ak[j0    ][i0 + 1] + ou * u2 * ak[j0    ][i0 + 2]) + u3 * ak[j0    ][i0 + 3];
                // f1 = ou3 * ak[j0 + 1][i0] + 3 * (ou2 * u * ak[j0 + 1][i0 + 1] + ou * u2 * ak[j0 + 1][i0 + 2]) + u3 * ak[j0 + 1][i0 + 3];
                // out[k] = f1 - f0;
            }
            return out;
        };
    } else if(bsmoothing) {
        // Same as the above case, except reversed:
        /* eslint-disable no-unused-vars */
        return function(out, i0, j0, u, v) {
        /* eslint-enable no-unused-vars */
            if(!out) out = [];
            var f0, f1, k, ak;
            j0 *= 3;
            var ou = 1 - u;
            var v2 = v * v;
            var ov = 1 - v;
            var ov2 = ov * ov;
            var ovv2 = ov * v * 2;
            var a = -3 * ov2;
            var b = 3 * (ov2 - ovv2);
            var c = 3 * (ovv2 - v2);
            var d = 3 * v2;
            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];
                f0 = a * ak[j0][i0] + b * ak[j0 + 1][i0] + c * ak[j0 + 2][i0] + d * ak[j0 + 3][i0];
                f1 = a * ak[j0][i0 + 1] + b * ak[j0 + 1][i0 + 1] + c * ak[j0 + 2][i0 + 1] + d * ak[j0 + 3][i0 + 1];

                out[k] = ou * f0 + u * f1;
            }
            return out;
        };
    } else {
        // Finally, both directions are linear:
        /* eslint-disable no-unused-vars */
        return function(out, i0, j0, v, u) {
        /* eslint-enable no-unused-vars */
            if(!out) out = [];
            var f0, f1, k, ak;
            var ov = 1 - v;
            for(k = 0; k < arrays.length; k++) {
                ak = arrays[k];
                f0 = ak[j0 + 1][i0] - ak[j0][i0];
                f1 = ak[j0 + 1][i0 + 1] - ak[j0][i0 + 1];

                out[k] = ov * f0 + v * f1;
            }
            return out;
        };
    }
};
