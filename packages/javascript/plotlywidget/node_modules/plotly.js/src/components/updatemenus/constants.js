/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';


module.exports = {

    // layout attribute name
    name: 'updatemenus',

    // class names
    containerClassName: 'updatemenu-container',
    headerGroupClassName: 'updatemenu-header-group',
    headerClassName: 'updatemenu-header',
    headerArrowClassName: 'updatemenu-header-arrow',
    dropdownButtonGroupClassName: 'updatemenu-dropdown-button-group',
    dropdownButtonClassName: 'updatemenu-dropdown-button',
    buttonClassName: 'updatemenu-button',
    itemRectClassName: 'updatemenu-item-rect',
    itemTextClassName: 'updatemenu-item-text',

    // DOM attribute name in button group keeping track
    // of active update menu
    menuIndexAttrName: 'updatemenu-active-index',

    // id root pass to Plots.autoMargin
    autoMarginIdRoot: 'updatemenu-',

    // options when 'active: -1'
    blankHeaderOpts: { label: '  ' },

    // min item width / height
    minWidth: 30,
    minHeight: 30,

    // padding around item text
    textPadX: 24,
    arrowPadX: 16,

    // item rect radii
    rx: 2,
    ry: 2,

    // item  text x offset off left edge
    textOffsetX: 12,

    // item  text y offset (w.r.t. middle)
    textOffsetY: 3,

    // arrow offset off right edge
    arrowOffsetX: 4,

    // gap between header and buttons
    gapButtonHeader: 5,

    // gap between between buttons
    gapButton: 2,

    // color given to active buttons
    activeColor: '#F4FAFF',

    // color given to hovered buttons
    hoverColor: '#F4FAFF',

    // symbol for menu open arrow
    arrowSymbol: {
        left: '◄',
        right: '►',
        up: '▲',
        down: '▼'
    }
};
