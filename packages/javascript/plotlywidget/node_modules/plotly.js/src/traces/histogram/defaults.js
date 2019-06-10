/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');
var Color = require('../../components/color');

var handleStyleDefaults = require('../bar/style_defaults');
var attributes = require('./attributes');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var x = coerce('x');
    var y = coerce('y');

    var cumulative = coerce('cumulative.enabled');
    if(cumulative) {
        coerce('cumulative.direction');
        coerce('cumulative.currentbin');
    }

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    var orientation = coerce('orientation', (y && !x) ? 'h' : 'v');
    var sampleLetter = orientation === 'v' ? 'x' : 'y';
    var aggLetter = orientation === 'v' ? 'y' : 'x';

    var len = (x && y) ?
        Math.min(Lib.minRowLength(x) && Lib.minRowLength(y)) :
        Lib.minRowLength(traceOut[sampleLetter] || []);

    if(!len) {
        traceOut.visible = false;
        return;
    }

    traceOut._length = len;

    var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleTraceDefaults');
    handleCalendarDefaults(traceIn, traceOut, ['x', 'y'], layout);

    var hasAggregationData = traceOut[aggLetter];
    if(hasAggregationData) coerce('histfunc');
    coerce('histnorm');

    // Note: bin defaults are now handled in Histogram.crossTraceDefaults
    // autobin(x|y) are only included here to appease Plotly.validate
    coerce('autobin' + sampleLetter);

    handleStyleDefaults(traceIn, traceOut, coerce, defaultColor, layout);

    Lib.coerceSelectionMarkerOpacity(traceOut, coerce);

    var lineColor = (traceOut.marker.line || {}).color;

    // override defaultColor for error bars with defaultLine
    var errorBarsSupplyDefaults = Registry.getComponentMethod('errorbars', 'supplyDefaults');
    errorBarsSupplyDefaults(traceIn, traceOut, lineColor || Color.defaultLine, {axis: 'y'});
    errorBarsSupplyDefaults(traceIn, traceOut, lineColor || Color.defaultLine, {axis: 'x', inherit: 'y'});
};
