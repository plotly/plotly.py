/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');


// set cursors pointing toward the closest corner/side,
// to indicate alignment
// x and y are 0-1, fractions of the plot area
var cursorset = [
    ['sw-resize', 's-resize', 'se-resize'],
    ['w-resize', 'move', 'e-resize'],
    ['nw-resize', 'n-resize', 'ne-resize']
];

module.exports = function getCursor(x, y, xanchor, yanchor) {
    if(xanchor === 'left') x = 0;
    else if(xanchor === 'center') x = 1;
    else if(xanchor === 'right') x = 2;
    else x = Lib.constrain(Math.floor(x * 3), 0, 2);

    if(yanchor === 'bottom') y = 0;
    else if(yanchor === 'middle') y = 1;
    else if(yanchor === 'top') y = 2;
    else y = Lib.constrain(Math.floor(y * 3), 0, 2);

    return cursorset[y][x];
};
