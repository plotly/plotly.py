/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var overrideAll = require('../../plot_api/edit_types').overrideAll;
var fxAttrs = require('../../components/fx/layout_attributes');

var Scene = require('./scene');
var getSubplotData = require('../get_data').getSubplotData;
var Lib = require('../../lib');
var xmlnsNamespaces = require('../../constants/xmlns_namespaces');

var GL3D = 'gl3d';
var SCENE = 'scene';


exports.name = GL3D;

exports.attr = SCENE;

exports.idRoot = SCENE;

exports.idRegex = exports.attrRegex = Lib.counterRegex('scene');

exports.attributes = require('./layout/attributes');

exports.layoutAttributes = require('./layout/layout_attributes');

exports.baseLayoutAttrOverrides = overrideAll({
    hoverlabel: fxAttrs.hoverlabel
}, 'plot', 'nested');

exports.supplyLayoutDefaults = require('./layout/defaults');

exports.plot = function plot(gd) {
    var fullLayout = gd._fullLayout;
    var fullData = gd._fullData;
    var sceneIds = fullLayout._subplots[GL3D];

    for(var i = 0; i < sceneIds.length; i++) {
        var sceneId = sceneIds[i];
        var fullSceneData = getSubplotData(fullData, GL3D, sceneId);
        var sceneLayout = fullLayout[sceneId];
        var camera = sceneLayout.camera;
        var scene = sceneLayout._scene;

        if(!scene) {
            scene = new Scene({
                id: sceneId,
                graphDiv: gd,
                container: gd.querySelector('.gl-container'),
                staticPlot: gd._context.staticPlot,
                plotGlPixelRatio: gd._context.plotGlPixelRatio,
                camera: camera
            },
                fullLayout
            );

            // set ref to Scene instance
            sceneLayout._scene = scene;
        }

        // save 'initial' camera view settings for modebar button
        if(!scene.viewInitial) {
            scene.viewInitial = {
                up: {
                    x: camera.up.x,
                    y: camera.up.y,
                    z: camera.up.z
                },
                eye: {
                    x: camera.eye.x,
                    y: camera.eye.y,
                    z: camera.eye.z
                },
                center: {
                    x: camera.center.x,
                    y: camera.center.y,
                    z: camera.center.z
                }
            };
        }

        scene.plot(fullSceneData, fullLayout, gd.layout);
    }
};

exports.clean = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var oldSceneKeys = oldFullLayout._subplots[GL3D] || [];

    for(var i = 0; i < oldSceneKeys.length; i++) {
        var oldSceneKey = oldSceneKeys[i];

        if(!newFullLayout[oldSceneKey] && !!oldFullLayout[oldSceneKey]._scene) {
            oldFullLayout[oldSceneKey]._scene.destroy();

            if(oldFullLayout._infolayer) {
                oldFullLayout._infolayer
                    .selectAll('.annotation-' + oldSceneKey)
                    .remove();
            }
        }
    }
};

exports.toSVG = function(gd) {
    var fullLayout = gd._fullLayout;
    var sceneIds = fullLayout._subplots[GL3D];
    var size = fullLayout._size;

    for(var i = 0; i < sceneIds.length; i++) {
        var sceneLayout = fullLayout[sceneIds[i]];
        var domain = sceneLayout.domain;
        var scene = sceneLayout._scene;

        var imageData = scene.toImage('png');
        var image = fullLayout._glimages.append('svg:image');

        image.attr({
            xmlns: xmlnsNamespaces.svg,
            'xlink:href': imageData,
            x: size.l + size.w * domain.x[0],
            y: size.t + size.h * (1 - domain.y[1]),
            width: size.w * (domain.x[1] - domain.x[0]),
            height: size.h * (domain.y[1] - domain.y[0]),
            preserveAspectRatio: 'none'
        });

        scene.destroy();
    }
};

// clean scene ids, 'scene1' -> 'scene'
exports.cleanId = function cleanId(id) {
    if(!id.match(/^scene[0-9]*$/)) return;

    var sceneNum = id.substr(5);
    if(sceneNum === '1') sceneNum = '';

    return SCENE + sceneNum;
};

exports.updateFx = function(gd) {
    var fullLayout = gd._fullLayout;
    var subplotIds = fullLayout._subplots[GL3D];

    for(var i = 0; i < subplotIds.length; i++) {
        var subplotObj = fullLayout[subplotIds[i]]._scene;
        subplotObj.updateFx(fullLayout.dragmode, fullLayout.hovermode);
    }
};
