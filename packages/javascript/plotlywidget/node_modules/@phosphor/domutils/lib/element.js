"use strict";
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * The namespace for element related utilities.
 */
var ElementExt;
(function (ElementExt) {
    /**
     * Compute the box sizing for an element.
     *
     * @param element - The element of interest.
     *
     * @returns The box sizing data for the specified element.
     */
    function boxSizing(element) {
        var style = window.getComputedStyle(element);
        var bt = parseFloat(style.borderTopWidth) || 0;
        var bl = parseFloat(style.borderLeftWidth) || 0;
        var br = parseFloat(style.borderRightWidth) || 0;
        var bb = parseFloat(style.borderBottomWidth) || 0;
        var pt = parseFloat(style.paddingTop) || 0;
        var pl = parseFloat(style.paddingLeft) || 0;
        var pr = parseFloat(style.paddingRight) || 0;
        var pb = parseFloat(style.paddingBottom) || 0;
        var hs = bl + pl + pr + br;
        var vs = bt + pt + pb + bb;
        return {
            borderTop: bt,
            borderLeft: bl,
            borderRight: br,
            borderBottom: bb,
            paddingTop: pt,
            paddingLeft: pl,
            paddingRight: pr,
            paddingBottom: pb,
            horizontalSum: hs,
            verticalSum: vs
        };
    }
    ElementExt.boxSizing = boxSizing;
    /**
     * Compute the size limits for an element.
     *
     * @param element - The element of interest.
     *
     * @returns The size limit data for the specified element.
     */
    function sizeLimits(element) {
        var style = window.getComputedStyle(element);
        var minWidth = parseFloat(style.minWidth) || 0;
        var minHeight = parseFloat(style.minHeight) || 0;
        var maxWidth = parseFloat(style.maxWidth) || Infinity;
        var maxHeight = parseFloat(style.maxHeight) || Infinity;
        maxWidth = Math.max(minWidth, maxWidth);
        maxHeight = Math.max(minHeight, maxHeight);
        return { minWidth: minWidth, minHeight: minHeight, maxWidth: maxWidth, maxHeight: maxHeight };
    }
    ElementExt.sizeLimits = sizeLimits;
    /**
     * Test whether a client position lies within an element.
     *
     * @param element - The DOM element of interest.
     *
     * @param clientX - The client X coordinate of interest.
     *
     * @param clientY - The client Y coordinate of interest.
     *
     * @returns Whether the point is within the given element.
     */
    function hitTest(element, clientX, clientY) {
        var rect = element.getBoundingClientRect();
        return (clientX >= rect.left &&
            clientX < rect.right &&
            clientY >= rect.top &&
            clientY < rect.bottom);
    }
    ElementExt.hitTest = hitTest;
    /**
     * Vertically scroll an element into view if needed.
     *
     * @param area - The scroll area element.
     *
     * @param element - The element of interest.
     *
     * #### Notes
     * This follows the "nearest" behavior of the native `scrollIntoView`
     * method, which is not supported by all browsers.
     * https://drafts.csswg.org/cssom-view/#element-scrolling-members
     *
     * If the element fully covers the visible area or is fully contained
     * within the visible area, no scrolling will take place. Otherwise,
     * the nearest edges of the area and element are aligned.
     */
    function scrollIntoViewIfNeeded(area, element) {
        var ar = area.getBoundingClientRect();
        var er = element.getBoundingClientRect();
        if (er.top <= ar.top && er.bottom >= ar.bottom) {
            return;
        }
        if (er.top < ar.top && er.height <= ar.height) {
            area.scrollTop -= ar.top - er.top;
            return;
        }
        if (er.bottom > ar.bottom && er.height >= ar.height) {
            area.scrollTop -= ar.top - er.top;
            return;
        }
        if (er.top < ar.top && er.height > ar.height) {
            area.scrollTop -= ar.bottom - er.bottom;
            return;
        }
        if (er.bottom > ar.bottom && er.height < ar.height) {
            area.scrollTop -= ar.bottom - er.bottom;
            return;
        }
    }
    ElementExt.scrollIntoViewIfNeeded = scrollIntoViewIfNeeded;
})(ElementExt = exports.ElementExt || (exports.ElementExt = {}));
