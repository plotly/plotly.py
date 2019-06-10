/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');

var attributes = require('./attributes');
var constants = require('./constants');

var name = constants.name;
var stepAttrs = attributes.steps;


module.exports = function slidersDefaults(layoutIn, layoutOut) {
    handleArrayContainerDefaults(layoutIn, layoutOut, {
        name: name,
        handleItemDefaults: sliderDefaults
    });
};

function sliderDefaults(sliderIn, sliderOut, layoutOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(sliderIn, sliderOut, attributes, attr, dflt);
    }

    var steps = handleArrayContainerDefaults(sliderIn, sliderOut, {
        name: 'steps',
        handleItemDefaults: stepDefaults
    });

    var stepCount = 0;
    for(var i = 0; i < steps.length; i++) {
        if(steps[i].visible) stepCount++;
    }

    var visible;
    // If it has fewer than two options, it's not really a slider
    if(stepCount < 2) visible = sliderOut.visible = false;
    else visible = coerce('visible');
    if(!visible) return;

    sliderOut._stepCount = stepCount;
    var visSteps = sliderOut._visibleSteps = Lib.filterVisible(steps);

    var active = coerce('active');
    if(!(steps[active] || {}).visible) sliderOut.active = visSteps[0]._index;

    coerce('x');
    coerce('y');
    Lib.noneOrAll(sliderIn, sliderOut, ['x', 'y']);

    coerce('xanchor');
    coerce('yanchor');

    coerce('len');
    coerce('lenmode');

    coerce('pad.t');
    coerce('pad.r');
    coerce('pad.b');
    coerce('pad.l');

    Lib.coerceFont(coerce, 'font', layoutOut.font);

    var currentValueIsVisible = coerce('currentvalue.visible');

    if(currentValueIsVisible) {
        coerce('currentvalue.xanchor');
        coerce('currentvalue.prefix');
        coerce('currentvalue.suffix');
        coerce('currentvalue.offset');

        Lib.coerceFont(coerce, 'currentvalue.font', sliderOut.font);
    }

    coerce('transition.duration');
    coerce('transition.easing');

    coerce('bgcolor');
    coerce('activebgcolor');
    coerce('bordercolor');
    coerce('borderwidth');
    coerce('ticklen');
    coerce('tickwidth');
    coerce('tickcolor');
    coerce('minorticklen');
}

function stepDefaults(valueIn, valueOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(valueIn, valueOut, stepAttrs, attr, dflt);
    }

    var visible;
    if(valueIn.method !== 'skip' && !Array.isArray(valueIn.args)) {
        visible = valueOut.visible = false;
    } else visible = coerce('visible');

    if(visible) {
        coerce('method');
        coerce('args');
        var label = coerce('label', 'step-' + valueOut._index);
        coerce('value', label);
        coerce('execute');
    }
}
