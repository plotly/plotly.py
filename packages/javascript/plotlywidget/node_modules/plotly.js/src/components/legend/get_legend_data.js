/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var helpers = require('./helpers');

module.exports = function getLegendData(calcdata, opts) {
    var lgroupToTraces = {};
    var lgroups = [];
    var hasOneNonBlankGroup = false;
    var slicesShown = {};
    var lgroupi = 0;
    var i, j;

    function addOneItem(legendGroup, legendItem) {
        // each '' legend group is treated as a separate group
        if(legendGroup === '' || !helpers.isGrouped(opts)) {
            var uniqueGroup = '~~i' + lgroupi; // TODO: check this against fullData legendgroups?

            lgroups.push(uniqueGroup);
            lgroupToTraces[uniqueGroup] = [[legendItem]];
            lgroupi++;
        } else if(lgroups.indexOf(legendGroup) === -1) {
            lgroups.push(legendGroup);
            hasOneNonBlankGroup = true;
            lgroupToTraces[legendGroup] = [[legendItem]];
        } else lgroupToTraces[legendGroup].push([legendItem]);
    }

    // build an { legendgroup: [cd0, cd0], ... } object
    for(i = 0; i < calcdata.length; i++) {
        var cd = calcdata[i];
        var cd0 = cd[0];
        var trace = cd0.trace;
        var lgroup = trace.legendgroup;

        if(!trace.visible || !trace.showlegend) continue;

        if(Registry.traceIs(trace, 'pie-like')) {
            if(!slicesShown[lgroup]) slicesShown[lgroup] = {};

            for(j = 0; j < cd.length; j++) {
                var labelj = cd[j].label;

                if(!slicesShown[lgroup][labelj]) {
                    addOneItem(lgroup, {
                        label: labelj,
                        color: cd[j].color,
                        i: cd[j].i,
                        trace: trace,
                        pts: cd[j].pts
                    });

                    slicesShown[lgroup][labelj] = true;
                }
            }
        } else addOneItem(lgroup, cd0);
    }

    // won't draw a legend in this case
    if(!lgroups.length) return [];

    // rearrange lgroupToTraces into a d3-friendly array of arrays
    var lgroupsLength = lgroups.length;
    var ltraces;
    var legendData;

    if(hasOneNonBlankGroup && helpers.isGrouped(opts)) {
        legendData = new Array(lgroupsLength);

        for(i = 0; i < lgroupsLength; i++) {
            ltraces = lgroupToTraces[lgroups[i]];
            legendData[i] = helpers.isReversed(opts) ? ltraces.reverse() : ltraces;
        }
    } else {
        // collapse all groups into one if all groups are blank
        legendData = [new Array(lgroupsLength)];

        for(i = 0; i < lgroupsLength; i++) {
            ltraces = lgroupToTraces[lgroups[i]][0];
            legendData[0][helpers.isReversed(opts) ? lgroupsLength - i - 1 : i] = ltraces;
        }
        lgroupsLength = 1;
    }

    // needed in repositionLegend
    opts._lgroupsLength = lgroupsLength;
    return legendData;
};
