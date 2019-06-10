/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var fontAttrs = require('../../plots/font_attributes');
var hoverLabelAttrs = require('./layout_attributes').hoverlabel;
var extendFlat = require('../../lib/extend').extendFlat;

module.exports = {
    hoverlabel: {
        bgcolor: extendFlat({}, hoverLabelAttrs.bgcolor, {
            arrayOk: true,
            description: 'Sets the background color of the hover labels for this trace'
        }),
        bordercolor: extendFlat({}, hoverLabelAttrs.bordercolor, {
            arrayOk: true,
            description: 'Sets the border color of the hover labels for this trace.'
        }),
        font: fontAttrs({
            arrayOk: true,
            editType: 'none',
            description: 'Sets the font used in hover labels.'
        }),
        align: extendFlat({}, hoverLabelAttrs.align, {arrayOk: true}),
        namelength: extendFlat({}, hoverLabelAttrs.namelength, {arrayOk: true}),
        editType: 'none'
    }
};
