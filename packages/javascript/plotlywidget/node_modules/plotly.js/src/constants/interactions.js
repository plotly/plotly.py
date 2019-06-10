/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';


module.exports = {
    /**
     * Timing information for interactive elements
     */
    SHOW_PLACEHOLDER: 100,
    HIDE_PLACEHOLDER: 1000,

    // ms between first mousedown and 2nd mouseup to constitute dblclick...
    // we don't seem to have access to the system setting
    DBLCLICKDELAY: 300,

    // opacity dimming fraction for points that are not in selection
    DESELECTDIM: 0.2
};
