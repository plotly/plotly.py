/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function selectPoints(searchInfo, selectionTester) {
    var cd = searchInfo.cd;
    var xa = searchInfo.xaxis;
    var ya = searchInfo.yaxis;
    var selection = [];

    var i, di, ct, x, y;

    if(selectionTester === false) {
        for(i = 0; i < cd.length; i++) {
            cd[i].selected = 0;
        }
    } else {
        for(i = 0; i < cd.length; i++) {
            di = cd[i];
            ct = di.ct;

            if(!ct) continue;

            x = xa.c2p(ct);
            y = ya.c2p(ct);

            if(selectionTester.contains([x, y], null, i, searchInfo)) {
                selection.push({
                    pointNumber: i,
                    lon: ct[0],
                    lat: ct[1]
                });
                di.selected = 1;
            } else {
                di.selected = 0;
            }
        }
    }

    return selection;
};
