/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

var handleRThetaDefaults = require('../scatterpolar/defaults').handleRThetaDefaults;
var handleStyleDefaults = require('../bar/style_defaults');
var attributes = require('./attributes');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var len = handleRThetaDefaults(traceIn, traceOut, layout, coerce);
    if(!len) {
        traceOut.visible = false;
        return;
    }

    // coerce('orientation', (traceOut.theta && !traceOut.r) ? 'angular' : 'radial');

    coerce('thetaunit');
    coerce('base');
    coerce('offset');
    coerce('width');

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    // var textPosition = coerce('textposition');
    // var hasBoth = Array.isArray(textPosition) || textPosition === 'auto';
    // var hasInside = hasBoth || textPosition === 'inside';
    // var hasOutside = hasBoth || textPosition === 'outside';

    // if(hasInside || hasOutside) {
    //     var textFont = coerceFont(coerce, 'textfont', layout.font);
    //     if(hasInside) coerceFont(coerce, 'insidetextfont', textFont);
    //     if(hasOutside) coerceFont(coerce, 'outsidetextfont', textFont);
    //     coerce('constraintext');
    //     coerce('selected.textfont.color');
    //     coerce('unselected.textfont.color');
    //     coerce('cliponaxis');
    // }

    handleStyleDefaults(traceIn, traceOut, coerce, defaultColor, layout);

    Lib.coerceSelectionMarkerOpacity(traceOut, coerce);
};
