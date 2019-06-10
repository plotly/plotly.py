/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Lib = require('../../../lib');
var Color = require('../../../components/color');
var Registry = require('../../../registry');

var handleSubplotDefaults = require('../../subplot_defaults');
var supplyGl3dAxisLayoutDefaults = require('./axis_defaults');
var layoutAttributes = require('./layout_attributes');
var getSubplotData = require('../../get_data').getSubplotData;

var GL3D = 'gl3d';

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut, fullData) {
    var hasNon3D = layoutOut._basePlotModules.length > 1;

    // some layout-wide attribute are used in all scenes
    // if 3D is the only visible plot type
    function getDfltFromLayout(attr) {
        if(hasNon3D) return;

        var isValid = Lib.validate(layoutIn[attr], layoutAttributes[attr]);
        if(isValid) return layoutIn[attr];
    }

    handleSubplotDefaults(layoutIn, layoutOut, fullData, {
        type: GL3D,
        attributes: layoutAttributes,
        handleDefaults: handleGl3dDefaults,
        fullLayout: layoutOut,
        font: layoutOut.font,
        fullData: fullData,
        getDfltFromLayout: getDfltFromLayout,
        paper_bgcolor: layoutOut.paper_bgcolor,
        calendar: layoutOut.calendar
    });
};

function handleGl3dDefaults(sceneLayoutIn, sceneLayoutOut, coerce, opts) {
    /*
     * Scene numbering proceeds as follows
     * scene
     * scene2
     * scene3
     *
     * and d.scene will be undefined or some number or number string
     *
     * Also write back a blank scene object to user layout so that some
     * attributes like aspectratio can be written back dynamically.
     */

    var bgcolor = coerce('bgcolor');
    var bgColorCombined = Color.combine(bgcolor, opts.paper_bgcolor);

    var cameraKeys = ['up', 'center', 'eye'];

    for(var j = 0; j < cameraKeys.length; j++) {
        coerce('camera.' + cameraKeys[j] + '.x');
        coerce('camera.' + cameraKeys[j] + '.y');
        coerce('camera.' + cameraKeys[j] + '.z');
    }

    coerce('camera.projection.type');

    /*
     * coerce to positive number (min 0) but also do not accept 0 (>0 not >=0)
     * note that 0's go false with the !! call
     */
    var hasAspect = !!coerce('aspectratio.x') &&
                    !!coerce('aspectratio.y') &&
                    !!coerce('aspectratio.z');

    var defaultAspectMode = hasAspect ? 'manual' : 'auto';
    var aspectMode = coerce('aspectmode', defaultAspectMode);

    /*
     * We need aspectratio object in all the Layouts as it is dynamically set
     * in the calculation steps, ie, we cant set the correct data now, it happens later.
     * We must also account for the case the user sends bad ratio data with 'manual' set
     * for the mode. In this case we must force change it here as the default coerce
     * misses it above.
     */
    if(!hasAspect) {
        sceneLayoutIn.aspectratio = sceneLayoutOut.aspectratio = {x: 1, y: 1, z: 1};

        if(aspectMode === 'manual') sceneLayoutOut.aspectmode = 'auto';

        /*
         * kind of like autorange - we need the calculated aspectmode back in
         * the input layout or relayout can cause problems later
         */
        sceneLayoutIn.aspectmode = sceneLayoutOut.aspectmode;
    }

    var fullGl3dData = getSubplotData(opts.fullData, GL3D, opts.id);

    supplyGl3dAxisLayoutDefaults(sceneLayoutIn, sceneLayoutOut, {
        font: opts.font,
        scene: opts.id,
        data: fullGl3dData,
        bgColor: bgColorCombined,
        calendar: opts.calendar,
        fullLayout: opts.fullLayout
    });

    Registry.getComponentMethod('annotations3d', 'handleDefaults')(
        sceneLayoutIn, sceneLayoutOut, opts
    );

    var dragmode = opts.getDfltFromLayout('dragmode');

    if(dragmode !== false) {
        if(!dragmode) {
            dragmode = 'orbit';

            if(sceneLayoutIn.camera &&
                sceneLayoutIn.camera.up) {
                var x = sceneLayoutIn.camera.up.x;
                var y = sceneLayoutIn.camera.up.y;
                var z = sceneLayoutIn.camera.up.z;

                if(z !== 0) {
                    if(!x || !y || !z) {
                        dragmode = 'turntable';
                    } else if(z / Math.sqrt(x * x + y * y + z * z) > 0.999) {
                        dragmode = 'turntable';
                    }
                }
            } else {
                dragmode = 'turntable';
            }
        }
    }

    coerce('dragmode', dragmode);
    coerce('hovermode', opts.getDfltFromLayout('hovermode'));
}
