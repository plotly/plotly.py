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

var INCREASING_COLOR = '#3D9970';
var DECREASING_COLOR = '#FF4136';
var TOTALS_COLOR = '#4499FF';

function handleDirection(coerce, direction, defaultColor) {
    coerce(direction + '.marker.color', defaultColor);
    coerce(direction + '.marker.line.color', Color.defaultLine);
    coerce(direction + '.marker.line.width');
}

function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var len = handleXYDefaults(traceIn, traceOut, layout, coerce);
    if(!len) {
        traceOut.visible = false;
        return;
    }

    coerce('measure');

    coerce('orientation', (traceOut.x && !traceOut.y) ? 'h' : 'v');
    coerce('base');
    coerce('offset');
    coerce('width');

    coerce('text');

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
        coerce('textinfo');
    }

    handleDirection(coerce, 'increasing', INCREASING_COLOR);
    handleDirection(coerce, 'decreasing', DECREASING_COLOR);
    handleDirection(coerce, 'totals', TOTALS_COLOR);

    var connectorVisible = coerce('connector.visible');
    if(connectorVisible) {
        coerce('connector.mode');
        var connectorLineWidth = coerce('connector.line.width');
        if(connectorLineWidth) {
            coerce('connector.line.color');
            coerce('connector.line.dash');
        }
    }
}

function crossTraceDefaults(fullData, fullLayout) {
    var traceIn, traceOut;

    function coerce(attr) {
        return Lib.coerce(traceOut._input, traceOut, attributes, attr);
    }

    if(fullLayout.waterfallmode === 'group') {
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
