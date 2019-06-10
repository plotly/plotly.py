/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var constants = require('./constants');

// Calculate all the marching indices, for ALL levels at once.
// since we want to be exhaustive we'll check for contour crossings
// at every intersection, rather than just following a path
// TODO: shorten the inner loop to only the relevant levels
module.exports = function makeCrossings(pathinfo) {
    var z = pathinfo[0].z;
    var m = z.length;
    var n = z[0].length; // we already made sure z isn't ragged in interp2d
    var twoWide = m === 2 || n === 2;
    var xi;
    var yi;
    var startIndices;
    var ystartIndices;
    var label;
    var corners;
    var mi;
    var pi;
    var i;

    for(yi = 0; yi < m - 1; yi++) {
        ystartIndices = [];
        if(yi === 0) ystartIndices = ystartIndices.concat(constants.BOTTOMSTART);
        if(yi === m - 2) ystartIndices = ystartIndices.concat(constants.TOPSTART);

        for(xi = 0; xi < n - 1; xi++) {
            startIndices = ystartIndices.slice();
            if(xi === 0) startIndices = startIndices.concat(constants.LEFTSTART);
            if(xi === n - 2) startIndices = startIndices.concat(constants.RIGHTSTART);

            label = xi + ',' + yi;
            corners = [[z[yi][xi], z[yi][xi + 1]],
                       [z[yi + 1][xi], z[yi + 1][xi + 1]]];
            for(i = 0; i < pathinfo.length; i++) {
                pi = pathinfo[i];
                mi = getMarchingIndex(pi.level, corners);
                if(!mi) continue;

                pi.crossings[label] = mi;
                if(startIndices.indexOf(mi) !== -1) {
                    pi.starts.push([xi, yi]);
                    if(twoWide && startIndices.indexOf(mi,
                            startIndices.indexOf(mi) + 1) !== -1) {
                        // the same square has starts from opposite sides
                        // it's not possible to have starts on opposite edges
                        // of a corner, only a start and an end...
                        // but if the array is only two points wide (either way)
                        // you can have starts on opposite sides.
                        pi.starts.push([xi, yi]);
                    }
                }
            }
        }
    }
};

// modified marching squares algorithm,
// so we disambiguate the saddle points from the start
// and we ignore the cases with no crossings
// the index I'm using is based on:
// http://en.wikipedia.org/wiki/Marching_squares
// except that the saddles bifurcate and I represent them
// as the decimal combination of the two appropriate
// non-saddle indices
function getMarchingIndex(val, corners) {
    var mi = (corners[0][0] > val ? 0 : 1) +
             (corners[0][1] > val ? 0 : 2) +
             (corners[1][1] > val ? 0 : 4) +
             (corners[1][0] > val ? 0 : 8);
    if(mi === 5 || mi === 10) {
        var avg = (corners[0][0] + corners[0][1] +
                   corners[1][0] + corners[1][1]) / 4;
        // two peaks with a big valley
        if(val > avg) return (mi === 5) ? 713 : 1114;
        // two valleys with a big ridge
        return (mi === 5) ? 104 : 208;
    }
    return (mi === 15) ? 0 : mi;
}
