/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorAttrs = require('../../components/color/attributes');
var domainAttrs = require('../domain').attributes;
var axesAttrs = require('../cartesian/layout_attributes');

var overrideAll = require('../../plot_api/edit_types').overrideAll;
var extendFlat = require('../../lib/extend').extendFlat;

var ternaryAxesAttrs = {
    title: axesAttrs.title,
    color: axesAttrs.color,
    // ticks
    tickmode: axesAttrs.tickmode,
    nticks: extendFlat({}, axesAttrs.nticks, {dflt: 6, min: 1}),
    tick0: axesAttrs.tick0,
    dtick: axesAttrs.dtick,
    tickvals: axesAttrs.tickvals,
    ticktext: axesAttrs.ticktext,
    ticks: axesAttrs.ticks,
    ticklen: axesAttrs.ticklen,
    tickwidth: axesAttrs.tickwidth,
    tickcolor: axesAttrs.tickcolor,
    showticklabels: axesAttrs.showticklabels,
    showtickprefix: axesAttrs.showtickprefix,
    tickprefix: axesAttrs.tickprefix,
    showticksuffix: axesAttrs.showticksuffix,
    ticksuffix: axesAttrs.ticksuffix,
    showexponent: axesAttrs.showexponent,
    exponentformat: axesAttrs.exponentformat,
    separatethousands: axesAttrs.separatethousands,
    tickfont: axesAttrs.tickfont,
    tickangle: axesAttrs.tickangle,
    tickformat: axesAttrs.tickformat,
    tickformatstops: axesAttrs.tickformatstops,
    hoverformat: axesAttrs.hoverformat,
    // lines and grids
    showline: extendFlat({}, axesAttrs.showline, {dflt: true}),
    linecolor: axesAttrs.linecolor,
    linewidth: axesAttrs.linewidth,
    showgrid: extendFlat({}, axesAttrs.showgrid, {dflt: true}),
    gridcolor: axesAttrs.gridcolor,
    gridwidth: axesAttrs.gridwidth,
    layer: axesAttrs.layer,
    // range
    min: {
        valType: 'number',
        dflt: 0,
        role: 'info',
        min: 0,
        description: [
            'The minimum value visible on this axis.',
            'The maximum is determined by the sum minus the minimum',
            'values of the other two axes. The full view corresponds to',
            'all the minima set to zero.'
        ].join(' ')
    },
    _deprecated: {
        title: axesAttrs._deprecated.title,
        titlefont: axesAttrs._deprecated.titlefont
    }
};

var attrs = module.exports = overrideAll({
    domain: domainAttrs({name: 'ternary'}),

    bgcolor: {
        valType: 'color',
        role: 'style',
        dflt: colorAttrs.background,
        description: 'Set the background color of the subplot'
    },
    sum: {
        valType: 'number',
        role: 'info',
        dflt: 1,
        min: 0,
        description: [
            'The number each triplet should sum to,',
            'and the maximum range of each axis'
        ].join(' ')
    },
    aaxis: ternaryAxesAttrs,
    baxis: ternaryAxesAttrs,
    caxis: ternaryAxesAttrs
}, 'plot', 'from-root');

// set uirevisions outside of `overrideAll` so we can get `editType: none`
attrs.uirevision = {
    valType: 'any',
    role: 'info',
    editType: 'none',
    description: [
        'Controls persistence of user-driven changes in axis `min` and `title`,',
        'if not overridden in the individual axes.',
        'Defaults to `layout.uirevision`.'
    ].join(' ')
};

attrs.aaxis.uirevision = attrs.baxis.uirevision = attrs.caxis.uirevision = {
    valType: 'any',
    role: 'info',
    editType: 'none',
    description: [
        'Controls persistence of user-driven changes in axis `min`,',
        'and `title` if in `editable: true` configuration.',
        'Defaults to `ternary<N>.uirevision`.'
    ].join(' ')
};
