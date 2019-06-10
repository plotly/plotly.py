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
var __assign = (this && this.__assign) || Object.assign || function(t) {
    for (var s, i = 1, n = arguments.length; i < n; i++) {
        s = arguments[i];
        for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
            t[p] = s[p];
    }
    return t;
};
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var algorithm_1 = require("@phosphor/algorithm");
var commands_1 = require("@phosphor/commands");
var coreutils_1 = require("@phosphor/coreutils");
var domutils_1 = require("@phosphor/domutils");
var keyboard_1 = require("@phosphor/keyboard");
var messaging_1 = require("@phosphor/messaging");
var signaling_1 = require("@phosphor/signaling");
var virtualdom_1 = require("@phosphor/virtualdom");
var widget_1 = require("./widget");
/**
 * A widget which displays items as a canonical menu.
 */
var Menu = (function (_super) {
    __extends(Menu, _super);
    /**
     * Construct a new menu.
     *
     * @param options - The options for initializing the menu.
     */
    function Menu(options) {
        var _this = _super.call(this, { node: Private.createNode() }) || this;
        _this._childIndex = -1;
        _this._activeIndex = -1;
        _this._openTimerID = 0;
        _this._closeTimerID = 0;
        _this._items = [];
        _this._childMenu = null;
        _this._parentMenu = null;
        _this._aboutToClose = new signaling_1.Signal(_this);
        _this._menuRequested = new signaling_1.Signal(_this);
        _this.addClass('p-Menu');
        _this.setFlag(widget_1.Widget.Flag.DisallowLayout);
        _this.commands = options.commands;
        _this.renderer = options.renderer || Menu.defaultRenderer;
        return _this;
    }
    /**
     * Dispose of the resources held by the menu.
     */
    Menu.prototype.dispose = function () {
        this.close();
        this._items.length = 0;
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(Menu.prototype, "aboutToClose", {
        /**
         * A signal emitted just before the menu is closed.
         *
         * #### Notes
         * This signal is emitted when the menu receives a `'close-request'`
         * message, just before it removes itself from the DOM.
         *
         * This signal is not emitted if the menu is already detached from
         * the DOM when it receives the `'close-request'` message.
         */
        get: function () {
            return this._aboutToClose;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "menuRequested", {
        /**
         * A signal emitted when a new menu is requested by the user.
         *
         * #### Notes
         * This signal is emitted whenever the user presses the right or left
         * arrow keys, and a submenu cannot be opened or closed in response.
         *
         * This signal is useful when implementing menu bars in order to open
         * the next or previous menu in response to a user key press.
         *
         * This signal is only emitted for the root menu in a hierarchy.
         */
        get: function () {
            return this._menuRequested;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "parentMenu", {
        /**
         * The parent menu of the menu.
         *
         * #### Notes
         * This is `null` unless the menu is an open submenu.
         */
        get: function () {
            return this._parentMenu;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "childMenu", {
        /**
         * The child menu of the menu.
         *
         * #### Notes
         * This is `null` unless the menu has an open submenu.
         */
        get: function () {
            return this._childMenu;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "rootMenu", {
        /**
         * The root menu of the menu hierarchy.
         */
        get: function () {
            var menu = this;
            while (menu._parentMenu) {
                menu = menu._parentMenu;
            }
            return menu;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "leafMenu", {
        /**
         * The leaf menu of the menu hierarchy.
         */
        get: function () {
            var menu = this;
            while (menu._childMenu) {
                menu = menu._childMenu;
            }
            return menu;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "contentNode", {
        /**
         * The menu content node.
         *
         * #### Notes
         * This is the node which holds the menu item nodes.
         *
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-Menu-content')[0];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "activeItem", {
        /**
         * Get the currently active menu item.
         */
        get: function () {
            return this._items[this._activeIndex] || null;
        },
        /**
         * Set the currently active menu item.
         *
         * #### Notes
         * If the item cannot be activated, the item will be set to `null`.
         */
        set: function (value) {
            this.activeIndex = value ? this._items.indexOf(value) : -1;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "activeIndex", {
        /**
         * Get the index of the currently active menu item.
         *
         * #### Notes
         * This will be `-1` if no menu item is active.
         */
        get: function () {
            return this._activeIndex;
        },
        /**
         * Set the index of the currently active menu item.
         *
         * #### Notes
         * If the item cannot be activated, the index will be set to `-1`.
         */
        set: function (value) {
            // Adjust the value for an out of range index.
            if (value < 0 || value >= this._items.length) {
                value = -1;
            }
            // Ensure the item can be activated.
            if (value !== -1 && !Private.canActivate(this._items[value])) {
                value = -1;
            }
            // Bail if the index will not change.
            if (this._activeIndex === value) {
                return;
            }
            // Update the active index.
            this._activeIndex = value;
            // schedule an update of the items.
            this.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Menu.prototype, "items", {
        /**
         * A read-only array of the menu items in the menu.
         */
        get: function () {
            return this._items;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Activate the next selectable item in the menu.
     *
     * #### Notes
     * If no item is selectable, the index will be set to `-1`.
     */
    Menu.prototype.activateNextItem = function () {
        var n = this._items.length;
        var ai = this._activeIndex;
        var start = ai < n - 1 ? ai + 1 : 0;
        var stop = start === 0 ? n - 1 : start - 1;
        this.activeIndex = algorithm_1.ArrayExt.findFirstIndex(this._items, Private.canActivate, start, stop);
    };
    /**
     * Activate the previous selectable item in the menu.
     *
     * #### Notes
     * If no item is selectable, the index will be set to `-1`.
     */
    Menu.prototype.activatePreviousItem = function () {
        var n = this._items.length;
        var ai = this._activeIndex;
        var start = ai <= 0 ? n - 1 : ai - 1;
        var stop = start === n - 1 ? 0 : start + 1;
        this.activeIndex = algorithm_1.ArrayExt.findLastIndex(this._items, Private.canActivate, start, stop);
    };
    /**
     * Trigger the active menu item.
     *
     * #### Notes
     * If the active item is a submenu, it will be opened and the first
     * item will be activated.
     *
     * If the active item is a command, the command will be executed.
     *
     * If the menu is not attached, this is a no-op.
     *
     * If there is no active item, this is a no-op.
     */
    Menu.prototype.triggerActiveItem = function () {
        // Bail if the menu is not attached.
        if (!this.isAttached) {
            return;
        }
        // Bail if there is no active item.
        var item = this.activeItem;
        if (!item) {
            return;
        }
        // Cancel the pending timers.
        this._cancelOpenTimer();
        this._cancelCloseTimer();
        // If the item is a submenu, open it.
        if (item.type === 'submenu') {
            this._openChildMenu(true);
            return;
        }
        // Close the root menu before executing the command.
        this.rootMenu.close();
        // Execute the command for the item.
        var command = item.command, args = item.args;
        if (this.commands.isEnabled(command, args)) {
            this.commands.execute(command, args);
        }
        else {
            console.log("Command '" + command + "' is disabled.");
        }
    };
    /**
     * Add a menu item to the end of the menu.
     *
     * @param options - The options for creating the menu item.
     *
     * @returns The menu item added to the menu.
     */
    Menu.prototype.addItem = function (options) {
        return this.insertItem(this._items.length, options);
    };
    /**
     * Insert a menu item into the menu at the specified index.
     *
     * @param index - The index at which to insert the item.
     *
     * @param options - The options for creating the menu item.
     *
     * @returns The menu item added to the menu.
     *
     * #### Notes
     * The index will be clamped to the bounds of the items.
     */
    Menu.prototype.insertItem = function (index, options) {
        // Close the menu if it's attached.
        if (this.isAttached) {
            this.close();
        }
        // Reset the active index.
        this.activeIndex = -1;
        // Clamp the insert index to the array bounds.
        var i = Math.max(0, Math.min(index, this._items.length));
        // Create the item for the options.
        var item = Private.createItem(this, options);
        // Insert the item into the array.
        algorithm_1.ArrayExt.insert(this._items, i, item);
        // Schedule an update of the items.
        this.update();
        // Return the item added to the menu.
        return item;
    };
    /**
     * Remove an item from the menu.
     *
     * @param item - The item to remove from the menu.
     *
     * #### Notes
     * This is a no-op if the item is not in the menu.
     */
    Menu.prototype.removeItem = function (item) {
        this.removeItemAt(this._items.indexOf(item));
    };
    /**
     * Remove the item at a given index from the menu.
     *
     * @param index - The index of the item to remove.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    Menu.prototype.removeItemAt = function (index) {
        // Close the menu if it's attached.
        if (this.isAttached) {
            this.close();
        }
        // Reset the active index.
        this.activeIndex = -1;
        // Remove the item from the array.
        var item = algorithm_1.ArrayExt.removeAt(this._items, index);
        // Bail if the index is out of range.
        if (!item) {
            return;
        }
        // Schedule an update of the items.
        this.update();
    };
    /**
     * Remove all menu items from the menu.
     */
    Menu.prototype.clearItems = function () {
        // Close the menu if it's attached.
        if (this.isAttached) {
            this.close();
        }
        // Reset the active index.
        this.activeIndex = -1;
        // Bail if there is nothing to remove.
        if (this._items.length === 0) {
            return;
        }
        // Clear the items.
        this._items.length = 0;
        // Schedule an update of the items.
        this.update();
    };
    /**
     * Open the menu at the specified location.
     *
     * @param x - The client X coordinate of the menu location.
     *
     * @param y - The client Y coordinate of the menu location.
     *
     * @param options - The additional options for opening the menu.
     *
     * #### Notes
     * The menu will be opened at the given location unless it will not
     * fully fit on the screen. If it will not fit, it will be adjusted
     * to fit naturally on the screen.
     *
     * This is a no-op if the menu is already attached to the DOM.
     */
    Menu.prototype.open = function (x, y, options) {
        if (options === void 0) { options = {}; }
        // Bail early if the menu is already attached.
        if (this.isAttached) {
            return;
        }
        // Extract the position options.
        var forceX = options.forceX || false;
        var forceY = options.forceY || false;
        // Open the menu as a root menu.
        Private.openRootMenu(this, x, y, forceX, forceY);
        // Activate the menu to accept keyboard input.
        this.activate();
    };
    /**
     * Handle the DOM events for the menu.
     *
     * @param event - The DOM event sent to the menu.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the menu's DOM nodes. It should
     * not be called directly by user code.
     */
    Menu.prototype.handleEvent = function (event) {
        switch (event.type) {
            case 'keydown':
                this._evtKeyDown(event);
                break;
            case 'mouseup':
                this._evtMouseUp(event);
                break;
            case 'mousemove':
                this._evtMouseMove(event);
                break;
            case 'mouseenter':
                this._evtMouseEnter(event);
                break;
            case 'mouseleave':
                this._evtMouseLeave(event);
                break;
            case 'mousedown':
                this._evtMouseDown(event);
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
    Menu.prototype.onBeforeAttach = function (msg) {
        this.node.addEventListener('keydown', this);
        this.node.addEventListener('mouseup', this);
        this.node.addEventListener('mousemove', this);
        this.node.addEventListener('mouseenter', this);
        this.node.addEventListener('mouseleave', this);
        this.node.addEventListener('contextmenu', this);
        document.addEventListener('mousedown', this, true);
    };
    /**
     * A message handler invoked on an `'after-detach'` message.
     */
    Menu.prototype.onAfterDetach = function (msg) {
        this.node.removeEventListener('keydown', this);
        this.node.removeEventListener('mouseup', this);
        this.node.removeEventListener('mousemove', this);
        this.node.removeEventListener('mouseenter', this);
        this.node.removeEventListener('mouseleave', this);
        this.node.removeEventListener('contextmenu', this);
        document.removeEventListener('mousedown', this, true);
    };
    /**
     * A message handler invoked on an `'activate-request'` message.
     */
    Menu.prototype.onActivateRequest = function (msg) {
        if (this.isAttached) {
            this.node.focus();
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    Menu.prototype.onUpdateRequest = function (msg) {
        var items = this._items;
        var renderer = this.renderer;
        var activeIndex = this._activeIndex;
        var collapsedFlags = Private.computeCollapsed(items);
        var content = new Array(items.length);
        for (var i = 0, n = items.length; i < n; ++i) {
            var item = items[i];
            var active = i === activeIndex;
            var collapsed = collapsedFlags[i];
            content[i] = renderer.renderItem({ item: item, active: active, collapsed: collapsed });
        }
        virtualdom_1.VirtualDOM.render(content, this.contentNode);
    };
    /**
     * A message handler invoked on a `'close-request'` message.
     */
    Menu.prototype.onCloseRequest = function (msg) {
        // Cancel the pending timers.
        this._cancelOpenTimer();
        this._cancelCloseTimer();
        // Reset the active index.
        this.activeIndex = -1;
        // Close any open child menu.
        var childMenu = this._childMenu;
        if (childMenu) {
            this._childIndex = -1;
            this._childMenu = null;
            childMenu._parentMenu = null;
            childMenu.close();
        }
        // Remove this menu from its parent and activate the parent.
        var parentMenu = this._parentMenu;
        if (parentMenu) {
            this._parentMenu = null;
            parentMenu._childIndex = -1;
            parentMenu._childMenu = null;
            parentMenu.activate();
        }
        // Emit the `aboutToClose` signal if the menu is attached.
        if (this.isAttached) {
            this._aboutToClose.emit(undefined);
        }
        // Finish closing the menu.
        _super.prototype.onCloseRequest.call(this, msg);
    };
    /**
     * Handle the `'keydown'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    Menu.prototype._evtKeyDown = function (event) {
        // A menu handles all keydown events.
        event.preventDefault();
        event.stopPropagation();
        // Fetch the key code for the event.
        var kc = event.keyCode;
        // Enter
        if (kc === 13) {
            this.triggerActiveItem();
            return;
        }
        // Escape
        if (kc === 27) {
            this.close();
            return;
        }
        // Left Arrow
        if (kc === 37) {
            if (this._parentMenu) {
                this.close();
            }
            else {
                this._menuRequested.emit('previous');
            }
            return;
        }
        // Up Arrow
        if (kc === 38) {
            this.activatePreviousItem();
            return;
        }
        // Right Arrow
        if (kc === 39) {
            var item = this.activeItem;
            if (item && item.type === 'submenu') {
                this.triggerActiveItem();
            }
            else {
                this.rootMenu._menuRequested.emit('next');
            }
            return;
        }
        // Down Arrow
        if (kc === 40) {
            this.activateNextItem();
            return;
        }
        // Get the pressed key character.
        var key = keyboard_1.getKeyboardLayout().keyForKeydownEvent(event);
        // Bail if the key is not valid.
        if (!key) {
            return;
        }
        // Search for the next best matching mnemonic item.
        var start = this._activeIndex + 1;
        var result = Private.findMnemonic(this._items, key, start);
        // Handle the requested mnemonic based on the search results.
        // If exactly one mnemonic is matched, that item is triggered.
        // Otherwise, the next mnemonic is activated if available,
        // followed by the auto mnemonic if available.
        if (result.index !== -1 && !result.multiple) {
            this.activeIndex = result.index;
            this.triggerActiveItem();
        }
        else if (result.index !== -1) {
            this.activeIndex = result.index;
        }
        else if (result.auto !== -1) {
            this.activeIndex = result.auto;
        }
    };
    /**
     * Handle the `'mouseup'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    Menu.prototype._evtMouseUp = function (event) {
        if (event.button !== 0) {
            return;
        }
        event.preventDefault();
        event.stopPropagation();
        this.triggerActiveItem();
    };
    /**
     * Handle the `'mousemove'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    Menu.prototype._evtMouseMove = function (event) {
        // Hit test the item nodes for the item under the mouse.
        var index = algorithm_1.ArrayExt.findFirstIndex(this.contentNode.children, function (node) {
            return domutils_1.ElementExt.hitTest(node, event.clientX, event.clientY);
        });
        // Bail early if the mouse is already over the active index.
        if (index === this._activeIndex) {
            return;
        }
        // Update and coerce the active index.
        this.activeIndex = index;
        index = this.activeIndex;
        // If the index is the current child index, cancel the timers.
        if (index === this._childIndex) {
            this._cancelOpenTimer();
            this._cancelCloseTimer();
            return;
        }
        // If a child menu is currently open, start the close timer.
        if (this._childIndex !== -1) {
            this._startCloseTimer();
        }
        // Cancel the open timer to give a full delay for opening.
        this._cancelOpenTimer();
        // Bail if the active item is not a valid submenu item.
        var item = this.activeItem;
        if (!item || item.type !== 'submenu' || !item.submenu) {
            return;
        }
        // Start the open timer to open the active item submenu.
        this._startOpenTimer();
    };
    /**
     * Handle the `'mouseenter'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    Menu.prototype._evtMouseEnter = function (event) {
        // Synchronize the active ancestor items.
        for (var menu = this._parentMenu; menu; menu = menu._parentMenu) {
            menu._cancelOpenTimer();
            menu._cancelCloseTimer();
            menu.activeIndex = menu._childIndex;
        }
    };
    /**
     * Handle the `'mouseleave'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    Menu.prototype._evtMouseLeave = function (event) {
        // Cancel any pending submenu opening.
        this._cancelOpenTimer();
        // If there is no open child menu, just reset the active index.
        if (!this._childMenu) {
            this.activeIndex = -1;
            return;
        }
        // If the mouse is over the child menu, cancel the close timer.
        var clientX = event.clientX, clientY = event.clientY;
        if (domutils_1.ElementExt.hitTest(this._childMenu.node, clientX, clientY)) {
            this._cancelCloseTimer();
            return;
        }
        // Otherwise, reset the active index and start the close timer.
        this.activeIndex = -1;
        this._startCloseTimer();
    };
    /**
     * Handle the `'mousedown'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the document node.
     */
    Menu.prototype._evtMouseDown = function (event) {
        // Bail if the menu is not a root menu.
        if (this._parentMenu) {
            return;
        }
        // The mouse button which is pressed is irrelevant. If the press
        // is not on a menu, the entire hierarchy is closed and the event
        // is allowed to propagate. This allows other code to act on the
        // event, such as focusing the clicked element.
        if (Private.hitTestMenus(this, event.clientX, event.clientY)) {
            event.preventDefault();
            event.stopPropagation();
        }
        else {
            this.close();
        }
    };
    /**
     * Open the child menu at the active index immediately.
     *
     * If a different child menu is already open, it will be closed,
     * even if the active item is not a valid submenu.
     */
    Menu.prototype._openChildMenu = function (activateFirst) {
        if (activateFirst === void 0) { activateFirst = false; }
        // If the item is not a valid submenu, close the child menu.
        var item = this.activeItem;
        if (!item || item.type !== 'submenu' || !item.submenu) {
            this._closeChildMenu();
            return;
        }
        // Do nothing if the child menu will not change.
        var submenu = item.submenu;
        if (submenu === this._childMenu) {
            return;
        }
        // Ensure the current child menu is closed.
        this._closeChildMenu();
        // Update the private child state.
        this._childMenu = submenu;
        this._childIndex = this._activeIndex;
        // Set the parent menu reference for the child.
        submenu._parentMenu = this;
        // Ensure the menu is updated and lookup the item node.
        messaging_1.MessageLoop.sendMessage(this, widget_1.Widget.Msg.UpdateRequest);
        var itemNode = this.contentNode.children[this._activeIndex];
        // Open the submenu at the active node.
        Private.openSubmenu(submenu, itemNode);
        // Activate the first item if desired.
        if (activateFirst) {
            submenu.activeIndex = -1;
            submenu.activateNextItem();
        }
        // Activate the child menu.
        submenu.activate();
    };
    /**
     * Close the child menu immediately.
     *
     * This is a no-op if a child menu is not open.
     */
    Menu.prototype._closeChildMenu = function () {
        if (this._childMenu) {
            this._childMenu.close();
        }
    };
    /**
     * Start the open timer, unless it is already pending.
     */
    Menu.prototype._startOpenTimer = function () {
        var _this = this;
        if (this._openTimerID === 0) {
            this._openTimerID = setTimeout(function () {
                _this._openTimerID = 0;
                _this._openChildMenu();
            }, Private.TIMER_DELAY);
        }
    };
    /**
     * Start the close timer, unless it is already pending.
     */
    Menu.prototype._startCloseTimer = function () {
        var _this = this;
        if (this._closeTimerID === 0) {
            this._closeTimerID = setTimeout(function () {
                _this._closeTimerID = 0;
                _this._closeChildMenu();
            }, Private.TIMER_DELAY);
        }
    };
    /**
     * Cancel the open timer, if the timer is pending.
     */
    Menu.prototype._cancelOpenTimer = function () {
        if (this._openTimerID !== 0) {
            clearTimeout(this._openTimerID);
            this._openTimerID = 0;
        }
    };
    /**
     * Cancel the close timer, if the timer is pending.
     */
    Menu.prototype._cancelCloseTimer = function () {
        if (this._closeTimerID !== 0) {
            clearTimeout(this._closeTimerID);
            this._closeTimerID = 0;
        }
    };
    return Menu;
}(widget_1.Widget));
exports.Menu = Menu;
/**
 * The namespace for the `Menu` class statics.
 */
(function (Menu) {
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
        }
        /**
         * Render the virtual element for a menu item.
         *
         * @param data - The data to use for rendering the item.
         *
         * @returns A virtual element representing the item.
         */
        Renderer.prototype.renderItem = function (data) {
            var className = this.createItemClass(data);
            var dataset = this.createItemDataset(data);
            return (virtualdom_1.h.li({ className: className, dataset: dataset }, this.renderIcon(data), this.renderLabel(data), this.renderShortcut(data), this.renderSubmenu(data)));
        };
        /**
         * Render the icon element for a menu item.
         *
         * @param data - The data to use for rendering the icon.
         *
         * @returns A virtual element representing the item icon.
         */
        Renderer.prototype.renderIcon = function (data) {
            var className = this.createIconClass(data);
            return virtualdom_1.h.div({ className: className }, data.item.iconLabel);
        };
        /**
         * Render the label element for a menu item.
         *
         * @param data - The data to use for rendering the label.
         *
         * @returns A virtual element representing the item label.
         */
        Renderer.prototype.renderLabel = function (data) {
            var content = this.formatLabel(data);
            return virtualdom_1.h.div({ className: 'p-Menu-itemLabel' }, content);
        };
        /**
         * Render the shortcut element for a menu item.
         *
         * @param data - The data to use for rendering the shortcut.
         *
         * @returns A virtual element representing the item shortcut.
         */
        Renderer.prototype.renderShortcut = function (data) {
            var content = this.formatShortcut(data);
            return virtualdom_1.h.div({ className: 'p-Menu-itemShortcut' }, content);
        };
        /**
         * Render the submenu icon element for a menu item.
         *
         * @param data - The data to use for rendering the submenu icon.
         *
         * @returns A virtual element representing the submenu icon.
         */
        Renderer.prototype.renderSubmenu = function (data) {
            return virtualdom_1.h.div({ className: 'p-Menu-itemSubmenuIcon' });
        };
        /**
         * Create the class name for the menu item.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the menu item.
         */
        Renderer.prototype.createItemClass = function (data) {
            // Setup the initial class name.
            var name = 'p-Menu-item';
            // Add the boolean state classes.
            if (!data.item.isEnabled) {
                name += ' p-mod-disabled';
            }
            if (data.item.isToggled) {
                name += ' p-mod-toggled';
            }
            if (!data.item.isVisible) {
                name += ' p-mod-hidden';
            }
            if (data.active) {
                name += ' p-mod-active';
            }
            if (data.collapsed) {
                name += ' p-mod-collapsed';
            }
            // Add the extra class.
            var extra = data.item.className;
            if (extra) {
                name += " " + extra;
            }
            // Return the complete class name.
            return name;
        };
        /**
         * Create the dataset for the menu item.
         *
         * @param data - The data to use for creating the dataset.
         *
         * @returns The dataset for the menu item.
         */
        Renderer.prototype.createItemDataset = function (data) {
            var result;
            var _a = data.item, type = _a.type, command = _a.command, dataset = _a.dataset;
            if (type === 'command') {
                result = __assign({}, dataset, { type: type, command: command });
            }
            else {
                result = __assign({}, dataset, { type: type });
            }
            return result;
        };
        /**
         * Create the class name for the menu item icon.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the item icon.
         */
        Renderer.prototype.createIconClass = function (data) {
            var name = 'p-Menu-itemIcon';
            var extra = data.item.iconClass;
            return extra ? name + " " + extra : name;
        };
        /**
         * Create the render content for the label node.
         *
         * @param data - The data to use for the label content.
         *
         * @returns The content to add to the label node.
         */
        Renderer.prototype.formatLabel = function (data) {
            // Fetch the label text and mnemonic index.
            var _a = data.item, label = _a.label, mnemonic = _a.mnemonic;
            // If the index is out of range, do not modify the label.
            if (mnemonic < 0 || mnemonic >= label.length) {
                return label;
            }
            // Split the label into parts.
            var prefix = label.slice(0, mnemonic);
            var suffix = label.slice(mnemonic + 1);
            var char = label[mnemonic];
            // Wrap the mnemonic character in a span.
            var span = virtualdom_1.h.span({ className: 'p-Menu-itemMnemonic' }, char);
            // Return the content parts.
            return [prefix, span, suffix];
        };
        /**
         * Create the render content for the shortcut node.
         *
         * @param data - The data to use for the shortcut content.
         *
         * @returns The content to add to the shortcut node.
         */
        Renderer.prototype.formatShortcut = function (data) {
            var kb = data.item.keyBinding;
            return kb ? kb.keys.map(Private.formatKeystroke).join(', ') : null;
        };
        return Renderer;
    }());
    Menu.Renderer = Renderer;
    /**
     * The default `Renderer` instance.
     */
    Menu.defaultRenderer = new Renderer();
})(Menu = exports.Menu || (exports.Menu = {}));
exports.Menu = Menu;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The ms delay for opening and closing a submenu.
     */
    Private.TIMER_DELAY = 300;
    /**
     * The horizontal pixel overlap for an open submenu.
     */
    Private.SUBMENU_OVERLAP = 3;
    /**
     * Create the DOM node for a menu.
     */
    function createNode() {
        var node = document.createElement('div');
        var content = document.createElement('ul');
        content.className = 'p-Menu-content';
        node.appendChild(content);
        node.tabIndex = -1;
        return node;
    }
    Private.createNode = createNode;
    /**
     * Test whether a menu item can be activated.
     */
    function canActivate(item) {
        return item.type !== 'separator' && item.isEnabled && item.isVisible;
    }
    Private.canActivate = canActivate;
    /**
     * Create a new menu item for an owner menu.
     */
    function createItem(owner, options) {
        return new MenuItem(owner.commands, options);
    }
    Private.createItem = createItem;
    /**
     * Format a keystroke for display on the local system.
     */
    function formatKeystroke(keystroke) {
        var mods = '';
        var parts = commands_1.CommandRegistry.parseKeystroke(keystroke);
        if (domutils_1.Platform.IS_MAC) {
            if (parts.ctrl) {
                mods += '\u2303 ';
            }
            if (parts.alt) {
                mods += '\u2325 ';
            }
            if (parts.shift) {
                mods += '\u21E7 ';
            }
            if (parts.cmd) {
                mods += '\u2318 ';
            }
        }
        else {
            if (parts.ctrl) {
                mods += 'Ctrl+';
            }
            if (parts.alt) {
                mods += 'Alt+';
            }
            if (parts.shift) {
                mods += 'Shift+';
            }
        }
        return mods + parts.key;
    }
    Private.formatKeystroke = formatKeystroke;
    /**
     * Hit test a menu hierarchy starting at the given root.
     */
    function hitTestMenus(menu, x, y) {
        for (var temp = menu; temp; temp = temp.childMenu) {
            if (domutils_1.ElementExt.hitTest(temp.node, x, y)) {
                return true;
            }
        }
        return false;
    }
    Private.hitTestMenus = hitTestMenus;
    /**
     * Compute which extra separator items should be collapsed.
     */
    function computeCollapsed(items) {
        // Allocate the return array and fill it with `false`.
        var result = new Array(items.length);
        algorithm_1.ArrayExt.fill(result, false);
        // Collapse the leading separators.
        var k1 = 0;
        var n = items.length;
        for (; k1 < n; ++k1) {
            var item = items[k1];
            if (!item.isVisible) {
                continue;
            }
            if (item.type !== 'separator') {
                break;
            }
            result[k1] = true;
        }
        // Hide the trailing separators.
        var k2 = n - 1;
        for (; k2 >= 0; --k2) {
            var item = items[k2];
            if (!item.isVisible) {
                continue;
            }
            if (item.type !== 'separator') {
                break;
            }
            result[k2] = true;
        }
        // Hide the remaining consecutive separators.
        var hide = false;
        while (++k1 < k2) {
            var item = items[k1];
            if (!item.isVisible) {
                continue;
            }
            if (item.type !== 'separator') {
                hide = false;
            }
            else if (hide) {
                result[k1] = true;
            }
            else {
                hide = true;
            }
        }
        // Return the resulting flags.
        return result;
    }
    Private.computeCollapsed = computeCollapsed;
    /**
     * Open a menu as a root menu at the target location.
     */
    function openRootMenu(menu, x, y, forceX, forceY) {
        // Ensure the menu is updated before attaching and measuring.
        messaging_1.MessageLoop.sendMessage(menu, widget_1.Widget.Msg.UpdateRequest);
        // Get the current position and size of the main viewport.
        var px = window.pageXOffset;
        var py = window.pageYOffset;
        var cw = document.documentElement.clientWidth;
        var ch = document.documentElement.clientHeight;
        // Compute the maximum allowed height for the menu.
        var maxHeight = ch - (forceY ? y : 0);
        // Fetch common variables.
        var node = menu.node;
        var style = node.style;
        // Clear the menu geometry and prepare it for measuring.
        style.top = '';
        style.left = '';
        style.width = '';
        style.height = '';
        style.visibility = 'hidden';
        style.maxHeight = maxHeight + "px";
        // Attach the menu to the document.
        widget_1.Widget.attach(menu, document.body);
        // Measure the size of the menu.
        var _a = node.getBoundingClientRect(), width = _a.width, height = _a.height;
        // Adjust the X position of the menu to fit on-screen.
        if (!forceX && (x + width > px + cw)) {
            x = px + cw - width;
        }
        // Adjust the Y position of the menu to fit on-screen.
        if (!forceY && (y + height > py + ch)) {
            if (y > py + ch) {
                y = py + ch - height;
            }
            else {
                y = y - height;
            }
        }
        // Update the position of the menu to the computed position.
        style.top = Math.max(0, y) + "px";
        style.left = Math.max(0, x) + "px";
        // Finally, make the menu visible on the screen.
        style.visibility = '';
    }
    Private.openRootMenu = openRootMenu;
    /**
     * Open a menu as a submenu using an item node for positioning.
     */
    function openSubmenu(submenu, itemNode) {
        // Ensure the menu is updated before opening.
        messaging_1.MessageLoop.sendMessage(submenu, widget_1.Widget.Msg.UpdateRequest);
        // Get the current position and size of the main viewport.
        var px = window.pageXOffset;
        var py = window.pageYOffset;
        var cw = document.documentElement.clientWidth;
        var ch = document.documentElement.clientHeight;
        // Compute the maximum allowed height for the menu.
        var maxHeight = ch;
        // Fetch common variables.
        var node = submenu.node;
        var style = node.style;
        // Clear the menu geometry and prepare it for measuring.
        style.top = '';
        style.left = '';
        style.width = '';
        style.height = '';
        style.visibility = 'hidden';
        style.maxHeight = maxHeight + "px";
        // Attach the menu to the document.
        widget_1.Widget.attach(submenu, document.body);
        // Measure the size of the menu.
        var _a = node.getBoundingClientRect(), width = _a.width, height = _a.height;
        // Compute the box sizing for the menu.
        var box = domutils_1.ElementExt.boxSizing(submenu.node);
        // Get the bounding rect for the target item node.
        var itemRect = itemNode.getBoundingClientRect();
        // Compute the target X position.
        var x = itemRect.right - Private.SUBMENU_OVERLAP;
        // Adjust the X position to fit on the screen.
        if (x + width > px + cw) {
            x = itemRect.left + Private.SUBMENU_OVERLAP - width;
        }
        // Compute the target Y position.
        var y = itemRect.top - box.borderTop - box.paddingTop;
        // Adjust the Y position to fit on the screen.
        if (y + height > py + ch) {
            y = itemRect.bottom + box.borderBottom + box.paddingBottom - height;
        }
        // Update the position of the menu to the computed position.
        style.top = Math.max(0, y) + "px";
        style.left = Math.max(0, x) + "px";
        // Finally, make the menu visible on the screen.
        style.visibility = '';
    }
    Private.openSubmenu = openSubmenu;
    /**
     * Find the best matching mnemonic item.
     *
     * The search starts at the given index and wraps around.
     */
    function findMnemonic(items, key, start) {
        // Setup the result variables.
        var index = -1;
        var auto = -1;
        var multiple = false;
        // Normalize the key to upper case.
        var upperKey = key.toUpperCase();
        // Search the items from the given start index.
        for (var i = 0, n = items.length; i < n; ++i) {
            // Compute the wrapped index.
            var k = (i + start) % n;
            // Lookup the item
            var item = items[k];
            // Ignore items which cannot be activated.
            if (!canActivate(item)) {
                continue;
            }
            // Ignore items with an empty label.
            var label = item.label;
            if (label.length === 0) {
                continue;
            }
            // Lookup the mnemonic index for the label.
            var mn = item.mnemonic;
            // Handle a valid mnemonic index.
            if (mn >= 0 && mn < label.length) {
                if (label[mn].toUpperCase() === upperKey) {
                    if (index === -1) {
                        index = k;
                    }
                    else {
                        multiple = true;
                    }
                }
                continue;
            }
            // Finally, handle the auto index if possible.
            if (auto === -1 && label[0].toUpperCase() === upperKey) {
                auto = k;
            }
        }
        // Return the search results.
        return { index: index, multiple: multiple, auto: auto };
    }
    Private.findMnemonic = findMnemonic;
    /**
     * A concrete implementation of `Menu.IItem`.
     */
    var MenuItem = (function () {
        /**
         * Construct a new menu item.
         */
        function MenuItem(commands, options) {
            this._commands = commands;
            this.type = options.type || 'command';
            this.command = options.command || '';
            this.args = options.args || coreutils_1.JSONExt.emptyObject;
            this.submenu = options.submenu || null;
        }
        Object.defineProperty(MenuItem.prototype, "label", {
            /**
             * The display label for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.label(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.label;
                }
                return '';
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "mnemonic", {
            /**
             * The mnemonic index for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.mnemonic(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.mnemonic;
                }
                return -1;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "icon", {
            /**
             * @deprecated Use `iconClass` instead.
             */
            get: function () {
                return this.iconClass;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "iconClass", {
            /**
             * The icon class for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.iconClass(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.iconClass;
                }
                return '';
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "iconLabel", {
            /**
             * The icon label for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.iconLabel(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.iconLabel;
                }
                return '';
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "caption", {
            /**
             * The display caption for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.caption(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.caption;
                }
                return '';
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "className", {
            /**
             * The extra class name for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.className(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.className;
                }
                return '';
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "dataset", {
            /**
             * The dataset for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.dataset(this.command, this.args);
                }
                if (this.type === 'submenu' && this.submenu) {
                    return this.submenu.title.dataset;
                }
                return {};
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "isEnabled", {
            /**
             * Whether the menu item is enabled.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.isEnabled(this.command, this.args);
                }
                if (this.type === 'submenu') {
                    return this.submenu !== null;
                }
                return true;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "isToggled", {
            /**
             * Whether the menu item is toggled.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.isToggled(this.command, this.args);
                }
                return false;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "isVisible", {
            /**
             * Whether the menu item is visible.
             */
            get: function () {
                if (this.type === 'command') {
                    return this._commands.isVisible(this.command, this.args);
                }
                if (this.type === 'submenu') {
                    return this.submenu !== null;
                }
                return true;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(MenuItem.prototype, "keyBinding", {
            /**
             * The key binding for the menu item.
             */
            get: function () {
                if (this.type === 'command') {
                    var _a = this, command_1 = _a.command, args_1 = _a.args;
                    return algorithm_1.ArrayExt.findLastValue(this._commands.keyBindings, function (kb) {
                        return kb.command === command_1 && coreutils_1.JSONExt.deepEqual(kb.args, args_1);
                    }) || null;
                }
                return null;
            },
            enumerable: true,
            configurable: true
        });
        return MenuItem;
    }());
})(Private || (Private = {}));
