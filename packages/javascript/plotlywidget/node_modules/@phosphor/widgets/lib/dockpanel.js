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
var coreutils_1 = require("@phosphor/coreutils");
var domutils_1 = require("@phosphor/domutils");
var dragdrop_1 = require("@phosphor/dragdrop");
var messaging_1 = require("@phosphor/messaging");
var properties_1 = require("@phosphor/properties");
var signaling_1 = require("@phosphor/signaling");
var docklayout_1 = require("./docklayout");
var tabbar_1 = require("./tabbar");
var widget_1 = require("./widget");
/**
 * A widget which provides a flexible docking area for widgets.
 */
var DockPanel = (function (_super) {
    __extends(DockPanel, _super);
    /**
     * Construct a new dock panel.
     *
     * @param options - The options for initializing the panel.
     */
    function DockPanel(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this) || this;
        _this._drag = null;
        _this._pressData = null;
        _this._layoutModified = new signaling_1.Signal(_this);
        _this.addClass('p-DockPanel');
        _this._mode = options.mode || 'multiple-document';
        _this._renderer = options.renderer || DockPanel.defaultRenderer;
        // Toggle the CSS mode attribute.
        _this.dataset['mode'] = _this._mode;
        // Create the delegate renderer for the layout.
        var renderer = {
            createTabBar: function () { return _this._createTabBar(); },
            createHandle: function () { return _this._createHandle(); }
        };
        // Set up the dock layout for the panel.
        _this.layout = new docklayout_1.DockLayout({ renderer: renderer, spacing: options.spacing });
        // Set up the overlay drop indicator.
        _this.overlay = options.overlay || new DockPanel.Overlay();
        _this.node.appendChild(_this.overlay.node);
        return _this;
    }
    /**
     * Dispose of the resources held by the panel.
     */
    DockPanel.prototype.dispose = function () {
        // Ensure the mouse is released.
        this._releaseMouse();
        // Hide the overlay.
        this.overlay.hide(0);
        // Cancel a drag if one is in progress.
        if (this._drag) {
            this._drag.dispose();
        }
        // Dispose of the base class.
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(DockPanel.prototype, "layoutModified", {
        /**
         * A signal emitted when the layout configuration is modified.
         *
         * #### Notes
         * This signal is emitted whenever the current layout configuration
         * may have changed.
         *
         * This signal is emitted asynchronously in a collapsed fashion, so
         * that multiple synchronous modifications results in only a single
         * emit of the signal.
         */
        get: function () {
            return this._layoutModified;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockPanel.prototype, "renderer", {
        /**
         * The renderer used by the dock panel.
         */
        get: function () {
            return this.layout.renderer;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockPanel.prototype, "spacing", {
        /**
         * Get the spacing between the widgets.
         */
        get: function () {
            return this.layout.spacing;
        },
        /**
         * Set the spacing between the widgets.
         */
        set: function (value) {
            this.layout.spacing = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockPanel.prototype, "mode", {
        /**
         * Get the mode for the dock panel.
         */
        get: function () {
            return this._mode;
        },
        /**
         * Set the mode for the dock panel.
         *
         * #### Notes
         * Changing the mode is a destructive operation with respect to the
         * panel's layout configuration. If layout state must be preserved,
         * save the current layout config before changing the mode.
         */
        set: function (value) {
            // Bail early if the mode does not change.
            if (this._mode === value) {
                return;
            }
            // Update the internal mode.
            this._mode = value;
            // Toggle the CSS mode attribute.
            this.dataset['mode'] = value;
            // Get the layout for the panel.
            var layout = this.layout;
            // Configure the layout for the specified mode.
            switch (value) {
                case 'multiple-document':
                    algorithm_1.each(layout.tabBars(), function (tabBar) { tabBar.show(); });
                    break;
                case 'single-document':
                    layout.restoreLayout(Private.createSingleDocumentConfig(this));
                    break;
                default:
                    throw 'unreachable';
            }
            // Schedule an emit of the layout modified signal.
            messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockPanel.prototype, "isEmpty", {
        /**
         * Whether the dock panel is empty.
         */
        get: function () {
            return this.layout.isEmpty;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Create an iterator over the user widgets in the panel.
     *
     * @returns A new iterator over the user widgets in the panel.
     *
     * #### Notes
     * This iterator does not include the generated tab bars.
     */
    DockPanel.prototype.widgets = function () {
        return this.layout.widgets();
    };
    /**
     * Create an iterator over the selected widgets in the panel.
     *
     * @returns A new iterator over the selected user widgets.
     *
     * #### Notes
     * This iterator yields the widgets corresponding to the current tab
     * of each tab bar in the panel.
     */
    DockPanel.prototype.selectedWidgets = function () {
        return this.layout.selectedWidgets();
    };
    /**
     * Create an iterator over the tab bars in the panel.
     *
     * @returns A new iterator over the tab bars in the panel.
     *
     * #### Notes
     * This iterator does not include the user widgets.
     */
    DockPanel.prototype.tabBars = function () {
        return this.layout.tabBars();
    };
    /**
     * Create an iterator over the handles in the panel.
     *
     * @returns A new iterator over the handles in the panel.
     */
    DockPanel.prototype.handles = function () {
        return this.layout.handles();
    };
    /**
     * Select a specific widget in the dock panel.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * This will make the widget the current widget in its tab area.
     */
    DockPanel.prototype.selectWidget = function (widget) {
        // Find the tab bar which contains the widget.
        var tabBar = algorithm_1.find(this.tabBars(), function (bar) {
            return bar.titles.indexOf(widget.title) !== -1;
        });
        // Throw an error if no tab bar is found.
        if (!tabBar) {
            throw new Error('Widget is not contained in the dock panel.');
        }
        // Ensure the widget is the current widget.
        tabBar.currentTitle = widget.title;
    };
    /**
     * Activate a specified widget in the dock panel.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * This will select and activate the given widget.
     */
    DockPanel.prototype.activateWidget = function (widget) {
        this.selectWidget(widget);
        widget.activate();
    };
    /**
     * Save the current layout configuration of the dock panel.
     *
     * @returns A new config object for the current layout state.
     *
     * #### Notes
     * The return value can be provided to the `restoreLayout` method
     * in order to restore the layout to its current configuration.
     */
    DockPanel.prototype.saveLayout = function () {
        return this.layout.saveLayout();
    };
    /**
     * Restore the layout to a previously saved configuration.
     *
     * @param config - The layout configuration to restore.
     *
     * #### Notes
     * Widgets which currently belong to the layout but which are not
     * contained in the config will be unparented.
     *
     * The dock panel automatically reverts to `'multiple-document'`
     * mode when a layout config is restored.
     */
    DockPanel.prototype.restoreLayout = function (config) {
        // Reset the mode.
        this._mode = 'multiple-document';
        // Restore the layout.
        this.layout.restoreLayout(config);
        // Flush the message loop on IE and Edge to prevent flicker.
        if (domutils_1.Platform.IS_EDGE || domutils_1.Platform.IS_IE) {
            messaging_1.MessageLoop.flush();
        }
        // Schedule an emit of the layout modified signal.
        messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
    };
    /**
     * Add a widget to the dock panel.
     *
     * @param widget - The widget to add to the dock panel.
     *
     * @param options - The additional options for adding the widget.
     *
     * #### Notes
     * If the panel is in single document mode, the options are ignored
     * and the widget is always added as tab in the hidden tab bar.
     */
    DockPanel.prototype.addWidget = function (widget, options) {
        if (options === void 0) { options = {}; }
        // Add the widget to the layout.
        if (this._mode === 'single-document') {
            this.layout.addWidget(widget);
        }
        else {
            this.layout.addWidget(widget, options);
        }
        // Schedule an emit of the layout modified signal.
        messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
    };
    /**
     * Process a message sent to the widget.
     *
     * @param msg - The message sent to the widget.
     */
    DockPanel.prototype.processMessage = function (msg) {
        if (msg.type === 'layout-modified') {
            this._layoutModified.emit(undefined);
        }
        else {
            _super.prototype.processMessage.call(this, msg);
        }
    };
    /**
     * Handle the DOM events for the dock panel.
     *
     * @param event - The DOM event sent to the panel.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the panel's DOM node. It should
     * not be called directly by user code.
     */
    DockPanel.prototype.handleEvent = function (event) {
        switch (event.type) {
            case 'p-dragenter':
                this._evtDragEnter(event);
                break;
            case 'p-dragleave':
                this._evtDragLeave(event);
                break;
            case 'p-dragover':
                this._evtDragOver(event);
                break;
            case 'p-drop':
                this._evtDrop(event);
                break;
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
    DockPanel.prototype.onBeforeAttach = function (msg) {
        this.node.addEventListener('p-dragenter', this);
        this.node.addEventListener('p-dragleave', this);
        this.node.addEventListener('p-dragover', this);
        this.node.addEventListener('p-drop', this);
        this.node.addEventListener('mousedown', this);
    };
    /**
     * A message handler invoked on an `'after-detach'` message.
     */
    DockPanel.prototype.onAfterDetach = function (msg) {
        this.node.removeEventListener('p-dragenter', this);
        this.node.removeEventListener('p-dragleave', this);
        this.node.removeEventListener('p-dragover', this);
        this.node.removeEventListener('p-drop', this);
        this.node.removeEventListener('mousedown', this);
        this._releaseMouse();
    };
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    DockPanel.prototype.onChildAdded = function (msg) {
        // Ignore the generated tab bars.
        if (Private.isGeneratedTabBarProperty.get(msg.child)) {
            return;
        }
        // Add the widget class to the child.
        msg.child.addClass('p-DockPanel-widget');
    };
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    DockPanel.prototype.onChildRemoved = function (msg) {
        // Ignore the generated tab bars.
        if (Private.isGeneratedTabBarProperty.get(msg.child)) {
            return;
        }
        // Remove the widget class from the child.
        msg.child.removeClass('p-DockPanel-widget');
        // Schedule an emit of the layout modified signal.
        messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
    };
    /**
     * Handle the `'p-dragenter'` event for the dock panel.
     */
    DockPanel.prototype._evtDragEnter = function (event) {
        // If the factory mime type is present, mark the event as
        // handled in order to get the rest of the drag events.
        if (event.mimeData.hasData('application/vnd.phosphor.widget-factory')) {
            event.preventDefault();
            event.stopPropagation();
        }
    };
    /**
     * Handle the `'p-dragleave'` event for the dock panel.
     */
    DockPanel.prototype._evtDragLeave = function (event) {
        // Mark the event as handled.
        event.preventDefault();
        event.stopPropagation();
        // Get the node into which the drag is entering.
        var related = event.relatedTarget;
        // Hide the overlay if the drag is leaving the dock panel.
        if (!related || !this.node.contains(related)) {
            this.overlay.hide(0);
        }
    };
    /**
     * Handle the `'p-dragover'` event for the dock panel.
     */
    DockPanel.prototype._evtDragOver = function (event) {
        // Mark the event as handled.
        event.preventDefault();
        event.stopPropagation();
        // Show the drop indicator overlay and update the drop
        // action based on the drop target zone under the mouse.
        if (this._showOverlay(event.clientX, event.clientY) === 'invalid') {
            event.dropAction = 'none';
        }
        else {
            event.dropAction = event.proposedAction;
        }
    };
    /**
     * Handle the `'p-drop'` event for the dock panel.
     */
    DockPanel.prototype._evtDrop = function (event) {
        // Mark the event as handled.
        event.preventDefault();
        event.stopPropagation();
        // Hide the drop indicator overlay.
        this.overlay.hide(0);
        // Bail if the proposed action is to do nothing.
        if (event.proposedAction === 'none') {
            event.dropAction = 'none';
            return;
        }
        // Find the drop target under the mouse.
        var clientX = event.clientX, clientY = event.clientY;
        var _a = Private.findDropTarget(this, clientX, clientY), zone = _a.zone, target = _a.target;
        // Bail if the drop zone is invalid.
        if (zone === 'invalid') {
            event.dropAction = 'none';
            return;
        }
        // Bail if the factory mime type has invalid data.
        var mimeData = event.mimeData;
        var factory = mimeData.getData('application/vnd.phosphor.widget-factory');
        if (typeof factory !== 'function') {
            event.dropAction = 'none';
            return;
        }
        // Bail if the factory does not produce a widget.
        var widget = factory();
        if (!(widget instanceof widget_1.Widget)) {
            event.dropAction = 'none';
            return;
        }
        // Bail if the widget is an ancestor of the dock panel.
        if (widget.contains(this)) {
            event.dropAction = 'none';
            return;
        }
        // Find the reference widget for the drop target.
        var ref = target ? Private.getDropRef(target.tabBar) : null;
        // Add the widget according to the indicated drop zone.
        switch (zone) {
            case 'root-all':
                this.addWidget(widget);
                break;
            case 'root-top':
                this.addWidget(widget, { mode: 'split-top' });
                break;
            case 'root-left':
                this.addWidget(widget, { mode: 'split-left' });
                break;
            case 'root-right':
                this.addWidget(widget, { mode: 'split-right' });
                break;
            case 'root-bottom':
                this.addWidget(widget, { mode: 'split-bottom' });
                break;
            case 'widget-all':
                this.addWidget(widget, { mode: 'tab-after', ref: ref });
                break;
            case 'widget-top':
                this.addWidget(widget, { mode: 'split-top', ref: ref });
                break;
            case 'widget-left':
                this.addWidget(widget, { mode: 'split-left', ref: ref });
                break;
            case 'widget-right':
                this.addWidget(widget, { mode: 'split-right', ref: ref });
                break;
            case 'widget-bottom':
                this.addWidget(widget, { mode: 'split-bottom', ref: ref });
                break;
            default:
                throw 'unreachable';
        }
        // Accept the proposed drop action.
        event.dropAction = event.proposedAction;
        // Activate the dropped widget.
        this.activateWidget(widget);
    };
    /**
     * Handle the `'keydown'` event for the dock panel.
     */
    DockPanel.prototype._evtKeyDown = function (event) {
        // Stop input events during drag.
        event.preventDefault();
        event.stopPropagation();
        // Release the mouse if `Escape` is pressed.
        if (event.keyCode === 27) {
            // Finalize the mouse release.
            this._releaseMouse();
            // Schedule an emit of the layout modified signal.
            messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
        }
    };
    /**
     * Handle the `'mousedown'` event for the dock panel.
     */
    DockPanel.prototype._evtMouseDown = function (event) {
        // Do nothing if the left mouse button is not pressed.
        if (event.button !== 0) {
            return;
        }
        // Find the handle which contains the mouse target, if any.
        var layout = this.layout;
        var target = event.target;
        var handle = algorithm_1.find(layout.handles(), function (handle) { return handle.contains(target); });
        if (!handle) {
            return;
        }
        // Stop the event when a handle is pressed.
        event.preventDefault();
        event.stopPropagation();
        // Add the extra document listeners.
        document.addEventListener('keydown', this, true);
        document.addEventListener('mouseup', this, true);
        document.addEventListener('mousemove', this, true);
        document.addEventListener('contextmenu', this, true);
        // Compute the offset deltas for the handle press.
        var rect = handle.getBoundingClientRect();
        var deltaX = event.clientX - rect.left;
        var deltaY = event.clientY - rect.top;
        // Override the cursor and store the press data.
        var style = window.getComputedStyle(handle);
        var override = dragdrop_1.Drag.overrideCursor(style.cursor);
        this._pressData = { handle: handle, deltaX: deltaX, deltaY: deltaY, override: override };
    };
    /**
     * Handle the `'mousemove'` event for the dock panel.
     */
    DockPanel.prototype._evtMouseMove = function (event) {
        // Bail early if no drag is in progress.
        if (!this._pressData) {
            return;
        }
        // Stop the event when dragging a handle.
        event.preventDefault();
        event.stopPropagation();
        // Compute the desired offset position for the handle.
        var rect = this.node.getBoundingClientRect();
        var xPos = event.clientX - rect.left - this._pressData.deltaX;
        var yPos = event.clientY - rect.top - this._pressData.deltaY;
        // Set the handle as close to the desired position as possible.
        var layout = this.layout;
        layout.moveHandle(this._pressData.handle, xPos, yPos);
    };
    /**
     * Handle the `'mouseup'` event for the dock panel.
     */
    DockPanel.prototype._evtMouseUp = function (event) {
        // Do nothing if the left mouse button is not released.
        if (event.button !== 0) {
            return;
        }
        // Stop the event when releasing a handle.
        event.preventDefault();
        event.stopPropagation();
        // Finalize the mouse release.
        this._releaseMouse();
        // Schedule an emit of the layout modified signal.
        messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
    };
    /**
     * Release the mouse grab for the dock panel.
     */
    DockPanel.prototype._releaseMouse = function () {
        // Bail early if no drag is in progress.
        if (!this._pressData) {
            return;
        }
        // Clear the override cursor.
        this._pressData.override.dispose();
        this._pressData = null;
        // Remove the extra document listeners.
        document.removeEventListener('keydown', this, true);
        document.removeEventListener('mouseup', this, true);
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('contextmenu', this, true);
    };
    /**
     * Show the overlay indicator at the given client position.
     *
     * Returns the drop zone at the specified client position.
     *
     * #### Notes
     * If the position is not over a valid zone, the overlay is hidden.
     */
    DockPanel.prototype._showOverlay = function (clientX, clientY) {
        // Find the dock target for the given client position.
        var _a = Private.findDropTarget(this, clientX, clientY), zone = _a.zone, target = _a.target;
        // If the drop zone is invalid, hide the overlay and bail.
        if (zone === 'invalid') {
            this.overlay.hide(100);
            return zone;
        }
        // Setup the variables needed to compute the overlay geometry.
        var top;
        var left;
        var right;
        var bottom;
        var box = domutils_1.ElementExt.boxSizing(this.node); // TODO cache this?
        var rect = this.node.getBoundingClientRect();
        // Compute the overlay geometry based on the dock zone.
        switch (zone) {
            case 'root-all':
                top = box.paddingTop;
                left = box.paddingLeft;
                right = box.paddingRight;
                bottom = box.paddingBottom;
                break;
            case 'root-top':
                top = box.paddingTop;
                left = box.paddingLeft;
                right = box.paddingRight;
                bottom = rect.height * Private.GOLDEN_RATIO;
                break;
            case 'root-left':
                top = box.paddingTop;
                left = box.paddingLeft;
                right = rect.width * Private.GOLDEN_RATIO;
                bottom = box.paddingBottom;
                break;
            case 'root-right':
                top = box.paddingTop;
                left = rect.width * Private.GOLDEN_RATIO;
                right = box.paddingRight;
                bottom = box.paddingBottom;
                break;
            case 'root-bottom':
                top = rect.height * Private.GOLDEN_RATIO;
                left = box.paddingLeft;
                right = box.paddingRight;
                bottom = box.paddingBottom;
                break;
            case 'widget-all':
                top = target.top;
                left = target.left;
                right = target.right;
                bottom = target.bottom;
                break;
            case 'widget-top':
                top = target.top;
                left = target.left;
                right = target.right;
                bottom = target.bottom + target.height / 2;
                break;
            case 'widget-left':
                top = target.top;
                left = target.left;
                right = target.right + target.width / 2;
                bottom = target.bottom;
                break;
            case 'widget-right':
                top = target.top;
                left = target.left + target.width / 2;
                right = target.right;
                bottom = target.bottom;
                break;
            case 'widget-bottom':
                top = target.top + target.height / 2;
                left = target.left;
                right = target.right;
                bottom = target.bottom;
                break;
            default:
                throw 'unreachable';
        }
        // Show the overlay with the computed geometry.
        this.overlay.show({ top: top, left: left, right: right, bottom: bottom });
        // Finally, return the computed drop zone.
        return zone;
    };
    /**
     * Create a new tab bar for use by the panel.
     */
    DockPanel.prototype._createTabBar = function () {
        // Create the tab bar.
        var tabBar = this._renderer.createTabBar();
        // Set the generated tab bar property for the tab bar.
        Private.isGeneratedTabBarProperty.set(tabBar, true);
        // Hide the tab bar when in single document mode.
        if (this._mode === 'single-document') {
            tabBar.hide();
        }
        // Enforce necessary tab bar behavior.
        // TODO do we really want to enforce *all* of these?
        tabBar.tabsMovable = true;
        tabBar.allowDeselect = false;
        tabBar.removeBehavior = 'select-previous-tab';
        tabBar.insertBehavior = 'select-tab-if-needed';
        // Connect the signal handlers for the tab bar.
        tabBar.tabMoved.connect(this._onTabMoved, this);
        tabBar.currentChanged.connect(this._onCurrentChanged, this);
        tabBar.tabCloseRequested.connect(this._onTabCloseRequested, this);
        tabBar.tabDetachRequested.connect(this._onTabDetachRequested, this);
        tabBar.tabActivateRequested.connect(this._onTabActivateRequested, this);
        // Return the initialized tab bar.
        return tabBar;
    };
    /**
     * Create a new handle for use by the panel.
     */
    DockPanel.prototype._createHandle = function () {
        return this._renderer.createHandle();
    };
    /**
     * Handle the `tabMoved` signal from a tab bar.
     */
    DockPanel.prototype._onTabMoved = function () {
        messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
    };
    /**
     * Handle the `currentChanged` signal from a tab bar.
     */
    DockPanel.prototype._onCurrentChanged = function (sender, args) {
        // Extract the previous and current title from the args.
        var previousTitle = args.previousTitle, currentTitle = args.currentTitle;
        // Hide the previous widget.
        if (previousTitle) {
            previousTitle.owner.hide();
        }
        // Show the current widget.
        if (currentTitle) {
            currentTitle.owner.show();
        }
        // Flush the message loop on IE and Edge to prevent flicker.
        if (domutils_1.Platform.IS_EDGE || domutils_1.Platform.IS_IE) {
            messaging_1.MessageLoop.flush();
        }
        // Schedule an emit of the layout modified signal.
        messaging_1.MessageLoop.postMessage(this, Private.LayoutModified);
    };
    /**
     * Handle the `tabActivateRequested` signal from a tab bar.
     */
    DockPanel.prototype._onTabActivateRequested = function (sender, args) {
        args.title.owner.activate();
    };
    /**
     * Handle the `tabCloseRequested` signal from a tab bar.
     */
    DockPanel.prototype._onTabCloseRequested = function (sender, args) {
        args.title.owner.close();
    };
    /**
     * Handle the `tabDetachRequested` signal from a tab bar.
     */
    DockPanel.prototype._onTabDetachRequested = function (sender, args) {
        var _this = this;
        // Do nothing if a drag is already in progress.
        if (this._drag) {
            return;
        }
        // Release the tab bar's hold on the mouse.
        sender.releaseMouse();
        // Extract the data from the args.
        var title = args.title, tab = args.tab, clientX = args.clientX, clientY = args.clientY;
        // Setup the mime data for the drag operation.
        var mimeData = new coreutils_1.MimeData();
        var factory = function () { return title.owner; };
        mimeData.setData('application/vnd.phosphor.widget-factory', factory);
        // Create the drag image for the drag operation.
        var dragImage = tab.cloneNode(true);
        // Create the drag object to manage the drag-drop operation.
        this._drag = new dragdrop_1.Drag({
            mimeData: mimeData, dragImage: dragImage,
            proposedAction: 'move',
            supportedActions: 'move',
        });
        // Hide the tab node in the original tab.
        tab.classList.add('p-mod-hidden');
        // Create the cleanup callback.
        var cleanup = (function () {
            _this._drag = null;
            tab.classList.remove('p-mod-hidden');
        });
        // Start the drag operation and cleanup when done.
        this._drag.start(clientX, clientY).then(cleanup);
    };
    return DockPanel;
}(widget_1.Widget));
exports.DockPanel = DockPanel;
/**
 * The namespace for the `DockPanel` class statics.
 */
(function (DockPanel) {
    /**
     * A concrete implementation of `IOverlay`.
     *
     * This is the default overlay implementation for a dock panel.
     */
    var Overlay = (function () {
        /**
         * Construct a new overlay.
         */
        function Overlay() {
            this._timer = -1;
            this._hidden = true;
            this.node = document.createElement('div');
            this.node.classList.add('p-DockPanel-overlay');
            this.node.classList.add('p-mod-hidden');
            this.node.style.position = 'absolute';
        }
        /**
         * Show the overlay using the given overlay geometry.
         *
         * @param geo - The desired geometry for the overlay.
         */
        Overlay.prototype.show = function (geo) {
            // Update the position of the overlay.
            var style = this.node.style;
            style.top = geo.top + "px";
            style.left = geo.left + "px";
            style.right = geo.right + "px";
            style.bottom = geo.bottom + "px";
            // Clear any pending hide timer.
            clearTimeout(this._timer);
            this._timer = -1;
            // If the overlay is already visible, we're done.
            if (!this._hidden) {
                return;
            }
            // Clear the hidden flag.
            this._hidden = false;
            // Finally, show the overlay.
            this.node.classList.remove('p-mod-hidden');
        };
        /**
         * Hide the overlay node.
         *
         * @param delay - The delay (in ms) before hiding the overlay.
         *   A delay value <= 0 will hide the overlay immediately.
         */
        Overlay.prototype.hide = function (delay) {
            var _this = this;
            // Do nothing if the overlay is already hidden.
            if (this._hidden) {
                return;
            }
            // Hide immediately if the delay is <= 0.
            if (delay <= 0) {
                clearTimeout(this._timer);
                this._timer = -1;
                this._hidden = true;
                this.node.classList.add('p-mod-hidden');
                return;
            }
            // Do nothing if a hide is already pending.
            if (this._timer !== -1) {
                return;
            }
            // Otherwise setup the hide timer.
            this._timer = setTimeout(function () {
                _this._timer = -1;
                _this._hidden = true;
                _this.node.classList.add('p-mod-hidden');
            }, delay);
        };
        return Overlay;
    }());
    DockPanel.Overlay = Overlay;
    /**
     * The default implementation of `IRenderer`.
     */
    var Renderer = (function () {
        function Renderer() {
        }
        /**
         * Create a new tab bar for use with a dock panel.
         *
         * @returns A new tab bar for a dock panel.
         */
        Renderer.prototype.createTabBar = function () {
            var bar = new tabbar_1.TabBar();
            bar.addClass('p-DockPanel-tabBar');
            return bar;
        };
        /**
         * Create a new handle node for use with a dock panel.
         *
         * @returns A new handle node for a dock panel.
         */
        Renderer.prototype.createHandle = function () {
            var handle = document.createElement('div');
            handle.className = 'p-DockPanel-handle';
            return handle;
        };
        return Renderer;
    }());
    DockPanel.Renderer = Renderer;
    /**
     * The default `Renderer` instance.
     */
    DockPanel.defaultRenderer = new Renderer();
})(DockPanel = exports.DockPanel || (exports.DockPanel = {}));
exports.DockPanel = DockPanel;
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
     * The size of the edge dock zone for the root panel, in pixels.
     */
    Private.EDGE_SIZE = 40;
    /**
     * A singleton `'layout-modified'` conflatable message.
     */
    Private.LayoutModified = new messaging_1.ConflatableMessage('layout-modified');
    /**
     * An attached property used to track generated tab bars.
     */
    Private.isGeneratedTabBarProperty = new properties_1.AttachedProperty({
        name: 'isGeneratedTabBar',
        create: function () { return false; }
    });
    /**
     * Create a single document config for the widgets in a dock panel.
     */
    function createSingleDocumentConfig(panel) {
        // Return an empty config if the panel is empty.
        if (panel.isEmpty) {
            return { main: null };
        }
        // Get a flat array of the widgets in the panel.
        var widgets = algorithm_1.toArray(panel.widgets());
        // Get the first selected widget in the panel.
        var selected = panel.selectedWidgets().next();
        // Compute the current index for the new config.
        var currentIndex = selected ? widgets.indexOf(selected) : -1;
        // Return the single document config.
        return { main: { type: 'tab-area', widgets: widgets, currentIndex: currentIndex } };
    }
    Private.createSingleDocumentConfig = createSingleDocumentConfig;
    /**
     * Find the drop target at the given client position.
     */
    function findDropTarget(panel, clientX, clientY) {
        // Bail if the mouse is not over the dock panel.
        if (!domutils_1.ElementExt.hitTest(panel.node, clientX, clientY)) {
            return { zone: 'invalid', target: null };
        }
        // Look up the layout for the panel.
        var layout = panel.layout;
        // If the layout is empty, indicate the entire root drop zone.
        if (layout.isEmpty) {
            return { zone: 'root-all', target: null };
        }
        // Test the edge zones when in multiple document mode.
        if (panel.mode === 'multiple-document') {
            // Get the client rect for the dock panel.
            var panelRect = panel.node.getBoundingClientRect();
            // Compute the distance to each edge of the panel.
            var pl = clientX - panelRect.left + 1;
            var pt = clientY - panelRect.top + 1;
            var pr = panelRect.right - clientX;
            var pb = panelRect.bottom - clientY;
            // Find the minimum distance to an edge.
            var pd = Math.min(pl, pt, pr, pb);
            // Return a root zone if the mouse is within an edge.
            if (pd <= Private.EDGE_SIZE) {
                var zone_1;
                switch (pd) {
                    case pl:
                        zone_1 = 'root-left';
                        break;
                    case pt:
                        zone_1 = 'root-top';
                        break;
                    case pr:
                        zone_1 = 'root-right';
                        break;
                    case pb:
                        zone_1 = 'root-bottom';
                        break;
                    default:
                        throw 'unreachable';
                }
                return { zone: zone_1, target: null };
            }
        }
        // Hit test the dock layout at the given client position.
        var target = layout.hitTestTabAreas(clientX, clientY);
        // Bail if no target area was found.
        if (!target) {
            return { zone: 'invalid', target: null };
        }
        // Return the whole tab area when in single document mode.
        if (panel.mode === 'single-document') {
            return { zone: 'widget-all', target: target };
        }
        // Compute the distance to each edge of the tab area.
        var al = target.x - target.left + 1;
        var at = target.y - target.top + 1;
        var ar = target.left + target.width - target.x;
        var ab = target.top + target.height - target.y;
        // Get the X and Y edge sizes for the area.
        var rx = Math.round(target.width / 3);
        var ry = Math.round(target.height / 3);
        // If the mouse is not within an edge, indicate the entire area.
        if (al > rx && ar > rx && at > ry && ab > ry) {
            return { zone: 'widget-all', target: target };
        }
        // Scale the distances by the slenderness ratio.
        al /= rx;
        at /= ry;
        ar /= rx;
        ab /= ry;
        // Find the minimum distance to the area edge.
        var ad = Math.min(al, at, ar, ab);
        // Find the widget zone for the area edge.
        var zone;
        switch (ad) {
            case al:
                zone = 'widget-left';
                break;
            case at:
                zone = 'widget-top';
                break;
            case ar:
                zone = 'widget-right';
                break;
            case ab:
                zone = 'widget-bottom';
                break;
            default:
                throw 'unreachable';
        }
        // Return the final drop target.
        return { zone: zone, target: target };
    }
    Private.findDropTarget = findDropTarget;
    /**
     * Get the drop reference widget for a tab bar.
     */
    function getDropRef(tabBar) {
        if (tabBar.titles.length === 0) {
            return null;
        }
        if (tabBar.currentTitle) {
            return tabBar.currentTitle.owner;
        }
        return tabBar.titles[tabBar.titles.length - 1].owner;
    }
    Private.getDropRef = getDropRef;
})(Private || (Private = {}));
