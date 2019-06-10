/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Color = require('../components/color');

var noop = function() {};


/**
 * Prints a no webgl error message into the scene container
 * @param {scene instance} scene
 *
 * Expects 'scene' to have property 'container'
 *
 */
module.exports = function showNoWebGlMsg(scene) {
    for(var prop in scene) {
        if(typeof scene[prop] === 'function') scene[prop] = noop;
    }

    scene.destroy = function() {
        scene.container.parentNode.removeChild(scene.container);
    };

    var div = document.createElement('div');
    div.className = 'no-webgl';
    div.style.cursor = 'pointer';
    div.style.fontSize = '24px';
    div.style.color = Color.defaults[0];
    div.style.position = 'absolute';
    div.style.left = div.style.top = '0px';
    div.style.width = div.style.height = '100%';
    div.style['background-color'] = Color.lightLine;
    div.style['z-index'] = 30;

    var p = document.createElement('p');
    p.textContent = 'WebGL is not supported by your browser - visit https://get.webgl.org for more info';
    p.style.position = 'relative';
    p.style.top = '50%';
    p.style.left = '50%';
    p.style.height = '30%';
    p.style.width = '50%';
    p.style.margin = '-15% 0 0 -25%';

    div.appendChild(p);
    scene.container.appendChild(div);
    scene.container.style.background = '#FFFFFF';
    scene.container.onclick = function() {
        window.open('https://get.webgl.org');
    };

    // return before setting up camera and onrender methods
    return false;
};
