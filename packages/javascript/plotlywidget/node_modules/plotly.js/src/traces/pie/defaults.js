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
var handleDomainDefaults = require('../../plots/domain').defaults;
var handleText = require('../bar/defaults').handleText;

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var len;
    var vals = coerce('values');
    var hasVals = Lib.isArrayOrTypedArray(vals);
    var labels = coerce('labels');
    if(Array.isArray(labels)) {
        len = labels.length;
        if(hasVals) len = Math.min(len, vals.length);
    } else if(hasVals) {
        len = vals.length;

        coerce('label0');
        coerce('dlabel');
    }

    if(!len) {
        traceOut.visible = false;
        return;
    }
    traceOut._length = len;

    var lineWidth = coerce('marker.line.width');
    if(lineWidth) coerce('marker.line.color');

    coerce('marker.colors');

    coerce('scalegroup');
    // TODO: hole needs to be coerced to the same value within a scaleegroup

    var textData = coerce('text');
    var textInfo = coerce('textinfo', Array.isArray(textData) ? 'text+percent' : 'percent');
    coerce('hovertext');
    coerce('hovertemplate');

    if(textInfo && textInfo !== 'none') {
        var textposition = coerce('textposition');
        handleText(traceIn, traceOut, layout, coerce, textposition, {
            moduleHasSelected: false,
            moduleHasUnselected: false,
            moduleHasConstrain: false,
            moduleHasCliponaxis: false,
            moduleHasTextangle: false,
            moduleHasInsideanchor: false
        });
    }

    handleDomainDefaults(traceOut, layout, coerce);

    var hole = coerce('hole');
    var title = coerce('title.text');
    if(title) {
        var titlePosition = coerce('title.position', hole ? 'middle center' : 'top center');
        if(!hole && titlePosition === 'middle center') traceOut.title.position = 'top center';
        Lib.coerceFont(coerce, 'title.font', layout.font);
    }

    coerce('sort');
    coerce('direction');
    coerce('rotation');
    coerce('pull');
};
