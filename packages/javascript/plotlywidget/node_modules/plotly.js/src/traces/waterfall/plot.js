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
var barPlot = require('../bar/plot').plot;

module.exports = function plot(gd, plotinfo, cdModule, traceLayer) {
    var fullLayout = gd._fullLayout;

    barPlot(gd, plotinfo, cdModule, traceLayer, {
        mode: fullLayout.waterfallmode,
        norm: fullLayout.waterfallmode,
        gap: fullLayout.waterfallgap,
        groupgap: fullLayout.waterfallgroupgap
    });

    plotConnectors(gd, plotinfo, cdModule, traceLayer);
};

function plotConnectors(gd, plotinfo, cdModule, traceLayer) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    Lib.makeTraceGroups(traceLayer, cdModule, 'trace bars').each(function(cd) {
        var plotGroup = d3.select(this);
        var trace = cd[0].trace;

        var group = Lib.ensureSingle(plotGroup, 'g', 'lines');

        if(!trace.connector || !trace.connector.visible) {
            group.remove();
            return;
        }

        var isHorizontal = (trace.orientation === 'h');
        var mode = trace.connector.mode;

        var connectors = group.selectAll('g.line').data(Lib.identity);

        connectors.enter().append('g')
            .classed('line', true);

        connectors.exit().remove();

        var len = connectors.size();

        connectors.each(function(di, i) {
            // don't draw lines between nulls
            if(i !== len - 1 && !di.cNext) return;

            var xy = getXY(di, xa, ya, isHorizontal);
            var x = xy[0];
            var y = xy[1];

            var shape = '';

            if(mode === 'spanning') {
                if(!di.isSum && i > 0) {
                    if(isHorizontal) {
                        shape += 'M' + x[0] + ',' + y[1] + 'V' + y[0];
                    } else {
                        shape += 'M' + x[1] + ',' + y[0] + 'H' + x[0];
                    }
                }
            }

            if(mode !== 'between') {
                if(di.isSum || i < len - 1) {
                    if(isHorizontal) {
                        shape += 'M' + x[1] + ',' + y[0] + 'V' + y[1];
                    } else {
                        shape += 'M' + x[0] + ',' + y[1] + 'H' + x[1];
                    }
                }
            }

            if(x[2] !== undefined && y[2] !== undefined) {
                if(isHorizontal) {
                    shape += 'M' + x[1] + ',' + y[1] + 'V' + y[2];
                } else {
                    shape += 'M' + x[1] + ',' + y[1] + 'H' + x[2];
                }
            }

            if(shape === '') shape = 'M0,0Z';

            Lib.ensureSingle(d3.select(this), 'path')
                .attr('d', shape)
                .call(Drawing.setClipUrl, plotinfo.layerClipId, gd);
        });
    });
}

function getXY(di, xa, ya, isHorizontal) {
    var s = [];
    var p = [];

    var sAxis = isHorizontal ? xa : ya;
    var pAxis = isHorizontal ? ya : xa;

    s[0] = sAxis.c2p(di.s0, true);
    p[0] = pAxis.c2p(di.p0, true);

    s[1] = sAxis.c2p(di.s1, true);
    p[1] = pAxis.c2p(di.p1, true);

    s[2] = sAxis.c2p(di.nextS0, true);
    p[2] = pAxis.c2p(di.nextP0, true);

    return isHorizontal ? [s, p] : [p, s];
}
