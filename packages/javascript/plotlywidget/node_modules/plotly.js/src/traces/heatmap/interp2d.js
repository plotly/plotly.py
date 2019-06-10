/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

var INTERPTHRESHOLD = 1e-2;
var NEIGHBORSHIFTS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

function correctionOvershoot(maxFractionalChange) {
    // start with less overshoot, until we know it's converging,
    // then ramp up the overshoot for faster convergence
    return 0.5 - 0.25 * Math.min(1, maxFractionalChange * 0.5);
}

/*
 * interp2d: Fill in missing data from a 2D array using an iterative
 *   poisson equation solver with zero-derivative BC at edges.
 *   Amazingly, this just amounts to repeatedly averaging all the existing
 *   nearest neighbors, at least if we don't take x/y scaling into account,
 *   which is the right approach here where x and y may not even have the
 *   same units.
 *
 * @param {array of arrays} z
 *      The 2D array to fill in. Will be mutated here. Assumed to already be
 *      cleaned, so all entries are numbers except gaps, which are `undefined`.
 * @param {array of arrays} emptyPoints
 *      Each entry [i, j, neighborCount] for empty points z[i][j] and the number
 *      of neighbors that are *not* missing. Assumed to be sorted from most to
 *      least neighbors, as produced by heatmap/find_empties.
 */
module.exports = function interp2d(z, emptyPoints) {
    var maxFractionalChange = 1;
    var i;

    // one pass to fill in a starting value for all the empties
    iterateInterp2d(z, emptyPoints);

    // we're don't need to iterate lone empties - remove them
    for(i = 0; i < emptyPoints.length; i++) {
        if(emptyPoints[i][2] < 4) break;
    }
    // but don't remove these points from the original array,
    // we'll use them for masking, so make a copy.
    emptyPoints = emptyPoints.slice(i);

    for(i = 0; i < 100 && maxFractionalChange > INTERPTHRESHOLD; i++) {
        maxFractionalChange = iterateInterp2d(z, emptyPoints,
            correctionOvershoot(maxFractionalChange));
    }
    if(maxFractionalChange > INTERPTHRESHOLD) {
        Lib.log('interp2d didn\'t converge quickly', maxFractionalChange);
    }

    return z;
};

function iterateInterp2d(z, emptyPoints, overshoot) {
    var maxFractionalChange = 0;
    var thisPt;
    var i;
    var j;
    var p;
    var q;
    var neighborShift;
    var neighborRow;
    var neighborVal;
    var neighborCount;
    var neighborSum;
    var initialVal;
    var minNeighbor;
    var maxNeighbor;

    for(p = 0; p < emptyPoints.length; p++) {
        thisPt = emptyPoints[p];
        i = thisPt[0];
        j = thisPt[1];
        initialVal = z[i][j];
        neighborSum = 0;
        neighborCount = 0;

        for(q = 0; q < 4; q++) {
            neighborShift = NEIGHBORSHIFTS[q];
            neighborRow = z[i + neighborShift[0]];
            if(!neighborRow) continue;
            neighborVal = neighborRow[j + neighborShift[1]];
            if(neighborVal !== undefined) {
                if(neighborSum === 0) {
                    minNeighbor = maxNeighbor = neighborVal;
                } else {
                    minNeighbor = Math.min(minNeighbor, neighborVal);
                    maxNeighbor = Math.max(maxNeighbor, neighborVal);
                }
                neighborCount++;
                neighborSum += neighborVal;
            }
        }

        if(neighborCount === 0) {
            throw 'iterateInterp2d order is wrong: no defined neighbors';
        }

        // this is the laplace equation interpolation:
        // each point is just the average of its neighbors
        // note that this ignores differential x/y scaling
        // which I think is the right approach, since we
        // don't know what that scaling means
        z[i][j] = neighborSum / neighborCount;

        if(initialVal === undefined) {
            if(neighborCount < 4) maxFractionalChange = 1;
        } else {
            // we can make large empty regions converge faster
            // if we overshoot the change vs the previous value
            z[i][j] = (1 + overshoot) * z[i][j] - overshoot * initialVal;

            if(maxNeighbor > minNeighbor) {
                maxFractionalChange = Math.max(maxFractionalChange,
                    Math.abs(z[i][j] - initialVal) / (maxNeighbor - minNeighbor));
            }
        }
    }

    return maxFractionalChange;
}
