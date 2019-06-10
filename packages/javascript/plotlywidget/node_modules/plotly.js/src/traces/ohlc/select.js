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
    var i;
    // for (potentially grouped) candlesticks
    var posOffset = cd[0].t.bPos || 0;

    if(selectionTester === false) {
        // clear selection
        for(i = 0; i < cd.length; i++) {
            cd[i].selected = 0;
        }
    } else {
        for(i = 0; i < cd.length; i++) {
            var di = cd[i];

            if(selectionTester.contains([xa.c2p(di.pos + posOffset), ya.c2p(di.yc)], null, di.i, searchInfo)) {
                selection.push({
                    pointNumber: di.i,
                    x: xa.c2d(di.pos),
                    y: ya.c2d(di.yc)
                });
                di.selected = 1;
            } else {
                di.selected = 0;
            }
        }
    }

    return selection;
};
