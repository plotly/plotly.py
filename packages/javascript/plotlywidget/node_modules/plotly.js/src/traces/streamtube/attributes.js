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
        description: 'Sets the x coordinates of the vector field.'
    },
    y: {
        valType: 'data_array',
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: 'Sets the y coordinates of the vector field.'
    },
    z: {
        valType: 'data_array',
        role: 'info',
        editType: 'calc+clearAxisTypes',
        description: 'Sets the z coordinates of the vector field.'
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

    starts: {
        x: {
            valType: 'data_array',
            editType: 'calc',
            description: [
                'Sets the x components of the starting position of the streamtubes',
            ].join(' ')
        },
        y: {
            valType: 'data_array',
            editType: 'calc',
            description: [
                'Sets the y components of the starting position of the streamtubes',
            ].join(' ')
        },
        z: {
            valType: 'data_array',
            editType: 'calc',
            description: [
                'Sets the z components of the starting position of the streamtubes',
            ].join(' ')
        },
        editType: 'calc'
    },

    maxdisplayed: {
        valType: 'integer',
        min: 0,
        dflt: 1000,
        role: 'info',
        editType: 'calc',
        description: [
            'The maximum number of displayed segments in a streamtube.'
        ].join(' ')
    },

    // TODO
    //
    // Should add 'absolute' (like cone traces have), but currently gl-streamtube3d's
    // `absoluteTubeSize` doesn't behave well enough for our needs.
    //
    // 'fixed' would be a nice addition to plot stream 'lines', see
    // https://github.com/plotly/plotly.js/commit/812be20750e21e0a1831975001c248d365850f73#r29129877
    //
    // sizemode: {
    //     valType: 'enumerated',
    //     values: ['scaled', 'absolute', 'fixed'],
    //     dflt: 'scaled',
    //     role: 'info',
    //     editType: 'calc',
    //     description: [
    //         'Sets the mode by which the streamtubes are sized.'
    //     ].join(' ')
    // },

    sizeref: {
        valType: 'number',
        role: 'info',
        editType: 'calc',
        min: 0,
        dflt: 1,
        description: [
            'The scaling factor for the streamtubes.',
            'The default is 1, which avoids two max divergence tubes from touching',
            'at adjacent starting positions.'
        ].join(' ')
    },

    text: {
        valType: 'string',
        role: 'info',
        dflt: '',
        editType: 'calc',
        description: [
            'Sets a text element associated with this trace.',
            'If trace `hoverinfo` contains a *text* flag,',
            'this text element will be seen in all hover labels.',
            'Note that streamtube traces do not support array `text` values.'
        ].join(' ')
    },
    hovertext: {
        valType: 'string',
        role: 'info',
        dflt: '',
        editType: 'calc',
        description: 'Same as `text`.'
    },
    hovertemplate: hovertemplateAttrs({editType: 'calc'}, {
        keys: [
            'tubex', 'tubey', 'tubez',
            'tubeu', 'tubev', 'tubew',
            'norm', 'divergence'
        ]
    })
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
    flags: ['x', 'y', 'z', 'u', 'v', 'w', 'norm', 'divergence', 'text', 'name'],
    dflt: 'x+y+z+norm+text+name'
});

attrs.transforms = undefined;

module.exports = attrs;
