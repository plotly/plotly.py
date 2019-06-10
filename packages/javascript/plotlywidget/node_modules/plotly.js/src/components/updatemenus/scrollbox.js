/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = ScrollBox;

var d3 = require('d3');

var Color = require('../color');
var Drawing = require('../drawing');

var Lib = require('../../lib');

/**
 * Helper class to setup a scroll box
 *
 * @class
 * @param           gd          Plotly's graph div
 * @param           container   Container to be scroll-boxed (as a D3 selection)
 * @param {string}  id          Id for the clip path to implement the scroll box
 */
function ScrollBox(gd, container, id) {
    this.gd = gd;
    this.container = container;
    this.id = id;

    // See ScrollBox.prototype.enable for further definition
    this.position = null;  // scrollbox position
    this.translateX = null;  // scrollbox horizontal translation
    this.translateY = null;  // scrollbox vertical translation
    this.hbar = null;  // horizontal scrollbar D3 selection
    this.vbar = null;  // vertical scrollbar D3 selection

    // <rect> element to capture pointer events
    this.bg = this.container.selectAll('rect.scrollbox-bg').data([0]);

    this.bg.exit()
        .on('.drag', null)
        .on('wheel', null)
        .remove();

    this.bg.enter().append('rect')
        .classed('scrollbox-bg', true)
        .style('pointer-events', 'all')
        .attr({
            opacity: 0,
            x: 0,
            y: 0,
            width: 0,
            height: 0
        });
}

// scroll bar dimensions
ScrollBox.barWidth = 2;
ScrollBox.barLength = 20;
ScrollBox.barRadius = 2;
ScrollBox.barPad = 1;
ScrollBox.barColor = '#808BA4';

/**
 * If needed, setup a clip path and scrollbars
 *
 * @method
 * @param {Object}  position
 * @param {number}  position.l  Left side position (in pixels)
 * @param {number}  position.t  Top side (in pixels)
 * @param {number}  position.w  Width (in pixels)
 * @param {number}  position.h  Height (in pixels)
 * @param {string}  [position.direction='down']
 *                  Either 'down', 'left', 'right' or 'up'
 * @param {number}  [translateX=0]  Horizontal offset (in pixels)
 * @param {number}  [translateY=0]  Vertical offset (in pixels)
 */
ScrollBox.prototype.enable = function enable(position, translateX, translateY) {
    var fullLayout = this.gd._fullLayout;
    var fullWidth = fullLayout.width;
    var fullHeight = fullLayout.height;

    // compute position of scrollbox
    this.position = position;

    var l = this.position.l;
    var w = this.position.w;
    var t = this.position.t;
    var h = this.position.h;
    var direction = this.position.direction;
    var isDown = (direction === 'down');
    var isLeft = (direction === 'left');
    var isRight = (direction === 'right');
    var isUp = (direction === 'up');
    var boxW = w;
    var boxH = h;
    var boxL, boxR;
    var boxT, boxB;

    if(!isDown && !isLeft && !isRight && !isUp) {
        this.position.direction = 'down';
        isDown = true;
    }

    var isVertical = isDown || isUp;
    if(isVertical) {
        boxL = l;
        boxR = boxL + boxW;

        if(isDown) {
            // anchor to top side
            boxT = t;
            boxB = Math.min(boxT + boxH, fullHeight);
            boxH = boxB - boxT;
        } else {
            // anchor to bottom side
            boxB = t + boxH;
            boxT = Math.max(boxB - boxH, 0);
            boxH = boxB - boxT;
        }
    } else {
        boxT = t;
        boxB = boxT + boxH;

        if(isLeft) {
            // anchor to right side
            boxR = l + boxW;
            boxL = Math.max(boxR - boxW, 0);
            boxW = boxR - boxL;
        } else {
            // anchor to left side
            boxL = l;
            boxR = Math.min(boxL + boxW, fullWidth);
            boxW = boxR - boxL;
        }
    }

    this._box = {
        l: boxL,
        t: boxT,
        w: boxW,
        h: boxH
    };

    // compute position of horizontal scroll bar
    var needsHorizontalScrollBar = (w > boxW);
    var hbarW = ScrollBox.barLength + 2 * ScrollBox.barPad;
    var hbarH = ScrollBox.barWidth + 2 * ScrollBox.barPad;
    // draw horizontal scrollbar on the bottom side
    var hbarL = l;
    var hbarT = t + h;

    if(hbarT + hbarH > fullHeight) hbarT = fullHeight - hbarH;

    var hbar = this.container.selectAll('rect.scrollbar-horizontal').data(
            (needsHorizontalScrollBar) ? [0] : []);

    hbar.exit()
        .on('.drag', null)
        .remove();

    hbar.enter().append('rect')
        .classed('scrollbar-horizontal', true)
        .call(Color.fill, ScrollBox.barColor);

    if(needsHorizontalScrollBar) {
        this.hbar = hbar.attr({
            'rx': ScrollBox.barRadius,
            'ry': ScrollBox.barRadius,
            'x': hbarL,
            'y': hbarT,
            'width': hbarW,
            'height': hbarH
        });

        // hbar center moves between hbarXMin and hbarXMin + hbarTranslateMax
        this._hbarXMin = hbarL + hbarW / 2;
        this._hbarTranslateMax = boxW - hbarW;
    } else {
        delete this.hbar;
        delete this._hbarXMin;
        delete this._hbarTranslateMax;
    }

    // compute position of vertical scroll bar
    var needsVerticalScrollBar = (h > boxH);
    var vbarW = ScrollBox.barWidth + 2 * ScrollBox.barPad;
    var vbarH = ScrollBox.barLength + 2 * ScrollBox.barPad;
    // draw vertical scrollbar on the right side
    var vbarL = l + w;
    var vbarT = t;

    if(vbarL + vbarW > fullWidth) vbarL = fullWidth - vbarW;

    var vbar = this.container.selectAll('rect.scrollbar-vertical').data(
            (needsVerticalScrollBar) ? [0] : []);

    vbar.exit()
        .on('.drag', null)
        .remove();

    vbar.enter().append('rect')
        .classed('scrollbar-vertical', true)
        .call(Color.fill, ScrollBox.barColor);

    if(needsVerticalScrollBar) {
        this.vbar = vbar.attr({
            'rx': ScrollBox.barRadius,
            'ry': ScrollBox.barRadius,
            'x': vbarL,
            'y': vbarT,
            'width': vbarW,
            'height': vbarH
        });

        // vbar center moves between vbarYMin and vbarYMin + vbarTranslateMax
        this._vbarYMin = vbarT + vbarH / 2;
        this._vbarTranslateMax = boxH - vbarH;
    } else {
        delete this.vbar;
        delete this._vbarYMin;
        delete this._vbarTranslateMax;
    }

    // setup a clip path (if scroll bars are needed)
    var clipId = this.id;
    var clipL = boxL - 0.5;
    var clipR = (needsVerticalScrollBar) ? boxR + vbarW + 0.5 : boxR + 0.5;
    var clipT = boxT - 0.5;
    var clipB = (needsHorizontalScrollBar) ? boxB + hbarH + 0.5 : boxB + 0.5;

    var clipPath = fullLayout._topdefs.selectAll('#' + clipId)
        .data((needsHorizontalScrollBar || needsVerticalScrollBar) ? [0] : []);

    clipPath.exit().remove();

    clipPath.enter()
        .append('clipPath').attr('id', clipId)
        .append('rect');

    if(needsHorizontalScrollBar || needsVerticalScrollBar) {
        this._clipRect = clipPath.select('rect').attr({
            x: Math.floor(clipL),
            y: Math.floor(clipT),
            width: Math.ceil(clipR) - Math.floor(clipL),
            height: Math.ceil(clipB) - Math.floor(clipT)
        });

        this.container.call(Drawing.setClipUrl, clipId, this.gd);

        this.bg.attr({
            x: l,
            y: t,
            width: w,
            height: h
        });
    } else {
        this.bg.attr({
            width: 0,
            height: 0
        });
        this.container
            .on('wheel', null)
            .on('.drag', null)
            .call(Drawing.setClipUrl, null);
        delete this._clipRect;
    }

    // set up drag listeners (if scroll bars are needed)
    if(needsHorizontalScrollBar || needsVerticalScrollBar) {
        var onBoxDrag = d3.behavior.drag()
            .on('dragstart', function() {
                d3.event.sourceEvent.preventDefault();
            })
            .on('drag', this._onBoxDrag.bind(this));

        this.container
            .on('wheel', null)
            .on('wheel', this._onBoxWheel.bind(this))
            .on('.drag', null)
            .call(onBoxDrag);

        var onBarDrag = d3.behavior.drag()
            .on('dragstart', function() {
                d3.event.sourceEvent.preventDefault();
                d3.event.sourceEvent.stopPropagation();
            })
            .on('drag', this._onBarDrag.bind(this));

        if(needsHorizontalScrollBar) {
            this.hbar
                .on('.drag', null)
                .call(onBarDrag);
        }

        if(needsVerticalScrollBar) {
            this.vbar
                .on('.drag', null)
                .call(onBarDrag);
        }
    }

    // set scrollbox translation
    this.setTranslate(translateX, translateY);
};

/**
 * If present, remove clip-path and scrollbars
 *
 * @method
 */
ScrollBox.prototype.disable = function disable() {
    if(this.hbar || this.vbar) {
        this.bg.attr({
            width: 0,
            height: 0
        });
        this.container
            .on('wheel', null)
            .on('.drag', null)
            .call(Drawing.setClipUrl, null);
        delete this._clipRect;
    }

    if(this.hbar) {
        this.hbar.on('.drag', null);
        this.hbar.remove();
        delete this.hbar;
        delete this._hbarXMin;
        delete this._hbarTranslateMax;
    }

    if(this.vbar) {
        this.vbar.on('.drag', null);
        this.vbar.remove();
        delete this.vbar;
        delete this._vbarYMin;
        delete this._vbarTranslateMax;
    }
};

/**
 * Handles scroll box drag events
 *
 * @method
 */
ScrollBox.prototype._onBoxDrag = function _onBoxDrag() {
    var translateX = this.translateX;
    var translateY = this.translateY;

    if(this.hbar) {
        translateX -= d3.event.dx;
    }

    if(this.vbar) {
        translateY -= d3.event.dy;
    }

    this.setTranslate(translateX, translateY);
};

/**
 * Handles scroll box wheel events
 *
 * @method
 */
ScrollBox.prototype._onBoxWheel = function _onBoxWheel() {
    var translateX = this.translateX;
    var translateY = this.translateY;

    if(this.hbar) {
        translateX += d3.event.deltaY;
    }

    if(this.vbar) {
        translateY += d3.event.deltaY;
    }

    this.setTranslate(translateX, translateY);
};

/**
 * Handles scroll bar drag events
 *
 * @method
 */
ScrollBox.prototype._onBarDrag = function _onBarDrag() {
    var translateX = this.translateX;
    var translateY = this.translateY;

    if(this.hbar) {
        var xMin = translateX + this._hbarXMin;
        var xMax = xMin + this._hbarTranslateMax;
        var x = Lib.constrain(d3.event.x, xMin, xMax);
        var xf = (x - xMin) / (xMax - xMin);

        var translateXMax = this.position.w - this._box.w;

        translateX = xf * translateXMax;
    }

    if(this.vbar) {
        var yMin = translateY + this._vbarYMin;
        var yMax = yMin + this._vbarTranslateMax;
        var y = Lib.constrain(d3.event.y, yMin, yMax);
        var yf = (y - yMin) / (yMax - yMin);

        var translateYMax = this.position.h - this._box.h;

        translateY = yf * translateYMax;
    }

    this.setTranslate(translateX, translateY);
};

/**
 * Set clip path and scroll bar translate transform
 *
 * @method
 * @param {number}  [translateX=0]  Horizontal offset (in pixels)
 * @param {number}  [translateY=0]  Vertical offset (in pixels)
 */
ScrollBox.prototype.setTranslate = function setTranslate(translateX, translateY) {
    // store translateX and translateY (needed by mouse event handlers)
    var translateXMax = this.position.w - this._box.w;
    var translateYMax = this.position.h - this._box.h;

    translateX = Lib.constrain(translateX || 0, 0, translateXMax);
    translateY = Lib.constrain(translateY || 0, 0, translateYMax);

    this.translateX = translateX;
    this.translateY = translateY;

    this.container.call(Drawing.setTranslate,
        this._box.l - this.position.l - translateX,
        this._box.t - this.position.t - translateY);

    if(this._clipRect) {
        this._clipRect.attr({
            x: Math.floor(this.position.l + translateX - 0.5),
            y: Math.floor(this.position.t + translateY - 0.5)
        });
    }

    if(this.hbar) {
        var xf = translateX / translateXMax;

        this.hbar.call(Drawing.setTranslate,
            translateX + xf * this._hbarTranslateMax,
            translateY);
    }

    if(this.vbar) {
        var yf = translateY / translateYMax;

        this.vbar.call(Drawing.setTranslate,
            translateX,
            translateY + yf * this._vbarTranslateMax);
    }
};
