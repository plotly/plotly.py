/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';


// IMPORTANT - default colors should be in hex for compatibility
exports.defaults = [
    '#1f77b4',  // muted blue
    '#ff7f0e',  // safety orange
    '#2ca02c',  // cooked asparagus green
    '#d62728',  // brick red
    '#9467bd',  // muted purple
    '#8c564b',  // chestnut brown
    '#e377c2',  // raspberry yogurt pink
    '#7f7f7f',  // middle gray
    '#bcbd22',  // curry yellow-green
    '#17becf'   // blue-teal
];

exports.defaultLine = '#444';

exports.lightLine = '#eee';

exports.background = '#fff';

exports.borderLine = '#BEC8D9';

// with axis.color and Color.interp we aren't using lightLine
// itself anymore, instead interpolating between axis.color
// and the background color using tinycolor.mix. lightFraction
// gives back exactly lightLine if the other colors are defaults.
exports.lightFraction = 100 * (0xe - 0x4) / (0xf - 0x4);
