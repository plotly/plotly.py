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
    var i, j;

    if(selectionTester === false) {
        for(i = 0; i < cd.length; i++) {
            for(j = 0; j < (cd[i].pts || []).length; j++) {
                // clear selection
                cd[i].pts[j].selected = 0;
            }
        }
    } else {
        for(i = 0; i < cd.length; i++) {
            for(j = 0; j < (cd[i].pts || []).length; j++) {
                var pt = cd[i].pts[j];
                var x = xa.c2p(pt.x);
                var y = ya.c2p(pt.y);

                if(selectionTester.contains([x, y], null, pt.i, searchInfo)) {
                    selection.push({
                        pointNumber: pt.i,
                        x: xa.c2d(pt.x),
                        y: ya.c2d(pt.y)
                    });
                    pt.selected = 1;
                } else {
                    pt.selected = 0;
                }
            }
        }
    }

    return selection;
};
