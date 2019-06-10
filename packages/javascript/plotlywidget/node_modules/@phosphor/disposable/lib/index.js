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
/**
 * A disposable object which delegates to a callback function.
 */
var DisposableDelegate = (function () {
    /**
     * Construct a new disposable delegate.
     *
     * @param fn - The callback function to invoke on dispose.
     */
    function DisposableDelegate(fn) {
        this._fn = fn;
    }
    Object.defineProperty(DisposableDelegate.prototype, "isDisposed", {
        /**
         * Test whether the delegate has been disposed.
         */
        get: function () {
            return !this._fn;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Dispose of the delegate and invoke the callback function.
     */
    DisposableDelegate.prototype.dispose = function () {
        if (!this._fn) {
            return;
        }
        var fn = this._fn;
        this._fn = null;
        fn();
    };
    return DisposableDelegate;
}());
exports.DisposableDelegate = DisposableDelegate;
/**
 * An object which manages a collection of disposable items.
 */
var DisposableSet = (function () {
    /**
     * Construct a new disposable set.
     */
    function DisposableSet() {
        this._disposed = false;
        this._items = new Set();
    }
    Object.defineProperty(DisposableSet.prototype, "isDisposed", {
        /**
         * Test whether the set has been disposed.
         */
        get: function () {
            return this._disposed;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Dispose of the set and the items it contains.
     *
     * #### Notes
     * Items are disposed in the order they are added to the set.
     */
    DisposableSet.prototype.dispose = function () {
        if (this._disposed) {
            return;
        }
        this._disposed = true;
        this._items.forEach(function (item) { item.dispose(); });
        this._items.clear();
    };
    /**
     * Test whether the set contains a specific item.
     *
     * @param item - The item of interest.
     *
     * @returns `true` if the set contains the item, `false` otherwise.
     */
    DisposableSet.prototype.contains = function (item) {
        return this._items.has(item);
    };
    /**
     * Add a disposable item to the set.
     *
     * @param item - The item to add to the set.
     *
     * #### Notes
     * If the item is already contained in the set, this is a no-op.
     */
    DisposableSet.prototype.add = function (item) {
        this._items.add(item);
    };
    /**
     * Remove a disposable item from the set.
     *
     * @param item - The item to remove from the set.
     *
     * #### Notes
     * If the item is not contained in the set, this is a no-op.
     */
    DisposableSet.prototype.remove = function (item) {
        this._items.delete(item);
    };
    /**
     * Remove all items from the set.
     */
    DisposableSet.prototype.clear = function () {
        this._items.clear();
    };
    return DisposableSet;
}());
exports.DisposableSet = DisposableSet;
/**
 * The namespace for the `DisposableSet` class statics.
 */
(function (DisposableSet) {
    /**
     * Create a disposable set from an iterable of items.
     *
     * @param items - The iterable or array-like object of interest.
     *
     * @returns A new disposable initialized with the given items.
     */
    function from(items) {
        var set = new DisposableSet();
        algorithm_1.each(items, function (item) { set.add(item); });
        return set;
    }
    DisposableSet.from = from;
})(DisposableSet = exports.DisposableSet || (exports.DisposableSet = {}));
exports.DisposableSet = DisposableSet;
