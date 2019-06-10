/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var perStackAttrs = ['orientation', 'groupnorm', 'stackgaps'];

module.exports = function handleStackDefaults(traceIn, traceOut, layout, coerce) {
    var stackOpts = layout._scatterStackOpts;

    var stackGroup = coerce('stackgroup');
    if(stackGroup) {
        // use independent stacking options per subplot
        var subplot = traceOut.xaxis + traceOut.yaxis;
        var subplotStackOpts = stackOpts[subplot];
        if(!subplotStackOpts) subplotStackOpts = stackOpts[subplot] = {};

        var groupOpts = subplotStackOpts[stackGroup];
        var firstTrace = false;
        if(groupOpts) {
            groupOpts.traces.push(traceOut);
        } else {
            groupOpts = subplotStackOpts[stackGroup] = {
                // keep track of trace indices for use during stacking calculations
                // this will be filled in during `calc` and used during `crossTraceCalc`
                // so it's OK if we don't recreate it during a non-calc edit
                traceIndices: [],
                // Hold on to the whole set of prior traces
                // First one is most important, so we can clear defaults
                // there if we find explicit values only in later traces.
                // We're only going to *use* the values stored in groupOpts,
                // but for the editor and validate we want things self-consistent
                // The full set of traces is used only to fix `fill` default if
                // we find `orientation: 'h'` beyond the first trace
                traces: [traceOut]
            };
            firstTrace = true;
        }
        // TODO: how is this going to work with groupby transforms?
        // in principle it should be OK I guess, as long as explicit group styles
        // don't override explicit base-trace styles?

        var dflts = {
            orientation: (traceOut.x && !traceOut.y) ? 'h' : 'v'
        };

        for(var i = 0; i < perStackAttrs.length; i++) {
            var attr = perStackAttrs[i];
            var attrFound = attr + 'Found';
            if(!groupOpts[attrFound]) {
                var traceHasAttr = traceIn[attr] !== undefined;
                var isOrientation = attr === 'orientation';
                if(traceHasAttr || firstTrace) {
                    groupOpts[attr] = coerce(attr, dflts[attr]);

                    if(isOrientation) {
                        groupOpts.fillDflt = groupOpts[attr] === 'h' ?
                            'tonextx' : 'tonexty';
                    }

                    if(traceHasAttr) {
                        // Note: this will show a value here even if it's invalid
                        // in which case it will revert to default.
                        groupOpts[attrFound] = true;

                        // Note: only one trace in the stack will get a _fullData
                        // entry for a given stack-wide attribute. If no traces
                        // (or the first trace) specify that attribute, the
                        // first trace will get it. If the first trace does NOT
                        // specify it but some later trace does, then it gets
                        // removed from the first trace and only included in the
                        // one that specified it. This is mostly important for
                        // editors (that want to see the full values to know
                        // what settings are available) and Plotly.react diffing.
                        // Editors may want to use fullLayout._scatterStackOpts
                        // directly and make these settings available from all
                        // traces in the stack... then set the new value into
                        // the first trace, and clear all later traces.
                        if(!firstTrace) {
                            delete groupOpts.traces[0][attr];

                            // orientation can affect default fill of previous traces
                            if(isOrientation) {
                                for(var j = 0; j < groupOpts.traces.length - 1; j++) {
                                    var trace2 = groupOpts.traces[j];
                                    if(trace2._input.fill !== trace2.fill) {
                                        trace2.fill = groupOpts.fillDflt;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return groupOpts;
    }
};
