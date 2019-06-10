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

    plotConnectorRegions(gd, plotinfo, cdModule, traceLayer);
    plotConnectorLines(gd, plotinfo, cdModule, traceLayer);

    barPlot(gd, plotinfo, cdModule, traceLayer, {
        mode: fullLayout.funnelmode,
        norm: fullLayout.funnelmode,
        gap: fullLayout.funnelgap,
        groupgap: fullLayout.funnelgroupgap
    });
};

function plotConnectorRegions(gd, plotinfo, cdModule, traceLayer) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    Lib.makeTraceGroups(traceLayer, cdModule, 'trace bars').each(function(cd) {
        var plotGroup = d3.select(this);
        var trace = cd[0].trace;

        var group = Lib.ensureSingle(plotGroup, 'g', 'regions');

        if(!trace.connector || !trace.connector.visible) {
            group.remove();
            return;
        }

        var isHorizontal = (trace.orientation === 'h');

        var connectors = group.selectAll('g.region').data(Lib.identity);

        connectors.enter().append('g')
            .classed('region', true);

        connectors.exit().remove();

        var len = connectors.size();

        connectors.each(function(di, i) {
            // don't draw lines between nulls
            if(i !== len - 1 && !di.cNext) return;

            var xy = getXY(di, xa, ya, isHorizontal);
            var x = xy[0];
            var y = xy[1];

            var shape = '';

            if(x[3] !== undefined && y[3] !== undefined) {
                if(isHorizontal) {
                    shape += 'M' + x[0] + ',' + y[1] + 'L' + x[2] + ',' + y[2] + 'H' + x[3] + 'L' + x[1] + ',' + y[1] + 'Z';
                } else {
                    shape += 'M' + x[1] + ',' + y[1] + 'L' + x[2] + ',' + y[3] + 'V' + y[2] + 'L' + x[1] + ',' + y[0] + 'Z';
                }
            }

            Lib.ensureSingle(d3.select(this), 'path')
                .attr('d', shape)
                .call(Drawing.setClipUrl, plotinfo.layerClipId, gd);
        });
    });
}

function plotConnectorLines(gd, plotinfo, cdModule, traceLayer) {
    var xa = plotinfo.xaxis;
    var ya = plotinfo.yaxis;

    Lib.makeTraceGroups(traceLayer, cdModule, 'trace bars').each(function(cd) {
        var plotGroup = d3.select(this);
        var trace = cd[0].trace;

        var group = Lib.ensureSingle(plotGroup, 'g', 'lines');

        if(!trace.connector || !trace.connector.visible || !trace.connector.line.width) {
            group.remove();
            return;
        }

        var isHorizontal = (trace.orientation === 'h');

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

            if(x[3] !== undefined && y[3] !== undefined) {
                if(isHorizontal) {
                    shape += 'M' + x[0] + ',' + y[1] + 'L' + x[2] + ',' + y[2];
                    shape += 'M' + x[1] + ',' + y[1] + 'L' + x[3] + ',' + y[2];
                } else {
                    shape += 'M' + x[1] + ',' + y[1] + 'L' + x[2] + ',' + y[3];
                    shape += 'M' + x[1] + ',' + y[0] + 'L' + x[2] + ',' + y[2];
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

    s[3] = sAxis.c2p(di.nextS1, true);
    p[3] = pAxis.c2p(di.nextP1, true);

    return isHorizontal ? [s, p] : [p, s];
}
