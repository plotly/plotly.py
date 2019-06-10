/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');

var Color = require('../color');

var ARROWPATHS = require('./arrow_paths');

/**
 * Add arrowhead(s) to a path or line element
 *
 * @param {d3.selection} el3: a d3-selected line or path element
 *
 * @param {string} ends: 'none', 'start', 'end', or 'start+end' for which ends get arrowheads
 *
 * @param {object} options: style information. Must have all the following:
 * @param {number} options.arrowhead: end head style - see ./arrow_paths
 * @param {number} options.startarrowhead: start head style - see ./arrow_paths
 * @param {number} options.arrowsize: relative size of the end head vs line width
 * @param {number} options.startarrowsize: relative size of the start head vs line width
 * @param {number} options.standoff: distance in px to move the end arrow point from its target
 * @param {number} options.startstandoff: distance in px to move the start arrow point from its target
 * @param {number} options.arrowwidth: width of the arrow line
 * @param {string} options.arrowcolor: color of the arrow line, for the head to match
 *     Note that the opacity of this color is ignored, as it's assumed the container
 *     of both the line and head has opacity applied to it so there isn't greater opacity
 *     where they overlap.
 */
module.exports = function drawArrowHead(el3, ends, options) {
    var el = el3.node();
    var headStyle = ARROWPATHS[options.arrowhead || 0];
    var startHeadStyle = ARROWPATHS[options.startarrowhead || 0];
    var scale = (options.arrowwidth || 1) * (options.arrowsize || 1);
    var startScale = (options.arrowwidth || 1) * (options.startarrowsize || 1);
    var doStart = ends.indexOf('start') >= 0;
    var doEnd = ends.indexOf('end') >= 0;
    var backOff = headStyle.backoff * scale + options.standoff;
    var startBackOff = startHeadStyle.backoff * startScale + options.startstandoff;

    var start, end, startRot, endRot;

    if(el.nodeName === 'line') {
        start = {x: +el3.attr('x1'), y: +el3.attr('y1')};
        end = {x: +el3.attr('x2'), y: +el3.attr('y2')};

        var dx = start.x - end.x;
        var dy = start.y - end.y;

        startRot = Math.atan2(dy, dx);
        endRot = startRot + Math.PI;
        if(backOff && startBackOff) {
            if(backOff + startBackOff > Math.sqrt(dx * dx + dy * dy)) {
                hideLine();
                return;
            }
        }

        if(backOff) {
            if(backOff * backOff > dx * dx + dy * dy) {
                hideLine();
                return;
            }
            var backOffX = backOff * Math.cos(startRot);
            var backOffY = backOff * Math.sin(startRot);

            end.x += backOffX;
            end.y += backOffY;
            el3.attr({x2: end.x, y2: end.y});
        }

        if(startBackOff) {
            if(startBackOff * startBackOff > dx * dx + dy * dy) {
                hideLine();
                return;
            }
            var startBackOffX = startBackOff * Math.cos(startRot);
            var startbackOffY = startBackOff * Math.sin(startRot);

            start.x -= startBackOffX;
            start.y -= startbackOffY;
            el3.attr({x1: start.x, y1: start.y});
        }
    } else if(el.nodeName === 'path') {
        var pathlen = el.getTotalLength();
        // using dash to hide the backOff region of the path.
        // if we ever allow dash for the arrow we'll have to
        // do better than this hack... maybe just manually
        // combine the two
        var dashArray = '';

        if(pathlen < backOff + startBackOff) {
            hideLine();
            return;
        }


        var start0 = el.getPointAtLength(0);
        var dstart = el.getPointAtLength(0.1);

        startRot = Math.atan2(start0.y - dstart.y, start0.x - dstart.x);
        start = el.getPointAtLength(Math.min(startBackOff, pathlen));

        dashArray = '0px,' + startBackOff + 'px,';

        var end0 = el.getPointAtLength(pathlen);
        var dend = el.getPointAtLength(pathlen - 0.1);

        endRot = Math.atan2(end0.y - dend.y, end0.x - dend.x);
        end = el.getPointAtLength(Math.max(0, pathlen - backOff));

        var shortening = dashArray ? startBackOff + backOff : backOff;
        dashArray += (pathlen - shortening) + 'px,' + pathlen + 'px';

        el3.style('stroke-dasharray', dashArray);
    }

    function hideLine() { el3.style('stroke-dasharray', '0px,100px'); }

    function drawhead(arrowHeadStyle, p, rot, arrowScale) {
        if(!arrowHeadStyle.path) return;
        if(arrowHeadStyle.noRotate) rot = 0;

        d3.select(el.parentNode).append('path')
            .attr({
                'class': el3.attr('class'),
                d: arrowHeadStyle.path,
                transform:
                    'translate(' + p.x + ',' + p.y + ')' +
                    (rot ? 'rotate(' + (rot * 180 / Math.PI) + ')' : '') +
                    'scale(' + arrowScale + ')'
            })
            .style({
                fill: Color.rgb(options.arrowcolor),
                'stroke-width': 0
            });
    }

    if(doStart) drawhead(startHeadStyle, start, startRot, startScale);
    if(doEnd) drawhead(headStyle, end, endRot, scale);
};
