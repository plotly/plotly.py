"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var domutils_1 = require("@phosphor/domutils");
var dragdrop_1 = require("@phosphor/dragdrop");
var signaling_1 = require("@phosphor/signaling");
var widget_1 = require("./widget");
/**
 * A widget which implements a canonical scroll bar.
 */
var ScrollBar = (function (_super) {
    __extends(ScrollBar, _super);
    /**
     * Construct a new scroll bar.
     *
     * @param options - The options for initializing the scroll bar.
     */
    function ScrollBar(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, { node: Private.createNode() }) || this;
        /**
         * A timeout callback for repeating the mouse press.
         */
        _this._onRepeat = function () {
            // Clear the repeat timer id.
            _this._repeatTimer = -1;
            // Bail if the mouse has been released.
            if (!_this._pressData) {
                return;
            }
            // Look up the part that was pressed.
            var part = _this._pressData.part;
            // Bail if the thumb was pressed.
            if (part === 'thumb') {
                return;
            }
            // Schedule the timer for another repeat.
            _this._repeatTimer = setTimeout(_this._onRepeat, 20);
            // Get the current mouse position.
            var mouseX = _this._pressData.mouseX;
            var mouseY = _this._pressData.mouseY;
            // Handle a decrement button repeat.
            if (part === 'decrement') {
                // Bail if the mouse is not over the button.
                if (!domutils_1.ElementExt.hitTest(_this.decrementNode, mouseX, mouseY)) {
                    return;
                }
                // Emit the step requested signal.
                _this._stepRequested.emit('decrement');
                // Finished.
                return;
            }
            // Handle an increment button repeat.
            if (part === 'increment') {
                // Bail if the mouse is not over the button.
                if (!domutils_1.ElementExt.hitTest(_this.incrementNode, mouseX, mouseY)) {
                    return;
                }
                // Emit the step requested signal.
                _this._stepRequested.emit('increment');
                // Finished.
                return;
            }
            // Handle a track repeat.
            if (part === 'track') {
                // Bail if the mouse is not over the track.
                if (!domutils_1.ElementExt.hitTest(_this.trackNode, mouseX, mouseY)) {
                    return;
                }
                // Fetch the thumb node.
                var thumbNode = _this.thumbNode;
                // Bail if the mouse is over the thumb.
                if (domutils_1.ElementExt.hitTest(thumbNode, mouseX, mouseY)) {
                    return;
                }
                // Fetch the client rect for the thumb.
                var thumbRect = thumbNode.getBoundingClientRect();
                // Determine the direction for the page request.
                var dir = void 0;
                if (_this._orientation === 'horizontal') {
                    dir = mouseX < thumbRect.left ? 'decrement' : 'increment';
                }
                else {
                    dir = mouseY < thumbRect.top ? 'decrement' : 'increment';
                }
                // Emit the page requested signal.
                _this._pageRequested.emit(dir);
                // Finished.
                return;
            }
        };
        _this._value = 0;
        _this._page = 10;
        _this._maximum = 100;
        _this._repeatTimer = -1;
        _this._pressData = null;
        _this._thumbMoved = new signaling_1.Signal(_this);
        _this._stepRequested = new signaling_1.Signal(_this);
        _this._pageRequested = new signaling_1.Signal(_this);
        _this.addClass('p-ScrollBar');
        _this.setFlag(widget_1.Widget.Flag.DisallowLayout);
        // Set the orientation.
        _this._orientation = options.orientation || 'vertical';
        _this.dataset['orientation'] = _this._orientation;
        // Parse the rest of the options.
        if (options.maximum !== undefined) {
            _this._maximum = Math.max(0, options.maximum);
        }
        if (options.page !== undefined) {
            _this._page = Math.max(0, options.page);
        }
        if (options.value !== undefined) {
            _this._value = Math.max(0, Math.min(options.value, _this._maximum));
        }
        return _this;
    }
    Object.defineProperty(ScrollBar.prototype, "thumbMoved", {
        /**
         * A signal emitted when the user moves the scroll thumb.
         *
         * #### Notes
         * The payload is the current value of the scroll bar.
         */
        get: function () {
            return this._thumbMoved;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "stepRequested", {
        /**
         * A signal emitted when the user clicks a step button.
         *
         * #### Notes
         * The payload is whether a decrease or increase is requested.
         */
        get: function () {
            return this._stepRequested;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "pageRequested", {
        /**
         * A signal emitted when the user clicks the scroll track.
         *
         * #### Notes
         * The payload is whether a decrease or increase is requested.
         */
        get: function () {
            return this._pageRequested;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "orientation", {
        /**
         * Get the orientation of the scroll bar.
         */
        get: function () {
            return this._orientation;
        },
        /**
         * Set the orientation of the scroll bar.
         */
        set: function (value) {
            // Do nothing if the orientation does not change.
            if (this._orientation === value) {
                return;
            }
            // Release the mouse before making changes.
            this._releaseMouse();
            // Update the internal orientation.
            this._orientation = value;
            this.dataset['orientation'] = value;
            // Schedule an update the scroll bar.
            this.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "value", {
        /**
         * Get the current value of the scroll bar.
         */
        get: function () {
            return this._value;
        },
        /**
         * Set the current value of the scroll bar.
         *
         * #### Notes
         * The value will be clamped to the range `[0, maximum]`.
         */
        set: function (value) {
            // Clamp the value to the allowable range.
            value = Math.max(0, Math.min(value, this._maximum));
            // Do nothing if the value does not change.
            if (this._value === value) {
                return;
            }
            // Update the internal value.
            this._value = value;
            // Schedule an update the scroll bar.
            this.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "page", {
        /**
         * Get the page size of the scroll bar.
         *
         * #### Notes
         * The page size is the amount of visible content in the scrolled
         * region, expressed in data units. It determines the size of the
         * scroll bar thumb.
         */
        get: function () {
            return this._page;
        },
        /**
         * Set the page size of the scroll bar.
         *
         * #### Notes
         * The page size will be clamped to the range `[0, Infinity]`.
         */
        set: function (value) {
            // Clamp the page size to the allowable range.
            value = Math.max(0, value);
            // Do nothing if the value does not change.
            if (this._page === value) {
                return;
            }
            // Update the internal page size.
            this._page = value;
            // Schedule an update the scroll bar.
            this.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "maximum", {
        /**
         * Get the maximum value of the scroll bar.
         */
        get: function () {
            return this._maximum;
        },
        /**
         * Set the maximum value of the scroll bar.
         *
         * #### Notes
         * The max size will be clamped to the range `[0, Infinity]`.
         */
        set: function (value) {
            // Clamp the value to the allowable range.
            value = Math.max(0, value);
            // Do nothing if the value does not change.
            if (this._maximum === value) {
                return;
            }
            // Update the internal values.
            this._maximum = value;
            // Clamp the current value to the new range.
            this._value = Math.min(this._value, value);
            // Schedule an update the scroll bar.
            this.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "decrementNode", {
        /**
         * The scroll bar decrement button node.
         *
         * #### Notes
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-ScrollBar-button')[0];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "incrementNode", {
        /**
         * The scroll bar increment button node.
         *
         * #### Notes
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-ScrollBar-button')[1];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "trackNode", {
        /**
         * The scroll bar track node.
         *
         * #### Notes
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-ScrollBar-track')[0];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ScrollBar.prototype, "thumbNode", {
        /**
         * The scroll bar thumb node.
         *
         * #### Notes
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-ScrollBar-thumb')[0];
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Handle the DOM events for the scroll bar.
     *
     * @param event - The DOM event sent to the scroll bar.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the scroll bar's DOM node.
     *
     * This should not be called directly by user code.
     */
    ScrollBar.prototype.handleEvent = function (event) {
        switch (event.type) {
            case 'mousedown':
                this._evtMouseDown(event);
                break;
            case 'mousemove':
                this._evtMouseMove(event);
                break;
            case 'mouseup':
                this._evtMouseUp(event);
                break;
            case 'keydown':
                this._evtKeyDown(event);
                break;
            case 'contextmenu':
                event.preventDefault();
                event.stopPropagation();
                break;
        }
    };
    /**
     * A method invoked on a 'before-attach' message.
     */
    ScrollBar.prototype.onBeforeAttach = function (msg) {
        this.node.addEventListener('mousedown', this);
        this.update();
    };
    /**
     * A method invoked on an 'after-detach' message.
     */
    ScrollBar.prototype.onAfterDetach = function (msg) {
        this.node.removeEventListener('mousedown', this);
        this._releaseMouse();
    };
    /**
     * A method invoked on an 'update-request' message.
     */
    ScrollBar.prototype.onUpdateRequest = function (msg) {
        // Convert the value and page into percentages.
        var value = this._value * 100 / this._maximum;
        var page = this._page * 100 / (this._page + this._maximum);
        // Clamp the value and page to the relevant range.
        value = Math.max(0, Math.min(value, 100));
        page = Math.max(0, Math.min(page, 100));
        // Fetch the thumb style.
        var thumbStyle = this.thumbNode.style;
        // Update the thumb style for the current orientation.
        if (this._orientation === 'horizontal') {
            thumbStyle.top = '';
            thumbStyle.height = '';
            thumbStyle.left = value + "%";
            thumbStyle.width = page + "%";
            thumbStyle.transform = "translate(" + -value + "%, 0%)";
        }
        else {
            thumbStyle.left = '';
            thumbStyle.width = '';
            thumbStyle.top = value + "%";
            thumbStyle.height = page + "%";
            thumbStyle.transform = "translate(0%, " + -value + "%)";
        }
    };
    /**
     * Handle the `'keydown'` event for the scroll bar.
     */
    ScrollBar.prototype._evtKeyDown = function (event) {
        // Stop all input events during drag.
        event.preventDefault();
        event.stopPropagation();
        // Ignore anything except the `Escape` key.
        if (event.keyCode !== 27) {
            return;
        }
        // Fetch the previous scroll value.
        var value = this._pressData ? this._pressData.value : -1;
        // Release the mouse.
        this._releaseMouse();
        // Restore the old scroll value if possible.
        if (value !== -1) {
            this._moveThumb(value);
        }
    };
    /**
     * Handle the `'mousedown'` event for the scroll bar.
     */
    ScrollBar.prototype._evtMouseDown = function (event) {
        // Do nothing if it's not a left mouse press.
        if (event.button !== 0) {
            return;
        }
        // Do nothing if the mouse is already captured.
        if (this._pressData) {
            return;
        }
        // Find the pressed scroll bar part.
        var part = Private.findPart(this, event.target);
        // Do nothing if the part is not of interest.
        if (!part) {
            return;
        }
        // Stop the event propagation.
        event.preventDefault();
        event.stopPropagation();
        // Override the mouse cursor.
        var override = dragdrop_1.Drag.overrideCursor('default');
        // Set up the press data.
        this._pressData = {
            part: part, override: override,
            delta: -1, value: -1,
            mouseX: event.clientX,
            mouseY: event.clientY
        };
        // Add the extra event listeners.
        document.addEventListener('mousemove', this, true);
        document.addEventListener('mouseup', this, true);
        document.addEventListener('keydown', this, true);
        document.addEventListener('contextmenu', this, true);
        // Handle a thumb press.
        if (part === 'thumb') {
            // Fetch the thumb node.
            var thumbNode = this.thumbNode;
            // Fetch the client rect for the thumb.
            var thumbRect = thumbNode.getBoundingClientRect();
            // Update the press data delta for the current orientation.
            if (this._orientation === 'horizontal') {
                this._pressData.delta = event.clientX - thumbRect.left;
            }
            else {
                this._pressData.delta = event.clientY - thumbRect.top;
            }
            // Add the active class to the thumb node.
            thumbNode.classList.add('p-mod-active');
            // Store the current value in the press data.
            this._pressData.value = this._value;
            // Finished.
            return;
        }
        // Handle a track press.
        if (part === 'track') {
            // Fetch the client rect for the thumb.
            var thumbRect = this.thumbNode.getBoundingClientRect();
            // Determine the direction for the page request.
            var dir = void 0;
            if (this._orientation === 'horizontal') {
                dir = event.clientX < thumbRect.left ? 'decrement' : 'increment';
            }
            else {
                dir = event.clientY < thumbRect.top ? 'decrement' : 'increment';
            }
            // Start the repeat timer.
            this._repeatTimer = setTimeout(this._onRepeat, 350);
            // Emit the page requested signal.
            this._pageRequested.emit(dir);
            // Finished.
            return;
        }
        // Handle a decrement button press.
        if (part === 'decrement') {
            // Add the active class to the decrement node.
            this.decrementNode.classList.add('p-mod-active');
            // Start the repeat timer.
            this._repeatTimer = setTimeout(this._onRepeat, 350);
            // Emit the step requested signal.
            this._stepRequested.emit('decrement');
            // Finished.
            return;
        }
        // Handle an increment button press.
        if (part === 'increment') {
            // Add the active class to the increment node.
            this.incrementNode.classList.add('p-mod-active');
            // Start the repeat timer.
            this._repeatTimer = setTimeout(this._onRepeat, 350);
            // Emit the step requested signal.
            this._stepRequested.emit('increment');
            // Finished.
            return;
        }
    };
    /**
     * Handle the `'mousemove'` event for the scroll bar.
     */
    ScrollBar.prototype._evtMouseMove = function (event) {
        // Do nothing if no drag is in progress.
        if (!this._pressData) {
            return;
        }
        // Stop the event propagation.
        event.preventDefault();
        event.stopPropagation();
        // Update the mouse position.
        this._pressData.mouseX = event.clientX;
        this._pressData.mouseY = event.clientY;
        // Bail if the thumb is not being dragged.
        if (this._pressData.part !== 'thumb') {
            return;
        }
        // Get the client rect for the thumb and track.
        var thumbRect = this.thumbNode.getBoundingClientRect();
        var trackRect = this.trackNode.getBoundingClientRect();
        // Fetch the scroll geometry based on the orientation.
        var trackPos;
        var trackSpan;
        if (this._orientation === 'horizontal') {
            trackPos = event.clientX - trackRect.left - this._pressData.delta;
            trackSpan = trackRect.width - thumbRect.width;
        }
        else {
            trackPos = event.clientY - trackRect.top - this._pressData.delta;
            trackSpan = trackRect.height - thumbRect.height;
        }
        // Compute the desired value from the scroll geometry.
        var value = trackSpan === 0 ? 0 : trackPos * this._maximum / trackSpan;
        // Move the thumb to the computed value.
        this._moveThumb(value);
    };
    /**
     * Handle the `'mouseup'` event for the scroll bar.
     */
    ScrollBar.prototype._evtMouseUp = function (event) {
        // Do nothing if it's not a left mouse release.
        if (event.button !== 0) {
            return;
        }
        // Stop the event propagation.
        event.preventDefault();
        event.stopPropagation();
        // Release the mouse.
        this._releaseMouse();
    };
    /**
     * Release the mouse and restore the node states.
     */
    ScrollBar.prototype._releaseMouse = function () {
        // Bail if there is no press data.
        if (!this._pressData) {
            return;
        }
        // Clear the repeat timer.
        clearTimeout(this._repeatTimer);
        this._repeatTimer = -1;
        // Clear the press data.
        this._pressData.override.dispose();
        this._pressData = null;
        // Remove the extra event listeners.
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('mouseup', this, true);
        document.removeEventListener('keydown', this, true);
        document.removeEventListener('contextmenu', this, true);
        // Remove the active classes from the nodes.
        this.thumbNode.classList.remove('p-mod-active');
        this.decrementNode.classList.remove('p-mod-active');
        this.incrementNode.classList.remove('p-mod-active');
    };
    /**
     * Move the thumb to the specified position.
     */
    ScrollBar.prototype._moveThumb = function (value) {
        // Clamp the value to the allowed range.
        value = Math.max(0, Math.min(value, this._maximum));
        // Bail if the value does not change.
        if (this._value === value) {
            return;
        }
        // Update the internal value.
        this._value = value;
        // Schedule an update of the scroll bar.
        this.update();
        // Emit the thumb moved signal.
        this._thumbMoved.emit(value);
    };
    return ScrollBar;
}(widget_1.Widget));
exports.ScrollBar = ScrollBar;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create the DOM node for a scroll bar.
     */
    function createNode() {
        var node = document.createElement('div');
        var decrement = document.createElement('div');
        var increment = document.createElement('div');
        var track = document.createElement('div');
        var thumb = document.createElement('div');
        decrement.className = 'p-ScrollBar-button';
        increment.className = 'p-ScrollBar-button';
        decrement.dataset['action'] = 'decrement';
        increment.dataset['action'] = 'increment';
        track.className = 'p-ScrollBar-track';
        thumb.className = 'p-ScrollBar-thumb';
        track.appendChild(thumb);
        node.appendChild(decrement);
        node.appendChild(track);
        node.appendChild(increment);
        return node;
    }
    Private.createNode = createNode;
    /**
     * Find the scroll bar part which contains the given target.
     */
    function findPart(scrollBar, target) {
        // Test the thumb.
        if (scrollBar.thumbNode.contains(target)) {
            return 'thumb';
        }
        // Test the track.
        if (scrollBar.trackNode.contains(target)) {
            return 'track';
        }
        // Test the decrement button.
        if (scrollBar.decrementNode.contains(target)) {
            return 'decrement';
        }
        // Test the increment button.
        if (scrollBar.incrementNode.contains(target)) {
            return 'increment';
        }
        // Indicate no match.
        return null;
    }
    Private.findPart = findPart;
})(Private || (Private = {}));
