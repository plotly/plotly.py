/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var attributes = require('./attributes');
var supplyIsoDefaults = require('../isosurface/defaults').supplyIsoDefaults;

var MIN = 0.1; // Note: often we don't want the data cube to be disappeared

function createWave(n, minOpacity) {
    var arr = [];
    var steps = 32; // Max: 256
    for(var i = 0; i < steps; i++) {
        var u = i / (steps - 1);
        var v = minOpacity + (1 - minOpacity) * (1 - Math.pow(Math.sin(n * u * Math.PI), 2));
        arr.push([
            u,
            Math.max(1, Math.min(0, v))
        ]);
    }
    return arr;
}

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    supplyIsoDefaults(traceIn, traceOut, defaultColor, layout, coerce);

    var opacityscale = coerce('opacityscale');
    if(opacityscale === 'max') {
        traceOut.opacityscale = [[0, MIN], [1, 1]];
    } else if(opacityscale === 'min') {
        traceOut.opacityscale = [[0, 1], [1, MIN]];
    } else if(opacityscale === 'extremes') {
        traceOut.opacityscale = createWave(1, MIN);
    } else if(!isValidScaleArray(opacityscale)) {
        traceOut.opacityscale = undefined;
    }
};

function isValidScaleArray(scl) {
    var highestVal = 0;

    if(!Array.isArray(scl) || scl.length < 2) return false;

    if(!scl[0] || !scl[scl.length - 1]) return false;

    if(+scl[0][0] !== 0 || +scl[scl.length - 1][0] !== 1) return false;

    for(var i = 0; i < scl.length; i++) {
        var si = scl[i];

        if(si.length !== 2 || +si[0] < highestVal) {
            return false;
        }

        highestVal = +si[0];
    }

    return true;
}
