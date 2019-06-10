/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var showNoWebGlMsg = require('./show_no_webgl_msg');

// Note that this module should be ONLY required into
// files corresponding to regl trace modules
// so that bundles with non-regl only don't include
// regl and all its bytes.
var createRegl = require('regl');

/**
 * Idempotent version of createRegl. Create regl instances
 * in the correct canvases with the correct attributes and
 * options
 *
 * @param {DOM node or object} gd : graph div object
 * @param {array} extensions : list of extension to pass to createRegl
 *
 * @return {boolean} true if all createRegl calls succeeded, false otherwise
 */
module.exports = function prepareRegl(gd, extensions) {
    var fullLayout = gd._fullLayout;
    var success = true;

    fullLayout._glcanvas.each(function(d) {
        if(d.regl) return;
        // only parcoords needs pick layer
        if(d.pick && !fullLayout._has('parcoords')) return;

        try {
            d.regl = createRegl({
                canvas: this,
                attributes: {
                    antialias: !d.pick,
                    preserveDrawingBuffer: true
                },
                pixelRatio: gd._context.plotGlPixelRatio || global.devicePixelRatio,
                extensions: extensions || []
            });
        } catch(e) {
            success = false;
        }

        if(success) {
            this.addEventListener('webglcontextlost', function(event) {
                if(gd && gd.emit) {
                    gd.emit('plotly_webglcontextlost', {
                        event: event,
                        layer: d.key
                    });
                }
            }, false);
        }
    });

    if(!success) {
        showNoWebGlMsg({container: fullLayout._glcontainer.node()});
    }
    return success;
};
