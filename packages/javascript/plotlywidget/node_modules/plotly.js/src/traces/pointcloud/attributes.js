/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var scatterglAttrs = require('../scatter/attributes');

module.exports = {
    x: scatterglAttrs.x,
    y: scatterglAttrs.y,
    xy: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Faster alternative to specifying `x` and `y` separately.',
            'If supplied, it must be a typed `Float32Array` array that',
            'represents points such that `xy[i * 2] = x[i]` and `xy[i * 2 + 1] = y[i]`'
        ].join(' ')
    },
    indices: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'A sequential value, 0..n, supply it to avoid creating this array inside plotting.',
            'If specified, it must be a typed `Int32Array` array.',
            'Its length must be equal to or greater than the number of points.',
            'For the best performance and memory use, create one large `indices` typed array',
            'that is guaranteed to be at least as long as the largest number of points during',
            'use, and reuse it on each `Plotly.restyle()` call.'
        ].join(' ')
    },
    xbounds: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Specify `xbounds` in the shape of `[xMin, xMax] to avoid looping through',
            'the `xy` typed array. Use it in conjunction with `xy` and `ybounds` for the performance benefits.'
        ].join(' ')
    },
    ybounds: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Specify `ybounds` in the shape of `[yMin, yMax] to avoid looping through',
            'the `xy` typed array. Use it in conjunction with `xy` and `xbounds` for the performance benefits.'
        ].join(' ')
    },
    text: scatterglAttrs.text,
    marker: {
        color: {
            valType: 'color',
            arrayOk: false,
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the marker fill color. It accepts a specific color.',
                'If the color is not fully opaque and there are hundreds of thousands',
                'of points, it may cause slower zooming and panning.'
            ].join('')
        },
        opacity: {
            valType: 'number',
            min: 0,
            max: 1,
            dflt: 1,
            arrayOk: false,
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the marker opacity. The default value is `1` (fully opaque).',
                'If the markers are not fully opaque and there are hundreds of thousands',
                'of points, it may cause slower zooming and panning.',
                'Opacity fades the color even if `blend` is left on `false` even if there',
                'is no translucency effect in that case.'
            ].join(' ')
        },
        blend: {
            valType: 'boolean',
            dflt: null,
            role: 'style',
            editType: 'calc',
            description: [
                'Determines if colors are blended together for a translucency effect',
                'in case `opacity` is specified as a value less then `1`.',
                'Setting `blend` to `true` reduces zoom/pan',
                'speed if used with large numbers of points.'
            ].join(' ')
        },
        sizemin: {
            valType: 'number',
            min: 0.1,
            max: 2,
            dflt: 0.5,
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the minimum size (in px) of the rendered marker points, effective when',
                'the `pointcloud` shows a million or more points.'
            ].join(' ')
        },
        sizemax: {
            valType: 'number',
            min: 0.1,
            dflt: 20,
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the maximum size (in px) of the rendered marker points.',
                'Effective when the `pointcloud` shows only few points.'
            ].join(' ')
        },
        border: {
            color: {
                valType: 'color',
                arrayOk: false,
                role: 'style',
                editType: 'calc',
                description: [
                    'Sets the stroke color. It accepts a specific color.',
                    'If the color is not fully opaque and there are hundreds of thousands',
                    'of points, it may cause slower zooming and panning.'
                ].join(' ')
            },
            arearatio: {
                valType: 'number',
                min: 0,
                max: 1,
                dflt: 0,
                role: 'style',
                editType: 'calc',
                description: [
                    'Specifies what fraction of the marker area is covered with the',
                    'border.'
                ].join(' ')
            },
            editType: 'calc'
        },
        editType: 'calc'
    },
    transforms: undefined
};
