/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');

var constants = require('../scatter/constants');
var subTypes = require('../scatter/subtypes');
var handleMarkerDefaults = require('../scatter/marker_defaults');
var handleLineDefaults = require('../scatter/line_defaults');
var handleLineShapeDefaults = require('../scatter/line_shape_defaults');
var handleTextDefaults = require('../scatter/text_defaults');
var handleFillColorDefaults = require('../scatter/fillcolor_defaults');

var attributes = require('./attributes');


module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var a = coerce('a');
    var b = coerce('b');
    var c = coerce('c');
    var len;

    // allow any one array to be missing, len is the minimum length of those
    // present. Note that after coerce data_array's are either Arrays (which
    // are truthy even if empty) or undefined. As in scatter, an empty array
    // is different from undefined, because it can signify that this data is
    // not known yet but expected in the future
    if(a) {
        len = a.length;
        if(b) {
            len = Math.min(len, b.length);
            if(c) len = Math.min(len, c.length);
        } else if(c) len = Math.min(len, c.length);
        else len = 0;
    } else if(b && c) {
        len = Math.min(b.length, c.length);
    }

    if(!len) {
        traceOut.visible = false;
        return;
    }

    traceOut._length = len;

    coerce('sum');

    coerce('text');
    coerce('hovertext');
    if(traceOut.hoveron !== 'fills') coerce('hovertemplate');

    var defaultMode = len < constants.PTS_LINESONLY ? 'lines+markers' : 'lines';
    coerce('mode', defaultMode);

    if(subTypes.hasLines(traceOut)) {
        handleLineDefaults(traceIn, traceOut, defaultColor, layout, coerce);
        handleLineShapeDefaults(traceIn, traceOut, coerce);
        coerce('connectgaps');
    }

    if(subTypes.hasMarkers(traceOut)) {
        handleMarkerDefaults(traceIn, traceOut, defaultColor, layout, coerce, {gradient: true});
    }

    if(subTypes.hasText(traceOut)) {
        handleTextDefaults(traceIn, traceOut, layout, coerce);
    }

    var dfltHoverOn = [];

    if(subTypes.hasMarkers(traceOut) || subTypes.hasText(traceOut)) {
        coerce('cliponaxis');
        coerce('marker.maxdisplayed');
        dfltHoverOn.push('points');
    }

    coerce('fill');
    if(traceOut.fill !== 'none') {
        handleFillColorDefaults(traceIn, traceOut, defaultColor, coerce);
        if(!subTypes.hasLines(traceOut)) handleLineShapeDefaults(traceIn, traceOut, coerce);
    }

    if(traceOut.fill === 'tonext' || traceOut.fill === 'toself') {
        dfltHoverOn.push('fills');
    }
    coerce('hoveron', dfltHoverOn.join('+') || 'points');

    Lib.coerceSelectionMarkerOpacity(traceOut, coerce);
};
