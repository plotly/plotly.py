/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var Lib = require('../../lib');
var dragElement = require('../dragelement');
var helpers = require('./helpers');
var layoutAttributes = require('./layout_attributes');
var hoverModule = require('./hover');

module.exports = {
    moduleType: 'component',
    name: 'fx',

    constants: require('./constants'),
    schema: {
        layout: layoutAttributes
    },

    attributes: require('./attributes'),
    layoutAttributes: layoutAttributes,

    supplyLayoutGlobalDefaults: require('./layout_global_defaults'),
    supplyDefaults: require('./defaults'),
    supplyLayoutDefaults: require('./layout_defaults'),

    calc: require('./calc'),

    getDistanceFunction: helpers.getDistanceFunction,
    getClosest: helpers.getClosest,
    inbox: helpers.inbox,
    quadrature: helpers.quadrature,
    appendArrayPointValue: helpers.appendArrayPointValue,

    castHoverOption: castHoverOption,
    castHoverinfo: castHoverinfo,

    hover: hoverModule.hover,
    unhover: dragElement.unhover,

    loneHover: hoverModule.loneHover,
    loneUnhover: loneUnhover,

    click: require('./click')
};

function loneUnhover(containerOrSelection) {
    // duck type whether the arg is a d3 selection because ie9 doesn't
    // handle instanceof like modern browsers do.
    var selection = Lib.isD3Selection(containerOrSelection) ?
            containerOrSelection :
            d3.select(containerOrSelection);

    selection.selectAll('g.hovertext').remove();
    selection.selectAll('.spikeline').remove();
}

// helpers for traces that use Fx.loneHover

function castHoverOption(trace, ptNumber, attr) {
    return Lib.castOption(trace, ptNumber, 'hoverlabel.' + attr);
}

function castHoverinfo(trace, fullLayout, ptNumber) {
    function _coerce(val) {
        return Lib.coerceHoverinfo({hoverinfo: val}, {_module: trace._module}, fullLayout);
    }

    return Lib.castOption(trace, ptNumber, 'hoverinfo', _coerce);
}
