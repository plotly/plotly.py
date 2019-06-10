/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../../plots/cartesian/axes');
var Lib = require('../../lib');

module.exports = function setContours(trace, vals) {
    var contours = trace.contours;

    // check if we need to auto-choose contour levels
    if(trace.autocontour) {
        // N.B. do not try to use coloraxis cmin/cmax,
        // these values here are meant to remain "per-trace" for now
        var zmin = trace.zmin;
        var zmax = trace.zmax;
        if(trace.zauto || zmin === undefined) {
            zmin = Lib.aggNums(Math.min, null, vals);
        }
        if(trace.zauto || zmax === undefined) {
            zmax = Lib.aggNums(Math.max, null, vals);
        }

        var dummyAx = autoContours(zmin, zmax, trace.ncontours);
        contours.size = dummyAx.dtick;
        contours.start = Axes.tickFirst(dummyAx);
        dummyAx.range.reverse();
        contours.end = Axes.tickFirst(dummyAx);

        if(contours.start === zmin) contours.start += contours.size;
        if(contours.end === zmax) contours.end -= contours.size;

        // if you set a small ncontours, *and* the ends are exactly on zmin/zmax
        // there's an edge case where start > end now. Make sure there's at least
        // one meaningful contour, put it midway between the crossed values
        if(contours.start > contours.end) {
            contours.start = contours.end = (contours.start + contours.end) / 2;
        }

        // copy auto-contour info back to the source data.
        // previously we copied the whole contours object back, but that had
        // other info (coloring, showlines) that should be left to supplyDefaults
        if(!trace._input.contours) trace._input.contours = {};
        Lib.extendFlat(trace._input.contours, {
            start: contours.start,
            end: contours.end,
            size: contours.size
        });
        trace._input.autocontour = true;
    } else if(contours.type !== 'constraint') {
        // sanity checks on manually-supplied start/end/size
        var start = contours.start;
        var end = contours.end;
        var inputContours = trace._input.contours;

        if(start > end) {
            contours.start = inputContours.start = end;
            end = contours.end = inputContours.end = start;
            start = contours.start;
        }

        if(!(contours.size > 0)) {
            var sizeOut;
            if(start === end) sizeOut = 1;
            else sizeOut = autoContours(start, end, trace.ncontours).dtick;

            inputContours.size = contours.size = sizeOut;
        }
    }
};


/*
 * autoContours: make a dummy axis object with dtick we can use
 * as contours.size, and if needed we can use Axes.tickFirst
 * with this axis object to calculate the start and end too
 *
 * start: the value to start the contours at
 * end: the value to end at (must be > start)
 * ncontours: max number of contours to make, like roughDTick
 *
 * returns: an axis object
 */
function autoContours(start, end, ncontours) {
    var dummyAx = {
        type: 'linear',
        range: [start, end]
    };

    Axes.autoTicks(
        dummyAx,
        (end - start) / (ncontours || 15)
    );

    return dummyAx;
}
