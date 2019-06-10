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
 * Transform the values of an iterable with a mapping function.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The mapping function to invoke for each value.
 *
 * @returns An iterator which yields the transformed values.
 *
 * #### Example
 * ```typescript
 * import { map, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3];
 *
 * let stream = map(data, value => value * 2);
 *
 * toArray(stream);  // [2, 4, 6]
 * ```
 */
function map(object, fn) {
    return new MapIterator(iter_1.iter(object), fn);
}
exports.map = map;
/**
 * An iterator which transforms values using a mapping function.
 */
var MapIterator = (function () {
    /**
     * Construct a new map iterator.
     *
     * @param source - The iterator of values of interest.
     *
     * @param fn - The mapping function to invoke for each value.
     */
    function MapIterator(source, fn) {
        this._index = 0;
        this._source = source;
        this._fn = fn;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    MapIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    MapIterator.prototype.clone = function () {
        var result = new MapIterator(this._source.clone(), this._fn);
        result._index = this._index;
        return result;
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    MapIterator.prototype.next = function () {
        var value = this._source.next();
        if (value === undefined) {
            return undefined;
        }
        return this._fn.call(undefined, value, this._index++);
    };
    return MapIterator;
}());
exports.MapIterator = MapIterator;
