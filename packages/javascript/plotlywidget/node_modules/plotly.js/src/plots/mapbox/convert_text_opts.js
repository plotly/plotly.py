/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');

/**
 * Convert plotly.js 'textposition' to mapbox-gl 'anchor' and 'offset'
 * (with the help of the icon size).
 *
 * @param {string} textpostion : plotly.js textposition value
 * @param {number} iconSize : plotly.js icon size (e.g. marker.size for traces)
 *
 * @return {object}
 *      - anchor
 *      - offset
 */
module.exports = function convertTextOpts(textposition, iconSize) {
    var parts = textposition.split(' ');
    var vPos = parts[0];
    var hPos = parts[1];

    // ballpack values
    var factor = Lib.isArrayOrTypedArray(iconSize) ? Lib.mean(iconSize) : iconSize;
    var xInc = 0.5 + (factor / 100);
    var yInc = 1.5 + (factor / 100);

    var anchorVals = ['', ''];
    var offset = [0, 0];

    switch(vPos) {
        case 'top':
            anchorVals[0] = 'top';
            offset[1] = -yInc;
            break;
        case 'bottom':
            anchorVals[0] = 'bottom';
            offset[1] = yInc;
            break;
    }

    switch(hPos) {
        case 'left':
            anchorVals[1] = 'right';
            offset[0] = -xInc;
            break;
        case 'right':
            anchorVals[1] = 'left';
            offset[0] = xInc;
            break;
    }

    // Mapbox text-anchor must be one of:
    //  center, left, right, top, bottom,
    //  top-left, top-right, bottom-left, bottom-right

    var anchor;
    if(anchorVals[0] && anchorVals[1]) anchor = anchorVals.join('-');
    else if(anchorVals[0]) anchor = anchorVals[0];
    else if(anchorVals[1]) anchor = anchorVals[1];
    else anchor = 'center';

    return { anchor: anchor, offset: offset };
};
