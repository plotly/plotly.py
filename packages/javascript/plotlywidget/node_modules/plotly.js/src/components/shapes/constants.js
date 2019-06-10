/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


module.exports = {
    segmentRE: /[MLHVQCTSZ][^MLHVQCTSZ]*/g,
    paramRE: /[^\s,]+/g,

    // which numbers in each path segment are x (or y) values
    // drawn is which param is a drawn point, as opposed to a
    // control point (which doesn't count toward autorange.
    // TODO: this means curved paths could extend beyond the
    // autorange bounds. This is a bit tricky to get right
    // unless we revert to bounding boxes, but perhaps there's
    // a calculation we could do...)
    paramIsX: {
        M: {0: true, drawn: 0},
        L: {0: true, drawn: 0},
        H: {0: true, drawn: 0},
        V: {},
        Q: {0: true, 2: true, drawn: 2},
        C: {0: true, 2: true, 4: true, drawn: 4},
        T: {0: true, drawn: 0},
        S: {0: true, 2: true, drawn: 2},
        // A: {0: true, 5: true},
        Z: {}
    },

    paramIsY: {
        M: {1: true, drawn: 1},
        L: {1: true, drawn: 1},
        H: {},
        V: {0: true, drawn: 0},
        Q: {1: true, 3: true, drawn: 3},
        C: {1: true, 3: true, 5: true, drawn: 5},
        T: {1: true, drawn: 1},
        S: {1: true, 3: true, drawn: 5},
        // A: {1: true, 6: true},
        Z: {}
    },

    numParams: {
        M: 2,
        L: 2,
        H: 1,
        V: 1,
        Q: 4,
        C: 6,
        T: 2,
        S: 4,
        // A: 7,
        Z: 0
    }
};
