/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

/*
 * make a font attribute group
 *
 * @param {object} opts
 *   @param {string}
 *     opts.description: where & how this font is used
 *   @param {optional bool} arrayOk:
 *     should each part (family, size, color) be arrayOk? default false.
 *   @param {string} editType:
 *     the editType for all pieces of this font
 *   @param {optional string} colorEditType:
 *     a separate editType just for color
 *
 * @return {object} attributes object containing {family, size, color} as specified
 */
module.exports = function(opts) {
    var editType = opts.editType;
    var colorEditType = opts.colorEditType;
    if(colorEditType === undefined) colorEditType = editType;
    var attrs = {
        family: {
            valType: 'string',
            role: 'style',
            noBlank: true,
            strict: true,
            editType: editType,
            description: [
                'HTML font family - the typeface that will be applied by the web browser.',
                'The web browser will only be able to apply a font if it is available on the system',
                'which it operates. Provide multiple font families, separated by commas, to indicate',
                'the preference in which to apply fonts if they aren\'t available on the system.',
                'The plotly service (at https://plot.ly or on-premise) generates images on a server,',
                'where only a select number of',
                'fonts are installed and supported.',
                'These include *Arial*, *Balto*, *Courier New*, *Droid Sans*,, *Droid Serif*,',
                '*Droid Sans Mono*, *Gravitas One*, *Old Standard TT*, *Open Sans*, *Overpass*,',
                '*PT Sans Narrow*, *Raleway*, *Times New Roman*.'
            ].join(' ')
        },
        size: {
            valType: 'number',
            role: 'style',
            min: 1,
            editType: editType
        },
        color: {
            valType: 'color',
            role: 'style',
            editType: colorEditType
        },
        editType: editType,
        // blank strings so compress_attributes can remove
        // TODO - that's uber hacky... better solution?
        description: '' + (opts.description || '') + ''
    };

    if(opts.arrayOk) {
        attrs.family.arrayOk = true;
        attrs.size.arrayOk = true;
        attrs.color.arrayOk = true;
    }

    return attrs;
};
