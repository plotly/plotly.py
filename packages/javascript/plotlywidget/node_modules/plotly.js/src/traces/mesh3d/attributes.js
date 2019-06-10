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
var surfaceAtts = require('../surface/attributes');
var baseAttrs = require('../../plots/attributes');

var extendFlat = require('../../lib/extend').extendFlat;

module.exports = extendFlat({
    x: {
        valType: 'data_array',
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the X coordinates of the vertices. The nth element of vectors `x`, `y` and `z`',
            'jointly represent the X, Y and Z coordinates of the nth vertex.'
        ].join(' ')
    },
    y: {
        valType: 'data_array',
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the Y coordinates of the vertices. The nth element of vectors `x`, `y` and `z`',
            'jointly represent the X, Y and Z coordinates of the nth vertex.'
        ].join(' ')
    },
    z: {
        valType: 'data_array',
        editType: 'calc+clearAxisTypes',
        description: [
            'Sets the Z coordinates of the vertices. The nth element of vectors `x`, `y` and `z`',
            'jointly represent the X, Y and Z coordinates of the nth vertex.'
        ].join(' ')
    },

    i: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'A vector of vertex indices, i.e. integer values between 0 and the length of the vertex',
            'vectors, representing the *first* vertex of a triangle. For example, `{i[m], j[m], k[m]}`',
            'together represent face m (triangle m) in the mesh, where `i[m] = n` points to the triplet',
            '`{x[n], y[n], z[n]}` in the vertex arrays. Therefore, each element in `i` represents a',
            'point in space, which is the first vertex of a triangle.'
        ].join(' ')
    },
    j: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'A vector of vertex indices, i.e. integer values between 0 and the length of the vertex',
            'vectors, representing the *second* vertex of a triangle. For example, `{i[m], j[m], k[m]}` ',
            'together represent face m (triangle m) in the mesh, where `j[m] = n` points to the triplet',
            '`{x[n], y[n], z[n]}` in the vertex arrays. Therefore, each element in `j` represents a',
            'point in space, which is the second vertex of a triangle.'
        ].join(' ')

    },
    k: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'A vector of vertex indices, i.e. integer values between 0 and the length of the vertex',
            'vectors, representing the *third* vertex of a triangle. For example, `{i[m], j[m], k[m]}`',
            'together represent face m (triangle m) in the mesh, where `k[m] = n` points to the triplet ',
            '`{x[n], y[n], z[n]}` in the vertex arrays. Therefore, each element in `k` represents a',
            'point in space, which is the third vertex of a triangle.'
        ].join(' ')

    },

    text: {
        valType: 'string',
        role: 'info',
        dflt: '',
        arrayOk: true,
        editType: 'calc',
        description: [
            'Sets the text elements associated with the vertices.',
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
    hovertemplate: hovertemplateAttrs({editType: 'calc'}),

    delaunayaxis: {
        valType: 'enumerated',
        role: 'info',
        values: [ 'x', 'y', 'z' ],
        dflt: 'z',
        editType: 'calc',
        description: [
            'Sets the Delaunay axis, which is the axis that is perpendicular to the surface of the',
            'Delaunay triangulation.',
            'It has an effect if `i`, `j`, `k` are not provided and `alphahull` is set to indicate',
            'Delaunay triangulation.'
        ].join(' ')
    },

    alphahull: {
        valType: 'number',
        role: 'style',
        dflt: -1,
        editType: 'calc',
        description: [
            'Determines how the mesh surface triangles are derived from the set of',
            'vertices (points) represented by the `x`, `y` and `z` arrays, if',
            'the `i`, `j`, `k` arrays are not supplied.',
            'For general use of `mesh3d` it is preferred that `i`, `j`, `k` are',
            'supplied.',

            'If *-1*, Delaunay triangulation is used, which is mainly suitable if the',
            'mesh is a single, more or less layer surface that is perpendicular to `delaunayaxis`.',
            'In case the `delaunayaxis` intersects the mesh surface at more than one point',
            'it will result triangles that are very long in the dimension of `delaunayaxis`.',

            'If *>0*, the alpha-shape algorithm is used. In this case, the positive `alphahull` value',
            'signals the use of the alpha-shape algorithm, _and_ its value',
            'acts as the parameter for the mesh fitting.',

            'If *0*,  the convex-hull algorithm is used. It is suitable for convex bodies',
            'or if the intention is to enclose the `x`, `y` and `z` point set into a convex',
            'hull.'
        ].join(' ')
    },

    intensity: {
        valType: 'data_array',
        editType: 'calc',
        description: [
            'Sets the vertex intensity values,',
            'used for plotting fields on meshes'
        ].join(' ')
    },

    // Color field
    color: {
        valType: 'color',
        role: 'style',
        editType: 'calc',
        description: 'Sets the color of the whole mesh'
    },
    vertexcolor: {
        valType: 'data_array',
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the color of each vertex',
            'Overrides *color*. While Red, green and blue colors',
            'are in the range of 0 and 255; in the case of having',
            'vertex color data in RGBA format, the alpha color',
            'should be normalized to be between 0 and 1.'
        ].join(' ')
    },
    facecolor: {
        valType: 'data_array',
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the color of each face',
            'Overrides *color* and *vertexcolor*.'
        ].join(' ')
    },
    transforms: undefined
},

colorScaleAttrs('', {
    colorAttr: '`intensity`',
    showScaleDflt: true,
    editTypeOverride: 'calc'
}), {
    opacity: surfaceAtts.opacity,

    // Flat shaded mode
    flatshading: {
        valType: 'boolean',
        role: 'style',
        dflt: false,
        editType: 'calc',
        description: [
            'Determines whether or not normal smoothing is applied to the meshes,',
            'creating meshes with an angular, low-poly look via flat reflections.'
        ].join(' ')
    },

    contour: {
        show: extendFlat({}, surfaceAtts.contours.x.show, {
            description: [
                'Sets whether or not dynamic contours are shown on hover'
            ].join(' ')
        }),
        color: surfaceAtts.contours.x.color,
        width: surfaceAtts.contours.x.width,
        editType: 'calc'
    },

    lightposition: {
        x: extendFlat({}, surfaceAtts.lightposition.x, {dflt: 1e5}),
        y: extendFlat({}, surfaceAtts.lightposition.y, {dflt: 1e5}),
        z: extendFlat({}, surfaceAtts.lightposition.z, {dflt: 0}),
        editType: 'calc'
    },
    lighting: extendFlat({
        vertexnormalsepsilon: {
            valType: 'number',
            role: 'style',
            min: 0.00,
            max: 1,
            dflt: 1e-12, // otherwise finely tessellated things eg. the brain will have no specular light reflection
            editType: 'calc',
            description: 'Epsilon for vertex normals calculation avoids math issues arising from degenerate geometry.'
        },
        facenormalsepsilon: {
            valType: 'number',
            role: 'style',
            min: 0.00,
            max: 1,
            dflt: 1e-6, // even the brain model doesn't appear to need finer than this
            editType: 'calc',
            description: 'Epsilon for face normals calculation avoids math issues arising from degenerate geometry.'
        },
        editType: 'calc'
    }, surfaceAtts.lighting),

    hoverinfo: extendFlat({}, baseAttrs.hoverinfo, {editType: 'calc'})
});
