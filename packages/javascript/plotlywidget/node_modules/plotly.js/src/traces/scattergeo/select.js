/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var subtypes = require('../scatter/subtypes');
var BADNUM = require('../../constants/numerical').BADNUM;

module.exports = function selectPoints(searchInfo, selectionTester) {
    var cd = searchInfo.cd;
    var xa = searchInfo.xaxis;
    var ya = searchInfo.yaxis;
    var selection = [];
    var trace = cd[0].trace;

    var di, lonlat, x, y, i;

    var hasOnlyLines = (!subtypes.hasMarkers(trace) && !subtypes.hasText(trace));
    if(hasOnlyLines) return [];

    if(selectionTester === false) {
        for(i = 0; i < cd.length; i++) {
            cd[i].selected = 0;
        }
    } else {
        for(i = 0; i < cd.length; i++) {
            di = cd[i];
            lonlat = di.lonlat;

            // some projection types can't handle BADNUMs
            if(lonlat[0] === BADNUM) continue;

            x = xa.c2p(lonlat);
            y = ya.c2p(lonlat);

            if(selectionTester.contains([x, y], null, i, searchInfo)) {
                selection.push({
                    pointNumber: i,
                    lon: lonlat[0],
                    lat: lonlat[1]
                });
                di.selected = 1;
            } else {
                di.selected = 0;
            }
        }
    }

    return selection;
};
