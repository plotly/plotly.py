"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Create an empty iterator.
 *
 * @returns A new iterator which yields nothing.
 *
 * #### Example
 * ```typescript
 * import { empty, toArray } from '@phosphor/algorithm';
 *
 * let stream = empty<number>();
 *
 * toArray(stream);  // []
 * ```
 */
function empty() {
    return new EmptyIterator();
}
exports.empty = empty;
/**
 * An iterator which is always empty.
 */
var EmptyIterator = (function () {
    /**
     * Construct a new empty iterator.
     */
    function EmptyIterator() {
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    EmptyIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    EmptyIterator.prototype.clone = function () {
        return new EmptyIterator();
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    EmptyIterator.prototype.next = function () {
        return undefined;
    };
    return EmptyIterator;
}());
exports.EmptyIterator = EmptyIterator;
