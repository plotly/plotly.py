/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');

var Plots = require('../../plots/plots');
var Color = require('../color');
var Drawing = require('../drawing');
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');
var arrayEditor = require('../../plot_api/plot_template').arrayEditor;

var constants = require('./constants');
var alignmentConstants = require('../../constants/alignment');
var LINE_SPACING = alignmentConstants.LINE_SPACING;
var FROM_TL = alignmentConstants.FROM_TL;
var FROM_BR = alignmentConstants.FROM_BR;

module.exports = function draw(gd) {
    var fullLayout = gd._fullLayout;
    var sliderData = makeSliderData(fullLayout, gd);

    // draw a container for *all* sliders:
    var sliders = fullLayout._infolayer
        .selectAll('g.' + constants.containerClassName)
        .data(sliderData.length > 0 ? [0] : []);

    sliders.enter().append('g')
        .classed(constants.containerClassName, true)
        .style('cursor', 'ew-resize');

    function clearSlider(sliderOpts) {
        if(sliderOpts._commandObserver) {
            sliderOpts._commandObserver.remove();
            delete sliderOpts._commandObserver;
        }

        // Most components don't need to explicitly remove autoMargin, because
        // marginPushers does this - but slider updates don't go through
        // a full replot so we need to explicitly remove it.
        Plots.autoMargin(gd, autoMarginId(sliderOpts));
    }

    sliders.exit().each(function() {
        d3.select(this).selectAll('g.' + constants.groupClassName)
            .each(clearSlider);
    })
    .remove();

    // Return early if no menus visible:
    if(sliderData.length === 0) return;

    var sliderGroups = sliders.selectAll('g.' + constants.groupClassName)
        .data(sliderData, keyFunction);

    sliderGroups.enter().append('g')
        .classed(constants.groupClassName, true);

    sliderGroups.exit()
        .each(clearSlider)
        .remove();

    // Find the dimensions of the sliders:
    for(var i = 0; i < sliderData.length; i++) {
        var sliderOpts = sliderData[i];
        findDimensions(gd, sliderOpts);
    }

    sliderGroups.each(function(sliderOpts) {
        var gSlider = d3.select(this);

        computeLabelSteps(sliderOpts);

        Plots.manageCommandObserver(gd, sliderOpts, sliderOpts._visibleSteps, function(data) {
            // NB: Same as below. This is *not* always the same as sliderOpts since
            // if a new set of steps comes in, the reference in this callback would
            // be invalid. We need to refetch it from the slider group, which is
            // the join data that creates this slider. So if this slider still exists,
            // the group should be valid, *to the best of my knowledge.* If not,
            // we'd have to look it up by d3 data join index/key.
            var opts = gSlider.data()[0];

            if(opts.active === data.index) return;
            if(opts._dragging) return;

            setActive(gd, gSlider, opts, data.index, false, true);
        });

        drawSlider(gd, d3.select(this), sliderOpts);
    });
};

function autoMarginId(sliderOpts) {
    return constants.autoMarginIdRoot + sliderOpts._index;
}

// This really only just filters by visibility:
function makeSliderData(fullLayout, gd) {
    var contOpts = fullLayout[constants.name];
    var sliderData = [];

    for(var i = 0; i < contOpts.length; i++) {
        var item = contOpts[i];
        if(!item.visible) continue;
        item._gd = gd;
        sliderData.push(item);
    }

    return sliderData;
}

// This is set in the defaults step:
function keyFunction(opts) {
    return opts._index;
}

// Compute the dimensions (mutates sliderOpts):
function findDimensions(gd, sliderOpts) {
    var sliderLabels = Drawing.tester.selectAll('g.' + constants.labelGroupClass)
        .data(sliderOpts._visibleSteps);

    sliderLabels.enter().append('g')
        .classed(constants.labelGroupClass, true);

    // loop over fake buttons to find width / height
    var maxLabelWidth = 0;
    var labelHeight = 0;
    sliderLabels.each(function(stepOpts) {
        var labelGroup = d3.select(this);

        var text = drawLabel(labelGroup, {step: stepOpts}, sliderOpts);

        var textNode = text.node();
        if(textNode) {
            var bBox = Drawing.bBox(textNode);
            labelHeight = Math.max(labelHeight, bBox.height);
            maxLabelWidth = Math.max(maxLabelWidth, bBox.width);
        }
    });

    sliderLabels.remove();

    var dims = sliderOpts._dims = {};

    dims.inputAreaWidth = Math.max(
        constants.railWidth,
        constants.gripHeight
    );

    // calculate some overall dimensions - some of these are needed for
    // calculating the currentValue dimensions
    var graphSize = gd._fullLayout._size;
    dims.lx = graphSize.l + graphSize.w * sliderOpts.x;
    dims.ly = graphSize.t + graphSize.h * (1 - sliderOpts.y);

    if(sliderOpts.lenmode === 'fraction') {
        // fraction:
        dims.outerLength = Math.round(graphSize.w * sliderOpts.len);
    } else {
        // pixels:
        dims.outerLength = sliderOpts.len;
    }

    // The length of the rail, *excluding* padding on either end:
    dims.inputAreaStart = 0;
    dims.inputAreaLength = Math.round(dims.outerLength - sliderOpts.pad.l - sliderOpts.pad.r);

    var textableInputLength = dims.inputAreaLength - 2 * constants.stepInset;
    var availableSpacePerLabel = textableInputLength / (sliderOpts._stepCount - 1);
    var computedSpacePerLabel = maxLabelWidth + constants.labelPadding;
    dims.labelStride = Math.max(1, Math.ceil(computedSpacePerLabel / availableSpacePerLabel));
    dims.labelHeight = labelHeight;

    // loop over all possible values for currentValue to find the
    // area we need for it
    dims.currentValueMaxWidth = 0;
    dims.currentValueHeight = 0;
    dims.currentValueTotalHeight = 0;
    dims.currentValueMaxLines = 1;

    if(sliderOpts.currentvalue.visible) {
        // Get the dimensions of the current value label:
        var dummyGroup = Drawing.tester.append('g');

        sliderLabels.each(function(stepOpts) {
            var curValPrefix = drawCurrentValue(dummyGroup, sliderOpts, stepOpts.label);
            var curValSize = (curValPrefix.node() && Drawing.bBox(curValPrefix.node())) || {width: 0, height: 0};
            var lines = svgTextUtils.lineCount(curValPrefix);
            dims.currentValueMaxWidth = Math.max(dims.currentValueMaxWidth, Math.ceil(curValSize.width));
            dims.currentValueHeight = Math.max(dims.currentValueHeight, Math.ceil(curValSize.height));
            dims.currentValueMaxLines = Math.max(dims.currentValueMaxLines, lines);
        });

        dims.currentValueTotalHeight = dims.currentValueHeight + sliderOpts.currentvalue.offset;

        dummyGroup.remove();
    }

    dims.height = dims.currentValueTotalHeight + constants.tickOffset + sliderOpts.ticklen + constants.labelOffset + dims.labelHeight + sliderOpts.pad.t + sliderOpts.pad.b;

    var xanchor = 'left';
    if(Lib.isRightAnchor(sliderOpts)) {
        dims.lx -= dims.outerLength;
        xanchor = 'right';
    }
    if(Lib.isCenterAnchor(sliderOpts)) {
        dims.lx -= dims.outerLength / 2;
        xanchor = 'center';
    }

    var yanchor = 'top';
    if(Lib.isBottomAnchor(sliderOpts)) {
        dims.ly -= dims.height;
        yanchor = 'bottom';
    }
    if(Lib.isMiddleAnchor(sliderOpts)) {
        dims.ly -= dims.height / 2;
        yanchor = 'middle';
    }

    dims.outerLength = Math.ceil(dims.outerLength);
    dims.height = Math.ceil(dims.height);
    dims.lx = Math.round(dims.lx);
    dims.ly = Math.round(dims.ly);

    var marginOpts = {
        y: sliderOpts.y,
        b: dims.height * FROM_BR[yanchor],
        t: dims.height * FROM_TL[yanchor]
    };

    if(sliderOpts.lenmode === 'fraction') {
        marginOpts.l = 0;
        marginOpts.xl = sliderOpts.x - sliderOpts.len * FROM_TL[xanchor];
        marginOpts.r = 0;
        marginOpts.xr = sliderOpts.x + sliderOpts.len * FROM_BR[xanchor];
    } else {
        marginOpts.x = sliderOpts.x;
        marginOpts.l = dims.outerLength * FROM_TL[xanchor];
        marginOpts.r = dims.outerLength * FROM_BR[xanchor];
    }

    Plots.autoMargin(gd, autoMarginId(sliderOpts), marginOpts);
}

function drawSlider(gd, sliderGroup, sliderOpts) {
    // This is related to the other long notes in this file regarding what happens
    // when slider steps disappear. This particular fix handles what happens when
    // the *current* slider step is removed. The drawing functions will error out
    // when they fail to find it, so the fix for now is that it will just draw the
    // slider in the first position but will not execute the command.
    if(!((sliderOpts.steps[sliderOpts.active] || {}).visible)) {
        sliderOpts.active = sliderOpts._visibleSteps[0]._index;
    }

    // These are carefully ordered for proper z-ordering:
    sliderGroup
        .call(drawCurrentValue, sliderOpts)
        .call(drawRail, sliderOpts)
        .call(drawLabelGroup, sliderOpts)
        .call(drawTicks, sliderOpts)
        .call(drawTouchRect, gd, sliderOpts)
        .call(drawGrip, gd, sliderOpts);

    var dims = sliderOpts._dims;

    // Position the rectangle:
    Drawing.setTranslate(sliderGroup, dims.lx + sliderOpts.pad.l, dims.ly + sliderOpts.pad.t);

    sliderGroup.call(setGripPosition, sliderOpts, false);
    sliderGroup.call(drawCurrentValue, sliderOpts);
}

function drawCurrentValue(sliderGroup, sliderOpts, valueOverride) {
    if(!sliderOpts.currentvalue.visible) return;

    var dims = sliderOpts._dims;
    var x0, textAnchor;

    switch(sliderOpts.currentvalue.xanchor) {
        case 'right':
            // This is anchored left and adjusted by the width of the longest label
            // so that the prefix doesn't move. The goal of this is to emphasize
            // what's actually changing and make the update less distracting.
            x0 = dims.inputAreaLength - constants.currentValueInset - dims.currentValueMaxWidth;
            textAnchor = 'left';
            break;
        case 'center':
            x0 = dims.inputAreaLength * 0.5;
            textAnchor = 'middle';
            break;
        default:
            x0 = constants.currentValueInset;
            textAnchor = 'left';
    }

    var text = Lib.ensureSingle(sliderGroup, 'text', constants.labelClass, function(s) {
        s.classed('user-select-none', true)
            .attr({
                'text-anchor': textAnchor,
                'data-notex': 1
            });
    });

    var str = sliderOpts.currentvalue.prefix ? sliderOpts.currentvalue.prefix : '';

    if(typeof valueOverride === 'string') {
        str += valueOverride;
    } else {
        var curVal = sliderOpts.steps[sliderOpts.active].label;
        var _meta = sliderOpts._gd._fullLayout._meta;
        if(_meta) curVal = Lib.templateString(curVal, _meta);
        str += curVal;
    }

    if(sliderOpts.currentvalue.suffix) {
        str += sliderOpts.currentvalue.suffix;
    }

    text.call(Drawing.font, sliderOpts.currentvalue.font)
        .text(str)
        .call(svgTextUtils.convertToTspans, sliderOpts._gd);

    var lines = svgTextUtils.lineCount(text);

    var y0 = (dims.currentValueMaxLines + 1 - lines) *
        sliderOpts.currentvalue.font.size * LINE_SPACING;

    svgTextUtils.positionText(text, x0, y0);

    return text;
}

function drawGrip(sliderGroup, gd, sliderOpts) {
    var grip = Lib.ensureSingle(sliderGroup, 'rect', constants.gripRectClass, function(s) {
        s.call(attachGripEvents, gd, sliderGroup, sliderOpts)
            .style('pointer-events', 'all');
    });

    grip.attr({
        width: constants.gripWidth,
        height: constants.gripHeight,
        rx: constants.gripRadius,
        ry: constants.gripRadius,
    })
    .call(Color.stroke, sliderOpts.bordercolor)
    .call(Color.fill, sliderOpts.bgcolor)
    .style('stroke-width', sliderOpts.borderwidth + 'px');
}

function drawLabel(item, data, sliderOpts) {
    var text = Lib.ensureSingle(item, 'text', constants.labelClass, function(s) {
        s.classed('user-select-none', true)
            .attr({
                'text-anchor': 'middle',
                'data-notex': 1
            });
    });

    var tx = data.step.label;
    var _meta = sliderOpts._gd._fullLayout._meta;
    if(_meta) tx = Lib.templateString(tx, _meta);

    text.call(Drawing.font, sliderOpts.font)
        .text(tx)
        .call(svgTextUtils.convertToTspans, sliderOpts._gd);

    return text;
}

function drawLabelGroup(sliderGroup, sliderOpts) {
    var labels = Lib.ensureSingle(sliderGroup, 'g', constants.labelsClass);
    var dims = sliderOpts._dims;

    var labelItems = labels.selectAll('g.' + constants.labelGroupClass)
        .data(dims.labelSteps);

    labelItems.enter().append('g')
        .classed(constants.labelGroupClass, true);

    labelItems.exit().remove();

    labelItems.each(function(d) {
        var item = d3.select(this);

        item.call(drawLabel, d, sliderOpts);

        Drawing.setTranslate(item,
            normalizedValueToPosition(sliderOpts, d.fraction),
            constants.tickOffset +
                sliderOpts.ticklen +
                // position is the baseline of the top line of text only, even
                // if the label spans multiple lines
                sliderOpts.font.size * LINE_SPACING +
                constants.labelOffset +
                dims.currentValueTotalHeight
        );
    });
}

function handleInput(gd, sliderGroup, sliderOpts, normalizedPosition, doTransition) {
    var quantizedPosition = Math.round(normalizedPosition * (sliderOpts._stepCount - 1));
    var quantizedIndex = sliderOpts._visibleSteps[quantizedPosition]._index;

    if(quantizedIndex !== sliderOpts.active) {
        setActive(gd, sliderGroup, sliderOpts, quantizedIndex, true, doTransition);
    }
}

function setActive(gd, sliderGroup, sliderOpts, index, doCallback, doTransition) {
    var previousActive = sliderOpts.active;
    sliderOpts.active = index;

    // due to templating, it's possible this slider doesn't even exist yet
    arrayEditor(gd.layout, constants.name, sliderOpts)
        .applyUpdate('active', index);

    var step = sliderOpts.steps[sliderOpts.active];

    sliderGroup.call(setGripPosition, sliderOpts, doTransition);
    sliderGroup.call(drawCurrentValue, sliderOpts);

    gd.emit('plotly_sliderchange', {
        slider: sliderOpts,
        step: sliderOpts.steps[sliderOpts.active],
        interaction: doCallback,
        previousActive: previousActive
    });

    if(step && step.method && doCallback) {
        if(sliderGroup._nextMethod) {
            // If we've already queued up an update, just overwrite it with the most recent:
            sliderGroup._nextMethod.step = step;
            sliderGroup._nextMethod.doCallback = doCallback;
            sliderGroup._nextMethod.doTransition = doTransition;
        } else {
            sliderGroup._nextMethod = {step: step, doCallback: doCallback, doTransition: doTransition};
            sliderGroup._nextMethodRaf = window.requestAnimationFrame(function() {
                var _step = sliderGroup._nextMethod.step;
                if(!_step.method) return;

                if(_step.execute) {
                    Plots.executeAPICommand(gd, _step.method, _step.args);
                }

                sliderGroup._nextMethod = null;
                sliderGroup._nextMethodRaf = null;
            });
        }
    }
}

function attachGripEvents(item, gd, sliderGroup) {
    var node = sliderGroup.node();
    var $gd = d3.select(gd);

    // NB: This is *not* the same as sliderOpts itself! These callbacks
    // are in a closure so this array won't actually be correct if the
    // steps have changed since this was initialized. The sliderGroup,
    // however, has not changed since that *is* the slider, so it must
    // be present to receive mouse events.
    function getSliderOpts() {
        return sliderGroup.data()[0];
    }

    item.on('mousedown', function() {
        var sliderOpts = getSliderOpts();
        gd.emit('plotly_sliderstart', {slider: sliderOpts});

        var grip = sliderGroup.select('.' + constants.gripRectClass);

        d3.event.stopPropagation();
        d3.event.preventDefault();
        grip.call(Color.fill, sliderOpts.activebgcolor);

        var normalizedPosition = positionToNormalizedValue(sliderOpts, d3.mouse(node)[0]);
        handleInput(gd, sliderGroup, sliderOpts, normalizedPosition, true);
        sliderOpts._dragging = true;

        $gd.on('mousemove', function() {
            var sliderOpts = getSliderOpts();
            var normalizedPosition = positionToNormalizedValue(sliderOpts, d3.mouse(node)[0]);
            handleInput(gd, sliderGroup, sliderOpts, normalizedPosition, false);
        });

        $gd.on('mouseup', function() {
            var sliderOpts = getSliderOpts();
            sliderOpts._dragging = false;
            grip.call(Color.fill, sliderOpts.bgcolor);
            $gd.on('mouseup', null);
            $gd.on('mousemove', null);

            gd.emit('plotly_sliderend', {
                slider: sliderOpts,
                step: sliderOpts.steps[sliderOpts.active]
            });
        });
    });
}

function drawTicks(sliderGroup, sliderOpts) {
    var tick = sliderGroup.selectAll('rect.' + constants.tickRectClass)
        .data(sliderOpts._visibleSteps);
    var dims = sliderOpts._dims;

    tick.enter().append('rect')
        .classed(constants.tickRectClass, true);

    tick.exit().remove();

    tick.attr({
        width: sliderOpts.tickwidth + 'px',
        'shape-rendering': 'crispEdges'
    });

    tick.each(function(d, i) {
        var isMajor = i % dims.labelStride === 0;
        var item = d3.select(this);

        item
            .attr({height: isMajor ? sliderOpts.ticklen : sliderOpts.minorticklen})
            .call(Color.fill, isMajor ? sliderOpts.tickcolor : sliderOpts.tickcolor);

        Drawing.setTranslate(item,
            normalizedValueToPosition(sliderOpts, i / (sliderOpts._stepCount - 1)) - 0.5 * sliderOpts.tickwidth,
            (isMajor ? constants.tickOffset : constants.minorTickOffset) + dims.currentValueTotalHeight
        );
    });
}

function computeLabelSteps(sliderOpts) {
    var dims = sliderOpts._dims;
    dims.labelSteps = [];
    var nsteps = sliderOpts._stepCount;

    for(var i = 0; i < nsteps; i += dims.labelStride) {
        dims.labelSteps.push({
            fraction: i / (nsteps - 1),
            step: sliderOpts._visibleSteps[i]
        });
    }
}

function setGripPosition(sliderGroup, sliderOpts, doTransition) {
    var grip = sliderGroup.select('rect.' + constants.gripRectClass);

    var quantizedIndex = 0;
    for(var i = 0; i < sliderOpts._stepCount; i++) {
        if(sliderOpts._visibleSteps[i]._index === sliderOpts.active) {
            quantizedIndex = i;
            break;
        }
    }

    var x = normalizedValueToPosition(sliderOpts, quantizedIndex / (sliderOpts._stepCount - 1));

    // If this is true, then *this component* is already invoking its own command
    // and has triggered its own animation.
    if(sliderOpts._invokingCommand) return;

    var el = grip;
    if(doTransition && sliderOpts.transition.duration > 0) {
        el = el.transition()
            .duration(sliderOpts.transition.duration)
            .ease(sliderOpts.transition.easing);
    }

    // Drawing.setTranslate doesn't work here becasue of the transition duck-typing.
    // It's also not necessary because there are no other transitions to preserve.
    el.attr('transform', 'translate(' + (x - constants.gripWidth * 0.5) + ',' + (sliderOpts._dims.currentValueTotalHeight) + ')');
}

// Convert a number from [0-1] to a pixel position relative to the slider group container:
function normalizedValueToPosition(sliderOpts, normalizedPosition) {
    var dims = sliderOpts._dims;
    return dims.inputAreaStart + constants.stepInset +
        (dims.inputAreaLength - 2 * constants.stepInset) * Math.min(1, Math.max(0, normalizedPosition));
}

// Convert a position relative to the slider group to a nubmer in [0, 1]
function positionToNormalizedValue(sliderOpts, position) {
    var dims = sliderOpts._dims;
    return Math.min(1, Math.max(0, (position - constants.stepInset - dims.inputAreaStart) / (dims.inputAreaLength - 2 * constants.stepInset - 2 * dims.inputAreaStart)));
}

function drawTouchRect(sliderGroup, gd, sliderOpts) {
    var dims = sliderOpts._dims;
    var rect = Lib.ensureSingle(sliderGroup, 'rect', constants.railTouchRectClass, function(s) {
        s.call(attachGripEvents, gd, sliderGroup, sliderOpts)
            .style('pointer-events', 'all');
    });

    rect.attr({
        width: dims.inputAreaLength,
        height: Math.max(dims.inputAreaWidth, constants.tickOffset + sliderOpts.ticklen + dims.labelHeight)
    })
        .call(Color.fill, sliderOpts.bgcolor)
        .attr('opacity', 0);

    Drawing.setTranslate(rect, 0, dims.currentValueTotalHeight);
}

function drawRail(sliderGroup, sliderOpts) {
    var dims = sliderOpts._dims;
    var computedLength = dims.inputAreaLength - constants.railInset * 2;
    var rect = Lib.ensureSingle(sliderGroup, 'rect', constants.railRectClass);

    rect.attr({
        width: computedLength,
        height: constants.railWidth,
        rx: constants.railRadius,
        ry: constants.railRadius,
        'shape-rendering': 'crispEdges'
    })
    .call(Color.stroke, sliderOpts.bordercolor)
    .call(Color.fill, sliderOpts.bgcolor)
    .style('stroke-width', sliderOpts.borderwidth + 'px');

    Drawing.setTranslate(rect,
        constants.railInset,
        (dims.inputAreaWidth - constants.railWidth) * 0.5 + dims.currentValueTotalHeight
    );
}
