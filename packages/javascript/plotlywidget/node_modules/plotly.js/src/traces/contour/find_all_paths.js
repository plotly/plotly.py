/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var constants = require('./constants');

module.exports = function findAllPaths(pathinfo, xtol, ytol) {
    var cnt,
        startLoc,
        i,
        pi,
        j;

    // Default just passes these values through as they were before:
    xtol = xtol || 0.01;
    ytol = ytol || 0.01;

    for(i = 0; i < pathinfo.length; i++) {
        pi = pathinfo[i];

        for(j = 0; j < pi.starts.length; j++) {
            startLoc = pi.starts[j];
            makePath(pi, startLoc, 'edge', xtol, ytol);
        }

        cnt = 0;
        while(Object.keys(pi.crossings).length && cnt < 10000) {
            cnt++;
            startLoc = Object.keys(pi.crossings)[0].split(',').map(Number);
            makePath(pi, startLoc, undefined, xtol, ytol);
        }
        if(cnt === 10000) Lib.log('Infinite loop in contour?');
    }
};

function equalPts(pt1, pt2, xtol, ytol) {
    return Math.abs(pt1[0] - pt2[0]) < xtol &&
           Math.abs(pt1[1] - pt2[1]) < ytol;
}

// distance in index units - uses the 3rd and 4th items in points
function ptDist(pt1, pt2) {
    var dx = pt1[2] - pt2[2];
    var dy = pt1[3] - pt2[3];
    return Math.sqrt(dx * dx + dy * dy);
}

function makePath(pi, loc, edgeflag, xtol, ytol) {
    var startLocStr = loc.join(',');
    var locStr = startLocStr;
    var mi = pi.crossings[locStr];
    var marchStep = startStep(mi, edgeflag, loc);
    // start by going backward a half step and finding the crossing point
    var pts = [getInterpPx(pi, loc, [-marchStep[0], -marchStep[1]])];
    var startStepStr = marchStep.join(',');
    var m = pi.z.length;
    var n = pi.z[0].length;
    var cnt;

    // now follow the path
    for(cnt = 0; cnt < 10000; cnt++) { // just to avoid infinite loops
        if(mi > 20) {
            mi = constants.CHOOSESADDLE[mi][(marchStep[0] || marchStep[1]) < 0 ? 0 : 1];
            pi.crossings[locStr] = constants.SADDLEREMAINDER[mi];
        } else {
            delete pi.crossings[locStr];
        }

        marchStep = constants.NEWDELTA[mi];
        if(!marchStep) {
            Lib.log('Found bad marching index:', mi, loc, pi.level);
            break;
        }

        // find the crossing a half step forward, and then take the full step
        pts.push(getInterpPx(pi, loc, marchStep));
        loc[0] += marchStep[0];
        loc[1] += marchStep[1];

        // don't include the same point multiple times
        if(equalPts(pts[pts.length - 1], pts[pts.length - 2], xtol, ytol)) pts.pop();
        locStr = loc.join(',');

        var atEdge = (marchStep[0] && (loc[0] < 0 || loc[0] > n - 2)) ||
                (marchStep[1] && (loc[1] < 0 || loc[1] > m - 2));
        var closedLoop = (locStr === startLocStr) && (marchStep.join(',') === startStepStr);

        // have we completed a loop, or reached an edge?
        if((closedLoop) || (edgeflag && atEdge)) break;

        mi = pi.crossings[locStr];
    }

    if(cnt === 10000) {
        Lib.log('Infinite loop in contour?');
    }
    var closedpath = equalPts(pts[0], pts[pts.length - 1], xtol, ytol);
    var totaldist = 0;
    var distThresholdFactor = 0.2 * pi.smoothing;
    var alldists = [];
    var cropstart = 0;
    var distgroup, cnt2, cnt3, newpt, ptcnt, ptavg, thisdist,
        i, j, edgepathi, edgepathj;

    /*
     * Check for points that are too close together (<1/5 the average dist
     * *in grid index units* (important for log axes and nonuniform grids),
     * less if less smoothed) and just take the center (or avg of center 2).
     * This cuts down on funny behavior when a point is very close to a
     * contour level.
     */
    for(cnt = 1; cnt < pts.length; cnt++) {
        thisdist = ptDist(pts[cnt], pts[cnt - 1]);
        totaldist += thisdist;
        alldists.push(thisdist);
    }

    var distThreshold = totaldist / alldists.length * distThresholdFactor;

    function getpt(i) { return pts[i % pts.length]; }

    for(cnt = pts.length - 2; cnt >= cropstart; cnt--) {
        distgroup = alldists[cnt];
        if(distgroup < distThreshold) {
            cnt3 = 0;
            for(cnt2 = cnt - 1; cnt2 >= cropstart; cnt2--) {
                if(distgroup + alldists[cnt2] < distThreshold) {
                    distgroup += alldists[cnt2];
                } else break;
            }

            // closed path with close points wrapping around the boundary?
            if(closedpath && cnt === pts.length - 2) {
                for(cnt3 = 0; cnt3 < cnt2; cnt3++) {
                    if(distgroup + alldists[cnt3] < distThreshold) {
                        distgroup += alldists[cnt3];
                    } else break;
                }
            }
            ptcnt = cnt - cnt2 + cnt3 + 1;
            ptavg = Math.floor((cnt + cnt2 + cnt3 + 2) / 2);

            // either endpoint included: keep the endpoint
            if(!closedpath && cnt === pts.length - 2) newpt = pts[pts.length - 1];
            else if(!closedpath && cnt2 === -1) newpt = pts[0];

            // odd # of points - just take the central one
            else if(ptcnt % 2) newpt = getpt(ptavg);

            // even # of pts - average central two
            else {
                newpt = [(getpt(ptavg)[0] + getpt(ptavg + 1)[0]) / 2,
                    (getpt(ptavg)[1] + getpt(ptavg + 1)[1]) / 2];
            }

            pts.splice(cnt2 + 1, cnt - cnt2 + 1, newpt);
            cnt = cnt2 + 1;
            if(cnt3) cropstart = cnt3;
            if(closedpath) {
                if(cnt === pts.length - 2) pts[cnt3] = pts[pts.length - 1];
                else if(cnt === 0) pts[pts.length - 1] = pts[0];
            }
        }
    }
    pts.splice(0, cropstart);

    // done with the index parts - remove them so path generation works right
    // because it depends on only having [xpx, ypx]
    for(cnt = 0; cnt < pts.length; cnt++) pts[cnt].length = 2;

    // don't return single-point paths (ie all points were the same
    // so they got deleted?)
    if(pts.length < 2) return;
    else if(closedpath) {
        pts.pop();
        pi.paths.push(pts);
    } else {
        if(!edgeflag) {
            Lib.log('Unclosed interior contour?',
                pi.level, startLocStr, pts.join('L'));
        }

        // edge path - does it start where an existing edge path ends, or vice versa?
        var merged = false;
        for(i = 0; i < pi.edgepaths.length; i++) {
            edgepathi = pi.edgepaths[i];
            if(!merged && equalPts(edgepathi[0], pts[pts.length - 1], xtol, ytol)) {
                pts.pop();
                merged = true;

                // now does it ALSO meet the end of another (or the same) path?
                var doublemerged = false;
                for(j = 0; j < pi.edgepaths.length; j++) {
                    edgepathj = pi.edgepaths[j];
                    if(equalPts(edgepathj[edgepathj.length - 1], pts[0], xtol, ytol)) {
                        doublemerged = true;
                        pts.shift();
                        pi.edgepaths.splice(i, 1);
                        if(j === i) {
                            // the path is now closed
                            pi.paths.push(pts.concat(edgepathj));
                        } else {
                            if(j > i) j--;
                            pi.edgepaths[j] = edgepathj.concat(pts, edgepathi);
                        }
                        break;
                    }
                }
                if(!doublemerged) {
                    pi.edgepaths[i] = pts.concat(edgepathi);
                }
            }
        }
        for(i = 0; i < pi.edgepaths.length; i++) {
            if(merged) break;
            edgepathi = pi.edgepaths[i];
            if(equalPts(edgepathi[edgepathi.length - 1], pts[0], xtol, ytol)) {
                pts.shift();
                pi.edgepaths[i] = edgepathi.concat(pts);
                merged = true;
            }
        }

        if(!merged) pi.edgepaths.push(pts);
    }
}

// special function to get the marching step of the
// first point in the path (leading to loc)
function startStep(mi, edgeflag, loc) {
    var dx = 0;
    var dy = 0;
    if(mi > 20 && edgeflag) {
        // these saddles start at +/- x
        if(mi === 208 || mi === 1114) {
            // if we're starting at the left side, we must be going right
            dx = loc[0] === 0 ? 1 : -1;
        } else {
            // if we're starting at the bottom, we must be going up
            dy = loc[1] === 0 ? 1 : -1;
        }
    } else if(constants.BOTTOMSTART.indexOf(mi) !== -1) dy = 1;
    else if(constants.LEFTSTART.indexOf(mi) !== -1) dx = 1;
    else if(constants.TOPSTART.indexOf(mi) !== -1) dy = -1;
    else dx = -1;
    return [dx, dy];
}

/*
 * Find the pixel coordinates of a particular crossing
 *
 * @param {object} pi: the pathinfo object at this level
 * @param {array} loc: the grid index [x, y] of the crossing
 * @param {array} step: the direction [dx, dy] we're moving on the grid
 *
 * @return {array} [xpx, ypx, xi, yi]: the first two are the pixel location,
 *   the next two are the interpolated grid indices, which we use for
 *   distance calculations to delete points that are too close together.
 *   This is important when the grid is nonuniform (and most dramatically when
 *   we're on log axes and include invalid (0 or negative) values.
 *   It's crucial to delete these extra two before turning an array of these
 *   points into a path, because those routines require length-2 points.
 */
function getInterpPx(pi, loc, step) {
    var locx = loc[0] + Math.max(step[0], 0);
    var locy = loc[1] + Math.max(step[1], 0);
    var zxy = pi.z[locy][locx];
    var xa = pi.xaxis;
    var ya = pi.yaxis;

    if(step[1]) {
        var dx = (pi.level - zxy) / (pi.z[locy][locx + 1] - zxy);

        return [xa.c2p((1 - dx) * pi.x[locx] + dx * pi.x[locx + 1], true),
            ya.c2p(pi.y[locy], true),
            locx + dx, locy];
    } else {
        var dy = (pi.level - zxy) / (pi.z[locy + 1][locx] - zxy);
        return [xa.c2p(pi.x[locx], true),
            ya.c2p((1 - dy) * pi.y[locy] + dy * pi.y[locy + 1], true),
            locx, locy + dy];
    }
}
