/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');

var attributes = require('./attributes');
var subTypes = require('../scatter/subtypes');
var handleMarkerDefaults = require('../scatter/marker_defaults');
var mergeLength = require('../parcoords/merge_length');
var OPEN_RE = /-open/;

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var dimensions = handleArrayContainerDefaults(traceIn, traceOut, {
        name: 'dimensions',
        handleItemDefaults: dimensionDefaults
    });

    var showDiag = coerce('diagonal.visible');
    var showUpper = coerce('showupperhalf');
    var showLower = coerce('showlowerhalf');

    var dimLength = mergeLength(traceOut, dimensions, 'values');

    if(!dimLength || (!showDiag && !showUpper && !showLower)) {
        traceOut.visible = false;
        return;
    }

    coerce('text');
    coerce('hovertext');
    coerce('hovertemplate');

    handleMarkerDefaults(traceIn, traceOut, defaultColor, layout, coerce);

    var isOpen = OPEN_RE.test(traceOut.marker.symbol);
    var isBubble = subTypes.isBubble(traceOut);
    coerce('marker.line.width', isOpen || isBubble ? 1 : 0);

    handleAxisDefaults(traceIn, traceOut, layout, coerce);

    Lib.coerceSelectionMarkerOpacity(traceOut, coerce);
};

function dimensionDefaults(dimIn, dimOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(dimIn, dimOut, attributes.dimensions, attr, dflt);
    }

    coerce('label');
    var values = coerce('values');

    if(!(values && values.length)) dimOut.visible = false;
    else coerce('visible');

    coerce('axis.type');
    coerce('axis.matches');
}

function handleAxisDefaults(traceIn, traceOut, layout, coerce) {
    var dimensions = traceOut.dimensions;
    var dimLength = dimensions.length;
    var showUpper = traceOut.showupperhalf;
    var showLower = traceOut.showlowerhalf;
    var showDiag = traceOut.diagonal.visible;
    var i, j;

    var xAxesDflt = new Array(dimLength);
    var yAxesDflt = new Array(dimLength);

    for(i = 0; i < dimLength; i++) {
        var suffix = i ? i + 1 : '';
        xAxesDflt[i] = 'x' + suffix;
        yAxesDflt[i] = 'y' + suffix;
    }

    var xaxes = coerce('xaxes', xAxesDflt);
    var yaxes = coerce('yaxes', yAxesDflt);

    // build list of [x,y] axis corresponding to each dimensions[i],
    // very useful for passing options to regl-splom
    var diag = traceOut._diag = new Array(dimLength);

    // lookup for 'drawn' x|y axes, to avoid costly indexOf downstream
    traceOut._xaxes = {};
    traceOut._yaxes = {};

    // list of 'drawn' x|y axes, use to generate list of subplots
    var xList = [];
    var yList = [];

    function fillAxisStashes(axId, counterAxId, dim, list) {
        if(!axId) return;

        var axLetter = axId.charAt(0);
        var stash = layout._splomAxes[axLetter];

        traceOut['_' + axLetter + 'axes'][axId] = 1;
        list.push(axId);

        if(!(axId in stash)) {
            var s = stash[axId] = {};
            if(dim) {
                s.label = dim.label || '';
                if(dim.visible && dim.axis) {
                    if(dim.axis.type) s.type = dim.axis.type;
                    if(dim.axis.matches) s.matches = counterAxId;
                }
            }
        }
    }

    // cases where showDiag and showLower or showUpper are false
    // no special treatment as the 'drawn' x-axes and y-axes no longer match
    // the dimensions items and xaxes|yaxes 1-to-1
    var mustShiftX = !showDiag && !showLower;
    var mustShiftY = !showDiag && !showUpper;

    traceOut._axesDim = {};
    for(i = 0; i < dimLength; i++) {
        var dim = dimensions[i];
        var i0 = i === 0;
        var iN = i === dimLength - 1;

        var xaId = (i0 && mustShiftX) || (iN && mustShiftY) ?
            undefined :
            xaxes[i];

        var yaId = (i0 && mustShiftY) || (iN && mustShiftX) ?
            undefined :
            yaxes[i];

        fillAxisStashes(xaId, yaId, dim, xList);
        fillAxisStashes(yaId, xaId, dim, yList);
        diag[i] = [xaId, yaId];
        traceOut._axesDim[xaId] = i;
        traceOut._axesDim[yaId] = i;
    }

    // fill in splom subplot keys
    for(i = 0; i < xList.length; i++) {
        for(j = 0; j < yList.length; j++) {
            var id = xList[i] + yList[j];

            if(i > j && showUpper) {
                layout._splomSubplots[id] = 1;
            } else if(i < j && showLower) {
                layout._splomSubplots[id] = 1;
            } else if(i === j && (showDiag || !showLower || !showUpper)) {
                // need to include diagonal subplots when
                // hiding one half and the diagonal
                layout._splomSubplots[id] = 1;
            }
        }
    }

    // when lower half is omitted, or when just the diagonal is gone,
    // override grid default to make sure axes remain on
    // the left/bottom of the plot area
    if(!showLower || (!showDiag && showUpper && showLower)) {
        layout._splomGridDflt.xside = 'bottom';
        layout._splomGridDflt.yside = 'left';
    }
}
