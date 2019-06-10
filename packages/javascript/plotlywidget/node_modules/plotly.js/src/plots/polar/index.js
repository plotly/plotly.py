/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var getSubplotCalcData = require('../get_data').getSubplotCalcData;
var counterRegex = require('../../lib').counterRegex;

var createPolar = require('./polar');
var constants = require('./constants');

var attr = constants.attr;
var name = constants.name;
var counter = counterRegex(name);

var attributes = {};
attributes[attr] = {
    valType: 'subplotid',
    role: 'info',
    dflt: name,
    editType: 'calc',
    description: [
        'Sets a reference between this trace\'s data coordinates and',
        'a polar subplot.',
        'If *polar* (the default value), the data refer to `layout.polar`.',
        'If *polar2*, the data refer to `layout.polar2`, and so on.'
    ].join(' ')
};

function plot(gd) {
    var fullLayout = gd._fullLayout;
    var calcData = gd.calcdata;
    var subplotIds = fullLayout._subplots[name];

    for(var i = 0; i < subplotIds.length; i++) {
        var id = subplotIds[i];
        var subplotCalcData = getSubplotCalcData(calcData, name, id);
        var subplot = fullLayout[id]._subplot;

        if(!subplot) {
            subplot = createPolar(gd, id);
            fullLayout[id]._subplot = subplot;
        }

        subplot.plot(subplotCalcData, fullLayout, gd._promises);
    }
}

function clean(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var oldIds = oldFullLayout._subplots[name] || [];
    var hadGl = (oldFullLayout._has && oldFullLayout._has('gl'));
    var hasGl = (newFullLayout._has && newFullLayout._has('gl'));
    var mustCleanScene = hadGl && !hasGl;

    for(var i = 0; i < oldIds.length; i++) {
        var id = oldIds[i];
        var oldSubplot = oldFullLayout[id]._subplot;

        if(!newFullLayout[id] && !!oldSubplot) {
            oldSubplot.framework.remove();
            oldSubplot.layers['radial-axis-title'].remove();

            for(var k in oldSubplot.clipPaths) {
                oldSubplot.clipPaths[k].remove();
            }
        }

        if(mustCleanScene && oldSubplot._scene) {
            oldSubplot._scene.destroy();
            oldSubplot._scene = null;
        }
    }
}

module.exports = {
    attr: attr,
    name: name,
    idRoot: name,
    idRegex: counter,
    attrRegex: counter,
    attributes: attributes,
    layoutAttributes: require('./layout_attributes'),
    supplyLayoutDefaults: require('./layout_defaults'),
    plot: plot,
    clean: clean,
    toSVG: require('../cartesian').toSVG
};
