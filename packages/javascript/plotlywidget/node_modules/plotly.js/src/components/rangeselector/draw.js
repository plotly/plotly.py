/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var Registry = require('../../registry');
var Plots = require('../../plots/plots');
var Color = require('../color');
var Drawing = require('../drawing');
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');
var axisIds = require('../../plots/cartesian/axis_ids');

var alignmentConstants = require('../../constants/alignment');
var LINE_SPACING = alignmentConstants.LINE_SPACING;
var FROM_TL = alignmentConstants.FROM_TL;
var FROM_BR = alignmentConstants.FROM_BR;

var constants = require('./constants');
var getUpdateObject = require('./get_update_object');

module.exports = function draw(gd) {
    var fullLayout = gd._fullLayout;

    var selectors = fullLayout._infolayer.selectAll('.rangeselector')
        .data(makeSelectorData(gd), selectorKeyFunc);

    selectors.enter().append('g')
        .classed('rangeselector', true);

    selectors.exit().remove();

    selectors.style({
        cursor: 'pointer',
        'pointer-events': 'all'
    });

    selectors.each(function(d) {
        var selector = d3.select(this);
        var axisLayout = d;
        var selectorLayout = axisLayout.rangeselector;

        var buttons = selector.selectAll('g.button')
            .data(Lib.filterVisible(selectorLayout.buttons));

        buttons.enter().append('g')
            .classed('button', true);

        buttons.exit().remove();

        buttons.each(function(d) {
            var button = d3.select(this);
            var update = getUpdateObject(axisLayout, d);

            d._isActive = isActive(axisLayout, d, update);

            button.call(drawButtonRect, selectorLayout, d);
            button.call(drawButtonText, selectorLayout, d, gd);

            button.on('click', function() {
                if(gd._dragged) return;

                Registry.call('_guiRelayout', gd, update);
            });

            button.on('mouseover', function() {
                d._isHovered = true;
                button.call(drawButtonRect, selectorLayout, d);
            });

            button.on('mouseout', function() {
                d._isHovered = false;
                button.call(drawButtonRect, selectorLayout, d);
            });
        });

        reposition(gd, buttons, selectorLayout, axisLayout._name, selector);
    });
};

function makeSelectorData(gd) {
    var axes = axisIds.list(gd, 'x', true);
    var data = [];

    for(var i = 0; i < axes.length; i++) {
        var axis = axes[i];

        if(axis.rangeselector && axis.rangeselector.visible) {
            data.push(axis);
        }
    }

    return data;
}

function selectorKeyFunc(d) {
    return d._id;
}

function isActive(axisLayout, opts, update) {
    if(opts.step === 'all') {
        return axisLayout.autorange === true;
    } else {
        var keys = Object.keys(update);

        return (
            axisLayout.range[0] === update[keys[0]] &&
            axisLayout.range[1] === update[keys[1]]
        );
    }
}

function drawButtonRect(button, selectorLayout, d) {
    var rect = Lib.ensureSingle(button, 'rect', 'selector-rect', function(s) {
        s.attr('shape-rendering', 'crispEdges');
    });

    rect.attr({
        'rx': constants.rx,
        'ry': constants.ry
    });

    rect.call(Color.stroke, selectorLayout.bordercolor)
        .call(Color.fill, getFillColor(selectorLayout, d))
        .style('stroke-width', selectorLayout.borderwidth + 'px');
}

function getFillColor(selectorLayout, d) {
    return (d._isActive || d._isHovered) ?
        selectorLayout.activecolor :
        selectorLayout.bgcolor;
}

function drawButtonText(button, selectorLayout, d, gd) {
    function textLayout(s) {
        svgTextUtils.convertToTspans(s, gd);
    }

    var text = Lib.ensureSingle(button, 'text', 'selector-text', function(s) {
        s.classed('user-select-none', true)
            .attr('text-anchor', 'middle');
    });

    text.call(Drawing.font, selectorLayout.font)
        .text(getLabel(d, gd._fullLayout._meta))
        .call(textLayout);
}

function getLabel(opts, _meta) {
    if(opts.label) {
        return _meta ?
            Lib.templateString(opts.label, _meta) :
            opts.label;
    }

    if(opts.step === 'all') return 'all';

    return opts.count + opts.step.charAt(0);
}

function reposition(gd, buttons, opts, axName, selector) {
    var width = 0;
    var height = 0;

    var borderWidth = opts.borderwidth;

    buttons.each(function() {
        var button = d3.select(this);
        var text = button.select('.selector-text');

        var tHeight = opts.font.size * LINE_SPACING;
        var hEff = Math.max(tHeight * svgTextUtils.lineCount(text), 16) + 3;

        height = Math.max(height, hEff);
    });

    buttons.each(function() {
        var button = d3.select(this);
        var rect = button.select('.selector-rect');
        var text = button.select('.selector-text');

        var tWidth = text.node() && Drawing.bBox(text.node()).width;
        var tHeight = opts.font.size * LINE_SPACING;
        var tLines = svgTextUtils.lineCount(text);

        var wEff = Math.max(tWidth + 10, constants.minButtonWidth);

        // TODO add MathJax support

        // TODO add buttongap attribute

        button.attr('transform', 'translate(' +
            (borderWidth + width) + ',' + borderWidth +
        ')');

        rect.attr({
            x: 0,
            y: 0,
            width: wEff,
            height: height
        });

        svgTextUtils.positionText(text, wEff / 2,
            height / 2 - ((tLines - 1) * tHeight / 2) + 3);

        width += wEff + 5;
    });

    var graphSize = gd._fullLayout._size;
    var lx = graphSize.l + graphSize.w * opts.x;
    var ly = graphSize.t + graphSize.h * (1 - opts.y);

    var xanchor = 'left';
    if(Lib.isRightAnchor(opts)) {
        lx -= width;
        xanchor = 'right';
    }
    if(Lib.isCenterAnchor(opts)) {
        lx -= width / 2;
        xanchor = 'center';
    }

    var yanchor = 'top';
    if(Lib.isBottomAnchor(opts)) {
        ly -= height;
        yanchor = 'bottom';
    }
    if(Lib.isMiddleAnchor(opts)) {
        ly -= height / 2;
        yanchor = 'middle';
    }

    width = Math.ceil(width);
    height = Math.ceil(height);
    lx = Math.round(lx);
    ly = Math.round(ly);

    Plots.autoMargin(gd, axName + '-range-selector', {
        x: opts.x,
        y: opts.y,
        l: width * FROM_TL[xanchor],
        r: width * FROM_BR[xanchor],
        b: height * FROM_BR[yanchor],
        t: height * FROM_TL[yanchor]
    });

    selector.attr('transform', 'translate(' + lx + ',' + ly + ')');
}
