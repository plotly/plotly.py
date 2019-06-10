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

var boxPlot = require('../box/plot');
var linePoints = require('../scatter/line_points');
var helpers = require('./helpers');

module.exports = function plot(gd, plotinfo, cdViolins, violinLayer) {
    var fullLayout = gd._fullLayout;
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    function makePath(pts) {
        var segments = linePoints(pts, {
            xaxis: xa,
            yaxis: ya,
            connectGaps: true,
            baseTolerance: 0.75,
            shape: 'spline',
            simplify: true
        });
        return Drawing.smoothopen(segments[0], 1);
    }

    Lib.makeTraceGroups(violinLayer, cdViolins, 'trace violins').each(function(cd) {
        var plotGroup = d3.select(this);
        var cd0 = cd[0];
        var t = cd0.t;
        var trace = cd0.trace;
        if(!plotinfo.isRangePlot) cd0.node3 = plotGroup;

        if(trace.visible !== true || t.empty) {
            plotGroup.remove();
            return;
        }

        var bPos = t.bPos;
        var bdPos = t.bdPos;
        var valAxis = plotinfo[t.valLetter + 'axis'];
        var posAxis = plotinfo[t.posLetter + 'axis'];
        var hasBothSides = trace.side === 'both';
        var hasPositiveSide = hasBothSides || trace.side === 'positive';
        var hasNegativeSide = hasBothSides || trace.side === 'negative';

        var violins = plotGroup.selectAll('path.violin').data(Lib.identity);

        violins.enter().append('path')
            .style('vector-effect', 'non-scaling-stroke')
            .attr('class', 'violin');

        violins.exit().remove();

        violins.each(function(d) {
            var pathSel = d3.select(this);
            var density = d.density;
            var len = density.length;
            var posCenter = d.pos + bPos;
            var posCenterPx = posAxis.c2p(posCenter);

            var scale;
            if(trace.width) {
                scale = t.maxKDE / bdPos;
            } else {
                var groupStats = fullLayout._violinScaleGroupStats[trace.scalegroup];
                scale = trace.scalemode === 'count' ?
                    (groupStats.maxKDE / bdPos) * (groupStats.maxCount / d.pts.length) :
                    groupStats.maxKDE / bdPos;
            }

            var pathPos, pathNeg, path;
            var i, k, pts, pt;

            if(hasPositiveSide) {
                pts = new Array(len);
                for(i = 0; i < len; i++) {
                    pt = pts[i] = {};
                    pt[t.posLetter] = posCenter + (density[i].v / scale);
                    pt[t.valLetter] = density[i].t;
                }
                pathPos = makePath(pts);
            }

            if(hasNegativeSide) {
                pts = new Array(len);
                for(k = 0, i = len - 1; k < len; k++, i--) {
                    pt = pts[k] = {};
                    pt[t.posLetter] = posCenter - (density[i].v / scale);
                    pt[t.valLetter] = density[i].t;
                }
                pathNeg = makePath(pts);
            }

            if(hasBothSides) {
                path = pathPos + 'L' + pathNeg.substr(1) + 'Z';
            } else {
                var startPt = [posCenterPx, valAxis.c2p(density[0].t)];
                var endPt = [posCenterPx, valAxis.c2p(density[len - 1].t)];

                if(trace.orientation === 'h') {
                    startPt.reverse();
                    endPt.reverse();
                }

                if(hasPositiveSide) {
                    path = 'M' + startPt + 'L' + pathPos.substr(1) + 'L' + endPt;
                } else {
                    path = 'M' + endPt + 'L' + pathNeg.substr(1) + 'L' + startPt;
                }
            }
            pathSel.attr('d', path);

            // save a few things used in getPositionOnKdePath, getKdeValue
            // on hover and for meanline draw block below
            d.posCenterPx = posCenterPx;
            d.posDensityScale = scale * bdPos;
            d.path = pathSel.node();
            d.pathLength = d.path.getTotalLength() / (hasBothSides ? 2 : 1);
        });

        var boxAttrs = trace.box;
        var boxWidth = boxAttrs.width;
        var boxLineWidth = (boxAttrs.line || {}).width;
        var bdPosScaled;
        var bPosPxOffset;

        if(hasBothSides) {
            bdPosScaled = bdPos * boxWidth;
            bPosPxOffset = 0;
        } else if(hasPositiveSide) {
            bdPosScaled = [0, bdPos * boxWidth / 2];
            bPosPxOffset = -boxLineWidth;
        } else {
            bdPosScaled = [bdPos * boxWidth / 2, 0];
            bPosPxOffset = boxLineWidth;
        }

        // inner box
        boxPlot.plotBoxAndWhiskers(plotGroup, {pos: posAxis, val: valAxis}, trace, {
            bPos: bPos,
            bdPos: bdPosScaled,
            bPosPxOffset: bPosPxOffset
        });

        // meanline insider box
        boxPlot.plotBoxMean(plotGroup, {pos: posAxis, val: valAxis}, trace, {
            bPos: bPos,
            bdPos: bdPosScaled,
            bPosPxOffset: bPosPxOffset
        });

        var fn;
        if(!trace.box.visible && trace.meanline.visible) {
            fn = Lib.identity;
        }

        // N.B. use different class name than boxPlot.plotBoxMean,
        // to avoid selectAll conflict
        var meanPaths = plotGroup.selectAll('path.meanline').data(fn || []);
        meanPaths.enter().append('path')
            .attr('class', 'meanline')
            .style('fill', 'none')
            .style('vector-effect', 'non-scaling-stroke');
        meanPaths.exit().remove();
        meanPaths.each(function(d) {
            var v = valAxis.c2p(d.mean, true);
            var p = helpers.getPositionOnKdePath(d, trace, v);

            d3.select(this).attr('d',
                trace.orientation === 'h' ?
                    'M' + v + ',' + p[0] + 'V' + p[1] :
                    'M' + p[0] + ',' + v + 'H' + p[1]
            );
        });

        boxPlot.plotPoints(plotGroup, {x: xa, y: ya}, trace, t);
    });
};
