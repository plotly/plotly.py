/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');
var handleXYDefaults = require('./xy_defaults');
var handleABDefaults = require('./ab_defaults');
var attributes = require('./attributes');
var colorAttrs = require('../../components/color/attributes');

module.exports = function supplyDefaults(traceIn, traceOut, dfltColor, fullLayout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    traceOut._clipPathId = 'clip' + traceOut.uid + 'carpet';

    var defaultColor = coerce('color', colorAttrs.defaultLine);
    Lib.coerceFont(coerce, 'font');

    coerce('carpet');

    handleABDefaults(traceIn, traceOut, fullLayout, coerce, defaultColor);

    if(!traceOut.a || !traceOut.b) {
        traceOut.visible = false;
        return;
    }

    if(traceOut.a.length < 3) {
        traceOut.aaxis.smoothing = 0;
    }

    if(traceOut.b.length < 3) {
        traceOut.baxis.smoothing = 0;
    }

    // NB: the input is x/y arrays. You should know that the *first* dimension of x and y
    // corresponds to b and the second to a. This sounds backwards but ends up making sense
    // the important part to know is that when you write y[j][i], j goes from 0 to b.length - 1
    // and i goes from 0 to a.length - 1.
    var validData = handleXYDefaults(traceIn, traceOut, coerce);
    if(!validData) {
        traceOut.visible = false;
    }

    if(traceOut._cheater) {
        coerce('cheaterslope');
    }
};
