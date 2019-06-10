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
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var algorithm_1 = require("@phosphor/algorithm");
var dragdrop_1 = require("@phosphor/dragdrop");
var panel_1 = require("./panel");
var splitlayout_1 = require("./splitlayout");
/**
 * A panel which arranges its widgets into resizable sections.
 *
 * #### Notes
 * This class provides a convenience wrapper around a [[SplitLayout]].
 */
var SplitPanel = (function (_super) {
    __extends(SplitPanel, _super);
    /**
     * Construct a new split panel.
     *
     * @param options - The options for initializing the split panel.
     */
    function SplitPanel(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, { layout: Private.createLayout(options) }) || this;
        _this._pressData = null;
        _this.addClass('p-SplitPanel');
        return _this;
    }
    /**
     * Dispose of the resources held by the panel.
     */
    SplitPanel.prototype.dispose = function () {
        this._releaseMouse();
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(SplitPanel.prototype, "orientation", {
        /**
         * Get the layout orientation for the split panel.
         */
        get: function () {
            return this.layout.orientation;
        },
        /**
         * Set the layout orientation for the split panel.
         */
        set: function (value) {
            this.layout.orientation = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitPanel.prototype, "alignment", {
        /**
         * Get the content alignment for the split panel.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand to fill the
         * entire split panel.
         */
        get: function () {
            return this.layout.alignment;
        },
        /**
         * Set the content alignment for the split panel.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand to fill the
         * entire split panel.
         */
        set: function (value) {
            this.layout.alignment = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitPanel.prototype, "spacing", {
        /**
         * Get the inter-element spacing for the split panel.
         */
        get: function () {
            return this.layout.spacing;
        },
        /**
         * Set the inter-element spacing for the split panel.
         */
        set: function (value) {
            this.layout.spacing = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitPanel.prototype, "renderer", {
        /**
         * The renderer used by the split panel.
         */
        get: function () {
            return this.layout.renderer;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitPanel.prototype, "handles", {
        /**
         * A read-only array of the split handles in the panel.
         */
        get: function () {
            return this.layout.handles;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Get the relative sizes of the widgets in the panel.
     *
     * @returns A new array of the relative sizes of the widgets.
     *
     * #### Notes
     * The returned sizes reflect the sizes of the widgets normalized
     * relative to their siblings.
     *
     * This method **does not** measure the DOM nodes.
     */
    SplitPanel.prototype.relativeSizes = function () {
        return this.layout.relativeSizes();
    };
    /**
     * Set the relative sizes for the widgets in the panel.
     *
     * @param sizes - The relative sizes for the widgets in the panel.
     *
     * #### Notes
     * Extra values are ignored, too few will yield an undefined layout.
     *
     * The actual geometry of the DOM nodes is updated asynchronously.
     */
    SplitPanel.prototype.setRelativeSizes = function (sizes) {
        this.layout.setRelativeSizes(sizes);
    };
    /**
     * Handle the DOM events for the split panel.
     *
     * @param event - The DOM event sent to the panel.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the panel's DOM node. It should
     * not be called directly by user code.
     */
    SplitPanel.prototype.handleEvent = function (event) {
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
     * A message handler invoked on a `'before-attach'` message.
     */
    SplitPanel.prototype.onBeforeAttach = function (msg) {
        this.node.addEventListener('mousedown', this);
    };
    /**
     * A message handler invoked on an `'after-detach'` message.
     */
    SplitPanel.prototype.onAfterDetach = function (msg) {
        this.node.removeEventListener('mousedown', this);
        this._releaseMouse();
    };
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    SplitPanel.prototype.onChildAdded = function (msg) {
        msg.child.addClass('p-SplitPanel-child');
        this._releaseMouse();
    };
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    SplitPanel.prototype.onChildRemoved = function (msg) {
        msg.child.removeClass('p-SplitPanel-child');
        this._releaseMouse();
    };
    /**
     * Handle the `'keydown'` event for the split panel.
     */
    SplitPanel.prototype._evtKeyDown = function (event) {
        // Stop input events during drag.
        event.preventDefault();
        event.stopPropagation();
        // Release the mouse if `Escape` is pressed.
        if (event.keyCode === 27) {
            this._releaseMouse();
        }
    };
    /**
     * Handle the `'mousedown'` event for the split panel.
     */
    SplitPanel.prototype._evtMouseDown = function (event) {
        // Do nothing if the left mouse button is not pressed.
        if (event.button !== 0) {
            return;
        }
        // Find the handle which contains the mouse target, if any.
        var layout = this.layout;
        var index = algorithm_1.ArrayExt.findFirstIndex(layout.handles, function (handle) {
            return handle.contains(event.target);
        });
        // Bail early if the mouse press was not on a handle.
        if (index === -1) {
            return;
        }
        // Stop the event when a split handle is pressed.
        event.preventDefault();
        event.stopPropagation();
        // Add the extra document listeners.
        document.addEventListener('mouseup', this, true);
        document.addEventListener('mousemove', this, true);
        document.addEventListener('keydown', this, true);
        document.addEventListener('contextmenu', this, true);
        // Compute the offset delta for the handle press.
        var delta;
        var handle = layout.handles[index];
        var rect = handle.getBoundingClientRect();
        if (layout.orientation === 'horizontal') {
            delta = event.clientX - rect.left;
        }
        else {
            delta = event.clientY - rect.top;
        }
        // Override the cursor and store the press data.
        var style = window.getComputedStyle(handle);
        var override = dragdrop_1.Drag.overrideCursor(style.cursor);
        this._pressData = { index: index, delta: delta, override: override };
    };
    /**
     * Handle the `'mousemove'` event for the split panel.
     */
    SplitPanel.prototype._evtMouseMove = function (event) {
        // Stop the event when dragging a split handle.
        event.preventDefault();
        event.stopPropagation();
        // Compute the desired offset position for the handle.
        var pos;
        var layout = this.layout;
        var rect = this.node.getBoundingClientRect();
        if (layout.orientation === 'horizontal') {
            pos = event.clientX - rect.left - this._pressData.delta;
        }
        else {
            pos = event.clientY - rect.top - this._pressData.delta;
        }
        // Move the handle as close to the desired position as possible.
        layout.moveHandle(this._pressData.index, pos);
    };
    /**
     * Handle the `'mouseup'` event for the split panel.
     */
    SplitPanel.prototype._evtMouseUp = function (event) {
        // Do nothing if the left mouse button is not released.
        if (event.button !== 0) {
            return;
        }
        // Stop the event when releasing a handle.
        event.preventDefault();
        event.stopPropagation();
        // Finalize the mouse release.
        this._releaseMouse();
    };
    /**
     * Release the mouse grab for the split panel.
     */
    SplitPanel.prototype._releaseMouse = function () {
        // Bail early if no drag is in progress.
        if (!this._pressData) {
            return;
        }
        // Clear the override cursor.
        this._pressData.override.dispose();
        this._pressData = null;
        // Remove the extra document listeners.
        document.removeEventListener('mouseup', this, true);
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('keydown', this, true);
        document.removeEventListener('contextmenu', this, true);
    };
    return SplitPanel;
}(panel_1.Panel));
exports.SplitPanel = SplitPanel;
/**
 * The namespace for the `SplitPanel` class statics.
 */
(function (SplitPanel) {
    /**
     * The default implementation of `IRenderer`.
     */
    var Renderer = (function () {
        function Renderer() {
        }
        /**
         * Create a new handle for use with a split panel.
         *
         * @returns A new handle element for a split panel.
         */
        Renderer.prototype.createHandle = function () {
            var handle = document.createElement('div');
            handle.className = 'p-SplitPanel-handle';
            return handle;
        };
        return Renderer;
    }());
    SplitPanel.Renderer = Renderer;
    /**
     * The default `Renderer` instance.
     */
    SplitPanel.defaultRenderer = new Renderer();
    /**
     * Get the split panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The split panel stretch factor for the widget.
     */
    function getStretch(widget) {
        return splitlayout_1.SplitLayout.getStretch(widget);
    }
    SplitPanel.getStretch = getStretch;
    /**
     * Set the split panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget, value) {
        splitlayout_1.SplitLayout.setStretch(widget, value);
    }
    SplitPanel.setStretch = setStretch;
})(SplitPanel = exports.SplitPanel || (exports.SplitPanel = {}));
exports.SplitPanel = SplitPanel;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create a split layout for the given panel options.
     */
    function createLayout(options) {
        return options.layout || new splitlayout_1.SplitLayout({
            renderer: options.renderer || SplitPanel.defaultRenderer,
            orientation: options.orientation,
            alignment: options.alignment,
            spacing: options.spacing
        });
    }
    Private.createLayout = createLayout;
})(Private || (Private = {}));
