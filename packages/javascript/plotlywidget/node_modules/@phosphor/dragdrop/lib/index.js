"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var disposable_1 = require("@phosphor/disposable");
/**
 * An object which manages a drag-drop operation.
 *
 * A drag object dispatches four different events to drop targets:
 *
 * - `'p-dragenter'` - Dispatched when the mouse enters the target
 *   element. This event must be canceled in order to receive any
 *   of the other events.
 *
 * - `'p-dragover'` - Dispatched when the mouse moves over the drop
 *   target. It must cancel the event and set the `dropAction` to one
 *   of the supported actions in order to receive drop events.
 *
 * - `'p-dragleave'` - Dispatched when the mouse leaves the target
 *   element. This includes moving the mouse into child elements.
 *
 * - `'p-drop'`- Dispatched when the mouse is released over the target
 *   element when the target indicates an appropriate drop action. If
 *   the event is canceled, the indicated drop action is returned to
 *   the initiator through the resolved promise.
 *
 * A drag operation can be terminated at any time by pressing `Escape`
 * or by disposing the drag object.
 *
 * A drag object has the ability to automatically scroll a scrollable
 * element when the mouse is hovered near one of its edges. To enable
 * this, add the `data-p-dragscroll` attribute to any element which
 * the drag object should consider for scrolling.
 *
 * #### Notes
 * This class is designed to be used when dragging and dropping custom
 * data *within* a single application. It is *not* a replacement for
 * the native drag-drop API. Instead, it provides an API which allows
 * drag operations to be initiated programmatically and enables the
 * transfer of arbitrary non-string objects; features which are not
 * possible with the native drag-drop API.
 */
var Drag = (function () {
    /**
     * Construct a new drag object.
     *
     * @param options - The options for initializing the drag.
     */
    function Drag(options) {
        var _this = this;
        /**
         * The scroll loop handler function.
         */
        this._onScrollFrame = function () {
            // Bail early if there is no scroll target.
            if (!_this._scrollTarget) {
                return;
            }
            // Unpack the scroll target.
            var _a = _this._scrollTarget, element = _a.element, edge = _a.edge, distance = _a.distance;
            // Calculate the scroll delta using nonlinear acceleration.
            var d = Private.SCROLL_EDGE_SIZE - distance;
            var f = Math.pow(d / Private.SCROLL_EDGE_SIZE, 2);
            var s = Math.max(1, Math.round(f * Private.SCROLL_EDGE_SIZE));
            // Scroll the element in the specified direction.
            switch (edge) {
                case 'top':
                    element.scrollTop -= s;
                    break;
                case 'left':
                    element.scrollLeft -= s;
                    break;
                case 'right':
                    element.scrollLeft += s;
                    break;
                case 'bottom':
                    element.scrollTop += s;
                    break;
            }
            // Request the next cycle of the scroll loop.
            requestAnimationFrame(_this._onScrollFrame);
        };
        this._disposed = false;
        this._dropAction = 'none';
        this._override = null;
        this._currentTarget = null;
        this._currentElement = null;
        this._promise = null;
        this._scrollTarget = null;
        this._resolve = null;
        this.mimeData = options.mimeData;
        this.dragImage = options.dragImage || null;
        this.proposedAction = options.proposedAction || 'copy';
        this.supportedActions = options.supportedActions || 'all';
        this.source = options.source || null;
    }
    /**
     * Dispose of the resources held by the drag object.
     *
     * #### Notes
     * This will cancel the drag operation if it is active.
     */
    Drag.prototype.dispose = function () {
        // Do nothing if the drag object is already disposed.
        if (this._disposed) {
            return;
        }
        this._disposed = true;
        // If there is a current target, dispatch a drag leave event.
        if (this._currentTarget) {
            var event_1 = Private.createMouseEvent('mouseup', -1, -1);
            Private.dispatchDragLeave(this, this._currentTarget, null, event_1);
        }
        // Finalize the drag object with `'none'`.
        this._finalize('none');
    };
    Object.defineProperty(Drag.prototype, "isDisposed", {
        /**
         * Test whether the drag object is disposed.
         */
        get: function () {
            return this._disposed;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Start the drag operation at the specified client position.
     *
     * @param clientX - The client X position for the drag start.
     *
     * @param clientY - The client Y position for the drag start.
     *
     * @returns A promise which resolves to the result of the drag.
     *
     * #### Notes
     * If the drag has already been started, the promise created by the
     * first call to `start` is returned.
     *
     * If the drag operation has ended, or if the drag object has been
     * disposed, the returned promise will resolve to `'none'`.
     *
     * The drag object will be automatically disposed when drag operation
     * completes. This means `Drag` objects are for single-use only.
     *
     * This method assumes the left mouse button is already held down.
     */
    Drag.prototype.start = function (clientX, clientY) {
        var _this = this;
        // If the drag object is already disposed, resolve to `None`.
        if (this._disposed) {
            return Promise.resolve('none');
        }
        // If the drag has already been started, return the promise.
        if (this._promise) {
            return this._promise;
        }
        // Install the document listeners for the drag object.
        this._addListeners();
        // Attach the drag image at the specified client position.
        this._attachDragImage(clientX, clientY);
        // Create the promise which will be resolved on completion.
        this._promise = new Promise(function (resolve, reject) {
            _this._resolve = resolve;
        });
        // Trigger a fake move event to kick off the drag operation.
        var event = Private.createMouseEvent('mousemove', clientX, clientY);
        document.dispatchEvent(event);
        // Return the pending promise for the drag operation.
        return this._promise;
    };
    /**
     * Handle the DOM events for the drag operation.
     *
     * @param event - The DOM event sent to the drag object.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the document. It should not be
     * called directly by user code.
     */
    Drag.prototype.handleEvent = function (event) {
        switch (event.type) {
            case 'mousemove':
                this._evtMouseMove(event);
                break;
            case 'mouseup':
                this._evtMouseUp(event);
                break;
            case 'keydown':
                this._evtKeyDown(event);
                break;
            default:
                // Stop all other events during drag-drop.
                event.preventDefault();
                event.stopPropagation();
                break;
        }
    };
    /**
     * Handle the `'mousemove'` event for the drag object.
     */
    Drag.prototype._evtMouseMove = function (event) {
        // Stop all input events during drag-drop.
        event.preventDefault();
        event.stopPropagation();
        // Update the current target node and dispatch enter/leave events.
        this._updateCurrentTarget(event);
        // Update the drag scroll element.
        this._updateDragScroll(event);
        // Move the drag image to the specified client position. This is
        // performed *after* dispatching to prevent unnecessary reflows.
        this._moveDragImage(event.clientX, event.clientY);
    };
    /**
     * Handle the `'mouseup'` event for the drag object.
     */
    Drag.prototype._evtMouseUp = function (event) {
        // Stop all input events during drag-drop.
        event.preventDefault();
        event.stopPropagation();
        // Do nothing if the left button is not released.
        if (event.button !== 0) {
            return;
        }
        // Update the current target node and dispatch enter/leave events.
        // This prevents a subtle issue where the DOM mutates under the
        // cursor after the last move event but before the drop event.
        this._updateCurrentTarget(event);
        // If there is no current target, finalize with `'none'`.
        if (!this._currentTarget) {
            this._finalize('none');
            return;
        }
        // If the last drop action was `'none'`, dispatch a leave event
        // to the current target and finalize the drag with `'none'`.
        if (this._dropAction === 'none') {
            Private.dispatchDragLeave(this, this._currentTarget, null, event);
            this._finalize('none');
            return;
        }
        // Dispatch the drop event at the current target and finalize
        // with the resulting drop action.
        var action = Private.dispatchDrop(this, this._currentTarget, event);
        this._finalize(action);
    };
    /**
     * Handle the `'keydown'` event for the drag object.
     */
    Drag.prototype._evtKeyDown = function (event) {
        // Stop all input events during drag-drop.
        event.preventDefault();
        event.stopPropagation();
        // Cancel the drag if `Escape` is pressed.
        if (event.keyCode === 27) {
            this.dispose();
        }
    };
    /**
     * Add the document event listeners for the drag object.
     */
    Drag.prototype._addListeners = function () {
        document.addEventListener('mousedown', this, true);
        document.addEventListener('mousemove', this, true);
        document.addEventListener('mouseup', this, true);
        document.addEventListener('mouseenter', this, true);
        document.addEventListener('mouseleave', this, true);
        document.addEventListener('mouseover', this, true);
        document.addEventListener('mouseout', this, true);
        document.addEventListener('keydown', this, true);
        document.addEventListener('keyup', this, true);
        document.addEventListener('keypress', this, true);
        document.addEventListener('contextmenu', this, true);
    };
    /**
     * Remove the document event listeners for the drag object.
     */
    Drag.prototype._removeListeners = function () {
        document.removeEventListener('mousedown', this, true);
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('mouseup', this, true);
        document.removeEventListener('mouseenter', this, true);
        document.removeEventListener('mouseleave', this, true);
        document.removeEventListener('mouseover', this, true);
        document.removeEventListener('mouseout', this, true);
        document.removeEventListener('keydown', this, true);
        document.removeEventListener('keyup', this, true);
        document.removeEventListener('keypress', this, true);
        document.removeEventListener('contextmenu', this, true);
    };
    /**
     * Update the drag scroll element under the mouse.
     */
    Drag.prototype._updateDragScroll = function (event) {
        // Find the scroll target under the mouse.
        var target = Private.findScrollTarget(event);
        // Bail if there is nothing to scroll.
        if (!this._scrollTarget && !target) {
            return;
        }
        // Start the scroll loop if needed.
        if (!this._scrollTarget) {
            setTimeout(this._onScrollFrame, 500);
        }
        // Update the scroll target.
        this._scrollTarget = target;
    };
    /**
     * Update the current target node using the given mouse event.
     */
    Drag.prototype._updateCurrentTarget = function (event) {
        // Fetch common local state.
        var prevTarget = this._currentTarget;
        var currTarget = this._currentTarget;
        var prevElem = this._currentElement;
        // Find the current indicated element at the given position.
        var currElem = document.elementFromPoint(event.clientX, event.clientY);
        // Update the current element reference.
        this._currentElement = currElem;
        // If the indicated element changes from the previous iteration,
        // and is different from the current target, dispatch the exit
        // event to the target.
        if (currElem !== prevElem && currElem !== currTarget) {
            Private.dispatchDragExit(this, currTarget, currElem, event);
        }
        // If the indicated element changes from the previous iteration,
        // and is different from the current target, dispatch the enter
        // event and compute the new target element.
        if (currElem !== prevElem && currElem !== currTarget) {
            currTarget = Private.dispatchDragEnter(this, currElem, currTarget, event);
        }
        // If the current target element has changed, update the current
        // target reference and dispatch the leave event to the old target.
        if (currTarget !== prevTarget) {
            this._currentTarget = currTarget;
            Private.dispatchDragLeave(this, prevTarget, currTarget, event);
        }
        // Dispatch the drag over event and update the drop action.
        var action = Private.dispatchDragOver(this, currTarget, event);
        this._setDropAction(action);
    };
    /**
     * Attach the drag image element at the specified location.
     *
     * This is a no-op if there is no drag image element.
     */
    Drag.prototype._attachDragImage = function (clientX, clientY) {
        if (!this.dragImage) {
            return;
        }
        this.dragImage.classList.add('p-mod-drag-image');
        var style = this.dragImage.style;
        style.pointerEvents = 'none';
        style.position = 'fixed';
        style.top = clientY + "px";
        style.left = clientX + "px";
        document.body.appendChild(this.dragImage);
    };
    /**
     * Move the drag image element to the specified location.
     *
     * This is a no-op if there is no drag image element.
     */
    Drag.prototype._moveDragImage = function (clientX, clientY) {
        if (!this.dragImage) {
            return;
        }
        var style = this.dragImage.style;
        style.top = clientY + "px";
        style.left = clientX + "px";
    };
    /**
     * Detach the drag image element from the DOM.
     *
     * This is a no-op if there is no drag image element.
     */
    Drag.prototype._detachDragImage = function () {
        if (!this.dragImage) {
            return;
        }
        var parent = this.dragImage.parentNode;
        if (!parent) {
            return;
        }
        parent.removeChild(this.dragImage);
    };
    /**
     * Set the internal drop action state and update the drag cursor.
     */
    Drag.prototype._setDropAction = function (action) {
        action = Private.validateAction(action, this.supportedActions);
        if (this._override && this._dropAction === action) {
            return;
        }
        switch (action) {
            case 'none':
                this._dropAction = action;
                this._override = Drag.overrideCursor('no-drop');
                break;
            case 'copy':
                this._dropAction = action;
                this._override = Drag.overrideCursor('copy');
                break;
            case 'link':
                this._dropAction = action;
                this._override = Drag.overrideCursor('alias');
                break;
            case 'move':
                this._dropAction = action;
                this._override = Drag.overrideCursor('move');
                break;
        }
    };
    /**
     * Finalize the drag operation and resolve the drag promise.
     */
    Drag.prototype._finalize = function (action) {
        // Store the resolve function as a temp variable.
        var resolve = this._resolve;
        // Remove the document event listeners.
        this._removeListeners();
        // Detach the drag image.
        this._detachDragImage();
        // Dispose of the cursor override.
        if (this._override) {
            this._override.dispose();
            this._override = null;
        }
        // Clear the mime data.
        this.mimeData.clear();
        // Clear the rest of the internal drag state.
        this._disposed = true;
        this._dropAction = 'none';
        this._currentTarget = null;
        this._currentElement = null;
        this._scrollTarget = null;
        this._promise = null;
        this._resolve = null;
        // Finally, resolve the promise to the given drop action.
        if (resolve) {
            resolve(action);
        }
    };
    return Drag;
}());
exports.Drag = Drag;
/**
 * The namespace for the `Drag` class statics.
 */
(function (Drag) {
    /**
     * Override the cursor icon for the entire document.
     *
     * @param cursor - The string representing the cursor style.
     *
     * @returns A disposable which will clear the override when disposed.
     *
     * #### Notes
     * The most recent call to `overrideCursor` takes precedence.
     * Disposing an old override has no effect on the current override.
     *
     * This utility function is used by the `Drag` class to override the
     * mouse cursor during a drag-drop operation, but it can also be used
     * by other classes to fix the cursor icon during normal mouse drags.
     *
     * #### Example
     * ```typescript
     * import { Drag } from '@phosphor/dragdrop';
     *
     * // Force the cursor to be 'wait' for the entire document.
     * let override = Drag.overrideCursor('wait');
     *
     * // Clear the override by disposing the return value.
     * override.dispose();
     * ```
     */
    function overrideCursor(cursor) {
        var id = ++overrideCursorID;
        document.body.style.cursor = cursor;
        document.body.classList.add('p-mod-override-cursor');
        return new disposable_1.DisposableDelegate(function () {
            if (id === overrideCursorID) {
                document.body.style.cursor = '';
                document.body.classList.remove('p-mod-override-cursor');
            }
        });
    }
    Drag.overrideCursor = overrideCursor;
    /**
     * The internal id for the active cursor override.
     */
    var overrideCursorID = 0;
})(Drag = exports.Drag || (exports.Drag = {}));
exports.Drag = Drag;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The size of a drag scroll edge, in pixels.
     */
    Private.SCROLL_EDGE_SIZE = 20;
    /**
     * Validate the given action is one of the supported actions.
     *
     * Returns the given action or `'none'` if the action is unsupported.
     */
    function validateAction(action, supported) {
        return (actionTable[action] & supportedTable[supported]) ? action : 'none';
    }
    Private.validateAction = validateAction;
    /**
     * Create a left mouse event at the given position.
     *
     * @param type - The event type for the mouse event.
     *
     * @param clientX - The client X position.
     *
     * @param clientY - The client Y position.
     *
     * @returns A newly created and initialized mouse event.
     */
    function createMouseEvent(type, clientX, clientY) {
        var event = document.createEvent('MouseEvent');
        event.initMouseEvent(type, true, true, window, 0, 0, 0, clientX, clientY, false, false, false, false, 0, null);
        return event;
    }
    Private.createMouseEvent = createMouseEvent;
    /**
     * Find the drag scroll target under the mouse, if any.
     */
    function findScrollTarget(event) {
        // Look up the client mouse position.
        var x = event.clientX;
        var y = event.clientY;
        // Get the element under the mouse.
        var element = document.elementFromPoint(x, y);
        // Search for a scrollable target based on the mouse position.
        // The null assert in third clause of for-loop is required due to:
        // https://github.com/Microsoft/TypeScript/issues/14143
        for (; element; element = element.parentElement) {
            // Ignore elements which are not marked as scrollable.
            if (!element.hasAttribute('data-p-dragscroll')) {
                continue;
            }
            // Set up the coordinate offsets for the element.
            var offsetX = 0;
            var offsetY = 0;
            if (element === document.body) {
                offsetX = window.pageXOffset;
                offsetY = window.pageYOffset;
            }
            // Get the element bounds in viewport coordinates.
            var r = element.getBoundingClientRect();
            var top_1 = r.top + offsetY;
            var left = r.left + offsetX;
            var right = left + r.width;
            var bottom = top_1 + r.height;
            // Skip the element if it's not under the mouse.
            if (x < left || x >= right || y < top_1 || y >= bottom) {
                continue;
            }
            // Compute the distance to each edge.
            var dl = x - left + 1;
            var dt = y - top_1 + 1;
            var dr = right - x;
            var db = bottom - y;
            // Find the smallest of the edge distances.
            var distance = Math.min(dl, dt, dr, db);
            // Skip the element if the mouse is not within a scroll edge.
            if (distance > Private.SCROLL_EDGE_SIZE) {
                continue;
            }
            // Set up the edge result variable.
            var edge = void 0;
            // Find the edge for the computed distance.
            switch (distance) {
                case db:
                    edge = 'bottom';
                    break;
                case dt:
                    edge = 'top';
                    break;
                case dr:
                    edge = 'right';
                    break;
                case dl:
                    edge = 'left';
                    break;
                default:
                    throw 'unreachable';
            }
            // Compute how much the element can scroll in width and height.
            var dsw = element.scrollWidth - element.clientWidth;
            var dsh = element.scrollHeight - element.clientHeight;
            // Determine if the element should be scrolled for the edge.
            var shouldScroll = void 0;
            switch (edge) {
                case 'top':
                    shouldScroll = dsh > 0 && element.scrollTop > 0;
                    break;
                case 'left':
                    shouldScroll = dsw > 0 && element.scrollLeft > 0;
                    break;
                case 'right':
                    shouldScroll = dsw > 0 && element.scrollLeft < dsw;
                    break;
                case 'bottom':
                    shouldScroll = dsh > 0 && element.scrollTop < dsh;
                    break;
                default:
                    throw 'unreachable';
            }
            // Skip the element if it should not be scrolled.
            if (!shouldScroll) {
                continue;
            }
            // Return the drag scroll target.
            return { element: element, edge: edge, distance: distance };
        }
        // No drag scroll target was found.
        return null;
    }
    Private.findScrollTarget = findScrollTarget;
    /**
     * Dispatch a drag enter event to the indicated element.
     *
     * @param drag - The drag object associated with the action.
     *
     * @param currElem - The currently indicated element, or `null`. This
     *   is the "immediate user selection" from the whatwg spec.
     *
     * @param currTarget - The current drag target element, or `null`. This
     *   is the "current target element" from the whatwg spec.
     *
     * @param event - The mouse event related to the action.
     *
     * @returns The element to use as the current drag target. This is the
     *   "current target element" from the whatwg spec, and may be `null`.
     *
     * #### Notes
     * This largely implements the drag enter portion of the whatwg spec:
     * https://html.spec.whatwg.org/multipage/interaction.html#drag-and-drop-processing-model
     */
    function dispatchDragEnter(drag, currElem, currTarget, event) {
        // If the current element is null, return null as the new target.
        if (!currElem) {
            return null;
        }
        // Dispatch a drag enter event to the current element.
        var dragEvent = createDragEvent('p-dragenter', drag, event, currTarget);
        var canceled = !currElem.dispatchEvent(dragEvent);
        // If the event was canceled, use the current element as the new target.
        if (canceled) {
            return currElem;
        }
        // If the current element is the document body, keep the original target.
        if (currElem === document.body) {
            return currTarget;
        }
        // Dispatch a drag enter event on the document body.
        dragEvent = createDragEvent('p-dragenter', drag, event, currTarget);
        document.body.dispatchEvent(dragEvent);
        // Ignore the event cancellation, and use the body as the new target.
        return document.body;
    }
    Private.dispatchDragEnter = dispatchDragEnter;
    /**
     * Dispatch a drag exit event to the indicated element.
     *
     * @param drag - The drag object associated with the action.
     *
     * @param prevTarget - The previous target element, or `null`. This
     *   is the previous "current target element" from the whatwg spec.
     *
     * @param currTarget - The current drag target element, or `null`. This
     *   is the "current target element" from the whatwg spec.
     *
     * @param event - The mouse event related to the action.
     *
     * #### Notes
     * This largely implements the drag exit portion of the whatwg spec:
     * https://html.spec.whatwg.org/multipage/interaction.html#drag-and-drop-processing-model
     */
    function dispatchDragExit(drag, prevTarget, currTarget, event) {
        // If the previous target is null, do nothing.
        if (!prevTarget) {
            return;
        }
        // Dispatch the drag exit event to the previous target.
        var dragEvent = createDragEvent('p-dragexit', drag, event, currTarget);
        prevTarget.dispatchEvent(dragEvent);
    }
    Private.dispatchDragExit = dispatchDragExit;
    /**
     * Dispatch a drag leave event to the indicated element.
     *
     * @param drag - The drag object associated with the action.
     *
     * @param prevTarget - The previous target element, or `null`. This
     *   is the previous "current target element" from the whatwg spec.
     *
     * @param currTarget - The current drag target element, or `null`. This
     *   is the "current target element" from the whatwg spec.
     *
     * @param event - The mouse event related to the action.
     *
     * #### Notes
     * This largely implements the drag leave portion of the whatwg spec:
     * https://html.spec.whatwg.org/multipage/interaction.html#drag-and-drop-processing-model
     */
    function dispatchDragLeave(drag, prevTarget, currTarget, event) {
        // If the previous target is null, do nothing.
        if (!prevTarget) {
            return;
        }
        // Dispatch the drag leave event to the previous target.
        var dragEvent = createDragEvent('p-dragleave', drag, event, currTarget);
        prevTarget.dispatchEvent(dragEvent);
    }
    Private.dispatchDragLeave = dispatchDragLeave;
    /**
     * Dispatch a drag over event to the indicated element.
     *
     * @param drag - The drag object associated with the action.
     *
     * @param currTarget - The current drag target element, or `null`. This
     *   is the "current target element" from the whatwg spec.
     *
     * @param event - The mouse event related to the action.
     *
     * @returns The `DropAction` result of the drag over event.
     *
     * #### Notes
     * This largely implements the drag over portion of the whatwg spec:
     * https://html.spec.whatwg.org/multipage/interaction.html#drag-and-drop-processing-model
     */
    function dispatchDragOver(drag, currTarget, event) {
        // If there is no current target, the drop action is none.
        if (!currTarget) {
            return 'none';
        }
        // Dispatch the drag over event to the current target.
        var dragEvent = createDragEvent('p-dragover', drag, event, null);
        var canceled = !currTarget.dispatchEvent(dragEvent);
        // If the event was canceled, return the drop action result.
        if (canceled) {
            return dragEvent.dropAction;
        }
        // Otherwise, the effective drop action is none.
        return 'none';
    }
    Private.dispatchDragOver = dispatchDragOver;
    /**
     * Dispatch a drop event to the indicated element.
     *
     * @param drag - The drag object associated with the action.
     *
     * @param currTarget - The current drag target element, or `null`. This
     *   is the "current target element" from the whatwg spec.
     *
     * @param event - The mouse event related to the action.
     *
     * @returns The `DropAction` result of the drop event.
     *
     * #### Notes
     * This largely implements the drag over portion of the whatwg spec:
     * https://html.spec.whatwg.org/multipage/interaction.html#drag-and-drop-processing-model
     */
    function dispatchDrop(drag, currTarget, event) {
        // If there is no current target, the drop action is none.
        if (!currTarget) {
            return 'none';
        }
        // Dispatch the drop event to the current target.
        var dragEvent = createDragEvent('p-drop', drag, event, null);
        var canceled = !currTarget.dispatchEvent(dragEvent);
        // If the event was canceled, return the drop action result.
        if (canceled) {
            return dragEvent.dropAction;
        }
        // Otherwise, the effective drop action is none.
        return 'none';
    }
    Private.dispatchDrop = dispatchDrop;
    /**
     * A lookup table from drop action to bit value.
     */
    var actionTable = {
        'none': 0x0,
        'copy': 0x1,
        'link': 0x2,
        'move': 0x4
    };
    /**
     * A lookup table from supported action to drop action bit mask.
     */
    var supportedTable = {
        'none': actionTable['none'],
        'copy': actionTable['copy'],
        'link': actionTable['link'],
        'move': actionTable['move'],
        'copy-link': actionTable['copy'] | actionTable['link'],
        'copy-move': actionTable['copy'] | actionTable['move'],
        'link-move': actionTable['link'] | actionTable['move'],
        'all': actionTable['copy'] | actionTable['link'] | actionTable['move']
    };
    /**
     * Create a new initialized `IDragEvent` from the given data.
     *
     * @param type - The event type for the drag event.
     *
     * @param drag - The drag object to use for seeding the drag data.
     *
     * @param event - The mouse event to use for seeding the mouse data.
     *
     * @param related - The related target for the event, or `null`.
     *
     * @returns A new object which implements `IDragEvent`.
     */
    function createDragEvent(type, drag, event, related) {
        // Create a new mouse event to use as the drag event. Currently,
        // JS engines do now allow user-defined Event subclasses.
        var dragEvent = document.createEvent('MouseEvent');
        // Initialize the mouse event data.
        dragEvent.initMouseEvent(type, true, true, window, 0, event.screenX, event.screenY, event.clientX, event.clientY, event.ctrlKey, event.altKey, event.shiftKey, event.metaKey, event.button, related);
        // Forcefully add the custom drag event properties.
        dragEvent.dropAction = 'none';
        dragEvent.mimeData = drag.mimeData;
        dragEvent.proposedAction = drag.proposedAction;
        dragEvent.supportedActions = drag.supportedActions;
        dragEvent.source = drag.source;
        // Return the fully initialized drag event.
        return dragEvent;
    }
})(Private || (Private = {}));
