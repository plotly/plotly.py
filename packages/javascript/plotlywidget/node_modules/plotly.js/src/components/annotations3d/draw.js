/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var drawRaw = require('../annotations/draw').drawRaw;
var project = require('../../plots/gl3d/project');
var axLetters = ['x', 'y', 'z'];

module.exports = function draw(scene) {
    var fullSceneLayout = scene.fullSceneLayout;
    var dataScale = scene.dataScale;
    var anns = fullSceneLayout.annotations;

    for(var i = 0; i < anns.length; i++) {
        var ann = anns[i];
        var annotationIsOffscreen = false;

        for(var j = 0; j < 3; j++) {
            var axLetter = axLetters[j];
            var pos = ann[axLetter];
            var ax = fullSceneLayout[axLetter + 'axis'];
            var posFraction = ax.r2fraction(pos);

            if(posFraction < 0 || posFraction > 1) {
                annotationIsOffscreen = true;
                break;
            }
        }

        if(annotationIsOffscreen) {
            scene.fullLayout._infolayer
                .select('.annotation-' + scene.id + '[data-index="' + i + '"]')
                .remove();
        } else {
            ann._pdata = project(scene.glplot.cameraParams, [
                fullSceneLayout.xaxis.r2l(ann.x) * dataScale[0],
                fullSceneLayout.yaxis.r2l(ann.y) * dataScale[1],
                fullSceneLayout.zaxis.r2l(ann.z) * dataScale[2]
            ]);

            drawRaw(scene.graphDiv, ann, i, scene.id, ann._xa, ann._ya);
        }
    }
};
