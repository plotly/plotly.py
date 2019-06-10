/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var Color = require('../color');
var Template = require('../../plot_api/plot_template');
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');

var attributes = require('./attributes');
var constants = require('./constants');


module.exports = function handleDefaults(containerIn, containerOut, layout, counterAxes, calendar) {
    var selectorIn = containerIn.rangeselector || {};
    var selectorOut = Template.newContainer(containerOut, 'rangeselector');

    function coerce(attr, dflt) {
        return Lib.coerce(selectorIn, selectorOut, attributes, attr, dflt);
    }

    var buttons = handleArrayContainerDefaults(selectorIn, selectorOut, {
        name: 'buttons',
        handleItemDefaults: buttonDefaults,
        calendar: calendar
    });

    var visible = coerce('visible', buttons.length > 0);
    if(visible) {
        var posDflt = getPosDflt(containerOut, layout, counterAxes);
        coerce('x', posDflt[0]);
        coerce('y', posDflt[1]);
        Lib.noneOrAll(containerIn, containerOut, ['x', 'y']);

        coerce('xanchor');
        coerce('yanchor');

        Lib.coerceFont(coerce, 'font', layout.font);

        var bgColor = coerce('bgcolor');
        coerce('activecolor', Color.contrast(bgColor, constants.lightAmount, constants.darkAmount));
        coerce('bordercolor');
        coerce('borderwidth');
    }
};

function buttonDefaults(buttonIn, buttonOut, selectorOut, opts) {
    var calendar = opts.calendar;

    function coerce(attr, dflt) {
        return Lib.coerce(buttonIn, buttonOut, attributes.buttons, attr, dflt);
    }

    var visible = coerce('visible');

    if(visible) {
        var step = coerce('step');
        if(step !== 'all') {
            if(calendar && calendar !== 'gregorian' && (step === 'month' || step === 'year')) {
                buttonOut.stepmode = 'backward';
            } else {
                coerce('stepmode');
            }

            coerce('count');
        }

        coerce('label');
    }
}

function getPosDflt(containerOut, layout, counterAxes) {
    var anchoredList = counterAxes.filter(function(ax) {
        return layout[ax].anchor === containerOut._id;
    });

    var posY = 0;
    for(var i = 0; i < anchoredList.length; i++) {
        var domain = layout[anchoredList[i]].domain;
        if(domain) posY = Math.max(domain[1], posY);
    }

    return [containerOut.domain[0], posY + constants.yPad];
}
