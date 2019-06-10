/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var Drawing = require('../../components/drawing');
var Registry = require('../../registry');

function style(gd, cd) {
    var s = cd ? cd[0].node3 : d3.select(gd).selectAll('g.trace.scatter');

    s.style('opacity', function(d) {
        return d[0].trace.opacity;
    });

    s.selectAll('g.points').each(function(d) {
        var sel = d3.select(this);
        var trace = d.trace || d[0].trace;
        stylePoints(sel, trace, gd);
    });

    s.selectAll('g.text').each(function(d) {
        var sel = d3.select(this);
        var trace = d.trace || d[0].trace;
        styleText(sel, trace, gd);
    });

    s.selectAll('g.trace path.js-line')
        .call(Drawing.lineGroupStyle);

    s.selectAll('g.trace path.js-fill')
        .call(Drawing.fillGroupStyle);

    Registry.getComponentMethod('errorbars', 'style')(s);
}

function stylePoints(sel, trace, gd) {
    Drawing.pointStyle(sel.selectAll('path.point'), trace, gd);
}

function styleText(sel, trace, gd) {
    Drawing.textPointStyle(sel.selectAll('text'), trace, gd);
}

function styleOnSelect(gd, cd) {
    var s = cd[0].node3;
    var trace = cd[0].trace;

    if(trace.selectedpoints) {
        Drawing.selectedPointStyle(s.selectAll('path.point'), trace);
        Drawing.selectedTextStyle(s.selectAll('text'), trace);
    } else {
        stylePoints(s, trace, gd);
        styleText(s, trace, gd);
    }
}

module.exports = {
    style: style,
    stylePoints: stylePoints,
    styleText: styleText,
    styleOnSelect: styleOnSelect
};
