"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var iter_1 = require("./iter");
/**
 * Take a fixed number of items from an iterable.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param count - The number of items to take from the iterable.
 *
 * @returns An iterator which yields the specified number of items
 *   from the source iterable.
 *
 * #### Notes
 * The returned iterator will exhaust early if the source iterable
 * contains an insufficient number of items.
 */
function take(object, count) {
    return new TakeIterator(iter_1.iter(object), count);
}
exports.take = take;
/**
 * An iterator which takes a fixed number of items from a source.
 */
var TakeIterator = (function () {
    /**
     * Construct a new take iterator.
     *
     * @param source - The iterator of interest.
     *
     * @param count - The number of items to take from the source.
     */
    function TakeIterator(source, count) {
        this._source = source;
        this._count = count;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    TakeIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    TakeIterator.prototype.clone = function () {
        return new TakeIterator(this._source.clone(), this._count);
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    TakeIterator.prototype.next = function () {
        if (this._count <= 0) {
            return undefined;
        }
        var value = this._source.next();
        if (value === undefined) {
            return undefined;
        }
        this._count--;
        return value;
    };
    return TakeIterator;
}());
exports.TakeIterator = TakeIterator;
