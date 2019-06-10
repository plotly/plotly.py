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
var attributes = require('./attributes');
var handleConstraintDefaults = require('../contour/constraint_defaults');
var handleContoursDefaults = require('../contour/contours_defaults');
var handleStyleDefaults = require('../contour/style_defaults');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    function coerce2(attr) {
        return Lib.coerce2(traceIn, traceOut, attributes, attr);
    }

    coerce('carpet');

    // If either a or b is not present, then it's not a valid trace *unless* the carpet
    // axis has the a or b values we're looking for. So if these are not found, just defer
    // that decision until the calc step.
    //
    // NB: the calc step will modify the original data input by assigning whichever of
    // a or b are missing. This is necessary because panning goes right from supplyDefaults
    // to plot (skipping calc). That means on subsequent updates, this *will* need to be
    // able to find a and b.
    //
    // The long-term proper fix is that this should perhaps use underscored attributes to
    // at least modify the user input to a slightly lesser extent. Fully removing the
    // input mutation is challenging. The underscore approach is not currently taken since
    // it requires modification to all of the functions below that expect the coerced
    // attribute name to match the property name -- except '_a' !== 'a' so that is not
    // straightforward.
    if(traceIn.a && traceIn.b) {
        var len = handleXYZDefaults(traceIn, traceOut, coerce, layout, 'a', 'b');

        if(!len) {
            traceOut.visible = false;
            return;
        }

        coerce('text');
        var isConstraint = (coerce('contours.type') === 'constraint');

        if(isConstraint) {
            handleConstraintDefaults(traceIn, traceOut, coerce, layout, defaultColor, {hasHover: false});
        } else {
            handleContoursDefaults(traceIn, traceOut, coerce, coerce2);
            handleStyleDefaults(traceIn, traceOut, coerce, layout, {hasHover: false});
        }
    } else {
        traceOut._defaultColor = defaultColor;
        traceOut._length = null;
    }
};
