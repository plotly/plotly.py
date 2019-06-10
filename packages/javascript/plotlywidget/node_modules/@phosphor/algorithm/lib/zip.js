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
 * Iterate several iterables in lockstep.
 *
 * @param objects - The iterable or array-like objects of interest.
 *
 * @returns An iterator which yields successive tuples of values where
 *   each value is taken in turn from the provided iterables. It will
 *   be as long as the shortest provided iterable.
 *
 * #### Example
 * ```typescript
 * import { zip, toArray } from '@phosphor/algorithm';
 *
 * let data1 = [1, 2, 3];
 * let data2 = [4, 5, 6];
 *
 * let stream = zip(data1, data2);
 *
 * toArray(stream);  // [[1, 4], [2, 5], [3, 6]]
 * ```
 */
function zip() {
    var objects = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        objects[_i] = arguments[_i];
    }
    return new ZipIterator(objects.map(iter_1.iter));
}
exports.zip = zip;
/**
 * An iterator which iterates several sources in lockstep.
 */
var ZipIterator = (function () {
    /**
     * Construct a new zip iterator.
     *
     * @param source - The iterators of interest.
     */
    function ZipIterator(source) {
        this._source = source;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    ZipIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    ZipIterator.prototype.clone = function () {
        return new ZipIterator(this._source.map(function (it) { return it.clone(); }));
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    ZipIterator.prototype.next = function () {
        var result = new Array(this._source.length);
        for (var i = 0, n = this._source.length; i < n; ++i) {
            var value = this._source[i].next();
            if (value === undefined) {
                return undefined;
            }
            result[i] = value;
        }
        return result;
    };
    return ZipIterator;
}());
exports.ZipIterator = ZipIterator;
