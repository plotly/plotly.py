/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var isNumeric = require('fast-isnumeric');

var Plots = require('../../plots/plots');
var Registry = require('../../registry');
var Lib = require('../../lib');
var Drawing = require('../drawing');
var Color = require('../color');
var svgTextUtils = require('../../lib/svg_text_utils');
var interactConstants = require('../../constants/interactions');

module.exports = {
    draw: draw
};

var numStripRE = / [XY][0-9]* /;

/**
 * Titles - (re)draw titles on the axes and plot:
 * @param {DOM element} gd - the graphDiv
 * @param {string} titleClass - the css class of this title
 * @param {object} options - how and what to draw
 *      propContainer - the layout object containing `title` and `titlefont`
 *          attributes that apply to this title
 *      propName - the full name of the title property (for Plotly.relayout)
 *      [traceIndex] - include only if this property applies to one trace
 *          (such as a colorbar title) - then editing pipes to Plotly.restyle
 *          instead of Plotly.relayout
 *      placeholder - placeholder text for an empty editable title
 *      [avoid] {object} - include if this title should move to avoid other elements
 *          selection - d3 selection of elements to avoid
 *          side - which direction to move if there is a conflict
 *          [offsetLeft] - if these elements are subject to a translation
 *              wrt the title element
 *          [offsetTop]
 *      attributes {object} - position and alignment attributes
 *          x - pixels
 *          y - pixels
 *          text-anchor - start|middle|end
 *      transform {object} - how to transform the title after positioning
 *          rotate - degrees
 *          offset - shift up/down in the rotated frame (unused?)
 *      containerGroup - if an svg <g> element already exists to hold this
 *          title, include here. Otherwise it will go in fullLayout._infolayer
 *      _meta {object (optional} - meta key-value to for title with
 *          Lib.templateString, default to fullLayout._meta, if not provided
 *
 *  @return {selection} d3 selection of title container group
 */
function draw(gd, titleClass, options) {
    var cont = options.propContainer;
    var prop = options.propName;
    var placeholder = options.placeholder;
    var traceIndex = options.traceIndex;
    var avoid = options.avoid || {};
    var attributes = options.attributes;
    var transform = options.transform;
    var group = options.containerGroup;

    var fullLayout = gd._fullLayout;

    var opacity = 1;
    var isplaceholder = false;
    var title = cont.title;
    var txt = (title && title.text ? title.text : '').trim();

    var font = title && title.font ? title.font : {};
    var fontFamily = font.family;
    var fontSize = font.size;
    var fontColor = font.color;

    // only make this title editable if we positively identify its property
    // as one that has editing enabled.
    var editAttr;
    if(prop === 'title.text') editAttr = 'titleText';
    else if(prop.indexOf('axis') !== -1) editAttr = 'axisTitleText';
    else if(prop.indexOf('colorbar' !== -1)) editAttr = 'colorbarTitleText';
    var editable = gd._context.edits[editAttr];

    if(txt === '') opacity = 0;
    // look for placeholder text while stripping out numbers from eg X2, Y3
    // this is just for backward compatibility with the old version that had
    // "Click to enter X2 title" and may have gotten saved in some old plots,
    // we don't want this to show up when these are displayed.
    else if(txt.replace(numStripRE, ' % ') === placeholder.replace(numStripRE, ' % ')) {
        opacity = 0.2;
        isplaceholder = true;
        if(!editable) txt = '';
    }

    if(options._meta) {
        txt = Lib.templateString(txt, options._meta);
    } else if(fullLayout._meta) {
        txt = Lib.templateString(txt, fullLayout._meta);
    }

    var elShouldExist = txt || editable;

    if(!group) {
        group = Lib.ensureSingle(fullLayout._infolayer, 'g', 'g-' + titleClass);
    }

    var el = group.selectAll('text')
        .data(elShouldExist ? [0] : []);
    el.enter().append('text');
    el.text(txt)
        // this is hacky, but convertToTspans uses the class
        // to determine whether to rotate mathJax...
        // so we need to clear out any old class and put the
        // correct one (only relevant for colorbars, at least
        // for now) - ie don't use .classed
        .attr('class', titleClass);
    el.exit().remove();

    if(!elShouldExist) return group;

    function titleLayout(titleEl) {
        Lib.syncOrAsync([drawTitle, scootTitle], titleEl);
    }

    function drawTitle(titleEl) {
        var transformVal;

        if(transform) {
            transformVal = '';
            if(transform.rotate) {
                transformVal += 'rotate(' + [transform.rotate, attributes.x, attributes.y] + ')';
            }
            if(transform.offset) {
                transformVal += 'translate(0, ' + transform.offset + ')';
            }
        } else {
            transformVal = null;
        }

        titleEl.attr('transform', transformVal);

        titleEl.style({
            'font-family': fontFamily,
            'font-size': d3.round(fontSize, 2) + 'px',
            fill: Color.rgb(fontColor),
            opacity: opacity * Color.opacity(fontColor),
            'font-weight': Plots.fontWeight
        })
        .attr(attributes)
        .call(svgTextUtils.convertToTspans, gd);

        return Plots.previousPromises(gd);
    }

    function scootTitle(titleElIn) {
        var titleGroup = d3.select(titleElIn.node().parentNode);

        if(avoid && avoid.selection && avoid.side && txt) {
            titleGroup.attr('transform', null);

            // move toward avoid.side (= left, right, top, bottom) if needed
            // can include pad (pixels, default 2)
            var shift = 0;
            var backside = {
                left: 'right',
                right: 'left',
                top: 'bottom',
                bottom: 'top'
            }[avoid.side];
            var shiftSign = (['left', 'top'].indexOf(avoid.side) !== -1) ?
                    -1 : 1;
            var pad = isNumeric(avoid.pad) ? avoid.pad : 2;
            var titlebb = Drawing.bBox(titleGroup.node());
            var paperbb = {
                left: 0,
                top: 0,
                right: fullLayout.width,
                bottom: fullLayout.height
            };
            var maxshift = avoid.maxShift || (
                (paperbb[avoid.side] - titlebb[avoid.side]) *
                ((avoid.side === 'left' || avoid.side === 'top') ? -1 : 1));
            // Prevent the title going off the paper
            if(maxshift < 0) shift = maxshift;
            else {
                // so we don't have to offset each avoided element,
                // give the title the opposite offset
                var offsetLeft = avoid.offsetLeft || 0;
                var offsetTop = avoid.offsetTop || 0;
                titlebb.left -= offsetLeft;
                titlebb.right -= offsetLeft;
                titlebb.top -= offsetTop;
                titlebb.bottom -= offsetTop;

                // iterate over a set of elements (avoid.selection)
                // to avoid collisions with
                avoid.selection.each(function() {
                    var avoidbb = Drawing.bBox(this);

                    if(Lib.bBoxIntersect(titlebb, avoidbb, pad)) {
                        shift = Math.max(shift, shiftSign * (
                            avoidbb[avoid.side] - titlebb[backside]) + pad);
                    }
                });
                shift = Math.min(maxshift, shift);
            }
            if(shift > 0 || maxshift < 0) {
                var shiftTemplate = {
                    left: [-shift, 0],
                    right: [shift, 0],
                    top: [0, -shift],
                    bottom: [0, shift]
                }[avoid.side];
                titleGroup.attr('transform',
                    'translate(' + shiftTemplate + ')');
            }
        }
    }

    el.call(titleLayout);

    function setPlaceholder() {
        opacity = 0;
        isplaceholder = true;
        el.text(placeholder)
            .on('mouseover.opacity', function() {
                d3.select(this).transition()
                    .duration(interactConstants.SHOW_PLACEHOLDER).style('opacity', 1);
            })
            .on('mouseout.opacity', function() {
                d3.select(this).transition()
                    .duration(interactConstants.HIDE_PLACEHOLDER).style('opacity', 0);
            });
    }

    if(editable) {
        if(!txt) setPlaceholder();
        else el.on('.opacity', null);

        el.call(svgTextUtils.makeEditable, {gd: gd})
            .on('edit', function(text) {
                if(traceIndex !== undefined) {
                    Registry.call('_guiRestyle', gd, prop, text, traceIndex);
                } else {
                    Registry.call('_guiRelayout', gd, prop, text);
                }
            })
            .on('cancel', function() {
                this.text(this.attr('data-unformatted'))
                    .call(titleLayout);
            })
            .on('input', function(d) {
                this.text(d || ' ')
                    .call(svgTextUtils.positionText, attributes.x, attributes.y);
            });
    }
    el.classed('js-placeholder', isplaceholder);

    return group;
}
