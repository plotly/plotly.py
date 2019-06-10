/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

/*
 * Given a 2D array as well as a basis in either direction, this function fills in the
 * 2D array using a combination of smoothing and extrapolation. This is rather important
 * for carpet plots since it's used for layout so that we can't simply omit or blank out
 * points. We need a reasonable guess so that the interpolation puts points somewhere
 * even if we were to somehow represent that the data was missing later on.
 *
 * input:
 *  - data: 2D array of arrays
 *  - a: array such that a.length === data[0].length
 *  - b: array such that b.length === data.length
 */
module.exports = function smoothFill2dArray(data, a, b) {
    var i, j, k;
    var ip = [];
    var jp = [];
    // var neighborCnts = [];

    var ni = data[0].length;
    var nj = data.length;

    function avgSurrounding(i, j) {
        // As a low-quality start, we can simply average surrounding points (in a not
        // non-uniform grid aware manner):
        var sum = 0.0;
        var val;
        var cnt = 0;
        if(i > 0 && (val = data[j][i - 1]) !== undefined) {
            cnt++;
            sum += val;
        }
        if(i < ni - 1 && (val = data[j][i + 1]) !== undefined) {
            cnt++;
            sum += val;
        }
        if(j > 0 && (val = data[j - 1][i]) !== undefined) {
            cnt++;
            sum += val;
        }
        if(j < nj - 1 && (val = data[j + 1][i]) !== undefined) {
            cnt++;
            sum += val;
        }
        return sum / Math.max(1, cnt);
    }

    // This loop iterates over all cells. Any cells that are null will be noted and those
    // are the only points we will loop over and update via laplace's equation. Points with
    // any neighbors will receive the average. If there are no neighboring points, then they
    // will be set to zero. Also as we go, track the maximum magnitude so that we can scale
    // our tolerance accordingly.
    var dmax = 0.0;
    for(i = 0; i < ni; i++) {
        for(j = 0; j < nj; j++) {
            if(data[j][i] === undefined) {
                ip.push(i);
                jp.push(j);

                data[j][i] = avgSurrounding(i, j);
                // neighborCnts.push(result.neighbors);
            }
            dmax = Math.max(dmax, Math.abs(data[j][i]));
        }
    }

    if(!ip.length) return data;

    // The tolerance doesn't need to be excessive. It's just for display positioning
    var dxp, dxm, dap, dam, dbp, dbm, c, d, diff, reldiff, overrelaxation;
    var tol = 1e-5;
    var resid = 0;
    var itermax = 100;
    var iter = 0;
    var n = ip.length;
    do {
        resid = 0;
        // Normally we'd loop in two dimensions, but not all points are blank and need
        // an update, so we instead loop only over the points that were tabulated above
        for(k = 0; k < n; k++) {
            i = ip[k];
            j = jp[k];
            // neighborCnt = neighborCnts[k];

            // Track a counter for how many contributions there are. We'll use this counter
            // to average at the end, which reduces to laplace's equation with neumann boundary
            // conditions on the first derivative (second derivative is zero so that we get
            // a nice linear extrapolation at the boundaries).
            var boundaryCnt = 0;
            var newVal = 0;

            var d0, d1, x0, x1, i0, j0;
            if(i === 0) {
                // If this lies along the i = 0 boundary, extrapolate from the two points
                // to the right of this point. Note that the finite differences take into
                // account non-uniform grid spacing:
                i0 = Math.min(ni - 1, 2);
                x0 = a[i0];
                x1 = a[1];
                d0 = data[j][i0];
                d1 = data[j][1];
                newVal += d1 + (d1 - d0) * (a[0] - x1) / (x1 - x0);
                boundaryCnt++;
            } else if(i === ni - 1) {
                // If along the high i boundary, extrapolate from the two points to the
                // left of this point
                i0 = Math.max(0, ni - 3);
                x0 = a[i0];
                x1 = a[ni - 2];
                d0 = data[j][i0];
                d1 = data[j][ni - 2];
                newVal += d1 + (d1 - d0) * (a[ni - 1] - x1) / (x1 - x0);
                boundaryCnt++;
            }

            if((i === 0 || i === ni - 1) && (j > 0 && j < nj - 1)) {
                // If along the min(i) or max(i) boundaries, also smooth vertically as long
                // as we're not in a corner. Note that the finite differences used here
                // are also aware of nonuniform grid spacing:
                dxp = b[j + 1] - b[j];
                dxm = b[j] - b[j - 1];
                newVal += (dxm * data[j + 1][i] + dxp * data[j - 1][i]) / (dxm + dxp);
                boundaryCnt++;
            }

            if(j === 0) {
                // If along the j = 0 boundary, extrpolate this point from the two points
                // above it
                j0 = Math.min(nj - 1, 2);
                x0 = b[j0];
                x1 = b[1];
                d0 = data[j0][i];
                d1 = data[1][i];
                newVal += d1 + (d1 - d0) * (b[0] - x1) / (x1 - x0);
                boundaryCnt++;
            } else if(j === nj - 1) {
                // Same for the max j boundary from the cells below it:
                j0 = Math.max(0, nj - 3);
                x0 = b[j0];
                x1 = b[nj - 2];
                d0 = data[j0][i];
                d1 = data[nj - 2][i];
                newVal += d1 + (d1 - d0) * (b[nj - 1] - x1) / (x1 - x0);
                boundaryCnt++;
            }

            if((j === 0 || j === nj - 1) && (i > 0 && i < ni - 1)) {
                // Now average points to the left/right as long as not in a corner:
                dxp = a[i + 1] - a[i];
                dxm = a[i] - a[i - 1];
                newVal += (dxm * data[j][i + 1] + dxp * data[j][i - 1]) / (dxm + dxp);
                boundaryCnt++;
            }

            if(!boundaryCnt) {
                // If none of the above conditions were triggered, then this is an interior
                // point and we can just do a laplace equation update. As above, these differences
                // are aware of nonuniform grid spacing:
                dap = a[i + 1] - a[i];
                dam = a[i] - a[i - 1];
                dbp = b[j + 1] - b[j];
                dbm = b[j] - b[j - 1];

                // These are just some useful constants for the iteration, which is perfectly
                // straightforward but a little long to derive from f_xx + f_yy = 0.
                c = dap * dam * (dap + dam);
                d = dbp * dbm * (dbp + dbm);

                newVal = (c * (dbm * data[j + 1][i] + dbp * data[j - 1][i]) +
                          d * (dam * data[j][i + 1] + dap * data[j][i - 1])) /
                          (d * (dam + dap) + c * (dbm + dbp));
            } else {
                // If we did have contributions from the boundary conditions, then average
                // the result from the various contributions:
                newVal /= boundaryCnt;
            }

            // Jacobi updates are ridiculously slow to converge, so this approach uses a
            // Gauss-seidel iteration which is dramatically faster.
            diff = newVal - data[j][i];
            reldiff = diff / dmax;
            resid += reldiff * reldiff;

            // Gauss-Seidel-ish iteration, omega chosen based on heuristics and some
            // quick tests.
            //
            // NB: Don't overrelax the boundarie. Otherwise set an overrelaxation factor
            // which is a little low but safely optimal-ish:
            overrelaxation = boundaryCnt ? 0 : 0.85;

            // If there are four non-null neighbors, then we want a simple average without
            // overrelaxation. If all the surrouding points are null, then we want the full
            // overrelaxation
            //
            // Based on experiments, this actually seems to slow down convergence just a bit.
            // I'll leave it here for reference in case this needs to be revisited, but
            // it seems to work just fine without this.
            // if (overrelaxation) overrelaxation *= (4 - neighborCnt) / 4;

            data[j][i] += diff * (1 + overrelaxation);
        }

        resid = Math.sqrt(resid);
    } while(iter++ < itermax && resid > tol);

    Lib.log('Smoother converged to', resid, 'after', iter, 'iterations');

    return data;
};
