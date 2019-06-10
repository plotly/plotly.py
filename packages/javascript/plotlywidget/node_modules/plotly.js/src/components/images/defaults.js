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

var attributes = require('./attributes');
var name = 'images';

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut) {
    var opts = {
        name: name,
        handleItemDefaults: imageDefaults
    };

    handleArrayContainerDefaults(layoutIn, layoutOut, opts);
};


function imageDefaults(imageIn, imageOut, fullLayout) {
    function coerce(attr, dflt) {
        return Lib.coerce(imageIn, imageOut, attributes, attr, dflt);
    }

    var source = coerce('source');
    var visible = coerce('visible', !!source);

    if(!visible) return imageOut;

    coerce('layer');
    coerce('xanchor');
    coerce('yanchor');
    coerce('sizex');
    coerce('sizey');
    coerce('sizing');
    coerce('opacity');

    var gdMock = { _fullLayout: fullLayout };
    var axLetters = ['x', 'y'];

    for(var i = 0; i < 2; i++) {
        // 'paper' is the fallback axref
        var axLetter = axLetters[i];
        var axRef = Axes.coerceRef(imageIn, imageOut, gdMock, axLetter, 'paper');

        if(axRef !== 'paper') {
            var ax = Axes.getFromId(gdMock, axRef);
            ax._imgIndices.push(imageOut._index);
        }

        Axes.coercePosition(imageOut, gdMock, coerce, axRef, axLetter, 0);
    }

    return imageOut;
}
