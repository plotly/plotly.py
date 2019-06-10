/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';
var isNumeric = require('fast-isnumeric');

var handleLabelDefaults = require('./label_defaults');

var Color = require('../../components/color');
var addOpacity = Color.addOpacity;
var opacity = Color.opacity;

var filterOps = require('../../constants/filter_ops');
var CONSTRAINT_REDUCTION = filterOps.CONSTRAINT_REDUCTION;
var COMPARISON_OPS2 = filterOps.COMPARISON_OPS2;

module.exports = function handleConstraintDefaults(traceIn, traceOut, coerce, layout, defaultColor, opts) {
    var contours = traceOut.contours;
    var showLines, lineColor, fillColor;

    var operation = coerce('contours.operation');
    contours._operation = CONSTRAINT_REDUCTION[operation];

    handleConstraintValueDefaults(coerce, contours);

    if(operation === '=') {
        showLines = contours.showlines = true;
    } else {
        showLines = coerce('contours.showlines');
        fillColor = coerce('fillcolor', addOpacity(
            (traceIn.line || {}).color || defaultColor, 0.5
        ));
    }

    if(showLines) {
        var lineDfltColor = fillColor && opacity(fillColor) ?
            addOpacity(traceOut.fillcolor, 1) :
            defaultColor;
        lineColor = coerce('line.color', lineDfltColor);
        coerce('line.width', 2);
        coerce('line.dash');
    }

    coerce('line.smoothing');

    handleLabelDefaults(coerce, layout, lineColor, opts);
};

function handleConstraintValueDefaults(coerce, contours) {
    var zvalue;

    if(COMPARISON_OPS2.indexOf(contours.operation) === -1) {
        // Requires an array of two numbers:
        coerce('contours.value', [0, 1]);

        if(!Array.isArray(contours.value)) {
            if(isNumeric(contours.value)) {
                zvalue = parseFloat(contours.value);
                contours.value = [zvalue, zvalue + 1];
            }
        } else if(contours.value.length > 2) {
            contours.value = contours.value.slice(2);
        } else if(contours.length === 0) {
            contours.value = [0, 1];
        } else if(contours.length < 2) {
            zvalue = parseFloat(contours.value[0]);
            contours.value = [zvalue, zvalue + 1];
        } else {
            contours.value = [
                parseFloat(contours.value[0]),
                parseFloat(contours.value[1])
            ];
        }
    } else {
        // Requires a single scalar:
        coerce('contours.value', 0);

        if(!isNumeric(contours.value)) {
            if(Array.isArray(contours.value)) {
                contours.value = parseFloat(contours.value[0]);
            } else {
                contours.value = 0;
            }
        }
    }
}
