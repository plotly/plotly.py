/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';
module.exports = {
    // some constants to help with marching squares algorithm
    // where does the path start for each index?
    BOTTOMSTART: [1, 9, 13, 104, 713],
    TOPSTART: [4, 6, 7, 104, 713],
    LEFTSTART: [8, 12, 14, 208, 1114],
    RIGHTSTART: [2, 3, 11, 208, 1114],

    // which way [dx,dy] do we leave a given index?
    // saddles are already disambiguated
    NEWDELTA: [
        null, [-1, 0], [0, -1], [-1, 0],
        [1, 0], null, [0, -1], [-1, 0],
        [0, 1], [0, 1], null, [0, 1],
        [1, 0], [1, 0], [0, -1]
    ],

    // for each saddle, the first index here is used
    // for dx||dy<0, the second for dx||dy>0
    CHOOSESADDLE: {
        104: [4, 1],
        208: [2, 8],
        713: [7, 13],
        1114: [11, 14]
    },

    // after one index has been used for a saddle, which do we
    // substitute to be used up later?
    SADDLEREMAINDER: {1: 4, 2: 8, 4: 1, 7: 13, 8: 2, 11: 14, 13: 7, 14: 11},

    // length of a contour, as a multiple of the plot area diagonal, per label
    LABELDISTANCE: 2,

    // number of contour levels after which we start increasing the number of
    // labels we draw. Many contours means they will generally be close
    // together, so it will be harder to follow a long way to find a label
    LABELINCREASE: 10,

    // minimum length of a contour line, as a multiple of the label length,
    // at which we draw *any* labels
    LABELMIN: 3,

    // max number of labels to draw on a single contour path, no matter how long
    LABELMAX: 10,

    // constants for the label position cost function
    LABELOPTIMIZER: {
        // weight given to edge proximity
        EDGECOST: 1,
        // weight given to the angle off horizontal
        ANGLECOST: 1,
        // weight given to distance from already-placed labels
        NEIGHBORCOST: 5,
        // cost multiplier for labels on the same level
        SAMELEVELFACTOR: 10,
        // minimum distance (as a multiple of the label length)
        // for labels on the same level
        SAMELEVELDISTANCE: 5,
        // maximum cost before we won't even place the label
        MAXCOST: 100,
        // number of evenly spaced points to look at in the first
        // iteration of the search
        INITIALSEARCHPOINTS: 10,
        // number of binary search iterations after the initial wide search
        ITERATIONS: 5
    }
};
