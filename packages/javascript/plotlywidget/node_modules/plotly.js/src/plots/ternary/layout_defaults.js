/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Color = require('../../components/color');
var Template = require('../../plot_api/plot_template');
var Lib = require('../../lib');

var handleSubplotDefaults = require('../subplot_defaults');
var handleTickLabelDefaults = require('../cartesian/tick_label_defaults');
var handleTickMarkDefaults = require('../cartesian/tick_mark_defaults');
var handleTickValueDefaults = require('../cartesian/tick_value_defaults');
var handleLineGridDefaults = require('../cartesian/line_grid_defaults');
var layoutAttributes = require('./layout_attributes');

var axesNames = ['aaxis', 'baxis', 'caxis'];

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut, fullData) {
    handleSubplotDefaults(layoutIn, layoutOut, fullData, {
        type: 'ternary',
        attributes: layoutAttributes,
        handleDefaults: handleTernaryDefaults,
        font: layoutOut.font,
        paper_bgcolor: layoutOut.paper_bgcolor
    });
};

function handleTernaryDefaults(ternaryLayoutIn, ternaryLayoutOut, coerce, options) {
    var bgColor = coerce('bgcolor');
    var sum = coerce('sum');
    options.bgColor = Color.combine(bgColor, options.paper_bgcolor);
    var axName, containerIn, containerOut;

    // TODO: allow most (if not all) axis attributes to be set
    // in the outer container and used as defaults in the individual axes?

    for(var j = 0; j < axesNames.length; j++) {
        axName = axesNames[j];
        containerIn = ternaryLayoutIn[axName] || {};
        containerOut = Template.newContainer(ternaryLayoutOut, axName);
        containerOut._name = axName;

        handleAxisDefaults(containerIn, containerOut, options, ternaryLayoutOut);
    }

    // if the min values contradict each other, set them all to default (0)
    // and delete *all* the inputs so the user doesn't get confused later by
    // changing one and having them all change.
    var aaxis = ternaryLayoutOut.aaxis;
    var baxis = ternaryLayoutOut.baxis;
    var caxis = ternaryLayoutOut.caxis;
    if(aaxis.min + baxis.min + caxis.min >= sum) {
        aaxis.min = 0;
        baxis.min = 0;
        caxis.min = 0;
        if(ternaryLayoutIn.aaxis) delete ternaryLayoutIn.aaxis.min;
        if(ternaryLayoutIn.baxis) delete ternaryLayoutIn.baxis.min;
        if(ternaryLayoutIn.caxis) delete ternaryLayoutIn.caxis.min;
    }
}

function handleAxisDefaults(containerIn, containerOut, options, ternaryLayoutOut) {
    var axAttrs = layoutAttributes[containerOut._name];

    function coerce(attr, dflt) {
        return Lib.coerce(containerIn, containerOut, axAttrs, attr, dflt);
    }

    coerce('uirevision', ternaryLayoutOut.uirevision);

    containerOut.type = 'linear'; // no other types allowed for ternary

    var dfltColor = coerce('color');
    // if axis.color was provided, use it for fonts too; otherwise,
    // inherit from global font color in case that was provided.
    var dfltFontColor = (dfltColor !== axAttrs.color.dflt) ? dfltColor : options.font.color;

    var axName = containerOut._name;
    var letterUpper = axName.charAt(0).toUpperCase();
    var dfltTitle = 'Component ' + letterUpper;

    var title = coerce('title.text', dfltTitle);
    containerOut._hovertitle = title === dfltTitle ? title : letterUpper;

    Lib.coerceFont(coerce, 'title.font', {
        family: options.font.family,
        size: Math.round(options.font.size * 1.2),
        color: dfltFontColor
    });

    // range is just set by 'min' - max is determined by the other axes mins
    coerce('min');

    handleTickValueDefaults(containerIn, containerOut, coerce, 'linear');
    handleTickLabelDefaults(containerIn, containerOut, coerce, 'linear', {});
    handleTickMarkDefaults(containerIn, containerOut, coerce,
        { outerTicks: true });

    var showTickLabels = coerce('showticklabels');
    if(showTickLabels) {
        Lib.coerceFont(coerce, 'tickfont', {
            family: options.font.family,
            size: options.font.size,
            color: dfltFontColor
        });
        coerce('tickangle');
        coerce('tickformat');
    }

    handleLineGridDefaults(containerIn, containerOut, coerce, {
        dfltColor: dfltColor,
        bgColor: options.bgColor,
        // default grid color is darker here (60%, vs cartesian default ~91%)
        // because the grid is not square so the eye needs heavier cues to follow
        blend: 60,
        showLine: true,
        showGrid: true,
        noZeroLine: true,
        attributes: axAttrs
    });

    coerce('hoverformat');
    coerce('layer');
}
