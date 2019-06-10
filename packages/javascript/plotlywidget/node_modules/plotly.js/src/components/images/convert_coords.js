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
 * you need to alter any images on that axis to keep them
 * pointing at the same data point.
 * In v2.0 this will become obsolete (or perhaps size will still need conversion?)
 * we convert size by declaring that the maximum extent *in data units* should be
 * the same, assuming the image is anchored by its center (could remove that restriction
 * if we think it's important) even though the actual left and right values will not be
 * quite the same since the scale becomes nonlinear (and central anchor means the pixel
 * center of the image, not the data units center)
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

    var images = gd._fullLayout.images;
    var axLetter = ax._id.charAt(0);
    var image;
    var attrPrefix;

    for(var i = 0; i < images.length; i++) {
        image = images[i];
        attrPrefix = 'images[' + i + '].';

        if(image[axLetter + 'ref'] === ax._id) {
            var currentPos = image[axLetter];
            var currentSize = image['size' + axLetter];
            var newPos = null;
            var newSize = null;

            if(toLog) {
                newPos = toLogRange(currentPos, ax.range);

                // this is the inverse of the conversion we do in fromLog below
                // so that the conversion is reversible (notice the fromLog conversion
                // is like sinh, and this one looks like arcsinh)
                var dx = currentSize / Math.pow(10, newPos) / 2;
                newSize = 2 * Math.log(dx + Math.sqrt(1 + dx * dx)) / Math.LN10;
            } else {
                newPos = Math.pow(10, currentPos);
                newSize = newPos * (Math.pow(10, currentSize / 2) - Math.pow(10, -currentSize / 2));
            }

            // if conversion failed, delete the value so it can get a default later on
            if(!isNumeric(newPos)) {
                newPos = null;
                newSize = null;
            } else if(!isNumeric(newSize)) newSize = null;

            doExtra(attrPrefix + axLetter, newPos);
            doExtra(attrPrefix + 'size' + axLetter, newSize);
        }
    }
};
