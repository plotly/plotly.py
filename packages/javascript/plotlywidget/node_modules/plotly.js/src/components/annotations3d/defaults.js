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
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');
var handleAnnotationCommonDefaults = require('../annotations/common_defaults');
var attributes = require('./attributes');

module.exports = function handleDefaults(sceneLayoutIn, sceneLayoutOut, opts) {
    handleArrayContainerDefaults(sceneLayoutIn, sceneLayoutOut, {
        name: 'annotations',
        handleItemDefaults: handleAnnotationDefaults,
        fullLayout: opts.fullLayout
    });
};

function handleAnnotationDefaults(annIn, annOut, sceneLayout, opts) {
    function coerce(attr, dflt) {
        return Lib.coerce(annIn, annOut, attributes, attr, dflt);
    }

    function coercePosition(axLetter) {
        var axName = axLetter + 'axis';

        // mock in such way that getFromId grabs correct 3D axis
        var gdMock = { _fullLayout: {} };
        gdMock._fullLayout[axName] = sceneLayout[axName];

        return Axes.coercePosition(annOut, gdMock, coerce, axLetter, axLetter, 0.5);
    }


    var visible = coerce('visible');
    if(!visible) return;

    handleAnnotationCommonDefaults(annIn, annOut, opts.fullLayout, coerce);

    coercePosition('x');
    coercePosition('y');
    coercePosition('z');

    // if you have one coordinate you should all three
    Lib.noneOrAll(annIn, annOut, ['x', 'y', 'z']);

    // hard-set here for completeness
    annOut.xref = 'x';
    annOut.yref = 'y';
    annOut.zref = 'z';

    coerce('xanchor');
    coerce('yanchor');
    coerce('xshift');
    coerce('yshift');

    if(annOut.showarrow) {
        annOut.axref = 'pixel';
        annOut.ayref = 'pixel';

        // TODO maybe default values should be bigger than the 2D case?
        coerce('ax', -10);
        coerce('ay', -30);

        // if you have one part of arrow length you should have both
        Lib.noneOrAll(annIn, annOut, ['ax', 'ay']);
    }
}
