/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../registry');

exports.getDelay = function(fullLayout) {
    if(!fullLayout._has) return 0;

    return (
        fullLayout._has('gl3d') ||
        fullLayout._has('gl2d') ||
        fullLayout._has('mapbox')
    ) ? 500 : 0;
};

exports.getRedrawFunc = function(gd) {
    return function() {
        var fullLayout = gd._fullLayout || {};
        var hasPolar = fullLayout._has && fullLayout._has('polar');
        var hasLegacyPolar = !hasPolar && gd.data && gd.data[0] && gd.data[0].r;

        if(!hasLegacyPolar) {
            Registry.getComponentMethod('colorbar', 'draw')(gd);
        }
    };
};
