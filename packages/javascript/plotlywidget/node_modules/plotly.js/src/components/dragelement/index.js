/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var mouseOffset = require('mouse-event-offset');
var hasHover = require('has-hover');
var supportsPassive = require('has-passive-events');

var removeElement = require('../../lib').removeElement;
var constants = require('../../plots/cartesian/constants');
var interactConstants = require('../../constants/interactions');

var dragElement = module.exports = {};

dragElement.align = require('./align');
dragElement.getCursor = require('./cursor');

var unhover = require('./unhover');
dragElement.unhover = unhover.wrapped;
dragElement.unhoverRaw = unhover.raw;

/**
 * Abstracts click & drag interactions
 *
 * During the interaction, a "coverSlip" element - a transparent
 * div covering the whole page - is created, which has two key effects:
 * - Lets you drag beyond the boundaries of the plot itself without
 *   dropping (but if you drag all the way out of the browser window the
 *   interaction will end)
 * - Freezes the cursor: whatever mouse cursor the drag element had when the
 *   interaction started gets copied to the coverSlip for use until mouseup
 *
 * If the user executes a drag bigger than MINDRAG, callbacks will fire as:
 *      prepFn, moveFn (1 or more times), doneFn
 * If the user does not drag enough, prepFn and clickFn will fire.
 *
 * Note: If you cancel contextmenu, clickFn will fire even with a right click
 * (unlike native events) so you'll get a `plotly_click` event. Cancel context eg:
 *    gd.addEventListener('contextmenu', function(e) { e.preventDefault(); });
 * TODO: we should probably turn this into a `config` parameter, so we can fix it
 * such that if you *don't* cancel contextmenu, we can prevent partial drags, which
 * put you in a weird state.
 *
 * If the user clicks multiple times quickly, clickFn will fire each time
 * but numClicks will increase to help you recognize doubleclicks.
 *
 * @param {object} options with keys:
 *      element (required) the DOM element to drag
 *      prepFn (optional) function(event, startX, startY)
 *          executed on mousedown
 *          startX and startY are the clientX and clientY pixel position
 *          of the mousedown event
 *      moveFn (optional) function(dx, dy)
 *          executed on move, ONLY after we've exceeded MINDRAG
 *          (we keep executing moveFn if you move back to where you started)
 *          dx and dy are the net pixel offset of the drag,
 *          dragged is true/false, has the mouse moved enough to
 *          constitute a drag
 *      doneFn (optional) function(e)
 *          executed on mouseup, ONLY if we exceeded MINDRAG (so you can be
 *          sure that moveFn has been called at least once)
 *          numClicks is how many clicks we've registered within
 *          a doubleclick time
 *          e is the original mouseup event
 *      clickFn (optional) function(numClicks, e)
 *          executed on mouseup if we have NOT exceeded MINDRAG (ie moveFn
 *          has not been called at all)
 *          numClicks is how many clicks we've registered within
 *          a doubleclick time
 *          e is the original mousedown event
 *      clampFn (optional, function(dx, dy) return [dx2, dy2])
 *          Provide custom clamping function for small displacements.
 *          By default, clamping is done using `minDrag` to x and y displacements
 *          independently.
 */
dragElement.init = function init(options) {
    var gd = options.gd;
    var numClicks = 1;
    var DBLCLICKDELAY = interactConstants.DBLCLICKDELAY;
    var element = options.element;

    var startX,
        startY,
        newMouseDownTime,
        cursor,
        dragCover,
        initialEvent,
        initialTarget,
        rightClick;

    if(!gd._mouseDownTime) gd._mouseDownTime = 0;

    element.style.pointerEvents = 'all';

    element.onmousedown = onStart;

    if(!supportsPassive) {
        element.ontouchstart = onStart;
    } else {
        if(element._ontouchstart) {
            element.removeEventListener('touchstart', element._ontouchstart);
        }
        element._ontouchstart = onStart;
        element.addEventListener('touchstart', onStart, {passive: false});
    }

    function _clampFn(dx, dy, minDrag) {
        if(Math.abs(dx) < minDrag) dx = 0;
        if(Math.abs(dy) < minDrag) dy = 0;
        return [dx, dy];
    }

    var clampFn = options.clampFn || _clampFn;

    function onStart(e) {
        // make dragging and dragged into properties of gd
        // so that others can look at and modify them
        gd._dragged = false;
        gd._dragging = true;
        var offset = pointerOffset(e);
        startX = offset[0];
        startY = offset[1];
        initialTarget = e.target;
        initialEvent = e;
        rightClick = e.buttons === 2 || e.ctrlKey;

        // fix Fx.hover for touch events
        if(typeof e.clientX === 'undefined' && typeof e.clientY === 'undefined') {
            e.clientX = startX;
            e.clientY = startY;
        }

        newMouseDownTime = (new Date()).getTime();
        if(newMouseDownTime - gd._mouseDownTime < DBLCLICKDELAY) {
            // in a click train
            numClicks += 1;
        } else {
            // new click train
            numClicks = 1;
            gd._mouseDownTime = newMouseDownTime;
        }

        if(options.prepFn) options.prepFn(e, startX, startY);

        if(hasHover && !rightClick) {
            dragCover = coverSlip();
            dragCover.style.cursor = window.getComputedStyle(element).cursor;
        } else if(!hasHover) {
            // document acts as a dragcover for mobile, bc we can't create dragcover dynamically
            dragCover = document;
            cursor = window.getComputedStyle(document.documentElement).cursor;
            document.documentElement.style.cursor = window.getComputedStyle(element).cursor;
        }

        document.addEventListener('mouseup', onDone);
        document.addEventListener('touchend', onDone);

        if(options.dragmode !== false) {
            e.preventDefault();
            document.addEventListener('mousemove', onMove);
            document.addEventListener('touchmove', onMove);
        }

        return;
    }

    function onMove(e) {
        e.preventDefault();

        var offset = pointerOffset(e);
        var minDrag = options.minDrag || constants.MINDRAG;
        var dxdy = clampFn(offset[0] - startX, offset[1] - startY, minDrag);
        var dx = dxdy[0];
        var dy = dxdy[1];

        if(dx || dy) {
            gd._dragged = true;
            dragElement.unhover(gd);
        }

        if(gd._dragged && options.moveFn && !rightClick) {
            gd._dragdata = {
                element: element,
                dx: dx,
                dy: dy
            };
            options.moveFn(dx, dy);
        }

        return;
    }

    function onDone(e) {
        delete gd._dragdata;

        if(options.dragmode !== false) {
            e.preventDefault();
            document.removeEventListener('mousemove', onMove);
            document.removeEventListener('touchmove', onMove);
        }

        document.removeEventListener('mouseup', onDone);
        document.removeEventListener('touchend', onDone);

        if(hasHover) {
            removeElement(dragCover);
        } else if(cursor) {
            dragCover.documentElement.style.cursor = cursor;
            cursor = null;
        }

        if(!gd._dragging) {
            gd._dragged = false;
            return;
        }
        gd._dragging = false;

        // don't count as a dblClick unless the mouseUp is also within
        // the dblclick delay
        if((new Date()).getTime() - gd._mouseDownTime > DBLCLICKDELAY) {
            numClicks = Math.max(numClicks - 1, 1);
        }

        if(gd._dragged) {
            if(options.doneFn) options.doneFn();
        } else {
            if(options.clickFn) options.clickFn(numClicks, initialEvent);

            // If we haven't dragged, this should be a click. But because of the
            // coverSlip changing the element, the natural system might not generate one,
            // so we need to make our own. But right clicks don't normally generate
            // click events, only contextmenu events, which happen on mousedown.
            if(!rightClick) {
                var e2;

                try {
                    e2 = new MouseEvent('click', e);
                } catch(err) {
                    var offset = pointerOffset(e);
                    e2 = document.createEvent('MouseEvents');
                    e2.initMouseEvent('click',
                        e.bubbles, e.cancelable,
                        e.view, e.detail,
                        e.screenX, e.screenY,
                        offset[0], offset[1],
                        e.ctrlKey, e.altKey, e.shiftKey, e.metaKey,
                        e.button, e.relatedTarget);
                }

                initialTarget.dispatchEvent(e2);
            }
        }

        gd._dragging = false;
        gd._dragged = false;
        return;
    }
};

function coverSlip() {
    var cover = document.createElement('div');

    cover.className = 'dragcover';
    var cStyle = cover.style;
    cStyle.position = 'fixed';
    cStyle.left = 0;
    cStyle.right = 0;
    cStyle.top = 0;
    cStyle.bottom = 0;
    cStyle.zIndex = 999999999;
    cStyle.background = 'none';

    document.body.appendChild(cover);

    return cover;
}

dragElement.coverSlip = coverSlip;

function pointerOffset(e) {
    return mouseOffset(
        e.changedTouches ? e.changedTouches[0] : e,
        document.body
    );
}
