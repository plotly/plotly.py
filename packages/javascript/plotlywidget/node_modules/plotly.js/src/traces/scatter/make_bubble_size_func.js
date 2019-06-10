/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isNumeric = require('fast-isnumeric');


// used in the drawing step for 'scatter' and 'scattegeo' and
// in the convert step for 'scatter3d'
module.exports = function makeBubbleSizeFn(trace) {
    var marker = trace.marker;
    var sizeRef = marker.sizeref || 1;
    var sizeMin = marker.sizemin || 0;

    // for bubble charts, allow scaling the provided value linearly
    // and by area or diameter.
    // Note this only applies to the array-value sizes

    var baseFn = (marker.sizemode === 'area') ?
        function(v) { return Math.sqrt(v / sizeRef); } :
        function(v) { return v / sizeRef; };

    // TODO add support for position/negative bubbles?
    // TODO add 'sizeoffset' attribute?
    return function(v) {
        var baseSize = baseFn(v / 2);

        // don't show non-numeric and negative sizes
        return (isNumeric(baseSize) && (baseSize > 0)) ?
            Math.max(baseSize, sizeMin) :
            0;
    };
};
