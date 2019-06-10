/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var extendFlat = require('../../lib').extendFlat;
var OHLCattrs = require('../ohlc/attributes');
var boxAttrs = require('../box/attributes');

function directionAttrs(lineColorDefault) {
    return {
        line: {
            color: extendFlat({}, boxAttrs.line.color, {dflt: lineColorDefault}),
            width: boxAttrs.line.width,
            editType: 'style'
        },

        fillcolor: boxAttrs.fillcolor,
        editType: 'style'
    };
}

module.exports = {
    x: OHLCattrs.x,
    open: OHLCattrs.open,
    high: OHLCattrs.high,
    low: OHLCattrs.low,
    close: OHLCattrs.close,

    line: {
        width: extendFlat({}, boxAttrs.line.width, {
            description: [
                boxAttrs.line.width.description,
                'Note that this style setting can also be set per',
                'direction via `increasing.line.width` and',
                '`decreasing.line.width`.'
            ].join(' ')
        }),
        editType: 'style'
    },

    increasing: directionAttrs(OHLCattrs.increasing.line.color.dflt),

    decreasing: directionAttrs(OHLCattrs.decreasing.line.color.dflt),

    text: OHLCattrs.text,
    hovertext: OHLCattrs.hovertext,
    whiskerwidth: extendFlat({}, boxAttrs.whiskerwidth, { dflt: 0 }),

    hoverlabel: OHLCattrs.hoverlabel,
};
