/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');

var handleGroupingDefaults = require('../bar/defaults').handleGroupingDefaults;
var handleText = require('../bar/defaults').handleText;
var handleXYDefaults = require('../scatter/xy_defaults');
var attributes = require('./attributes');
var Color = require('../../components/color');

function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var len = handleXYDefaults(traceIn, traceOut, layout, coerce);
    if(!len) {
        traceOut.visible = false;
        return;
    }

    coerce('orientation', (traceOut.y && !traceOut.x) ? 'v' : 'h');
    coerce('offset');
    coerce('width');

    var text = coerce('text');

    coerce('hovertext');
    coerce('hovertemplate');

    var textposition = coerce('textposition');
    handleText(traceIn, traceOut, layout, coerce, textposition, {
        moduleHasSelected: false,
        moduleHasUnselected: false,
        moduleHasConstrain: true,
        moduleHasCliponaxis: true,
        moduleHasTextangle: true,
        moduleHasInsideanchor: true
    });

    if(traceOut.textposition !== 'none') {
        coerce('textinfo', Array.isArray(text) ? 'text+value' : 'value');
    }

    var markerColor = coerce('marker.color', defaultColor);
    coerce('marker.line.color', Color.defaultLine);
    coerce('marker.line.width');

    var connectorVisible = coerce('connector.visible');
    if(connectorVisible) {
        coerce('connector.fillcolor', defaultFillColor(markerColor));

        var connectorLineWidth = coerce('connector.line.width');
        if(connectorLineWidth) {
            coerce('connector.line.color');
            coerce('connector.line.dash');
        }
    }
}

function defaultFillColor(markerColor) {
    var cBase = Lib.isArrayOrTypedArray(markerColor) ? '#000' : markerColor;

    return Color.addOpacity(cBase, 0.5 * Color.opacity(cBase));
}

function crossTraceDefaults(fullData, fullLayout) {
    var traceIn, traceOut;

    function coerce(attr) {
        return Lib.coerce(traceOut._input, traceOut, attributes, attr);
    }

    if(fullLayout.funnelmode === 'group') {
        for(var i = 0; i < fullData.length; i++) {
            traceOut = fullData[i];
            traceIn = traceOut._input;

            handleGroupingDefaults(traceIn, traceOut, fullLayout, coerce);
        }
    }
}

module.exports = {
    supplyDefaults: supplyDefaults,
    crossTraceDefaults: crossTraceDefaults
};
