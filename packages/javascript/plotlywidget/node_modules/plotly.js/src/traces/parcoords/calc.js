/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Colorscale = require('../../components/colorscale');
var Lib = require('../../lib');
var wrap = require('../../lib/gup').wrap;

module.exports = function calc(gd, trace) {
    for(var i = 0; i < trace.dimensions.length; i++) {
        trace.dimensions[i].values = convertTypedArray(trace.dimensions[i].values);
    }
    trace.line.color = convertTypedArray(trace.line.color);

    var lineColor;
    var cscale;

    if(Colorscale.hasColorscale(trace, 'line') && Array.isArray(trace.line.color)) {
        lineColor = trace.line.color;
        cscale = Colorscale.extractOpts(trace.line).colorscale;

        Colorscale.calc(gd, trace, {
            vals: lineColor,
            containerStr: 'line',
            cLetter: 'c'
        });
    } else {
        lineColor = constHalf(trace._length);
        cscale = [[0, trace.line.color], [1, trace.line.color]];
    }

    return wrap({lineColor: lineColor, cscale: cscale});
};

function constHalf(len) {
    var out = new Array(len);
    for(var i = 0; i < len; i++) {
        out[i] = 0.5;
    }
    return out;
}

function convertTypedArray(a) {
    return Lib.isTypedArray(a) ? Array.prototype.slice.call(a) : a;
}
