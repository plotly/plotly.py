/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function mapPathinfo(pathinfo, map) {
    var i, j, k, pi, pedgepaths, ppaths, pedgepath, ppath, path;

    for(i = 0; i < pathinfo.length; i++) {
        pi = pathinfo[i];
        pedgepaths = pi.pedgepaths = [];
        ppaths = pi.ppaths = [];
        for(j = 0; j < pi.edgepaths.length; j++) {
            path = pi.edgepaths[j];
            pedgepath = [];
            for(k = 0; k < path.length; k++) {
                pedgepath[k] = map(path[k]);
            }
            pedgepaths.push(pedgepath);
        }
        for(j = 0; j < pi.paths.length; j++) {
            path = pi.paths[j];
            ppath = [];
            for(k = 0; k < path.length; k++) {
                ppath[k] = map(path[k]);
            }
            ppaths.push(ppath);
        }
    }
};
