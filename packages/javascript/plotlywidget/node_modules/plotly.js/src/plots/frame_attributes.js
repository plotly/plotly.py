/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    _isLinkedToArray: 'frames_entry',

    group: {
        valType: 'string',
        role: 'info',
        description: [
            'An identifier that specifies the group to which the frame belongs,',
            'used by animate to select a subset of frames.'
        ].join(' ')
    },
    name: {
        valType: 'string',
        role: 'info',
        description: 'A label by which to identify the frame'
    },
    traces: {
        valType: 'any',
        role: 'info',
        description: [
            'A list of trace indices that identify the respective traces in the',
            'data attribute'
        ].join(' ')
    },
    baseframe: {
        valType: 'string',
        role: 'info',
        description: [
            'The name of the frame into which this frame\'s properties are merged',
            'before applying. This is used to unify properties and avoid needing',
            'to specify the same values for the same properties in multiple frames.'
        ].join(' ')
    },
    data: {
        valType: 'any',
        role: 'object',
        description: [
            'A list of traces this frame modifies. The format is identical to the',
            'normal trace definition.'
        ].join(' ')
    },
    layout: {
        valType: 'any',
        role: 'object',
        description: [
            'Layout properties which this frame modifies. The format is identical',
            'to the normal layout definition.'
        ].join(' ')
    }
};
