/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var mod = require('./mod').mod;

/*
 * look for intersection of two line segments
 *   (1->2 and 3->4) - returns array [x,y] if they do, null if not
 */
exports.segmentsIntersect = segmentsIntersect;
function segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4) {
    var a = x2 - x1;
    var b = x3 - x1;
    var c = x4 - x3;
    var d = y2 - y1;
    var e = y3 - y1;
    var f = y4 - y3;
    var det = a * f - c * d;
    // parallel lines? intersection is undefined
    // ignore the case where they are colinear
    if(det === 0) return null;
    var t = (b * f - c * e) / det;
    var u = (b * d - a * e) / det;
    // segments do not intersect?
    if(u < 0 || u > 1 || t < 0 || t > 1) return null;

    return {x: x1 + a * t, y: y1 + d * t};
}

/*
 * find the minimum distance between two line segments (1->2 and 3->4)
 */
exports.segmentDistance = function segmentDistance(x1, y1, x2, y2, x3, y3, x4, y4) {
    if(segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4)) return 0;

    // the two segments and their lengths squared
    var x12 = x2 - x1;
    var y12 = y2 - y1;
    var x34 = x4 - x3;
    var y34 = y4 - y3;
    var ll12 = x12 * x12 + y12 * y12;
    var ll34 = x34 * x34 + y34 * y34;

    // calculate distance squared, then take the sqrt at the very end
    var dist2 = Math.min(
        perpDistance2(x12, y12, ll12, x3 - x1, y3 - y1),
        perpDistance2(x12, y12, ll12, x4 - x1, y4 - y1),
        perpDistance2(x34, y34, ll34, x1 - x3, y1 - y3),
        perpDistance2(x34, y34, ll34, x2 - x3, y2 - y3)
    );

    return Math.sqrt(dist2);
};

/*
 * distance squared from segment ab to point c
 * [xab, yab] is the vector b-a
 * [xac, yac] is the vector c-a
 * llab is the length squared of (b-a), just to simplify calculation
 */
function perpDistance2(xab, yab, llab, xac, yac) {
    var fcAB = (xac * xab + yac * yab);
    if(fcAB < 0) {
        // point c is closer to point a
        return xac * xac + yac * yac;
    } else if(fcAB > llab) {
        // point c is closer to point b
        var xbc = xac - xab;
        var ybc = yac - yab;
        return xbc * xbc + ybc * ybc;
    } else {
        // perpendicular distance is the shortest
        var crossProduct = xac * yab - yac * xab;
        return crossProduct * crossProduct / llab;
    }
}

// a very short-term cache for getTextLocation, just because
// we're often looping over the same locations multiple times
// invalidated as soon as we look at a different path
var locationCache, workingPath, workingTextWidth;

// turn a path and position along it into x, y, and angle for the given text
exports.getTextLocation = function getTextLocation(path, totalPathLen, positionOnPath, textWidth) {
    if(path !== workingPath || textWidth !== workingTextWidth) {
        locationCache = {};
        workingPath = path;
        workingTextWidth = textWidth;
    }
    if(locationCache[positionOnPath]) {
        return locationCache[positionOnPath];
    }

    // for the angle, use points on the path separated by the text width
    // even though due to curvature, the text will cover a bit more than that
    var p0 = path.getPointAtLength(mod(positionOnPath - textWidth / 2, totalPathLen));
    var p1 = path.getPointAtLength(mod(positionOnPath + textWidth / 2, totalPathLen));
    // note: atan handles 1/0 nicely
    var theta = Math.atan((p1.y - p0.y) / (p1.x - p0.x));
    // center the text at 2/3 of the center position plus 1/3 the p0/p1 midpoint
    // that's the average position of this segment, assuming it's roughly quadratic
    var pCenter = path.getPointAtLength(mod(positionOnPath, totalPathLen));
    var x = (pCenter.x * 4 + p0.x + p1.x) / 6;
    var y = (pCenter.y * 4 + p0.y + p1.y) / 6;

    var out = {x: x, y: y, theta: theta};
    locationCache[positionOnPath] = out;
    return out;
};

exports.clearLocationCache = function() {
    workingPath = null;
};

/*
 * Find the segment of `path` that's within the visible area
 * given by `bounds` {left, right, top, bottom}, to within a
 * precision of `buffer` px
 *
 * returns: undefined if nothing is visible, else object:
 * {
 *   min: position where the path first enters bounds, or 0 if it
 *        starts within bounds
 *   max: position where the path last exits bounds, or the path length
 *        if it finishes within bounds
 *   len: max - min, ie the length of visible path
 *   total: the total path length - just included so the caller doesn't
 *        need to call path.getTotalLength() again
 *   isClosed: true iff the start and end points of the path are both visible
 *        and are at the same point
 * }
 *
 * Works by starting from either end and repeatedly finding the distance from
 * that point to the plot area, and if it's outside the plot, moving along the
 * path by that distance (because the plot must be at least that far away on
 * the path). Note that if a path enters, exits, and re-enters the plot, we
 * will not capture this behavior.
 */
exports.getVisibleSegment = function getVisibleSegment(path, bounds, buffer) {
    var left = bounds.left;
    var right = bounds.right;
    var top = bounds.top;
    var bottom = bounds.bottom;

    var pMin = 0;
    var pTotal = path.getTotalLength();
    var pMax = pTotal;

    var pt0, ptTotal;

    function getDistToPlot(len) {
        var pt = path.getPointAtLength(len);

        // hold on to the start and end points for `closed`
        if(len === 0) pt0 = pt;
        else if(len === pTotal) ptTotal = pt;

        var dx = (pt.x < left) ? left - pt.x : (pt.x > right ? pt.x - right : 0);
        var dy = (pt.y < top) ? top - pt.y : (pt.y > bottom ? pt.y - bottom : 0);
        return Math.sqrt(dx * dx + dy * dy);
    }

    var distToPlot = getDistToPlot(pMin);
    while(distToPlot) {
        pMin += distToPlot + buffer;
        if(pMin > pMax) return;
        distToPlot = getDistToPlot(pMin);
    }

    distToPlot = getDistToPlot(pMax);
    while(distToPlot) {
        pMax -= distToPlot + buffer;
        if(pMin > pMax) return;
        distToPlot = getDistToPlot(pMax);
    }

    return {
        min: pMin,
        max: pMax,
        len: pMax - pMin,
        total: pTotal,
        isClosed: pMin === 0 && pMax === pTotal &&
            Math.abs(pt0.x - ptTotal.x) < 0.1 &&
            Math.abs(pt0.y - ptTotal.y) < 0.1
    };
};

/**
 * Find point on SVG path corresponding to a given constraint coordinate
 *
 * @param {SVGPathElement} path
 * @param {Number} val : constraint coordinate value
 * @param {String} coord : 'x' or 'y' the constraint coordinate
 * @param {Object} opts :
 *  - {Number} pathLength : supply total path length before hand
 *  - {Number} tolerance
 *  - {Number} iterationLimit
 * @return {SVGPoint}
 */
exports.findPointOnPath = function findPointOnPath(path, val, coord, opts) {
    opts = opts || {};

    var pathLength = opts.pathLength || path.getTotalLength();
    var tolerance = opts.tolerance || 1e-3;
    var iterationLimit = opts.iterationLimit || 30;

    // if path starts at a val greater than the path tail (like on vertical violins),
    // we must flip the sign of the computed diff.
    var mul = path.getPointAtLength(0)[coord] > path.getPointAtLength(pathLength)[coord] ? -1 : 1;

    var i = 0;
    var b0 = 0;
    var b1 = pathLength;
    var mid;
    var pt;
    var diff;

    while(i < iterationLimit) {
        mid = (b0 + b1) / 2;
        pt = path.getPointAtLength(mid);
        diff = pt[coord] - val;

        if(Math.abs(diff) < tolerance) {
            return pt;
        } else {
            if(mul * diff > 0) {
                b1 = mid;
            } else {
                b0 = mid;
            }
            i++;
        }
    }
    return pt;
};
