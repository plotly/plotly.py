/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../lib');
var PlotSchema = require('../plot_api/plot_schema');
var Plots = require('../plots/plots');
var pointsAccessorFunction = require('./helpers').pointsAccessorFunction;

exports.moduleType = 'transform';

exports.name = 'groupby';

exports.attributes = {
    enabled: {
        valType: 'boolean',
        dflt: true,
        role: 'info',
        editType: 'calc',
        description: [
            'Determines whether this group-by transform is enabled or disabled.'
        ].join(' ')
    },
    groups: {
        valType: 'data_array',
        dflt: [],
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the groups in which the trace data will be split.',
            'For example, with `x` set to *[1, 2, 3, 4]* and',
            '`groups` set to *[\'a\', \'b\', \'a\', \'b\']*,',
            'the groupby transform with split in one trace',
            'with `x` [1, 3] and one trace with `x` [2, 4].'
        ].join(' ')
    },
    nameformat: {
        valType: 'string',
        role: 'info',
        editType: 'calc',
        description: [
            'Pattern by which grouped traces are named. If only one trace is present,',
            'defaults to the group name (`"%{group}"`), otherwise defaults to the group name',
            'with trace name (`"%{group} (%{trace})"`). Available escape sequences are `%{group}`, which',
            'inserts the group name, and `%{trace}`, which inserts the trace name. If grouping',
            'GDP data by country when more than one trace is present, for example, the',
            'default "%{group} (%{trace})" would return "Monaco (GDP per capita)".'
        ].join(' ')
    },
    styles: {
        _isLinkedToArray: 'style',
        target: {
            valType: 'string',
            role: 'info',
            editType: 'calc',
            description: [
                'The group value which receives these styles.'
            ].join(' ')
        },
        value: {
            valType: 'any',
            role: 'info',
            dflt: {},
            editType: 'calc',
            description: [
                'Sets each group styles.',
                'For example, with `groups` set to *[\'a\', \'b\', \'a\', \'b\']*',
                'and `styles` set to *[{target: \'a\', value: { marker: { color: \'red\' } }}]',
                'marker points in group *\'a\'* will be drawn in red.'
            ].join(' '),
            _compareAsJSON: true
        },
        editType: 'calc'
    },
    editType: 'calc'
};

/**
 * Supply transform attributes defaults
 *
 * @param {object} transformIn
 *  object linked to trace.transforms[i] with 'type' set to exports.name
 * @param {object} traceOut
 *  the _fullData trace this transform applies to
 * @param {object} layout
 *  the plot's (not-so-full) layout
 * @param {object} traceIn
 *  the input data trace this transform applies to
 *
 * @return {object} transformOut
 *  copy of transformIn that contains attribute defaults
 */
exports.supplyDefaults = function(transformIn, traceOut, layout) {
    var i;
    var transformOut = {};

    function coerce(attr, dflt) {
        return Lib.coerce(transformIn, transformOut, exports.attributes, attr, dflt);
    }

    var enabled = coerce('enabled');

    if(!enabled) return transformOut;

    coerce('groups');
    coerce('nameformat', layout._dataLength > 1 ? '%{group} (%{trace})' : '%{group}');

    var styleIn = transformIn.styles;
    var styleOut = transformOut.styles = [];

    if(styleIn) {
        for(i = 0; i < styleIn.length; i++) {
            var thisStyle = styleOut[i] = {};
            Lib.coerce(styleIn[i], styleOut[i], exports.attributes.styles, 'target');
            var value = Lib.coerce(styleIn[i], styleOut[i], exports.attributes.styles, 'value');

            // so that you can edit value in place and have Plotly.react notice it, or
            // rebuild it every time and have Plotly.react NOT think it changed:
            // use _compareAsJSON to say we should diff the _JSON_value
            if(Lib.isPlainObject(value)) thisStyle.value = Lib.extendDeep({}, value);
            else if(value) delete thisStyle.value;
        }
    }

    return transformOut;
};


/**
 * Apply transform !!!
 *
 * @param {array} data
 *  array of transformed traces (is [fullTrace] upon first transform)
 *
 * @param {object} state
 *  state object which includes:
 *      - transform {object} full transform attributes
 *      - fullTrace {object} full trace object which is being transformed
 *      - fullData {array} full pre-transform(s) data array
 *      - layout {object} the plot's (not-so-full) layout
 *
 * @return {object} newData
 *  array of transformed traces
 */
exports.transform = function(data, state) {
    var newTraces, i, j;
    var newData = [];

    for(i = 0; i < data.length; i++) {
        newTraces = transformOne(data[i], state);

        for(j = 0; j < newTraces.length; j++) {
            newData.push(newTraces[j]);
        }
    }

    return newData;
};

function transformOne(trace, state) {
    var i, j, k, attr, srcArray, groupName, newTrace, transforms, arrayLookup;
    var groupNameObj;

    var opts = state.transform;
    var transformIndex = state.transformIndex;
    var groups = trace.transforms[transformIndex].groups;
    var originalPointsAccessor = pointsAccessorFunction(trace.transforms, opts);

    if(!(Array.isArray(groups)) || groups.length === 0) {
        return [trace];
    }

    var groupNames = Lib.filterUnique(groups);
    var newData = new Array(groupNames.length);
    var len = groups.length;

    var arrayAttrs = PlotSchema.findArrayAttributes(trace);

    var styles = opts.styles || [];
    var styleLookup = {};
    for(i = 0; i < styles.length; i++) {
        styleLookup[styles[i].target] = styles[i].value;
    }

    if(opts.styles) {
        groupNameObj = Lib.keyedContainer(opts, 'styles', 'target', 'value.name');
    }

    // An index to map group name --> expanded trace index
    var indexLookup = {};
    var indexCnts = {};

    for(i = 0; i < groupNames.length; i++) {
        groupName = groupNames[i];
        indexLookup[groupName] = i;
        indexCnts[groupName] = 0;

        // Start with a deep extend that just copies array references.
        newTrace = newData[i] = Lib.extendDeepNoArrays({}, trace);
        newTrace._group = groupName;
        newTrace.transforms[transformIndex]._indexToPoints = {};

        var suppliedName = null;
        if(groupNameObj) {
            suppliedName = groupNameObj.get(groupName);
        }

        if(suppliedName || suppliedName === '') {
            newTrace.name = suppliedName;
        } else {
            newTrace.name = Lib.templateString(opts.nameformat, {
                trace: trace.name,
                group: groupName
            });
        }

        // In order for groups to apply correctly to other transform data (e.g.
        // a filter transform), we have to break the connection and clone the
        // transforms so that each group writes grouped values into a different
        // destination. This function does not break the array reference
        // connection between the split transforms it creates. That's handled in
        // initialize, which creates a new empty array for each arrayAttr.
        transforms = newTrace.transforms;
        newTrace.transforms = [];
        for(j = 0; j < transforms.length; j++) {
            newTrace.transforms[j] = Lib.extendDeepNoArrays({}, transforms[j]);
        }

        // Initialize empty arrays for the arrayAttrs, to be split in the next step
        for(j = 0; j < arrayAttrs.length; j++) {
            Lib.nestedProperty(newTrace, arrayAttrs[j]).set([]);
        }
    }

    // For each array attribute including those nested inside this and other
    // transforms (small note that we technically only need to do this for
    // transforms that have not yet been applied):
    for(k = 0; k < arrayAttrs.length; k++) {
        attr = arrayAttrs[k];

        // Cache all the arrays to which we'll push:
        for(j = 0, arrayLookup = []; j < groupNames.length; j++) {
            arrayLookup[j] = Lib.nestedProperty(newData[j], attr).get();
        }

        // Get the input data:
        srcArray = Lib.nestedProperty(trace, attr).get();

        // Send each data point to the appropriate expanded trace:
        for(j = 0; j < len; j++) {
            // Map group data --> trace index --> array and push data onto it
            arrayLookup[indexLookup[groups[j]]].push(srcArray[j]);
        }
    }

    for(j = 0; j < len; j++) {
        newTrace = newData[indexLookup[groups[j]]];

        var indexToPoints = newTrace.transforms[transformIndex]._indexToPoints;
        indexToPoints[indexCnts[groups[j]]] = originalPointsAccessor(j);
        indexCnts[groups[j]]++;
    }

    for(i = 0; i < groupNames.length; i++) {
        groupName = groupNames[i];
        newTrace = newData[i];

        Plots.clearExpandedTraceDefaultColors(newTrace);

        // there's no need to coerce styleLookup[groupName] here
        // as another round of supplyDefaults is done on the transformed traces
        newTrace = Lib.extendDeepNoArrays(newTrace, styleLookup[groupName] || {});
    }

    return newData;
}
