/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scatterAttrs = require('../../../traces/scatter/attributes');
var scatterMarkerAttrs = scatterAttrs.marker;
var extendFlat = require('../../../lib/extend').extendFlat;

var deprecationWarning = [
    'Area traces are deprecated!',
    'Please switch to the *barpolar* trace type.'
].join(' ');

module.exports = {
    r: extendFlat({}, scatterAttrs.r, {
        description: [
            deprecationWarning,
            'Sets the radial coordinates',
            'for legacy polar chart only.'
        ].join(' ')
    }),
    t: extendFlat({}, scatterAttrs.t, {
        description: [
            deprecationWarning,
            'Sets the angular coordinates',
            'for legacy polar chart only.'
        ].join(' ')
    }),
    marker: {
        color: extendFlat({}, scatterMarkerAttrs.color, {
            description: [
                deprecationWarning,
                scatterMarkerAttrs.color.description
            ].join(' ')
        }),
        size: extendFlat({}, scatterMarkerAttrs.size, {
            description: [
                deprecationWarning,
                scatterMarkerAttrs.size.description
            ].join(' ')
        }),
        symbol: extendFlat({}, scatterMarkerAttrs.symbol, {
            description: [
                deprecationWarning,
                scatterMarkerAttrs.symbol.description
            ].join(' ')
        }),
        opacity: extendFlat({}, scatterMarkerAttrs.opacity, {
            description: [
                deprecationWarning,
                scatterMarkerAttrs.opacity.description
            ].join(' ')
        }),
        editType: 'calc'
    }
};
