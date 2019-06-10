/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var calc = require('./calc');

/*
 * Scatter stacking & normalization calculations
 * runs per subplot, and can handle multiple stacking groups
 */

module.exports = function crossTraceCalc(gd, plotinfo) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;
    var subplot = xa._id + ya._id;

    var subplotStackOpts = gd._fullLayout._scatterStackOpts[subplot];
    if(!subplotStackOpts) return;

    var calcTraces = gd.calcdata;

    var i, j, k, i2, cd, cd0, posj, sumj, norm;
    var groupOpts, interpolate, groupnorm, posAttr, valAttr;
    var hasAnyBlanks;

    for(var stackGroup in subplotStackOpts) {
        groupOpts = subplotStackOpts[stackGroup];
        var indices = groupOpts.traceIndices;

        // can get here with no indices if the stack axis is non-numeric
        if(!indices.length) continue;

        interpolate = groupOpts.stackgaps === 'interpolate';
        groupnorm = groupOpts.groupnorm;
        if(groupOpts.orientation === 'v') {
            posAttr = 'x';
            valAttr = 'y';
        } else {
            posAttr = 'y';
            valAttr = 'x';
        }
        hasAnyBlanks = new Array(indices.length);
        for(i = 0; i < hasAnyBlanks.length; i++) {
            hasAnyBlanks[i] = false;
        }

        // Collect the complete set of all positions across ALL traces.
        // Start with the first trace, then interleave items from later traces
        // as needed.
        // Fill in mising items as we go.
        cd0 = calcTraces[indices[0]];
        var allPositions = new Array(cd0.length);
        for(i = 0; i < cd0.length; i++) {
            allPositions[i] = cd0[i][posAttr];
        }

        for(i = 1; i < indices.length; i++) {
            cd = calcTraces[indices[i]];

            for(j = k = 0; j < cd.length; j++) {
                posj = cd[j][posAttr];
                for(; posj > allPositions[k] && k < allPositions.length; k++) {
                    // the current trace is missing a position from some previous trace(s)
                    insertBlank(cd, j, allPositions[k], i, hasAnyBlanks, interpolate, posAttr);
                    j++;
                }
                if(posj !== allPositions[k]) {
                    // previous trace(s) are missing a position from the current trace
                    for(i2 = 0; i2 < i; i2++) {
                        insertBlank(calcTraces[indices[i2]], k, posj, i2, hasAnyBlanks, interpolate, posAttr);
                    }
                    allPositions.splice(k, 0, posj);
                }
                k++;
            }
            for(; k < allPositions.length; k++) {
                insertBlank(cd, j, allPositions[k], i, hasAnyBlanks, interpolate, posAttr);
                j++;
            }
        }

        var serieslen = allPositions.length;

        // stack (and normalize)!
        for(j = 0; j < cd0.length; j++) {
            sumj = cd0[j][valAttr] = cd0[j].s;
            for(i = 1; i < indices.length; i++) {
                cd = calcTraces[indices[i]];
                cd[0].trace._rawLength = cd[0].trace._length;
                cd[0].trace._length = serieslen;
                sumj += cd[j].s;
                cd[j][valAttr] = sumj;
            }

            if(groupnorm) {
                norm = ((groupnorm === 'fraction') ? sumj : (sumj / 100)) || 1;
                for(i = 0; i < indices.length; i++) {
                    var cdj = calcTraces[indices[i]][j];
                    cdj[valAttr] /= norm;
                    cdj.sNorm = cdj.s / norm;
                }
            }
        }

        // autorange
        for(i = 0; i < indices.length; i++) {
            cd = calcTraces[indices[i]];
            var trace = cd[0].trace;
            var ppad = calc.calcMarkerSize(trace, trace._rawLength);
            var arrayPad = Array.isArray(ppad);
            if((ppad && hasAnyBlanks[i]) || arrayPad) {
                var ppadRaw = ppad;
                ppad = new Array(serieslen);
                for(j = 0; j < serieslen; j++) {
                    ppad[j] = cd[j].gap ? 0 : (arrayPad ? ppadRaw[cd[j].i] : ppadRaw);
                }
            }
            var x = new Array(serieslen);
            var y = new Array(serieslen);
            for(j = 0; j < serieslen; j++) {
                x[j] = cd[j].x;
                y[j] = cd[j].y;
            }
            calc.calcAxisExpansion(gd, trace, xa, ya, x, y, ppad);

            // while we're here (in a loop over all traces in the stack)
            // record the orientation, so hover can find it easily
            cd[0].t.orientation = groupOpts.orientation;
        }
    }
};

function insertBlank(calcTrace, index, position, traceIndex, hasAnyBlanks, interpolate, posAttr) {
    hasAnyBlanks[traceIndex] = true;
    var newEntry = {
        i: null,
        gap: true,
        s: 0
    };
    newEntry[posAttr] = position;
    calcTrace.splice(index, 0, newEntry);
    // Even if we're not interpolating, if one trace has multiple
    // values at the same position and this trace only has one value there,
    // we just duplicate that one value rather than insert a zero.
    // We also make it look like a real point - because it's ambiguous which
    // one really is the real one!
    if(index && position === calcTrace[index - 1][posAttr]) {
        var prevEntry = calcTrace[index - 1];
        newEntry.s = prevEntry.s;
        // TODO is it going to cause any problems to have multiple
        // calcdata points with the same index?
        newEntry.i = prevEntry.i;
        newEntry.gap = prevEntry.gap;
    } else if(interpolate) {
        newEntry.s = getInterp(calcTrace, index, position, posAttr);
    }
    if(!index) {
        // t and trace need to stay on the first cd entry
        calcTrace[0].t = calcTrace[1].t;
        calcTrace[0].trace = calcTrace[1].trace;
        delete calcTrace[1].t;
        delete calcTrace[1].trace;
    }
}

function getInterp(calcTrace, index, position, posAttr) {
    var pt0 = calcTrace[index - 1];
    var pt1 = calcTrace[index + 1];
    if(!pt1) return pt0.s;
    if(!pt0) return pt1.s;
    return pt0.s + (pt1.s - pt0.s) * (position - pt0[posAttr]) / (pt1[posAttr] - pt0[posAttr]);
}
