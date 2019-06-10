/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/**
 * Creates a set of padding attributes.
 *
 * @param {object} opts
 *   @param {string} editType:
 *     the editType for all pieces of this padding definition
 *
 * @return {object} attributes object containing {t, r, b, l} as specified
 */
module.exports = function(opts) {
    var editType = opts.editType;
    return {
        t: {
            valType: 'number',
            dflt: 0,
            role: 'style',
            editType: editType,
            description: 'The amount of padding (in px) along the top of the component.'
        },
        r: {
            valType: 'number',
            dflt: 0,
            role: 'style',
            editType: editType,
            description: 'The amount of padding (in px) on the right side of the component.'
        },
        b: {
            valType: 'number',
            dflt: 0,
            role: 'style',
            editType: editType,
            description: 'The amount of padding (in px) along the bottom of the component.'
        },
        l: {
            valType: 'number',
            dflt: 0,
            role: 'style',
            editType: editType,
            description: 'The amount of padding (in px) on the left side of the component.'
        },
        editType: editType
    };
};
