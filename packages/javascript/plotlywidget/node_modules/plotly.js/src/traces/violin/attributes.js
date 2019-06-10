/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var boxAttrs = require('../box/attributes');
var extendFlat = require('../../lib/extend').extendFlat;

module.exports = {
    y: boxAttrs.y,
    x: boxAttrs.x,
    x0: boxAttrs.x0,
    y0: boxAttrs.y0,
    name: extendFlat({}, boxAttrs.name, {
        description: [
            'Sets the trace name.',
            'The trace name appear as the legend item and on hover.',
            'For violin traces, the name will also be used for the position',
            'coordinate, if `x` and `x0` (`y` and `y0` if horizontal) are',
            'missing and the position axis is categorical.',
            'Note that the trace name is also used as a default value',
            'for attribute `scalegroup` (please see its description for details).'
        ].join(' ')
    }),
    orientation: extendFlat({}, boxAttrs.orientation, {
        description: [
            'Sets the orientation of the violin(s).',
            'If *v* (*h*), the distribution is visualized along',
            'the vertical (horizontal).'
        ].join(' ')
    }),

    bandwidth: {
        valType: 'number',
        min: 0,
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the bandwidth used to compute the kernel density estimate.',
            'By default, the bandwidth is determined by Silverman\'s rule of thumb.'
        ].join(' ')
    },

    scalegroup: {
        valType: 'string',
        role: 'info',
        dflt: '',
        editType: 'calc',
        description: [
            'If there are multiple violins that should be sized according to',
            'to some metric (see `scalemode`), link them by providing a non-empty group id here',
            'shared by every trace in the same group.',
            'If a violin\'s `width` is undefined, `scalegroup` will default to the trace\'s name.',
            'In this case, violins with the same names will be linked together'
        ].join(' ')
    },
    scalemode: {
        valType: 'enumerated',
        values: ['width', 'count'],
        dflt: 'width',
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the metric by which the width of each violin is determined.',
            '*width* means each violin has the same (max) width',
            '*count* means the violins are scaled by the number of sample points making',
            'up each violin.'
        ].join('')
    },

    spanmode: {
        valType: 'enumerated',
        values: ['soft', 'hard', 'manual'],
        dflt: 'soft',
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the method by which the span in data space where the density function will be computed.',
            '*soft* means the span goes from the sample\'s minimum value minus two bandwidths',
            'to the sample\'s maximum value plus two bandwidths.',
            '*hard* means the span goes from the sample\'s minimum to its maximum value.',
            'For custom span settings, use mode *manual* and fill in the `span` attribute.'
        ].join(' ')
    },
    span: {
        valType: 'info_array',
        items: [
            {valType: 'any', editType: 'calc'},
            {valType: 'any', editType: 'calc'}
        ],
        role: 'info',
        editType: 'calc',
        description: [
            'Sets the span in data space for which the density function will be computed.',
            'Has an effect only when `spanmode` is set to *manual*.'
        ].join(' ')
    },

    line: {
        color: {
            valType: 'color',
            role: 'style',
            editType: 'style',
            description: 'Sets the color of line bounding the violin(s).'
        },
        width: {
            valType: 'number',
            role: 'style',
            min: 0,
            dflt: 2,
            editType: 'style',
            description: 'Sets the width (in px) of line bounding the violin(s).'
        },
        editType: 'plot'
    },
    fillcolor: boxAttrs.fillcolor,

    points: extendFlat({}, boxAttrs.boxpoints, {
        description: [
            'If *outliers*, only the sample points lying outside the whiskers',
            'are shown',
            'If *suspectedoutliers*, the outlier points are shown and',
            'points either less than 4*Q1-3*Q3 or greater than 4*Q3-3*Q1',
            'are highlighted (see `outliercolor`)',
            'If *all*, all sample points are shown',
            'If *false*, only the violins are shown with no sample points'
        ].join(' ')
    }),
    jitter: extendFlat({}, boxAttrs.jitter, {
        description: [
            'Sets the amount of jitter in the sample points drawn.',
            'If *0*, the sample points align along the distribution axis.',
            'If *1*, the sample points are drawn in a random jitter of width',
            'equal to the width of the violins.'
        ].join(' ')
    }),
    pointpos: extendFlat({}, boxAttrs.pointpos, {
        description: [
            'Sets the position of the sample points in relation to the violins.',
            'If *0*, the sample points are places over the center of the violins.',
            'Positive (negative) values correspond to positions to the',
            'right (left) for vertical violins and above (below) for horizontal violins.'
        ].join(' ')
    }),

    width: extendFlat({}, boxAttrs.width, {
        description: [
            'Sets the width of the violin in data coordinates.',
            'If *0* (default value) the width is automatically selected based on the positions',
            'of other violin traces in the same subplot.',
        ].join(' ')
    }),

    marker: boxAttrs.marker,
    text: boxAttrs.text,
    hovertext: boxAttrs.hovertext,
    hovertemplate: boxAttrs.hovertemplate,

    box: {
        visible: {
            valType: 'boolean',
            dflt: false,
            role: 'info',
            editType: 'plot',
            description: [
                'Determines if an miniature box plot is drawn inside the violins. '
            ].join(' ')
        },
        width: {
            valType: 'number',
            min: 0,
            max: 1,
            dflt: 0.25,
            role: 'info',
            editType: 'plot',
            description: [
                'Sets the width of the inner box plots relative to',
                'the violins\' width.',
                'For example, with 1, the inner box plots are as wide as the violins.'
            ].join(' ')
        },
        fillcolor: {
            valType: 'color',
            role: 'style',
            editType: 'style',
            description: 'Sets the inner box plot fill color.'
        },
        line: {
            color: {
                valType: 'color',
                role: 'style',
                editType: 'style',
                description: 'Sets the inner box plot bounding line color.'
            },
            width: {
                valType: 'number',
                min: 0,
                role: 'style',
                editType: 'style',
                description: 'Sets the inner box plot bounding line width.'
            },
            editType: 'style'
        },
        editType: 'plot'
    },

    meanline: {
        visible: {
            valType: 'boolean',
            dflt: false,
            role: 'info',
            editType: 'plot',
            description: [
                'Determines if a line corresponding to the sample\'s mean is shown',
                'inside the violins.',
                'If `box.visible` is turned on, the mean line is drawn inside the inner box.',
                'Otherwise, the mean line is drawn from one side of the violin to other.'
            ].join(' ')
        },
        color: {
            valType: 'color',
            role: 'style',
            editType: 'style',
            description: 'Sets the mean line color.'
        },
        width: {
            valType: 'number',
            min: 0,
            role: 'style',
            editType: 'style',
            description: 'Sets the mean line width.'
        },
        editType: 'plot'
    },

    side: {
        valType: 'enumerated',
        values: ['both', 'positive', 'negative'],
        dflt: 'both',
        role: 'info',
        editType: 'calc',
        description: [
            'Determines on which side of the position value the density function making up',
            'one half of a violin is plotted.',
            'Useful when comparing two violin traces under *overlay* mode, where one trace',
            'has `side` set to *positive* and the other to *negative*.'
        ].join(' ')
    },

    offsetgroup: boxAttrs.offsetgroup,
    alignmentgroup: boxAttrs.alignmentgroup,

    selected: boxAttrs.selected,
    unselected: boxAttrs.unselected,

    hoveron: {
        valType: 'flaglist',
        flags: ['violins', 'points', 'kde'],
        dflt: 'violins+points+kde',
        extras: ['all'],
        role: 'info',
        editType: 'style',
        description: [
            'Do the hover effects highlight individual violins',
            'or sample points or the kernel density estimate or any combination of them?'
        ].join(' ')
    }
};
