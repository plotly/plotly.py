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
var messaging_1 = require("@phosphor/messaging");
var layout_1 = require("./layout");
var widget_1 = require("./widget");
/**
 * A concrete layout implementation suitable for many use cases.
 *
 * #### Notes
 * This class is suitable as a base class for implementing a variety of
 * layouts, but can also be used directly with standard CSS to layout a
 * collection of widgets.
 */
var PanelLayout = (function (_super) {
    __extends(PanelLayout, _super);
    function PanelLayout() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this._widgets = [];
        return _this;
    }
    /**
     * Dispose of the resources held by the layout.
     *
     * #### Notes
     * This will clear and dispose all widgets in the layout.
     *
     * All reimplementations should call the superclass method.
     *
     * This method is called automatically when the parent is disposed.
     */
    PanelLayout.prototype.dispose = function () {
        while (this._widgets.length > 0) {
            this._widgets.pop().dispose();
        }
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(PanelLayout.prototype, "widgets", {
        /**
         * A read-only array of the widgets in the layout.
         */
        get: function () {
            return this._widgets;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Create an iterator over the widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     */
    PanelLayout.prototype.iter = function () {
        return algorithm_1.iter(this._widgets);
    };
    /**
     * Add a widget to the end of the layout.
     *
     * @param widget - The widget to add to the layout.
     *
     * #### Notes
     * If the widget is already contained in the layout, it will be moved.
     */
    PanelLayout.prototype.addWidget = function (widget) {
        this.insertWidget(this._widgets.length, widget);
    };
    /**
     * Insert a widget into the layout at the specified index.
     *
     * @param index - The index at which to insert the widget.
     *
     * @param widget - The widget to insert into the layout.
     *
     * #### Notes
     * The index will be clamped to the bounds of the widgets.
     *
     * If the widget is already added to the layout, it will be moved.
     *
     * #### Undefined Behavior
     * An `index` which is non-integral.
     */
    PanelLayout.prototype.insertWidget = function (index, widget) {
        // Remove the widget from its current parent. This is a no-op
        // if the widget's parent is already the layout parent widget.
        widget.parent = this.parent;
        // Look up the current index of the widget.
        var i = this._widgets.indexOf(widget);
        // Clamp the insert index to the array bounds.
        var j = Math.max(0, Math.min(index, this._widgets.length));
        // If the widget is not in the array, insert it.
        if (i === -1) {
            // Insert the widget into the array.
            algorithm_1.ArrayExt.insert(this._widgets, j, widget);
            // If the layout is parented, attach the widget to the DOM.
            if (this.parent) {
                this.attachWidget(j, widget);
            }
            // There is nothing more to do.
            return;
        }
        // Otherwise, the widget exists in the array and should be moved.
        // Adjust the index if the location is at the end of the array.
        if (j === this._widgets.length) {
            j--;
        }
        // Bail if there is no effective move.
        if (i === j) {
            return;
        }
        // Move the widget to the new location.
        algorithm_1.ArrayExt.move(this._widgets, i, j);
        // If the layout is parented, move the widget in the DOM.
        if (this.parent) {
            this.moveWidget(i, j, widget);
        }
    };
    /**
     * Remove a widget from the layout.
     *
     * @param widget - The widget to remove from the layout.
     *
     * #### Notes
     * A widget is automatically removed from the layout when its `parent`
     * is set to `null`. This method should only be invoked directly when
     * removing a widget from a layout which has yet to be installed on a
     * parent widget.
     *
     * This method does *not* modify the widget's `parent`.
     */
    PanelLayout.prototype.removeWidget = function (widget) {
        this.removeWidgetAt(this._widgets.indexOf(widget));
    };
    /**
     * Remove the widget at a given index from the layout.
     *
     * @param index - The index of the widget to remove.
     *
     * #### Notes
     * A widget is automatically removed from the layout when its `parent`
     * is set to `null`. This method should only be invoked directly when
     * removing a widget from a layout which has yet to be installed on a
     * parent widget.
     *
     * This method does *not* modify the widget's `parent`.
     *
     * #### Undefined Behavior
     * An `index` which is non-integral.
     */
    PanelLayout.prototype.removeWidgetAt = function (index) {
        // Remove the widget from the array.
        var widget = algorithm_1.ArrayExt.removeAt(this._widgets, index);
        // If the layout is parented, detach the widget from the DOM.
        if (widget && this.parent) {
            this.detachWidget(index, widget);
        }
    };
    /**
     * Perform layout initialization which requires the parent widget.
     */
    PanelLayout.prototype.init = function () {
        var _this = this;
        _super.prototype.init.call(this);
        algorithm_1.each(this, function (widget, index) {
            _this.attachWidget(index, widget);
        });
    };
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param index - The current index of the widget in the layout.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This method is called automatically by the panel layout at the
     * appropriate time. It should not be called directly by user code.
     *
     * The default implementation adds the widgets's node to the parent's
     * node at the proper location, and sends the appropriate attach
     * messages to the widget if the parent is attached to the DOM.
     *
     * Subclasses may reimplement this method to control how the widget's
     * node is added to the parent's node.
     */
    PanelLayout.prototype.attachWidget = function (index, widget) {
        // Look up the next sibling reference node.
        var ref = this.parent.node.children[index];
        // Send a `'before-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeAttach);
        }
        // Insert the widget's node before the sibling.
        this.parent.node.insertBefore(widget.node, ref);
        // Send an `'after-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterAttach);
        }
    };
    /**
     * Move a widget in the parent's DOM node.
     *
     * @param fromIndex - The previous index of the widget in the layout.
     *
     * @param toIndex - The current index of the widget in the layout.
     *
     * @param widget - The widget to move in the parent.
     *
     * #### Notes
     * This method is called automatically by the panel layout at the
     * appropriate time. It should not be called directly by user code.
     *
     * The default implementation moves the widget's node to the proper
     * location in the parent's node and sends the appropriate attach and
     * detach messages to the widget if the parent is attached to the DOM.
     *
     * Subclasses may reimplement this method to control how the widget's
     * node is moved in the parent's node.
     */
    PanelLayout.prototype.moveWidget = function (fromIndex, toIndex, widget) {
        // Send a `'before-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeDetach);
        }
        // Remove the widget's node from the parent.
        this.parent.node.removeChild(widget.node);
        // Send an `'after-detach'` and  message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterDetach);
        }
        // Look up the next sibling reference node.
        var ref = this.parent.node.children[toIndex];
        // Send a `'before-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeAttach);
        }
        // Insert the widget's node before the sibling.
        this.parent.node.insertBefore(widget.node, ref);
        // Send an `'after-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterAttach);
        }
    };
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param index - The previous index of the widget in the layout.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This method is called automatically by the panel layout at the
     * appropriate time. It should not be called directly by user code.
     *
     * The default implementation removes the widget's node from the
     * parent's node, and sends the appropriate detach messages to the
     * widget if the parent is attached to the DOM.
     *
     * Subclasses may reimplement this method to control how the widget's
     * node is removed from the parent's node.
     */
    PanelLayout.prototype.detachWidget = function (index, widget) {
        // Send a `'before-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeDetach);
        }
        // Remove the widget's node from the parent.
        this.parent.node.removeChild(widget.node);
        // Send an `'after-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterDetach);
        }
    };
    return PanelLayout;
}(layout_1.Layout));
exports.PanelLayout = PanelLayout;
