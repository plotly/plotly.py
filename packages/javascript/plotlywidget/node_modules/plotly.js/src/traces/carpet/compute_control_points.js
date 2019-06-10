/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var makeControlPoints = require('./catmull_rom');
var ensureArray = require('../../lib').ensureArray;

/*
 * Turns a coarse grid into a fine grid with control points.
 *
 * Here's an ASCII representation:
 *
 *       o ----- o ----- o ----- o
 *       |       |       |       |
 *       |       |       |       |
 *       |       |       |       |
 *       o ----- o ----- o ----- o
 *       |       |       |       |
 *       |       |       |       |
 *    ^  |       |       |       |
 *    |  o ----- o ----- o ----- o
 *  b |  |       |       |       |
 *    |  |       |       |       |
 *    |  |       |       |       |
 *       o ----- o ----- o ----- o
 *         ------>
 *           a
 *
 * First of all, note that we want to do this in *cartesian* space. This means
 * we might run into problems when there are extreme differences in x/y scaling,
 * but the alternative is that the topology of the contours might actually be
 * view-dependent, which seems worse. As a fallback, the only parameter that
 * actually affects the result is the *aspect ratio*, so that we can at least
 * improve the situation a bit without going all the way to screen coordinates.
 *
 * This function flattens the points + tangents  into a slightly denser grid of
 * *control points*. The resulting grid looks like this:
 *
 *       9 +--o-o--+ -o-o--+--o-o--+
 *       8 o  o o  o  o o  o  o o  o
 *         |       |       |       |
 *       7 o  o o  o  o o  o  o o  o
 *       6 +--o-o--+ -o-o--+--o-o--+
 *       5 o  o o  o  o o  o  o o  o
 *         |       |       |       |
 *    ^  4 o  o o  o  o o  o  o o  o
 *    |  3 +--o-o--+ -o-o--+--o-o--+
 *  b |  2 o  o o  o  o o  o  o o  o
 *    |    |       |       |       |
 *    |  1 o  o o  o  o o  o  o o  o
 *       0 +--o-o--+ -o-o--+--o-o--+
 *         0  1 2  3  4 5  6  7 8  9
 *         ------>
 *           a
 *
 * where `o`s represent newly-computed control points. the resulting dimension is
 *
 *     (m - 1) * 3 + 1
 *   = 3 * m - 2
 *
 * We could simply store the tangents separately, but that's a nightmare to organize
 * in two dimensions since we'll be slicing grid lines in both directions and since
 * that basically requires very nearly just as much storage as just storing the dense
 * grid.
 *
 * Wow!
 */


/*
 * Catmull-rom is biased at the boundaries toward the interior and we actually
 * can't use catmull-rom to compute the control point closest to (but inside)
 * the boundary.
 *
 * A note on plotly's spline interpolation. It uses the catmull rom control point
 * closest to the boundary *as* a quadratic control point. This seems incorrect,
 * so I've elected not to follow that. Given control points 0 and 1, regular plotly
 * splines give *equivalent* cubic control points:
 *
 * Input:
 *
 *   boundary
 *     |                    |
 *     p0           p2      p3    --> interior
 *     0.0          0.667   1.0
 *     |                    |
 *
 * Cubic-equivalent of what plotly splines draw::
 *
 *   boundary
 *     |                    |
 *     p0   p1      p2      p3    --> interior
 *     0.0  0.4444  0.8888  1.0
 *     |                    |
 *
 * What this function fills in:
 *
 *   boundary
 *     |                    |
 *     p0    p1     p2      p3    --> interior
 *     0.0   0.333  0.667   1.0
 *     |                    |
 *
 * Parameters:
 *   p0: boundary point
 *   p2: catmull rom point based on computation at p3
 *   p3: first grid point
 *
 * Of course it works whichever way it's oriented; you just need to interpret the
 * input/output accordingly.
 */
function inferCubicControlPoint(p0, p2, p3) {
    // Extend p1 away from p0 by 50%. This is the equivalent quadratic point that
    // would give the same slope as catmull rom at p0.
    var p2e0 = -0.5 * p3[0] + 1.5 * p2[0];
    var p2e1 = -0.5 * p3[1] + 1.5 * p2[1];

    return [
        (2 * p2e0 + p0[0]) / 3,
        (2 * p2e1 + p0[1]) / 3,
    ];
}

module.exports = function computeControlPoints(xe, ye, x, y, asmoothing, bsmoothing) {
    var i, j, ie, je, xej, yej, xj, yj, cp, p1;
    // At this point, we know these dimensions are correct and representative of
    // the whole 2D arrays:
    var na = x[0].length;
    var nb = x.length;

    // (n)umber of (e)xpanded points:
    var nea = asmoothing ? 3 * na - 2 : na;
    var neb = bsmoothing ? 3 * nb - 2 : nb;

    xe = ensureArray(xe, neb);
    ye = ensureArray(ye, neb);

    for(ie = 0; ie < neb; ie++) {
        xe[ie] = ensureArray(xe[ie], nea);
        ye[ie] = ensureArray(ye[ie], nea);
    }

    // This loop fills in the X'd points:
    //
    //    .       .       .       .
    //    .       .       .       .
    //    |       |       |       |
    //    |       |       |       |
    //    X ----- X ----- X ----- X
    //    |       |       |       |
    //    |       |       |       |
    //    |       |       |       |
    //    X ----- X ----- X ----- X
    //
    //
    // ie = (i) (e)xpanded:
    for(j = 0, je = 0; j < nb; j++, je += bsmoothing ? 3 : 1) {
        xej = xe[je];
        yej = ye[je];
        xj = x[j];
        yj = y[j];

        // je = (j) (e)xpanded:
        for(i = 0, ie = 0; i < na; i++, ie += asmoothing ? 3 : 1) {
            xej[ie] = xj[i];
            yej[ie] = yj[i];
        }
    }

    if(asmoothing) {
        // If there's a-smoothing, this loop fills in the X'd points with catmull-rom
        // control points computed along the a-axis:
        //     .       .       .       .
        //     .       .       .       .
        //     |       |       |       |
        //     |       |       |       |
        //     o -Y-X- o -X-X- o -X-Y- o
        //     |       |       |       |
        //     |       |       |       |
        //     |       |       |       |
        //     o -Y-X- o -X-X- o -X-Y- o
        //
        // i:  0       1       2       3
        // ie: 0  1 3  3  4 5  6  7 8  9
        //
        //           ------>
        //             a
        //
        for(j = 0, je = 0; j < nb; j++, je += bsmoothing ? 3 : 1) {
            // Fill in the points marked X for this a-row:
            for(i = 1, ie = 3; i < na - 1; i++, ie += 3) {
                cp = makeControlPoints(
                    [x[j][i - 1], y[j][i - 1]],
                    [x[j][i ], y[j][i]],
                    [x[j][i + 1], y[j][i + 1]],
                    asmoothing
                );

                xe[je][ie - 1] = cp[0][0];
                ye[je][ie - 1] = cp[0][1];
                xe[je][ie + 1] = cp[1][0];
                ye[je][ie + 1] = cp[1][1];
            }

            // The very first cubic interpolation point (to the left for i = 1 above) is
            // used as a *quadratic* interpolation point by the spline drawing function
            // which isn't really correct. But for the sake of consistency, we'll use it
            // as such. Since we're using cubic splines, that means we need to shorten the
            // tangent by 1/3 and also construct a new cubic spline control point 1/3 from
            // the original to the i = 0 point.
            p1 = inferCubicControlPoint(
                [xe[je][0], ye[je][0]],
                [xe[je][2], ye[je][2]],
                [xe[je][3], ye[je][3]]
            );
            xe[je][1] = p1[0];
            ye[je][1] = p1[1];

            // Ditto last points, sans explanation:
            p1 = inferCubicControlPoint(
                [xe[je][nea - 1], ye[je][nea - 1]],
                [xe[je][nea - 3], ye[je][nea - 3]],
                [xe[je][nea - 4], ye[je][nea - 4]]
            );
            xe[je][nea - 2] = p1[0];
            ye[je][nea - 2] = p1[1];
        }
    }

    if(bsmoothing) {
        // If there's a-smoothing, this loop fills in the X'd points with catmull-rom
        // control points computed along the b-axis:
        //     .       .       .       .
        //     X  X X  X  X X  X  X X  X
        //     |       |       |       |
        //     X  X X  X  X X  X  X X  X
        //     o -o-o- o -o-o- o -o-o- o
        //     X  X X  X  X X  X  X X  X
        //     |       |       |       |
        //     Y  Y Y  Y  Y Y  Y  Y Y  Y
        //     o -o-o- o -o-o- o -o-o- o
        //
        // i:  0       1       2       3
        // ie: 0  1 3  3  4 5  6  7 8  9
        //
        //           ------>
        //             a
        //
        for(ie = 0; ie < nea; ie++) {
            for(je = 3; je < neb - 3; je += 3) {
                cp = makeControlPoints(
                    [xe[je - 3][ie], ye[je - 3][ie]],
                    [xe[je][ie], ye[je][ie]],
                    [xe[je + 3][ie], ye[je + 3][ie]],
                    bsmoothing
                );

                xe[je - 1][ie] = cp[0][0];
                ye[je - 1][ie] = cp[0][1];
                xe[je + 1][ie] = cp[1][0];
                ye[je + 1][ie] = cp[1][1];
            }
            // Do the same boundary condition magic for these control points marked Y above:
            p1 = inferCubicControlPoint(
                [xe[0][ie], ye[0][ie]],
                [xe[2][ie], ye[2][ie]],
                [xe[3][ie], ye[3][ie]]
            );
            xe[1][ie] = p1[0];
            ye[1][ie] = p1[1];

            p1 = inferCubicControlPoint(
                [xe[neb - 1][ie], ye[neb - 1][ie]],
                [xe[neb - 3][ie], ye[neb - 3][ie]],
                [xe[neb - 4][ie], ye[neb - 4][ie]]
            );
            xe[neb - 2][ie] = p1[0];
            ye[neb - 2][ie] = p1[1];
        }
    }

    if(asmoothing && bsmoothing) {
        // Do one more pass, this time recomputing exactly what we just computed.
        // It's overdetermined since we're peforming catmull-rom in two directions,
        // so we'll just average the overdetermined. These points don't lie along the
        // grid lines, so note that only grid lines will follow normal plotly spline
        // interpolation.
        //
        // Unless of course there was no b smoothing. Then these intermediate points
        // don't actually exist and this section is bypassed.
        //     .       .       .       .
        //     o  X X  o  X X  o  X X  o
        //     |       |       |       |
        //     o  X X  o  X X  o  X X  o
        //     o -o-o- o -o-o- o -o-o- o
        //     o  X X  o  X X  o  X X  o
        //     |       |       |       |
        //     o  Y Y  o  Y Y  o  Y Y  o
        //     o -o-o- o -o-o- o -o-o- o
        //
        // i:  0       1       2       3
        // ie: 0  1 3  3  4 5  6  7 8  9
        //
        //           ------>
        //             a
        //
        for(je = 1; je < neb; je += (je + 1) % 3 === 0 ? 2 : 1) {
            // Fill in the points marked X for this a-row:
            for(ie = 3; ie < nea - 3; ie += 3) {
                cp = makeControlPoints(
                    [xe[je][ie - 3], ye[je][ie - 3]],
                    [xe[je][ie], ye[je][ie]],
                    [xe[je][ie + 3], ye[je][ie + 3]],
                    asmoothing
                );

                xe[je][ie - 1] = 0.5 * (xe[je][ie - 1] + cp[0][0]);
                ye[je][ie - 1] = 0.5 * (ye[je][ie - 1] + cp[0][1]);
                xe[je][ie + 1] = 0.5 * (xe[je][ie + 1] + cp[1][0]);
                ye[je][ie + 1] = 0.5 * (ye[je][ie + 1] + cp[1][1]);
            }

            // This case is just slightly different. The computation is the same,
            // but having computed this, we'll average with the existing result.
            p1 = inferCubicControlPoint(
                [xe[je][0], ye[je][0]],
                [xe[je][2], ye[je][2]],
                [xe[je][3], ye[je][3]]
            );
            xe[je][1] = 0.5 * (xe[je][1] + p1[0]);
            ye[je][1] = 0.5 * (ye[je][1] + p1[1]);

            p1 = inferCubicControlPoint(
                [xe[je][nea - 1], ye[je][nea - 1]],
                [xe[je][nea - 3], ye[je][nea - 3]],
                [xe[je][nea - 4], ye[je][nea - 4]]
            );
            xe[je][nea - 2] = 0.5 * (xe[je][nea - 2] + p1[0]);
            ye[je][nea - 2] = 0.5 * (ye[je][nea - 2] + p1[1]);
        }
    }

    return [xe, ye];
};
