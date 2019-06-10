/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');

var colorscaleDefaults = require('../../components/colorscale/defaults');
var attributes = require('./attributes');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var u = coerce('u');
    var v = coerce('v');
    var w = coerce('w');

    var x = coerce('x');
    var y = coerce('y');
    var z = coerce('z');

    if(
        !u || !u.length || !v || !v.length || !w || !w.length ||
        !x || !x.length || !y || !y.length || !z || !z.length
    ) {
        traceOut.visible = false;
        return;
    }

    coerce('sizeref');
    coerce('sizemode');

    coerce('anchor');

    coerce('lighting.ambient');
    coerce('lighting.diffuse');
    coerce('lighting.specular');
    coerce('lighting.roughness');
    coerce('lighting.fresnel');
    coerce('lightposition.x');
    coerce('lightposition.y');
    coerce('lightposition.z');

    colorscaleDefaults(traceIn, traceOut, layout, coerce, {prefix: '', cLetter: 'c'});

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    // disable 1D transforms (for now)
    traceOut._length = null;
};
