/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var map1dArray = require('../carpet/map_1d_array');
var makepath = require('../carpet/makepath');
var Drawing = require('../../components/drawing');
var Lib = require('../../lib');

var makeCrossings = require('../contour/make_crossings');
var findAllPaths = require('../contour/find_all_paths');
var contourPlot = require('../contour/plot');
var constants = require('../contour/constants');
var convertToConstraints = require('../contour/convert_to_constraints');
var joinAllPaths = require('./join_all_paths');
var emptyPathinfo = require('../contour/empty_pathinfo');
var mapPathinfo = require('./map_pathinfo');
var lookupCarpet = require('../carpet/lookup_carpetid');
var closeBoundaries = require('../contour/close_boundaries');

module.exports = function plot(gd, plotinfo, cdcontours, contourcarpetLayer) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    Lib.makeTraceGroups(contourcarpetLayer, cdcontours, 'contour').each(function(cd) {
        var plotGroup = d3.select(this);
        var cd0 = cd[0];
        var trace = cd0.trace;

        var carpet = trace._carpetTrace = lookupCarpet(gd, trace);
        var carpetcd = gd.calcdata[carpet.index][0];

        if(!carpet.visible || carpet.visible === 'legendonly') return;

        var a = cd0.a;
        var b = cd0.b;
        var contours = trace.contours;
        var pathinfo = emptyPathinfo(contours, plotinfo, cd0);
        var isConstraint = contours.type === 'constraint';
        var operation = contours._operation;
        var coloring = isConstraint ? (operation === '=' ? 'lines' : 'fill') : contours.coloring;

        // Map [a, b] (data) --> [i, j] (pixels)
        function ab2p(ab) {
            var pt = carpet.ab2xy(ab[0], ab[1], true);
            return [xa.c2p(pt[0]), ya.c2p(pt[1])];
        }

        // Define the perimeter in a/b coordinates:
        var perimeter = [
            [a[0], b[b.length - 1]],
            [a[a.length - 1], b[b.length - 1]],
            [a[a.length - 1], b[0]],
            [a[0], b[0]]
        ];

        // Extract the contour levels:
        makeCrossings(pathinfo);
        var atol = (a[a.length - 1] - a[0]) * 1e-8;
        var btol = (b[b.length - 1] - b[0]) * 1e-8;
        findAllPaths(pathinfo, atol, btol);

        // Constraints might need to be draw inverted, which is not something contours
        // handle by default since they're assumed fully opaque so that they can be
        // drawn overlapping. This function flips the paths as necessary so that they're
        // drawn correctly.
        //
        // TODO: Perhaps this should be generalized and *all* paths should be drawn as
        // closed regions so that translucent contour levels would be valid.
        // See: https://github.com/plotly/plotly.js/issues/1356
        var fillPathinfo = pathinfo;
        if(contours.type === 'constraint') {
            fillPathinfo = convertToConstraints(pathinfo, operation);
            closeBoundaries(fillPathinfo, operation, perimeter, trace);
        }

        // Map the paths in a/b coordinates to pixel coordinates:
        mapPathinfo(pathinfo, ab2p);

        // draw everything

        // Compute the boundary path
        var seg, xp, yp, i;
        var segs = [];
        for(i = carpetcd.clipsegments.length - 1; i >= 0; i--) {
            seg = carpetcd.clipsegments[i];
            xp = map1dArray([], seg.x, xa.c2p);
            yp = map1dArray([], seg.y, ya.c2p);
            xp.reverse();
            yp.reverse();
            segs.push(makepath(xp, yp, seg.bicubic));
        }

        var boundaryPath = 'M' + segs.join('L') + 'Z';

        // Draw the baseline background fill that fills in the space behind any other
        // contour levels:
        makeBackground(plotGroup, carpetcd.clipsegments, xa, ya, isConstraint, coloring);

        // Draw the specific contour fills. As a simplification, they're assumed to be
        // fully opaque so that it's easy to draw them simply overlapping. The alternative
        // would be to flip adjacent paths and draw closed paths for each level instead.
        makeFills(trace, plotGroup, xa, ya, fillPathinfo, perimeter, ab2p, carpet, carpetcd, coloring, boundaryPath);

        // Draw contour lines:
        makeLinesAndLabels(plotGroup, pathinfo, gd, cd0, contours, plotinfo, carpet);

        // Clip the boundary of the plot
        Drawing.setClipUrl(plotGroup, carpet._clipPathId, gd);
    });
};

function makeLinesAndLabels(plotgroup, pathinfo, gd, cd0, contours, plotinfo, carpet) {
    var lineContainer = Lib.ensureSingle(plotgroup, 'g', 'contourlines');
    var showLines = contours.showlines !== false;
    var showLabels = contours.showlabels;
    var clipLinesForLabels = showLines && showLabels;

    // Even if we're not going to show lines, we need to create them
    // if we're showing labels, because the fill paths include the perimeter
    // so can't be used to position the labels correctly.
    // In this case we'll remove the lines after making the labels.
    var linegroup = contourPlot.createLines(lineContainer, showLines || showLabels, pathinfo);

    var lineClip = contourPlot.createLineClip(lineContainer, clipLinesForLabels, gd, cd0.trace.uid);

    var labelGroup = plotgroup.selectAll('g.contourlabels')
        .data(showLabels ? [0] : []);

    labelGroup.exit().remove();

    labelGroup.enter().append('g')
        .classed('contourlabels', true);

    if(showLabels) {
        var xa = plotinfo.xaxis;
        var ya = plotinfo.yaxis;
        var xLen = xa._length;
        var yLen = ya._length;
        // for simplicity use the xy box for label clipping outline.
        var labelClipPathData = [[
            [0, 0],
            [xLen, 0],
            [xLen, yLen],
            [0, yLen]
        ]];


        var labelData = [];

        // invalidate the getTextLocation cache in case paths changed
        Lib.clearLocationCache();

        var contourFormat = contourPlot.labelFormatter(contours, cd0.t.cb, gd._fullLayout);

        var dummyText = Drawing.tester.append('text')
            .attr('data-notex', 1)
            .call(Drawing.font, contours.labelfont);

        // use `bounds` only to keep labels away from the x/y boundaries
        // `constrainToCarpet` below ensures labels don't go off the
        // carpet edges
        var bounds = {
            left: 0,
            right: xLen,
            center: xLen / 2,
            top: 0,
            bottom: yLen,
            middle: yLen / 2
        };

        var plotDiagonal = Math.sqrt(xLen * xLen + yLen * yLen);

        // the path length to use to scale the number of labels to draw:
        var normLength = constants.LABELDISTANCE * plotDiagonal /
            Math.max(1, pathinfo.length / constants.LABELINCREASE);

        linegroup.each(function(d) {
            var textOpts = contourPlot.calcTextOpts(d.level, contourFormat, dummyText, gd);

            d3.select(this).selectAll('path').each(function(pathData) {
                var path = this;
                var pathBounds = Lib.getVisibleSegment(path, bounds, textOpts.height / 2);
                if(!pathBounds) return;

                constrainToCarpet(path, pathData, d, pathBounds, carpet, textOpts.height);

                if(pathBounds.len < (textOpts.width + textOpts.height) * constants.LABELMIN) return;

                var maxLabels = Math.min(Math.ceil(pathBounds.len / normLength),
                    constants.LABELMAX);

                for(var i = 0; i < maxLabels; i++) {
                    var loc = contourPlot.findBestTextLocation(path, pathBounds, textOpts,
                        labelData, bounds);

                    if(!loc) break;

                    contourPlot.addLabelData(loc, textOpts, labelData, labelClipPathData);
                }
            });
        });

        dummyText.remove();

        contourPlot.drawLabels(labelGroup, labelData, gd, lineClip,
            clipLinesForLabels ? labelClipPathData : null);
    }

    if(showLabels && !showLines) linegroup.remove();
}

// figure out if this path goes off the edge of the carpet
// and shorten the part we call visible to keep labels away from the edge
function constrainToCarpet(path, pathData, levelData, pathBounds, carpet, textHeight) {
    var pathABData;
    for(var i = 0; i < levelData.pedgepaths.length; i++) {
        if(pathData === levelData.pedgepaths[i]) {
            pathABData = levelData.edgepaths[i];
        }
    }
    if(!pathABData) return;

    var aMin = carpet.a[0];
    var aMax = carpet.a[carpet.a.length - 1];
    var bMin = carpet.b[0];
    var bMax = carpet.b[carpet.b.length - 1];

    function getOffset(abPt, pathVector) {
        var offset = 0;
        var edgeVector;
        var dAB = 0.1;
        if(Math.abs(abPt[0] - aMin) < dAB || Math.abs(abPt[0] - aMax) < dAB) {
            edgeVector = normalizeVector(carpet.dxydb_rough(abPt[0], abPt[1], dAB));
            offset = Math.max(offset, textHeight * vectorTan(pathVector, edgeVector) / 2);
        }

        if(Math.abs(abPt[1] - bMin) < dAB || Math.abs(abPt[1] - bMax) < dAB) {
            edgeVector = normalizeVector(carpet.dxyda_rough(abPt[0], abPt[1], dAB));
            offset = Math.max(offset, textHeight * vectorTan(pathVector, edgeVector) / 2);
        }
        return offset;
    }

    var startVector = getUnitVector(path, 0, 1);
    var endVector = getUnitVector(path, pathBounds.total, pathBounds.total - 1);
    var minStart = getOffset(pathABData[0], startVector);
    var maxEnd = pathBounds.total - getOffset(pathABData[pathABData.length - 1], endVector);

    if(pathBounds.min < minStart) pathBounds.min = minStart;
    if(pathBounds.max > maxEnd) pathBounds.max = maxEnd;

    pathBounds.len = pathBounds.max - pathBounds.min;
}

function getUnitVector(path, p0, p1) {
    var pt0 = path.getPointAtLength(p0);
    var pt1 = path.getPointAtLength(p1);
    var dx = pt1.x - pt0.x;
    var dy = pt1.y - pt0.y;
    var len = Math.sqrt(dx * dx + dy * dy);
    return [dx / len, dy / len];
}

function normalizeVector(v) {
    var len = Math.sqrt(v[0] * v[0] + v[1] * v[1]);
    return [v[0] / len, v[1] / len];
}

function vectorTan(v0, v1) {
    var cos = Math.abs(v0[0] * v1[0] + v0[1] * v1[1]);
    var sin = Math.sqrt(1 - cos * cos);
    return sin / cos;
}

function makeBackground(plotgroup, clipsegments, xaxis, yaxis, isConstraint, coloring) {
    var seg, xp, yp, i;
    var bggroup = Lib.ensureSingle(plotgroup, 'g', 'contourbg');

    var bgfill = bggroup.selectAll('path')
        .data((coloring === 'fill' && !isConstraint) ? [0] : []);
    bgfill.enter().append('path');
    bgfill.exit().remove();

    var segs = [];
    for(i = 0; i < clipsegments.length; i++) {
        seg = clipsegments[i];
        xp = map1dArray([], seg.x, xaxis.c2p);
        yp = map1dArray([], seg.y, yaxis.c2p);
        segs.push(makepath(xp, yp, seg.bicubic));
    }

    bgfill
        .attr('d', 'M' + segs.join('L') + 'Z')
        .style('stroke', 'none');
}

function makeFills(trace, plotgroup, xa, ya, pathinfo, perimeter, ab2p, carpet, carpetcd, coloring, boundaryPath) {
    var fillgroup = Lib.ensureSingle(plotgroup, 'g', 'contourfill');

    var fillitems = fillgroup.selectAll('path')
        .data(coloring === 'fill' ? pathinfo : []);
    fillitems.enter().append('path');
    fillitems.exit().remove();
    fillitems.each(function(pi) {
        // join all paths for this level together into a single path
        // first follow clockwise around the perimeter to close any open paths
        // if the whole perimeter is above this level, start with a path
        // enclosing the whole thing. With all that, the parity should mean
        // that we always fill everything above the contour, nothing below
        var fullpath = joinAllPaths(trace, pi, perimeter, ab2p, carpet, carpetcd, xa, ya);

        if(pi.prefixBoundary) {
            fullpath = boundaryPath + fullpath;
        }

        if(!fullpath) {
            d3.select(this).remove();
        } else {
            d3.select(this)
                .attr('d', fullpath)
                .style('stroke', 'none');
        }
    });
}
