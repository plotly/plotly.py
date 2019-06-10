/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var LINKEDFILLS = {tonextx: 1, tonexty: 1, tonext: 1};

module.exports = function linkTraces(gd, plotinfo, cdscatter) {
    var trace, i, group, prevtrace, groupIndex;

    // first sort traces to keep stacks & filled-together groups together
    var groupIndices = {};
    var needsSort = false;
    var prevGroupIndex = -1;
    var nextGroupIndex = 0;
    var prevUnstackedGroupIndex = -1;
    for(i = 0; i < cdscatter.length; i++) {
        trace = cdscatter[i][0].trace;
        group = trace.stackgroup || '';
        if(group) {
            if(group in groupIndices) {
                groupIndex = groupIndices[group];
            } else {
                groupIndex = groupIndices[group] = nextGroupIndex;
                nextGroupIndex++;
            }
        } else if(trace.fill in LINKEDFILLS && prevUnstackedGroupIndex >= 0) {
            groupIndex = prevUnstackedGroupIndex;
        } else {
            groupIndex = prevUnstackedGroupIndex = nextGroupIndex;
            nextGroupIndex++;
        }

        if(groupIndex < prevGroupIndex) needsSort = true;
        trace._groupIndex = prevGroupIndex = groupIndex;
    }

    var cdscatterSorted = cdscatter.slice();
    if(needsSort) {
        cdscatterSorted.sort(function(a, b) {
            var traceA = a[0].trace;
            var traceB = b[0].trace;
            return (traceA._groupIndex - traceB._groupIndex) ||
                (traceA.index - traceB.index);
        });
    }

    // now link traces to each other
    var prevtraces = {};
    for(i = 0; i < cdscatterSorted.length; i++) {
        trace = cdscatterSorted[i][0].trace;
        group = trace.stackgroup || '';

        // Note: The check which ensures all cdscatter here are for the same axis and
        // are either cartesian or scatterternary has been removed. This code assumes
        // the passed scattertraces have been filtered to the proper plot types and
        // the proper subplots.
        if(trace.visible === true) {
            trace._nexttrace = null;

            if(trace.fill in LINKEDFILLS) {
                prevtrace = prevtraces[group];
                trace._prevtrace = prevtrace || null;

                if(prevtrace) {
                    prevtrace._nexttrace = trace;
                }
            }

            trace._ownfill = (trace.fill && (
                trace.fill.substr(0, 6) === 'tozero' ||
                trace.fill === 'toself' ||
                (trace.fill.substr(0, 2) === 'to' && !trace._prevtrace)
            ));

            prevtraces[group] = trace;
        } else {
            trace._prevtrace = trace._nexttrace = trace._ownfill = null;
        }
    }

    return cdscatterSorted;
};
