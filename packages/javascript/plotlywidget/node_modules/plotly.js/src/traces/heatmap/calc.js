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
var Axes = require('../../plots/cartesian/axes');

var histogram2dCalc = require('../histogram2d/calc');
var colorscaleCalc = require('../../components/colorscale/calc');
var convertColumnData = require('./convert_column_xyz');
var clean2dArray = require('./clean_2d_array');
var interp2d = require('./interp2d');
var findEmpties = require('./find_empties');
var makeBoundArray = require('./make_bound_array');

module.exports = function calc(gd, trace) {
    // prepare the raw data
    // run makeCalcdata on x and y even for heatmaps, in case of category mappings
    var xa = Axes.getFromId(gd, trace.xaxis || 'x');
    var ya = Axes.getFromId(gd, trace.yaxis || 'y');
    var isContour = Registry.traceIs(trace, 'contour');
    var isHist = Registry.traceIs(trace, 'histogram');
    var isGL2D = Registry.traceIs(trace, 'gl2d');
    var zsmooth = isContour ? 'best' : trace.zsmooth;
    var x;
    var x0;
    var dx;
    var y;
    var y0;
    var dy;
    var z;
    var i;
    var binned;

    // cancel minimum tick spacings (only applies to bars and boxes)
    xa._minDtick = 0;
    ya._minDtick = 0;

    if(isHist) {
        binned = histogram2dCalc(gd, trace);
        x = binned.x;
        x0 = binned.x0;
        dx = binned.dx;
        y = binned.y;
        y0 = binned.y0;
        dy = binned.dy;
        z = binned.z;
    } else {
        var zIn = trace.z;
        if(Lib.isArray1D(zIn)) {
            convertColumnData(trace, xa, ya, 'x', 'y', ['z']);
            x = trace._x;
            y = trace._y;
            zIn = trace._z;
        } else {
            x = trace._x = trace.x ? xa.makeCalcdata(trace, 'x') : [];
            y = trace._y = trace.y ? ya.makeCalcdata(trace, 'y') : [];
        }

        x0 = trace.x0;
        dx = trace.dx;
        y0 = trace.y0;
        dy = trace.dy;

        z = clean2dArray(zIn, trace, xa, ya);

        if(isContour || trace.connectgaps) {
            trace._emptypoints = findEmpties(z);
            interp2d(z, trace._emptypoints);
        }
    }

    function noZsmooth(msg) {
        zsmooth = trace._input.zsmooth = trace.zsmooth = false;
        Lib.warn('cannot use zsmooth: "fast": ' + msg);
    }

    // check whether we really can smooth (ie all boxes are about the same size)
    if(zsmooth === 'fast') {
        if(xa.type === 'log' || ya.type === 'log') {
            noZsmooth('log axis found');
        } else if(!isHist) {
            if(x.length) {
                var avgdx = (x[x.length - 1] - x[0]) / (x.length - 1);
                var maxErrX = Math.abs(avgdx / 100);
                for(i = 0; i < x.length - 1; i++) {
                    if(Math.abs(x[i + 1] - x[i] - avgdx) > maxErrX) {
                        noZsmooth('x scale is not linear');
                        break;
                    }
                }
            }
            if(y.length && zsmooth === 'fast') {
                var avgdy = (y[y.length - 1] - y[0]) / (y.length - 1);
                var maxErrY = Math.abs(avgdy / 100);
                for(i = 0; i < y.length - 1; i++) {
                    if(Math.abs(y[i + 1] - y[i] - avgdy) > maxErrY) {
                        noZsmooth('y scale is not linear');
                        break;
                    }
                }
            }
        }
    }

    // create arrays of brick boundaries, to be used by autorange and heatmap.plot
    var xlen = Lib.maxRowLength(z);
    var xIn = trace.xtype === 'scaled' ? '' : x;
    var xArray = makeBoundArray(trace, xIn, x0, dx, xlen, xa);
    var yIn = trace.ytype === 'scaled' ? '' : y;
    var yArray = makeBoundArray(trace, yIn, y0, dy, z.length, ya);

    // handled in gl2d convert step
    if(!isGL2D) {
        trace._extremes[xa._id] = Axes.findExtremes(xa, xArray);
        trace._extremes[ya._id] = Axes.findExtremes(ya, yArray);
    }

    var cd0 = {
        x: xArray,
        y: yArray,
        z: z,
        text: trace._text || trace.text,
        hovertext: trace._hovertext || trace.hovertext
    };

    if(xIn && xIn.length === xArray.length - 1) cd0.xCenter = xIn;
    if(yIn && yIn.length === yArray.length - 1) cd0.yCenter = yIn;

    if(isHist) {
        cd0.xRanges = binned.xRanges;
        cd0.yRanges = binned.yRanges;
        cd0.pts = binned.pts;
    }

    if(!isContour) {
        colorscaleCalc(gd, trace, {vals: z, cLetter: 'z'});
    }

    if(isContour && trace.contours && trace.contours.coloring === 'heatmap') {
        var dummyTrace = {
            type: trace.type === 'contour' ? 'heatmap' : 'histogram2d',
            xcalendar: trace.xcalendar,
            ycalendar: trace.ycalendar
        };
        cd0.xfill = makeBoundArray(dummyTrace, xIn, x0, dx, xlen, xa);
        cd0.yfill = makeBoundArray(dummyTrace, yIn, y0, dy, z.length, ya);
    }

    return [cd0];
};
