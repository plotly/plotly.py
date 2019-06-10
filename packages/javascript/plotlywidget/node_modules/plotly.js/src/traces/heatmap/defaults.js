/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');

var handleXYZDefaults = require('./xyz_defaults');
var handleStyleDefaults = require('./style_defaults');
var colorscaleDefaults = require('../../components/colorscale/defaults');
var attributes = require('./attributes');


module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var validData = handleXYZDefaults(traceIn, traceOut, coerce, layout);
    if(!validData) {
        traceOut.visible = false;
        return;
    }

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    handleStyleDefaults(traceIn, traceOut, coerce, layout);

    coerce('connectgaps', Lib.isArray1D(traceOut.z) && (traceOut.zsmooth !== false));

    colorscaleDefaults(traceIn, traceOut, layout, coerce, {prefix: '', cLetter: 'z'});
};
