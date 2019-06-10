/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../lib');

module.exports = {
    hasLines: function(trace) {
        return trace.visible && trace.mode &&
            trace.mode.indexOf('lines') !== -1;
    },

    hasMarkers: function(trace) {
        return trace.visible && (
            (trace.mode && trace.mode.indexOf('markers') !== -1) ||
            // until splom implements 'mode'
            trace.type === 'splom'
        );
    },

    hasText: function(trace) {
        return trace.visible && trace.mode &&
            trace.mode.indexOf('text') !== -1;
    },

    isBubble: function(trace) {
        return Lib.isPlainObject(trace.marker) &&
            Lib.isArrayOrTypedArray(trace.marker.size);
    }
};
