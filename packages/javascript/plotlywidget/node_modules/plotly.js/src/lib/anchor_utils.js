/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


/**
 * Determine the position anchor property of x/y xanchor/yanchor components.
 *
 * - values < 1/3 align the low side at that fraction,
 * - values [1/3, 2/3] align the center at that fraction,
 * - values > 2/3 align the right at that fraction.
 */


exports.isLeftAnchor = function isLeftAnchor(opts) {
    return (
      opts.xanchor === 'left' ||
      (opts.xanchor === 'auto' && opts.x <= 1 / 3)
    );
};

exports.isCenterAnchor = function isCenterAnchor(opts) {
    return (
        opts.xanchor === 'center' ||
        (opts.xanchor === 'auto' && opts.x > 1 / 3 && opts.x < 2 / 3)
    );
};

exports.isRightAnchor = function isRightAnchor(opts) {
    return (
      opts.xanchor === 'right' ||
      (opts.xanchor === 'auto' && opts.x >= 2 / 3)
    );
};

exports.isTopAnchor = function isTopAnchor(opts) {
    return (
        opts.yanchor === 'top' ||
        (opts.yanchor === 'auto' && opts.y >= 2 / 3)
    );
};

exports.isMiddleAnchor = function isMiddleAnchor(opts) {
    return (
        opts.yanchor === 'middle' ||
        (opts.yanchor === 'auto' && opts.y > 1 / 3 && opts.y < 2 / 3)
    );
};

exports.isBottomAnchor = function isBottomAnchor(opts) {
    return (
      opts.yanchor === 'bottom' ||
      (opts.yanchor === 'auto' && opts.y <= 1 / 3)
    );
};
