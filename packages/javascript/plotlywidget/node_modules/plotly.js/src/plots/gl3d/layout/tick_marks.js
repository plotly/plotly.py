/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

/* eslint block-scoped-var: 0*/
/* eslint no-redeclare: 0*/

'use strict';

module.exports = computeTickMarks;

var Axes = require('../../cartesian/axes');
var Lib = require('../../../lib');

var AXES_NAMES = ['xaxis', 'yaxis', 'zaxis'];

var centerPoint = [0, 0, 0];

function contourLevelsFromTicks(ticks) {
    var result = new Array(3);
    for(var i = 0; i < 3; ++i) {
        var tlevel = ticks[i];
        var clevel = new Array(tlevel.length);
        for(var j = 0; j < tlevel.length; ++j) {
            clevel[j] = tlevel[j].x;
        }
        result[i] = clevel;
    }
    return result;
}

function computeTickMarks(scene) {
    var axesOptions = scene.axesOptions;
    var glRange = scene.glplot.axesPixels;
    var sceneLayout = scene.fullSceneLayout;

    var ticks = [[], [], []];

    for(var i = 0; i < 3; ++i) {
        var axes = sceneLayout[AXES_NAMES[i]];

        axes._length = (glRange[i].hi - glRange[i].lo) *
            glRange[i].pixelsPerDataUnit / scene.dataScale[i];

        if(Math.abs(axes._length) === Infinity ||
           isNaN(axes._length)) {
            ticks[i] = [];
        } else {
            axes._input_range = axes.range.slice();
            axes.range[0] = (glRange[i].lo) / scene.dataScale[i];
            axes.range[1] = (glRange[i].hi) / scene.dataScale[i];
            axes._m = 1.0 / (scene.dataScale[i] * glRange[i].pixelsPerDataUnit);

            if(axes.range[0] === axes.range[1]) {
                axes.range[0] -= 1;
                axes.range[1] += 1;
            }
            // this is necessary to short-circuit the 'y' handling
            // in autotick part of calcTicks... Treating all axes as 'y' in this case
            // running the autoticks here, then setting
            // autoticks to false to get around the 2D handling in calcTicks.
            var tickModeCached = axes.tickmode;
            if(axes.tickmode === 'auto') {
                axes.tickmode = 'linear';
                var nticks = axes.nticks || Lib.constrain((axes._length / 40), 4, 9);
                Axes.autoTicks(axes, Math.abs(axes.range[1] - axes.range[0]) / nticks);
            }
            var dataTicks = Axes.calcTicks(axes);
            for(var j = 0; j < dataTicks.length; ++j) {
                dataTicks[j].x = dataTicks[j].x * scene.dataScale[i];

                if(axes.type === 'date') {
                    dataTicks[j].text =
                    dataTicks[j].text.replace(/\<br\>/g, ' ');
                }
            }
            ticks[i] = dataTicks;


            axes.tickmode = tickModeCached;
        }
    }

    axesOptions.ticks = ticks;

    // Calculate tick lengths dynamically
    for(var i = 0; i < 3; ++i) {
        centerPoint[i] = 0.5 * (scene.glplot.bounds[0][i] + scene.glplot.bounds[1][i]);
        for(var j = 0; j < 2; ++j) {
            axesOptions.bounds[j][i] = scene.glplot.bounds[j][i];
        }
    }

    scene.contourLevels = contourLevelsFromTicks(ticks);
}
