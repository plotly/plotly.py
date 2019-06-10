/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var overrideAll = require('../../plot_api/edit_types').overrideAll;

var Scene2D = require('./scene2d');
var layoutGlobalAttrs = require('../layout_attributes');
var xmlnsNamespaces = require('../../constants/xmlns_namespaces');
var constants = require('../cartesian/constants');
var Cartesian = require('../cartesian');
var fxAttrs = require('../../components/fx/layout_attributes');
var getSubplotData = require('../get_data').getSubplotData;

exports.name = 'gl2d';

exports.attr = ['xaxis', 'yaxis'];

exports.idRoot = ['x', 'y'];

exports.idRegex = constants.idRegex;

exports.attrRegex = constants.attrRegex;

exports.attributes = require('../cartesian/attributes');

exports.supplyLayoutDefaults = function(layoutIn, layoutOut, fullData) {
    if(!layoutOut._has('cartesian')) {
        Cartesian.supplyLayoutDefaults(layoutIn, layoutOut, fullData);
    }
};

// gl2d uses svg axis attributes verbatim, but overrides editType
// this could potentially be just `layoutAttributes` but it would
// still need special handling somewhere to give it precedence over
// the svg version when both are in use on one plot
exports.layoutAttrOverrides = overrideAll(Cartesian.layoutAttributes, 'plot', 'from-root');

// similar overrides for base plot attributes (and those added by components)
exports.baseLayoutAttrOverrides = overrideAll({
    plot_bgcolor: layoutGlobalAttrs.plot_bgcolor,
    hoverlabel: fxAttrs.hoverlabel
    // dragmode needs calc but only when transitioning TO lasso or select
    // so for now it's left inside _relayout
    // dragmode: fxAttrs.dragmode
}, 'plot', 'nested');

exports.plot = function plot(gd) {
    var fullLayout = gd._fullLayout;
    var fullData = gd._fullData;
    var subplotIds = fullLayout._subplots.gl2d;

    for(var i = 0; i < subplotIds.length; i++) {
        var subplotId = subplotIds[i];
        var subplotObj = fullLayout._plots[subplotId];
        var fullSubplotData = getSubplotData(fullData, 'gl2d', subplotId);

        // ref. to corresp. Scene instance
        var scene = subplotObj._scene2d;

        // If Scene is not instantiated, create one!
        if(scene === undefined) {
            scene = new Scene2D({
                id: subplotId,
                graphDiv: gd,
                container: gd.querySelector('.gl-container'),
                staticPlot: gd._context.staticPlot,
                plotGlPixelRatio: gd._context.plotGlPixelRatio
            },
                fullLayout
            );

            // set ref to Scene instance
            subplotObj._scene2d = scene;
        }

        scene.plot(fullSubplotData, gd.calcdata, fullLayout, gd.layout);
    }
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var oldSceneKeys = oldFullLayout._subplots.gl2d || [];

    for(var i = 0; i < oldSceneKeys.length; i++) {
        var id = oldSceneKeys[i];
        var oldSubplot = oldFullLayout._plots[id];

        // old subplot wasn't gl2d; nothing to do
        if(!oldSubplot._scene2d) continue;

        // if no traces are present, delete gl2d subplot
        var subplotData = getSubplotData(newFullData, 'gl2d', id);
        if(subplotData.length === 0) {
            oldSubplot._scene2d.destroy();
            delete oldFullLayout._plots[id];
        }
    }

    // since we use cartesian interactions, do cartesian clean
    Cartesian.clean.apply(this, arguments);
};

exports.drawFramework = function(gd) {
    if(!gd._context.staticPlot) {
        Cartesian.drawFramework(gd);
    }
};

exports.toSVG = function(gd) {
    var fullLayout = gd._fullLayout;
    var subplotIds = fullLayout._subplots.gl2d;

    for(var i = 0; i < subplotIds.length; i++) {
        var subplot = fullLayout._plots[subplotIds[i]];
        var scene = subplot._scene2d;

        var imageData = scene.toImage('png');
        var image = fullLayout._glimages.append('svg:image');

        image.attr({
            xmlns: xmlnsNamespaces.svg,
            'xlink:href': imageData,
            x: 0,
            y: 0,
            width: '100%',
            height: '100%',
            preserveAspectRatio: 'none'
        });

        scene.destroy();
    }
};

exports.updateFx = function(gd) {
    var fullLayout = gd._fullLayout;
    var subplotIds = fullLayout._subplots.gl2d;

    for(var i = 0; i < subplotIds.length; i++) {
        var subplotObj = fullLayout._plots[subplotIds[i]]._scene2d;
        subplotObj.updateFx(fullLayout.dragmode);
    }
};
