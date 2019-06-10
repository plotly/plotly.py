/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var layoutAttributes = require('./layout_attributes');

module.exports = function(layoutIn, layoutOut, fullData) {
    var hasTraceType = false;

    function coerce(attr, dflt) {
        return Lib.coerce(layoutIn, layoutOut, layoutAttributes, attr, dflt);
    }

    for(var i = 0; i < fullData.length; i++) {
        var trace = fullData[i];

        if(trace.visible && trace.type === 'funnel') {
            hasTraceType = true;
            break;
        }
    }

    if(hasTraceType) {
        coerce('funnelmode');
        coerce('funnelgap', 0.2);
        coerce('funnelgroupgap');
    }
};
