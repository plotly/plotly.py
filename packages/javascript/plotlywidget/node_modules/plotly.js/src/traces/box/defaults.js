/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Registry = require('../../registry');
var Color = require('../../components/color');
var handleGroupingDefaults = require('../bar/defaults').handleGroupingDefaults;
var attributes = require('./attributes');

function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    handleSampleDefaults(traceIn, traceOut, coerce, layout);
    if(traceOut.visible === false) return;

    coerce('line.color', (traceIn.marker || {}).color || defaultColor);
    coerce('line.width');
    coerce('fillcolor', Color.addOpacity(traceOut.line.color, 0.5));

    coerce('whiskerwidth');
    coerce('boxmean');
    coerce('width');

    var notched = coerce('notched', traceIn.notchwidth !== undefined);
    if(notched) coerce('notchwidth');

    handlePointsDefaults(traceIn, traceOut, coerce, {prefix: 'box'});
}

function handleSampleDefaults(traceIn, traceOut, coerce, layout) {
    var y = coerce('y');
    var x = coerce('x');
    var hasX = x && x.length;

    var defaultOrientation, len;

    if(y && y.length) {
        defaultOrientation = 'v';
        if(hasX) {
            len = Math.min(Lib.minRowLength(x), Lib.minRowLength(y));
        } else {
            coerce('x0');
            len = Lib.minRowLength(y);
        }
    } else if(hasX) {
        defaultOrientation = 'h';
        coerce('y0');
        len = Lib.minRowLength(x);
    } else {
        traceOut.visible = false;
        return;
    }
    traceOut._length = len;

    var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleTraceDefaults');
    handleCalendarDefaults(traceIn, traceOut, ['x', 'y'], layout);

    coerce('orientation', defaultOrientation);
}

function handlePointsDefaults(traceIn, traceOut, coerce, opts) {
    var prefix = opts.prefix;

    var outlierColorDflt = Lib.coerce2(traceIn, traceOut, attributes, 'marker.outliercolor');
    var lineoutliercolor = coerce('marker.line.outliercolor');

    var points = coerce(
        prefix + 'points',
        (outlierColorDflt || lineoutliercolor) ? 'suspectedoutliers' : undefined
    );

    if(points) {
        coerce('jitter', points === 'all' ? 0.3 : 0);
        coerce('pointpos', points === 'all' ? -1.5 : 0);

        coerce('marker.symbol');
        coerce('marker.opacity');
        coerce('marker.size');
        coerce('marker.color', traceOut.line.color);
        coerce('marker.line.color');
        coerce('marker.line.width');

        if(points === 'suspectedoutliers') {
            coerce('marker.line.outliercolor', traceOut.marker.color);
            coerce('marker.line.outlierwidth');
        }

        coerce('selected.marker.color');
        coerce('unselected.marker.color');
        coerce('selected.marker.size');
        coerce('unselected.marker.size');

        coerce('text');
        coerce('hovertext');
    } else {
        delete traceOut.marker;
    }

    var hoveron = coerce('hoveron');
    if(hoveron === 'all' || hoveron.indexOf('points') !== -1) {
        coerce('hovertemplate');
    }

    Lib.coerceSelectionMarkerOpacity(traceOut, coerce);
}

function crossTraceDefaults(fullData, fullLayout) {
    var traceIn, traceOut;

    function coerce(attr) {
        return Lib.coerce(traceOut._input, traceOut, attributes, attr);
    }

    for(var i = 0; i < fullData.length; i++) {
        traceOut = fullData[i];
        var traceType = traceOut.type;

        if(traceType === 'box' || traceType === 'violin') {
            traceIn = traceOut._input;
            if(fullLayout[traceType + 'mode'] === 'group') {
                handleGroupingDefaults(traceIn, traceOut, fullLayout, coerce);
            }
        }
    }
}

module.exports = {
    supplyDefaults: supplyDefaults,
    crossTraceDefaults: crossTraceDefaults,

    handleSampleDefaults: handleSampleDefaults,
    handlePointsDefaults: handlePointsDefaults
};
