/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var heatmapAttrs = require('../heatmap/attributes');
var contourAttrs = require('../contour/attributes');
var contourContourAttrs = contourAttrs.contours;
var scatterAttrs = require('../scatter/attributes');
var colorScaleAttrs = require('../../components/colorscale/attributes');

var extendFlat = require('../../lib/extend').extendFlat;

var scatterLineAttrs = scatterAttrs.line;

module.exports = extendFlat({
    carpet: {
        valType: 'string',
        role: 'info',
        editType: 'calc',
        description: [
            'The `carpet` of the carpet axes on which this contour trace lies'
        ].join(' ')
    },
    z: heatmapAttrs.z,
    a: heatmapAttrs.x,
    a0: heatmapAttrs.x0,
    da: heatmapAttrs.dx,
    b: heatmapAttrs.y,
    b0: heatmapAttrs.y0,
    db: heatmapAttrs.dy,
    text: heatmapAttrs.text,
    hovertext: heatmapAttrs.hovertext,
    transpose: heatmapAttrs.transpose,
    atype: heatmapAttrs.xtype,
    btype: heatmapAttrs.ytype,

    fillcolor: contourAttrs.fillcolor,

    autocontour: contourAttrs.autocontour,
    ncontours: contourAttrs.ncontours,

    contours: {
        type: contourContourAttrs.type,
        start: contourContourAttrs.start,
        end: contourContourAttrs.end,
        size: contourContourAttrs.size,
        coloring: {
            // from contourAttrs.contours.coloring but no 'heatmap' option
            valType: 'enumerated',
            values: ['fill', 'lines', 'none'],
            dflt: 'fill',
            role: 'style',
            editType: 'calc',
            description: [
                'Determines the coloring method showing the contour values.',
                'If *fill*, coloring is done evenly between each contour level',
                'If *lines*, coloring is done on the contour lines.',
                'If *none*, no coloring is applied on this trace.'
            ].join(' ')
        },
        showlines: contourContourAttrs.showlines,
        showlabels: contourContourAttrs.showlabels,
        labelfont: contourContourAttrs.labelfont,
        labelformat: contourContourAttrs.labelformat,
        operation: contourContourAttrs.operation,
        value: contourContourAttrs.value,
        editType: 'calc',
        impliedEdits: {'autocontour': false}
    },

    line: {
        color: extendFlat({}, scatterLineAttrs.color, {
            description: [
                'Sets the color of the contour level.',
                'Has no if `contours.coloring` is set to *lines*.'
            ].join(' ')
        }),
        width: scatterLineAttrs.width,
        dash: scatterLineAttrs.dash,
        smoothing: extendFlat({}, scatterLineAttrs.smoothing, {
            description: [
                'Sets the amount of smoothing for the contour lines,',
                'where *0* corresponds to no smoothing.'
            ].join(' ')
        }),
        editType: 'plot'
    },
    transforms: undefined
},

    colorScaleAttrs('', {
        cLetter: 'z',
        autoColorDflt: false
    })
);
