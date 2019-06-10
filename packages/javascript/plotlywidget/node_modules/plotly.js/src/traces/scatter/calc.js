/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');
var Lib = require('../../lib');

var Axes = require('../../plots/cartesian/axes');
var BADNUM = require('../../constants/numerical').BADNUM;

var subTypes = require('./subtypes');
var calcColorscale = require('./colorscale_calc');
var arraysToCalcdata = require('./arrays_to_calcdata');
var calcSelection = require('./calc_selection');

function calc(gd, trace) {
    var fullLayout = gd._fullLayout;
    var xa = Axes.getFromId(gd, trace.xaxis || 'x');
    var ya = Axes.getFromId(gd, trace.yaxis || 'y');
    var x = xa.makeCalcdata(trace, 'x');
    var y = ya.makeCalcdata(trace, 'y');
    var serieslen = trace._length;
    var cd = new Array(serieslen);
    var ids = trace.ids;
    var stackGroupOpts = getStackOpts(trace, fullLayout, xa, ya);
    var interpolateGaps = false;
    var isV, i, j, k, interpolate, vali;

    setFirstScatter(fullLayout, trace);

    var xAttr = 'x';
    var yAttr = 'y';
    var posAttr;
    if(stackGroupOpts) {
        Lib.pushUnique(stackGroupOpts.traceIndices, trace._expandedIndex);
        isV = stackGroupOpts.orientation === 'v';

        // size, like we use for bar
        if(isV) {
            yAttr = 's';
            posAttr = 'x';
        } else {
            xAttr = 's';
            posAttr = 'y';
        }
        interpolate = stackGroupOpts.stackgaps === 'interpolate';
    } else {
        var ppad = calcMarkerSize(trace, serieslen);
        calcAxisExpansion(gd, trace, xa, ya, x, y, ppad);
    }

    for(i = 0; i < serieslen; i++) {
        var cdi = cd[i] = {};
        var xValid = isNumeric(x[i]);
        var yValid = isNumeric(y[i]);
        if(xValid && yValid) {
            cdi[xAttr] = x[i];
            cdi[yAttr] = y[i];
        } else if(stackGroupOpts && (isV ? xValid : yValid)) {
            // if we're stacking we need to hold on to all valid positions
            // even with invalid sizes

            cdi[posAttr] = isV ? x[i] : y[i];
            cdi.gap = true;
            if(interpolate) {
                cdi.s = BADNUM;
                interpolateGaps = true;
            } else {
                cdi.s = 0;
            }
        } else {
            cdi[xAttr] = cdi[yAttr] = BADNUM;
        }

        if(ids) {
            cdi.id = String(ids[i]);
        }
    }

    arraysToCalcdata(cd, trace);
    calcColorscale(gd, trace);
    calcSelection(cd, trace);

    if(stackGroupOpts) {
        // remove bad positions and sort
        // note that original indices get added to cd in arraysToCalcdata
        i = 0;
        while(i < cd.length) {
            if(cd[i][posAttr] === BADNUM) {
                cd.splice(i, 1);
            } else i++;
        }

        Lib.sort(cd, function(a, b) {
            return (a[posAttr] - b[posAttr]) || (a.i - b.i);
        });

        if(interpolateGaps) {
            // first fill the beginning with constant from the first point
            i = 0;
            while(i < cd.length - 1 && cd[i].gap) {
                i++;
            }
            vali = cd[i].s;
            if(!vali) vali = cd[i].s = 0; // in case of no data AT ALL in this trace - use 0
            for(j = 0; j < i; j++) {
                cd[j].s = vali;
            }
            // then fill the end with constant from the last point
            k = cd.length - 1;
            while(k > i && cd[k].gap) {
                k--;
            }
            vali = cd[k].s;
            for(j = cd.length - 1; j > k; j--) {
                cd[j].s = vali;
            }
            // now interpolate internal gaps linearly
            while(i < k) {
                i++;
                if(cd[i].gap) {
                    j = i + 1;
                    while(cd[j].gap) {
                        j++;
                    }
                    var pos0 = cd[i - 1][posAttr];
                    var size0 = cd[i - 1].s;
                    var m = (cd[j].s - size0) / (cd[j][posAttr] - pos0);
                    while(i < j) {
                        cd[i].s = size0 + (cd[i][posAttr] - pos0) * m;
                        i++;
                    }
                }
            }
        }
    }

    return cd;
}

function calcAxisExpansion(gd, trace, xa, ya, x, y, ppad) {
    var serieslen = trace._length;
    var fullLayout = gd._fullLayout;
    var xId = xa._id;
    var yId = ya._id;
    var firstScatter = fullLayout._firstScatter[firstScatterGroup(trace)] === trace.uid;
    var stackOrientation = (getStackOpts(trace, fullLayout, xa, ya) || {}).orientation;
    var fill = trace.fill;

    // cancel minimum tick spacings (only applies to bars and boxes)
    xa._minDtick = 0;
    ya._minDtick = 0;

    // check whether bounds should be tight, padded, extended to zero...
    // most cases both should be padded on both ends, so start with that.
    var xOptions = {padded: true};
    var yOptions = {padded: true};

    if(ppad) {
        xOptions.ppad = yOptions.ppad = ppad;
    }

    // TODO: text size

    var openEnded = serieslen < 2 || (x[0] !== x[serieslen - 1]) || (y[0] !== y[serieslen - 1]);

    if(openEnded && (
        (fill === 'tozerox') ||
        ((fill === 'tonextx') && (firstScatter || stackOrientation === 'h'))
    )) {
        // include zero (tight) and extremes (padded) if fill to zero
        // (unless the shape is closed, then it's just filling the shape regardless)

        xOptions.tozero = true;
    } else if(!(trace.error_y || {}).visible && (
        // if no error bars, markers or text, or fill to y=0 remove x padding

            (fill === 'tonexty' || fill === 'tozeroy') ||
            (!subTypes.hasMarkers(trace) && !subTypes.hasText(trace))
        )) {
        xOptions.padded = false;
        xOptions.ppad = 0;
    }

    if(openEnded && (
        (fill === 'tozeroy') ||
        ((fill === 'tonexty') && (firstScatter || stackOrientation === 'v'))
    )) {
        // now check for y - rather different logic, though still mostly padded both ends
        // include zero (tight) and extremes (padded) if fill to zero
        // (unless the shape is closed, then it's just filling the shape regardless)

        yOptions.tozero = true;
    } else if(fill === 'tonextx' || fill === 'tozerox') {
        // tight y: any x fill

        yOptions.padded = false;
    }

    // N.B. asymmetric splom traces call this with blank {} xa or ya
    if(xId) trace._extremes[xId] = Axes.findExtremes(xa, x, xOptions);
    if(yId) trace._extremes[yId] = Axes.findExtremes(ya, y, yOptions);
}

function calcMarkerSize(trace, serieslen) {
    if(!subTypes.hasMarkers(trace)) return;

    // Treat size like x or y arrays --- Run d2c
    // this needs to go before ppad computation
    var marker = trace.marker;
    var sizeref = 1.6 * (trace.marker.sizeref || 1);
    var markerTrans;

    if(trace.marker.sizemode === 'area') {
        markerTrans = function(v) {
            return Math.max(Math.sqrt((v || 0) / sizeref), 3);
        };
    } else {
        markerTrans = function(v) {
            return Math.max((v || 0) / sizeref, 3);
        };
    }

    if(Lib.isArrayOrTypedArray(marker.size)) {
        // I tried auto-type but category and dates dont make much sense.
        var ax = {type: 'linear'};
        Axes.setConvert(ax);

        var s = ax.makeCalcdata(trace.marker, 'size');

        var sizeOut = new Array(serieslen);
        for(var i = 0; i < serieslen; i++) {
            sizeOut[i] = markerTrans(s[i]);
        }
        return sizeOut;
    } else {
        return markerTrans(marker.size);
    }
}

/**
 * mark the first scatter trace for each subplot
 * note that scatter and scattergl each get their own first trace
 * note also that I'm doing this during calc rather than supplyDefaults
 * so I don't need to worry about transforms, but if we ever do
 * per-trace calc this will get confused.
 */
function setFirstScatter(fullLayout, trace) {
    var group = firstScatterGroup(trace);
    var firstScatter = fullLayout._firstScatter;
    if(!firstScatter[group]) firstScatter[group] = trace.uid;
}

function firstScatterGroup(trace) {
    var stackGroup = trace.stackgroup;
    return trace.xaxis + trace.yaxis + trace.type +
        (stackGroup ? '-' + stackGroup : '');
}

function getStackOpts(trace, fullLayout, xa, ya) {
    var stackGroup = trace.stackgroup;
    if(!stackGroup) return;
    var stackOpts = fullLayout._scatterStackOpts[xa._id + ya._id][stackGroup];
    var stackAx = stackOpts.orientation === 'v' ? ya : xa;
    // Allow stacking only on numeric axes
    // calc is a little late to be figuring this out, but during supplyDefaults
    // we don't know the axis type yet
    if(stackAx.type === 'linear' || stackAx.type === 'log') return stackOpts;
}

module.exports = {
    calc: calc,
    calcMarkerSize: calcMarkerSize,
    calcAxisExpansion: calcAxisExpansion,
    setFirstScatter: setFirstScatter,
    getStackOpts: getStackOpts
};
