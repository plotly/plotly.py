/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var colorMix = require('tinycolor2').mix;

var Lib = require('../../../lib');
var Template = require('../../../plot_api/plot_template');

var layoutAttributes = require('./axis_attributes');
var handleTypeDefaults = require('../../cartesian/type_defaults');
var handleAxisDefaults = require('../../cartesian/axis_defaults');

var axesNames = ['xaxis', 'yaxis', 'zaxis'];

// TODO: hard-coded lightness fraction based on gridline default colors
// that differ from other subplot types.
var gridLightness = 100 * (204 - 0x44) / (255 - 0x44);

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut, options) {
    var containerIn, containerOut;

    function coerce(attr, dflt) {
        return Lib.coerce(containerIn, containerOut, layoutAttributes, attr, dflt);
    }

    for(var j = 0; j < axesNames.length; j++) {
        var axName = axesNames[j];
        containerIn = layoutIn[axName] || {};

        containerOut = Template.newContainer(layoutOut, axName);
        containerOut._id = axName[0] + options.scene;
        containerOut._name = axName;

        handleTypeDefaults(containerIn, containerOut, coerce, options);

        handleAxisDefaults(
            containerIn,
            containerOut,
            coerce,
            {
                font: options.font,
                letter: axName[0],
                data: options.data,
                showGrid: true,
                noTickson: true,
                bgColor: options.bgColor,
                calendar: options.calendar
            },
            options.fullLayout);

        coerce('gridcolor', colorMix(containerOut.color, options.bgColor, gridLightness).toRgbString());
        coerce('title.text', axName[0]);  // shouldn't this be on-par with 2D?

        containerOut.setScale = Lib.noop;

        if(coerce('showspikes')) {
            coerce('spikesides');
            coerce('spikethickness');
            coerce('spikecolor', containerOut.color);
        }

        coerce('showaxeslabels');
        if(coerce('showbackground')) coerce('backgroundcolor');
    }
};
