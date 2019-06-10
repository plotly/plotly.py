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
 * Filter an iterable for values which pass a test.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The predicate function to invoke for each value.
 *
 * @returns An iterator which yields the values which pass the test.
 *
 * #### Example
 * ```typescript
 * import { filter, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3, 4, 5, 6];
 *
 * let stream = filter(data, value => value % 2 === 0);
 *
 * toArray(stream);  // [2, 4, 6]
 * ```
 */
function filter(object, fn) {
    return new FilterIterator(iter_1.iter(object), fn);
}
exports.filter = filter;
/**
 * An iterator which yields values which pass a test.
 */
var FilterIterator = (function () {
    /**
     * Construct a new filter iterator.
     *
     * @param source - The iterator of values of interest.
     *
     * @param fn - The predicate function to invoke for each value.
     */
    function FilterIterator(source, fn) {
        this._index = 0;
        this._source = source;
        this._fn = fn;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    FilterIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    FilterIterator.prototype.clone = function () {
        var result = new FilterIterator(this._source.clone(), this._fn);
        result._index = this._index;
        return result;
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    FilterIterator.prototype.next = function () {
        var fn = this._fn;
        var it = this._source;
        var value;
        while ((value = it.next()) !== undefined) {
            if (fn(value, this._index++)) {
                return value;
            }
        }
        return undefined;
    };
    return FilterIterator;
}());
exports.FilterIterator = FilterIterator;
