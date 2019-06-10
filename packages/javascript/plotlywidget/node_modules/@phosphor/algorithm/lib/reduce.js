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
function reduce(object, fn, initial) {
    // Setup the iterator and fetch the first value.
    var index = 0;
    var it = iter_1.iter(object);
    var first = it.next();
    // An empty iterator and no initial value is an error.
    if (first === undefined && initial === undefined) {
        throw new TypeError('Reduce of empty iterable with no initial value.');
    }
    // If the iterator is empty, return the initial value.
    if (first === undefined) {
        return initial;
    }
    // If the iterator has a single item and no initial value, the
    // reducer is not invoked and the first item is the return value.
    var second = it.next();
    if (second === undefined && initial === undefined) {
        return first;
    }
    // If iterator has a single item and an initial value is provided,
    // the reducer is invoked and that result is the return value.
    if (second === undefined) {
        return fn(initial, first, index++);
    }
    // Setup the initial accumlated value.
    var accumulator;
    if (initial === undefined) {
        accumulator = fn(first, second, index++);
    }
    else {
        accumulator = fn(fn(initial, first, index++), second, index++);
    }
    // Iterate the rest of the values, updating the accumulator.
    var next;
    while ((next = it.next()) !== undefined) {
        accumulator = fn(accumulator, next, index++);
    }
    // Return the final accumulated value.
    return accumulator;
}
exports.reduce = reduce;
