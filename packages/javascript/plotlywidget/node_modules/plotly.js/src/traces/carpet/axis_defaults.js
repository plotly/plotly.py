/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var carpetAttrs = require('./attributes');

var addOpacity = require('../../components/color').addOpacity;
var Registry = require('../../registry');
var Lib = require('../../lib');
var handleTickValueDefaults = require('../../plots/cartesian/tick_value_defaults');
var handleTickLabelDefaults = require('../../plots/cartesian/tick_label_defaults');
var handleCategoryOrderDefaults = require('../../plots/cartesian/category_order_defaults');
var setConvert = require('../../plots/cartesian/set_convert');
var autoType = require('../../plots/cartesian/axis_autotype');

/**
 * options: object containing:
 *
 *  letter: 'a' or 'b'
 *  title: name of the axis (ie 'Colorbar') to go in default title
 *  name: axis object name (ie 'xaxis') if one should be stored
 *  font: the default font to inherit
 *  outerTicks: boolean, should ticks default to outside?
 *  showGrid: boolean, should gridlines be shown by default?
 *  data: the plot data to use in choosing auto type
 *  bgColor: the plot background color, to calculate default gridline colors
 */
module.exports = function handleAxisDefaults(containerIn, containerOut, options) {
    var letter = options.letter;
    var font = options.font || {};
    var attributes = carpetAttrs[letter + 'axis'];

    function coerce(attr, dflt) {
        return Lib.coerce(containerIn, containerOut, attributes, attr, dflt);
    }

    function coerce2(attr, dflt) {
        return Lib.coerce2(containerIn, containerOut, attributes, attr, dflt);
    }

    // set up some private properties
    if(options.name) {
        containerOut._name = options.name;
        containerOut._id = options.name;
    }

    // now figure out type and do some more initialization
    var axType = coerce('type');
    if(axType === '-') {
        if(options.data) setAutoType(containerOut, options.data);

        if(containerOut.type === '-') {
            containerOut.type = 'linear';
        } else {
            // copy autoType back to input axis
            // note that if this object didn't exist
            // in the input layout, we have to put it in
            // this happens in the main supplyDefaults function
            axType = containerIn.type = containerOut.type;
        }
    }

    coerce('smoothing');
    coerce('cheatertype');

    coerce('showticklabels');
    coerce('labelprefix', letter + ' = ');
    coerce('labelsuffix');
    coerce('showtickprefix');
    coerce('showticksuffix');

    coerce('separatethousands');
    coerce('tickformat');
    coerce('exponentformat');
    coerce('showexponent');
    coerce('categoryorder');

    coerce('tickmode');
    coerce('tickvals');
    coerce('ticktext');
    coerce('tick0');
    coerce('dtick');

    if(containerOut.tickmode === 'array') {
        coerce('arraytick0');
        coerce('arraydtick');
    }

    coerce('labelpadding');

    containerOut._hovertitle = letter;


    if(axType === 'date') {
        var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleDefaults');
        handleCalendarDefaults(containerIn, containerOut, 'calendar', options.calendar);
    }

    // we need some of the other functions setConvert attaches, but for
    // path finding, override pixel scaling to simple passthrough (identity)
    setConvert(containerOut, options.fullLayout);
    containerOut.c2p = Lib.identity;

    var dfltColor = coerce('color', options.dfltColor);
    // if axis.color was provided, use it for fonts too; otherwise,
    // inherit from global font color in case that was provided.
    var dfltFontColor = (dfltColor === containerIn.color) ? dfltColor : font.color;

    var title = coerce('title.text');
    if(title) {
        Lib.coerceFont(coerce, 'title.font', {
            family: font.family,
            size: Math.round(font.size * 1.2),
            color: dfltFontColor
        });
        coerce('title.offset');
    }

    coerce('tickangle');

    var autoRange = coerce('autorange', !containerOut.isValidRange(containerIn.range));

    if(autoRange) coerce('rangemode');

    coerce('range');
    containerOut.cleanRange();

    coerce('fixedrange');

    handleTickValueDefaults(containerIn, containerOut, coerce, axType);
    handleTickLabelDefaults(containerIn, containerOut, coerce, axType, options);
    handleCategoryOrderDefaults(containerIn, containerOut, coerce, {
        data: options.data,
        dataAttr: letter
    });

    var gridColor = coerce2('gridcolor', addOpacity(dfltColor, 0.3));
    var gridWidth = coerce2('gridwidth');
    var showGrid = coerce('showgrid');

    if(!showGrid) {
        delete containerOut.gridcolor;
        delete containerOut.gridwidth;
    }

    var startLineColor = coerce2('startlinecolor', dfltColor);
    var startLineWidth = coerce2('startlinewidth', gridWidth);
    var showStartLine = coerce('startline', containerOut.showgrid || !!startLineColor || !!startLineWidth);

    if(!showStartLine) {
        delete containerOut.startlinecolor;
        delete containerOut.startlinewidth;
    }

    var endLineColor = coerce2('endlinecolor', dfltColor);
    var endLineWidth = coerce2('endlinewidth', gridWidth);
    var showEndLine = coerce('endline', containerOut.showgrid || !!endLineColor || !!endLineWidth);

    if(!showEndLine) {
        delete containerOut.endlinecolor;
        delete containerOut.endlinewidth;
    }

    if(!showGrid) {
        delete containerOut.gridcolor;
        delete containerOut.gridWidth;
    } else {
        coerce('minorgridcount');
        coerce('minorgridwidth', gridWidth);
        coerce('minorgridcolor', addOpacity(gridColor, 0.06));

        if(!containerOut.minorgridcount) {
            delete containerOut.minorgridwidth;
            delete containerOut.minorgridcolor;
        }
    }

    if(containerOut.showticklabels === 'none') {
        delete containerOut.tickfont;
        delete containerOut.tickangle;
        delete containerOut.showexponent;
        delete containerOut.exponentformat;
        delete containerOut.tickformat;
        delete containerOut.showticksuffix;
        delete containerOut.showtickprefix;
    }

    if(!containerOut.showticksuffix) {
        delete containerOut.ticksuffix;
    }

    if(!containerOut.showtickprefix) {
        delete containerOut.tickprefix;
    }

    // It needs to be coerced, then something above overrides this deep in the axis code,
    // but no, we *actually* want to coerce this.
    coerce('tickmode');

    return containerOut;
};

function setAutoType(ax, data) {
    // new logic: let people specify any type they want,
    // only autotype if type is '-'
    if(ax.type !== '-') return;

    var id = ax._id;
    var axLetter = id.charAt(0);

    var calAttr = axLetter + 'calendar';
    var calendar = ax[calAttr];

    ax.type = autoType(data, calendar);
}
