/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');

var layoutAttributes = require('./layout_attributes');
var handleTickValueDefaults = require('./tick_value_defaults');
var handleTickMarkDefaults = require('./tick_mark_defaults');
var handleTickLabelDefaults = require('./tick_label_defaults');
var handleCategoryOrderDefaults = require('./category_order_defaults');
var handleLineGridDefaults = require('./line_grid_defaults');
var setConvert = require('./set_convert');

/**
 * options: object containing:
 *
 *  letter: 'x' or 'y'
 *  title: name of the axis (ie 'Colorbar') to go in default title
 *  font: the default font to inherit
 *  outerTicks: boolean, should ticks default to outside?
 *  showGrid: boolean, should gridlines be shown by default?
 *  noHover: boolean, this axis doesn't support hover effects?
 *  noTickson: boolean, this axis doesn't support 'tickson'
 *  data: the plot data, used to manage categories
 *  bgColor: the plot background color, to calculate default gridline colors
 *  calendar:
 *  splomStash:
 *  visibleDflt: boolean
 *  reverseDflt: boolean
 *  automargin: boolean
 */
module.exports = function handleAxisDefaults(containerIn, containerOut, coerce, options, layoutOut) {
    var letter = options.letter;
    var font = options.font || {};
    var splomStash = options.splomStash || {};

    var visible = coerce('visible', !options.visibleDflt);

    var axType = containerOut.type;

    if(axType === 'date') {
        var handleCalendarDefaults = Registry.getComponentMethod('calendars', 'handleDefaults');
        handleCalendarDefaults(containerIn, containerOut, 'calendar', options.calendar);
    }

    setConvert(containerOut, layoutOut);

    var autorangeDflt = !containerOut.isValidRange(containerIn.range);
    if(autorangeDflt && options.reverseDflt) autorangeDflt = 'reversed';
    var autoRange = coerce('autorange', autorangeDflt);
    if(autoRange && (axType === 'linear' || axType === '-')) coerce('rangemode');

    coerce('range');
    containerOut.cleanRange();

    handleCategoryOrderDefaults(containerIn, containerOut, coerce, options);

    if(axType !== 'category' && !options.noHover) coerce('hoverformat');

    var dfltColor = coerce('color');
    // if axis.color was provided, use it for fonts too; otherwise,
    // inherit from global font color in case that was provided.
    // Compare to dflt rather than to containerIn, so we can provide color via
    // template too.
    var dfltFontColor = (dfltColor !== layoutAttributes.color.dflt) ? dfltColor : font.color;
    // try to get default title from splom trace, fallback to graph-wide value
    var dfltTitle = splomStash.label || layoutOut._dfltTitle[letter];

    handleTickLabelDefaults(containerIn, containerOut, coerce, axType, options, {pass: 1});
    if(!visible) return containerOut;

    coerce('title.text', dfltTitle);
    Lib.coerceFont(coerce, 'title.font', {
        family: font.family,
        size: Math.round(font.size * 1.2),
        color: dfltFontColor
    });

    handleTickValueDefaults(containerIn, containerOut, coerce, axType);
    handleTickLabelDefaults(containerIn, containerOut, coerce, axType, options, {pass: 2});
    handleTickMarkDefaults(containerIn, containerOut, coerce, options);
    handleLineGridDefaults(containerIn, containerOut, coerce, {
        dfltColor: dfltColor,
        bgColor: options.bgColor,
        showGrid: options.showGrid,
        attributes: layoutAttributes
    });

    if(containerOut.showline || containerOut.ticks) coerce('mirror');

    if(options.automargin) coerce('automargin');

    var isMultiCategory = containerOut.type === 'multicategory';

    if(!options.noTickson &&
        (containerOut.type === 'category' || isMultiCategory) &&
        (containerOut.ticks || containerOut.showgrid)
    ) {
        var ticksonDflt;
        if(isMultiCategory) ticksonDflt = 'boundaries';
        coerce('tickson', ticksonDflt);
    }

    if(isMultiCategory) {
        var showDividers = coerce('showdividers');
        if(showDividers) {
            coerce('dividercolor');
            coerce('dividerwidth');
        }
    }

    return containerOut;
};
