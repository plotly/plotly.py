/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');
var toLogRange = require('../../lib/to_log_range');

/*
 * convertCoords: when converting an axis between log and linear
 * you need to alter any annotations on that axis to keep them
 * pointing at the same data point.
 * In v2.0 this will become obsolete
 *
 * gd: the plot div
 * ax: the axis being changed
 * newType: the type it's getting
 * doExtra: function(attr, val) from inside relayout that sets the attribute.
 *     Use this to make the changes as it's aware if any other changes in the
 *     same relayout call should override this conversion.
 */
module.exports = function convertCoords(gd, ax, newType, doExtra) {
    ax = ax || {};

    var toLog = (newType === 'log') && (ax.type === 'linear');
    var fromLog = (newType === 'linear') && (ax.type === 'log');

    if(!(toLog || fromLog)) return;

    var annotations = gd._fullLayout.annotations;
    var axLetter = ax._id.charAt(0);
    var ann;
    var attrPrefix;

    function convert(attr) {
        var currentVal = ann[attr];
        var newVal = null;

        if(toLog) newVal = toLogRange(currentVal, ax.range);
        else newVal = Math.pow(10, currentVal);

        // if conversion failed, delete the value so it gets a default value
        if(!isNumeric(newVal)) newVal = null;

        doExtra(attrPrefix + attr, newVal);
    }

    for(var i = 0; i < annotations.length; i++) {
        ann = annotations[i];
        attrPrefix = 'annotations[' + i + '].';

        if(ann[axLetter + 'ref'] === ax._id) convert(axLetter);
        if(ann['a' + axLetter + 'ref'] === ax._id) convert('a' + axLetter);
    }
};
