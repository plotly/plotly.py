/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


exports.xmlns = 'http://www.w3.org/2000/xmlns/';
exports.svg = 'http://www.w3.org/2000/svg';
exports.xlink = 'http://www.w3.org/1999/xlink';

// the 'old' d3 quirk got fix in v3.5.7
// https://github.com/mbostock/d3/commit/a6f66e9dd37f764403fc7c1f26be09ab4af24fed
exports.svgAttrs = {
    xmlns: exports.svg,
    'xmlns:xlink': exports.xlink
};
