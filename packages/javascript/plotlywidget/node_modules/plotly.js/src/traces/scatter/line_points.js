/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var numConstants = require('../../constants/numerical');
var BADNUM = numConstants.BADNUM;
var LOG_CLIP = numConstants.LOG_CLIP;
var LOG_CLIP_PLUS = LOG_CLIP + 0.5;
var LOG_CLIP_MINUS = LOG_CLIP - 0.5;
var Lib = require('../../lib');
var segmentsIntersect = Lib.segmentsIntersect;
var constrain = Lib.constrain;
var constants = require('./constants');


module.exports = function linePoints(d, opts) {
    var xa = opts.xaxis;
    var ya = opts.yaxis;
    var xLog = xa.type === 'log';
    var yLog = ya.type === 'log';
    var xLen = xa._length;
    var yLen = ya._length;
    var connectGaps = opts.connectGaps;
    var baseTolerance = opts.baseTolerance;
    var shape = opts.shape;
    var linear = shape === 'linear';
    var fill = opts.fill && opts.fill !== 'none';
    var segments = [];
    var minTolerance = constants.minTolerance;
    var len = d.length;
    var pts = new Array(len);
    var pti = 0;

    var i;

    // pt variables are pixel coordinates [x,y] of one point
    // these four are the outputs of clustering on a line
    var clusterStartPt, clusterEndPt, clusterHighPt, clusterLowPt;

    // "this" is the next point we're considering adding to the cluster
    var thisPt;

    // did we encounter the high point first, then a low point, or vice versa?
    var clusterHighFirst;

    // the first two points in the cluster determine its unit vector
    // so the second is always in the "High" direction
    var clusterUnitVector;

    // the pixel delta from clusterStartPt
    var thisVector;

    // val variables are (signed) pixel distances along the cluster vector
    var clusterRefDist, clusterHighVal, clusterLowVal, thisVal;

    // deviation variables are (signed) pixel distances normal to the cluster vector
    var clusterMinDeviation, clusterMaxDeviation, thisDeviation;

    // turn one calcdata point into pixel coordinates
    function getPt(index) {
        var di = d[index];
        if(!di) return false;
        var x = xa.c2p(di.x);
        var y = ya.c2p(di.y);

        // if non-positive log values, set them VERY far off-screen
        // so the line looks essentially straight from the previous point.
        if(x === BADNUM) {
            if(xLog) x = xa.c2p(di.x, true);
            if(x === BADNUM) return false;
            // If BOTH were bad log values, make the line follow a constant
            // exponent rather than a constant slope
            if(yLog && y === BADNUM) {
                x *= Math.abs(xa._m * yLen * (xa._m > 0 ? LOG_CLIP_PLUS : LOG_CLIP_MINUS) /
                    (ya._m * xLen * (ya._m > 0 ? LOG_CLIP_PLUS : LOG_CLIP_MINUS)));
            }
            x *= 1000;
        }
        if(y === BADNUM) {
            if(yLog) y = ya.c2p(di.y, true);
            if(y === BADNUM) return false;
            y *= 1000;
        }
        return [x, y];
    }

    function crossesViewport(xFrac0, yFrac0, xFrac1, yFrac1) {
        var dx = xFrac1 - xFrac0;
        var dy = yFrac1 - yFrac0;
        var dx0 = 0.5 - xFrac0;
        var dy0 = 0.5 - yFrac0;
        var norm2 = dx * dx + dy * dy;
        var dot = dx * dx0 + dy * dy0;
        if(dot > 0 && dot < norm2) {
            var cross = dx0 * dy - dy0 * dx;
            if(cross * cross < norm2) return true;
        }
    }

    var latestXFrac, latestYFrac;
    // if we're off-screen, increase tolerance over baseTolerance
    function getTolerance(pt, nextPt) {
        var xFrac = pt[0] / xLen;
        var yFrac = pt[1] / yLen;
        var offScreenFraction = Math.max(0, -xFrac, xFrac - 1, -yFrac, yFrac - 1);
        if(offScreenFraction && (latestXFrac !== undefined) &&
            crossesViewport(xFrac, yFrac, latestXFrac, latestYFrac)
        ) {
            offScreenFraction = 0;
        }
        if(offScreenFraction && nextPt &&
            crossesViewport(xFrac, yFrac, nextPt[0] / xLen, nextPt[1] / yLen)
        ) {
            offScreenFraction = 0;
        }

        return (1 + constants.toleranceGrowth * offScreenFraction) * baseTolerance;
    }

    function ptDist(pt1, pt2) {
        var dx = pt1[0] - pt2[0];
        var dy = pt1[1] - pt2[1];
        return Math.sqrt(dx * dx + dy * dy);
    }

    // last bit of filtering: clip paths that are VERY far off-screen
    // so we don't get near the browser's hard limit (+/- 2^29 px in Chrome and FF)

    var maxScreensAway = constants.maxScreensAway;

    // find the intersections between the segment from pt1 to pt2
    // and the large rectangle maxScreensAway around the viewport
    // if one of pt1 and pt2 is inside and the other outside, there
    // will be only one intersection.
    // if both are outside there will be 0 or 2 intersections
    // (or 1 if it's right at a corner - we'll treat that like 0)
    // returns an array of intersection pts
    var xEdge0 = -xLen * maxScreensAway;
    var xEdge1 = xLen * (1 + maxScreensAway);
    var yEdge0 = -yLen * maxScreensAway;
    var yEdge1 = yLen * (1 + maxScreensAway);
    var edges = [
        [xEdge0, yEdge0, xEdge1, yEdge0],
        [xEdge1, yEdge0, xEdge1, yEdge1],
        [xEdge1, yEdge1, xEdge0, yEdge1],
        [xEdge0, yEdge1, xEdge0, yEdge0]
    ];
    var xEdge, yEdge, lastXEdge, lastYEdge, lastFarPt, edgePt;

    // for linear line shape, edge intersections should be linearly interpolated
    // spline uses this too, which isn't precisely correct but is actually pretty
    // good, because Catmull-Rom weights far-away points less in creating the curvature
    function getLinearEdgeIntersections(pt1, pt2) {
        var out = [];
        var ptCount = 0;
        for(var i = 0; i < 4; i++) {
            var edge = edges[i];
            var ptInt = segmentsIntersect(
                pt1[0], pt1[1], pt2[0], pt2[1],
                edge[0], edge[1], edge[2], edge[3]
            );
            if(ptInt && (!ptCount ||
                Math.abs(ptInt.x - out[0][0]) > 1 ||
                Math.abs(ptInt.y - out[0][1]) > 1
            )) {
                ptInt = [ptInt.x, ptInt.y];
                // if we have 2 intersections, make sure the closest one to pt1 comes first
                if(ptCount && ptDist(ptInt, pt1) < ptDist(out[0], pt1)) out.unshift(ptInt);
                else out.push(ptInt);
                ptCount++;
            }
        }
        return out;
    }

    function onlyConstrainedPoint(pt) {
        if(pt[0] < xEdge0 || pt[0] > xEdge1 || pt[1] < yEdge0 || pt[1] > yEdge1) {
            return [constrain(pt[0], xEdge0, xEdge1), constrain(pt[1], yEdge0, yEdge1)];
        }
    }

    function sameEdge(pt1, pt2) {
        if(pt1[0] === pt2[0] && (pt1[0] === xEdge0 || pt1[0] === xEdge1)) return true;
        if(pt1[1] === pt2[1] && (pt1[1] === yEdge0 || pt1[1] === yEdge1)) return true;
    }

    // for line shapes hv and vh, movement in the two dimensions is decoupled,
    // so all we need to do is constrain each dimension independently
    function getHVEdgeIntersections(pt1, pt2) {
        var out = [];
        var ptInt1 = onlyConstrainedPoint(pt1);
        var ptInt2 = onlyConstrainedPoint(pt2);
        if(ptInt1 && ptInt2 && sameEdge(ptInt1, ptInt2)) return out;

        if(ptInt1) out.push(ptInt1);
        if(ptInt2) out.push(ptInt2);
        return out;
    }

    // hvh and vhv we sometimes have to move one of the intersection points
    // out BEYOND the clipping rect, by a maximum of a factor of 2, so that
    // the midpoint line is drawn in the right place
    function getABAEdgeIntersections(dim, limit0, limit1) {
        return function(pt1, pt2) {
            var ptInt1 = onlyConstrainedPoint(pt1);
            var ptInt2 = onlyConstrainedPoint(pt2);

            var out = [];
            if(ptInt1 && ptInt2 && sameEdge(ptInt1, ptInt2)) return out;

            if(ptInt1) out.push(ptInt1);
            if(ptInt2) out.push(ptInt2);

            var midShift = 2 * Lib.constrain((pt1[dim] + pt2[dim]) / 2, limit0, limit1) -
                ((ptInt1 || pt1)[dim] + (ptInt2 || pt2)[dim]);
            if(midShift) {
                var ptToAlter;
                if(ptInt1 && ptInt2) {
                    ptToAlter = (midShift > 0 === ptInt1[dim] > ptInt2[dim]) ? ptInt1 : ptInt2;
                } else ptToAlter = ptInt1 || ptInt2;

                ptToAlter[dim] += midShift;
            }

            return out;
        };
    }

    var getEdgeIntersections;
    if(shape === 'linear' || shape === 'spline') {
        getEdgeIntersections = getLinearEdgeIntersections;
    } else if(shape === 'hv' || shape === 'vh') {
        getEdgeIntersections = getHVEdgeIntersections;
    } else if(shape === 'hvh') getEdgeIntersections = getABAEdgeIntersections(0, xEdge0, xEdge1);
    else if(shape === 'vhv') getEdgeIntersections = getABAEdgeIntersections(1, yEdge0, yEdge1);

    // a segment pt1->pt2 entirely outside the nearby region:
    // find the corner it gets closest to touching
    function getClosestCorner(pt1, pt2) {
        var dx = pt2[0] - pt1[0];
        var m = (pt2[1] - pt1[1]) / dx;
        var b = (pt1[1] * pt2[0] - pt2[1] * pt1[0]) / dx;

        if(b > 0) return [m > 0 ? xEdge0 : xEdge1, yEdge1];
        else return [m > 0 ? xEdge1 : xEdge0, yEdge0];
    }

    function updateEdge(pt) {
        var x = pt[0];
        var y = pt[1];
        var xSame = x === pts[pti - 1][0];
        var ySame = y === pts[pti - 1][1];
        // duplicate point?
        if(xSame && ySame) return;
        if(pti > 1) {
            // backtracking along an edge?
            var xSame2 = x === pts[pti - 2][0];
            var ySame2 = y === pts[pti - 2][1];
            if(xSame && (x === xEdge0 || x === xEdge1) && xSame2) {
                if(ySame2) pti--; // backtracking exactly - drop prev pt and don't add
                else pts[pti - 1] = pt; // not exact: replace the prev pt
            } else if(ySame && (y === yEdge0 || y === yEdge1) && ySame2) {
                if(xSame2) pti--;
                else pts[pti - 1] = pt;
            } else pts[pti++] = pt;
        } else pts[pti++] = pt;
    }

    function updateEdgesForReentry(pt) {
        // if we're outside the nearby region and going back in,
        // we may need to loop around a corner point
        if(pts[pti - 1][0] !== pt[0] && pts[pti - 1][1] !== pt[1]) {
            updateEdge([lastXEdge, lastYEdge]);
        }
        updateEdge(pt);
        lastFarPt = null;
        lastXEdge = lastYEdge = 0;
    }

    function addPt(pt) {
        latestXFrac = pt[0] / xLen;
        latestYFrac = pt[1] / yLen;
        // Are we more than maxScreensAway off-screen any direction?
        // if so, clip to this box, but in such a way that on-screen
        // drawing is unchanged
        xEdge = (pt[0] < xEdge0) ? xEdge0 : (pt[0] > xEdge1) ? xEdge1 : 0;
        yEdge = (pt[1] < yEdge0) ? yEdge0 : (pt[1] > yEdge1) ? yEdge1 : 0;
        if(xEdge || yEdge) {
            if(!pti) {
                // to get fills right - if first point is far, push it toward the
                // screen in whichever direction(s) are far

                pts[pti++] = [xEdge || pt[0], yEdge || pt[1]];
            } else if(lastFarPt) {
                // both this point and the last are outside the nearby region
                // check if we're crossing the nearby region
                var intersections = getEdgeIntersections(lastFarPt, pt);
                if(intersections.length > 1) {
                    updateEdgesForReentry(intersections[0]);
                    pts[pti++] = intersections[1];
                }
            } else {
                // we're leaving the nearby region - add the point where we left it

                edgePt = getEdgeIntersections(pts[pti - 1], pt)[0];
                pts[pti++] = edgePt;
            }

            var lastPt = pts[pti - 1];
            if(xEdge && yEdge && (lastPt[0] !== xEdge || lastPt[1] !== yEdge)) {
                // we've gone out beyond a new corner: add the corner too
                // so that the next point will take the right winding
                if(lastFarPt) {
                    if(lastXEdge !== xEdge && lastYEdge !== yEdge) {
                        if(lastXEdge && lastYEdge) {
                            // we've gone around to an opposite corner - we
                            // need to add the correct extra corner
                            // in order to get the right winding
                            updateEdge(getClosestCorner(lastFarPt, pt));
                        } else {
                            // we're coming from a far edge - the extra corner
                            // we need is determined uniquely by the sectors
                            updateEdge([lastXEdge || xEdge, lastYEdge || yEdge]);
                        }
                    } else if(lastXEdge && lastYEdge) {
                        updateEdge([lastXEdge, lastYEdge]);
                    }
                }
                updateEdge([xEdge, yEdge]);
            } else if((lastXEdge - xEdge) && (lastYEdge - yEdge)) {
                // we're coming from an edge or far corner to an edge - again the
                // extra corner we need is uniquely determined by the sectors
                updateEdge([xEdge || lastXEdge, yEdge || lastYEdge]);
            }
            lastFarPt = pt;
            lastXEdge = xEdge;
            lastYEdge = yEdge;
        } else {
            if(lastFarPt) {
                // this point is in range but the previous wasn't: add its entry pt first
                updateEdgesForReentry(getEdgeIntersections(lastFarPt, pt)[0]);
            }

            pts[pti++] = pt;
        }
    }

    // loop over ALL points in this trace
    for(i = 0; i < len; i++) {
        clusterStartPt = getPt(i);
        if(!clusterStartPt) continue;

        pti = 0;
        lastFarPt = null;
        addPt(clusterStartPt);

        // loop over one segment of the trace
        for(i++; i < len; i++) {
            clusterHighPt = getPt(i);
            if(!clusterHighPt) {
                if(connectGaps) continue;
                else break;
            }

            // can't decimate if nonlinear line shape
            // TODO: we *could* decimate [hv]{2,3} shapes if we restricted clusters to horz or vert again
            // but spline would be verrry awkward to decimate
            if(!linear || !opts.simplify) {
                addPt(clusterHighPt);
                continue;
            }

            var nextPt = getPt(i + 1);

            clusterRefDist = ptDist(clusterHighPt, clusterStartPt);

            // #3147 - always include the very first and last points for fills
            if(!(fill && (pti === 0 || pti === len - 1)) &&
                clusterRefDist < getTolerance(clusterHighPt, nextPt) * minTolerance) continue;

            clusterUnitVector = [
                (clusterHighPt[0] - clusterStartPt[0]) / clusterRefDist,
                (clusterHighPt[1] - clusterStartPt[1]) / clusterRefDist
            ];

            clusterLowPt = clusterStartPt;
            clusterHighVal = clusterRefDist;
            clusterLowVal = clusterMinDeviation = clusterMaxDeviation = 0;
            clusterHighFirst = false;
            clusterEndPt = clusterHighPt;

            // loop over one cluster of points that collapse onto one line
            for(i++; i < d.length; i++) {
                thisPt = nextPt;
                nextPt = getPt(i + 1);
                if(!thisPt) {
                    if(connectGaps) continue;
                    else break;
                }
                thisVector = [
                    thisPt[0] - clusterStartPt[0],
                    thisPt[1] - clusterStartPt[1]
                ];
                // cross product (or dot with normal to the cluster vector)
                thisDeviation = thisVector[0] * clusterUnitVector[1] - thisVector[1] * clusterUnitVector[0];
                clusterMinDeviation = Math.min(clusterMinDeviation, thisDeviation);
                clusterMaxDeviation = Math.max(clusterMaxDeviation, thisDeviation);

                if(clusterMaxDeviation - clusterMinDeviation > getTolerance(thisPt, nextPt)) break;

                clusterEndPt = thisPt;
                thisVal = thisVector[0] * clusterUnitVector[0] + thisVector[1] * clusterUnitVector[1];

                if(thisVal > clusterHighVal) {
                    clusterHighVal = thisVal;
                    clusterHighPt = thisPt;
                    clusterHighFirst = false;
                } else if(thisVal < clusterLowVal) {
                    clusterLowVal = thisVal;
                    clusterLowPt = thisPt;
                    clusterHighFirst = true;
                }
            }

            // insert this cluster into pts
            // we've already inserted the start pt, now check if we have high and low pts
            if(clusterHighFirst) {
                addPt(clusterHighPt);
                if(clusterEndPt !== clusterLowPt) addPt(clusterLowPt);
            } else {
                if(clusterLowPt !== clusterStartPt) addPt(clusterLowPt);
                if(clusterEndPt !== clusterHighPt) addPt(clusterHighPt);
            }
            // and finally insert the end pt
            addPt(clusterEndPt);

            // have we reached the end of this segment?
            if(i >= d.length || !thisPt) break;

            // otherwise we have an out-of-cluster point to insert as next clusterStartPt
            addPt(thisPt);
            clusterStartPt = thisPt;
        }

        // to get fills right - repeat what we did at the start
        if(lastFarPt) updateEdge([lastXEdge || lastFarPt[0], lastYEdge || lastFarPt[1]]);

        segments.push(pts.slice(0, pti));
    }

    return segments;
};
