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
 * Chain together several iterables.
 *
 * @param objects - The iterable or array-like objects of interest.
 *
 * @returns An iterator which yields the values of the iterables
 *   in the order in which they are supplied.
 *
 * #### Example
 * ```typescript
 * import { chain, toArray } from '@phosphor/algorithm';
 *
 * let data1 = [1, 2, 3];
 * let data2 = [4, 5, 6];
 *
 * let stream = chain(data1, data2);
 *
 * toArray(stream);  // [1, 2, 3, 4, 5, 6]
 * ```
 */
function chain() {
    var objects = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        objects[_i] = arguments[_i];
    }
    return new ChainIterator(iter_1.iter(objects.map(iter_1.iter)));
}
exports.chain = chain;
/**
 * An iterator which chains together several iterators.
 */
var ChainIterator = (function () {
    /**
     * Construct a new chain iterator.
     *
     * @param source - The iterator of iterators of interest.
     */
    function ChainIterator(source) {
        this._cloned = false;
        this._source = source;
        this._active = undefined;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    ChainIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    ChainIterator.prototype.clone = function () {
        var result = new ChainIterator(this._source.clone());
        result._active = this._active && this._active.clone();
        result._cloned = true;
        this._cloned = true;
        return result;
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    ChainIterator.prototype.next = function () {
        if (this._active === undefined) {
            var active = this._source.next();
            if (active === undefined) {
                return undefined;
            }
            this._active = this._cloned ? active.clone() : active;
        }
        var value = this._active.next();
        if (value !== undefined) {
            return value;
        }
        this._active = undefined;
        return this.next();
    };
    return ChainIterator;
}());
exports.ChainIterator = ChainIterator;
