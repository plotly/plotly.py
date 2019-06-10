/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var subtypes = require('../scatter/subtypes');
var BADNUM = require('../../constants/numerical').BADNUM;

module.exports = function selectPoints(searchInfo, selectionTester) {
    var cd = searchInfo.cd;
    var xa = searchInfo.xaxis;
    var ya = searchInfo.yaxis;
    var selection = [];
    var trace = cd[0].trace;
    var i;

    if(!subtypes.hasMarkers(trace)) return [];

    if(selectionTester === false) {
        for(i = 0; i < cd.length; i++) {
            cd[i].selected = 0;
        }
    } else {
        for(i = 0; i < cd.length; i++) {
            var di = cd[i];
            var lonlat = di.lonlat;

            if(lonlat[0] !== BADNUM) {
                var lonlat2 = [Lib.modHalf(lonlat[0], 360), lonlat[1]];
                var xy = [xa.c2p(lonlat2), ya.c2p(lonlat2)];

                if(selectionTester.contains(xy, null, i, searchInfo)) {
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
    }

    return selection;
};
