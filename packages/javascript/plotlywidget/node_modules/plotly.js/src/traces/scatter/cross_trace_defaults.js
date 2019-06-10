/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


// remove opacity for any trace that has a fill or is filled to
module.exports = function crossTraceDefaults(fullData) {
    for(var i = 0; i < fullData.length; i++) {
        var tracei = fullData[i];
        if(tracei.type !== 'scatter') continue;

        var filli = tracei.fill;
        if(filli === 'none' || filli === 'toself') continue;

        tracei.opacity = undefined;

        if(filli === 'tonexty' || filli === 'tonextx') {
            for(var j = i - 1; j >= 0; j--) {
                var tracej = fullData[j];

                if((tracej.type === 'scatter') &&
                        (tracej.xaxis === tracei.xaxis) &&
                        (tracej.yaxis === tracei.yaxis)) {
                    tracej.opacity = undefined;
                    break;
                }
            }
        }
    }
};
