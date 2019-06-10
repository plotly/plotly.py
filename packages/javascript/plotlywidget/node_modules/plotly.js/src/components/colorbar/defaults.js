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

var handleTickValueDefaults = require('../../plots/cartesian/tick_value_defaults');
var handleTickMarkDefaults = require('../../plots/cartesian/tick_mark_defaults');
var handleTickLabelDefaults = require('../../plots/cartesian/tick_label_defaults');

var attributes = require('./attributes');

module.exports = function colorbarDefaults(containerIn, containerOut, layout) {
    var colorbarOut = Template.newContainer(containerOut, 'colorbar');
    var colorbarIn = containerIn.colorbar || {};

    function coerce(attr, dflt) {
        return Lib.coerce(colorbarIn, colorbarOut, attributes, attr, dflt);
    }

    var thicknessmode = coerce('thicknessmode');
    coerce('thickness', (thicknessmode === 'fraction') ?
        30 / (layout.width - layout.margin.l - layout.margin.r) :
        30
    );

    var lenmode = coerce('lenmode');
    coerce('len', (lenmode === 'fraction') ?
        1 :
        layout.height - layout.margin.t - layout.margin.b
    );

    coerce('x');
    coerce('xanchor');
    coerce('xpad');
    coerce('y');
    coerce('yanchor');
    coerce('ypad');
    Lib.noneOrAll(colorbarIn, colorbarOut, ['x', 'y']);

    coerce('outlinecolor');
    coerce('outlinewidth');
    coerce('bordercolor');
    coerce('borderwidth');
    coerce('bgcolor');

    handleTickValueDefaults(colorbarIn, colorbarOut, coerce, 'linear');

    var opts = {outerTicks: false, font: layout.font};
    handleTickLabelDefaults(colorbarIn, colorbarOut, coerce, 'linear', opts);
    handleTickMarkDefaults(colorbarIn, colorbarOut, coerce, 'linear', opts);

    coerce('title.text', layout._dfltTitle.colorbar);
    Lib.coerceFont(coerce, 'title.font', layout.font);
    coerce('title.side');
};
