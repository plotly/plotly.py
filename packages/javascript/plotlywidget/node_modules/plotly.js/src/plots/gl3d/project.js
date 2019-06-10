/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

function xformMatrix(m, v) {
    var out = [0, 0, 0, 0];
    var i, j;

    for(i = 0; i < 4; ++i) {
        for(j = 0; j < 4; ++j) {
            out[j] += m[4 * i + j] * v[i];
        }
    }

    return out;
}

function project(camera, v) {
    var p = xformMatrix(camera.projection,
        xformMatrix(camera.view,
        xformMatrix(camera.model, [v[0], v[1], v[2], 1])));
    return p;
}

module.exports = project;
