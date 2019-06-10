/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Template = require('../../plot_api/plot_template');

var colorScaleAttrs = require('./layout_attributes');
var colorScaleDefaults = require('./defaults');

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(layoutIn, layoutOut, colorScaleAttrs, attr, dflt);
    }

    coerce('colorscale.sequential');
    coerce('colorscale.sequentialminus');
    coerce('colorscale.diverging');

    var colorAxes = layoutOut._colorAxes;
    var colorAxIn, colorAxOut;

    function coerceAx(attr, dflt) {
        return Lib.coerce(colorAxIn, colorAxOut, colorScaleAttrs.coloraxis, attr, dflt);
    }

    for(var k in colorAxes) {
        var stash = colorAxes[k];

        if(stash[0]) {
            colorAxIn = layoutIn[k] || {};
            colorAxOut = Template.newContainer(layoutOut, k, 'coloraxis');
            colorAxOut._name = k;
            colorScaleDefaults(colorAxIn, colorAxOut, layoutOut, coerceAx, {prefix: '', cLetter: 'c'});
        } else {
            // re-coerce colorscale attributes w/o coloraxis
            for(var i = 0; i < stash[2].length; i++) {
                stash[2][i]();
            }
            delete layoutOut._colorAxes[k];
        }
    }
};
