/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');
var Color = require('../../components/color');
var handleOHLC = require('../ohlc/ohlc_defaults');
var attributes = require('./attributes');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var len = handleOHLC(traceIn, traceOut, coerce, layout);
    if(!len) {
        traceOut.visible = false;
        return;
    }

    coerce('line.width');

    handleDirection(traceIn, traceOut, coerce, 'increasing');
    handleDirection(traceIn, traceOut, coerce, 'decreasing');

    coerce('text');
    coerce('hovertext');
    coerce('whiskerwidth');

    layout._requestRangeslider[traceOut.xaxis] = true;
};

function handleDirection(traceIn, traceOut, coerce, direction) {
    var lineColor = coerce(direction + '.line.color');
    coerce(direction + '.line.width', traceOut.line.width);
    coerce(direction + '.fillcolor', Color.addOpacity(lineColor, 0.5));
}
