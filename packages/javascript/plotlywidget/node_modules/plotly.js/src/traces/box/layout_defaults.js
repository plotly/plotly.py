/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');
var layoutAttributes = require('./layout_attributes');

function _supply(layoutIn, layoutOut, fullData, coerce, traceType) {
    var category = traceType + 'Layout';
    var hasTraceType = false;

    for(var i = 0; i < fullData.length; i++) {
        var trace = fullData[i];

        if(Registry.traceIs(trace, category)) {
            hasTraceType = true;
            break;
        }
    }
    if(!hasTraceType) return;

    coerce(traceType + 'mode');
    coerce(traceType + 'gap');
    coerce(traceType + 'groupgap');
}

function supplyLayoutDefaults(layoutIn, layoutOut, fullData) {
    function coerce(attr, dflt) {
        return Lib.coerce(layoutIn, layoutOut, layoutAttributes, attr, dflt);
    }
    _supply(layoutIn, layoutOut, fullData, coerce, 'box');
}

module.exports = {
    supplyLayoutDefaults: supplyLayoutDefaults,
    _supply: _supply
};
