"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Create an iterator of evenly spaced values.
 *
 * @param start - The starting value for the range, inclusive.
 *
 * @param stop - The stopping value for the range, exclusive.
 *
 * @param step - The distance between each value.
 *
 * @returns An iterator which produces evenly spaced values.
 *
 * #### Notes
 * In the single argument form of `range(stop)`, `start` defaults to
 * `0` and `step` defaults to `1`.
 *
 * In the two argument form of `range(start, stop)`, `step` defaults
 * to `1`.
 */
function range(start, stop, step) {
    if (stop === undefined) {
        return new RangeIterator(0, start, 1);
    }
    if (step === undefined) {
        return new RangeIterator(start, stop, 1);
    }
    return new RangeIterator(start, stop, step);
}
exports.range = range;
/**
 * An iterator which produces a range of evenly spaced values.
 */
var RangeIterator = (function () {
    /**
     * Construct a new range iterator.
     *
     * @param start - The starting value for the range, inclusive.
     *
     * @param stop - The stopping value for the range, exclusive.
     *
     * @param step - The distance between each value.
     */
    function RangeIterator(start, stop, step) {
        this._index = 0;
        this._start = start;
        this._stop = stop;
        this._step = step;
        this._length = Private.rangeLength(start, stop, step);
    }
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    RangeIterator.prototype.iter = function () {
        return this;
    };
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    RangeIterator.prototype.clone = function () {
        var result = new RangeIterator(this._start, this._stop, this._step);
        result._index = this._index;
        return result;
    };
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    RangeIterator.prototype.next = function () {
        if (this._index >= this._length) {
            return undefined;
        }
        return this._start + this._step * this._index++;
    };
    return RangeIterator;
}());
exports.RangeIterator = RangeIterator;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Compute the effective length of a range.
     *
     * @param start - The starting value for the range, inclusive.
     *
     * @param stop - The stopping value for the range, exclusive.
     *
     * @param step - The distance between each value.
     *
     * @returns The number of steps need to traverse the range.
     */
    function rangeLength(start, stop, step) {
        if (step === 0) {
            return Infinity;
        }
        if (start > stop && step > 0) {
            return 0;
        }
        if (start < stop && step < 0) {
            return 0;
        }
        return Math.ceil((stop - start) / step);
    }
    Private.rangeLength = rangeLength;
})(Private || (Private = {}));
