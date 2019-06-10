/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

/*
 * tiny helper to move the end of the contours a little to prevent
 * losing the last contour to rounding errors
 */
module.exports = function endPlus(contours) {
    return contours.end + contours.size / 1e6;
};
