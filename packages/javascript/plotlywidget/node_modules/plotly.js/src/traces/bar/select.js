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
    var trace = cd[0].trace;
    var isFunnel = (trace.type === 'funnel');
    var isHorizontal = (trace.orientation === 'h');
    var selection = [];
    var i;

    if(selectionTester === false) {
        // clear selection
        for(i = 0; i < cd.length; i++) {
            cd[i].selected = 0;
        }
    } else {
        for(i = 0; i < cd.length; i++) {
            var di = cd[i];
            var ct = 'ct' in di ? di.ct : getCentroid(di, xa, ya, isHorizontal, isFunnel);

            if(selectionTester.contains(ct, false, i, searchInfo)) {
                selection.push({
                    pointNumber: i,
                    x: xa.c2d(di.x),
                    y: ya.c2d(di.y)
                });
                di.selected = 1;
            } else {
                di.selected = 0;
            }
        }
    }

    return selection;
};

function getCentroid(d, xa, ya, isHorizontal, isFunnel) {
    var x0 = xa.c2p(isHorizontal ? d.s0 : d.p0, true);
    var x1 = xa.c2p(isHorizontal ? d.s1 : d.p1, true);
    var y0 = ya.c2p(isHorizontal ? d.p0 : d.s0, true);
    var y1 = ya.c2p(isHorizontal ? d.p1 : d.s1, true);

    if(isFunnel) {
        return [(x0 + x1) / 2, (y0 + y1) / 2];
    } else {
        if(isHorizontal) {
            return [x1, (y0 + y1) / 2];
        } else {
            return [(x0 + x1) / 2, y1];
        }
    }
}
