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
 * The namespace for array-specific algorithms.
 */
var ArrayExt;
(function (ArrayExt) {
    /**
     * Find the index of the first occurrence of a value in an array.
     *
     * @param array - The array-like object to search.
     *
     * @param value - The value to locate in the array. Values are
     *   compared using strict `===` equality.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the first occurrence of the value, or `-1`
     *   if the value is not found.
     *
     * #### Notes
     * If `stop < start` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = ['one', 'two', 'three', 'four', 'one'];
     * ArrayExt.firstIndexOf(data, 'red');        // -1
     * ArrayExt.firstIndexOf(data, 'one');        // 0
     * ArrayExt.firstIndexOf(data, 'one', 1);     // 4
     * ArrayExt.firstIndexOf(data, 'two', 2);     // -1
     * ArrayExt.firstIndexOf(data, 'two', 2, 1);  // 1
     * ```
     */
    function firstIndexOf(array, value, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return -1;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var span;
        if (stop < start) {
            span = (stop + 1) + (n - start);
        }
        else {
            span = stop - start + 1;
        }
        for (var i = 0; i < span; ++i) {
            var j = (start + i) % n;
            if (array[j] === value) {
                return j;
            }
        }
        return -1;
    }
    ArrayExt.firstIndexOf = firstIndexOf;
    /**
     * Find the index of the last occurrence of a value in an array.
     *
     * @param array - The array-like object to search.
     *
     * @param value - The value to locate in the array. Values are
     *   compared using strict `===` equality.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the last occurrence of the value, or `-1`
     *   if the value is not found.
     *
     * #### Notes
     * If `start < stop` the search will wrap at the front of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = ['one', 'two', 'three', 'four', 'one'];
     * ArrayExt.lastIndexOf(data, 'red');        // -1
     * ArrayExt.lastIndexOf(data, 'one');        // 4
     * ArrayExt.lastIndexOf(data, 'one', 1);     // 0
     * ArrayExt.lastIndexOf(data, 'two', 0);     // -1
     * ArrayExt.lastIndexOf(data, 'two', 0, 1);  // 1
     * ```
     */
    function lastIndexOf(array, value, start, stop) {
        if (start === void 0) { start = -1; }
        if (stop === void 0) { stop = 0; }
        var n = array.length;
        if (n === 0) {
            return -1;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var span;
        if (start < stop) {
            span = (start + 1) + (n - stop);
        }
        else {
            span = start - stop + 1;
        }
        for (var i = 0; i < span; ++i) {
            var j = (start - i + n) % n;
            if (array[j] === value) {
                return j;
            }
        }
        return -1;
    }
    ArrayExt.lastIndexOf = lastIndexOf;
    /**
     * Find the index of the first value which matches a predicate.
     *
     * @param array - The array-like object to search.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the first matching value, or `-1` if no
     *   matching value is found.
     *
     * #### Notes
     * If `stop < start` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * Modifying the length of the array while searching.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * let data = [1, 2, 3, 4, 3, 2, 1];
     * ArrayExt.findFirstIndex(data, isEven);       // 1
     * ArrayExt.findFirstIndex(data, isEven, 4);    // 5
     * ArrayExt.findFirstIndex(data, isEven, 6);    // -1
     * ArrayExt.findFirstIndex(data, isEven, 6, 5); // 1
     * ```
     */
    function findFirstIndex(array, fn, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return -1;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var span;
        if (stop < start) {
            span = (stop + 1) + (n - start);
        }
        else {
            span = stop - start + 1;
        }
        for (var i = 0; i < span; ++i) {
            var j = (start + i) % n;
            if (fn(array[j], j)) {
                return j;
            }
        }
        return -1;
    }
    ArrayExt.findFirstIndex = findFirstIndex;
    /**
     * Find the index of the last value which matches a predicate.
     *
     * @param object - The array-like object to search.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the last matching value, or `-1` if no
     *   matching value is found.
     *
     * #### Notes
     * If `start < stop` the search will wrap at the front of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * Modifying the length of the array while searching.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * let data = [1, 2, 3, 4, 3, 2, 1];
     * ArrayExt.findLastIndex(data, isEven);        // 5
     * ArrayExt.findLastIndex(data, isEven, 4);     // 3
     * ArrayExt.findLastIndex(data, isEven, 0);     // -1
     * ArrayExt.findLastIndex(data, isEven, 0, 1);  // 5
     * ```
     */
    function findLastIndex(array, fn, start, stop) {
        if (start === void 0) { start = -1; }
        if (stop === void 0) { stop = 0; }
        var n = array.length;
        if (n === 0) {
            return -1;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var d;
        if (start < stop) {
            d = (start + 1) + (n - stop);
        }
        else {
            d = start - stop + 1;
        }
        for (var i = 0; i < d; ++i) {
            var j = (start - i + n) % n;
            if (fn(array[j], j)) {
                return j;
            }
        }
        return -1;
    }
    ArrayExt.findLastIndex = findLastIndex;
    /**
     * Find the first value which matches a predicate.
     *
     * @param array - The array-like object to search.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The first matching value, or `undefined` if no matching
     *   value is found.
     *
     * #### Notes
     * If `stop < start` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * Modifying the length of the array while searching.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * let data = [1, 2, 3, 4, 3, 2, 1];
     * ArrayExt.findFirstValue(data, isEven);       // 2
     * ArrayExt.findFirstValue(data, isEven, 2);    // 4
     * ArrayExt.findFirstValue(data, isEven, 6);    // undefined
     * ArrayExt.findFirstValue(data, isEven, 6, 5); // 2
     * ```
     */
    function findFirstValue(array, fn, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var index = findFirstIndex(array, fn, start, stop);
        return index !== -1 ? array[index] : undefined;
    }
    ArrayExt.findFirstValue = findFirstValue;
    /**
     * Find the last value which matches a predicate.
     *
     * @param object - The array-like object to search.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The last matching value, or `undefined` if no matching
     *   value is found.
     *
     * #### Notes
     * If `start < stop` the search will wrap at the front of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * Modifying the length of the array while searching.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * let data = [1, 2, 3, 4, 3, 2, 1];
     * ArrayExt.findLastValue(data, isEven);        // 2
     * ArrayExt.findLastValue(data, isEven, 4);     // 4
     * ArrayExt.findLastValue(data, isEven, 0);     // undefined
     * ArrayExt.findLastValue(data, isEven, 0, 1);  // 2
     * ```
     */
    function findLastValue(array, fn, start, stop) {
        if (start === void 0) { start = -1; }
        if (stop === void 0) { stop = 0; }
        var index = findLastIndex(array, fn, start, stop);
        return index !== -1 ? array[index] : undefined;
    }
    ArrayExt.findLastValue = findLastValue;
    /**
     * Find the index of the first element which compares `>=` to a value.
     *
     * @param array - The sorted array-like object to search.
     *
     * @param value - The value to locate in the array.
     *
     * @param fn - The 3-way comparison function to apply to the values.
     *   It should return `< 0` if an element is less than a value, `0` if
     *   an element is equal to a value, or `> 0` if an element is greater
     *   than a value.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the first element which compares `>=` to the
     *   value, or `length` if there is no such element. If the computed
     *   index for `stop` is less than `start`, then the computed index
     *   for `start` is returned.
     *
     * #### Notes
     * The array must already be sorted in ascending order according to
     * the comparison function.
     *
     * #### Complexity
     * Logarithmic.
     *
     * #### Undefined Behavior
     * Searching a range which is not sorted in ascending order.
     *
     * A `start` or `stop` which is non-integral.
     *
     * Modifying the length of the array while searching.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function numberCmp(a: number, b: number): number {
     *   return a - b;
     * }
     *
     * let data = [0, 3, 4, 7, 7, 9];
     * ArrayExt.lowerBound(data, 0, numberCmp);   // 0
     * ArrayExt.lowerBound(data, 6, numberCmp);   // 3
     * ArrayExt.lowerBound(data, 7, numberCmp);   // 3
     * ArrayExt.lowerBound(data, -1, numberCmp);  // 0
     * ArrayExt.lowerBound(data, 10, numberCmp);  // 6
     * ```
     */
    function lowerBound(array, value, fn, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return 0;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var begin = start;
        var span = stop - start + 1;
        while (span > 0) {
            var half = span >> 1;
            var middle = begin + half;
            if (fn(array[middle], value) < 0) {
                begin = middle + 1;
                span -= half + 1;
            }
            else {
                span = half;
            }
        }
        return begin;
    }
    ArrayExt.lowerBound = lowerBound;
    /**
     * Find the index of the first element which compares `>` than a value.
     *
     * @param array - The sorted array-like object to search.
     *
     * @param value - The value to locate in the array.
     *
     * @param fn - The 3-way comparison function to apply to the values.
     *   It should return `< 0` if an element is less than a value, `0` if
     *   an element is equal to a value, or `> 0` if an element is greater
     *   than a value.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the first element which compares `>` than the
     *   value, or `length` if there is no such element. If the computed
     *   index for `stop` is less than `start`, then the computed index
     *   for `start` is returned.
     *
     * #### Notes
     * The array must already be sorted in ascending order according to
     * the comparison function.
     *
     * #### Complexity
     * Logarithmic.
     *
     * #### Undefined Behavior
     * Searching a range which is not sorted in ascending order.
     *
     * A `start` or `stop` which is non-integral.
     *
     * Modifying the length of the array while searching.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function numberCmp(a: number, b: number): number {
     *   return a - b;
     * }
     *
     * let data = [0, 3, 4, 7, 7, 9];
     * ArrayExt.upperBound(data, 0, numberCmp);   // 1
     * ArrayExt.upperBound(data, 6, numberCmp);   // 3
     * ArrayExt.upperBound(data, 7, numberCmp);   // 5
     * ArrayExt.upperBound(data, -1, numberCmp);  // 0
     * ArrayExt.upperBound(data, 10, numberCmp);  // 6
     * ```
     */
    function upperBound(array, value, fn, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return 0;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var begin = start;
        var span = stop - start + 1;
        while (span > 0) {
            var half = span >> 1;
            var middle = begin + half;
            if (fn(array[middle], value) > 0) {
                span = half;
            }
            else {
                begin = middle + 1;
                span -= half + 1;
            }
        }
        return begin;
    }
    ArrayExt.upperBound = upperBound;
    /**
     * Move an element in an array from one index to another.
     *
     * @param array - The mutable array-like object of interest.
     *
     * @param fromIndex - The index of the element to move. Negative
     *   values are taken as an offset from the end of the array.
     *
     * @param toIndex - The target index of the element. Negative
     *   values are taken as an offset from the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `fromIndex` or `toIndex` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from from '@phosphor/algorithm';
     *
     * let data = [0, 1, 2, 3, 4];
     * ArrayExt.move(data, 1, 2);  // [0, 2, 1, 3, 4]
     * ArrayExt.move(data, 4, 2);  // [0, 2, 4, 1, 3]
     * ```
     */
    function move(array, fromIndex, toIndex) {
        var n = array.length;
        if (n <= 1) {
            return;
        }
        if (fromIndex < 0) {
            fromIndex = Math.max(0, fromIndex + n);
        }
        else {
            fromIndex = Math.min(fromIndex, n - 1);
        }
        if (toIndex < 0) {
            toIndex = Math.max(0, toIndex + n);
        }
        else {
            toIndex = Math.min(toIndex, n - 1);
        }
        if (fromIndex === toIndex) {
            return;
        }
        var value = array[fromIndex];
        var d = fromIndex < toIndex ? 1 : -1;
        for (var i = fromIndex; i !== toIndex; i += d) {
            array[i] = array[i + d];
        }
        array[toIndex] = value;
    }
    ArrayExt.move = move;
    /**
     * Reverse an array in-place.
     *
     * @param array - The mutable array-like object of interest.
     *
     * @param start - The index of the first element in the range to be
     *   reversed, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   reversed, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or  `stop` index which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [0, 1, 2, 3, 4];
     * ArrayExt.reverse(data, 1, 3);  // [0, 3, 2, 1, 4]
     * ArrayExt.reverse(data, 3);     // [0, 3, 2, 4, 1]
     * ArrayExt.reverse(data);        // [1, 4, 2, 3, 0]
     * ```
     */
    function reverse(array, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n <= 1) {
            return;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        while (start < stop) {
            var a = array[start];
            var b = array[stop];
            array[start++] = b;
            array[stop--] = a;
        }
    }
    ArrayExt.reverse = reverse;
    /**
     * Rotate the elements of an array in-place.
     *
     * @param array - The mutable array-like object of interest.
     *
     * @param delta - The amount of rotation to apply to the elements. A
     *   positive value will rotate the elements to the left. A negative
     *   value will rotate the elements to the right.
     *
     * @param start - The index of the first element in the range to be
     *   rotated, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   rotated, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `delta`, `start`, or `stop` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [0, 1, 2, 3, 4];
     * ArrayExt.rotate(data, 2);        // [2, 3, 4, 0, 1]
     * ArrayExt.rotate(data, -2);       // [0, 1, 2, 3, 4]
     * ArrayExt.rotate(data, 10);       // [0, 1, 2, 3, 4]
     * ArrayExt.rotate(data, 9);        // [4, 0, 1, 2, 3]
     * ArrayExt.rotate(data, 2, 1, 3);  // [4, 2, 0, 1, 3]
     * ```
     */
    function rotate(array, delta, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n <= 1) {
            return;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        if (start >= stop) {
            return;
        }
        var length = stop - start + 1;
        if (delta > 0) {
            delta = delta % length;
        }
        else if (delta < 0) {
            delta = ((delta % length) + length) % length;
        }
        if (delta === 0) {
            return;
        }
        var pivot = start + delta;
        reverse(array, start, pivot - 1);
        reverse(array, pivot, stop);
        reverse(array, start, stop);
    }
    ArrayExt.rotate = rotate;
    /**
     * Fill an array with a static value.
     *
     * @param array - The mutable array-like object to fill.
     *
     * @param value - The static value to use to fill the array.
     *
     * @param start - The index of the first element in the range to be
     *   filled, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   filled, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * #### Notes
     * If `stop < start` the fill will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * A `start` or `stop` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = ['one', 'two', 'three', 'four'];
     * ArrayExt.fill(data, 'r');        // ['r', 'r', 'r', 'r']
     * ArrayExt.fill(data, 'g', 1);     // ['r', 'g', 'g', 'g']
     * ArrayExt.fill(data, 'b', 2, 3);  // ['r', 'g', 'b', 'b']
     * ArrayExt.fill(data, 'z', 3, 1);  // ['z', 'z', 'b', 'z']
     * ```
     */
    function fill(array, value, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var span;
        if (stop < start) {
            span = (stop + 1) + (n - start);
        }
        else {
            span = stop - start + 1;
        }
        for (var i = 0; i < span; ++i) {
            array[(start + i) % n] = value;
        }
    }
    ArrayExt.fill = fill;
    /**
     * Insert a value into an array at a specific index.
     *
     * @param array - The array of interest.
     *
     * @param index - The index at which to insert the value. Negative
     *   values are taken as an offset from the end of the array.
     *
     * @param value - The value to set at the specified index.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * An `index` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [0, 1, 2];
     * ArrayExt.insert(data, 0, -1);  // [-1, 0, 1, 2]
     * ArrayExt.insert(data, 2, 12);  // [-1, 0, 12, 1, 2]
     * ArrayExt.insert(data, -1, 7);  // [-1, 0, 12, 1, 7, 2]
     * ArrayExt.insert(data, 6, 19);  // [-1, 0, 12, 1, 7, 2, 19]
     * ```
     */
    function insert(array, index, value) {
        var n = array.length;
        if (index < 0) {
            index = Math.max(0, index + n);
        }
        else {
            index = Math.min(index, n);
        }
        for (var i = n; i > index; --i) {
            array[i] = array[i - 1];
        }
        array[index] = value;
    }
    ArrayExt.insert = insert;
    /**
     * Remove and return a value at a specific index in an array.
     *
     * @param array - The array of interest.
     *
     * @param index - The index of the value to remove. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The value at the specified index, or `undefined` if the
     *   index is out of range.
     *
     * #### Complexity
     * Linear.
     *
     * #### Undefined Behavior
     * An `index` which is non-integral.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [0, 12, 23, 39, 14, 12, 75];
     * ArrayExt.removeAt(data, 2);   // 23
     * ArrayExt.removeAt(data, -2);  // 12
     * ArrayExt.removeAt(data, 10);  // undefined;
     * ```
     */
    function removeAt(array, index) {
        var n = array.length;
        if (index < 0) {
            index += n;
        }
        if (index < 0 || index >= n) {
            return undefined;
        }
        var value = array[index];
        for (var i = index + 1; i < n; ++i) {
            array[i - 1] = array[i];
        }
        array.length = n - 1;
        return value;
    }
    ArrayExt.removeAt = removeAt;
    /**
     * Remove the first occurrence of a value from an array.
     *
     * @param array - The array of interest.
     *
     * @param value - The value to remove from the array. Values are
     *   compared using strict `===` equality.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the removed value, or `-1` if the value
     *   is not contained in the array.
     *
     * #### Notes
     * If `stop < start` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [0, 12, 23, 39, 14, 12, 75];
     * ArrayExt.removeFirstOf(data, 12);        // 1
     * ArrayExt.removeFirstOf(data, 17);        // -1
     * ArrayExt.removeFirstOf(data, 39, 3);     // -1
     * ArrayExt.removeFirstOf(data, 39, 3, 2);  // 2
     * ```
     */
    function removeFirstOf(array, value, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var index = firstIndexOf(array, value, start, stop);
        if (index !== -1) {
            removeAt(array, index);
        }
        return index;
    }
    ArrayExt.removeFirstOf = removeFirstOf;
    /**
     * Remove the last occurrence of a value from an array.
     *
     * @param array - The array of interest.
     *
     * @param value - The value to remove from the array. Values are
     *   compared using strict `===` equality.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The index of the removed value, or `-1` if the value
     *   is not contained in the array.
     *
     * #### Notes
     * If `start < stop` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [0, 12, 23, 39, 14, 12, 75];
     * ArrayExt.removeLastOf(data, 12);        // 5
     * ArrayExt.removeLastOf(data, 17);        // -1
     * ArrayExt.removeLastOf(data, 39, 2);     // -1
     * ArrayExt.removeLastOf(data, 39, 2, 3);  // 3
     * ```
     */
    function removeLastOf(array, value, start, stop) {
        if (start === void 0) { start = -1; }
        if (stop === void 0) { stop = 0; }
        var index = lastIndexOf(array, value, start, stop);
        if (index !== -1) {
            removeAt(array, index);
        }
        return index;
    }
    ArrayExt.removeLastOf = removeLastOf;
    /**
     * Remove all occurrences of a value from an array.
     *
     * @param array - The array of interest.
     *
     * @param value - The value to remove from the array. Values are
     *   compared using strict `===` equality.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The number of elements removed from the array.
     *
     * #### Notes
     * If `stop < start` the search will conceptually wrap at the end of
     * the array, however the array will be traversed front-to-back.
     *
     * #### Complexity
     * Linear.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * let data = [14, 12, 23, 39, 14, 12, 19, 14];
     * ArrayExt.removeAllOf(data, 12);        // 2
     * ArrayExt.removeAllOf(data, 17);        // 0
     * ArrayExt.removeAllOf(data, 14, 1, 4);  // 1
     * ```
     */
    function removeAllOf(array, value, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return 0;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var count = 0;
        for (var i = 0; i < n; ++i) {
            if (start <= stop && (i >= start && i <= stop) && array[i] === value) {
                count++;
            }
            else if (stop < start && (i <= stop || i >= start) && array[i] === value) {
                count++;
            }
            else if (count > 0) {
                array[i - count] = array[i];
            }
        }
        if (count > 0) {
            array.length = n - count;
        }
        return count;
    }
    ArrayExt.removeAllOf = removeAllOf;
    /**
     * Remove the first occurrence of a value which matches a predicate.
     *
     * @param array - The array of interest.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The removed `{ index, value }`, which will be `-1` and
     *   `undefined` if the value is not contained in the array.
     *
     * #### Notes
     * If `stop < start` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * let data = [0, 12, 23, 39, 14, 12, 75];
     * ArrayExt.removeFirstWhere(data, isEven);     // { index: 0, value: 0 }
     * ArrayExt.removeFirstWhere(data, isEven, 2);  // { index: 3, value: 14 }
     * ArrayExt.removeFirstWhere(data, isEven, 4);  // { index: -1, value: undefined }
     * ```
     */
    function removeFirstWhere(array, fn, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var value;
        var index = findFirstIndex(array, fn, start, stop);
        if (index !== -1) {
            value = removeAt(array, index);
        }
        return { index: index, value: value };
    }
    ArrayExt.removeFirstWhere = removeFirstWhere;
    /**
     * Remove the last occurrence of a value which matches a predicate.
     *
     * @param array - The array of interest.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The removed `{ index, value }`, which will be `-1` and
     *   `undefined` if the value is not contained in the array.
     *
     * #### Notes
     * If `start < stop` the search will wrap at the end of the array.
     *
     * #### Complexity
     * Linear.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * let data = [0, 12, 23, 39, 14, 12, 75];
     * ArrayExt.removeLastWhere(data, isEven);        // { index: 5, value: 12 }
     * ArrayExt.removeLastWhere(data, isEven, 2);     // { index: 1, value: 12 }
     * ArrayExt.removeLastWhere(data, isEven, 2, 1);  // { index: -1, value: undefined }
     * ```
     */
    function removeLastWhere(array, fn, start, stop) {
        if (start === void 0) { start = -1; }
        if (stop === void 0) { stop = 0; }
        var value;
        var index = findLastIndex(array, fn, start, stop);
        if (index !== -1) {
            value = removeAt(array, index);
        }
        return { index: index, value: value };
    }
    ArrayExt.removeLastWhere = removeLastWhere;
    /**
     * Remove all occurrences of values which match a predicate.
     *
     * @param array - The array of interest.
     *
     * @param fn - The predicate function to apply to the values.
     *
     * @param start - The index of the first element in the range to be
     *   searched, inclusive. The default value is `0`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @param stop - The index of the last element in the range to be
     *   searched, inclusive. The default value is `-1`. Negative values
     *   are taken as an offset from the end of the array.
     *
     * @returns The number of elements removed from the array.
     *
     * #### Notes
     * If `stop < start` the search will conceptually wrap at the end of
     * the array, however the array will be traversed front-to-back.
     *
     * #### Complexity
     * Linear.
     *
     * #### Example
     * ```typescript
     * import { ArrayExt } from '@phosphor/algorithm';
     *
     * function isEven(value: number): boolean {
     *   return value % 2 === 0;
     * }
     *
     * function isNegative(value: number): boolean {
     *   return value < 0;
     * }
     *
     * let data = [0, 12, -13, -9, 23, 39, 14, -15, 12, 75];
     * ArrayExt.removeAllWhere(data, isEven);            // 4
     * ArrayExt.removeAllWhere(data, isNegative, 0, 3);  // 2
     * ```
     */
    function removeAllWhere(array, fn, start, stop) {
        if (start === void 0) { start = 0; }
        if (stop === void 0) { stop = -1; }
        var n = array.length;
        if (n === 0) {
            return 0;
        }
        if (start < 0) {
            start = Math.max(0, start + n);
        }
        else {
            start = Math.min(start, n - 1);
        }
        if (stop < 0) {
            stop = Math.max(0, stop + n);
        }
        else {
            stop = Math.min(stop, n - 1);
        }
        var count = 0;
        for (var i = 0; i < n; ++i) {
            if (start <= stop && (i >= start && i <= stop) && fn(array[i], i)) {
                count++;
            }
            else if (stop < start && (i <= stop || i >= start) && fn(array[i], i)) {
                count++;
            }
            else if (count > 0) {
                array[i - count] = array[i];
            }
        }
        if (count > 0) {
            array.length = n - count;
        }
        return count;
    }
    ArrayExt.removeAllWhere = removeAllWhere;
})(ArrayExt = exports.ArrayExt || (exports.ArrayExt = {}));
