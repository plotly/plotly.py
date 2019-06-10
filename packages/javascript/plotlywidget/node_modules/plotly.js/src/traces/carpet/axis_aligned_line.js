/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;

/* This function retrns a set of control points that define a curve aligned along
 * either the a or b axis. Exactly one of a or b must be an array defining the range
 * spanned.
 *
 * Honestly this is the most complicated function I've implemente here so far because
 * of the way it handles knot insertion and direction/axis-agnostic slices.
 */
module.exports = function(carpet, carpetcd, a, b) {
    var idx, tangent, tanIsoIdx, tanIsoPar, segment, refidx;
    var p0, p1, v0, v1, start, end, range;

    var axis = isArrayOrTypedArray(a) ? 'a' : 'b';
    var ax = axis === 'a' ? carpet.aaxis : carpet.baxis;
    var smoothing = ax.smoothing;
    var toIdx = axis === 'a' ? carpet.a2i : carpet.b2j;
    var pt = axis === 'a' ? a : b;
    var iso = axis === 'a' ? b : a;
    var n = axis === 'a' ? carpetcd.a.length : carpetcd.b.length;
    var m = axis === 'a' ? carpetcd.b.length : carpetcd.a.length;
    var isoIdx = Math.floor(axis === 'a' ? carpet.b2j(iso) : carpet.a2i(iso));

    var xy = axis === 'a' ? function(value) {
        return carpet.evalxy([], value, isoIdx);
    } : function(value) {
        return carpet.evalxy([], isoIdx, value);
    };

    if(smoothing) {
        tanIsoIdx = Math.max(0, Math.min(m - 2, isoIdx));
        tanIsoPar = isoIdx - tanIsoIdx;
        tangent = axis === 'a' ? function(i, ti) {
            return carpet.dxydi([], i, tanIsoIdx, ti, tanIsoPar);
        } : function(j, tj) {
            return carpet.dxydj([], tanIsoIdx, j, tanIsoPar, tj);
        };
    }

    var vstart = toIdx(pt[0]);
    var vend = toIdx(pt[1]);

    // So that we can make this work in two directions, flip all of the
    // math functions if the direction is from higher to lower indices:
    //
    // Note that the tolerance is directional!
    var dir = vstart < vend ? 1 : -1;
    var tol = (vend - vstart) * 1e-8;
    var dirfloor = dir > 0 ? Math.floor : Math.ceil;
    var dirceil = dir > 0 ? Math.ceil : Math.floor;
    var dirmin = dir > 0 ? Math.min : Math.max;
    var dirmax = dir > 0 ? Math.max : Math.min;

    var idx0 = dirfloor(vstart + tol);
    var idx1 = dirceil(vend - tol);

    p0 = xy(vstart);
    var segments = [[p0]];

    for(idx = idx0; idx * dir < idx1 * dir; idx += dir) {
        segment = [];
        start = dirmax(vstart, idx);
        end = dirmin(vend, idx + dir);
        range = end - start;

        // In order to figure out which cell we're in for the derivative (remember,
        // the derivatives are *not* constant across grid lines), let's just average
        // the start and end points. This cuts out just a tiny bit of logic and
        // there's really no computational difference:
        refidx = Math.max(0, Math.min(n - 2, Math.floor(0.5 * (start + end))));

        p1 = xy(end);
        if(smoothing) {
            v0 = tangent(refidx, start - refidx);
            v1 = tangent(refidx, end - refidx);

            segment.push([
                p0[0] + v0[0] / 3 * range,
                p0[1] + v0[1] / 3 * range
            ]);

            segment.push([
                p1[0] - v1[0] / 3 * range,
                p1[1] - v1[1] / 3 * range
            ]);
        }

        segment.push(p1);

        segments.push(segment);
        p0 = p1;
    }

    return segments;
};
