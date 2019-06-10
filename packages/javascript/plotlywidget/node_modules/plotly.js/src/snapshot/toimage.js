/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var EventEmitter = require('events').EventEmitter;

var Registry = require('../registry');
var Lib = require('../lib');

var helpers = require('./helpers');
var clonePlot = require('./cloneplot');
var toSVG = require('./tosvg');
var svgToImg = require('./svgtoimg');

/**
 * @param {object} gd figure Object
 * @param {object} opts option object
 * @param opts.format 'jpeg' | 'png' | 'webp' | 'svg'
 */
function toImage(gd, opts) {
    // first clone the GD so we can operate in a clean environment
    var ev = new EventEmitter();

    var clone = clonePlot(gd, {format: 'png'});
    var clonedGd = clone.gd;

    // put the cloned div somewhere off screen before attaching to DOM
    clonedGd.style.position = 'absolute';
    clonedGd.style.left = '-5000px';
    document.body.appendChild(clonedGd);

    function wait() {
        var delay = helpers.getDelay(clonedGd._fullLayout);

        setTimeout(function() {
            var svg = toSVG(clonedGd);

            var canvas = document.createElement('canvas');
            canvas.id = Lib.randstr();

            ev = svgToImg({
                format: opts.format,
                width: clonedGd._fullLayout.width,
                height: clonedGd._fullLayout.height,
                canvas: canvas,
                emitter: ev,
                svg: svg
            });

            ev.clean = function() {
                if(clonedGd) document.body.removeChild(clonedGd);
            };
        }, delay);
    }

    var redrawFunc = helpers.getRedrawFunc(clonedGd);

    Registry.call('plot', clonedGd, clone.data, clone.layout, clone.config)
        .then(redrawFunc)
        .then(wait)
        .catch(function(err) {
            ev.emit('error', err);
        });


    return ev;
}

module.exports = toImage;
