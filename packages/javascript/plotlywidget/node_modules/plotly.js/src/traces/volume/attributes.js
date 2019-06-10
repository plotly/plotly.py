/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorScaleAttrs = require('../../components/colorscale/attributes');
var isosurfaceAttrs = require('../isosurface/attributes');
var baseAttrs = require('../../plots/attributes');

var extendFlat = require('../../lib/extend').extendFlat;
var overrideAll = require('../../plot_api/edit_types').overrideAll;

var attrs = module.exports = overrideAll(extendFlat({
    x: isosurfaceAttrs.x,
    y: isosurfaceAttrs.y,
    z: isosurfaceAttrs.z,
    value: isosurfaceAttrs.value,
    isomin: isosurfaceAttrs.isomin,
    isomax: isosurfaceAttrs.isomax,
    surface: isosurfaceAttrs.surface,
    spaceframe: {
        show: {
            valType: 'boolean',
            role: 'info',
            dflt: false,
            description: [
                'Displays/hides tetrahedron shapes between minimum and',
                'maximum iso-values. Often useful when either caps or',
                'surfaces are disabled or filled with values less than 1.'
            ].join(' ')
        },
        fill: {
            valType: 'number',
            role: 'style',
            min: 0,
            max: 1,
            dflt: 1,
            description: [
                'Sets the fill ratio of the `spaceframe` elements. The default fill value',
                'is 1 meaning that they are entirely shaded. Applying a `fill` ratio less',
                'than one would allow the creation of openings parallel to the edges.'
            ].join(' ')
        }
    },

    slices: isosurfaceAttrs.slices,
    caps: isosurfaceAttrs.caps,
    text: isosurfaceAttrs.text,
    hovertext: isosurfaceAttrs.hovertext,
    hovertemplate: isosurfaceAttrs.hovertemplate
},

colorScaleAttrs('', {
    colorAttr: '`value`',
    showScaleDflt: true,
    editTypeOverride: 'calc'
}), {

    colorbar: isosurfaceAttrs.colorbar,
    opacity: isosurfaceAttrs.opacity,
    opacityscale: {
        valType: 'any',
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the opacityscale.',
            ' The opacityscale must be an array containing',
            ' arrays mapping a normalized value to an opacity value.',
            ' At minimum, a mapping for the lowest (0) and highest (1)',
            ' values are required. For example,',
            ' `[[0, 1], [0.5, 0.2], [1, 1]]` means that higher/lower values would have',
            ' higher opacity values and those in the middle would be more transparent',
            ' Alternatively, `opacityscale` may be a palette name string',
            ' of the following list: \'min\', \'max\', \'extremes\' and \'uniform\'.',
            ' The default is \'uniform\'.'
        ].join('')
    },

    lightposition: isosurfaceAttrs.lightposition,
    lighting: isosurfaceAttrs.lighting,
    flatshading: isosurfaceAttrs.flatshading,
    contour: isosurfaceAttrs.contour,

    hoverinfo: extendFlat({}, baseAttrs.hoverinfo)
}), 'calc', 'nested');

attrs.x.editType = attrs.y.editType = attrs.z.editType = attrs.value.editType = 'calc+clearAxisTypes';
attrs.transforms = undefined;
