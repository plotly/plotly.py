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

module.exports = function calc(gd) {
    var calcdata = gd.calcdata;
    var fullLayout = gd._fullLayout;

    function makeCoerceHoverInfo(trace) {
        return function(val) {
            return Lib.coerceHoverinfo({hoverinfo: val}, {_module: trace._module}, fullLayout);
        };
    }

    for(var i = 0; i < calcdata.length; i++) {
        var cd = calcdata[i];
        var trace = cd[0].trace;

        // don't include hover calc fields for pie traces
        // as calcdata items might be sorted by value and
        // won't match the data array order.
        if(Registry.traceIs(trace, 'pie-like')) continue;

        var fillFn = Registry.traceIs(trace, '2dMap') ? paste : Lib.fillArray;

        fillFn(trace.hoverinfo, cd, 'hi', makeCoerceHoverInfo(trace));

        if(trace.hovertemplate) fillFn(trace.hovertemplate, cd, 'ht');

        if(!trace.hoverlabel) continue;

        fillFn(trace.hoverlabel.bgcolor, cd, 'hbg');
        fillFn(trace.hoverlabel.bordercolor, cd, 'hbc');
        fillFn(trace.hoverlabel.font.size, cd, 'hts');
        fillFn(trace.hoverlabel.font.color, cd, 'htc');
        fillFn(trace.hoverlabel.font.family, cd, 'htf');
        fillFn(trace.hoverlabel.namelength, cd, 'hnl');
        fillFn(trace.hoverlabel.align, cd, 'hta');
    }
};

function paste(traceAttr, cd, cdAttr, fn) {
    fn = fn || Lib.identity;

    if(Array.isArray(traceAttr)) {
        cd[0][cdAttr] = fn(traceAttr);
    }
}
