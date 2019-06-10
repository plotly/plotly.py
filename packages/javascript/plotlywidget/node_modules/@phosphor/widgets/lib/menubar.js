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
var keyboard_1 = require("@phosphor/keyboard");
var messaging_1 = require("@phosphor/messaging");
var virtualdom_1 = require("@phosphor/virtualdom");
var widget_1 = require("./widget");
/**
 * A widget which displays menus as a canonical menu bar.
 */
var MenuBar = (function (_super) {
    __extends(MenuBar, _super);
    /**
     * Construct a new menu bar.
     *
     * @param options - The options for initializing the menu bar.
     */
    function MenuBar(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, { node: Private.createNode() }) || this;
        _this._activeIndex = -1;
        _this._menus = [];
        _this._childMenu = null;
        _this.addClass('p-MenuBar');
        _this.setFlag(widget_1.Widget.Flag.DisallowLayout);
        _this.renderer = options.renderer || MenuBar.defaultRenderer;
        return _this;
    }
    /**
     * Dispose of the resources held by the widget.
     */
    MenuBar.prototype.dispose = function () {
        this._closeChildMenu();
        this._menus.length = 0;
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(MenuBar.prototype, "childMenu", {
        /**
         * The child menu of the menu bar.
         *
         * #### Notes
         * This will be `null` if the menu bar does not have an open menu.
         */
        get: function () {
            return this._childMenu;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(MenuBar.prototype, "contentNode", {
        /**
         * Get the menu bar content node.
         *
         * #### Notes
         * This is the node which holds the menu title nodes.
         *
         * Modifying this node directly can lead to undefined behavior.
         */
        get: function () {
            return this.node.getElementsByClassName('p-MenuBar-content')[0];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(MenuBar.prototype, "activeMenu", {
        /**
         * Get the currently active menu.
         */
        get: function () {
            return this._menus[this._activeIndex] || null;
        },
        /**
         * Set the currently active menu.
         *
         * #### Notes
         * If the menu does not exist, the menu will be set to `null`.
         */
        set: function (value) {
            this.activeIndex = value ? this._menus.indexOf(value) : -1;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(MenuBar.prototype, "activeIndex", {
        /**
         * Get the index of the currently active menu.
         *
         * #### Notes
         * This will be `-1` if no menu is active.
         */
        get: function () {
            return this._activeIndex;
        },
        /**
         * Set the index of the currently active menu.
         *
         * #### Notes
         * If the menu cannot be activated, the index will be set to `-1`.
         */
        set: function (value) {
            // Adjust the value for an out of range index.
            if (value < 0 || value >= this._menus.length) {
                value = -1;
            }
            // Bail early if the index will not change.
            if (this._activeIndex === value) {
                return;
            }
            // Update the active index.
            this._activeIndex = value;
            // Schedule an update of the items.
            this.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(MenuBar.prototype, "menus", {
        /**
         * A read-only array of the menus in the menu bar.
         */
        get: function () {
            return this._menus;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Open the active menu and activate its first menu item.
     *
     * #### Notes
     * If there is no active menu, this is a no-op.
     */
    MenuBar.prototype.openActiveMenu = function () {
        // Bail early if there is no active item.
        if (this._activeIndex === -1) {
            return;
        }
        // Open the child menu.
        this._openChildMenu();
        // Activate the first item in the child menu.
        if (this._childMenu) {
            this._childMenu.activeIndex = -1;
            this._childMenu.activateNextItem();
        }
    };
    /**
     * Add a menu to the end of the menu bar.
     *
     * @param menu - The menu to add to the menu bar.
     *
     * #### Notes
     * If the menu is already added to the menu bar, it will be moved.
     */
    MenuBar.prototype.addMenu = function (menu) {
        this.insertMenu(this._menus.length, menu);
    };
    /**
     * Insert a menu into the menu bar at the specified index.
     *
     * @param index - The index at which to insert the menu.
     *
     * @param menu - The menu to insert into the menu bar.
     *
     * #### Notes
     * The index will be clamped to the bounds of the menus.
     *
     * If the menu is already added to the menu bar, it will be moved.
     */
    MenuBar.prototype.insertMenu = function (index, menu) {
        // Close the child menu before making changes.
        this._closeChildMenu();
        // Look up the index of the menu.
        var i = this._menus.indexOf(menu);
        // Clamp the insert index to the array bounds.
        var j = Math.max(0, Math.min(index, this._menus.length));
        // If the menu is not in the array, insert it.
        if (i === -1) {
            // Insert the menu into the array.
            algorithm_1.ArrayExt.insert(this._menus, j, menu);
            // Add the styling class to the menu.
            menu.addClass('p-MenuBar-menu');
            // Connect to the menu signals.
            menu.aboutToClose.connect(this._onMenuAboutToClose, this);
            menu.menuRequested.connect(this._onMenuMenuRequested, this);
            menu.title.changed.connect(this._onTitleChanged, this);
            // Schedule an update of the items.
            this.update();
            // There is nothing more to do.
            return;
        }
        // Otherwise, the menu exists in the array and should be moved.
        // Adjust the index if the location is at the end of the array.
        if (j === this._menus.length) {
            j--;
        }
        // Bail if there is no effective move.
        if (i === j) {
            return;
        }
        // Move the menu to the new locations.
        algorithm_1.ArrayExt.move(this._menus, i, j);
        // Schedule an update of the items.
        this.update();
    };
    /**
     * Remove a menu from the menu bar.
     *
     * @param menu - The menu to remove from the menu bar.
     *
     * #### Notes
     * This is a no-op if the menu is not in the menu bar.
     */
    MenuBar.prototype.removeMenu = function (menu) {
        this.removeMenuAt(this._menus.indexOf(menu));
    };
    /**
     * Remove the menu at a given index from the menu bar.
     *
     * @param index - The index of the menu to remove.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    MenuBar.prototype.removeMenuAt = function (index) {
        // Close the child menu before making changes.
        this._closeChildMenu();
        // Remove the menu from the array.
        var menu = algorithm_1.ArrayExt.removeAt(this._menus, index);
        // Bail if the index is out of range.
        if (!menu) {
            return;
        }
        // Disconnect from the menu signals.
        menu.aboutToClose.disconnect(this._onMenuAboutToClose, this);
        menu.menuRequested.disconnect(this._onMenuMenuRequested, this);
        menu.title.changed.disconnect(this._onTitleChanged, this);
        // Remove the styling class from the menu.
        menu.removeClass('p-MenuBar-menu');
        // Schedule an update of the items.
        this.update();
    };
    /**
     * Remove all menus from the menu bar.
     */
    MenuBar.prototype.clearMenus = function () {
        // Bail if there is nothing to remove.
        if (this._menus.length === 0) {
            return;
        }
        // Close the child menu before making changes.
        this._closeChildMenu();
        // Disconnect from the menu signals and remove the styling class.
        for (var _i = 0, _a = this._menus; _i < _a.length; _i++) {
            var menu = _a[_i];
            menu.aboutToClose.disconnect(this._onMenuAboutToClose, this);
            menu.menuRequested.disconnect(this._onMenuMenuRequested, this);
            menu.title.changed.disconnect(this._onTitleChanged, this);
            menu.removeClass('p-MenuBar-menu');
        }
        // Clear the menus array.
        this._menus.length = 0;
        // Schedule an update of the items.
        this.update();
    };
    /**
     * Handle the DOM events for the menu bar.
     *
     * @param event - The DOM event sent to the menu bar.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the menu bar's DOM nodes. It
     * should not be called directly by user code.
     */
    MenuBar.prototype.handleEvent = function (event) {
        switch (event.type) {
            case 'keydown':
                this._evtKeyDown(event);
                break;
            case 'mousedown':
                this._evtMouseDown(event);
                break;
            case 'mousemove':
                this._evtMouseMove(event);
                break;
            case 'mouseleave':
                this._evtMouseLeave(event);
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
    MenuBar.prototype.onBeforeAttach = function (msg) {
        this.node.addEventListener('keydown', this);
        this.node.addEventListener('mousedown', this);
        this.node.addEventListener('mousemove', this);
        this.node.addEventListener('mouseleave', this);
        this.node.addEventListener('contextmenu', this);
    };
    /**
     * A message handler invoked on an `'after-detach'` message.
     */
    MenuBar.prototype.onAfterDetach = function (msg) {
        this.node.removeEventListener('keydown', this);
        this.node.removeEventListener('mousedown', this);
        this.node.removeEventListener('mousemove', this);
        this.node.removeEventListener('mouseleave', this);
        this.node.removeEventListener('contextmenu', this);
        this._closeChildMenu();
    };
    /**
     * A message handler invoked on an `'activate-request'` message.
     */
    MenuBar.prototype.onActivateRequest = function (msg) {
        if (this.isAttached) {
            this.node.focus();
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    MenuBar.prototype.onUpdateRequest = function (msg) {
        var menus = this._menus;
        var renderer = this.renderer;
        var activeIndex = this._activeIndex;
        var content = new Array(menus.length);
        for (var i = 0, n = menus.length; i < n; ++i) {
            var title = menus[i].title;
            var active = i === activeIndex;
            content[i] = renderer.renderItem({ title: title, active: active });
        }
        virtualdom_1.VirtualDOM.render(content, this.contentNode);
    };
    /**
     * Handle the `'keydown'` event for the menu bar.
     */
    MenuBar.prototype._evtKeyDown = function (event) {
        // A menu bar handles all keydown events.
        event.preventDefault();
        event.stopPropagation();
        // Fetch the key code for the event.
        var kc = event.keyCode;
        // Enter, Up Arrow, Down Arrow
        if (kc === 13 || kc === 38 || kc === 40) {
            this.openActiveMenu();
            return;
        }
        // Escape
        if (kc === 27) {
            this._closeChildMenu();
            this.activeIndex = -1;
            this.node.blur();
            return;
        }
        // Left Arrow
        if (kc === 37) {
            var i = this._activeIndex;
            var n = this._menus.length;
            this.activeIndex = i === 0 ? n - 1 : i - 1;
            return;
        }
        // Right Arrow
        if (kc === 39) {
            var i = this._activeIndex;
            var n = this._menus.length;
            this.activeIndex = i === n - 1 ? 0 : i + 1;
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
        var result = Private.findMnemonic(this._menus, key, start);
        // Handle the requested mnemonic based on the search results.
        // If exactly one mnemonic is matched, that menu is opened.
        // Otherwise, the next mnemonic is activated if available,
        // followed by the auto mnemonic if available.
        if (result.index !== -1 && !result.multiple) {
            this.activeIndex = result.index;
            this.openActiveMenu();
        }
        else if (result.index !== -1) {
            this.activeIndex = result.index;
        }
        else if (result.auto !== -1) {
            this.activeIndex = result.auto;
        }
    };
    /**
     * Handle the `'mousedown'` event for the menu bar.
     */
    MenuBar.prototype._evtMouseDown = function (event) {
        // Bail if the mouse press was not on the menu bar. This can occur
        // when the document listener is installed for an active menu bar.
        if (!domutils_1.ElementExt.hitTest(this.node, event.clientX, event.clientY)) {
            return;
        }
        // Stop the propagation of the event. Immediate propagation is
        // also stopped so that an open menu does not handle the event.
        event.preventDefault();
        event.stopPropagation();
        event.stopImmediatePropagation();
        // Check if the mouse is over one of the menu items.
        var index = algorithm_1.ArrayExt.findFirstIndex(this.contentNode.children, function (node) {
            return domutils_1.ElementExt.hitTest(node, event.clientX, event.clientY);
        });
        // If the press was not on an item, close the child menu.
        if (index === -1) {
            this._closeChildMenu();
            return;
        }
        // If the press was not the left mouse button, do nothing further.
        if (event.button !== 0) {
            return;
        }
        // Otherwise, toggle the open state of the child menu.
        if (this._childMenu) {
            this._closeChildMenu();
            this.activeIndex = index;
        }
        else {
            this.activeIndex = index;
            this._openChildMenu();
        }
    };
    /**
     * Handle the `'mousemove'` event for the menu bar.
     */
    MenuBar.prototype._evtMouseMove = function (event) {
        // Check if the mouse is over one of the menu items.
        var index = algorithm_1.ArrayExt.findFirstIndex(this.contentNode.children, function (node) {
            return domutils_1.ElementExt.hitTest(node, event.clientX, event.clientY);
        });
        // Bail early if the active index will not change.
        if (index === this._activeIndex) {
            return;
        }
        // Bail early if a child menu is open and the mouse is not over
        // an item. This allows the child menu to be kept open when the
        // mouse is over the empty part of the menu bar.
        if (index === -1 && this._childMenu) {
            return;
        }
        // Update the active index to the hovered item.
        this.activeIndex = index;
        // Open the new menu if a menu is already open.
        if (this._childMenu) {
            this._openChildMenu();
        }
    };
    /**
     * Handle the `'mouseleave'` event for the menu bar.
     */
    MenuBar.prototype._evtMouseLeave = function (event) {
        // Reset the active index if there is no open menu.
        if (!this._childMenu) {
            this.activeIndex = -1;
        }
    };
    /**
     * Open the child menu at the active index immediately.
     *
     * If a different child menu is already open, it will be closed,
     * even if there is no active menu.
     */
    MenuBar.prototype._openChildMenu = function () {
        // If there is no active menu, close the current menu.
        var newMenu = this.activeMenu;
        if (!newMenu) {
            this._closeChildMenu();
            return;
        }
        // Bail if there is no effective menu change.
        var oldMenu = this._childMenu;
        if (oldMenu === newMenu) {
            return;
        }
        // Swap the internal menu reference.
        this._childMenu = newMenu;
        // Close the current menu, or setup for the new menu.
        if (oldMenu) {
            oldMenu.close();
        }
        else {
            this.addClass('p-mod-active');
            document.addEventListener('mousedown', this, true);
        }
        // Ensure the menu bar is updated and look up the item node.
        messaging_1.MessageLoop.sendMessage(this, widget_1.Widget.Msg.UpdateRequest);
        var itemNode = this.contentNode.children[this._activeIndex];
        // Get the positioning data for the new menu.
        var _a = itemNode.getBoundingClientRect(), left = _a.left, bottom = _a.bottom;
        // Open the new menu at the computed location.
        newMenu.open(left, bottom, { forceX: true, forceY: true });
    };
    /**
     * Close the child menu immediately.
     *
     * This is a no-op if a child menu is not open.
     */
    MenuBar.prototype._closeChildMenu = function () {
        // Bail if no child menu is open.
        if (!this._childMenu) {
            return;
        }
        // Remove the active class from the menu bar.
        this.removeClass('p-mod-active');
        // Remove the document listeners.
        document.removeEventListener('mousedown', this, true);
        // Clear the internal menu reference.
        var menu = this._childMenu;
        this._childMenu = null;
        // Close the menu.
        menu.close();
        // Reset the active index.
        this.activeIndex = -1;
    };
    /**
     * Handle the `aboutToClose` signal of a menu.
     */
    MenuBar.prototype._onMenuAboutToClose = function (sender) {
        // Bail if the sender is not the child menu.
        if (sender !== this._childMenu) {
            return;
        }
        // Remove the active class from the menu bar.
        this.removeClass('p-mod-active');
        // Remove the document listeners.
        document.removeEventListener('mousedown', this, true);
        // Clear the internal menu reference.
        this._childMenu = null;
        // Reset the active index.
        this.activeIndex = -1;
    };
    /**
     * Handle the `menuRequested` signal of a child menu.
     */
    MenuBar.prototype._onMenuMenuRequested = function (sender, args) {
        // Bail if the sender is not the child menu.
        if (sender !== this._childMenu) {
            return;
        }
        // Look up the active index and menu count.
        var i = this._activeIndex;
        var n = this._menus.length;
        // Active the next requested index.
        switch (args) {
            case 'next':
                this.activeIndex = i === n - 1 ? 0 : i + 1;
                break;
            case 'previous':
                this.activeIndex = i === 0 ? n - 1 : i - 1;
                break;
        }
        // Open the active menu.
        this.openActiveMenu();
    };
    /**
     * Handle the `changed` signal of a title object.
     */
    MenuBar.prototype._onTitleChanged = function () {
        this.update();
    };
    return MenuBar;
}(widget_1.Widget));
exports.MenuBar = MenuBar;
/**
 * The namespace for the `MenuBar` class statics.
 */
(function (MenuBar) {
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
         * Render the virtual element for a menu bar item.
         *
         * @param data - The data to use for rendering the item.
         *
         * @returns A virtual element representing the item.
         */
        Renderer.prototype.renderItem = function (data) {
            var className = this.createItemClass(data);
            var dataset = this.createItemDataset(data);
            return (virtualdom_1.h.li({ className: className, dataset: dataset }, this.renderIcon(data), this.renderLabel(data)));
        };
        /**
         * Render the icon element for a menu bar item.
         *
         * @param data - The data to use for rendering the icon.
         *
         * @returns A virtual element representing the item icon.
         */
        Renderer.prototype.renderIcon = function (data) {
            var className = this.createIconClass(data);
            return virtualdom_1.h.div({ className: className }, data.title.iconLabel);
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
            return virtualdom_1.h.div({ className: 'p-MenuBar-itemLabel' }, content);
        };
        /**
         * Create the class name for the menu bar item.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the menu item.
         */
        Renderer.prototype.createItemClass = function (data) {
            var name = 'p-MenuBar-item';
            if (data.title.className) {
                name += " " + data.title.className;
            }
            if (data.active) {
                name += ' p-mod-active';
            }
            return name;
        };
        /**
         * Create the dataset for a menu bar item.
         *
         * @param data - The data to use for the item.
         *
         * @returns The dataset for the menu bar item.
         */
        Renderer.prototype.createItemDataset = function (data) {
            return data.title.dataset;
        };
        /**
         * Create the class name for the menu bar item icon.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the item icon.
         */
        Renderer.prototype.createIconClass = function (data) {
            var name = 'p-MenuBar-itemIcon';
            var extra = data.title.iconClass;
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
            var _a = data.title, label = _a.label, mnemonic = _a.mnemonic;
            // If the index is out of range, do not modify the label.
            if (mnemonic < 0 || mnemonic >= label.length) {
                return label;
            }
            // Split the label into parts.
            var prefix = label.slice(0, mnemonic);
            var suffix = label.slice(mnemonic + 1);
            var char = label[mnemonic];
            // Wrap the mnemonic character in a span.
            var span = virtualdom_1.h.span({ className: 'p-MenuBar-itemMnemonic' }, char);
            // Return the content parts.
            return [prefix, span, suffix];
        };
        return Renderer;
    }());
    MenuBar.Renderer = Renderer;
    /**
     * The default `Renderer` instance.
     */
    MenuBar.defaultRenderer = new Renderer();
})(MenuBar = exports.MenuBar || (exports.MenuBar = {}));
exports.MenuBar = MenuBar;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create the DOM node for a menu bar.
     */
    function createNode() {
        var node = document.createElement('div');
        var content = document.createElement('ul');
        content.className = 'p-MenuBar-content';
        node.appendChild(content);
        node.tabIndex = -1;
        return node;
    }
    Private.createNode = createNode;
    /**
     * Find the best matching mnemonic item.
     *
     * The search starts at the given index and wraps around.
     */
    function findMnemonic(menus, key, start) {
        // Setup the result variables.
        var index = -1;
        var auto = -1;
        var multiple = false;
        // Normalize the key to upper case.
        var upperKey = key.toUpperCase();
        // Search the items from the given start index.
        for (var i = 0, n = menus.length; i < n; ++i) {
            // Compute the wrapped index.
            var k = (i + start) % n;
            // Look up the menu title.
            var title = menus[k].title;
            // Ignore titles with an empty label.
            if (title.label.length === 0) {
                continue;
            }
            // Look up the mnemonic index for the label.
            var mn = title.mnemonic;
            // Handle a valid mnemonic index.
            if (mn >= 0 && mn < title.label.length) {
                if (title.label[mn].toUpperCase() === upperKey) {
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
            if (auto === -1 && title.label[0].toUpperCase() === upperKey) {
                auto = k;
            }
        }
        // Return the search results.
        return { index: index, multiple: multiple, auto: auto };
    }
    Private.findMnemonic = findMnemonic;
})(Private || (Private = {}));
