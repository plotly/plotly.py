/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var Lib = require('../../lib');
var Drawing = require('../../components/drawing');

// constants for dynamic jitter (ie less jitter for sparser points)
var JITTERCOUNT = 5; // points either side of this to include
var JITTERSPREAD = 0.01; // fraction of IQR to count as "dense"

function plot(gd, plotinfo, cdbox, boxLayer) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    Lib.makeTraceGroups(boxLayer, cdbox, 'trace boxes').each(function(cd) {
        var plotGroup = d3.select(this);
        var cd0 = cd[0];
        var t = cd0.t;
        var trace = cd0.trace;
        if(!plotinfo.isRangePlot) cd0.node3 = plotGroup;

        // whisker width
        t.wdPos = t.bdPos * trace.whiskerwidth;

        if(trace.visible !== true || t.empty) {
            plotGroup.remove();
            return;
        }

        var posAxis, valAxis;

        if(trace.orientation === 'h') {
            posAxis = ya;
            valAxis = xa;
        } else {
            posAxis = xa;
            valAxis = ya;
        }

        plotBoxAndWhiskers(plotGroup, {pos: posAxis, val: valAxis}, trace, t);
        plotPoints(plotGroup, {x: xa, y: ya}, trace, t);
        plotBoxMean(plotGroup, {pos: posAxis, val: valAxis}, trace, t);
    });
}

function plotBoxAndWhiskers(sel, axes, trace, t) {
    var posAxis = axes.pos;
    var valAxis = axes.val;
    var bPos = t.bPos;
    var wdPos = t.wdPos || 0;
    var bPosPxOffset = t.bPosPxOffset || 0;
    var whiskerWidth = trace.whiskerwidth || 0;
    var notched = trace.notched || false;
    var nw = notched ? 1 - 2 * trace.notchwidth : 1;

    // to support for one-sided box
    var bdPos0;
    var bdPos1;
    if(Array.isArray(t.bdPos)) {
        bdPos0 = t.bdPos[0];
        bdPos1 = t.bdPos[1];
    } else {
        bdPos0 = t.bdPos;
        bdPos1 = t.bdPos;
    }

    var paths = sel.selectAll('path.box').data((
        trace.type !== 'violin' ||
        trace.box.visible
    ) ? Lib.identity : []);

    paths.enter().append('path')
        .style('vector-effect', 'non-scaling-stroke')
        .attr('class', 'box');

    paths.exit().remove();

    paths.each(function(d) {
        if(d.empty) return 'M0,0Z';

        var pos = d.pos;
        var posc = posAxis.c2p(pos + bPos, true) + bPosPxOffset;
        var pos0 = posAxis.c2p(pos + bPos - bdPos0, true) + bPosPxOffset;
        var pos1 = posAxis.c2p(pos + bPos + bdPos1, true) + bPosPxOffset;
        var posw0 = posAxis.c2p(pos + bPos - wdPos, true) + bPosPxOffset;
        var posw1 = posAxis.c2p(pos + bPos + wdPos, true) + bPosPxOffset;
        var posm0 = posAxis.c2p(pos + bPos - bdPos0 * nw, true) + bPosPxOffset;
        var posm1 = posAxis.c2p(pos + bPos + bdPos1 * nw, true) + bPosPxOffset;
        var q1 = valAxis.c2p(d.q1, true);
        var q3 = valAxis.c2p(d.q3, true);
        // make sure median isn't identical to either of the
        // quartiles, so we can see it
        var m = Lib.constrain(
            valAxis.c2p(d.med, true),
            Math.min(q1, q3) + 1, Math.max(q1, q3) - 1
        );

        // for compatibility with box, violin, and candlestick
        // perhaps we should put this into cd0.t instead so it's more explicit,
        // but what we have now is:
        // - box always has d.lf, but boxpoints can be anything
        // - violin has d.lf and should always use it (boxpoints is undefined)
        // - candlestick has only min/max
        var useExtremes = (d.lf === undefined) || (trace.boxpoints === false);
        var lf = valAxis.c2p(useExtremes ? d.min : d.lf, true);
        var uf = valAxis.c2p(useExtremes ? d.max : d.uf, true);
        var ln = valAxis.c2p(d.ln, true);
        var un = valAxis.c2p(d.un, true);

        if(trace.orientation === 'h') {
            d3.select(this).attr('d',
                'M' + m + ',' + posm0 + 'V' + posm1 + // median line
                'M' + q1 + ',' + pos0 + 'V' + pos1 + // left edge
                (notched ? 'H' + ln + 'L' + m + ',' + posm1 + 'L' + un + ',' + pos1 : '') + // top notched edge
                'H' + q3 + // end of the top edge
                'V' + pos0 + // right edge
                (notched ? 'H' + un + 'L' + m + ',' + posm0 + 'L' + ln + ',' + pos0 : '') + // bottom notched edge
                'Z' + // end of the box
                'M' + q1 + ',' + posc + 'H' + lf + 'M' + q3 + ',' + posc + 'H' + uf + // whiskers
                ((whiskerWidth === 0) ? '' : // whisker caps
                    'M' + lf + ',' + posw0 + 'V' + posw1 + 'M' + uf + ',' + posw0 + 'V' + posw1));
        } else {
            d3.select(this).attr('d',
                'M' + posm0 + ',' + m + 'H' + posm1 + // median line
                'M' + pos0 + ',' + q1 + 'H' + pos1 + // top of the box
                (notched ? 'V' + ln + 'L' + posm1 + ',' + m + 'L' + pos1 + ',' + un : '') + // notched right edge
                'V' + q3 + // end of the right edge
                'H' + pos0 + // bottom of the box
                (notched ? 'V' + un + 'L' + posm0 + ',' + m + 'L' + pos0 + ',' + ln : '') + // notched left edge
                'Z' + // end of the box
                'M' + posc + ',' + q1 + 'V' + lf + 'M' + posc + ',' + q3 + 'V' + uf + // whiskers
                ((whiskerWidth === 0) ? '' : // whisker caps
                    'M' + posw0 + ',' + lf + 'H' + posw1 + 'M' + posw0 + ',' + uf + 'H' + posw1));
        }
    });
}

function plotPoints(sel, axes, trace, t) {
    var xa = axes.x;
    var ya = axes.y;
    var bdPos = t.bdPos;
    var bPos = t.bPos;

    // to support violin points
    var mode = trace.boxpoints || trace.points;

    // repeatable pseudo-random number generator
    Lib.seedPseudoRandom();

    // since box plot points get an extra level of nesting, each
    // box needs the trace styling info
    var fn = function(d) {
        d.forEach(function(v) {
            v.t = t;
            v.trace = trace;
        });
        return d;
    };

    var gPoints = sel.selectAll('g.points')
        .data(mode ? fn : []);

    gPoints.enter().append('g')
        .attr('class', 'points');

    gPoints.exit().remove();

    var paths = gPoints.selectAll('path')
        .data(function(d) {
            var i;
            var pts = d.pts2;

            // normally use IQR, but if this is 0 or too small, use max-min
            var typicalSpread = Math.max((d.max - d.min) / 10, d.q3 - d.q1);
            var minSpread = typicalSpread * 1e-9;
            var spreadLimit = typicalSpread * JITTERSPREAD;
            var jitterFactors = [];
            var maxJitterFactor = 0;
            var newJitter;

            // dynamic jitter
            if(trace.jitter) {
                if(typicalSpread === 0) {
                    // edge case of no spread at all: fall back to max jitter
                    maxJitterFactor = 1;
                    jitterFactors = new Array(pts.length);
                    for(i = 0; i < pts.length; i++) {
                        jitterFactors[i] = 1;
                    }
                } else {
                    for(i = 0; i < pts.length; i++) {
                        var i0 = Math.max(0, i - JITTERCOUNT);
                        var pmin = pts[i0].v;
                        var i1 = Math.min(pts.length - 1, i + JITTERCOUNT);
                        var pmax = pts[i1].v;

                        if(mode !== 'all') {
                            if(pts[i].v < d.lf) pmax = Math.min(pmax, d.lf);
                            else pmin = Math.max(pmin, d.uf);
                        }

                        var jitterFactor = Math.sqrt(spreadLimit * (i1 - i0) / (pmax - pmin + minSpread)) || 0;
                        jitterFactor = Lib.constrain(Math.abs(jitterFactor), 0, 1);

                        jitterFactors.push(jitterFactor);
                        maxJitterFactor = Math.max(jitterFactor, maxJitterFactor);
                    }
                }
                newJitter = trace.jitter * 2 / (maxJitterFactor || 1);
            }

            // fills in 'x' and 'y' in calcdata 'pts' item
            for(i = 0; i < pts.length; i++) {
                var pt = pts[i];
                var v = pt.v;

                var jitterOffset = trace.jitter ?
                    (newJitter * jitterFactors[i] * (Lib.pseudoRandom() - 0.5)) :
                    0;

                var posPx = d.pos + bPos + bdPos * (trace.pointpos + jitterOffset);

                if(trace.orientation === 'h') {
                    pt.y = posPx;
                    pt.x = v;
                } else {
                    pt.x = posPx;
                    pt.y = v;
                }

                // tag suspected outliers
                if(mode === 'suspectedoutliers' && v < d.uo && v > d.lo) {
                    pt.so = true;
                }
            }

            return pts;
        });

    paths.enter().append('path')
        .classed('point', true);

    paths.exit().remove();

    paths.call(Drawing.translatePoints, xa, ya);
}

function plotBoxMean(sel, axes, trace, t) {
    var posAxis = axes.pos;
    var valAxis = axes.val;
    var bPos = t.bPos;
    var bPosPxOffset = t.bPosPxOffset || 0;

    // to support violin mean lines
    var mode = trace.boxmean || (trace.meanline || {}).visible;

    // to support for one-sided box
    var bdPos0;
    var bdPos1;
    if(Array.isArray(t.bdPos)) {
        bdPos0 = t.bdPos[0];
        bdPos1 = t.bdPos[1];
    } else {
        bdPos0 = t.bdPos;
        bdPos1 = t.bdPos;
    }

    var paths = sel.selectAll('path.mean').data((
        (trace.type === 'box' && trace.boxmean) ||
        (trace.type === 'violin' && trace.box.visible && trace.meanline.visible)
    ) ? Lib.identity : []);

    paths.enter().append('path')
        .attr('class', 'mean')
        .style({
            fill: 'none',
            'vector-effect': 'non-scaling-stroke'
        });

    paths.exit().remove();

    paths.each(function(d) {
        var posc = posAxis.c2p(d.pos + bPos, true) + bPosPxOffset;
        var pos0 = posAxis.c2p(d.pos + bPos - bdPos0, true) + bPosPxOffset;
        var pos1 = posAxis.c2p(d.pos + bPos + bdPos1, true) + bPosPxOffset;
        var m = valAxis.c2p(d.mean, true);
        var sl = valAxis.c2p(d.mean - d.sd, true);
        var sh = valAxis.c2p(d.mean + d.sd, true);

        if(trace.orientation === 'h') {
            d3.select(this).attr('d',
                'M' + m + ',' + pos0 + 'V' + pos1 +
                (mode === 'sd' ?
                    'm0,0L' + sl + ',' + posc + 'L' + m + ',' + pos0 + 'L' + sh + ',' + posc + 'Z' :
                    '')
            );
        } else {
            d3.select(this).attr('d',
                'M' + pos0 + ',' + m + 'H' + pos1 +
                (mode === 'sd' ?
                    'm0,0L' + posc + ',' + sl + 'L' + pos0 + ',' + m + 'L' + posc + ',' + sh + 'Z' :
                    '')
            );
        }
    });
}

module.exports = {
    plot: plot,
    plotBoxAndWhiskers: plotBoxAndWhiskers,
    plotPoints: plotPoints,
    plotBoxMean: plotBoxMean
};
