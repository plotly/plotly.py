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
var buttonAttrs = attributes.buttons;


module.exports = function updateMenusDefaults(layoutIn, layoutOut) {
    var opts = {
        name: name,
        handleItemDefaults: menuDefaults
    };

    handleArrayContainerDefaults(layoutIn, layoutOut, opts);
};

function menuDefaults(menuIn, menuOut, layoutOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(menuIn, menuOut, attributes, attr, dflt);
    }

    var buttons = handleArrayContainerDefaults(menuIn, menuOut, {
        name: 'buttons',
        handleItemDefaults: buttonDefaults
    });

    var visible = coerce('visible', buttons.length > 0);
    if(!visible) return;

    coerce('active');
    coerce('direction');
    coerce('type');
    coerce('showactive');

    coerce('x');
    coerce('y');
    Lib.noneOrAll(menuIn, menuOut, ['x', 'y']);

    coerce('xanchor');
    coerce('yanchor');

    coerce('pad.t');
    coerce('pad.r');
    coerce('pad.b');
    coerce('pad.l');

    Lib.coerceFont(coerce, 'font', layoutOut.font);

    coerce('bgcolor', layoutOut.paper_bgcolor);
    coerce('bordercolor');
    coerce('borderwidth');
}

function buttonDefaults(buttonIn, buttonOut) {
    function coerce(attr, dflt) {
        return Lib.coerce(buttonIn, buttonOut, buttonAttrs, attr, dflt);
    }

    var visible = coerce('visible',
        (buttonIn.method === 'skip' || Array.isArray(buttonIn.args)));
    if(visible) {
        coerce('method');
        coerce('args');
        coerce('label');
        coerce('execute');
    }
}
