/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var isNumeric = require('fast-isnumeric');
var isArrayOrTypedArray = require('../../lib').isArrayOrTypedArray;
var tinycolor = require('tinycolor2');

var Color = require('../../components/color');
var helpers = require('./helpers');
var isValidTextValue = require('../../lib').isValidTextValue;

var extendedColorWayList = {};

function calc(gd, trace) {
    var cd = [];

    var fullLayout = gd._fullLayout;
    var hiddenLabels = fullLayout.hiddenlabels || [];

    var labels = trace.labels;
    var colors = trace.marker.colors || [];
    var vals = trace.values;
    var hasVals = isArrayOrTypedArray(vals) && vals.length;

    var i, pt;

    if(trace.dlabel) {
        labels = new Array(vals.length);
        for(i = 0; i < vals.length; i++) {
            labels[i] = String(trace.label0 + i * trace.dlabel);
        }
    }

    var allThisTraceLabels = {};
    var pullColor = makePullColorFn(fullLayout['_' + trace.type + 'colormap']);
    var seriesLen = (hasVals ? vals : labels).length;
    var vTotal = 0;
    var isAggregated = false;

    for(i = 0; i < seriesLen; i++) {
        var v, label, hidden;
        if(hasVals) {
            v = vals[i];
            if(!isNumeric(v)) continue;
            v = +v;
            if(v < 0) continue;
        } else v = 1;

        label = labels[i];
        if(label === undefined || label === '') label = i;
        label = String(label);

        var thisLabelIndex = allThisTraceLabels[label];
        if(thisLabelIndex === undefined) {
            allThisTraceLabels[label] = cd.length;

            hidden = hiddenLabels.indexOf(label) !== -1;

            if(!hidden) vTotal += v;

            cd.push({
                v: v,
                label: label,
                color: pullColor(colors[i], label),
                i: i,
                pts: [i],
                hidden: hidden
            });
        } else {
            isAggregated = true;

            pt = cd[thisLabelIndex];
            pt.v += v;
            pt.pts.push(i);
            if(!pt.hidden) vTotal += v;

            if(pt.color === false && colors[i]) {
                pt.color = pullColor(colors[i], label);
            }
        }
    }

    var shouldSort = (trace.type === 'funnelarea') ? isAggregated : trace.sort;
    if(shouldSort) cd.sort(function(a, b) { return b.v - a.v; });

    // include the sum of all values in the first point
    if(cd[0]) cd[0].vTotal = vTotal;

    // now insert text
    var textinfo = trace.textinfo;
    if(textinfo && textinfo !== 'none') {
        var parts = textinfo.split('+');
        var hasFlag = function(flag) { return parts.indexOf(flag) !== -1; };
        var hasLabel = hasFlag('label');
        var hasText = hasFlag('text');
        var hasValue = hasFlag('value');
        var hasPercent = hasFlag('percent');

        var separators = fullLayout.separators;
        var text;

        for(i = 0; i < cd.length; i++) {
            pt = cd[i];
            text = hasLabel ? [pt.label] : [];
            if(hasText) {
                var tx = helpers.getFirstFilled(trace.text, pt.pts);
                if(isValidTextValue(tx)) text.push(tx);
            }
            if(hasValue) text.push(helpers.formatPieValue(pt.v, separators));
            if(hasPercent) text.push(helpers.formatPiePercent(pt.v / vTotal, separators));
            pt.text = text.join('<br>');
        }
    }

    return cd;
}

function makePullColorFn(colorMap) {
    return function pullColor(color, id) {
        if(!color) return false;

        color = tinycolor(color);
        if(!color.isValid()) return false;

        color = Color.addOpacity(color, color.getAlpha());
        if(!colorMap[id]) colorMap[id] = color;

        return color;
    };
}

/*
 * `calc` filled in (and collated) explicit colors.
 * Now we need to propagate these explicit colors to other traces,
 * and fill in default colors.
 * This is done after sorting, so we pick defaults
 * in the order slices will be displayed
 */
function crossTraceCalc(gd, plotinfo) { // TODO: should we name the second argument opts?
    var desiredType = (plotinfo || {}).type;
    if(!desiredType) desiredType = 'pie';

    var fullLayout = gd._fullLayout;
    var calcdata = gd.calcdata;
    var colorWay = fullLayout[desiredType + 'colorway'];
    var colorMap = fullLayout['_' + desiredType + 'colormap'];

    if(fullLayout['extend' + desiredType + 'colors']) {
        colorWay = generateExtendedColors(colorWay, extendedColorWayList);
    }
    var dfltColorCount = 0;

    for(var i = 0; i < calcdata.length; i++) {
        var cd = calcdata[i];
        var traceType = cd[0].trace.type;
        if(traceType !== desiredType) continue;

        for(var j = 0; j < cd.length; j++) {
            var pt = cd[j];
            if(pt.color === false) {
                // have we seen this label and assigned a color to it in a previous trace?
                if(colorMap[pt.label]) {
                    pt.color = colorMap[pt.label];
                } else {
                    colorMap[pt.label] = pt.color = colorWay[dfltColorCount % colorWay.length];
                    dfltColorCount++;
                }
            }
        }
    }
}

/**
 * pick a default color from the main default set, augmented by
 * itself lighter then darker before repeating
 */
function generateExtendedColors(colorList, extendedColorWays) {
    var i;
    var colorString = JSON.stringify(colorList);
    var colors = extendedColorWays[colorString];
    if(!colors) {
        colors = colorList.slice();

        for(i = 0; i < colorList.length; i++) {
            colors.push(tinycolor(colorList[i]).lighten(20).toHexString());
        }

        for(i = 0; i < colorList.length; i++) {
            colors.push(tinycolor(colorList[i]).darken(20).toHexString());
        }
        extendedColorWays[colorString] = colors;
    }

    return colors;
}

module.exports = {
    calc: calc,
    crossTraceCalc: crossTraceCalc,

    makePullColorFn: makePullColorFn,
    generateExtendedColors: generateExtendedColors
};
