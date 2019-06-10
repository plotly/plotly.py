/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorScaleAttrs = require('../../components/colorscale/attributes');
var hovertemplateAttrs = require('../../components/fx/hovertemplate_attributes');
var mesh3dAttrs = require('../mesh3d/attributes');
var baseAttrs = require('../../plots/attributes');

var extendFlat = require('../../lib/extend').extendFlat;

var attrs = {
    x: {
        valType: 'data_array',
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the x coordinates of the vector field',
            'and of the displayed cones.'
        ].join(' ')
    },
    y: {
        valType: 'data_array',
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the y coordinates of the vector field',
            'and of the displayed cones.'
        ].join(' ')
    },
    z: {
        valType: 'data_array',
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the z coordinates of the vector field',
            'and of the displayed cones.'
        ].join(' ')
    },

    u: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the x components of the vector field.'
    },
    v: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the y components of the vector field.'
    },
    w: {
        valType: 'data_array',
        editType: 'calc',
        description: 'Sets the z components of the vector field.'
    },

    // TODO add way to specify cone positions independently of the vector field
    // provided, similar to MATLAB's coneplot Cx/Cy/Cz meshgrids,
    // see https://www.mathworks.com/help/matlab/ref/coneplot.html
    //
    // Alternatively, if our goal is only to 'fill in gaps' in the vector data,
    // we could try to extend the heatmap 'connectgaps' algorithm to 3D.
    // From AJ: this particular algorithm which amounts to a Poisson equation,
    // both for interpolation and extrapolation - is the right one to use for
    // cones too.  It makes a field with zero divergence, which is a good
    // baseline assumption for vector fields.
    //
    // cones: {
    //     // potential attributes to add:
    //     //
    //     // - meshmode: 'cartesian-product', 'pts', 'grid'
    //     //
    //     // under `meshmode: 'grid'`
    //     // - (x|y|z)grid.start
    //     // - (x|y|z)grid.end
    //     // - (x|y|z)grid.size
    //
    //     x: {
    //         valType: 'data_array',
    //         editType: 'calc',
    //         description: 'Sets the x coordinates of the cones to be displayed.'
    //     },
    //     y: {
    //         valType: 'data_array',
    //         editType: 'calc',
    //         description: 'Sets the y coordinates of the cones to be displayed.'
    //     },
    //     z: {
    //         valType: 'data_array',
    //         editType: 'calc',
    //         description: 'Sets the z coordinates of the cones to be displayed.'
    //     },
    //
    //     editType: 'calc',
    //     description: [
    //         'By setting `cones.x`, `cones.y` and `cones.z` to 1D arrays,',
    //         'plotly creates a mesh using the cartesian product of those 3 arrays.'
    //     ].join(' ')
    // },

    sizemode: {
        valType: 'enumerated',
        values: ['scaled', 'absolute'],
        role: 'info',
        editType: 'calc',
        dflt: 'scaled',
        description: [
            'Determines whether `sizeref` is set as a *scaled* (i.e unitless) scalar',
            '(normalized by the max u/v/w norm in the vector field) or as',
            '*absolute* value (in the same units as the vector field).'
        ].join(' ')
    },
    sizeref: {
        valType: 'number',
        role: 'info',
        editType: 'calc',
        min: 0,
        description: [
            'Adjusts the cone size scaling.',
            'The size of the cones is determined by their u/v/w norm multiplied a factor and `sizeref`.',
            'This factor (computed internally) corresponds to the minimum "time" to travel across',
            'two successive x/y/z positions at the average velocity of those two successive positions.',
            'All cones in a given trace use the same factor.',
            'With `sizemode` set to *scaled*, `sizeref` is unitless, its default value is *0.5*',
            'With `sizemode` set to *absolute*, `sizeref` has the same units as the u/v/w vector field,',
            'its the default value is half the sample\'s maximum vector norm.'
        ].join(' ')
    },

    anchor: {
        valType: 'enumerated',
        role: 'info',
        editType: 'calc',
        values: ['tip', 'tail', 'cm', 'center'],
        dflt: 'cm',
        description: [
            'Sets the cones\' anchor with respect to their x/y/z positions.',
            'Note that *cm* denote the cone\'s center of mass which corresponds to',
            '1/4 from the tail to tip.'
        ].join(' ')
    },

    text: {
        valType: 'string',
        role: 'info',
        dflt: '',
        arrayOk: true,
        editType: 'calc',
        description: [
            'Sets the text elements associated with the cones.',
            'If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,',
            'these elements will be seen in the hover labels.'
        ].join(' ')
    },
    hovertext: {
        valType: 'string',
        role: 'info',
        dflt: '',
        arrayOk: true,
        editType: 'calc',
        description: 'Same as `text`.'
    },
    hovertemplate: hovertemplateAttrs({editType: 'calc'}, {keys: ['norm']})
};

extendFlat(attrs, colorScaleAttrs('', {
    colorAttr: 'u/v/w norm',
    showScaleDflt: true,
    editTypeOverride: 'calc'
}));

var fromMesh3d = ['opacity', 'lightposition', 'lighting'];

fromMesh3d.forEach(function(k) {
    attrs[k] = mesh3dAttrs[k];
});

attrs.hoverinfo = extendFlat({}, baseAttrs.hoverinfo, {
    editType: 'calc',
    flags: ['x', 'y', 'z', 'u', 'v', 'w', 'norm', 'text', 'name'],
    dflt: 'x+y+z+norm+text+name'
});

attrs.transforms = undefined;

module.exports = attrs;
