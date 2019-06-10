/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    mode: {
        valType: 'enumerated',
        dflt: 'afterall',
        role: 'info',
        values: ['immediate', 'next', 'afterall'],
        description: [
            'Describes how a new animate call interacts with currently-running',
            'animations. If `immediate`, current animations are interrupted and',
            'the new animation is started. If `next`, the current frame is allowed',
            'to complete, after which the new animation is started. If `afterall`',
            'all existing frames are animated to completion before the new animation',
            'is started.'
        ].join(' ')
    },
    direction: {
        valType: 'enumerated',
        role: 'info',
        values: ['forward', 'reverse'],
        dflt: 'forward',
        description: [
            'The direction in which to play the frames triggered by the animation call'
        ].join(' ')
    },
    fromcurrent: {
        valType: 'boolean',
        dflt: false,
        role: 'info',
        description: [
            'Play frames starting at the current frame instead of the beginning.'
        ].join(' ')
    },
    frame: {
        duration: {
            valType: 'number',
            role: 'info',
            min: 0,
            dflt: 500,
            description: [
                'The duration in milliseconds of each frame. If greater than the frame',
                'duration, it will be limited to the frame duration.'
            ].join(' ')
        },
        redraw: {
            valType: 'boolean',
            role: 'info',
            dflt: true,
            description: [
                'Redraw the plot at completion of the transition. This is desirable',
                'for transitions that include properties that cannot be transitioned,',
                'but may significantly slow down updates that do not require a full',
                'redraw of the plot'
            ].join(' ')
        },
    },
    transition: {
        duration: {
            valType: 'number',
            role: 'info',
            min: 0,
            dflt: 500,
            editType: 'none',
            description: [
                'The duration of the transition, in milliseconds. If equal to zero,',
                'updates are synchronous.'
            ].join(' ')
        },
        easing: {
            valType: 'enumerated',
            dflt: 'cubic-in-out',
            values: [
                'linear',
                'quad',
                'cubic',
                'sin',
                'exp',
                'circle',
                'elastic',
                'back',
                'bounce',
                'linear-in',
                'quad-in',
                'cubic-in',
                'sin-in',
                'exp-in',
                'circle-in',
                'elastic-in',
                'back-in',
                'bounce-in',
                'linear-out',
                'quad-out',
                'cubic-out',
                'sin-out',
                'exp-out',
                'circle-out',
                'elastic-out',
                'back-out',
                'bounce-out',
                'linear-in-out',
                'quad-in-out',
                'cubic-in-out',
                'sin-in-out',
                'exp-in-out',
                'circle-in-out',
                'elastic-in-out',
                'back-in-out',
                'bounce-in-out'
            ],
            role: 'info',
            editType: 'none',
            description: 'The easing function used for the transition'
        },
        ordering: {
            valType: 'enumerated',
            values: ['layout first', 'traces first'],
            dflt: 'layout first',
            role: 'info',
            editType: 'none',
            description: [
                'Determines whether the figure\'s layout or traces smoothly transitions',
                'during updates that make both traces and layout change.'
            ].join(' ')
        }
    }
};
