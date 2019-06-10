/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

// fraction of some size to get to a named position
module.exports = {
    // from bottom left: this is the origin of our paper-reference
    // positioning system
    FROM_BL: {
        left: 0,
        center: 0.5,
        right: 1,
        bottom: 0,
        middle: 0.5,
        top: 1
    },
    // from top left: this is the screen pixel positioning origin
    FROM_TL: {
        left: 0,
        center: 0.5,
        right: 1,
        bottom: 1,
        middle: 0.5,
        top: 0
    },
    // from bottom right: sometimes you just need the opposite of ^^
    FROM_BR: {
        left: 1,
        center: 0.5,
        right: 0,
        bottom: 0,
        middle: 0.5,
        top: 1
    },
    // multiple of fontSize to get the vertical offset between lines
    LINE_SPACING: 1.3,

    // multiple of fontSize to shift from the baseline
    // to the cap (captical letter) line
    // (to use when we don't calculate this shift from Drawing.bBox)
    // This is an approximation since in reality cap height can differ
    // from font to font. However, according to Wikipedia
    //   an "average" font might have a cap height of 70% of the em
    // https://en.wikipedia.org/wiki/Em_(typography)#History
    CAP_SHIFT: 0.70,

    // half the cap height (distance between baseline and cap line)
    // of an "average" font (for more info see above).
    MID_SHIFT: 0.35,

    OPPOSITE_SIDE: {
        left: 'right',
        right: 'left',
        top: 'bottom',
        bottom: 'top'
    }
};
