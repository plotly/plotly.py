/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';


module.exports = {
    boxmode: {
        valType: 'enumerated',
        values: ['group', 'overlay'],
        dflt: 'overlay',
        role: 'info',
        editType: 'calc',
        description: [
            'Determines how boxes at the same location coordinate',
            'are displayed on the graph.',
            'If *group*, the boxes are plotted next to one another',
            'centered around the shared location.',
            'If *overlay*, the boxes are plotted over one another,',
            'you might need to set *opacity* to see them multiple boxes.',
            'Has no effect on traces that have *width* set.'
        ].join(' ')
    },
    boxgap: {
        valType: 'number',
        min: 0,
        max: 1,
        dflt: 0.3,
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the gap (in plot fraction) between boxes of',
            'adjacent location coordinates.',
            'Has no effect on traces that have *width* set.'
        ].join(' ')
    },
    boxgroupgap: {
        valType: 'number',
        min: 0,
        max: 1,
        dflt: 0.3,
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the gap (in plot fraction) between boxes of',
            'the same location coordinate.',
            'Has no effect on traces that have *width* set.'
        ].join(' ')
    }
};
