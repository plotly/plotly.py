"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Create an iterator for a retroable object.
 *
 * @param object - The retroable or array-like object of interest.
 *
 * @returns An iterator which traverses the object's values in reverse.
 *
 * #### Example
 * ```typescript
 * import { retro, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3, 4, 5, 6];
 *
 * let stream = retro(data);
 *
 * toArray(stream);  // [6, 5, 4, 3, 2, 1]
 * ```
 */
function retro(object) {
    var it;
    if (typeof object.retro === 'function') {
        it = object.retro();
    }
    else {
        it = new RetroArrayIterator(object);
    }
    return it;
}
exports.retro = retro;
/**
 * An iterator which traverses an array-like object in reverse.
 *
 * #### Notes
 * This iterator can be used for any builtin JS array-like object.
 */
var RetroArrayIterator = (function () {
    /**
     * Construct a new retro iterator.
     *
     * @param source - The array-like object of interest.
     */
    function RetroArrayIterator(source) {
        this._source = source;
        this._index = source.length - 1;
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    RetroArrayIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    RetroArrayIterator.prototype.clone = function () {
        var result = new RetroArrayIterator(this._source);
        result._index = this._index;
        return result;
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    RetroArrayIterator.prototype.next = function () {
        if (this._index < 0 || this._index >= this._source.length) {
            return undefined;
        }
        return this._source[this._index--];
    };
    return RetroArrayIterator;
}());
exports.RetroArrayIterator = RetroArrayIterator;
