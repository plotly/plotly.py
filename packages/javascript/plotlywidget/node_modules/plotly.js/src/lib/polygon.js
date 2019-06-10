/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var dot = require('./matrix').dot;
var BADNUM = require('../constants/numerical').BADNUM;

var polygon = module.exports = {};

/**
 * Turn an array of [x, y] pairs into a polygon object
 * that can test if points are inside it
 *
 * @param ptsIn Array of [x, y] pairs
 *
 * @returns polygon Object {xmin, xmax, ymin, ymax, pts, contains}
 *      (x|y)(min|max) are the bounding rect of the polygon
 *      pts is the original array, with the first pair repeated at the end
 *      contains is a function: (pt, omitFirstEdge)
 *          pt is the [x, y] pair to test
 *          omitFirstEdge truthy means points exactly on the first edge don't
 *              count. This is for use adding one polygon to another so we
 *              don't double-count the edge where they meet.
 *          returns boolean: is pt inside the polygon (including on its edges)
 */
polygon.tester = function tester(ptsIn) {
    var pts = ptsIn.slice();
    var xmin = pts[0][0];
    var xmax = xmin;
    var ymin = pts[0][1];
    var ymax = ymin;
    var i;

    pts.push(pts[0]);
    for(i = 1; i < pts.length; i++) {
        xmin = Math.min(xmin, pts[i][0]);
        xmax = Math.max(xmax, pts[i][0]);
        ymin = Math.min(ymin, pts[i][1]);
        ymax = Math.max(ymax, pts[i][1]);
    }

    // do we have a rectangle? Handle this here, so we can use the same
    // tester for the rectangular case without sacrificing speed

    var isRect = false;
    var rectFirstEdgeTest;

    if(pts.length === 5) {
        if(pts[0][0] === pts[1][0]) { // vert, horz, vert, horz
            if(pts[2][0] === pts[3][0] &&
                    pts[0][1] === pts[3][1] &&
                    pts[1][1] === pts[2][1]) {
                isRect = true;
                rectFirstEdgeTest = function(pt) { return pt[0] === pts[0][0]; };
            }
        } else if(pts[0][1] === pts[1][1]) { // horz, vert, horz, vert
            if(pts[2][1] === pts[3][1] &&
                    pts[0][0] === pts[3][0] &&
                    pts[1][0] === pts[2][0]) {
                isRect = true;
                rectFirstEdgeTest = function(pt) { return pt[1] === pts[0][1]; };
            }
        }
    }

    function rectContains(pt, omitFirstEdge) {
        var x = pt[0];
        var y = pt[1];

        if(x === BADNUM || x < xmin || x > xmax || y === BADNUM || y < ymin || y > ymax) {
            // pt is outside the bounding box of polygon
            return false;
        }
        if(omitFirstEdge && rectFirstEdgeTest(pt)) return false;

        return true;
    }

    function contains(pt, omitFirstEdge) {
        var x = pt[0];
        var y = pt[1];

        if(x === BADNUM || x < xmin || x > xmax || y === BADNUM || y < ymin || y > ymax) {
            // pt is outside the bounding box of polygon
            return false;
        }

        var imax = pts.length;
        var x1 = pts[0][0];
        var y1 = pts[0][1];
        var crossings = 0;
        var i;
        var x0;
        var y0;
        var xmini;
        var ycross;

        for(i = 1; i < imax; i++) {
            // find all crossings of a vertical line upward from pt with
            // polygon segments
            // crossings exactly at xmax don't count, unless the point is
            // exactly on the segment, then it counts as inside.
            x0 = x1;
            y0 = y1;
            x1 = pts[i][0];
            y1 = pts[i][1];
            xmini = Math.min(x0, x1);

            if(x < xmini || x > Math.max(x0, x1) || y > Math.max(y0, y1)) {
                // outside the bounding box of this segment, it's only a crossing
                // if it's below the box.

                continue;
            } else if(y < Math.min(y0, y1)) {
                // don't count the left-most point of the segment as a crossing
                // because we don't want to double-count adjacent crossings
                // UNLESS the polygon turns past vertical at exactly this x
                // Note that this is repeated below, but we can't factor it out
                // because
                if(x !== xmini) crossings++;
            } else {
                // inside the bounding box, check the actual line intercept

                // vertical segment - we know already that the point is exactly
                // on the segment, so mark the crossing as exactly at the point.
                if(x1 === x0) ycross = y;
                // any other angle
                else ycross = y0 + (x - x0) * (y1 - y0) / (x1 - x0);

                // exactly on the edge: counts as inside the polygon, unless it's the
                // first edge and we're omitting it.
                if(y === ycross) {
                    if(i === 1 && omitFirstEdge) return false;
                    return true;
                }

                if(y <= ycross && x !== xmini) crossings++;
            }
        }

        // if we've gotten this far, odd crossings means inside, even is outside
        return crossings % 2 === 1;
    }

    // detect if poly is degenerate
    var degenerate = true;
    var lastPt = pts[0];
    for(i = 1; i < pts.length; i++) {
        if(lastPt[0] !== pts[i][0] || lastPt[1] !== pts[i][1]) {
            degenerate = false;
            break;
        }
    }

    return {
        xmin: xmin,
        xmax: xmax,
        ymin: ymin,
        ymax: ymax,
        pts: pts,
        contains: isRect ? rectContains : contains,
        isRect: isRect,
        degenerate: degenerate
    };
};

/**
 * Test if a segment of a points array is bent or straight
 *
 * @param pts Array of [x, y] pairs
 * @param start the index of the proposed start of the straight section
 * @param end the index of the proposed end point
 * @param tolerance the max distance off the line connecting start and end
 *      before the line counts as bent
 * @returns boolean: true means this segment is bent, false means straight
 */
polygon.isSegmentBent = function isSegmentBent(pts, start, end, tolerance) {
    var startPt = pts[start];
    var segment = [pts[end][0] - startPt[0], pts[end][1] - startPt[1]];
    var segmentSquared = dot(segment, segment);
    var segmentLen = Math.sqrt(segmentSquared);
    var unitPerp = [-segment[1] / segmentLen, segment[0] / segmentLen];
    var i;
    var part;
    var partParallel;

    for(i = start + 1; i < end; i++) {
        part = [pts[i][0] - startPt[0], pts[i][1] - startPt[1]];
        partParallel = dot(part, segment);

        if(partParallel < 0 || partParallel > segmentSquared ||
            Math.abs(dot(part, unitPerp)) > tolerance) return true;
    }
    return false;
};

/**
 * Make a filtering polygon, to minimize the number of segments
 *
 * @param pts Array of [x, y] pairs (must start with at least 1 pair)
 * @param tolerance the maximum deviation from straight allowed for
 *      removing points to simplify the polygon
 *
 * @returns Object {addPt, raw, filtered}
 *      addPt is a function(pt: [x, y] pair) to add a raw point and
 *          continue filtering
 *      raw is all the input points
 *      filtered is the resulting filtered Array of [x, y] pairs
 */
polygon.filter = function filter(pts, tolerance) {
    var ptsFiltered = [pts[0]];
    var doneRawIndex = 0;
    var doneFilteredIndex = 0;

    function addPt(pt) {
        pts.push(pt);
        var prevFilterLen = ptsFiltered.length;
        var iLast = doneRawIndex;
        ptsFiltered.splice(doneFilteredIndex + 1);

        for(var i = iLast + 1; i < pts.length; i++) {
            if(i === pts.length - 1 || polygon.isSegmentBent(pts, iLast, i + 1, tolerance)) {
                ptsFiltered.push(pts[i]);
                if(ptsFiltered.length < prevFilterLen - 2) {
                    doneRawIndex = i;
                    doneFilteredIndex = ptsFiltered.length - 1;
                }
                iLast = i;
            }
        }
    }

    if(pts.length > 1) {
        var lastPt = pts.pop();
        addPt(lastPt);
    }

    return {
        addPt: addPt,
        raw: pts,
        filtered: ptsFiltered
    };
};
