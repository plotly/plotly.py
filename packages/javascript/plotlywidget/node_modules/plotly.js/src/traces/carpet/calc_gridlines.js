/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Axes = require('../../plots/cartesian/axes');
var extendFlat = require('../../lib/extend').extendFlat;

module.exports = function calcGridlines(trace, axisLetter, crossAxisLetter) {
    var i, j, j0;
    var eps, bounds, n1, n2, n, value, v;
    var j1, v0, v1, d;

    var data = trace['_' + axisLetter];
    var axis = trace[axisLetter + 'axis'];

    var gridlines = axis._gridlines = [];
    var minorgridlines = axis._minorgridlines = [];
    var boundarylines = axis._boundarylines = [];

    var crossData = trace['_' + crossAxisLetter];
    var crossAxis = trace[crossAxisLetter + 'axis'];

    if(axis.tickmode === 'array') {
        axis.tickvals = data.slice();
    }

    var xcp = trace._xctrl;
    var ycp = trace._yctrl;
    var nea = xcp[0].length;
    var neb = xcp.length;
    var na = trace._a.length;
    var nb = trace._b.length;

    Axes.prepTicks(axis);

    // don't leave tickvals in axis looking like an attribute
    if(axis.tickmode === 'array') delete axis.tickvals;

    // The default is an empty array that will cause the join to remove the gridline if
    // it's just disappeared:
    // axis._startline = axis._endline = [];

    // If the cross axis uses bicubic interpolation, then the grid
    // lines fall once every three expanded grid row/cols:
    var stride = axis.smoothing ? 3 : 1;

    function constructValueGridline(value) {
        var i, j, j0, tj, pxy, i0, ti, xy, dxydi0, dxydi1, dxydj0, dxydj1;
        var xpoints = [];
        var ypoints = [];
        var ret = {};
        // Search for the fractional grid index giving this line:
        if(axisLetter === 'b') {
            // For the position we use just the i-j coordinates:
            j = trace.b2j(value);

            // The derivatives for catmull-rom splines are discontinuous across cell
            // boundaries though, so we need to provide both the cell and the position
            // within the cell separately:
            j0 = Math.floor(Math.max(0, Math.min(nb - 2, j)));
            tj = j - j0;

            ret.length = nb;
            ret.crossLength = na;

            ret.xy = function(i) {
                return trace.evalxy([], i, j);
            };

            ret.dxy = function(i0, ti) {
                return trace.dxydi([], i0, j0, ti, tj);
            };

            for(i = 0; i < na; i++) {
                i0 = Math.min(na - 2, i);
                ti = i - i0;
                xy = trace.evalxy([], i, j);

                if(crossAxis.smoothing && i > 0) {
                    // First control point:
                    dxydi0 = trace.dxydi([], i - 1, j0, 0, tj);
                    xpoints.push(pxy[0] + dxydi0[0] / 3);
                    ypoints.push(pxy[1] + dxydi0[1] / 3);

                    // Second control point:
                    dxydi1 = trace.dxydi([], i - 1, j0, 1, tj);
                    xpoints.push(xy[0] - dxydi1[0] / 3);
                    ypoints.push(xy[1] - dxydi1[1] / 3);
                }

                xpoints.push(xy[0]);
                ypoints.push(xy[1]);

                pxy = xy;
            }
        } else {
            i = trace.a2i(value);
            i0 = Math.floor(Math.max(0, Math.min(na - 2, i)));
            ti = i - i0;

            ret.length = na;
            ret.crossLength = nb;

            ret.xy = function(j) {
                return trace.evalxy([], i, j);
            };

            ret.dxy = function(j0, tj) {
                return trace.dxydj([], i0, j0, ti, tj);
            };

            for(j = 0; j < nb; j++) {
                j0 = Math.min(nb - 2, j);
                tj = j - j0;
                xy = trace.evalxy([], i, j);

                if(crossAxis.smoothing && j > 0) {
                    // First control point:
                    dxydj0 = trace.dxydj([], i0, j - 1, ti, 0);
                    xpoints.push(pxy[0] + dxydj0[0] / 3);
                    ypoints.push(pxy[1] + dxydj0[1] / 3);

                    // Second control point:
                    dxydj1 = trace.dxydj([], i0, j - 1, ti, 1);
                    xpoints.push(xy[0] - dxydj1[0] / 3);
                    ypoints.push(xy[1] - dxydj1[1] / 3);
                }

                xpoints.push(xy[0]);
                ypoints.push(xy[1]);

                pxy = xy;
            }
        }

        ret.axisLetter = axisLetter;
        ret.axis = axis;
        ret.crossAxis = crossAxis;
        ret.value = value;
        ret.constvar = crossAxisLetter;
        ret.index = n;
        ret.x = xpoints;
        ret.y = ypoints;
        ret.smoothing = crossAxis.smoothing;

        return ret;
    }

    function constructArrayGridline(idx) {
        var j, i0, j0, ti, tj;
        var xpoints = [];
        var ypoints = [];
        var ret = {};
        ret.length = data.length;
        ret.crossLength = crossData.length;

        if(axisLetter === 'b') {
            j0 = Math.max(0, Math.min(nb - 2, idx));
            tj = Math.min(1, Math.max(0, idx - j0));

            ret.xy = function(i) {
                return trace.evalxy([], i, idx);
            };

            ret.dxy = function(i0, ti) {
                return trace.dxydi([], i0, j0, ti, tj);
            };

            // In the tickmode: array case, this operation is a simple
            // transfer of data:
            for(j = 0; j < nea; j++) {
                xpoints[j] = xcp[idx * stride][j];
                ypoints[j] = ycp[idx * stride][j];
            }
        } else {
            i0 = Math.max(0, Math.min(na - 2, idx));
            ti = Math.min(1, Math.max(0, idx - i0));

            ret.xy = function(j) {
                return trace.evalxy([], idx, j);
            };

            ret.dxy = function(j0, tj) {
                return trace.dxydj([], i0, j0, ti, tj);
            };

            // In the tickmode: array case, this operation is a simple
            // transfer of data:
            for(j = 0; j < neb; j++) {
                xpoints[j] = xcp[j][idx * stride];
                ypoints[j] = ycp[j][idx * stride];
            }
        }

        ret.axisLetter = axisLetter;
        ret.axis = axis;
        ret.crossAxis = crossAxis;
        ret.value = data[idx];
        ret.constvar = crossAxisLetter;
        ret.index = idx;
        ret.x = xpoints;
        ret.y = ypoints;
        ret.smoothing = crossAxis.smoothing;

        return ret;
    }

    if(axis.tickmode === 'array') {
        // var j0 = axis.startline ? 1 : 0;
        // var j1 = data.length - (axis.endline ? 1 : 0);

        eps = 5e-15;
        bounds = [
            Math.floor(((data.length - 1) - axis.arraytick0) / axis.arraydtick * (1 + eps)),
            Math.ceil((- axis.arraytick0) / axis.arraydtick / (1 + eps))
        ].sort(function(a, b) {return a - b;});

        // Unpack sorted values so we can be sure to avoid infinite loops if something
        // is backwards:
        n1 = bounds[0] - 1;
        n2 = bounds[1] + 1;

        // If the axes fall along array lines, then this is a much simpler process since
        // we already have all the control points we need
        for(n = n1; n < n2; n++) {
            j = axis.arraytick0 + axis.arraydtick * n;
            if(j < 0 || j > data.length - 1) continue;
            gridlines.push(extendFlat(constructArrayGridline(j), {
                color: axis.gridcolor,
                width: axis.gridwidth
            }));
        }

        for(n = n1; n < n2; n++) {
            j0 = axis.arraytick0 + axis.arraydtick * n;
            j1 = Math.min(j0 + axis.arraydtick, data.length - 1);

            // TODO: fix the bounds computation so we don't have to do a large range and then throw
            // out unneeded numbers
            if(j0 < 0 || j0 > data.length - 1) continue;
            if(j1 < 0 || j1 > data.length - 1) continue;

            v0 = data[j0];
            v1 = data[j1];

            for(i = 0; i < axis.minorgridcount; i++) {
                d = j1 - j0;

                // TODO: fix the bounds computation so we don't have to do a large range and then throw
                // out unneeded numbers
                if(d <= 0) continue;

                // XXX: This calculation isn't quite right. Off by one somewhere?
                v = v0 + (v1 - v0) * (i + 1) / (axis.minorgridcount + 1) * (axis.arraydtick / d);

                // TODO: fix the bounds computation so we don't have to do a large range and then throw
                // out unneeded numbers
                if(v < data[0] || v > data[data.length - 1]) continue;
                minorgridlines.push(extendFlat(constructValueGridline(v), {
                    color: axis.minorgridcolor,
                    width: axis.minorgridwidth
                }));
            }
        }

        if(axis.startline) {
            boundarylines.push(extendFlat(constructArrayGridline(0), {
                color: axis.startlinecolor,
                width: axis.startlinewidth
            }));
        }

        if(axis.endline) {
            boundarylines.push(extendFlat(constructArrayGridline(data.length - 1), {
                color: axis.endlinecolor,
                width: axis.endlinewidth
            }));
        }
    } else {
        // If the lines do not fall along the axes, then we have to interpolate
        // the contro points and so some math to figure out where the lines are
        // in the first place.

        // Compute the integer boudns of tick0 + n * dtick that fall within the range
        // (roughly speaking):
        // Give this a nice generous epsilon. We use at as * (1 + eps) in order to make
        // inequalities a little tolerant in a more or less correct manner:
        eps = 5e-15;
        bounds = [
            Math.floor((data[data.length - 1] - axis.tick0) / axis.dtick * (1 + eps)),
            Math.ceil((data[0] - axis.tick0) / axis.dtick / (1 + eps))
        ].sort(function(a, b) {return a - b;});

        // Unpack sorted values so we can be sure to avoid infinite loops if something
        // is backwards:
        n1 = bounds[0];
        n2 = bounds[1];

        for(n = n1; n <= n2; n++) {
            value = axis.tick0 + axis.dtick * n;

            gridlines.push(extendFlat(constructValueGridline(value), {
                color: axis.gridcolor,
                width: axis.gridwidth
            }));
        }

        for(n = n1 - 1; n < n2 + 1; n++) {
            value = axis.tick0 + axis.dtick * n;

            for(i = 0; i < axis.minorgridcount; i++) {
                v = value + axis.dtick * (i + 1) / (axis.minorgridcount + 1);
                if(v < data[0] || v > data[data.length - 1]) continue;
                minorgridlines.push(extendFlat(constructValueGridline(v), {
                    color: axis.minorgridcolor,
                    width: axis.minorgridwidth
                }));
            }
        }

        if(axis.startline) {
            boundarylines.push(extendFlat(constructValueGridline(data[0]), {
                color: axis.startlinecolor,
                width: axis.startlinewidth
            }));
        }

        if(axis.endline) {
            boundarylines.push(extendFlat(constructValueGridline(data[data.length - 1]), {
                color: axis.endlinecolor,
                width: axis.endlinewidth
            }));
        }
    }
};
