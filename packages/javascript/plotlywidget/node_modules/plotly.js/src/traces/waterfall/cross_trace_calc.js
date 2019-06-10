/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var setGroupPositions = require('../bar/cross_trace_calc').setGroupPositions;

module.exports = function crossTraceCalc(gd, plotinfo) {
    var fullLayout = gd._fullLayout;
    var fullData = gd._fullData;
    var calcdata = gd.calcdata;
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;
    var waterfalls = [];
    var waterfallsVert = [];
    var waterfallsHorz = [];
    var cd, i;

    for(i = 0; i < fullData.length; i++) {
        var fullTrace = fullData[i];

        if(
            fullTrace.visible === true &&
            fullTrace.xaxis === xa._id &&
            fullTrace.yaxis === ya._id &&
            fullTrace.type === 'waterfall'
        ) {
            cd = calcdata[i];

            if(fullTrace.orientation === 'h') {
                waterfallsHorz.push(cd);
            } else {
                waterfallsVert.push(cd);
            }

            waterfalls.push(cd);
        }
    }

    var opts = {
        mode: fullLayout.waterfallmode,
        norm: fullLayout.waterfallnorm,
        gap: fullLayout.waterfallgap,
        groupgap: fullLayout.waterfallgroupgap
    };

    setGroupPositions(gd, xa, ya, waterfallsVert, opts);
    setGroupPositions(gd, ya, xa, waterfallsHorz, opts);

    for(i = 0; i < waterfalls.length; i++) {
        cd = waterfalls[i];

        for(var j = 0; j < cd.length; j++) {
            var di = cd[j];

            if(di.isSum === false) {
                di.s0 += (j === 0) ? 0 : cd[j - 1].s;
            }

            if(j + 1 < cd.length) {
                cd[j].nextP0 = cd[j + 1].p0;
                cd[j].nextS0 = cd[j + 1].s0;
            }
        }
    }
};
