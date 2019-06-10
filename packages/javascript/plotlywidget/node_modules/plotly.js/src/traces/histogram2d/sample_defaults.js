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

module.exports = function handleSampleDefaults(traceIn, traceOut, coerce, layout) {
    var x = coerce('x');
    var y = coerce('y');
    var xlen = Lib.minRowLength(x);
    var ylen = Lib.minRowLength(y);

    // we could try to accept x0 and dx, etc...
    // but that's a pretty weird use case.
    // for now require both x and y explicitly specified.
    if(!xlen || !ylen) {
        traceOut.visible = false;
        return;
    }

    traceOut._length = Math.min(xlen, ylen);

    var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleTraceDefaults');
    handleCalendarDefaults(traceIn, traceOut, ['x', 'y'], layout);

    // if marker.color is an array, we can use it in aggregation instead of z
    var hasAggregationData = coerce('z') || coerce('marker.color');

    if(hasAggregationData) coerce('histfunc');
    coerce('histnorm');

    // Note: bin defaults are now handled in Histogram2D.crossTraceDefaults
    // autobin(x|y) are only included here to appease Plotly.validate
    coerce('autobinx');
    coerce('autobiny');
};
