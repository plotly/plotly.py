/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');

var calcCommon = require('../ohlc/calc').calcCommon;

module.exports = function(gd, trace) {
    var fullLayout = gd._fullLayout;
    var xa = Axes.getFromId(gd, trace.xaxis);
    var ya = Axes.getFromId(gd, trace.yaxis);

    var x = xa.makeCalcdata(trace, 'x');

    var cd = calcCommon(gd, trace, x, ya, ptFunc);

    if(cd.length) {
        Lib.extendFlat(cd[0].t, {
            num: fullLayout._numBoxes,
            dPos: Lib.distinctVals(x).minDiff / 2,
            posLetter: 'x',
            valLetter: 'y',
        });

        fullLayout._numBoxes++;
        return cd;
    } else {
        return [{t: {empty: true}}];
    }
};

function ptFunc(o, h, l, c) {
    return {
        min: l,
        q1: Math.min(o, c),
        med: c,
        q3: Math.max(o, c),
        max: h,
    };
}
