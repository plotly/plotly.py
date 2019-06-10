/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Color = require('../../components/color');
var Registry = require('../../registry');

var handleXYDefaults = require('../scatter/xy_defaults');
var handleStyleDefaults = require('./style_defaults');
var getAxisGroup = require('../../plots/cartesian/axis_ids').getAxisGroup;
var attributes = require('./attributes');

var coerceFont = Lib.coerceFont;

function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var len = handleXYDefaults(traceIn, traceOut, layout, coerce);
    if(!len) {
        traceOut.visible = false;
        return;
    }

    coerce('orientation', (traceOut.x && !traceOut.y) ? 'h' : 'v');
    coerce('base');
    coerce('offset');
    coerce('width');

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    var textposition = coerce('textposition');
    handleText(traceIn, traceOut, layout, coerce, textposition, {
        moduleHasSelected: true,
        moduleHasUnselected: true,
        moduleHasConstrain: true,
        moduleHasCliponaxis: true,
        moduleHasTextangle: true,
        moduleHasInsideanchor: true
    });

    handleStyleDefaults(traceIn, traceOut, coerce, defaultColor, layout);

    var lineColor = (traceOut.marker.line || {}).color;

    // override defaultColor for error bars with defaultLine
    var errorBarsSupplyDefaults = Registry.getComponentMethod('errorbars', 'supplyDefaults');
    errorBarsSupplyDefaults(traceIn, traceOut, lineColor || Color.defaultLine, {axis: 'y'});
    errorBarsSupplyDefaults(traceIn, traceOut, lineColor || Color.defaultLine, {axis: 'x', inherit: 'y'});

    Lib.coerceSelectionMarkerOpacity(traceOut, coerce);
}

function handleGroupingDefaults(traceIn, traceOut, fullLayout, coerce) {
    var orientation = traceOut.orientation;
    // N.B. grouping is done across all trace types that support it
    var posAxId = traceOut[{v: 'x', h: 'y'}[orientation] + 'axis'];
    var groupId = getAxisGroup(fullLayout, posAxId) + orientation;

    var alignmentOpts = fullLayout._alignmentOpts || {};
    var alignmentgroup = coerce('alignmentgroup');

    var alignmentGroups = alignmentOpts[groupId];
    if(!alignmentGroups) alignmentGroups = alignmentOpts[groupId] = {};

    var alignmentGroupOpts = alignmentGroups[alignmentgroup];

    if(alignmentGroupOpts) {
        alignmentGroupOpts.traces.push(traceOut);
    } else {
        alignmentGroupOpts = alignmentGroups[alignmentgroup] = {
            traces: [traceOut],
            alignmentIndex: Object.keys(alignmentGroups).length,
            offsetGroups: {}
        };
    }

    var offsetgroup = coerce('offsetgroup');
    var offsetGroups = alignmentGroupOpts.offsetGroups;
    var offsetGroupOpts = offsetGroups[offsetgroup];

    if(offsetgroup) {
        if(!offsetGroupOpts) {
            offsetGroupOpts = offsetGroups[offsetgroup] = {
                offsetIndex: Object.keys(offsetGroups).length
            };
        }

        traceOut._offsetIndex = offsetGroupOpts.offsetIndex;
    }
}

function crossTraceDefaults(fullData, fullLayout) {
    var traceIn, traceOut;

    function coerce(attr) {
        return Lib.coerce(traceOut._input, traceOut, attributes, attr);
    }

    if(fullLayout.barmode === 'group') {
        for(var i = 0; i < fullData.length; i++) {
            traceOut = fullData[i];

            if(traceOut.type === 'bar') {
                traceIn = traceOut._input;
                handleGroupingDefaults(traceIn, traceOut, fullLayout, coerce);
            }
        }
    }
}

function handleText(traceIn, traceOut, layout, coerce, textposition, opts) {
    opts = opts || {};
    var moduleHasSelected = !(opts.moduleHasSelected === false);
    var moduleHasUnselected = !(opts.moduleHasUnselected === false);
    var moduleHasConstrain = !(opts.moduleHasConstrain === false);
    var moduleHasCliponaxis = !(opts.moduleHasCliponaxis === false);
    var moduleHasTextangle = !(opts.moduleHasTextangle === false);
    var moduleHasInsideanchor = !(opts.moduleHasInsideanchor === false);

    var hasBoth = Array.isArray(textposition) || textposition === 'auto';
    var hasInside = hasBoth || textposition === 'inside';
    var hasOutside = hasBoth || textposition === 'outside';

    if(hasInside || hasOutside) {
        var dfltFont = coerceFont(coerce, 'textfont', layout.font);

        // Note that coercing `insidetextfont` is always needed –
        // even if `textposition` is `outside` for each trace – since
        // an outside label can become an inside one, for example because
        // of a bar being stacked on top of it.
        var insideTextFontDefault = Lib.extendFlat({}, dfltFont);
        var isTraceTextfontColorSet = traceIn.textfont && traceIn.textfont.color;
        var isColorInheritedFromLayoutFont = !isTraceTextfontColorSet;
        if(isColorInheritedFromLayoutFont) {
            delete insideTextFontDefault.color;
        }
        coerceFont(coerce, 'insidetextfont', insideTextFontDefault);

        if(hasOutside) coerceFont(coerce, 'outsidetextfont', dfltFont);


        if(moduleHasSelected) coerce('selected.textfont.color');
        if(moduleHasUnselected) coerce('unselected.textfont.color');
        if(moduleHasConstrain) coerce('constraintext');
        if(moduleHasCliponaxis) coerce('cliponaxis');
        if(moduleHasTextangle) coerce('textangle');
    }

    if(hasInside) {
        if(moduleHasInsideanchor) coerce('insidetextanchor');
    }
}

module.exports = {
    supplyDefaults: supplyDefaults,
    crossTraceDefaults: crossTraceDefaults,
    handleGroupingDefaults: handleGroupingDefaults,
    handleText: handleText
};
