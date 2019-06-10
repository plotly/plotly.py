/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Color = require('../../../components/color');
var axesAttrs = require('../../cartesian/layout_attributes');
var extendFlat = require('../../../lib/extend').extendFlat;
var overrideAll = require('../../../plot_api/edit_types').overrideAll;

module.exports = overrideAll({
    visible: axesAttrs.visible,
    showspikes: {
        valType: 'boolean',
        role: 'info',
        dflt: true,
        description: [
            'Sets whether or not spikes starting from',
            'data points to this axis\' wall are shown on hover.'
        ].join(' ')
    },
    spikesides: {
        valType: 'boolean',
        role: 'info',
        dflt: true,
        description: [
            'Sets whether or not spikes extending from the',
            'projection data points to this axis\' wall boundaries',
            'are shown on hover.'
        ].join(' ')
    },
    spikethickness: {
        valType: 'number',
        role: 'style',
        min: 0,
        dflt: 2,
        description: 'Sets the thickness (in px) of the spikes.'
    },
    spikecolor: {
        valType: 'color',
        role: 'style',
        dflt: Color.defaultLine,
        description: 'Sets the color of the spikes.'
    },
    showbackground: {
        valType: 'boolean',
        role: 'info',
        dflt: false,
        description: [
            'Sets whether or not this axis\' wall',
            'has a background color.'
        ].join(' ')
    },
    backgroundcolor: {
        valType: 'color',
        role: 'style',
        dflt: 'rgba(204, 204, 204, 0.5)',
        description: 'Sets the background color of this axis\' wall.'
    },
    showaxeslabels: {
        valType: 'boolean',
        role: 'info',
        dflt: true,
        description: 'Sets whether or not this axis is labeled'
    },
    color: axesAttrs.color,
    categoryorder: axesAttrs.categoryorder,
    categoryarray: axesAttrs.categoryarray,
    title: axesAttrs.title,
    type: extendFlat({}, axesAttrs.type, {
        values: ['-', 'linear', 'log', 'date', 'category']
    }),
    autorange: axesAttrs.autorange,
    rangemode: axesAttrs.rangemode,
    range: extendFlat({}, axesAttrs.range, {
        items: [
            {valType: 'any', editType: 'plot', impliedEdits: {'^autorange': false}},
            {valType: 'any', editType: 'plot', impliedEdits: {'^autorange': false}}
        ],
        anim: false
    }),
    // ticks
    tickmode: axesAttrs.tickmode,
    nticks: axesAttrs.nticks,
    tick0: axesAttrs.tick0,
    dtick: axesAttrs.dtick,
    tickvals: axesAttrs.tickvals,
    ticktext: axesAttrs.ticktext,
    ticks: axesAttrs.ticks,
    mirror: axesAttrs.mirror,
    ticklen: axesAttrs.ticklen,
    tickwidth: axesAttrs.tickwidth,
    tickcolor: axesAttrs.tickcolor,
    showticklabels: axesAttrs.showticklabels,
    tickfont: axesAttrs.tickfont,
    tickangle: axesAttrs.tickangle,
    tickprefix: axesAttrs.tickprefix,
    showtickprefix: axesAttrs.showtickprefix,
    ticksuffix: axesAttrs.ticksuffix,
    showticksuffix: axesAttrs.showticksuffix,
    showexponent: axesAttrs.showexponent,
    exponentformat: axesAttrs.exponentformat,
    separatethousands: axesAttrs.separatethousands,
    tickformat: axesAttrs.tickformat,
    tickformatstops: axesAttrs.tickformatstops,
    hoverformat: axesAttrs.hoverformat,
    // lines and grids
    showline: axesAttrs.showline,
    linecolor: axesAttrs.linecolor,
    linewidth: axesAttrs.linewidth,
    showgrid: axesAttrs.showgrid,
    gridcolor: extendFlat({}, axesAttrs.gridcolor,  // shouldn't this be on-par with 2D?
        {dflt: 'rgb(204, 204, 204)'}),
    gridwidth: axesAttrs.gridwidth,
    zeroline: axesAttrs.zeroline,
    zerolinecolor: axesAttrs.zerolinecolor,
    zerolinewidth: axesAttrs.zerolinewidth,
    _deprecated: {
        title: axesAttrs._deprecated.title,
        titlefont: axesAttrs._deprecated.titlefont
    }
}, 'plot', 'from-root');
