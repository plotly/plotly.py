"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var algorithm_1 = require("@phosphor/algorithm");
var signaling_1 = require("@phosphor/signaling");
/**
 * A class which tracks focus among a set of widgets.
 *
 * This class is useful when code needs to keep track of the most
 * recently focused widget(s) among a set of related widgets.
 */
var FocusTracker = (function () {
    /**
     * Construct a new focus tracker.
     */
    function FocusTracker() {
        this._counter = 0;
        this._widgets = [];
        this._activeWidget = null;
        this._currentWidget = null;
        this._numbers = new Map();
        this._nodes = new Map();
        this._activeChanged = new signaling_1.Signal(this);
        this._currentChanged = new signaling_1.Signal(this);
    }
    /**
     * Dispose of the resources held by the tracker.
     */
    FocusTracker.prototype.dispose = function () {
        var _this = this;
        // Do nothing if the tracker is already disposed.
        if (this._counter < 0) {
            return;
        }
        // Mark the tracker as disposed.
        this._counter = -1;
        // Clear the connections for the tracker.
        signaling_1.Signal.clearData(this);
        // Remove all event listeners.
        algorithm_1.each(this._widgets, function (w) {
            w.node.removeEventListener('focus', _this, true);
            w.node.removeEventListener('blur', _this, true);
        });
        // Clear the internal data structures.
        this._activeWidget = null;
        this._currentWidget = null;
        this._nodes.clear();
        this._numbers.clear();
        this._widgets.length = 0;
    };
    Object.defineProperty(FocusTracker.prototype, "currentChanged", {
        /**
         * A signal emitted when the current widget has changed.
         */
        get: function () {
            return this._currentChanged;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FocusTracker.prototype, "activeChanged", {
        /**
         * A signal emitted when the active widget has changed.
         */
        get: function () {
            return this._activeChanged;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FocusTracker.prototype, "isDisposed", {
        /**
         * A flag indicating whether the tracker is disposed.
         */
        get: function () {
            return this._counter < 0;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FocusTracker.prototype, "currentWidget", {
        /**
         * The current widget in the tracker.
         *
         * #### Notes
         * The current widget is the widget among the tracked widgets which
         * has the *descendant node* which has most recently been focused.
         *
         * The current widget will not be updated if the node loses focus. It
         * will only be updated when a different tracked widget gains focus.
         *
         * If the current widget is removed from the tracker, the previous
         * current widget will be restored.
         *
         * This behavior is intended to follow a user's conceptual model of
         * a semantically "current" widget, where the "last thing of type X"
         * to be interacted with is the "current instance of X", regardless
         * of whether that instance still has focus.
         */
        get: function () {
            return this._currentWidget;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FocusTracker.prototype, "activeWidget", {
        /**
         * The active widget in the tracker.
         *
         * #### Notes
         * The active widget is the widget among the tracked widgets which
         * has the *descendant node* which is currently focused.
         */
        get: function () {
            return this._activeWidget;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FocusTracker.prototype, "widgets", {
        /**
         * A read only array of the widgets being tracked.
         */
        get: function () {
            return this._widgets;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Get the focus number for a particular widget in the tracker.
     *
     * @param widget - The widget of interest.
     *
     * @returns The focus number for the given widget, or `-1` if the
     *   widget has not had focus since being added to the tracker, or
     *   is not contained by the tracker.
     *
     * #### Notes
     * The focus number indicates the relative order in which the widgets
     * have gained focus. A widget with a larger number has gained focus
     * more recently than a widget with a smaller number.
     *
     * The `currentWidget` will always have the largest focus number.
     *
     * All widgets start with a focus number of `-1`, which indicates that
     * the widget has not been focused since being added to the tracker.
     */
    FocusTracker.prototype.focusNumber = function (widget) {
        var n = this._numbers.get(widget);
        return n === undefined ? -1 : n;
    };
    /**
     * Test whether the focus tracker contains a given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns `true` if the widget is tracked, `false` otherwise.
     */
    FocusTracker.prototype.has = function (widget) {
        return this._numbers.has(widget);
    };
    /**
     * Add a widget to the focus tracker.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * A widget will be automatically removed from the tracker if it
     * is disposed after being added.
     *
     * If the widget is already tracked, this is a no-op.
     */
    FocusTracker.prototype.add = function (widget) {
        // Do nothing if the widget is already tracked.
        if (this._numbers.has(widget)) {
            return;
        }
        // Test whether the widget has focus.
        var focused = widget.node.contains(document.activeElement);
        // Set up the initial focus number.
        var n = focused ? this._counter++ : -1;
        // Add the widget to the internal data structures.
        this._widgets.push(widget);
        this._numbers.set(widget, n);
        this._nodes.set(widget.node, widget);
        // Set up the event listeners. The capturing phase must be used
        // since the 'focus' and 'blur' events don't bubble and Firefox
        // doesn't support the 'focusin' or 'focusout' events.
        widget.node.addEventListener('focus', this, true);
        widget.node.addEventListener('blur', this, true);
        // Connect the disposed signal handler.
        widget.disposed.connect(this._onWidgetDisposed, this);
        // Set the current and active widgets if needed.
        if (focused) {
            this._setWidgets(widget, widget);
        }
    };
    /**
     * Remove a widget from the focus tracker.
     *
     * #### Notes
     * If the widget is the `currentWidget`, the previous current widget
     * will become the new `currentWidget`.
     *
     * A widget will be automatically removed from the tracker if it
     * is disposed after being added.
     *
     * If the widget is not tracked, this is a no-op.
     */
    FocusTracker.prototype.remove = function (widget) {
        var _this = this;
        // Bail early if the widget is not tracked.
        if (!this._numbers.has(widget)) {
            return;
        }
        // Disconnect the disposed signal handler.
        widget.disposed.disconnect(this._onWidgetDisposed, this);
        // Remove the event listeners.
        widget.node.removeEventListener('focus', this, true);
        widget.node.removeEventListener('blur', this, true);
        // Remove the widget from the internal data structures.
        algorithm_1.ArrayExt.removeFirstOf(this._widgets, widget);
        this._nodes.delete(widget.node);
        this._numbers.delete(widget);
        // Bail early if the widget is not the current widget.
        if (this._currentWidget !== widget) {
            return;
        }
        // Filter the widgets for those which have had focus.
        var valid = algorithm_1.filter(this._widgets, function (w) { return _this._numbers.get(w) !== -1; });
        // Get the valid widget with the max focus number.
        var previous = algorithm_1.max(valid, function (first, second) {
            var a = _this._numbers.get(first);
            var b = _this._numbers.get(second);
            return a - b;
        }) || null;
        // Set the current and active widgets.
        this._setWidgets(previous, null);
    };
    /**
     * Handle the DOM events for the focus tracker.
     *
     * @param event - The DOM event sent to the panel.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the tracked nodes. It should
     * not be called directly by user code.
     */
    FocusTracker.prototype.handleEvent = function (event) {
        switch (event.type) {
            case 'focus':
                this._evtFocus(event);
                break;
            case 'blur':
                this._evtBlur(event);
                break;
        }
    };
    /**
     * Set the current and active widgets for the tracker.
     */
    FocusTracker.prototype._setWidgets = function (current, active) {
        // Swap the current widget.
        var oldCurrent = this._currentWidget;
        this._currentWidget = current;
        // Swap the active widget.
        var oldActive = this._activeWidget;
        this._activeWidget = active;
        // Emit the `currentChanged` signal if needed.
        if (oldCurrent !== current) {
            this._currentChanged.emit({ oldValue: oldCurrent, newValue: current });
        }
        // Emit the `activeChanged` signal if needed.
        if (oldActive !== active) {
            this._activeChanged.emit({ oldValue: oldActive, newValue: active });
        }
    };
    /**
     * Handle the `'focus'` event for a tracked widget.
     */
    FocusTracker.prototype._evtFocus = function (event) {
        // Find the widget which gained focus, which is known to exist.
        var widget = this._nodes.get(event.currentTarget);
        // Update the focus number if necessary.
        if (widget !== this._currentWidget) {
            this._numbers.set(widget, this._counter++);
        }
        // Set the current and active widgets.
        this._setWidgets(widget, widget);
    };
    /**
     * Handle the `'blur'` event for a tracked widget.
     */
    FocusTracker.prototype._evtBlur = function (event) {
        // Find the widget which lost focus, which is known to exist.
        var widget = this._nodes.get(event.currentTarget);
        // Get the node which being focused after this blur.
        var focusTarget = event.relatedTarget;
        // If no other node is being focused, clear the active widget.
        if (!focusTarget) {
            this._setWidgets(this._currentWidget, null);
            return;
        }
        // Bail if the focus widget is not changing.
        if (widget.node.contains(focusTarget)) {
            return;
        }
        // If no tracked widget is being focused, clear the active widget.
        if (!algorithm_1.find(this._widgets, function (w) { return w.node.contains(focusTarget); })) {
            this._setWidgets(this._currentWidget, null);
            return;
        }
    };
    /**
     * Handle the `disposed` signal for a tracked widget.
     */
    FocusTracker.prototype._onWidgetDisposed = function (sender) {
        this.remove(sender);
    };
    return FocusTracker;
}());
exports.FocusTracker = FocusTracker;
