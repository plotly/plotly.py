/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var createLine = require('regl-line2d');

var Registry = require('../../registry');
var prepareRegl = require('../../lib/prepare_regl');
var getModuleCalcData = require('../../plots/get_data').getModuleCalcData;
var Cartesian = require('../../plots/cartesian');
var getFromId = require('../../plots/cartesian/axis_ids').getFromId;
var shouldShowZeroLine = require('../../plots/cartesian/axes').shouldShowZeroLine;

var SPLOM = 'splom';

function plot(gd) {
    var fullLayout = gd._fullLayout;
    var _module = Registry.getModule(SPLOM);
    var splomCalcData = getModuleCalcData(gd.calcdata, _module)[0];

    var success = prepareRegl(gd, ['ANGLE_instanced_arrays', 'OES_element_index_uint']);
    if(!success) return;

    if(fullLayout._hasOnlyLargeSploms) {
        updateGrid(gd);
    }

    _module.plot(gd, {}, splomCalcData);
}

function drag(gd) {
    var cd = gd.calcdata;
    var fullLayout = gd._fullLayout;

    if(fullLayout._hasOnlyLargeSploms) {
        updateGrid(gd);
    }

    for(var i = 0; i < cd.length; i++) {
        var cd0 = cd[i][0];
        var trace = cd0.trace;
        var scene = fullLayout._splomScenes[trace.uid];

        if(trace.type === 'splom' && scene && scene.matrix) {
            dragOne(gd, trace, scene);
        }
    }
}

function dragOne(gd, trace, scene) {
    var visibleLength = scene.matrixOptions.data.length;
    var visibleDims = trace._visibleDims;
    var ranges = scene.viewOpts.ranges = new Array(visibleLength);

    for(var k = 0; k < visibleDims.length; k++) {
        var i = visibleDims[k];
        var rng = ranges[k] = new Array(4);

        var xa = getFromId(gd, trace._diag[i][0]);
        if(xa) {
            rng[0] = xa.r2l(xa.range[0]);
            rng[2] = xa.r2l(xa.range[1]);
        }

        var ya = getFromId(gd, trace._diag[i][1]);
        if(ya) {
            rng[1] = ya.r2l(ya.range[0]);
            rng[3] = ya.r2l(ya.range[1]);
        }
    }

    if(scene.selectBatch.length || scene.unselectBatch.length) {
        scene.matrix.update({ranges: ranges}, {ranges: ranges});
    } else {
        scene.matrix.update({ranges: ranges});
    }
}

function updateGrid(gd) {
    var fullLayout = gd._fullLayout;
    var regl = fullLayout._glcanvas.data()[0].regl;
    var splomGrid = fullLayout._splomGrid;

    if(!splomGrid) {
        splomGrid = fullLayout._splomGrid = createLine(regl);
    }
    splomGrid.update(makeGridData(gd));
}

function makeGridData(gd) {
    var fullLayout = gd._fullLayout;
    var gs = fullLayout._size;
    var fullView = [0, 0, fullLayout.width, fullLayout.height];
    var lookup = {};
    var k;

    function push(prefix, ax, x0, x1, y0, y1) {
        var lcolor = ax[prefix + 'color'];
        var lwidth = ax[prefix + 'width'];
        var key = String(lcolor + lwidth);

        if(key in lookup) {
            lookup[key].data.push(NaN, NaN, x0, x1, y0, y1);
        } else {
            lookup[key] = {
                data: [x0, x1, y0, y1],
                join: 'rect',
                thickness: lwidth,
                color: lcolor,
                viewport: fullView,
                range: fullView,
                overlay: false
            };
        }
    }

    for(k in fullLayout._splomSubplots) {
        var sp = fullLayout._plots[k];
        var xa = sp.xaxis;
        var ya = sp.yaxis;
        var xVals = xa._vals;
        var yVals = ya._vals;
        // ya.l2p assumes top-to-bottom coordinate system (a la SVG),
        // we need to compute bottom-to-top offsets and slopes:
        var yOffset = gs.b + ya.domain[0] * gs.h;
        var ym = -ya._m;
        var yb = -ym * ya.r2l(ya.range[0], ya.calendar);
        var x, y;

        if(xa.showgrid) {
            for(k = 0; k < xVals.length; k++) {
                x = xa._offset + xa.l2p(xVals[k].x);
                push('grid', xa, x, yOffset, x, yOffset + ya._length);
            }
        }
        if(ya.showgrid) {
            for(k = 0; k < yVals.length; k++) {
                y = yOffset + yb + ym * yVals[k].x;
                push('grid', ya, xa._offset, y, xa._offset + xa._length, y);
            }
        }
        if(shouldShowZeroLine(gd, xa, ya)) {
            x = xa._offset + xa.l2p(0);
            push('zeroline', xa, x, yOffset, x, yOffset + ya._length);
        }
        if(shouldShowZeroLine(gd, ya, xa)) {
            y = yOffset + yb + 0;
            push('zeroline', ya, xa._offset, y, xa._offset + xa._length, y);
        }
    }

    var gridBatches = [];
    for(k in lookup) {
        gridBatches.push(lookup[k]);
    }

    return gridBatches;
}

function clean(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var lookup = {};
    var i;

    if(oldFullLayout._splomScenes) {
        for(i = 0; i < newFullData.length; i++) {
            var newTrace = newFullData[i];
            if(newTrace.type === 'splom') {
                lookup[newTrace.uid] = 1;
            }
        }
        for(i = 0; i < oldFullData.length; i++) {
            var oldTrace = oldFullData[i];
            if(!lookup[oldTrace.uid]) {
                var scene = oldFullLayout._splomScenes[oldTrace.uid];
                if(scene && scene.destroy) scene.destroy();
                // must first set scene to null in order to get garbage collected
                oldFullLayout._splomScenes[oldTrace.uid] = null;
                delete oldFullLayout._splomScenes[oldTrace.uid];
            }
        }
    }

    if(Object.keys(oldFullLayout._splomScenes || {}).length === 0) {
        delete oldFullLayout._splomScenes;
    }

    if(oldFullLayout._splomGrid &&
        (!newFullLayout._hasOnlyLargeSploms && oldFullLayout._hasOnlyLargeSploms)) {
        // must first set scene to null in order to get garbage collected
        oldFullLayout._splomGrid.destroy();
        oldFullLayout._splomGrid = null;
        delete oldFullLayout._splomGrid;
    }

    Cartesian.clean(newFullData, newFullLayout, oldFullData, oldFullLayout);
}

module.exports = {
    name: SPLOM,
    attr: Cartesian.attr,
    attrRegex: Cartesian.attrRegex,
    layoutAttributes: Cartesian.layoutAttributes,
    supplyLayoutDefaults: Cartesian.supplyLayoutDefaults,
    drawFramework: Cartesian.drawFramework,
    plot: plot,
    drag: drag,
    updateGrid: updateGrid,
    clean: clean,
    updateFx: Cartesian.updateFx,
    toSVG: Cartesian.toSVG
};
