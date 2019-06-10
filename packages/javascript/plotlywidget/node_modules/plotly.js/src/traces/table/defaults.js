/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var attributes = require('./attributes');
var handleDomainDefaults = require('../../plots/domain').defaults;

function defaultColumnOrder(traceOut, coerce) {
    var specifiedColumnOrder = traceOut.columnorder || [];
    var commonLength = traceOut.header.values.length;
    var truncated = specifiedColumnOrder.slice(0, commonLength);
    var sorted = truncated.slice().sort(function(a, b) {return a - b;});
    var oneStepped = truncated.map(function(d) {return sorted.indexOf(d);});
    for(var i = oneStepped.length; i < commonLength; i++) {
        oneStepped.push(i);
    }
    coerce('columnorder', oneStepped);
}

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    handleDomainDefaults(traceOut, layout, coerce);

    coerce('columnwidth');

    coerce('header.values');
    coerce('header.format');
    coerce('header.align');

    coerce('header.prefix');
    coerce('header.suffix');
    coerce('header.height');
    coerce('header.line.width');
    coerce('header.line.color');
    coerce('header.fill.color');
    Lib.coerceFont(coerce, 'header.font', Lib.extendFlat({}, layout.font));

    defaultColumnOrder(traceOut, coerce);

    coerce('cells.values');
    coerce('cells.format');
    coerce('cells.align');
    coerce('cells.prefix');
    coerce('cells.suffix');
    coerce('cells.height');
    coerce('cells.line.width');
    coerce('cells.line.color');
    coerce('cells.fill.color');
    Lib.coerceFont(coerce, 'cells.font', Lib.extendFlat({}, layout.font));

    // disable 1D transforms
    traceOut._length = null;
};
