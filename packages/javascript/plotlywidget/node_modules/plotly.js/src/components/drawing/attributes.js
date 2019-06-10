/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

exports.dash = {
    valType: 'string',
    // string type usually doesn't take values... this one should really be
    // a special type or at least a special coercion function, from the GUI
    // you only get these values but elsewhere the user can supply a list of
    // dash lengths in px, and it will be honored
    values: ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot'],
    dflt: 'solid',
    role: 'style',
    editType: 'style',
    description: [
        'Sets the dash style of lines. Set to a dash type string',
        '(*solid*, *dot*, *dash*, *longdash*, *dashdot*, or *longdashdot*)',
        'or a dash length list in px (eg *5px,10px,2px,2px*).'
    ].join(' ')
};
