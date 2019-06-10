/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Lib = require('../../lib');

module.exports = {
    moduleType: 'component',
    name: 'annotations3d',

    schema: {
        subplots: {
            scene: {annotations: require('./attributes')}
        }
    },

    layoutAttributes: require('./attributes'),
    handleDefaults: require('./defaults'),
    includeBasePlot: includeGL3D,

    convert: require('./convert'),
    draw: require('./draw')
};

function includeGL3D(layoutIn, layoutOut) {
    var GL3D = Registry.subplotsRegistry.gl3d;
    if(!GL3D) return;

    var attrRegex = GL3D.attrRegex;

    var keys = Object.keys(layoutIn);
    for(var i = 0; i < keys.length; i++) {
        var k = keys[i];
        if(attrRegex.test(k) && (layoutIn[k].annotations || []).length) {
            Lib.pushUnique(layoutOut._basePlotModules, GL3D);
            Lib.pushUnique(layoutOut._subplots.gl3d, k);
        }
    }
}
