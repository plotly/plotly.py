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
var dragdrop_1 = require("@phosphor/dragdrop");
var messaging_1 = require("@phosphor/messaging");
var signaling_1 = require("@phosphor/signaling");
var virtualdom_1 = require("@phosphor/virtualdom");
var title_1 = require("./title");
var widget_1 = require("./widget");
/**
 * A widget which displays titles as a single row or column of tabs.
 *
 * #### Notes
 * If CSS transforms are used to rotate nodes for vertically oriented
 * text, then tab dragging will not work correctly. The `tabsMovable`
 * property should be set to `false` when rotating nodes from CSS.
 */
var TabBar = (function (_super) {
    __extends(TabBar, _super);
    /**
     * Construct a new tab bar.
     *
     * @param options - The options for initializing the tab bar.
     */
    function TabBar(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, { node: Private.createNode() }) || this;
        _this._currentIndex = -1;
        _this._titles = [];
        _this._previousTitle = null;
        _this._dragData = null;
        _this._tabMoved = new signaling_1.Signal(_this);
        _this._currentChanged = new signaling_1.Signal(_this);
        _this._tabCloseRequested = new signaling_1.Signal(_this);
        _this._tabDetachRequested = new signaling_1.Signal(_this);
        _this._tabActivateRequested = new signaling_1.Signal(_this);
        _this.addClass('p-TabBar');
        _this.setFlag(widget_1.Widget.Flag.DisallowLayout);
        _this.tabsMovable = options.tabsMovable || false;
        _this.allowDeselect = options.allowDeselect || false;
        _this.insertBehavior = options.insertBehavior || 'select-tab-if-needed';
        _this.removeBehavior = options.removeBehavior || 'select-tab-after';
        _this.renderer = options.renderer || TabBar.defaultRenderer;
        _this._orientation = options.orientation || 'horizontal';
        _this.dataset['orientation'] = _this._orientation;
        return _this;
    }
    /**
     * Dispose of the resources held by the widget.
     */
    TabBar.prototype.dispose = function () {
        this._releaseMouse();
        this._titles.length = 0;
        this._previousTitle = null;
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(TabBar.prototype, "currentChanged", {
        /**
         * A signal emitted when the current tab is changed.
         *
         * #### Notes
         * This signal is emitted when the currently selected tab is changed
         * either through user or programmatic interaction.
         *
         * Notably, this signal is not emitted when the index of the current
         * tab changes due to tabs being inserted, removed, or moved. It is
         * only emitted when the actual current tab node is changed.
         */
        get: function () {
            return this._currentChanged;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "tabMoved", {
        /**
         * A signal emitted when a tab is moved by the user.
         *
         * #### Notes
         * This signal is emitted when a tab is moved by user interaction.
         *
         * This signal is not emitted when a tab is moved programmatically.
         */
        get: function () {
            return this._tabMoved;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "tabActivateRequested", {
        /**
         * A signal emitted when a tab is clicked by the user.
         *
         * #### Notes
         * If the clicked tab is not the current tab, the clicked tab will be
         * made current and the `currentChanged` signal will be emitted first.
         *
         * This signal is emitted even if the clicked tab is the current tab.
         */
        get: function () {
            return this._tabActivateRequested;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "tabCloseRequested", {
        /**
         * A signal emitted when a tab close icon is clicked.
         *
         * #### Notes
         * This signal is not emitted unless the tab title is `closable`.
         */
        get: function () {
            return this._tabCloseRequested;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "tabDetachRequested", {
        /**
         * A signal emitted when a tab is dragged beyond the detach threshold.
         *
         * #### Notes
         * This signal is emitted when the user drags a tab with the mouse,
         * and mouse is dragged beyond the detach threshold.
         *
         * The consumer of the signal should call `releaseMouse` and remove
         * the tab in order to complete the detach.
         *
         * This signal is only emitted once per drag cycle.
         */
        get: function () {
            return this._tabDetachRequested;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "currentTitle", {
        /**
         * Get the currently selected title.
         *
         * #### Notes
         * This will be `null` if no tab is selected.
         */
        get: function () {
            return this._titles[this._currentIndex] || null;
        },
        /**
         * Set the currently selected title.
         *
         * #### Notes
         * If the title does not exist, the title will be set to `null`.
         */
        set: function (value) {
            this.currentIndex = value ? this._titles.indexOf(value) : -1;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "currentIndex", {
        /**
         * Get the index of the currently selected tab.
         *
         * #### Notes
         * This will be `-1` if no tab is selected.
         */
        get: function () {
            return this._currentIndex;
        },
        /**
         * Set the index of the currently selected tab.
         *
         * #### Notes
         * If the value is out of range, the index will be set to `-1`.
         */
        set: function (value) {
            // Adjust for an out of range index.
            if (value < 0 || value >= this._titles.length) {
                value = -1;
            }
            // Bail early if the index will not change.
            if (this._currentIndex === value) {
                return;
            }
            // Look up the previous index and title.
            var pi = this._currentIndex;
            var pt = this._titles[pi] || null;
            // Look up the current index and title.
            var ci = value;
            var ct = this._titles[ci] || null;
            // Update the current index and previous title.
            this._currentIndex = ci;
            this._previousTitle = pt;
            // Schedule an update of the tabs.
            this.update();
            // Emit the current changed signal.
            this._currentChanged.emit({
                previousIndex: pi, previousTitle: pt,
                currentIndex: ci, currentTitle: ct
            });
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "orientation", {
        /**
         * Get the orientation of the tab bar.
         *
         * #### Notes
         * This controls whether the tabs are arranged in a row or column.
         */
        get: function () {
            return this._orientation;
        },
        /**
         * Set the orientation of the tab bar.
         *
         * #### Notes
         * This controls whether the tabs are arranged in a row or column.
         */
        set: function (value) {
            // Do nothing if the orientation does not change.
            if (this._orientation === value) {
                return;
            }
            // Release the mouse before making any changes.
            this._releaseMouse();
            // Toggle the orientation values.
            this._orientation = value;
            this.dataset['orientation'] = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "titles", {
        /**
         * A read-only array of the titles in the tab bar.
         */
        get: function () {
            return this._titles;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabBar.prototype, "contentNode", {
        /**
         * The tab bar content node.
         *
         * #### Notes
         * This is the node which holds the tab nodes.
         *
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-TabBar-content')[0];
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Add a tab to the end of the tab bar.
     *
     * @param value - The title which holds the data for the tab,
     *   or an options object to convert to a title.
     *
     * @returns The title object added to the tab bar.
     *
     * #### Notes
     * If the title is already added to the tab bar, it will be moved.
     */
    TabBar.prototype.addTab = function (value) {
        return this.insertTab(this._titles.length, value);
    };
    /**
     * Insert a tab into the tab bar at the specified index.
     *
     * @param index - The index at which to insert the tab.
     *
     * @param value - The title which holds the data for the tab,
     *   or an options object to convert to a title.
     *
     * @returns The title object added to the tab bar.
     *
     * #### Notes
     * The index will be clamped to the bounds of the tabs.
     *
     * If the title is already added to the tab bar, it will be moved.
     */
    TabBar.prototype.insertTab = function (index, value) {
        // Release the mouse before making any changes.
        this._releaseMouse();
        // Coerce the value to a title.
        var title = Private.asTitle(value);
        // Look up the index of the title.
        var i = this._titles.indexOf(title);
        // Clamp the insert index to the array bounds.
        var j = Math.max(0, Math.min(index, this._titles.length));
        // If the title is not in the array, insert it.
        if (i === -1) {
            // Insert the title into the array.
            algorithm_1.ArrayExt.insert(this._titles, j, title);
            // Connect to the title changed signal.
            title.changed.connect(this._onTitleChanged, this);
            // Schedule an update of the tabs.
            this.update();
            // Adjust the current index for the insert.
            this._adjustCurrentForInsert(j, title);
            // Return the title added to the tab bar.
            return title;
        }
        // Otherwise, the title exists in the array and should be moved.
        // Adjust the index if the location is at the end of the array.
        if (j === this._titles.length) {
            j--;
        }
        // Bail if there is no effective move.
        if (i === j) {
            return title;
        }
        // Move the title to the new location.
        algorithm_1.ArrayExt.move(this._titles, i, j);
        // Schedule an update of the tabs.
        this.update();
        // Adjust the current index for the move.
        this._adjustCurrentForMove(i, j);
        // Return the title added to the tab bar.
        return title;
    };
    /**
     * Remove a tab from the tab bar.
     *
     * @param title - The title for the tab to remove.
     *
     * #### Notes
     * This is a no-op if the title is not in the tab bar.
     */
    TabBar.prototype.removeTab = function (title) {
        this.removeTabAt(this._titles.indexOf(title));
    };
    /**
     * Remove the tab at a given index from the tab bar.
     *
     * @param index - The index of the tab to remove.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    TabBar.prototype.removeTabAt = function (index) {
        // Release the mouse before making any changes.
        this._releaseMouse();
        // Remove the title from the array.
        var title = algorithm_1.ArrayExt.removeAt(this._titles, index);
        // Bail if the index is out of range.
        if (!title) {
            return;
        }
        // Disconnect from the title changed signal.
        title.changed.disconnect(this._onTitleChanged, this);
        // Clear the previous title if it's being removed.
        if (title === this._previousTitle) {
            this._previousTitle = null;
        }
        // Schedule an update of the tabs.
        this.update();
        // Adjust the current index for the remove.
        this._adjustCurrentForRemove(index, title);
    };
    /**
     * Remove all tabs from the tab bar.
     */
    TabBar.prototype.clearTabs = function () {
        // Bail if there is nothing to remove.
        if (this._titles.length === 0) {
            return;
        }
        // Release the mouse before making any changes.
        this._releaseMouse();
        // Disconnect from the title changed signals.
        for (var _i = 0, _a = this._titles; _i < _a.length; _i++) {
            var title = _a[_i];
            title.changed.disconnect(this._onTitleChanged, this);
        }
        // Get the current index and title.
        var pi = this.currentIndex;
        var pt = this.currentTitle;
        // Reset the current index and previous title.
        this._currentIndex = -1;
        this._previousTitle = null;
        // Clear the title array.
        this._titles.length = 0;
        // Schedule an update of the tabs.
        this.update();
        // If no tab was selected, there's nothing else to do.
        if (pi === -1) {
            return;
        }
        // Emit the current changed signal.
        this._currentChanged.emit({
            previousIndex: pi, previousTitle: pt,
            currentIndex: -1, currentTitle: null
        });
    };
    /**
     * Release the mouse and restore the non-dragged tab positions.
     *
     * #### Notes
     * This will cause the tab bar to stop handling mouse events and to
     * restore the tabs to their non-dragged positions.
     */
    TabBar.prototype.releaseMouse = function () {
        this._releaseMouse();
    };
    /**
     * Handle the DOM events for the tab bar.
     *
     * @param event - The DOM event sent to the tab bar.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the tab bar's DOM node.
     *
     * This should not be called directly by user code.
     */
    TabBar.prototype.handleEvent = function (event) {
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
    TabBar.prototype.onBeforeAttach = function (msg) {
        this.node.addEventListener('mousedown', this);
    };
    /**
     * A message handler invoked on an `'after-detach'` message.
     */
    TabBar.prototype.onAfterDetach = function (msg) {
        this.node.removeEventListener('mousedown', this);
        this._releaseMouse();
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    TabBar.prototype.onUpdateRequest = function (msg) {
        var titles = this._titles;
        var renderer = this.renderer;
        var currentTitle = this.currentTitle;
        var content = new Array(titles.length);
        for (var i = 0, n = titles.length; i < n; ++i) {
            var title = titles[i];
            var current = title === currentTitle;
            var zIndex = current ? n : n - i - 1;
            content[i] = renderer.renderTab({ title: title, current: current, zIndex: zIndex });
        }
        virtualdom_1.VirtualDOM.render(content, this.contentNode);
    };
    /**
     * Handle the `'keydown'` event for the tab bar.
     */
    TabBar.prototype._evtKeyDown = function (event) {
        // Stop all input events during drag.
        event.preventDefault();
        event.stopPropagation();
        // Release the mouse if `Escape` is pressed.
        if (event.keyCode === 27) {
            this._releaseMouse();
        }
    };
    /**
     * Handle the `'mousedown'` event for the tab bar.
     */
    TabBar.prototype._evtMouseDown = function (event) {
        // Do nothing if it's not a left or middle mouse press.
        if (event.button !== 0 && event.button !== 1) {
            return;
        }
        // Do nothing if a drag is in progress.
        if (this._dragData) {
            return;
        }
        // Lookup the tab nodes.
        var tabs = this.contentNode.children;
        // Find the index of the pressed tab.
        var index = algorithm_1.ArrayExt.findFirstIndex(tabs, function (tab) {
            return domutils_1.ElementExt.hitTest(tab, event.clientX, event.clientY);
        });
        // Do nothing if the press is not on a tab.
        if (index === -1) {
            return;
        }
        // Pressing on a tab stops the event propagation.
        event.preventDefault();
        event.stopPropagation();
        // Initialize the non-measured parts of the drag data.
        this._dragData = {
            tab: tabs[index],
            index: index,
            pressX: event.clientX,
            pressY: event.clientY,
            tabPos: -1,
            tabSize: -1,
            tabPressPos: -1,
            targetIndex: -1,
            tabLayout: null,
            contentRect: null,
            override: null,
            dragActive: false,
            dragAborted: false,
            detachRequested: false
        };
        // Add the document mouse up listener.
        document.addEventListener('mouseup', this, true);
        // Do nothing else if the middle button is clicked.
        if (event.button === 1) {
            return;
        }
        // Do nothing else if the close icon is clicked.
        var icon = tabs[index].querySelector(this.renderer.closeIconSelector);
        if (icon && icon.contains(event.target)) {
            return;
        }
        // Add the extra listeners if the tabs are movable.
        if (this.tabsMovable) {
            document.addEventListener('mousemove', this, true);
            document.addEventListener('keydown', this, true);
            document.addEventListener('contextmenu', this, true);
        }
        // Update the current index as appropriate.
        if (this.allowDeselect && this.currentIndex === index) {
            this.currentIndex = -1;
        }
        else {
            this.currentIndex = index;
        }
        // Do nothing else if there is no current tab.
        if (this.currentIndex === -1) {
            return;
        }
        // Emit the tab activate request signal.
        this._tabActivateRequested.emit({
            index: this.currentIndex, title: this.currentTitle
        });
    };
    /**
     * Handle the `'mousemove'` event for the tab bar.
     */
    TabBar.prototype._evtMouseMove = function (event) {
        // Do nothing if no drag is in progress.
        var data = this._dragData;
        if (!data) {
            return;
        }
        // Suppress the event during a drag.
        event.preventDefault();
        event.stopPropagation();
        // Lookup the tab nodes.
        var tabs = this.contentNode.children;
        // Bail early if the drag threshold has not been met.
        if (!data.dragActive && !Private.dragExceeded(data, event)) {
            return;
        }
        // Activate the drag if necessary.
        if (!data.dragActive) {
            // Fill in the rest of the drag data measurements.
            var tabRect = data.tab.getBoundingClientRect();
            if (this._orientation === 'horizontal') {
                data.tabPos = data.tab.offsetLeft;
                data.tabSize = tabRect.width;
                data.tabPressPos = data.pressX - tabRect.left;
            }
            else {
                data.tabPos = data.tab.offsetTop;
                data.tabSize = tabRect.height;
                data.tabPressPos = data.pressY - tabRect.top;
            }
            data.tabLayout = Private.snapTabLayout(tabs, this._orientation);
            data.contentRect = this.contentNode.getBoundingClientRect();
            data.override = dragdrop_1.Drag.overrideCursor('default');
            // Add the dragging style classes.
            data.tab.classList.add('p-mod-dragging');
            this.addClass('p-mod-dragging');
            // Mark the drag as active.
            data.dragActive = true;
        }
        // Emit the detach requested signal if the threshold is exceeded.
        if (!data.detachRequested && Private.detachExceeded(data, event)) {
            // Only emit the signal once per drag cycle.
            data.detachRequested = true;
            // Setup the arguments for the signal.
            var index = data.index;
            var clientX = event.clientX;
            var clientY = event.clientY;
            var tab = tabs[index];
            var title = this._titles[index];
            // Emit the tab detach requested signal.
            this._tabDetachRequested.emit({ index: index, title: title, tab: tab, clientX: clientX, clientY: clientY });
            // Bail if the signal handler aborted the drag.
            if (data.dragAborted) {
                return;
            }
        }
        // Update the positions of the tabs.
        Private.layoutTabs(tabs, data, event, this._orientation);
    };
    /**
     * Handle the `'mouseup'` event for the document.
     */
    TabBar.prototype._evtMouseUp = function (event) {
        var _this = this;
        // Do nothing if it's not a left or middle mouse release.
        if (event.button !== 0 && event.button !== 1) {
            return;
        }
        // Do nothing if no drag is in progress.
        var data = this._dragData;
        if (!data) {
            return;
        }
        // Stop the event propagation.
        event.preventDefault();
        event.stopPropagation();
        // Remove the extra mouse event listeners.
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('mouseup', this, true);
        document.removeEventListener('keydown', this, true);
        document.removeEventListener('contextmenu', this, true);
        // Handle a release when the drag is not active.
        if (!data.dragActive) {
            // Clear the drag data.
            this._dragData = null;
            // Lookup the tab nodes.
            var tabs = this.contentNode.children;
            // Find the index of the released tab.
            var index = algorithm_1.ArrayExt.findFirstIndex(tabs, function (tab) {
                return domutils_1.ElementExt.hitTest(tab, event.clientX, event.clientY);
            });
            // Do nothing if the release is not on the original pressed tab.
            if (index !== data.index) {
                return;
            }
            // Ignore the release if the title is not closable.
            var title = this._titles[index];
            if (!title.closable) {
                return;
            }
            // Emit the close requested signal if the middle button is released.
            if (event.button === 1) {
                this._tabCloseRequested.emit({ index: index, title: title });
                return;
            }
            // Emit the close requested signal if the close icon was released.
            var icon = tabs[index].querySelector(this.renderer.closeIconSelector);
            if (icon && icon.contains(event.target)) {
                this._tabCloseRequested.emit({ index: index, title: title });
                return;
            }
            // Otherwise, there is nothing left to do.
            return;
        }
        // Do nothing if the left button is not released.
        if (event.button !== 0) {
            return;
        }
        // Position the tab at its final resting position.
        Private.finalizeTabPosition(data, this._orientation);
        // Remove the dragging class from the tab so it can be transitioned.
        data.tab.classList.remove('p-mod-dragging');
        // Parse the transition duration for releasing the tab.
        var duration = Private.parseTransitionDuration(data.tab);
        // Complete the release on a timer to allow the tab to transition.
        setTimeout(function () {
            // Do nothing if the drag has been aborted.
            if (data.dragAborted) {
                return;
            }
            // Clear the drag data reference.
            _this._dragData = null;
            // Reset the positions of the tabs.
            Private.resetTabPositions(_this.contentNode.children, _this._orientation);
            // Clear the cursor grab.
            data.override.dispose();
            // Remove the remaining dragging style.
            _this.removeClass('p-mod-dragging');
            // If the tab was not moved, there is nothing else to do.
            var i = data.index;
            var j = data.targetIndex;
            if (j === -1 || i === j) {
                return;
            }
            // Move the title to the new locations.
            algorithm_1.ArrayExt.move(_this._titles, i, j);
            // Adjust the current index for the move.
            _this._adjustCurrentForMove(i, j);
            // Emit the tab moved signal.
            _this._tabMoved.emit({
                fromIndex: i, toIndex: j, title: _this._titles[j]
            });
            // Update the tabs immediately to prevent flicker.
            messaging_1.MessageLoop.sendMessage(_this, widget_1.Widget.Msg.UpdateRequest);
        }, duration);
    };
    /**
     * Release the mouse and restore the non-dragged tab positions.
     */
    TabBar.prototype._releaseMouse = function () {
        // Do nothing if no drag is in progress.
        var data = this._dragData;
        if (!data) {
            return;
        }
        // Clear the drag data reference.
        this._dragData = null;
        // Remove the extra mouse listeners.
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('mouseup', this, true);
        document.removeEventListener('keydown', this, true);
        document.removeEventListener('contextmenu', this, true);
        // Indicate the drag has been aborted. This allows the mouse
        // event handlers to return early when the drag is canceled.
        data.dragAborted = true;
        // If the drag is not active, there's nothing more to do.
        if (!data.dragActive) {
            return;
        }
        // Reset the tabs to their non-dragged positions.
        Private.resetTabPositions(this.contentNode.children, this._orientation);
        // Clear the cursor override.
        data.override.dispose();
        // Clear the dragging style classes.
        data.tab.classList.remove('p-mod-dragging');
        this.removeClass('p-mod-dragging');
    };
    /**
     * Adjust the current index for a tab insert operation.
     *
     * This method accounts for the tab bar's insertion behavior when
     * adjusting the current index and emitting the changed signal.
     */
    TabBar.prototype._adjustCurrentForInsert = function (i, title) {
        // Lookup commonly used variables.
        var ct = this.currentTitle;
        var ci = this._currentIndex;
        var bh = this.insertBehavior;
        // Handle the behavior where the new tab is always selected,
        // or the behavior where the new tab is selected if needed.
        if (bh === 'select-tab' || (bh === 'select-tab-if-needed' && ci === -1)) {
            this._currentIndex = i;
            this._previousTitle = ct;
            this._currentChanged.emit({
                previousIndex: ci, previousTitle: ct,
                currentIndex: i, currentTitle: title
            });
            return;
        }
        // Otherwise, silently adjust the current index if needed.
        if (ci >= i) {
            this._currentIndex++;
        }
    };
    /**
     * Adjust the current index for a tab move operation.
     *
     * This method will not cause the actual current tab to change.
     * It silently adjusts the index to account for the given move.
     */
    TabBar.prototype._adjustCurrentForMove = function (i, j) {
        if (this._currentIndex === i) {
            this._currentIndex = j;
        }
        else if (this._currentIndex < i && this._currentIndex >= j) {
            this._currentIndex++;
        }
        else if (this._currentIndex > i && this._currentIndex <= j) {
            this._currentIndex--;
        }
    };
    /**
     * Adjust the current index for a tab remove operation.
     *
     * This method accounts for the tab bar's remove behavior when
     * adjusting the current index and emitting the changed signal.
     */
    TabBar.prototype._adjustCurrentForRemove = function (i, title) {
        // Lookup commonly used variables.
        var ci = this._currentIndex;
        var bh = this.removeBehavior;
        // Silently adjust the index if the current tab is not removed.
        if (ci !== i) {
            if (ci > i) {
                this._currentIndex--;
            }
            return;
        }
        // No tab gets selected if the tab bar is empty.
        if (this._titles.length === 0) {
            this._currentIndex = -1;
            this._currentChanged.emit({
                previousIndex: i, previousTitle: title,
                currentIndex: -1, currentTitle: null
            });
            return;
        }
        // Handle behavior where the next sibling tab is selected.
        if (bh === 'select-tab-after') {
            this._currentIndex = Math.min(i, this._titles.length - 1);
            this._currentChanged.emit({
                previousIndex: i, previousTitle: title,
                currentIndex: this._currentIndex, currentTitle: this.currentTitle
            });
            return;
        }
        // Handle behavior where the previous sibling tab is selected.
        if (bh === 'select-tab-before') {
            this._currentIndex = Math.max(0, i - 1);
            this._currentChanged.emit({
                previousIndex: i, previousTitle: title,
                currentIndex: this._currentIndex, currentTitle: this.currentTitle
            });
            return;
        }
        // Handle behavior where the previous history tab is selected.
        if (bh === 'select-previous-tab') {
            if (this._previousTitle) {
                this._currentIndex = this._titles.indexOf(this._previousTitle);
                this._previousTitle = null;
            }
            else {
                this._currentIndex = Math.min(i, this._titles.length - 1);
            }
            this._currentChanged.emit({
                previousIndex: i, previousTitle: title,
                currentIndex: this._currentIndex, currentTitle: this.currentTitle
            });
            return;
        }
        // Otherwise, no tab gets selected.
        this._currentIndex = -1;
        this._currentChanged.emit({
            previousIndex: i, previousTitle: title,
            currentIndex: -1, currentTitle: null
        });
    };
    /**
     * Handle the `changed` signal of a title object.
     */
    TabBar.prototype._onTitleChanged = function (sender) {
        this.update();
    };
    return TabBar;
}(widget_1.Widget));
exports.TabBar = TabBar;
/**
 * The namespace for the `TabBar` class statics.
 */
(function (TabBar) {
    /**
     * The default implementation of `IRenderer`.
     *
     * #### Notes
     * Subclasses are free to reimplement rendering methods as needed.
     */
    var Renderer = (function () {
        /**
         * Construct a new renderer.
         */
        function Renderer() {
            /**
             * A selector which matches the close icon node in a tab.
             */
            this.closeIconSelector = '.p-TabBar-tabCloseIcon';
            this._tabID = 0;
            this._tabKeys = new WeakMap();
        }
        /**
         * Render the virtual element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab.
         */
        Renderer.prototype.renderTab = function (data) {
            var title = data.title.caption;
            var key = this.createTabKey(data);
            var style = this.createTabStyle(data);
            var className = this.createTabClass(data);
            var dataset = this.createTabDataset(data);
            return (virtualdom_1.h.li({ key: key, className: className, title: title, style: style, dataset: dataset }, this.renderIcon(data), this.renderLabel(data), this.renderCloseIcon(data)));
        };
        /**
         * Render the icon element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab icon.
         */
        Renderer.prototype.renderIcon = function (data) {
            var className = this.createIconClass(data);
            return virtualdom_1.h.div({ className: className }, data.title.iconLabel);
        };
        /**
         * Render the label element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab label.
         */
        Renderer.prototype.renderLabel = function (data) {
            return virtualdom_1.h.div({ className: 'p-TabBar-tabLabel' }, data.title.label);
        };
        /**
         * Render the close icon element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab close icon.
         */
        Renderer.prototype.renderCloseIcon = function (data) {
            return virtualdom_1.h.div({ className: 'p-TabBar-tabCloseIcon' });
        };
        /**
         * Create a unique render key for the tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The unique render key for the tab.
         *
         * #### Notes
         * This method caches the key against the tab title the first time
         * the key is generated. This enables efficient rendering of moved
         * tabs and avoids subtle hover style artifacts.
         */
        Renderer.prototype.createTabKey = function (data) {
            var key = this._tabKeys.get(data.title);
            if (key === undefined) {
                key = "tab-key-" + this._tabID++;
                this._tabKeys.set(data.title, key);
            }
            return key;
        };
        /**
         * Create the inline style object for a tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The inline style data for the tab.
         */
        Renderer.prototype.createTabStyle = function (data) {
            return { zIndex: "" + data.zIndex };
        };
        /**
         * Create the class name for the tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The full class name for the tab.
         */
        Renderer.prototype.createTabClass = function (data) {
            var name = 'p-TabBar-tab';
            if (data.title.className) {
                name += " " + data.title.className;
            }
            if (data.title.closable) {
                name += ' p-mod-closable';
            }
            if (data.current) {
                name += ' p-mod-current';
            }
            return name;
        };
        /**
         * Create the dataset for a tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The dataset for the tab.
         */
        Renderer.prototype.createTabDataset = function (data) {
            return data.title.dataset;
        };
        /**
         * Create the class name for the tab icon.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The full class name for the tab icon.
         */
        Renderer.prototype.createIconClass = function (data) {
            var name = 'p-TabBar-tabIcon';
            var extra = data.title.iconClass;
            return extra ? name + " " + extra : name;
        };
        return Renderer;
    }());
    TabBar.Renderer = Renderer;
    /**
     * The default `Renderer` instance.
     */
    TabBar.defaultRenderer = new Renderer();
})(TabBar = exports.TabBar || (exports.TabBar = {}));
exports.TabBar = TabBar;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The start drag distance threshold.
     */
    Private.DRAG_THRESHOLD = 5;
    /**
     * The detach distance threshold.
     */
    Private.DETACH_THRESHOLD = 20;
    /**
     * Create the DOM node for a tab bar.
     */
    function createNode() {
        var node = document.createElement('div');
        var content = document.createElement('ul');
        content.className = 'p-TabBar-content';
        node.appendChild(content);
        return node;
    }
    Private.createNode = createNode;
    /**
     * Coerce a title or options into a real title.
     */
    function asTitle(value) {
        return value instanceof title_1.Title ? value : new title_1.Title(value);
    }
    Private.asTitle = asTitle;
    /**
     * Parse the transition duration for a tab node.
     */
    function parseTransitionDuration(tab) {
        var style = window.getComputedStyle(tab);
        return 1000 * (parseFloat(style.transitionDuration) || 0);
    }
    Private.parseTransitionDuration = parseTransitionDuration;
    /**
     * Get a snapshot of the current tab layout values.
     */
    function snapTabLayout(tabs, orientation) {
        var layout = new Array(tabs.length);
        for (var i = 0, n = tabs.length; i < n; ++i) {
            var node = tabs[i];
            var style = window.getComputedStyle(node);
            if (orientation === 'horizontal') {
                layout[i] = {
                    pos: node.offsetLeft,
                    size: node.offsetWidth,
                    margin: parseFloat(style.marginLeft) || 0
                };
            }
            else {
                layout[i] = {
                    pos: node.offsetTop,
                    size: node.offsetHeight,
                    margin: parseFloat(style.marginTop) || 0
                };
            }
        }
        return layout;
    }
    Private.snapTabLayout = snapTabLayout;
    /**
     * Test if the event exceeds the drag threshold.
     */
    function dragExceeded(data, event) {
        var dx = Math.abs(event.clientX - data.pressX);
        var dy = Math.abs(event.clientY - data.pressY);
        return dx >= Private.DRAG_THRESHOLD || dy >= Private.DRAG_THRESHOLD;
    }
    Private.dragExceeded = dragExceeded;
    /**
     * Test if the event exceeds the drag detach threshold.
     */
    function detachExceeded(data, event) {
        var rect = data.contentRect;
        return ((event.clientX < rect.left - Private.DETACH_THRESHOLD) ||
            (event.clientX >= rect.right + Private.DETACH_THRESHOLD) ||
            (event.clientY < rect.top - Private.DETACH_THRESHOLD) ||
            (event.clientY >= rect.bottom + Private.DETACH_THRESHOLD));
    }
    Private.detachExceeded = detachExceeded;
    /**
     * Update the relative tab positions and computed target index.
     */
    function layoutTabs(tabs, data, event, orientation) {
        // Compute the orientation-sensitive values.
        var pressPos;
        var localPos;
        var clientPos;
        var clientSize;
        if (orientation === 'horizontal') {
            pressPos = data.pressX;
            localPos = event.clientX - data.contentRect.left;
            clientPos = event.clientX;
            clientSize = data.contentRect.width;
        }
        else {
            pressPos = data.pressY;
            localPos = event.clientY - data.contentRect.top;
            clientPos = event.clientY;
            clientSize = data.contentRect.height;
        }
        // Compute the target data.
        var targetIndex = data.index;
        var targetPos = localPos - data.tabPressPos;
        var targetEnd = targetPos + data.tabSize;
        // Update the relative tab positions.
        for (var i = 0, n = tabs.length; i < n; ++i) {
            var pxPos = void 0;
            var layout = data.tabLayout[i];
            var threshold = layout.pos + (layout.size >> 1);
            if (i < data.index && targetPos < threshold) {
                pxPos = data.tabSize + data.tabLayout[i + 1].margin + "px";
                targetIndex = Math.min(targetIndex, i);
            }
            else if (i > data.index && targetEnd > threshold) {
                pxPos = -data.tabSize - layout.margin + "px";
                targetIndex = Math.max(targetIndex, i);
            }
            else if (i === data.index) {
                var ideal = clientPos - pressPos;
                var limit = clientSize - (data.tabPos + data.tabSize);
                pxPos = Math.max(-data.tabPos, Math.min(ideal, limit)) + "px";
            }
            else {
                pxPos = '';
            }
            if (orientation === 'horizontal') {
                tabs[i].style.left = pxPos;
            }
            else {
                tabs[i].style.top = pxPos;
            }
        }
        // Update the computed target index.
        data.targetIndex = targetIndex;
    }
    Private.layoutTabs = layoutTabs;
    /**
     * Position the drag tab at its final resting relative position.
     */
    function finalizeTabPosition(data, orientation) {
        // Compute the orientation-sensitive client size.
        var clientSize;
        if (orientation === 'horizontal') {
            clientSize = data.contentRect.width;
        }
        else {
            clientSize = data.contentRect.height;
        }
        // Compute the ideal final tab position.
        var ideal;
        if (data.targetIndex === data.index) {
            ideal = 0;
        }
        else if (data.targetIndex > data.index) {
            var tgt = data.tabLayout[data.targetIndex];
            ideal = tgt.pos + tgt.size - data.tabSize - data.tabPos;
        }
        else {
            var tgt = data.tabLayout[data.targetIndex];
            ideal = tgt.pos - data.tabPos;
        }
        // Compute the tab position limit.
        var limit = clientSize - (data.tabPos + data.tabSize);
        var final = Math.max(-data.tabPos, Math.min(ideal, limit));
        // Set the final orientation-sensitive position.
        if (orientation === 'horizontal') {
            data.tab.style.left = final + "px";
        }
        else {
            data.tab.style.top = final + "px";
        }
    }
    Private.finalizeTabPosition = finalizeTabPosition;
    /**
     * Reset the relative positions of the given tabs.
     */
    function resetTabPositions(tabs, orientation) {
        algorithm_1.each(tabs, function (tab) {
            if (orientation === 'horizontal') {
                tab.style.left = '';
            }
            else {
                tab.style.top = '';
            }
        });
    }
    Private.resetTabPositions = resetTabPositions;
})(Private || (Private = {}));
