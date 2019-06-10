/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    barmode: {
        valType: 'enumerated',
        values: ['stack', 'overlay'],
        dflt: 'stack',
        role: 'info',
        editType: 'calc',
        description: [
            'Determines how bars at the same location coordinate',
            'are displayed on the graph.',
            'With *stack*, the bars are stacked on top of one another',
            'With *overlay*, the bars are plotted over one another,',
            'you might need to an *opacity* to see multiple bars.'
        ].join(' ')
    },
    bargap: {
        valType: 'number',
        dflt: 0.1,
        min: 0,
        max: 1,
        role: 'style',
        editType: 'calc',
        description: [
            'Sets the gap between bars of',
            'adjacent location coordinates.',
            'Values are unitless, they represent fractions of the minimum difference',
            'in bar positions in the data.'
        ].join(' ')
    }
};
