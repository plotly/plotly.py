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
var domutils_1 = require("@phosphor/domutils");
var messaging_1 = require("@phosphor/messaging");
var layout_1 = require("./layout");
var panellayout_1 = require("./panellayout");
var widget_1 = require("./widget");
/**
 * A layout where visible widgets are stacked atop one another.
 *
 * #### Notes
 * The Z-order of the visible widgets follows their layout order.
 */
var StackedLayout = (function (_super) {
    __extends(StackedLayout, _super);
    function StackedLayout() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this._dirty = false;
        _this._items = [];
        _this._box = null;
        return _this;
    }
    /**
     * Dispose of the resources held by the layout.
     */
    StackedLayout.prototype.dispose = function () {
        // Dispose of the layout items.
        algorithm_1.each(this._items, function (item) { item.dispose(); });
        // Clear the layout state.
        this._box = null;
        this._items.length = 0;
        // Dispose of the rest of the layout.
        _super.prototype.dispose.call(this);
    };
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param index - The current index of the widget in the layout.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    StackedLayout.prototype.attachWidget = function (index, widget) {
        // Create and add a new layout item for the widget.
        algorithm_1.ArrayExt.insert(this._items, index, new layout_1.LayoutItem(widget));
        // Send a `'before-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeAttach);
        }
        // Add the widget's node to the parent.
        this.parent.node.appendChild(widget.node);
        // Send an `'after-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterAttach);
        }
        // Post a fit request for the parent widget.
        this.parent.fit();
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
     * This is a reimplementation of the superclass method.
     */
    StackedLayout.prototype.moveWidget = function (fromIndex, toIndex, widget) {
        // Move the layout item for the widget.
        algorithm_1.ArrayExt.move(this._items, fromIndex, toIndex);
        // Post an update request for the parent widget.
        this.parent.update();
    };
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param index - The previous index of the widget in the layout.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    StackedLayout.prototype.detachWidget = function (index, widget) {
        // Remove the layout item for the widget.
        var item = algorithm_1.ArrayExt.removeAt(this._items, index);
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
        // Reset the z-index for the widget.
        item.widget.node.style.zIndex = '';
        // Dispose of the layout item.
        item.dispose();
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'before-show'` message.
     */
    StackedLayout.prototype.onBeforeShow = function (msg) {
        _super.prototype.onBeforeShow.call(this, msg);
        this.parent.update();
    };
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    StackedLayout.prototype.onBeforeAttach = function (msg) {
        _super.prototype.onBeforeAttach.call(this, msg);
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-shown'` message.
     */
    StackedLayout.prototype.onChildShown = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-hidden'` message.
     */
    StackedLayout.prototype.onChildHidden = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'resize'` message.
     */
    StackedLayout.prototype.onResize = function (msg) {
        if (this.parent.isVisible) {
            this._update(msg.width, msg.height);
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    StackedLayout.prototype.onUpdateRequest = function (msg) {
        if (this.parent.isVisible) {
            this._update(-1, -1);
        }
    };
    /**
     * A message handler invoked on a `'fit-request'` message.
     */
    StackedLayout.prototype.onFitRequest = function (msg) {
        if (this.parent.isAttached) {
            this._fit();
        }
    };
    /**
     * Fit the layout to the total size required by the widgets.
     */
    StackedLayout.prototype._fit = function () {
        // Set up the computed minimum size.
        var minW = 0;
        var minH = 0;
        // Update the computed minimum size.
        for (var i = 0, n = this._items.length; i < n; ++i) {
            // Fetch the item.
            var item = this._items[i];
            // Ignore hidden items.
            if (item.isHidden) {
                continue;
            }
            // Update the size limits for the item.
            item.fit();
            // Update the computed minimum size.
            minW = Math.max(minW, item.minWidth);
            minH = Math.max(minH, item.minHeight);
        }
        // Update the box sizing and add it to the computed min size.
        var box = this._box = domutils_1.ElementExt.boxSizing(this.parent.node);
        minW += box.horizontalSum;
        minH += box.verticalSum;
        // Update the parent's min size constraints.
        var style = this.parent.node.style;
        style.minWidth = minW + "px";
        style.minHeight = minH + "px";
        // Set the dirty flag to ensure only a single update occurs.
        this._dirty = true;
        // Notify the ancestor that it should fit immediately. This may
        // cause a resize of the parent, fulfilling the required update.
        if (this.parent.parent) {
            messaging_1.MessageLoop.sendMessage(this.parent.parent, widget_1.Widget.Msg.FitRequest);
        }
        // If the dirty flag is still set, the parent was not resized.
        // Trigger the required update on the parent widget immediately.
        if (this._dirty) {
            messaging_1.MessageLoop.sendMessage(this.parent, widget_1.Widget.Msg.UpdateRequest);
        }
    };
    /**
     * Update the layout position and size of the widgets.
     *
     * The parent offset dimensions should be `-1` if unknown.
     */
    StackedLayout.prototype._update = function (offsetWidth, offsetHeight) {
        // Clear the dirty flag to indicate the update occurred.
        this._dirty = false;
        // Compute the visible item count.
        var nVisible = 0;
        for (var i = 0, n = this._items.length; i < n; ++i) {
            nVisible += +!this._items[i].isHidden;
        }
        // Bail early if there are no visible items to layout.
        if (nVisible === 0) {
            return;
        }
        // Measure the parent if the offset dimensions are unknown.
        if (offsetWidth < 0) {
            offsetWidth = this.parent.node.offsetWidth;
        }
        if (offsetHeight < 0) {
            offsetHeight = this.parent.node.offsetHeight;
        }
        // Ensure the parent box sizing data is computed.
        if (!this._box) {
            this._box = domutils_1.ElementExt.boxSizing(this.parent.node);
        }
        // Compute the actual layout bounds adjusted for border and padding.
        var top = this._box.paddingTop;
        var left = this._box.paddingLeft;
        var width = offsetWidth - this._box.horizontalSum;
        var height = offsetHeight - this._box.verticalSum;
        // Update the widget stacking order and layout geometry.
        for (var i = 0, n = this._items.length; i < n; ++i) {
            // Fetch the item.
            var item = this._items[i];
            // Ignore hidden items.
            if (item.isHidden) {
                continue;
            }
            // Set the z-index for the widget.
            item.widget.node.style.zIndex = "" + i;
            // Update the item geometry.
            item.update(left, top, width, height);
        }
    };
    return StackedLayout;
}(panellayout_1.PanelLayout));
exports.StackedLayout = StackedLayout;
