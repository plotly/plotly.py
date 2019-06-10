/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Fx = require('../../components/fx');
var Registry = require('../../registry');
var getTraceColor = require('./get_trace_color');
var Color = require('../../components/color');
var fillText = Lib.fillText;

module.exports = function hoverPoints(pointData, xval, yval, hovermode) {
    var cd = pointData.cd;
    var trace = cd[0].trace;
    var xa = pointData.xa;
    var ya = pointData.ya;
    var xpx = xa.c2p(xval);
    var ypx = ya.c2p(yval);
    var pt = [xpx, ypx];
    var hoveron = trace.hoveron || '';
    var minRad = (trace.mode.indexOf('markers') !== -1) ? 3 : 0.5;

    // look for points to hover on first, then take fills only if we
    // didn't find a point
    if(hoveron.indexOf('points') !== -1) {
        var dx = function(di) {
            // dx and dy are used in compare modes - here we want to always
            // prioritize the closest data point, at least as long as markers are
            // the same size or nonexistent, but still try to prioritize small markers too.
            var rad = Math.max(3, di.mrc || 0);
            var kink = 1 - 1 / rad;
            var dxRaw = Math.abs(xa.c2p(di.x) - xpx);
            var d = (dxRaw < rad) ? (kink * dxRaw / rad) : (dxRaw - rad + kink);
            return d;
        };
        var dy = function(di) {
            var rad = Math.max(3, di.mrc || 0);
            var kink = 1 - 1 / rad;
            var dyRaw = Math.abs(ya.c2p(di.y) - ypx);
            return (dyRaw < rad) ? (kink * dyRaw / rad) : (dyRaw - rad + kink);
        };
        var dxy = function(di) {
            // scatter points: d.mrc is the calculated marker radius
            // adjust the distance so if you're inside the marker it
            // always will show up regardless of point size, but
            // prioritize smaller points
            var rad = Math.max(minRad, di.mrc || 0);
            var dx = xa.c2p(di.x) - xpx;
            var dy = ya.c2p(di.y) - ypx;
            return Math.max(Math.sqrt(dx * dx + dy * dy) - rad, 1 - minRad / rad);
        };
        var distfn = Fx.getDistanceFunction(hovermode, dx, dy, dxy);

        Fx.getClosest(cd, distfn, pointData);

        // skip the rest (for this trace) if we didn't find a close point
        if(pointData.index !== false) {
            // the closest data point
            var di = cd[pointData.index];
            var xc = xa.c2p(di.x, true);
            var yc = ya.c2p(di.y, true);
            var rad = di.mrc || 1;

            // now we're done using the whole `calcdata` array, replace the
            // index with the original index (in case of inserted point from
            // stacked area)
            pointData.index = di.i;

            var orientation = cd[0].t.orientation;
            // TODO: for scatter and bar, option to show (sub)totals and
            // raw data? Currently stacked and/or normalized bars just show
            // the normalized individual sizes, so that's what I'm doing here
            // for now.
            var sizeVal = orientation && (di.sNorm || di.s);
            var xLabelVal = (orientation === 'h') ? sizeVal : di.x;
            var yLabelVal = (orientation === 'v') ? sizeVal : di.y;

            Lib.extendFlat(pointData, {
                color: getTraceColor(trace, di),

                x0: xc - rad,
                x1: xc + rad,
                xLabelVal: xLabelVal,

                y0: yc - rad,
                y1: yc + rad,
                yLabelVal: yLabelVal,

                spikeDistance: dxy(di),
                hovertemplate: trace.hovertemplate
            });

            fillText(di, trace, pointData);
            Registry.getComponentMethod('errorbars', 'hoverInfo')(di, trace, pointData);

            return [pointData];
        }
    }

    // even if hoveron is 'fills', only use it if we have polygons too
    if(hoveron.indexOf('fills') !== -1 && trace._polygons) {
        var polygons = trace._polygons;
        var polygonsIn = [];
        var inside = false;
        var xmin = Infinity;
        var xmax = -Infinity;
        var ymin = Infinity;
        var ymax = -Infinity;

        var i, j, polygon, pts, xCross, x0, x1, y0, y1;

        for(i = 0; i < polygons.length; i++) {
            polygon = polygons[i];
            // TODO: this is not going to work right for curved edges, it will
            // act as though they're straight. That's probably going to need
            // the elements themselves to capture the events. Worth it?
            if(polygon.contains(pt)) {
                inside = !inside;
                // TODO: need better than just the overall bounding box
                polygonsIn.push(polygon);
                ymin = Math.min(ymin, polygon.ymin);
                ymax = Math.max(ymax, polygon.ymax);
            }
        }

        if(inside) {
            // constrain ymin/max to the visible plot, so the label goes
            // at the middle of the piece you can see
            ymin = Math.max(ymin, 0);
            ymax = Math.min(ymax, ya._length);

            // find the overall left-most and right-most points of the
            // polygon(s) we're inside at their combined vertical midpoint.
            // This is where we will draw the hover label.
            // Note that this might not be the vertical midpoint of the
            // whole trace, if it's disjoint.
            var yAvg = (ymin + ymax) / 2;
            for(i = 0; i < polygonsIn.length; i++) {
                pts = polygonsIn[i].pts;
                for(j = 1; j < pts.length; j++) {
                    y0 = pts[j - 1][1];
                    y1 = pts[j][1];
                    if((y0 > yAvg) !== (y1 >= yAvg)) {
                        x0 = pts[j - 1][0];
                        x1 = pts[j][0];
                        if(y1 - y0) {
                            xCross = x0 + (x1 - x0) * (yAvg - y0) / (y1 - y0);
                            xmin = Math.min(xmin, xCross);
                            xmax = Math.max(xmax, xCross);
                        }
                    }
                }
            }

            // constrain xmin/max to the visible plot now too
            xmin = Math.max(xmin, 0);
            xmax = Math.min(xmax, xa._length);

            // get only fill or line color for the hover color
            var color = Color.defaultLine;
            if(Color.opacity(trace.fillcolor)) color = trace.fillcolor;
            else if(Color.opacity((trace.line || {}).color)) {
                color = trace.line.color;
            }

            Lib.extendFlat(pointData, {
                // never let a 2D override 1D type as closest point
                // also: no spikeDistance, it's not allowed for fills
                distance: pointData.maxHoverDistance,
                x0: xmin,
                x1: xmax,
                y0: yAvg,
                y1: yAvg,
                color: color,
                hovertemplate: false
            });

            delete pointData.index;

            if(trace.text && !Array.isArray(trace.text)) {
                pointData.text = String(trace.text);
            } else pointData.text = trace.name;

            return [pointData];
        }
    }
};
