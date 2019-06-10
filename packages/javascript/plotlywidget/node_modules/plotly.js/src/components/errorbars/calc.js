/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');

var Registry = require('../../registry');
var Axes = require('../../plots/cartesian/axes');
var Lib = require('../../lib');

var makeComputeError = require('./compute_error');

module.exports = function calc(gd) {
    var calcdata = gd.calcdata;

    for(var i = 0; i < calcdata.length; i++) {
        var calcTrace = calcdata[i];
        var trace = calcTrace[0].trace;

        if(trace.visible === true && Registry.traceIs(trace, 'errorBarsOK')) {
            var xa = Axes.getFromId(gd, trace.xaxis);
            var ya = Axes.getFromId(gd, trace.yaxis);
            calcOneAxis(calcTrace, trace, xa, 'x');
            calcOneAxis(calcTrace, trace, ya, 'y');
        }
    }
};

function calcOneAxis(calcTrace, trace, axis, coord) {
    var opts = trace['error_' + coord] || {};
    var isVisible = (opts.visible && ['linear', 'log'].indexOf(axis.type) !== -1);
    var vals = [];

    if(!isVisible) return;

    var computeError = makeComputeError(opts);

    for(var i = 0; i < calcTrace.length; i++) {
        var calcPt = calcTrace[i];

        var iIn = calcPt.i;

        // for types that don't include `i` in each calcdata point
        if(iIn === undefined) iIn = i;

        // for stacked area inserted points
        // TODO: errorbars have been tested cursorily with stacked area,
        // but not thoroughly. It's not even really clear what you want to do:
        // Should it just be calculated based on that trace's size data?
        // Should you add errors from below in quadrature?
        // And what about normalization, where in principle the errors shrink
        // again when you get up to the top end?
        // One option would be to forbid errorbars with stacking until we
        // decide how to handle these questions.
        else if(iIn === null) continue;

        var calcCoord = calcPt[coord];

        if(!isNumeric(axis.c2l(calcCoord))) continue;

        var errors = computeError(calcCoord, iIn);
        if(isNumeric(errors[0]) && isNumeric(errors[1])) {
            var shoe = calcPt[coord + 's'] = calcCoord - errors[0];
            var hat = calcPt[coord + 'h'] = calcCoord + errors[1];
            vals.push(shoe, hat);
        }
    }

    var axId = axis._id;
    var baseExtremes = trace._extremes[axId];
    var extremes = Axes.findExtremes(
        axis,
        vals,
        Lib.extendFlat({tozero: baseExtremes.opts.tozero}, {padded: true})
    );
    baseExtremes.min = baseExtremes.min.concat(extremes.min);
    baseExtremes.max = baseExtremes.max.concat(extremes.max);
}
