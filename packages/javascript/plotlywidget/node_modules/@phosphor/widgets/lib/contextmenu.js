"use strict";
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
var disposable_1 = require("@phosphor/disposable");
var domutils_1 = require("@phosphor/domutils");
var menu_1 = require("./menu");
/**
 * An object which implements a universal context menu.
 *
 * #### Notes
 * The items shown in the context menu are determined by CSS selector
 * matching against the DOM hierarchy at the site of the mouse click.
 * This is similar in concept to how keyboard shortcuts are matched
 * in the command registry.
 */
var ContextMenu = (function () {
    /**
     * Construct a new context menu.
     *
     * @param options - The options for initializing the menu.
     */
    function ContextMenu(options) {
        this._idTick = 0;
        this._items = [];
        this.menu = new menu_1.Menu(options);
    }
    /**
     * Add an item to the context menu.
     *
     * @param options - The options for creating the item.
     *
     * @returns A disposable which will remove the item from the menu.
     */
    ContextMenu.prototype.addItem = function (options) {
        var _this = this;
        // Create an item from the given options.
        var item = Private.createItem(options, this._idTick++);
        // Add the item to the internal array.
        this._items.push(item);
        // Return a disposable which will remove the item.
        return new disposable_1.DisposableDelegate(function () {
            algorithm_1.ArrayExt.removeFirstOf(_this._items, item);
        });
    };
    /**
     * Open the context menu in response to a `'contextmenu'` event.
     *
     * @param event - The `'contextmenu'` event of interest.
     *
     * @returns `true` if the menu was opened, or `false` if no items
     *   matched the event and the menu was not opened.
     *
     * #### Notes
     * This method will populate the context menu with items which match
     * the propagation path of the event, then open the menu at the mouse
     * position indicated by the event.
     */
    ContextMenu.prototype.open = function (event) {
        var _this = this;
        // Clear the current contents of the context menu.
        this.menu.clearItems();
        // Bail early if there are no items to match.
        if (this._items.length === 0) {
            return false;
        }
        // Find the matching items for the event.
        var items = Private.matchItems(this._items, event);
        // Bail if there are no matching items.
        if (!items || items.length === 0) {
            return false;
        }
        // Add the filtered items to the menu.
        algorithm_1.each(items, function (item) { _this.menu.addItem(item); });
        // Open the context menu at the current mouse position.
        this.menu.open(event.clientX, event.clientY);
        // Indicate success.
        return true;
    };
    return ContextMenu;
}());
exports.ContextMenu = ContextMenu;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create a normalized context menu item from an options object.
     */
    function createItem(options, id) {
        var selector = validateSelector(options.selector);
        var rank = options.rank !== undefined ? options.rank : Infinity;
        return __assign({}, options, { selector: selector, rank: rank, id: id });
    }
    Private.createItem = createItem;
    /**
     * Find the items which match a context menu event.
     *
     * The results are sorted by DOM level, specificity, and rank.
     */
    function matchItems(items, event) {
        // Look up the target of the event.
        var target = event.target;
        // Bail if there is no target.
        if (!target) {
            return null;
        }
        // Look up the current target of the event.
        var currentTarget = event.currentTarget;
        // Bail if there is no current target.
        if (!currentTarget) {
            return null;
        }
        // There are some third party libraries that cause the `target` to
        // be detached from the DOM before Phosphor can process the event.
        // If that happens, search for a new target node by point. If that
        // node is still dangling, bail.
        if (!currentTarget.contains(target)) {
            target = document.elementFromPoint(event.clientX, event.clientY);
            if (!target || !currentTarget.contains(target)) {
                return null;
            }
        }
        // Set up the result array.
        var result = [];
        // Copy the items array to allow in-place modification.
        var availableItems = items.slice();
        // Walk up the DOM hierarchy searching for matches.
        while (target !== null) {
            // Set up the match array for this DOM level.
            var matches = [];
            // Search the remaining items for matches.
            for (var i = 0, n = availableItems.length; i < n; ++i) {
                // Fetch the item.
                var item = availableItems[i];
                // Skip items which are already consumed.
                if (!item) {
                    continue;
                }
                // Skip items which do not match the element.
                if (!domutils_1.Selector.matches(target, item.selector)) {
                    continue;
                }
                // Add the matched item to the result for this DOM level.
                matches.push(item);
                // Mark the item as consumed.
                availableItems[i] = null;
            }
            // Sort the matches for this level and add them to the results.
            if (matches.length !== 0) {
                matches.sort(itemCmp);
                result.push.apply(result, matches);
            }
            // Stop searching at the limits of the DOM range.
            if (target === currentTarget) {
                break;
            }
            // Step to the parent DOM level.
            target = target.parentElement;
        }
        // Return the matched and sorted results.
        return result;
    }
    Private.matchItems = matchItems;
    /**
     * Validate the selector for a menu item.
     *
     * This returns the validated selector, or throws if the selector is
     * invalid or contains commas.
     */
    function validateSelector(selector) {
        if (selector.indexOf(',') !== -1) {
            throw new Error("Selector cannot contain commas: " + selector);
        }
        if (!domutils_1.Selector.isValid(selector)) {
            throw new Error("Invalid selector: " + selector);
        }
        return selector;
    }
    /**
     * A sort comparison function for a context menu item.
     */
    function itemCmp(a, b) {
        // Sort first based on selector specificity.
        var s1 = domutils_1.Selector.calculateSpecificity(a.selector);
        var s2 = domutils_1.Selector.calculateSpecificity(b.selector);
        if (s1 !== s2) {
            return s2 - s1;
        }
        // If specificities are equal, sort based on rank.
        var r1 = a.rank;
        var r2 = b.rank;
        if (r1 !== r2) {
            return r1 < r2 ? -1 : 1; // Infinity-safe
        }
        // When all else fails, sort by item id.
        return a.id - b.id;
    }
})(Private || (Private = {}));
