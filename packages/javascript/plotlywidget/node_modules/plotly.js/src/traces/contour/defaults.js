/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

var handleXYZDefaults = require('../heatmap/xyz_defaults');
var handleConstraintDefaults = require('./constraint_defaults');
var handleContoursDefaults = require('./contours_defaults');
var handleStyleDefaults = require('./style_defaults');
var attributes = require('./attributes');


module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    function coerce2(attr) {
        return Lib.coerce2(traceIn, traceOut, attributes, attr);
    }

    var len = handleXYZDefaults(traceIn, traceOut, coerce, layout);
    if(!len) {
        traceOut.visible = false;
        return;
    }

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    var isConstraint = (coerce('contours.type') === 'constraint');
    coerce('connectgaps', Lib.isArray1D(traceOut.z));

    if(isConstraint) {
        handleConstraintDefaults(traceIn, traceOut, coerce, layout, defaultColor);
    } else {
        handleContoursDefaults(traceIn, traceOut, coerce, coerce2);
        handleStyleDefaults(traceIn, traceOut, coerce, layout);
    }
};
