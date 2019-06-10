/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Axes = require('../../plots/cartesian/axes');

module.exports = function convert(scene) {
    var fullSceneLayout = scene.fullSceneLayout;
    var anns = fullSceneLayout.annotations;

    for(var i = 0; i < anns.length; i++) {
        mockAnnAxes(anns[i], scene);
    }

    scene.fullLayout._infolayer
        .selectAll('.annotation-' + scene.id)
        .remove();
};

function mockAnnAxes(ann, scene) {
    var fullSceneLayout = scene.fullSceneLayout;
    var domain = fullSceneLayout.domain;
    var size = scene.fullLayout._size;

    var base = {
        // this gets fill in on render
        pdata: null,

        // to get setConvert to not execute cleanly
        type: 'linear',

        // don't try to update them on `editable: true`
        autorange: false,

        // set infinite range so that annotation draw routine
        // does not try to remove 'outside-range' annotations,
        // this case is handled in the render loop
        range: [-Infinity, Infinity]
    };

    ann._xa = {};
    Lib.extendFlat(ann._xa, base);
    Axes.setConvert(ann._xa);
    ann._xa._offset = size.l + domain.x[0] * size.w;
    ann._xa.l2p = function() {
        return 0.5 * (1 + ann._pdata[0] / ann._pdata[3]) * size.w * (domain.x[1] - domain.x[0]);
    };

    ann._ya = {};
    Lib.extendFlat(ann._ya, base);
    Axes.setConvert(ann._ya);
    ann._ya._offset = size.t + (1 - domain.y[1]) * size.h;
    ann._ya.l2p = function() {
        return 0.5 * (1 - ann._pdata[1] / ann._pdata[3]) * size.h * (domain.y[1] - domain.y[0]);
    };
}
