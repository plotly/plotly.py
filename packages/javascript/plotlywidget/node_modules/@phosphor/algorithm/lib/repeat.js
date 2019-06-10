"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Create an iterator which repeats a value a number of times.
 *
 * @param value - The value to repeat.
 *
 * @param count - The number of times to repeat the value.
 *
 * @returns A new iterator which repeats the specified value.
 *
 * #### Example
 * ```typescript
 * import { repeat, toArray } from '@phosphor/algorithm';
 *
 * let stream = repeat(7, 3);
 *
 * toArray(stream);  // [7, 7, 7]
 * ```
 */
function repeat(value, count) {
    return new RepeatIterator(value, count);
}
exports.repeat = repeat;
/**
 * Create an iterator which yields a value a single time.
 *
 * @param value - The value to wrap in an iterator.
 *
 * @returns A new iterator which yields the value a single time.
 *
 * #### Example
 * ```typescript
 * import { once, toArray } from '@phosphor/algorithm';
 *
 * let stream = once(7);
 *
 * toArray(stream);  // [7]
 * ```
 */
function once(value) {
    return new RepeatIterator(value, 1);
}
exports.once = once;
/**
 * An iterator which repeats a value a specified number of times.
 */
var RepeatIterator = (function () {
    /**
     * Construct a new repeat iterator.
     *
     * @param value - The value to repeat.
     *
     * @param count - The number of times to repeat the value.
     */
    function RepeatIterator(value, count) {
        this._value = value;
        this._count = count;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    RepeatIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    RepeatIterator.prototype.clone = function () {
        return new RepeatIterator(this._value, this._count);
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    RepeatIterator.prototype.next = function () {
        if (this._count <= 0) {
            return undefined;
        }
        this._count--;
        return this._value;
    };
    return RepeatIterator;
}());
exports.RepeatIterator = RepeatIterator;
