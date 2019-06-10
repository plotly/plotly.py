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

var Lib = require('../../lib');
var Drawing = require('../../components/drawing');
var helpers = require('../../plots/polar/helpers');

module.exports = function plot(gd, subplot, cdbar) {
    var xa = subplot.xaxis;
    var ya = subplot.yaxis;
    var radialAxis = subplot.radialAxis;
    var angularAxis = subplot.angularAxis;
    var pathFn = makePathFn(subplot);
    var barLayer = subplot.layers.frontplot.select('g.barlayer');

    Lib.makeTraceGroups(barLayer, cdbar, 'trace bars').each(function(cd) {
        var plotGroup = cd[0].node3 = d3.select(this);
        var pointGroup = Lib.ensureSingle(plotGroup, 'g', 'points');
        var bars = pointGroup.selectAll('g.point').data(Lib.identity);

        bars.enter().append('g')
            .style('vector-effect', 'non-scaling-stroke')
            .style('stroke-miterlimit', 2)
            .classed('point', true);

        bars.exit().remove();

        bars.each(function(di) {
            var bar = d3.select(this);

            var rp0 = di.rp0 = radialAxis.c2p(di.s0);
            var rp1 = di.rp1 = radialAxis.c2p(di.s1);
            var thetag0 = di.thetag0 = angularAxis.c2g(di.p0);
            var thetag1 = di.thetag1 = angularAxis.c2g(di.p1);

            var dPath;

            if(!isNumeric(rp0) || !isNumeric(rp1) ||
                !isNumeric(thetag0) || !isNumeric(thetag1) ||
                rp0 === rp1 || thetag0 === thetag1
            ) {
                // do not remove blank bars, to keep data-to-node
                // mapping intact during radial drag, that we
                // can skip calling _module.style during interactions
                dPath = 'M0,0Z';
            } else {
                // this 'center' pt is used for selections and hover labels
                var rg1 = radialAxis.c2g(di.s1);
                var thetagMid = (thetag0 + thetag1) / 2;
                di.ct = [
                    xa.c2p(rg1 * Math.cos(thetagMid)),
                    ya.c2p(rg1 * Math.sin(thetagMid))
                ];

                dPath = pathFn(rp0, rp1, thetag0, thetag1);
            }

            Lib.ensureSingle(bar, 'path').attr('d', dPath);
        });

        // clip plotGroup, when trace layer isn't clipped
        Drawing.setClipUrl(
            plotGroup,
            subplot._hasClipOnAxisFalse ? subplot.clipIds.forTraces : null,
            gd
        );
    });
};

function makePathFn(subplot) {
    var cxx = subplot.cxx;
    var cyy = subplot.cyy;

    if(subplot.vangles) {
        return function(r0, r1, _a0, _a1) {
            var a0, a1;

            if(Lib.angleDelta(_a0, _a1) > 0) {
                a0 = _a0;
                a1 = _a1;
            } else {
                a0 = _a1;
                a1 = _a0;
            }

            var va0 = helpers.findEnclosingVertexAngles(a0, subplot.vangles)[0];
            var va1 = helpers.findEnclosingVertexAngles(a1, subplot.vangles)[1];
            var vaBar = [va0, (a0 + a1) / 2, va1];
            return helpers.pathPolygonAnnulus(r0, r1, a0, a1, vaBar, cxx, cyy);
        };
    }

    return function(r0, r1, a0, a1) {
        return Lib.pathAnnulus(r0, r1, a0, a1, cxx, cyy);
    };
}
