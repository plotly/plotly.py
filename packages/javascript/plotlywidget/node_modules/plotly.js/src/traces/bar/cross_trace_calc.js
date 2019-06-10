/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');
var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;
var BADNUM = require('../../constants/numerical').BADNUM;

var Registry = require('../../registry');
var Axes = require('../../plots/cartesian/axes');
var getAxisGroup = require('../../plots/cartesian/axis_ids').getAxisGroup;
var Sieve = require('./sieve.js');

/*
 * Bar chart stacking/grouping positioning and autoscaling calculations
 * for each direction separately calculate the ranges and positions
 * note that this handles histograms too
 * now doing this one subplot at a time
 */

function crossTraceCalc(gd, plotinfo) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    var fullLayout = gd._fullLayout;
    var fullTraces = gd._fullData;
    var calcTraces = gd.calcdata;
    var calcTracesHorz = [];
    var calcTracesVert = [];

    for(var i = 0; i < fullTraces.length; i++) {
        var fullTrace = fullTraces[i];
        if(
            fullTrace.visible === true &&
            Registry.traceIs(fullTrace, 'bar') &&
            fullTrace.xaxis === xa._id &&
            fullTrace.yaxis === ya._id
        ) {
            if(fullTrace.orientation === 'h') {
                calcTracesHorz.push(calcTraces[i]);
            } else {
                calcTracesVert.push(calcTraces[i]);
            }
        }
    }

    var opts = {
        mode: fullLayout.barmode,
        norm: fullLayout.barnorm,
        gap: fullLayout.bargap,
        groupgap: fullLayout.bargroupgap
    };

    setGroupPositions(gd, xa, ya, calcTracesVert, opts);
    setGroupPositions(gd, ya, xa, calcTracesHorz, opts);
}

function setGroupPositions(gd, pa, sa, calcTraces, opts) {
    if(!calcTraces.length) return;

    var excluded;
    var included;
    var i, calcTrace, fullTrace;

    initBase(sa, calcTraces);

    switch(opts.mode) {
        case 'overlay':
            setGroupPositionsInOverlayMode(pa, sa, calcTraces, opts);
            break;

        case 'group':
            // exclude from the group those traces for which the user set an offset
            excluded = [];
            included = [];
            for(i = 0; i < calcTraces.length; i++) {
                calcTrace = calcTraces[i];
                fullTrace = calcTrace[0].trace;

                if(fullTrace.offset === undefined) included.push(calcTrace);
                else excluded.push(calcTrace);
            }

            if(included.length) {
                setGroupPositionsInGroupMode(gd, pa, sa, included, opts);
            }
            if(excluded.length) {
                setGroupPositionsInOverlayMode(pa, sa, excluded, opts);
            }
            break;

        case 'stack':
        case 'relative':
            // exclude from the stack those traces for which the user set a base
            excluded = [];
            included = [];
            for(i = 0; i < calcTraces.length; i++) {
                calcTrace = calcTraces[i];
                fullTrace = calcTrace[0].trace;

                if(fullTrace.base === undefined) included.push(calcTrace);
                else excluded.push(calcTrace);
            }

            if(included.length) {
                setGroupPositionsInStackOrRelativeMode(gd, pa, sa, included, opts);
            }
            if(excluded.length) {
                setGroupPositionsInOverlayMode(pa, sa, excluded, opts);
            }
            break;
    }

    collectExtents(calcTraces, pa);
}

function initBase(sa, calcTraces) {
    var i, j;

    for(i = 0; i < calcTraces.length; i++) {
        var cd = calcTraces[i];
        var trace = cd[0].trace;
        var base = (trace.type === 'funnel') ? trace._base : trace.base;
        var b;

        // not sure if it really makes sense to have dates for bar size data...
        // ideally if we want to make gantt charts or something we'd treat
        // the actual size (trace.x or y) as time delta but base as absolute
        // time. But included here for completeness.
        var scalendar = trace.orientation === 'h' ? trace.xcalendar : trace.ycalendar;

        // 'base' on categorical axes makes no sense
        var d2c = sa.type === 'category' || sa.type === 'multicategory' ?
            function() { return null; } :
            sa.d2c;

        if(isArrayOrTypedArray(base)) {
            for(j = 0; j < Math.min(base.length, cd.length); j++) {
                b = d2c(base[j], 0, scalendar);
                if(isNumeric(b)) {
                    cd[j].b = +b;
                    cd[j].hasB = 1;
                } else cd[j].b = 0;
            }
            for(; j < cd.length; j++) {
                cd[j].b = 0;
            }
        } else {
            b = d2c(base, 0, scalendar);
            var hasBase = isNumeric(b);
            b = hasBase ? b : 0;
            for(j = 0; j < cd.length; j++) {
                cd[j].b = b;
                if(hasBase) cd[j].hasB = 1;
            }
        }
    }
}

function setGroupPositionsInOverlayMode(pa, sa, calcTraces, opts) {
    // update position axis and set bar offsets and widths
    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];

        var sieve = new Sieve([calcTrace], {
            sepNegVal: false,
            overlapNoMerge: !opts.norm
        });

        // set bar offsets and widths, and update position axis
        setOffsetAndWidth(pa, sieve, opts);

        // set bar bases and sizes, and update size axis
        //
        // (note that `setGroupPositionsInOverlayMode` handles the case barnorm
        // is defined, because this function is also invoked for traces that
        // can't be grouped or stacked)
        if(opts.norm) {
            sieveBars(sieve);
            normalizeBars(sa, sieve, opts);
        } else {
            setBaseAndTop(sa, sieve);
        }
    }
}

function setGroupPositionsInGroupMode(gd, pa, sa, calcTraces, opts) {
    var sieve = new Sieve(calcTraces, {
        sepNegVal: false,
        overlapNoMerge: !opts.norm
    });

    // set bar offsets and widths, and update position axis
    setOffsetAndWidthInGroupMode(gd, pa, sieve, opts);

    // relative-stack bars within the same trace that would otherwise
    // be hidden
    unhideBarsWithinTrace(sieve);

    // set bar bases and sizes, and update size axis
    if(opts.norm) {
        sieveBars(sieve);
        normalizeBars(sa, sieve, opts);
    } else {
        setBaseAndTop(sa, sieve);
    }
}

function setGroupPositionsInStackOrRelativeMode(gd, pa, sa, calcTraces, opts) {
    var sieve = new Sieve(calcTraces, {
        sepNegVal: opts.mode === 'relative',
        overlapNoMerge: !(opts.norm || opts.mode === 'stack' || opts.mode === 'relative')
    });

    // set bar offsets and widths, and update position axis
    setOffsetAndWidth(pa, sieve, opts);

    // set bar bases and sizes, and update size axis
    stackBars(sa, sieve, opts);

    // flag the outmost bar (for text display purposes)
    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];

        for(var j = 0; j < calcTrace.length; j++) {
            var bar = calcTrace[j];

            if(bar.s !== BADNUM) {
                var isOutmostBar = ((bar.b + bar.s) === sieve.get(bar.p, bar.s));
                if(isOutmostBar) bar._outmost = true;
            }
        }
    }

    // Note that marking the outmost bars has to be done
    // before `normalizeBars` changes `bar.b` and `bar.s`.
    if(opts.norm) normalizeBars(sa, sieve, opts);
}

function setOffsetAndWidth(pa, sieve, opts) {
    var minDiff = sieve.minDiff;
    var calcTraces = sieve.traces;

    // set bar offsets and widths
    var barGroupWidth = minDiff * (1 - opts.gap);
    var barWidthPlusGap = barGroupWidth;
    var barWidth = barWidthPlusGap * (1 - (opts.groupgap || 0));

    // computer bar group center and bar offset
    var offsetFromCenter = -barWidth / 2;

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var t = calcTrace[0].t;

        // store bar width and offset for this trace
        t.barwidth = barWidth;
        t.poffset = offsetFromCenter;
        t.bargroupwidth = barGroupWidth;
        t.bardelta = minDiff;
    }

    // stack bars that only differ by rounding
    sieve.binWidth = calcTraces[0][0].t.barwidth / 100;

    // if defined, apply trace offset and width
    applyAttributes(sieve);

    // store the bar center in each calcdata item
    setBarCenterAndWidth(pa, sieve);

    // update position axes
    updatePositionAxis(pa, sieve);
}

function setOffsetAndWidthInGroupMode(gd, pa, sieve, opts) {
    var fullLayout = gd._fullLayout;
    var positions = sieve.positions;
    var distinctPositions = sieve.distinctPositions;
    var minDiff = sieve.minDiff;
    var calcTraces = sieve.traces;
    var nTraces = calcTraces.length;

    // if there aren't any overlapping positions,
    // let them have full width even if mode is group
    var overlap = (positions.length !== distinctPositions.length);
    var barGroupWidth = minDiff * (1 - opts.gap);

    var groupId = getAxisGroup(fullLayout, pa._id) + calcTraces[0][0].trace.orientation;
    var alignmentGroups = fullLayout._alignmentOpts[groupId] || {};

    for(var i = 0; i < nTraces; i++) {
        var calcTrace = calcTraces[i];
        var trace = calcTrace[0].trace;

        var alignmentGroupOpts = alignmentGroups[trace.alignmentgroup] || {};
        var nOffsetGroups = Object.keys(alignmentGroupOpts.offsetGroups || {}).length;

        var barWidthPlusGap;
        if(nOffsetGroups) {
            barWidthPlusGap = barGroupWidth / nOffsetGroups;
        } else {
            barWidthPlusGap = overlap ? barGroupWidth / nTraces : barGroupWidth;
        }

        var barWidth = barWidthPlusGap * (1 - (opts.groupgap || 0));

        var offsetFromCenter;
        if(nOffsetGroups) {
            offsetFromCenter = ((2 * trace._offsetIndex + 1 - nOffsetGroups) * barWidthPlusGap - barWidth) / 2;
        } else {
            offsetFromCenter = overlap ?
                ((2 * i + 1 - nTraces) * barWidthPlusGap - barWidth) / 2 :
                -barWidth / 2;
        }

        var t = calcTrace[0].t;
        t.barwidth = barWidth;
        t.poffset = offsetFromCenter;
        t.bargroupwidth = barGroupWidth;
        t.bardelta = minDiff;
    }

    // stack bars that only differ by rounding
    sieve.binWidth = calcTraces[0][0].t.barwidth / 100;

    // if defined, apply trace width
    applyAttributes(sieve);

    // store the bar center in each calcdata item
    setBarCenterAndWidth(pa, sieve);

    // update position axes
    updatePositionAxis(pa, sieve, overlap);
}

function applyAttributes(sieve) {
    var calcTraces = sieve.traces;
    var i, j;

    for(i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var calcTrace0 = calcTrace[0];
        var fullTrace = calcTrace0.trace;
        var t = calcTrace0.t;
        var offset = fullTrace._offset || fullTrace.offset;
        var initialPoffset = t.poffset;
        var newPoffset;

        if(isArrayOrTypedArray(offset)) {
            // if offset is an array, then clone it into t.poffset.
            newPoffset = Array.prototype.slice.call(offset, 0, calcTrace.length);

            // guard against non-numeric items
            for(j = 0; j < newPoffset.length; j++) {
                if(!isNumeric(newPoffset[j])) {
                    newPoffset[j] = initialPoffset;
                }
            }

            // if the length of the array is too short,
            // then extend it with the initial value of t.poffset
            for(j = newPoffset.length; j < calcTrace.length; j++) {
                newPoffset.push(initialPoffset);
            }

            t.poffset = newPoffset;
        } else if(offset !== undefined) {
            t.poffset = offset;
        }

        var width = fullTrace._width || fullTrace.width;
        var initialBarwidth = t.barwidth;

        if(isArrayOrTypedArray(width)) {
            // if width is an array, then clone it into t.barwidth.
            var newBarwidth = Array.prototype.slice.call(width, 0, calcTrace.length);

            // guard against non-numeric items
            for(j = 0; j < newBarwidth.length; j++) {
                if(!isNumeric(newBarwidth[j])) newBarwidth[j] = initialBarwidth;
            }

            // if the length of the array is too short,
            // then extend it with the initial value of t.barwidth
            for(j = newBarwidth.length; j < calcTrace.length; j++) {
                newBarwidth.push(initialBarwidth);
            }

            t.barwidth = newBarwidth;

            // if user didn't set offset,
            // then correct t.poffset to ensure bars remain centered
            if(offset === undefined) {
                newPoffset = [];
                for(j = 0; j < calcTrace.length; j++) {
                    newPoffset.push(
                        initialPoffset + (initialBarwidth - newBarwidth[j]) / 2
                    );
                }
                t.poffset = newPoffset;
            }
        } else if(width !== undefined) {
            t.barwidth = width;

            // if user didn't set offset,
            // then correct t.poffset to ensure bars remain centered
            if(offset === undefined) {
                t.poffset = initialPoffset + (initialBarwidth - width) / 2;
            }
        }
    }
}

function setBarCenterAndWidth(pa, sieve) {
    var calcTraces = sieve.traces;
    var pLetter = getAxisLetter(pa);

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var t = calcTrace[0].t;
        var poffset = t.poffset;
        var poffsetIsArray = Array.isArray(poffset);
        var barwidth = t.barwidth;
        var barwidthIsArray = Array.isArray(barwidth);

        for(var j = 0; j < calcTrace.length; j++) {
            var calcBar = calcTrace[j];

            // store the actual bar width and position, for use by hover
            var width = calcBar.w = barwidthIsArray ? barwidth[j] : barwidth;
            calcBar[pLetter] = calcBar.p + (poffsetIsArray ? poffset[j] : poffset) + width / 2;
        }
    }
}

function updatePositionAxis(pa, sieve, allowMinDtick) {
    var calcTraces = sieve.traces;
    var minDiff = sieve.minDiff;
    var vpad = minDiff / 2;

    Axes.minDtick(pa, sieve.minDiff, sieve.distinctPositions[0], allowMinDtick);

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var calcTrace0 = calcTrace[0];
        var fullTrace = calcTrace0.trace;
        var pts = [];
        var bar, l, r, j;

        for(j = 0; j < calcTrace.length; j++) {
            bar = calcTrace[j];
            l = bar.p - vpad;
            r = bar.p + vpad;
            pts.push(l, r);
        }

        if(fullTrace.width || fullTrace.offset) {
            var t = calcTrace0.t;
            var poffset = t.poffset;
            var barwidth = t.barwidth;
            var poffsetIsArray = Array.isArray(poffset);
            var barwidthIsArray = Array.isArray(barwidth);

            for(j = 0; j < calcTrace.length; j++) {
                bar = calcTrace[j];
                var calcBarOffset = poffsetIsArray ? poffset[j] : poffset;
                var calcBarWidth = barwidthIsArray ? barwidth[j] : barwidth;
                l = bar.p + calcBarOffset;
                r = l + calcBarWidth;
                pts.push(l, r);
            }
        }

        fullTrace._extremes[pa._id] = Axes.findExtremes(pa, pts, {padded: false});
    }
}

// store these bar bases and tops in calcdata
// and make sure the size axis includes zero,
// along with the bases and tops of each bar.
function setBaseAndTop(sa, sieve) {
    var calcTraces = sieve.traces;
    var sLetter = getAxisLetter(sa);

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var fullTrace = calcTrace[0].trace;
        var pts = [];
        var allBaseAboveZero = true;

        for(var j = 0; j < calcTrace.length; j++) {
            var bar = calcTrace[j];
            var base = bar.b;
            var top = base + bar.s;

            bar[sLetter] = top;
            pts.push(top);
            if(bar.hasB) pts.push(base);

            if(!bar.hasB || !(bar.b > 0 && bar.s > 0)) {
                allBaseAboveZero = false;
            }
        }

        fullTrace._extremes[sa._id] = Axes.findExtremes(sa, pts, {
            tozero: !allBaseAboveZero,
            padded: true
        });
    }
}

function stackBars(sa, sieve, opts) {
    var sLetter = getAxisLetter(sa);
    var calcTraces = sieve.traces;
    var calcTrace;
    var fullTrace;
    var isFunnel;
    var i, j;
    var bar;

    for(i = 0; i < calcTraces.length; i++) {
        calcTrace = calcTraces[i];
        fullTrace = calcTrace[0].trace;

        if(fullTrace.type === 'funnel') {
            for(j = 0; j < calcTrace.length; j++) {
                bar = calcTrace[j];

                if(bar.s !== BADNUM) {
                    // create base of funnels
                    sieve.put(bar.p, -0.5 * bar.s);
                }
            }
        }
    }

    for(i = 0; i < calcTraces.length; i++) {
        calcTrace = calcTraces[i];
        fullTrace = calcTrace[0].trace;

        isFunnel = (fullTrace.type === 'funnel');

        var pts = [];

        for(j = 0; j < calcTrace.length; j++) {
            bar = calcTrace[j];

            if(bar.s !== BADNUM) {
                // stack current bar and get previous sum
                var value;
                if(isFunnel) {
                    value = bar.s;
                } else {
                    value = bar.s + bar.b;
                }

                var base = sieve.put(bar.p, value);

                var top = base + value;

                // store the bar base and top in each calcdata item
                bar.b = base;
                bar[sLetter] = top;

                if(!opts.norm) {
                    pts.push(top);
                    if(bar.hasB) {
                        pts.push(base);
                    }
                }
            }
        }

        // if barnorm is set, let normalizeBars update the axis range
        if(!opts.norm) {
            fullTrace._extremes[sa._id] = Axes.findExtremes(sa, pts, {
                // N.B. we don't stack base with 'base',
                // so set tozero:true always!
                tozero: true,
                padded: true
            });
        }
    }
}

function sieveBars(sieve) {
    var calcTraces = sieve.traces;

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];

        for(var j = 0; j < calcTrace.length; j++) {
            var bar = calcTrace[j];

            if(bar.s !== BADNUM) {
                sieve.put(bar.p, bar.b + bar.s);
            }
        }
    }
}

function unhideBarsWithinTrace(sieve) {
    var calcTraces = sieve.traces;

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var fullTrace = calcTrace[0].trace;

        if(fullTrace.base === undefined) {
            var inTraceSieve = new Sieve([calcTrace], {
                sepNegVal: true,
                overlapNoMerge: true
            });

            for(var j = 0; j < calcTrace.length; j++) {
                var bar = calcTrace[j];

                if(bar.p !== BADNUM) {
                    // stack current bar and get previous sum
                    var base = inTraceSieve.put(bar.p, bar.b + bar.s);

                    // if previous sum if non-zero, this means:
                    // multiple bars have same starting point are potentially hidden,
                    // shift them vertically so that all bars are visible by default
                    if(base) bar.b = base;
                }
            }
        }
    }
}

// Note:
//
// normalizeBars requires that either sieveBars or stackBars has been
// previously invoked.
function normalizeBars(sa, sieve, opts) {
    var calcTraces = sieve.traces;
    var sLetter = getAxisLetter(sa);
    var sTop = opts.norm === 'fraction' ? 1 : 100;
    var sTiny = sTop / 1e9; // in case of rounding error in sum
    var sMin = sa.l2c(sa.c2l(0));
    var sMax = opts.mode === 'stack' ? sTop : sMin;

    function needsPadding(v) {
        return (
            isNumeric(sa.c2l(v)) &&
            ((v < sMin - sTiny) || (v > sMax + sTiny) || !isNumeric(sMin))
        );
    }

    for(var i = 0; i < calcTraces.length; i++) {
        var calcTrace = calcTraces[i];
        var fullTrace = calcTrace[0].trace;
        var pts = [];
        var allBaseAboveZero = true;
        var padded = false;

        for(var j = 0; j < calcTrace.length; j++) {
            var bar = calcTrace[j];

            if(bar.s !== BADNUM) {
                var scale = Math.abs(sTop / sieve.get(bar.p, bar.s));
                bar.b *= scale;
                bar.s *= scale;

                var base = bar.b;
                var top = base + bar.s;

                bar[sLetter] = top;
                pts.push(top);
                padded = padded || needsPadding(top);

                if(bar.hasB) {
                    pts.push(base);
                    padded = padded || needsPadding(base);
                }

                if(!bar.hasB || !(bar.b > 0 && bar.s > 0)) {
                    allBaseAboveZero = false;
                }
            }
        }

        fullTrace._extremes[sa._id] = Axes.findExtremes(sa, pts, {
            tozero: !allBaseAboveZero,
            padded: padded
        });
    }
}

// find the full position span of bars at each position
// for use by hover, to ensure labels move in if bars are
// narrower than the space they're in.
// run once per trace group (subplot & direction) and
// the same mapping is attached to all calcdata traces
function collectExtents(calcTraces, pa) {
    var pLetter = getAxisLetter(pa);
    var extents = {};
    var i, j, cd;

    var pMin = Infinity;
    var pMax = -Infinity;

    for(i = 0; i < calcTraces.length; i++) {
        cd = calcTraces[i];
        for(j = 0; j < cd.length; j++) {
            var p = cd[j].p;
            if(isNumeric(p)) {
                pMin = Math.min(pMin, p);
                pMax = Math.max(pMax, p);
            }
        }
    }

    // this is just for positioning of hover labels, and nobody will care if
    // the label is 1px too far out; so round positions to 1/10K in case
    // position values don't exactly match from trace to trace
    var roundFactor = 10000 / (pMax - pMin);
    var round = extents.round = function(p) {
        return String(Math.round(roundFactor * (p - pMin)));
    };

    for(i = 0; i < calcTraces.length; i++) {
        cd = calcTraces[i];
        cd[0].t.extents = extents;

        var poffset = cd[0].t.poffset;
        var poffsetIsArray = Array.isArray(poffset);

        for(j = 0; j < cd.length; j++) {
            var di = cd[j];
            var p0 = di[pLetter] - di.w / 2;

            if(isNumeric(p0)) {
                var p1 = di[pLetter] + di.w / 2;
                var pVal = round(di.p);
                if(extents[pVal]) {
                    extents[pVal] = [Math.min(p0, extents[pVal][0]), Math.max(p1, extents[pVal][1])];
                } else {
                    extents[pVal] = [p0, p1];
                }
            }

            di.p0 = di.p + (poffsetIsArray ? poffset[j] : poffset);
            di.p1 = di.p0 + di.w;
            di.s0 = di.b;
            di.s1 = di.s0 + di.s;
        }
    }
}

function getAxisLetter(ax) {
    return ax._id.charAt(0);
}

module.exports = {
    crossTraceCalc: crossTraceCalc,
    setGroupPositions: setGroupPositions
};
