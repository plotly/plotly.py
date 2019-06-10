/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var isNumeric = require('fast-isnumeric');

var Drawing = require('../drawing');
var subTypes = require('../../traces/scatter/subtypes');

module.exports = function plot(gd, traces, plotinfo, transitionOpts) {
    var isNew;

    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    var hasAnimation = transitionOpts && transitionOpts.duration > 0;

    traces.each(function(d) {
        var trace = d[0].trace;
        // || {} is in case the trace (specifically scatterternary)
        // doesn't support error bars at all, but does go through
        // the scatter.plot mechanics, which calls ErrorBars.plot
        // internally
        var xObj = trace.error_x || {};
        var yObj = trace.error_y || {};

        var keyFunc;

        if(trace.ids) {
            keyFunc = function(d) {return d.id;};
        }

        var sparse = (
            subTypes.hasMarkers(trace) &&
            trace.marker.maxdisplayed > 0
        );

        if(!yObj.visible && !xObj.visible) d = [];

        var errorbars = d3.select(this).selectAll('g.errorbar')
            .data(d, keyFunc);

        errorbars.exit().remove();

        if(!d.length) return;

        if(!xObj.visible) errorbars.selectAll('path.xerror').remove();
        if(!yObj.visible) errorbars.selectAll('path.yerror').remove();

        errorbars.style('opacity', 1);

        var enter = errorbars.enter().append('g')
            .classed('errorbar', true);

        if(hasAnimation) {
            enter.style('opacity', 0).transition()
                .duration(transitionOpts.duration)
                .style('opacity', 1);
        }

        Drawing.setClipUrl(errorbars, plotinfo.layerClipId, gd);

        errorbars.each(function(d) {
            var errorbar = d3.select(this);
            var coords = errorCoords(d, xa, ya);

            if(sparse && !d.vis) return;

            var path;

            var yerror = errorbar.select('path.yerror');
            if(yObj.visible && isNumeric(coords.x) &&
                    isNumeric(coords.yh) &&
                    isNumeric(coords.ys)) {
                var yw = yObj.width;

                path = 'M' + (coords.x - yw) + ',' +
                    coords.yh + 'h' + (2 * yw) + // hat
                    'm-' + yw + ',0V' + coords.ys; // bar


                if(!coords.noYS) path += 'm-' + yw + ',0h' + (2 * yw); // shoe

                isNew = !yerror.size();

                if(isNew) {
                    yerror = errorbar.append('path')
                        .style('vector-effect', 'non-scaling-stroke')
                        .classed('yerror', true);
                } else if(hasAnimation) {
                    yerror = yerror
                        .transition()
                            .duration(transitionOpts.duration)
                            .ease(transitionOpts.easing);
                }

                yerror.attr('d', path);
            } else yerror.remove();

            var xerror = errorbar.select('path.xerror');
            if(xObj.visible && isNumeric(coords.y) &&
                    isNumeric(coords.xh) &&
                    isNumeric(coords.xs)) {
                var xw = (xObj.copy_ystyle ? yObj : xObj).width;

                path = 'M' + coords.xh + ',' +
                    (coords.y - xw) + 'v' + (2 * xw) + // hat
                    'm0,-' + xw + 'H' + coords.xs; // bar

                if(!coords.noXS) path += 'm0,-' + xw + 'v' + (2 * xw); // shoe

                isNew = !xerror.size();

                if(isNew) {
                    xerror = errorbar.append('path')
                        .style('vector-effect', 'non-scaling-stroke')
                        .classed('xerror', true);
                } else if(hasAnimation) {
                    xerror = xerror
                        .transition()
                            .duration(transitionOpts.duration)
                            .ease(transitionOpts.easing);
                }

                xerror.attr('d', path);
            } else xerror.remove();
        });
    });
};

// compute the coordinates of the error-bar objects
function errorCoords(d, xa, ya) {
    var out = {
        x: xa.c2p(d.x),
        y: ya.c2p(d.y)
    };

    // calculate the error bar size and hat and shoe locations
    if(d.yh !== undefined) {
        out.yh = ya.c2p(d.yh);
        out.ys = ya.c2p(d.ys);

        // if the shoes go off-scale (ie log scale, error bars past zero)
        // clip the bar and hide the shoes
        if(!isNumeric(out.ys)) {
            out.noYS = true;
            out.ys = ya.c2p(d.ys, true);
        }
    }

    if(d.xh !== undefined) {
        out.xh = xa.c2p(d.xh);
        out.xs = xa.c2p(d.xs);

        if(!isNumeric(out.xs)) {
            out.noXS = true;
            out.xs = xa.c2p(d.xs, true);
        }
    }

    return out;
}
