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
var boxengine_1 = require("./boxengine");
var layout_1 = require("./layout");
var widget_1 = require("./widget");
/**
 * A layout which provides a flexible docking arrangement.
 *
 * #### Notes
 * The consumer of this layout is repsonsible for handling all signals
 * from the generated tab bars and managing the visibility of widgets
 * and tab bars as needed.
 */
var DockLayout = (function (_super) {
    __extends(DockLayout, _super);
    /**
     * Construct a new dock layout.
     *
     * @param options - The options for initializing the layout.
     */
    function DockLayout(options) {
        var _this = _super.call(this) || this;
        _this._spacing = 4;
        _this._dirty = false;
        _this._root = null;
        _this._box = null;
        _this._items = new Map();
        _this.renderer = options.renderer;
        if (options.spacing !== undefined) {
            _this._spacing = Private.clampSpacing(options.spacing);
        }
        return _this;
    }
    /**
     * Dispose of the resources held by the layout.
     *
     * #### Notes
     * This will clear and dispose all widgets in the layout.
     */
    DockLayout.prototype.dispose = function () {
        // Get an iterator over the widgets in the layout.
        var widgets = this.iter();
        // Dispose of the layout items.
        this._items.forEach(function (item) { item.dispose(); });
        // Clear the layout state before disposing the widgets.
        this._box = null;
        this._root = null;
        this._items.clear();
        // Dispose of the widgets contained in the old layout root.
        algorithm_1.each(widgets, function (widget) { widget.dispose(); });
        // Dispose of the base class.
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(DockLayout.prototype, "spacing", {
        /**
         * Get the inter-element spacing for the dock layout.
         */
        get: function () {
            return this._spacing;
        },
        /**
         * Set the inter-element spacing for the dock layout.
         */
        set: function (value) {
            value = Private.clampSpacing(value);
            if (this._spacing === value) {
                return;
            }
            this._spacing = value;
            if (!this.parent) {
                return;
            }
            this.parent.fit();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockLayout.prototype, "isEmpty", {
        /**
         * Whether the dock layout is empty.
         */
        get: function () {
            return this._root === null;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Create an iterator over all widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     *
     * #### Notes
     * This iterator includes the generated tab bars.
     */
    DockLayout.prototype.iter = function () {
        return this._root ? this._root.iterAllWidgets() : algorithm_1.empty();
    };
    /**
     * Create an iterator over the user widgets in the layout.
     *
     * @returns A new iterator over the user widgets in the layout.
     *
     * #### Notes
     * This iterator does not include the generated tab bars.
     */
    DockLayout.prototype.widgets = function () {
        return this._root ? this._root.iterUserWidgets() : algorithm_1.empty();
    };
    /**
     * Create an iterator over the selected widgets in the layout.
     *
     * @returns A new iterator over the selected user widgets.
     *
     * #### Notes
     * This iterator yields the widgets corresponding to the current tab
     * of each tab bar in the layout.
     */
    DockLayout.prototype.selectedWidgets = function () {
        return this._root ? this._root.iterSelectedWidgets() : algorithm_1.empty();
    };
    /**
     * Create an iterator over the tab bars in the layout.
     *
     * @returns A new iterator over the tab bars in the layout.
     *
     * #### Notes
     * This iterator does not include the user widgets.
     */
    DockLayout.prototype.tabBars = function () {
        return this._root ? this._root.iterTabBars() : algorithm_1.empty();
    };
    /**
     * Create an iterator over the handles in the layout.
     *
     * @returns A new iterator over the handles in the layout.
     */
    DockLayout.prototype.handles = function () {
        return this._root ? this._root.iterHandles() : algorithm_1.empty();
    };
    /**
     * Move a handle to the given offset position.
     *
     * @param handle - The handle to move.
     *
     * @param offsetX - The desired offset X position of the handle.
     *
     * @param offsetY - The desired offset Y position of the handle.
     *
     * #### Notes
     * If the given handle is not contained in the layout, this is no-op.
     *
     * The handle will be moved as close as possible to the desired
     * position without violating any of the layout constraints.
     *
     * Only one of the coordinates is used depending on the orientation
     * of the handle. This method accepts both coordinates to make it
     * easy to invoke from a mouse move event without needing to know
     * the handle orientation.
     */
    DockLayout.prototype.moveHandle = function (handle, offsetX, offsetY) {
        // Bail early if there is no root or if the handle is hidden.
        if (!this._root || handle.classList.contains('p-mod-hidden')) {
            return;
        }
        // Lookup the split node for the handle.
        var data = this._root.findSplitNode(handle);
        if (!data) {
            return;
        }
        // Compute the desired delta movement for the handle.
        var delta;
        if (data.node.orientation === 'horizontal') {
            delta = offsetX - handle.offsetLeft;
        }
        else {
            delta = offsetY - handle.offsetTop;
        }
        // Bail if there is no handle movement.
        if (delta === 0) {
            return;
        }
        // Prevent sibling resizing unless needed.
        data.node.holdSizes();
        // Adjust the sizers to reflect the handle movement.
        boxengine_1.BoxEngine.adjust(data.node.sizers, data.index, delta);
        // Update the layout of the widgets.
        if (this.parent) {
            this.parent.update();
        }
    };
    /**
     * Save the current configuration of the dock layout.
     *
     * @returns A new config object for the current layout state.
     *
     * #### Notes
     * The return value can be provided to the `restoreLayout` method
     * in order to restore the layout to its current configuration.
     */
    DockLayout.prototype.saveLayout = function () {
        // Bail early if there is no root.
        if (!this._root) {
            return { main: null };
        }
        // Hold the current sizes in the layout tree.
        this._root.holdAllSizes();
        // Return the layout config.
        return { main: this._root.createConfig() };
    };
    /**
     * Restore the layout to a previously saved configuration.
     *
     * @param config - The layout configuration to restore.
     *
     * #### Notes
     * Widgets which currently belong to the layout but which are not
     * contained in the config will be unparented.
     */
    DockLayout.prototype.restoreLayout = function (config) {
        var _this = this;
        // Create the widget set for validating the config.
        var widgetSet = new Set();
        // Normalize the main area config and collect the widgets.
        var mainConfig;
        if (config.main) {
            mainConfig = Private.normalizeAreaConfig(config.main, widgetSet);
        }
        else {
            mainConfig = null;
        }
        // Create iterators over the old content.
        var oldWidgets = this.widgets();
        var oldTabBars = this.tabBars();
        var oldHandles = this.handles();
        // Clear the root before removing the old content.
        this._root = null;
        // Unparent the old widgets which are not in the new config.
        algorithm_1.each(oldWidgets, function (widget) {
            if (!widgetSet.has(widget)) {
                widget.parent = null;
            }
        });
        // Dispose of the old tab bars.
        algorithm_1.each(oldTabBars, function (tabBar) {
            tabBar.dispose();
        });
        // Remove the old handles.
        algorithm_1.each(oldHandles, function (handle) {
            if (handle.parentNode) {
                handle.parentNode.removeChild(handle);
            }
        });
        // Reparent the new widgets to the current parent.
        widgetSet.forEach(function (widget) {
            widget.parent = _this.parent;
        });
        // Create the root node for the new config.
        if (mainConfig) {
            this._root = Private.realizeAreaConfig(mainConfig, {
                createTabBar: function () { return _this._createTabBar(); },
                createHandle: function () { return _this._createHandle(); }
            });
        }
        else {
            this._root = null;
        }
        // If there is no parent, there is nothing more to do.
        if (!this.parent) {
            return;
        }
        // Attach the new widgets to the parent.
        widgetSet.forEach(function (widget) {
            _this.attachWidget(widget);
        });
        // Post a fit request to the parent.
        this.parent.fit();
    };
    /**
     * Add a widget to the dock layout.
     *
     * @param widget - The widget to add to the dock layout.
     *
     * @param options - The additional options for adding the widget.
     *
     * #### Notes
     * The widget will be moved if it is already contained in the layout.
     *
     * An error will be thrown if the reference widget is invalid.
     */
    DockLayout.prototype.addWidget = function (widget, options) {
        if (options === void 0) { options = {}; }
        // Parse the options.
        var ref = options.ref || null;
        var mode = options.mode || 'tab-after';
        // Find the tab node which holds the reference widget.
        var refNode = null;
        if (this._root && ref) {
            refNode = this._root.findTabNode(ref);
        }
        // Throw an error if the reference widget is invalid.
        if (ref && !refNode) {
            throw new Error('Reference widget is not in the layout.');
        }
        // Reparent the widget to the current layout parent.
        widget.parent = this.parent;
        // Insert the widget according to the insert mode.
        switch (mode) {
            case 'tab-after':
                this._insertTab(widget, ref, refNode, true);
                break;
            case 'tab-before':
                this._insertTab(widget, ref, refNode, false);
                break;
            case 'split-top':
                this._insertSplit(widget, ref, refNode, 'vertical', false);
                break;
            case 'split-left':
                this._insertSplit(widget, ref, refNode, 'horizontal', false);
                break;
            case 'split-right':
                this._insertSplit(widget, ref, refNode, 'horizontal', true);
                break;
            case 'split-bottom':
                this._insertSplit(widget, ref, refNode, 'vertical', true);
                break;
        }
        // Do nothing else if there is no parent widget.
        if (!this.parent) {
            return;
        }
        // Ensure the widget is attached to the parent widget.
        this.attachWidget(widget);
        // Post a fit request for the parent widget.
        this.parent.fit();
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
    DockLayout.prototype.removeWidget = function (widget) {
        // Remove the widget from its current layout location.
        this._removeWidget(widget);
        // Do nothing else if there is no parent widget.
        if (!this.parent) {
            return;
        }
        // Detach the widget from the parent widget.
        this.detachWidget(widget);
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * Find the tab area which contains the given client position.
     *
     * @param clientX - The client X position of interest.
     *
     * @param clientY - The client Y position of interest.
     *
     * @returns The geometry of the tab area at the given position, or
     *   `null` if there is no tab area at the given position.
     */
    DockLayout.prototype.hitTestTabAreas = function (clientX, clientY) {
        // Bail early if hit testing cannot produce valid results.
        if (!this._root || !this.parent || !this.parent.isVisible) {
            return null;
        }
        // Ensure the parent box sizing data is computed.
        if (!this._box) {
            this._box = domutils_1.ElementExt.boxSizing(this.parent.node);
        }
        // Convert from client to local coordinates.
        var rect = this.parent.node.getBoundingClientRect();
        var x = clientX - rect.left - this._box.borderLeft;
        var y = clientY - rect.top - this._box.borderTop;
        // Find the tab layout node at the local position.
        var tabNode = this._root.hitTestTabNodes(x, y);
        // Bail if a tab layout node was not found.
        if (!tabNode) {
            return null;
        }
        // Extract the data from the tab node.
        var tabBar = tabNode.tabBar, top = tabNode.top, left = tabNode.left, width = tabNode.width, height = tabNode.height;
        // Compute the right and bottom edges of the tab area.
        var borderWidth = this._box.borderLeft + this._box.borderRight;
        var borderHeight = this._box.borderTop + this._box.borderBottom;
        var right = rect.width - borderWidth - (left + width);
        var bottom = rect.height - borderHeight - (top + height);
        // Return the hit test results.
        return { tabBar: tabBar, x: x, y: y, top: top, left: left, right: right, bottom: bottom, width: width, height: height };
    };
    /**
     * Perform layout initialization which requires the parent widget.
     */
    DockLayout.prototype.init = function () {
        var _this = this;
        // Perform superclass initialization.
        _super.prototype.init.call(this);
        // Attach each widget to the parent.
        algorithm_1.each(this, function (widget) { _this.attachWidget(widget); });
        // Attach each handle to the parent.
        algorithm_1.each(this.handles(), function (handle) { _this.parent.node.appendChild(handle); });
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * Attach the widget to the layout parent widget.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This is a no-op if the widget is already attached.
     */
    DockLayout.prototype.attachWidget = function (widget) {
        // Do nothing if the widget is already attached.
        if (this.parent.node === widget.node.parentNode) {
            return;
        }
        // Create the layout item for the widget.
        this._items.set(widget, new layout_1.LayoutItem(widget));
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
    };
    /**
     * Detach the widget from the layout parent widget.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This is a no-op if the widget is not attached.
     */
    DockLayout.prototype.detachWidget = function (widget) {
        // Do nothing if the widget is not attached.
        if (this.parent.node !== widget.node.parentNode) {
            return;
        }
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
        // Delete the layout item for the widget.
        var item = this._items.get(widget);
        if (item) {
            this._items.delete(widget);
            item.dispose();
        }
    };
    /**
     * A message handler invoked on a `'before-show'` message.
     */
    DockLayout.prototype.onBeforeShow = function (msg) {
        _super.prototype.onBeforeShow.call(this, msg);
        this.parent.update();
    };
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    DockLayout.prototype.onBeforeAttach = function (msg) {
        _super.prototype.onBeforeAttach.call(this, msg);
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-shown'` message.
     */
    DockLayout.prototype.onChildShown = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-hidden'` message.
     */
    DockLayout.prototype.onChildHidden = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'resize'` message.
     */
    DockLayout.prototype.onResize = function (msg) {
        if (this.parent.isVisible) {
            this._update(msg.width, msg.height);
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    DockLayout.prototype.onUpdateRequest = function (msg) {
        if (this.parent.isVisible) {
            this._update(-1, -1);
        }
    };
    /**
     * A message handler invoked on a `'fit-request'` message.
     */
    DockLayout.prototype.onFitRequest = function (msg) {
        if (this.parent.isAttached) {
            this._fit();
        }
    };
    /**
     * Remove the specified widget from the layout structure.
     *
     * #### Notes
     * This is a no-op if the widget is not in the layout tree.
     *
     * This does not detach the widget from the parent node.
     */
    DockLayout.prototype._removeWidget = function (widget) {
        // Bail early if there is no layout root.
        if (!this._root) {
            return;
        }
        // Find the tab node which contains the given widget.
        var tabNode = this._root.findTabNode(widget);
        // Bail early if the tab node is not found.
        if (!tabNode) {
            return;
        }
        // If there are multiple tabs, just remove the widget's tab.
        if (tabNode.tabBar.titles.length > 1) {
            tabNode.tabBar.removeTab(widget.title);
            return;
        }
        // Otherwise, the tab node needs to be removed...
        // Dispose the tab bar.
        tabNode.tabBar.dispose();
        // Handle the case where the tab node is the root.
        if (this._root === tabNode) {
            this._root = null;
            return;
        }
        // Otherwise, remove the tab node from its parent...
        // Prevent widget resizing unless needed.
        this._root.holdAllSizes();
        // Clear the parent reference on the tab node.
        var splitNode = tabNode.parent;
        tabNode.parent = null;
        // Remove the tab node from its parent split node.
        var i = algorithm_1.ArrayExt.removeFirstOf(splitNode.children, tabNode);
        var handle = algorithm_1.ArrayExt.removeAt(splitNode.handles, i);
        algorithm_1.ArrayExt.removeAt(splitNode.sizers, i);
        // Remove the handle from its parent DOM node.
        if (handle.parentNode) {
            handle.parentNode.removeChild(handle);
        }
        // If there are multiple children, just update the handles.
        if (splitNode.children.length > 1) {
            splitNode.syncHandles();
            return;
        }
        // Otherwise, the split node also needs to be removed...
        // Clear the parent reference on the split node.
        var maybeParent = splitNode.parent;
        splitNode.parent = null;
        // Lookup the remaining child node and handle.
        var childNode = splitNode.children[0];
        var childHandle = splitNode.handles[0];
        // Clear the split node data.
        splitNode.children.length = 0;
        splitNode.handles.length = 0;
        splitNode.sizers.length = 0;
        // Remove the child handle from its parent node.
        if (childHandle.parentNode) {
            childHandle.parentNode.removeChild(childHandle);
        }
        // Handle the case where the split node is the root.
        if (this._root === splitNode) {
            childNode.parent = null;
            this._root = childNode;
            return;
        }
        // Otherwise, move the child node to the parent node...
        var parentNode = maybeParent;
        // Lookup the index of the split node.
        var j = parentNode.children.indexOf(splitNode);
        // Handle the case where the child node is a tab node.
        if (childNode instanceof Private.TabLayoutNode) {
            childNode.parent = parentNode;
            parentNode.children[j] = childNode;
            return;
        }
        // Remove the split data from the parent.
        var splitHandle = algorithm_1.ArrayExt.removeAt(parentNode.handles, j);
        algorithm_1.ArrayExt.removeAt(parentNode.children, j);
        algorithm_1.ArrayExt.removeAt(parentNode.sizers, j);
        // Remove the handle from its parent node.
        if (splitHandle.parentNode) {
            splitHandle.parentNode.removeChild(splitHandle);
        }
        // The child node and the split parent node will have the same
        // orientation. Merge the grand-children with the parent node.
        for (var i_1 = 0, n = childNode.children.length; i_1 < n; ++i_1) {
            var gChild = childNode.children[i_1];
            var gHandle = childNode.handles[i_1];
            var gSizer = childNode.sizers[i_1];
            algorithm_1.ArrayExt.insert(parentNode.children, j + i_1, gChild);
            algorithm_1.ArrayExt.insert(parentNode.handles, j + i_1, gHandle);
            algorithm_1.ArrayExt.insert(parentNode.sizers, j + i_1, gSizer);
            gChild.parent = parentNode;
        }
        // Clear the child node.
        childNode.children.length = 0;
        childNode.handles.length = 0;
        childNode.sizers.length = 0;
        childNode.parent = null;
        // Sync the handles on the parent node.
        parentNode.syncHandles();
    };
    /**
     * Insert a widget next to an existing tab.
     *
     * #### Notes
     * This does not attach the widget to the parent widget.
     */
    DockLayout.prototype._insertTab = function (widget, ref, refNode, after) {
        // Do nothing if the tab is inserted next to itself.
        if (widget === ref) {
            return;
        }
        // Create the root if it does not exist.
        if (!this._root) {
            var tabNode = new Private.TabLayoutNode(this._createTabBar());
            tabNode.tabBar.addTab(widget.title);
            this._root = tabNode;
            return;
        }
        // Use the first tab node as the ref node if needed.
        if (!refNode) {
            refNode = this._root.findFirstTabNode();
        }
        // If the widget is not contained in the ref node, ensure it is
        // removed from the layout and hidden before being added again.
        if (refNode.tabBar.titles.indexOf(widget.title) === -1) {
            this._removeWidget(widget);
            widget.hide();
        }
        // Lookup the target index for inserting the tab.
        var index;
        if (ref) {
            index = refNode.tabBar.titles.indexOf(ref.title);
        }
        else {
            index = refNode.tabBar.currentIndex;
        }
        // Insert the widget's tab relative to the target index.
        refNode.tabBar.insertTab(index + (after ? 1 : 0), widget.title);
    };
    /**
     * Insert a widget as a new split area.
     *
     * #### Notes
     * This does not attach the widget to the parent widget.
     */
    DockLayout.prototype._insertSplit = function (widget, ref, refNode, orientation, after) {
        // Do nothing if there is no effective split.
        if (widget === ref && refNode && refNode.tabBar.titles.length === 1) {
            return;
        }
        // Ensure the widget is removed from the current layout.
        this._removeWidget(widget);
        // Create the tab layout node to hold the widget.
        var tabNode = new Private.TabLayoutNode(this._createTabBar());
        tabNode.tabBar.addTab(widget.title);
        // Set the root if it does not exist.
        if (!this._root) {
            this._root = tabNode;
            return;
        }
        // If the ref node parent is null, split the root.
        if (!refNode || !refNode.parent) {
            // Ensure the root is split with the correct orientation.
            var root = this._splitRoot(orientation);
            // Determine the insert index for the new tab node.
            var i_2 = after ? root.children.length : 0;
            // Normalize the split node.
            root.normalizeSizes();
            // Create the sizer for new tab node.
            var sizer = Private.createSizer(refNode ? 1 : Private.GOLDEN_RATIO);
            // Insert the tab node sized to the golden ratio.
            algorithm_1.ArrayExt.insert(root.children, i_2, tabNode);
            algorithm_1.ArrayExt.insert(root.sizers, i_2, sizer);
            algorithm_1.ArrayExt.insert(root.handles, i_2, this._createHandle());
            tabNode.parent = root;
            // Re-normalize the split node to maintain the ratios.
            root.normalizeSizes();
            // Finally, synchronize the visibility of the handles.
            root.syncHandles();
            return;
        }
        // Lookup the split node for the ref widget.
        var splitNode = refNode.parent;
        // If the split node already had the correct orientation,
        // the widget can be inserted into the split node directly.
        if (splitNode.orientation === orientation) {
            // Find the index of the ref node.
            var i_3 = splitNode.children.indexOf(refNode);
            // Normalize the split node.
            splitNode.normalizeSizes();
            // Consume half the space for the insert location.
            var s = splitNode.sizers[i_3].sizeHint /= 2;
            // Insert the tab node sized to the other half.
            var j_1 = i_3 + (after ? 1 : 0);
            algorithm_1.ArrayExt.insert(splitNode.children, j_1, tabNode);
            algorithm_1.ArrayExt.insert(splitNode.sizers, j_1, Private.createSizer(s));
            algorithm_1.ArrayExt.insert(splitNode.handles, j_1, this._createHandle());
            tabNode.parent = splitNode;
            // Finally, synchronize the visibility of the handles.
            splitNode.syncHandles();
            return;
        }
        // Remove the ref node from the split node.
        var i = algorithm_1.ArrayExt.removeFirstOf(splitNode.children, refNode);
        // Create a new normalized split node for the children.
        var childNode = new Private.SplitLayoutNode(orientation);
        childNode.normalized = true;
        // Add the ref node sized to half the space.
        childNode.children.push(refNode);
        childNode.sizers.push(Private.createSizer(0.5));
        childNode.handles.push(this._createHandle());
        refNode.parent = childNode;
        // Add the tab node sized to the other half.
        var j = after ? 1 : 0;
        algorithm_1.ArrayExt.insert(childNode.children, j, tabNode);
        algorithm_1.ArrayExt.insert(childNode.sizers, j, Private.createSizer(0.5));
        algorithm_1.ArrayExt.insert(childNode.handles, j, this._createHandle());
        tabNode.parent = childNode;
        // Synchronize the visibility of the handles.
        childNode.syncHandles();
        // Finally, add the new child node to the original split node.
        algorithm_1.ArrayExt.insert(splitNode.children, i, childNode);
        childNode.parent = splitNode;
    };
    /**
     * Ensure the root is a split node with the given orientation.
     */
    DockLayout.prototype._splitRoot = function (orientation) {
        // Bail early if the root already meets the requirements.
        var oldRoot = this._root;
        if (oldRoot instanceof Private.SplitLayoutNode) {
            if (oldRoot.orientation === orientation) {
                return oldRoot;
            }
        }
        // Create a new root node with the specified orientation.
        var newRoot = this._root = new Private.SplitLayoutNode(orientation);
        // Add the old root to the new root.
        if (oldRoot) {
            newRoot.children.push(oldRoot);
            newRoot.sizers.push(Private.createSizer(0));
            newRoot.handles.push(this._createHandle());
            oldRoot.parent = newRoot;
        }
        // Return the new root as a convenience.
        return newRoot;
    };
    /**
     * Fit the layout to the total size required by the widgets.
     */
    DockLayout.prototype._fit = function () {
        // Set up the computed minimum size.
        var minW = 0;
        var minH = 0;
        // Update the size limits for the layout tree.
        if (this._root) {
            var limits = this._root.fit(this._spacing, this._items);
            minW = limits.minWidth;
            minH = limits.minHeight;
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
    DockLayout.prototype._update = function (offsetWidth, offsetHeight) {
        // Clear the dirty flag to indicate the update occurred.
        this._dirty = false;
        // Bail early if there is no root layout node.
        if (!this._root) {
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
        var x = this._box.paddingTop;
        var y = this._box.paddingLeft;
        var width = offsetWidth - this._box.horizontalSum;
        var height = offsetHeight - this._box.verticalSum;
        // Update the geometry of the layout tree.
        this._root.update(x, y, width, height, this._spacing, this._items);
    };
    /**
     * Create a new tab bar for use by the dock layout.
     *
     * #### Notes
     * The tab bar will be attached to the parent if it exists.
     */
    DockLayout.prototype._createTabBar = function () {
        // Create the tab bar using the renderer.
        var tabBar = this.renderer.createTabBar();
        // Enforce necessary tab bar behavior.
        tabBar.orientation = 'horizontal';
        // Reparent and attach the tab bar to the parent if possible.
        if (this.parent) {
            tabBar.parent = this.parent;
            this.attachWidget(tabBar);
        }
        // Return the initialized tab bar.
        return tabBar;
    };
    /**
     * Create a new handle for the dock layout.
     *
     * #### Notes
     * The handle will be attached to the parent if it exists.
     */
    DockLayout.prototype._createHandle = function () {
        // Create the handle using the renderer.
        var handle = this.renderer.createHandle();
        // Initialize the handle layout behavior.
        var style = handle.style;
        style.position = 'absolute';
        style.top = '0';
        style.left = '0';
        style.width = '0';
        style.height = '0';
        // Attach the handle to the parent if it exists.
        if (this.parent) {
            this.parent.node.appendChild(handle);
        }
        // Return the initialized handle.
        return handle;
    };
    return DockLayout;
}(layout_1.Layout));
exports.DockLayout = DockLayout;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * A fraction used for sizing root panels; ~= `1 / golden_ratio`.
     */
    Private.GOLDEN_RATIO = 0.618;
    /**
     * Clamp a spacing value to an integer >= 0.
     */
    function clampSpacing(value) {
        return Math.max(0, Math.floor(value));
    }
    Private.clampSpacing = clampSpacing;
    /**
     * Create a box sizer with an initial size hint.
     */
    function createSizer(hint) {
        var sizer = new boxengine_1.BoxSizer();
        sizer.sizeHint = hint;
        sizer.size = hint;
        return sizer;
    }
    Private.createSizer = createSizer;
    /**
     * Normalize an area config object and collect the visited widgets.
     */
    function normalizeAreaConfig(config, widgetSet) {
        var result;
        if (config.type === 'tab-area') {
            result = normalizeTabAreaConfig(config, widgetSet);
        }
        else {
            result = normalizeSplitAreaConfig(config, widgetSet);
        }
        return result;
    }
    Private.normalizeAreaConfig = normalizeAreaConfig;
    /**
     * Convert a normalized area config into a layout tree.
     */
    function realizeAreaConfig(config, renderer) {
        var node;
        if (config.type === 'tab-area') {
            node = realizeTabAreaConfig(config, renderer);
        }
        else {
            node = realizeSplitAreaConfig(config, renderer);
        }
        return node;
    }
    Private.realizeAreaConfig = realizeAreaConfig;
    /**
     * A layout node which holds the data for a tabbed area.
     */
    var TabLayoutNode = (function () {
        /**
         * Construct a new tab layout node.
         *
         * @param tabBar - The tab bar to use for the layout node.
         */
        function TabLayoutNode(tabBar) {
            /**
             * The parent of the layout node.
             */
            this.parent = null;
            this._top = 0;
            this._left = 0;
            this._width = 0;
            this._height = 0;
            var tabSizer = new boxengine_1.BoxSizer();
            var widgetSizer = new boxengine_1.BoxSizer();
            tabSizer.stretch = 0;
            widgetSizer.stretch = 1;
            this.tabBar = tabBar;
            this.sizers = [tabSizer, widgetSizer];
        }
        Object.defineProperty(TabLayoutNode.prototype, "top", {
            /**
             * The most recent value for the `top` edge of the layout box.
             */
            get: function () {
                return this._top;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(TabLayoutNode.prototype, "left", {
            /**
             * The most recent value for the `left` edge of the layout box.
             */
            get: function () {
                return this._left;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(TabLayoutNode.prototype, "width", {
            /**
             * The most recent value for the `width` of the layout box.
             */
            get: function () {
                return this._width;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(TabLayoutNode.prototype, "height", {
            /**
             * The most recent value for the `height` of the layout box.
             */
            get: function () {
                return this._height;
            },
            enumerable: true,
            configurable: true
        });
        /**
         * Create an iterator for all widgets in the layout tree.
         */
        TabLayoutNode.prototype.iterAllWidgets = function () {
            return algorithm_1.chain(algorithm_1.once(this.tabBar), this.iterUserWidgets());
        };
        /**
         * Create an iterator for the user widgets in the layout tree.
         */
        TabLayoutNode.prototype.iterUserWidgets = function () {
            return algorithm_1.map(this.tabBar.titles, function (title) { return title.owner; });
        };
        /**
         * Create an iterator for the selected widgets in the layout tree.
         */
        TabLayoutNode.prototype.iterSelectedWidgets = function () {
            var title = this.tabBar.currentTitle;
            return title ? algorithm_1.once(title.owner) : algorithm_1.empty();
        };
        /**
         * Create an iterator for the tab bars in the layout tree.
         */
        TabLayoutNode.prototype.iterTabBars = function () {
            return algorithm_1.once(this.tabBar);
        };
        /**
         * Create an iterator for the handles in the layout tree.
         */
        TabLayoutNode.prototype.iterHandles = function () {
            return algorithm_1.empty();
        };
        /**
         * Find the tab layout node which contains the given widget.
         */
        TabLayoutNode.prototype.findTabNode = function (widget) {
            return this.tabBar.titles.indexOf(widget.title) !== -1 ? this : null;
        };
        /**
         * Find the split layout node which contains the given handle.
         */
        TabLayoutNode.prototype.findSplitNode = function (handle) {
            return null;
        };
        /**
         * Find the first tab layout node in a layout tree.
         */
        TabLayoutNode.prototype.findFirstTabNode = function () {
            return this;
        };
        /**
         * Find the tab layout node which contains the local point.
         */
        TabLayoutNode.prototype.hitTestTabNodes = function (x, y) {
            if (x < this._left || x >= this._left + this._width) {
                return null;
            }
            if (y < this._top || y >= this._top + this._height) {
                return null;
            }
            return this;
        };
        /**
         * Create a configuration object for the layout tree.
         */
        TabLayoutNode.prototype.createConfig = function () {
            var widgets = this.tabBar.titles.map(function (title) { return title.owner; });
            var currentIndex = this.tabBar.currentIndex;
            return { type: 'tab-area', widgets: widgets, currentIndex: currentIndex };
        };
        /**
         * Recursively hold all of the sizes in the layout tree.
         *
         * This ignores the sizers of tab layout nodes.
         */
        TabLayoutNode.prototype.holdAllSizes = function () {
            return;
        };
        /**
         * Fit the layout tree.
         */
        TabLayoutNode.prototype.fit = function (spacing, items) {
            // Set up the limit variables.
            var minWidth = 0;
            var minHeight = 0;
            var maxWidth = Infinity;
            var maxHeight = Infinity;
            // Lookup the tab bar layout item.
            var tabBarItem = items.get(this.tabBar);
            // Lookup the widget layout item.
            var current = this.tabBar.currentTitle;
            var widgetItem = current ? items.get(current.owner) : undefined;
            // Lookup the tab bar and widget sizers.
            var _a = this.sizers, tabBarSizer = _a[0], widgetSizer = _a[1];
            // Update the tab bar limits.
            if (tabBarItem) {
                tabBarItem.fit();
            }
            // Update the widget limits.
            if (widgetItem) {
                widgetItem.fit();
            }
            // Update the results and sizer for the tab bar.
            if (tabBarItem && !tabBarItem.isHidden) {
                minWidth = Math.max(minWidth, tabBarItem.minWidth);
                minHeight += tabBarItem.minHeight;
                tabBarSizer.minSize = tabBarItem.minHeight;
                tabBarSizer.maxSize = tabBarItem.maxHeight;
            }
            else {
                tabBarSizer.minSize = 0;
                tabBarSizer.maxSize = 0;
            }
            // Update the results and sizer for the current widget.
            if (widgetItem && !widgetItem.isHidden) {
                minWidth = Math.max(minWidth, widgetItem.minWidth);
                minHeight += widgetItem.minHeight;
                widgetSizer.minSize = widgetItem.minHeight;
                widgetSizer.maxSize = Infinity;
            }
            else {
                widgetSizer.minSize = 0;
                widgetSizer.maxSize = Infinity;
            }
            // Return the computed size limits for the layout node.
            return { minWidth: minWidth, minHeight: minHeight, maxWidth: maxWidth, maxHeight: maxHeight };
        };
        /**
         * Update the layout tree.
         */
        TabLayoutNode.prototype.update = function (left, top, width, height, spacing, items) {
            // Update the layout box values.
            this._top = top;
            this._left = left;
            this._width = width;
            this._height = height;
            // Lookup the tab bar layout item.
            var tabBarItem = items.get(this.tabBar);
            // Lookup the widget layout item.
            var current = this.tabBar.currentTitle;
            var widgetItem = current ? items.get(current.owner) : undefined;
            // Distribute the layout space to the sizers.
            boxengine_1.BoxEngine.calc(this.sizers, height);
            // Update the tab bar item using the computed size.
            if (tabBarItem && !tabBarItem.isHidden) {
                var size = this.sizers[0].size;
                tabBarItem.update(left, top, width, size);
                top += size;
            }
            // Layout the widget using the computed size.
            if (widgetItem && !widgetItem.isHidden) {
                var size = this.sizers[1].size;
                widgetItem.update(left, top, width, size);
            }
        };
        return TabLayoutNode;
    }());
    Private.TabLayoutNode = TabLayoutNode;
    /**
     * A layout node which holds the data for a split area.
     */
    var SplitLayoutNode = (function () {
        /**
         * Construct a new split layout node.
         *
         * @param orientation - The orientation of the node.
         */
        function SplitLayoutNode(orientation) {
            /**
             * The parent of the layout node.
             */
            this.parent = null;
            /**
             * Whether the sizers have been normalized.
             */
            this.normalized = false;
            /**
             * The child nodes for the split node.
             */
            this.children = [];
            /**
             * The box sizers for the layout children.
             */
            this.sizers = [];
            /**
             * The handles for the layout children.
             */
            this.handles = [];
            this.orientation = orientation;
        }
        /**
         * Create an iterator for all widgets in the layout tree.
         */
        SplitLayoutNode.prototype.iterAllWidgets = function () {
            var children = algorithm_1.map(this.children, function (child) { return child.iterAllWidgets(); });
            return new algorithm_1.ChainIterator(children);
        };
        /**
         * Create an iterator for the user widgets in the layout tree.
         */
        SplitLayoutNode.prototype.iterUserWidgets = function () {
            var children = algorithm_1.map(this.children, function (child) { return child.iterUserWidgets(); });
            return new algorithm_1.ChainIterator(children);
        };
        /**
         * Create an iterator for the selected widgets in the layout tree.
         */
        SplitLayoutNode.prototype.iterSelectedWidgets = function () {
            var children = algorithm_1.map(this.children, function (child) { return child.iterSelectedWidgets(); });
            return new algorithm_1.ChainIterator(children);
        };
        /**
         * Create an iterator for the tab bars in the layout tree.
         */
        SplitLayoutNode.prototype.iterTabBars = function () {
            var children = algorithm_1.map(this.children, function (child) { return child.iterTabBars(); });
            return new algorithm_1.ChainIterator(children);
        };
        /**
         * Create an iterator for the handles in the layout tree.
         */
        SplitLayoutNode.prototype.iterHandles = function () {
            var children = algorithm_1.map(this.children, function (child) { return child.iterHandles(); });
            return algorithm_1.chain(this.handles, new algorithm_1.ChainIterator(children));
        };
        /**
         * Find the tab layout node which contains the given widget.
         */
        SplitLayoutNode.prototype.findTabNode = function (widget) {
            for (var i = 0, n = this.children.length; i < n; ++i) {
                var result = this.children[i].findTabNode(widget);
                if (result) {
                    return result;
                }
            }
            return null;
        };
        /**
         * Find the split layout node which contains the given handle.
         */
        SplitLayoutNode.prototype.findSplitNode = function (handle) {
            var index = this.handles.indexOf(handle);
            if (index !== -1) {
                return { index: index, node: this };
            }
            for (var i = 0, n = this.children.length; i < n; ++i) {
                var result = this.children[i].findSplitNode(handle);
                if (result) {
                    return result;
                }
            }
            return null;
        };
        /**
         * Find the first tab layout node in a layout tree.
         */
        SplitLayoutNode.prototype.findFirstTabNode = function () {
            if (this.children.length === 0) {
                return null;
            }
            return this.children[0].findFirstTabNode();
        };
        /**
         * Find the tab layout node which contains the local point.
         */
        SplitLayoutNode.prototype.hitTestTabNodes = function (x, y) {
            for (var i = 0, n = this.children.length; i < n; ++i) {
                var result = this.children[i].hitTestTabNodes(x, y);
                if (result) {
                    return result;
                }
            }
            return null;
        };
        /**
         * Create a configuration object for the layout tree.
         */
        SplitLayoutNode.prototype.createConfig = function () {
            var orientation = this.orientation;
            var sizes = this.createNormalizedSizes();
            var children = this.children.map(function (child) { return child.createConfig(); });
            return { type: 'split-area', orientation: orientation, children: children, sizes: sizes };
        };
        /**
         * Sync the visibility and orientation of the handles.
         */
        SplitLayoutNode.prototype.syncHandles = function () {
            var _this = this;
            algorithm_1.each(this.handles, function (handle, i) {
                handle.setAttribute('data-orientation', _this.orientation);
                if (i === _this.handles.length - 1) {
                    handle.classList.add('p-mod-hidden');
                }
                else {
                    handle.classList.remove('p-mod-hidden');
                }
            });
        };
        /**
         * Hold the current sizes of the box sizers.
         *
         * This sets the size hint of each sizer to its current size.
         */
        SplitLayoutNode.prototype.holdSizes = function () {
            algorithm_1.each(this.sizers, function (sizer) { sizer.sizeHint = sizer.size; });
        };
        /**
         * Recursively hold all of the sizes in the layout tree.
         *
         * This ignores the sizers of tab layout nodes.
         */
        SplitLayoutNode.prototype.holdAllSizes = function () {
            algorithm_1.each(this.children, function (child) { return child.holdAllSizes(); });
            this.holdSizes();
        };
        /**
         * Normalize the sizes of the split layout node.
         */
        SplitLayoutNode.prototype.normalizeSizes = function () {
            // Bail early if the sizers are empty.
            var n = this.sizers.length;
            if (n === 0) {
                return;
            }
            // Hold the current sizes of the sizers.
            this.holdSizes();
            // Compute the sum of the sizes.
            var sum = algorithm_1.reduce(this.sizers, function (v, sizer) { return v + sizer.sizeHint; }, 0);
            // Normalize the sizes based on the sum.
            if (sum === 0) {
                algorithm_1.each(this.sizers, function (sizer) {
                    sizer.size = sizer.sizeHint = 1 / n;
                });
            }
            else {
                algorithm_1.each(this.sizers, function (sizer) {
                    sizer.size = sizer.sizeHint /= sum;
                });
            }
            // Mark the sizes as normalized.
            this.normalized = true;
        };
        /**
         * Snap the normalized sizes of the split layout node.
         */
        SplitLayoutNode.prototype.createNormalizedSizes = function () {
            // Bail early if the sizers are empty.
            var n = this.sizers.length;
            if (n === 0) {
                return [];
            }
            // Grab the current sizes of the sizers.
            var sizes = this.sizers.map(function (sizer) { return sizer.size; });
            // Compute the sum of the sizes.
            var sum = algorithm_1.reduce(sizes, function (v, size) { return v + size; }, 0);
            // Normalize the sizes based on the sum.
            if (sum === 0) {
                algorithm_1.each(sizes, function (size, i) { sizes[i] = 1 / n; });
            }
            else {
                algorithm_1.each(sizes, function (size, i) { sizes[i] = size / sum; });
            }
            // Return the normalized sizes.
            return sizes;
        };
        /**
         * Fit the layout tree.
         */
        SplitLayoutNode.prototype.fit = function (spacing, items) {
            // Compute the required fixed space.
            var horizontal = this.orientation === 'horizontal';
            var fixed = Math.max(0, this.children.length - 1) * spacing;
            // Set up the limit variables.
            var minWidth = horizontal ? fixed : 0;
            var minHeight = horizontal ? 0 : fixed;
            var maxWidth = Infinity;
            var maxHeight = Infinity;
            // Fit the children and update the limits.
            for (var i = 0, n = this.children.length; i < n; ++i) {
                var limits = this.children[i].fit(spacing, items);
                if (horizontal) {
                    minHeight = Math.max(minHeight, limits.minHeight);
                    minWidth += limits.minWidth;
                    this.sizers[i].minSize = limits.minWidth;
                }
                else {
                    minWidth = Math.max(minWidth, limits.minWidth);
                    minHeight += limits.minHeight;
                    this.sizers[i].minSize = limits.minHeight;
                }
            }
            // Return the computed limits for the layout node.
            return { minWidth: minWidth, minHeight: minHeight, maxWidth: maxWidth, maxHeight: maxHeight };
        };
        /**
         * Update the layout tree.
         */
        SplitLayoutNode.prototype.update = function (left, top, width, height, spacing, items) {
            // Compute the available layout space.
            var horizontal = this.orientation === 'horizontal';
            var fixed = Math.max(0, this.children.length - 1) * spacing;
            var space = Math.max(0, (horizontal ? width : height) - fixed);
            // De-normalize the sizes if needed.
            if (this.normalized) {
                algorithm_1.each(this.sizers, function (sizer) { sizer.sizeHint *= space; });
                this.normalized = false;
            }
            // Distribute the layout space to the sizers.
            boxengine_1.BoxEngine.calc(this.sizers, space);
            // Update the geometry of the child nodes and handles.
            for (var i = 0, n = this.children.length; i < n; ++i) {
                var child = this.children[i];
                var size = this.sizers[i].size;
                var handleStyle = this.handles[i].style;
                if (horizontal) {
                    child.update(left, top, size, height, spacing, items);
                    left += size;
                    handleStyle.top = top + "px";
                    handleStyle.left = left + "px";
                    handleStyle.width = spacing + "px";
                    handleStyle.height = height + "px";
                    left += spacing;
                }
                else {
                    child.update(left, top, width, size, spacing, items);
                    top += size;
                    handleStyle.top = top + "px";
                    handleStyle.left = left + "px";
                    handleStyle.width = width + "px";
                    handleStyle.height = spacing + "px";
                    top += spacing;
                }
            }
        };
        return SplitLayoutNode;
    }());
    Private.SplitLayoutNode = SplitLayoutNode;
    /**
     * Normalize a tab area config and collect the visited widgets.
     */
    function normalizeTabAreaConfig(config, widgetSet) {
        // Bail early if there is no content.
        if (config.widgets.length === 0) {
            return null;
        }
        // Setup the filtered widgets array.
        var widgets = [];
        // Filter the config for unique widgets.
        algorithm_1.each(config.widgets, function (widget) {
            if (!widgetSet.has(widget)) {
                widgetSet.add(widget);
                widgets.push(widget);
            }
        });
        // Bail if there are no effective widgets.
        if (widgets.length === 0) {
            return null;
        }
        // Normalize the current index.
        var index = config.currentIndex;
        if (index !== -1 && (index < 0 || index >= widgets.length)) {
            index = 0;
        }
        // Return a normalized config object.
        return { type: 'tab-area', widgets: widgets, currentIndex: index };
    }
    /**
     * Normalize a split area config and collect the visited widgets.
     */
    function normalizeSplitAreaConfig(config, widgetSet) {
        // Set up the result variables.
        var orientation = config.orientation;
        var children = [];
        var sizes = [];
        // Normalize the config children.
        for (var i = 0, n = config.children.length; i < n; ++i) {
            // Normalize the child config.
            var child = normalizeAreaConfig(config.children[i], widgetSet);
            // Ignore an empty child.
            if (!child) {
                continue;
            }
            // Add the child or hoist its content as appropriate.
            if (child.type === 'tab-area' || child.orientation !== orientation) {
                children.push(child);
                sizes.push(Math.abs(config.sizes[i] || 0));
            }
            else {
                children.push.apply(children, child.children);
                sizes.push.apply(sizes, child.sizes);
            }
        }
        // Bail if there are no effective children.
        if (children.length === 0) {
            return null;
        }
        // If there is only one effective child, return that child.
        if (children.length === 1) {
            return children[0];
        }
        // Return a normalized config object.
        return { type: 'split-area', orientation: orientation, children: children, sizes: sizes };
    }
    /**
     * Convert a normalized tab area config into a layout tree.
     */
    function realizeTabAreaConfig(config, renderer) {
        // Create the tab bar for the layout node.
        var tabBar = renderer.createTabBar();
        // Hide each widget and add it to the tab bar.
        algorithm_1.each(config.widgets, function (widget) {
            widget.hide();
            tabBar.addTab(widget.title);
        });
        // Set the current index of the tab bar.
        tabBar.currentIndex = config.currentIndex;
        // Return the new tab layout node.
        return new TabLayoutNode(tabBar);
    }
    /**
     * Convert a normalized split area config into a layout tree.
     */
    function realizeSplitAreaConfig(config, renderer) {
        // Create the split layout node.
        var node = new SplitLayoutNode(config.orientation);
        // Add each child to the layout node.
        algorithm_1.each(config.children, function (child, i) {
            // Create the child data for the layout node.
            var childNode = realizeAreaConfig(child, renderer);
            var sizer = createSizer(config.sizes[i]);
            var handle = renderer.createHandle();
            // Add the child data to the layout node.
            node.children.push(childNode);
            node.handles.push(handle);
            node.sizers.push(sizer);
            // Update the parent for the child node.
            childNode.parent = node;
        });
        // Synchronize the handle state for the layout node.
        node.syncHandles();
        // Normalize the sizes for the layout node.
        node.normalizeSizes();
        // Return the new layout node.
        return node;
    }
})(Private || (Private = {}));
