/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../../plots/cartesian/axes');
var isArray1D = require('../../lib').isArray1D;
var cheaterBasis = require('./cheater_basis');
var arrayMinmax = require('./array_minmax');
var calcGridlines = require('./calc_gridlines');
var calcLabels = require('./calc_labels');
var calcClipPath = require('./calc_clippath');
var clean2dArray = require('../heatmap/clean_2d_array');
var smoothFill2dArray = require('./smooth_fill_2d_array');
var convertColumnData = require('../heatmap/convert_column_xyz');
var setConvert = require('./set_convert');

module.exports = function calc(gd, trace) {
    var xa = Axes.getFromId(gd, trace.xaxis);
    var ya = Axes.getFromId(gd, trace.yaxis);
    var aax = trace.aaxis;
    var bax = trace.baxis;

    var x = trace.x;
    var y = trace.y;
    var cols = [];
    if(x && isArray1D(x)) cols.push('x');
    if(y && isArray1D(y)) cols.push('y');

    if(cols.length) {
        convertColumnData(trace, aax, bax, 'a', 'b', cols);
    }

    var a = trace._a = trace._a || trace.a;
    var b = trace._b = trace._b || trace.b;
    x = trace._x || trace.x;
    y = trace._y || trace.y;

    var t = {};

    if(trace._cheater) {
        var avals = aax.cheatertype === 'index' ? a.length : a;
        var bvals = bax.cheatertype === 'index' ? b.length : b;
        x = cheaterBasis(avals, bvals, trace.cheaterslope);
    }

    trace._x = x = clean2dArray(x);
    trace._y = y = clean2dArray(y);

    // Fill in any undefined values with elliptic smoothing. This doesn't take
    // into account the spacing of the values. That is, the derivatives should
    // be modified to use a and b values. It's not that hard, but this is already
    // moderate overkill for just filling in missing values.
    smoothFill2dArray(x, a, b);
    smoothFill2dArray(y, a, b);

    setConvert(trace);

    // create conversion functions that depend on the data
    trace.setScale();

    // This is a rather expensive scan. Nothing guarantees monotonicity,
    // so we need to scan through all data to get proper ranges:
    var xrange = arrayMinmax(x);
    var yrange = arrayMinmax(y);

    var dx = 0.5 * (xrange[1] - xrange[0]);
    var xc = 0.5 * (xrange[1] + xrange[0]);

    var dy = 0.5 * (yrange[1] - yrange[0]);
    var yc = 0.5 * (yrange[1] + yrange[0]);

    // Expand the axes to fit the plot, except just grow it by a factor of 1.3
    // because the labels should be taken into account except that's difficult
    // hence 1.3.
    var grow = 1.3;
    xrange = [xc - dx * grow, xc + dx * grow];
    yrange = [yc - dy * grow, yc + dy * grow];

    trace._extremes[xa._id] = Axes.findExtremes(xa, xrange, {padded: true});
    trace._extremes[ya._id] = Axes.findExtremes(ya, yrange, {padded: true});

    // Enumerate the gridlines, both major and minor, and store them on the trace
    // object:
    calcGridlines(trace, 'a', 'b');
    calcGridlines(trace, 'b', 'a');

    // Calculate the text labels for each major gridline and store them on the
    // trace object:
    calcLabels(trace, aax);
    calcLabels(trace, bax);

    // Tabulate points for the four segments that bound the axes so that we can
    // map to pixel coordinates in the plot function and create a clip rect:
    t.clipsegments = calcClipPath(trace._xctrl, trace._yctrl, aax, bax);

    t.x = x;
    t.y = y;
    t.a = a;
    t.b = b;

    return [t];
};
