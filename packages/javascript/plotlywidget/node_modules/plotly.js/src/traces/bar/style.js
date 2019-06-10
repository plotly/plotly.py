/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var Color = require('../../components/color');
var Drawing = require('../../components/drawing');
var Lib = require('../../lib');
var Registry = require('../../registry');

var attributes = require('./attributes');
var attributeTextFont = attributes.textfont;
var attributeInsideTextFont = attributes.insidetextfont;
var attributeOutsideTextFont = attributes.outsidetextfont;
var helpers = require('./helpers');

function style(gd, cd) {
    var s = cd ? cd[0].node3 : d3.select(gd).selectAll('g.barlayer').selectAll('g.trace');
    var barcount = s.size();
    var fullLayout = gd._fullLayout;

    // trace styling
    s.style('opacity', function(d) { return d[0].trace.opacity; })

    // for gapless (either stacked or neighboring grouped) bars use
    // crispEdges to turn off antialiasing so an artificial gap
    // isn't introduced.
    .each(function(d) {
        if((fullLayout.barmode === 'stack' && barcount > 1) ||
                (fullLayout.bargap === 0 &&
                 fullLayout.bargroupgap === 0 &&
                 !d[0].trace.marker.line.width)) {
            d3.select(this).attr('shape-rendering', 'crispEdges');
        }
    });

    s.selectAll('g.points').each(function(d) {
        var sel = d3.select(this);
        var trace = d[0].trace;
        stylePoints(sel, trace, gd);
    });

    Registry.getComponentMethod('errorbars', 'style')(s);
}

function stylePoints(sel, trace, gd) {
    Drawing.pointStyle(sel.selectAll('path'), trace, gd);
    styleTextPoints(sel, trace, gd);
}

function styleTextPoints(sel, trace, gd) {
    sel.selectAll('text').each(function(d) {
        var tx = d3.select(this);
        var font = determineFont(tx, d, trace, gd);
        Drawing.font(tx, font);
    });
}

function styleOnSelect(gd, cd) {
    var s = cd[0].node3;
    var trace = cd[0].trace;

    if(trace.selectedpoints) {
        stylePointsInSelectionMode(s, trace, gd);
    } else {
        stylePoints(s, trace, gd);

        Registry.getComponentMethod('errorbars', 'style')(s);
    }
}

function stylePointsInSelectionMode(s, trace, gd) {
    Drawing.selectedPointStyle(s.selectAll('path'), trace);
    styleTextInSelectionMode(s.selectAll('text'), trace, gd);
}

function styleTextInSelectionMode(txs, trace, gd) {
    txs.each(function(d) {
        var tx = d3.select(this);
        var font;

        if(d.selected) {
            font = Lib.extendFlat({}, determineFont(tx, d, trace, gd));

            var selectedFontColor = trace.selected.textfont && trace.selected.textfont.color;
            if(selectedFontColor) {
                font.color = selectedFontColor;
            }

            Drawing.font(tx, font);
        } else {
            Drawing.selectedTextStyle(tx, trace);
        }
    });
}

function determineFont(tx, d, trace, gd) {
    var layoutFont = gd._fullLayout.font;
    var textFont = trace.textfont;

    if(tx.classed('bartext-inside')) {
        var barColor = getBarColor(d, trace);
        textFont = getInsideTextFont(trace, d.i, layoutFont, barColor);
    } else if(tx.classed('bartext-outside')) {
        textFont = getOutsideTextFont(trace, d.i, layoutFont);
    }

    return textFont;
}

function getTextFont(trace, index, defaultValue) {
    return getFontValue(
      attributeTextFont, trace.textfont, index, defaultValue);
}

function getInsideTextFont(trace, index, layoutFont, barColor) {
    var defaultFont = getTextFont(trace, index, layoutFont);

    var wouldFallBackToLayoutFont =
      (trace._input.textfont === undefined || trace._input.textfont.color === undefined) ||
      (Array.isArray(trace.textfont.color) && trace.textfont.color[index] === undefined);
    if(wouldFallBackToLayoutFont) {
        defaultFont = {
            color: Color.contrast(barColor),
            family: defaultFont.family,
            size: defaultFont.size
        };
    }

    return getFontValue(
      attributeInsideTextFont, trace.insidetextfont, index, defaultFont);
}

function getOutsideTextFont(trace, index, layoutFont) {
    var defaultFont = getTextFont(trace, index, layoutFont);
    return getFontValue(
      attributeOutsideTextFont, trace.outsidetextfont, index, defaultFont);
}

function getFontValue(attributeDefinition, attributeValue, index, defaultValue) {
    attributeValue = attributeValue || {};

    var familyValue = helpers.getValue(attributeValue.family, index);
    var sizeValue = helpers.getValue(attributeValue.size, index);
    var colorValue = helpers.getValue(attributeValue.color, index);

    return {
        family: helpers.coerceString(
          attributeDefinition.family, familyValue, defaultValue.family),
        size: helpers.coerceNumber(
          attributeDefinition.size, sizeValue, defaultValue.size),
        color: helpers.coerceColor(
          attributeDefinition.color, colorValue, defaultValue.color)
    };
}

function getBarColor(cd, trace) {
    if(trace.type === 'waterfall') {
        return trace[cd.dir].marker.color;
    }
    return cd.mc || trace.marker.color;
}

module.exports = {
    style: style,
    styleTextPoints: styleTextPoints,
    styleOnSelect: styleOnSelect,
    getInsideTextFont: getInsideTextFont,
    getOutsideTextFont: getOutsideTextFont,
    getBarColor: getBarColor
};
