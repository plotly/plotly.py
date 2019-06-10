/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/**
 * Clear responsive handlers (if any).
 *
 * @param {DOM node or object} gd : graph div object
 */
module.exports = function clearResponsive(gd) {
    if(gd._responsiveChartHandler) {
        window.removeEventListener('resize', gd._responsiveChartHandler);
        delete gd._responsiveChartHandler;
    }
};
