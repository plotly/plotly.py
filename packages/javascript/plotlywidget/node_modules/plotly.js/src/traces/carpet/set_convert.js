/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var constants = require('./constants');
var search = require('../../lib/search').findBin;
var computeControlPoints = require('./compute_control_points');
var createSplineEvaluator = require('./create_spline_evaluator');
var createIDerivativeEvaluator = require('./create_i_derivative_evaluator');
var createJDerivativeEvaluator = require('./create_j_derivative_evaluator');

/*
 * Create conversion functions to go from one basis to another. In particular the letter
 * abbreviations are:
 *
 *   i: i/j coordinates along the grid. Integer values correspond to data points
 *   a: real-valued coordinates along the a/b axes
 *   c: cartesian x-y coordinates
 *   p: screen-space pixel coordinates
 */
module.exports = function setConvert(trace) {
    var a = trace._a;
    var b = trace._b;
    var na = a.length;
    var nb = b.length;
    var aax = trace.aaxis;
    var bax = trace.baxis;

    // Grab the limits once rather than recomputing the bounds for every point
    // independently:
    var amin = a[0];
    var amax = a[na - 1];
    var bmin = b[0];
    var bmax = b[nb - 1];
    var arange = a[a.length - 1] - a[0];
    var brange = b[b.length - 1] - b[0];

    // Compute the tolerance so that points are visible slightly outside the
    // defined carpet axis:
    var atol = arange * constants.RELATIVE_CULL_TOLERANCE;
    var btol = brange * constants.RELATIVE_CULL_TOLERANCE;

    // Expand the limits to include the relative tolerance:
    amin -= atol;
    amax += atol;
    bmin -= btol;
    bmax += btol;

    trace.isVisible = function(a, b) {
        return a > amin && a < amax && b > bmin && b < bmax;
    };

    trace.isOccluded = function(a, b) {
        return a < amin || a > amax || b < bmin || b > bmax;
    };

    trace.setScale = function() {
        var x = trace._x;
        var y = trace._y;

        // This is potentially a very expensive step! It does the bulk of the work of constructing
        // an expanded basis of control points. Note in particular that it overwrites the existing
        // basis without creating a new array since that would potentially thrash the garbage
        // collector.
        var result = computeControlPoints(trace._xctrl, trace._yctrl, x, y, aax.smoothing, bax.smoothing);
        trace._xctrl = result[0];
        trace._yctrl = result[1];

        // This step is the second step in the process, but it's somewhat simpler. It just unrolls
        // some logic since it would be unnecessarily expensive to compute both interpolations
        // nearly identically but separately and to include a bunch of linear vs. bicubic logic in
        // every single call.
        trace.evalxy = createSplineEvaluator([trace._xctrl, trace._yctrl], na, nb, aax.smoothing, bax.smoothing);

        trace.dxydi = createIDerivativeEvaluator([trace._xctrl, trace._yctrl], aax.smoothing, bax.smoothing);
        trace.dxydj = createJDerivativeEvaluator([trace._xctrl, trace._yctrl], aax.smoothing, bax.smoothing);
    };

    /*
     * Convert from i/j data grid coordinates to a/b values. Note in particular that this
     * is *linear* interpolation, even if the data is interpolated bicubically.
     */
    trace.i2a = function(i) {
        var i0 = Math.max(0, Math.floor(i[0]), na - 2);
        var ti = i[0] - i0;
        return (1 - ti) * a[i0] + ti * a[i0 + 1];
    };

    trace.j2b = function(j) {
        var j0 = Math.max(0, Math.floor(j[1]), na - 2);
        var tj = j[1] - j0;
        return (1 - tj) * b[j0] + tj * b[j0 + 1];
    };

    trace.ij2ab = function(ij) {
        return [trace.i2a(ij[0]), trace.j2b(ij[1])];
    };

    /*
     * Convert from a/b coordinates to i/j grid-numbered coordinates. This requires searching
     * through the a/b data arrays and assumes they are monotonic, which is presumed to have
     * been enforced already.
     */
    trace.a2i = function(aval) {
        var i0 = Math.max(0, Math.min(search(aval, a), na - 2));
        var a0 = a[i0];
        var a1 = a[i0 + 1];
        return Math.max(0, Math.min(na - 1, i0 + (aval - a0) / (a1 - a0)));
    };

    trace.b2j = function(bval) {
        var j0 = Math.max(0, Math.min(search(bval, b), nb - 2));
        var b0 = b[j0];
        var b1 = b[j0 + 1];
        return Math.max(0, Math.min(nb - 1, j0 + (bval - b0) / (b1 - b0)));
    };

    trace.ab2ij = function(ab) {
        return [trace.a2i(ab[0]), trace.b2j(ab[1])];
    };

    /*
     * Convert from i/j coordinates to x/y caretesian coordinates. This means either bilinear
     * or bicubic spline evaluation, but the hard part is already done at this point.
     */
    trace.i2c = function(i, j) {
        return trace.evalxy([], i, j);
    };

    trace.ab2xy = function(aval, bval, extrapolate) {
        if(!extrapolate && (aval < a[0] || aval > a[na - 1] | bval < b[0] || bval > b[nb - 1])) {
            return [false, false];
        }
        var i = trace.a2i(aval);
        var j = trace.b2j(bval);

        var pt = trace.evalxy([], i, j);

        if(extrapolate) {
            // This section uses the boundary derivatives to extrapolate linearly outside
            // the defined range. Consider a scatter line with one point inside the carpet
            // axis and one point outside. If we don't extrapolate, we can't draw the line
            // at all.
            var iex = 0;
            var jex = 0;
            var der = [];

            var i0, ti, j0, tj;
            if(aval < a[0]) {
                i0 = 0;
                ti = 0;
                iex = (aval - a[0]) / (a[1] - a[0]);
            } else if(aval > a[na - 1]) {
                i0 = na - 2;
                ti = 1;
                iex = (aval - a[na - 1]) / (a[na - 1] - a[na - 2]);
            } else {
                i0 = Math.max(0, Math.min(na - 2, Math.floor(i)));
                ti = i - i0;
            }

            if(bval < b[0]) {
                j0 = 0;
                tj = 0;
                jex = (bval - b[0]) / (b[1] - b[0]);
            } else if(bval > b[nb - 1]) {
                j0 = nb - 2;
                tj = 1;
                jex = (bval - b[nb - 1]) / (b[nb - 1] - b[nb - 2]);
            } else {
                j0 = Math.max(0, Math.min(nb - 2, Math.floor(j)));
                tj = j - j0;
            }

            if(iex) {
                trace.dxydi(der, i0, j0, ti, tj);
                pt[0] += der[0] * iex;
                pt[1] += der[1] * iex;
            }

            if(jex) {
                trace.dxydj(der, i0, j0, ti, tj);
                pt[0] += der[0] * jex;
                pt[1] += der[1] * jex;
            }
        }

        return pt;
    };


    trace.c2p = function(xy, xa, ya) {
        return [xa.c2p(xy[0]), ya.c2p(xy[1])];
    };

    trace.p2x = function(p, xa, ya) {
        return [xa.p2c(p[0]), ya.p2c(p[1])];
    };

    trace.dadi = function(i /* , u*/) {
        // Right now only a piecewise linear a or b basis is permitted since smoother interpolation
        // would cause monotonicity problems. As a retult, u is entirely disregarded in this
        // computation, though we'll specify it as a parameter for the sake of completeness and
        // future-proofing. It would be possible to use monotonic cubic interpolation, for example.
        //
        // See: https://en.wikipedia.org/wiki/Monotone_cubic_interpolation

        // u = u || 0;

        var i0 = Math.max(0, Math.min(a.length - 2, i));

        // The step (demoninator) is implicitly 1 since that's the grid spacing.
        return a[i0 + 1] - a[i0];
    };

    trace.dbdj = function(j /* , v*/) {
        // See above caveats for dadi which also apply here
        var j0 = Math.max(0, Math.min(b.length - 2, j));

        // The step (demoninator) is implicitly 1 since that's the grid spacing.
        return b[j0 + 1] - b[j0];
    };

    // Takes: grid cell coordinate (i, j) and fractional grid cell coordinates (u, v)
    // Returns: (dx/da, dy/db)
    //
    // NB: separate grid cell + fractional grid cell coordinate format is due to the discontinuous
    // derivative, as described better in create_i_derivative_evaluator.js
    trace.dxyda = function(i0, j0, u, v) {
        var dxydi = trace.dxydi(null, i0, j0, u, v);
        var dadi = trace.dadi(i0, u);

        return [dxydi[0] / dadi, dxydi[1] / dadi];
    };

    trace.dxydb = function(i0, j0, u, v) {
        var dxydj = trace.dxydj(null, i0, j0, u, v);
        var dbdj = trace.dbdj(j0, v);

        return [dxydj[0] / dbdj, dxydj[1] / dbdj];
    };

    // Sometimes we don't care about precision and all we really want is decent rough
    // directions (as is the case with labels). In that case, we can do a very rough finite
    // difference and spare having to worry about precise grid coordinates:
    trace.dxyda_rough = function(a, b, reldiff) {
        var h = arange * (reldiff || 0.1);
        var plus = trace.ab2xy(a + h, b, true);
        var minus = trace.ab2xy(a - h, b, true);

        return [
            (plus[0] - minus[0]) * 0.5 / h,
            (plus[1] - minus[1]) * 0.5 / h
        ];
    };

    trace.dxydb_rough = function(a, b, reldiff) {
        var h = brange * (reldiff || 0.1);
        var plus = trace.ab2xy(a, b + h, true);
        var minus = trace.ab2xy(a, b - h, true);

        return [
            (plus[0] - minus[0]) * 0.5 / h,
            (plus[1] - minus[1]) * 0.5 / h
        ];
    };

    trace.dpdx = function(xa) {
        return xa._m;
    };

    trace.dpdy = function(ya) {
        return ya._m;
    };
};
