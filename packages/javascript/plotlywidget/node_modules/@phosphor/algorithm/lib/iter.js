"use strict";
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Create an iterator for an iterable object.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @returns A new iterator for the given object.
 *
 * #### Notes
 * This function allows iteration algorithms to operate on user-defined
 * iterable types and builtin array-like objects in a uniform fashion.
 */
function iter(object) {
    var it;
    if (typeof object.iter === 'function') {
        it = object.iter();
    }
    else {
        it = new ArrayIterator(object);
    }
    return it;
}
exports.iter = iter;
/**
 * Invoke a function for each value in an iterable.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The callback function to invoke for each value.
 *
 * #### Notes
 * Iteration can be terminated early by returning `false` from the
 * callback function.
 *
 * #### Complexity
 * Linear.
 *
 * #### Example
 * ```typescript
 * import { each } from '@phosphor/algorithm';
 *
 * let data = [5, 7, 0, -2, 9];
 *
 * each(data, value => { console.log(value); });
 * ```
 */
function each(object, fn) {
    var index = 0;
    var it = iter(object);
    var value;
    while ((value = it.next()) !== undefined) {
        if (fn(value, index++) === false) {
            return;
        }
    }
}
exports.each = each;
/**
 * Test whether all values in an iterable satisfy a predicate.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The predicate function to invoke for each value.
 *
 * @returns `true` if all values pass the test, `false` otherwise.
 *
 * #### Notes
 * Iteration terminates on the first `false` predicate result.
 *
 * #### Complexity
 * Linear.
 *
 * #### Example
 * ```typescript
 * import { every } from '@phosphor/algorithm';
 *
 * let data = [5, 7, 1];
 *
 * every(data, value => value % 2 === 0);  // false
 * every(data, value => value % 2 === 1);  // true
 * ```
 */
function every(object, fn) {
    var index = 0;
    var it = iter(object);
    var value;
    while ((value = it.next()) !== undefined) {
        if (!fn(value, index++)) {
            return false;
        }
    }
    return true;
}
exports.every = every;
/**
 * Test whether any value in an iterable satisfies a predicate.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The predicate function to invoke for each value.
 *
 * @returns `true` if any value passes the test, `false` otherwise.
 *
 * #### Notes
 * Iteration terminates on the first `true` predicate result.
 *
 * #### Complexity
 * Linear.
 *
 * #### Example
 * ```typescript
 * import { some } from '@phosphor/algorithm';
 *
 * let data = [5, 7, 1];
 *
 * some(data, value => value === 7);  // true
 * some(data, value => value === 3);  // false
 * ```
 */
function some(object, fn) {
    var index = 0;
    var it = iter(object);
    var value;
    while ((value = it.next()) !== undefined) {
        if (fn(value, index++)) {
            return true;
        }
    }
    return false;
}
exports.some = some;
/**
 * Create an array from an iterable of values.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @returns A new array of values from the given object.
 *
 * #### Example
 * ```typescript
 * import { iter, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3, 4, 5, 6];
 *
 * let stream = iter(data);
 *
 * toArray(stream);  // [1, 2, 3, 4, 5, 6];
 * ```
 */
function toArray(object) {
    var index = 0;
    var result = [];
    var it = iter(object);
    var value;
    while ((value = it.next()) !== undefined) {
        result[index++] = value;
    }
    return result;
}
exports.toArray = toArray;
/**
 * An iterator for an array-like object.
 *
 * #### Notes
 * This iterator can be used for any builtin JS array-like object.
 */
var ArrayIterator = (function () {
    /**
     * Construct a new array iterator.
     *
     * @param source - The array-like object of interest.
     */
    function ArrayIterator(source) {
        this._index = 0;
        this._source = source;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    ArrayIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    ArrayIterator.prototype.clone = function () {
        var result = new ArrayIterator(this._source);
        result._index = this._index;
        return result;
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    ArrayIterator.prototype.next = function () {
        if (this._index >= this._source.length) {
            return undefined;
        }
        return this._source[this._index++];
    };
    return ArrayIterator;
}());
exports.ArrayIterator = ArrayIterator;
