/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var axisIds = require('../../plots/cartesian/axis_ids');

var traceIs = require('../../registry').traceIs;
var handleGroupingDefaults = require('../bar/defaults').handleGroupingDefaults;

var nestedProperty = Lib.nestedProperty;
var getAxisGroup = axisIds.getAxisGroup;

var BINATTRS = [
    {aStr: {x: 'xbins.start', y: 'ybins.start'}, name: 'start'},
    {aStr: {x: 'xbins.end', y: 'ybins.end'}, name: 'end'},
    {aStr: {x: 'xbins.size', y: 'ybins.size'}, name: 'size'},
    {aStr: {x: 'nbinsx', y: 'nbinsy'}, name: 'nbins'}
];

var BINDIRECTIONS = ['x', 'y'];

// handle bin attrs and relink auto-determined values so fullData is complete
module.exports = function crossTraceDefaults(fullData, fullLayout) {
    var allBinOpts = fullLayout._histogramBinOpts = {};
    var histTraces = [];
    var mustMatchTracesLookup = {};
    var otherTracesList = [];

    var traceOut, traces, groupName, binDir;
    var i, j, k;

    function coerce(attr, dflt) {
        return Lib.coerce(traceOut._input, traceOut, traceOut._module.attributes, attr, dflt);
    }

    function orientation2binDir(traceOut) {
        return traceOut.orientation === 'v' ? 'x' : 'y';
    }

    function getAxisType(traceOut, binDir) {
        var ax = axisIds.getFromTrace({_fullLayout: fullLayout}, traceOut, binDir);
        return ax.type;
    }

    function fillBinOpts(traceOut, groupName, binDir) {
        // N.B. group traces that don't have a bingroup with themselves
        var fallbackGroupName = traceOut.uid + '__' + binDir;
        if(!groupName) groupName = fallbackGroupName;

        var axType = getAxisType(traceOut, binDir);
        var calendar = traceOut[binDir + 'calendar'];
        var binOpts = allBinOpts[groupName];
        var needsNewItem = true;

        if(binOpts) {
            if(axType === binOpts.axType && calendar === binOpts.calendar) {
                needsNewItem = false;
                binOpts.traces.push(traceOut);
                binOpts.dirs.push(binDir);
            } else {
                groupName = fallbackGroupName;

                if(axType !== binOpts.axType) {
                    Lib.warn([
                        'Attempted to group the bins of trace', traceOut.index,
                        'set on a', 'type:' + axType, 'axis',
                        'with bins on', 'type:' + binOpts.axType, 'axis.'
                    ].join(' '));
                }
                if(calendar !== binOpts.calendar) {
                    // prohibit bingroup for traces using different calendar,
                    // there's probably a way to make this work, but skip for now
                    Lib.warn([
                        'Attempted to group the bins of trace', traceOut.index,
                        'set with a', calendar, 'calendar',
                        'with bins',
                        (binOpts.calendar ? 'on a ' + binOpts.calendar + ' calendar' : 'w/o a set calendar')
                    ].join(' '));
                }
            }
        }

        if(needsNewItem) {
            allBinOpts[groupName] = {
                traces: [traceOut],
                dirs: [binDir],
                axType: axType,
                calendar: traceOut[binDir + 'calendar'] || ''
            };
        }
        traceOut['_' + binDir + 'bingroup'] = groupName;
    }

    for(i = 0; i < fullData.length; i++) {
        traceOut = fullData[i];

        if(traceIs(traceOut, 'histogram')) {
            histTraces.push(traceOut);

            // TODO: this shouldn't be relinked as it's only used within calc
            // https://github.com/plotly/plotly.js/issues/749
            delete traceOut._xautoBinFinished;
            delete traceOut._yautoBinFinished;

            // N.B. need to coerce *alignmentgroup* before *bingroup*, as traces
            // in same alignmentgroup "have to match"
            if(!traceIs(traceOut, '2dMap')) {
                handleGroupingDefaults(traceOut._input, traceOut, fullLayout, coerce);
            }
        }
    }

    var alignmentOpts = fullLayout._alignmentOpts || {};

    // Look for traces that "have to match", that is:
    // - 1d histogram traces on the same subplot with same orientation under barmode:stack,
    // - 1d histogram traces on the same subplot with same orientation under barmode:group
    // - 1d histogram traces on the same position axis with the same orientation
    //   and the same *alignmentgroup* (coerced under barmode:group)
    // - Once `stackgroup` gets implemented (see https://github.com/plotly/plotly.js/issues/3614),
    //   traces within the same stackgroup will also "have to match"
    for(i = 0; i < histTraces.length; i++) {
        traceOut = histTraces[i];
        groupName = '';

        if(!traceIs(traceOut, '2dMap')) {
            binDir = orientation2binDir(traceOut);

            if(fullLayout.barmode === 'group' && traceOut.alignmentgroup) {
                var pa = traceOut[binDir + 'axis'];
                var aGroupId = getAxisGroup(fullLayout, pa) + traceOut.orientation;
                if((alignmentOpts[aGroupId] || {})[traceOut.alignmentgroup]) {
                    groupName = aGroupId;
                }
            }

            if(!groupName && fullLayout.barmode !== 'overlay') {
                groupName = (
                    getAxisGroup(fullLayout, traceOut.xaxis) +
                    getAxisGroup(fullLayout, traceOut.yaxis) +
                    orientation2binDir(traceOut)
                );
            }
        }

        if(groupName) {
            if(!mustMatchTracesLookup[groupName]) {
                mustMatchTracesLookup[groupName] = [];
            }
            mustMatchTracesLookup[groupName].push(traceOut);
        } else {
            otherTracesList.push(traceOut);
        }
    }

    // Setup binOpts for traces that have to match,
    // if the traces have a valid bingroup, use that
    // if not use axis+binDir groupName
    for(groupName in mustMatchTracesLookup) {
        traces = mustMatchTracesLookup[groupName];

        // no need to 'force' anything when a single
        // trace is detected as "must match"
        if(traces.length === 1) {
            otherTracesList.push(traces[0]);
            continue;
        }

        var binGroupFound = false;
        for(i = 0; i < traces.length; i++) {
            traceOut = traces[i];
            binGroupFound = coerce('bingroup');
            break;
        }

        groupName = binGroupFound || groupName;

        for(i = 0; i < traces.length; i++) {
            traceOut = traces[i];
            var bingroupIn = traceOut._input.bingroup;
            if(bingroupIn && bingroupIn !== groupName) {
                Lib.warn([
                    'Trace', traceOut.index, 'must match',
                    'within bingroup', groupName + '.',
                    'Ignoring its bingroup:', bingroupIn, 'setting.'
                ].join(' '));
            }
            traceOut.bingroup = groupName;

            // N.B. no need to worry about 2dMap case
            // (where both bin direction are set in each trace)
            // as 2dMap trace never "have to match"
            fillBinOpts(traceOut, groupName, orientation2binDir(traceOut));
        }
    }

    // setup binOpts for traces that can but don't have to match,
    // notice that these traces can be matched with traces that have to match
    for(i = 0; i < otherTracesList.length; i++) {
        traceOut = otherTracesList[i];

        var binGroup = coerce('bingroup');

        if(traceIs(traceOut, '2dMap')) {
            for(k = 0; k < 2; k++) {
                binDir = BINDIRECTIONS[k];
                var binGroupInDir = coerce(binDir + 'bingroup',
                    binGroup ? binGroup + '__' + binDir : null
                );
                fillBinOpts(traceOut, binGroupInDir, binDir);
            }
        } else {
            fillBinOpts(traceOut, binGroup, orientation2binDir(traceOut));
        }
    }

    // coerce bin attrs!
    for(groupName in allBinOpts) {
        var binOpts = allBinOpts[groupName];
        traces = binOpts.traces;

        for(j = 0; j < BINATTRS.length; j++) {
            var attrSpec = BINATTRS[j];
            var attr = attrSpec.name;
            var aStr;
            var autoVals;

            // nbins(x|y) is moot if we have a size. This depends on
            // nbins coming after size in binAttrs.
            if(attr === 'nbins' && binOpts.sizeFound) continue;

            for(i = 0; i < traces.length; i++) {
                traceOut = traces[i];
                binDir = binOpts.dirs[i];
                aStr = attrSpec.aStr[binDir];

                if(nestedProperty(traceOut._input, aStr).get() !== undefined) {
                    binOpts[attr] = coerce(aStr);
                    binOpts[attr + 'Found'] = true;
                    break;
                }

                autoVals = (traceOut._autoBin || {})[binDir] || {};
                if(autoVals[attr]) {
                    // if this is the *first* autoval
                    nestedProperty(traceOut, aStr).set(autoVals[attr]);
                }
            }

            // start and end we need to coerce anyway, after having collected the
            // first of each into binOpts, in case a trace wants to restrict its
            // data to a certain range
            if(attr === 'start' || attr === 'end') {
                for(; i < traces.length; i++) {
                    traceOut = traces[i];
                    if(traceOut['_' + binDir + 'bingroup']) {
                        autoVals = (traceOut._autoBin || {})[binDir] || {};
                        coerce(aStr, autoVals[attr]);
                    }
                }
            }

            if(attr === 'nbins' && !binOpts.sizeFound && !binOpts.nbinsFound) {
                traceOut = traces[0];
                binOpts[attr] = coerce(aStr);
            }
        }
    }
};
