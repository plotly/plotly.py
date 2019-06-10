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

var boxDefaults = require('../box/defaults');
var attributes = require('./attributes');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }
    function coerce2(attr, dflt) {
        return Lib.coerce2(traceIn, traceOut, attributes, attr, dflt);
    }

    boxDefaults.handleSampleDefaults(traceIn, traceOut, coerce, layout);
    if(traceOut.visible === false) return;

    coerce('bandwidth');
    coerce('side');

    var width = coerce('width');
    if(!width) {
        coerce('scalegroup', traceOut.name);
        coerce('scalemode');
    }

    var span = coerce('span');
    var spanmodeDflt;
    if(Array.isArray(span)) spanmodeDflt = 'manual';
    coerce('spanmode', spanmodeDflt);

    var lineColor = coerce('line.color', (traceIn.marker || {}).color || defaultColor);
    var lineWidth = coerce('line.width');
    var fillColor = coerce('fillcolor', Color.addOpacity(traceOut.line.color, 0.5));

    boxDefaults.handlePointsDefaults(traceIn, traceOut, coerce, {prefix: ''});

    var boxWidth = coerce2('box.width');
    var boxFillColor = coerce2('box.fillcolor', fillColor);
    var boxLineColor = coerce2('box.line.color', lineColor);
    var boxLineWidth = coerce2('box.line.width', lineWidth);
    var boxVisible = coerce('box.visible', Boolean(boxWidth || boxFillColor || boxLineColor || boxLineWidth));
    if(!boxVisible) traceOut.box = {visible: false};

    var meanLineColor = coerce2('meanline.color', lineColor);
    var meanLineWidth = coerce2('meanline.width', lineWidth);
    var meanLineVisible = coerce('meanline.visible', Boolean(meanLineColor || meanLineWidth));
    if(!meanLineVisible) traceOut.meanline = {visible: false};
};
