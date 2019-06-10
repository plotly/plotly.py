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
 * The namespace for JSON-specific functions.
 */
var JSONExt;
(function (JSONExt) {
    /**
     * A shared frozen empty JSONObject
     */
    JSONExt.emptyObject = Object.freeze({});
    /**
     * A shared frozen empty JSONArray
     */
    JSONExt.emptyArray = Object.freeze([]);
    /**
     * Test whether a JSON value is a primitive.
     *
     * @param value - The JSON value of interest.
     *
     * @returns `true` if the value is a primitive,`false` otherwise.
     */
    function isPrimitive(value) {
        return (value === null ||
            typeof value === 'boolean' ||
            typeof value === 'number' ||
            typeof value === 'string');
    }
    JSONExt.isPrimitive = isPrimitive;
    function isArray(value) {
        return Array.isArray(value);
    }
    JSONExt.isArray = isArray;
    function isObject(value) {
        return !isPrimitive(value) && !isArray(value);
    }
    JSONExt.isObject = isObject;
    /**
     * Compare two JSON values for deep equality.
     *
     * @param first - The first JSON value of interest.
     *
     * @param second - The second JSON value of interest.
     *
     * @returns `true` if the values are equivalent, `false` otherwise.
     */
    function deepEqual(first, second) {
        // Check referential and primitive equality first.
        if (first === second) {
            return true;
        }
        // If one is a primitive, the `===` check ruled out the other.
        if (isPrimitive(first) || isPrimitive(second)) {
            return false;
        }
        // Test whether they are arrays.
        var a1 = isArray(first);
        var a2 = isArray(second);
        // Bail if the types are different.
        if (a1 !== a2) {
            return false;
        }
        // If they are both arrays, compare them.
        if (a1 && a2) {
            return deepArrayEqual(first, second);
        }
        // At this point, they must both be objects.
        return deepObjectEqual(first, second);
    }
    JSONExt.deepEqual = deepEqual;
    /**
     * Create a deep copy of a JSON value.
     *
     * @param value - The JSON value to copy.
     *
     * @returns A deep copy of the given JSON value.
     */
    function deepCopy(value) {
        // Do nothing for primitive values.
        if (isPrimitive(value)) {
            return value;
        }
        // Deep copy an array.
        if (isArray(value)) {
            return deepArrayCopy(value);
        }
        // Deep copy an object.
        return deepObjectCopy(value);
    }
    JSONExt.deepCopy = deepCopy;
    /**
     * Compare two JSON arrays for deep equality.
     */
    function deepArrayEqual(first, second) {
        // Check referential equality first.
        if (first === second) {
            return true;
        }
        // Test the arrays for equal length.
        if (first.length !== second.length) {
            return false;
        }
        // Compare the values for equality.
        for (var i = 0, n = first.length; i < n; ++i) {
            if (!deepEqual(first[i], second[i])) {
                return false;
            }
        }
        // At this point, the arrays are equal.
        return true;
    }
    /**
     * Compare two JSON objects for deep equality.
     */
    function deepObjectEqual(first, second) {
        // Check referential equality first.
        if (first === second) {
            return true;
        }
        // Check for the first object's keys in the second object.
        for (var key in first) {
            if (!(key in second)) {
                return false;
            }
        }
        // Check for the second object's keys in the first object.
        for (var key in second) {
            if (!(key in first)) {
                return false;
            }
        }
        // Compare the values for equality.
        for (var key in first) {
            if (!deepEqual(first[key], second[key])) {
                return false;
            }
        }
        // At this point, the objects are equal.
        return true;
    }
    /**
     * Create a deep copy of a JSON array.
     */
    function deepArrayCopy(value) {
        var result = new Array(value.length);
        for (var i = 0, n = value.length; i < n; ++i) {
            result[i] = deepCopy(value[i]);
        }
        return result;
    }
    /**
     * Create a deep copy of a JSON object.
     */
    function deepObjectCopy(value) {
        var result = {};
        for (var key in value) {
            result[key] = deepCopy(value[key]);
        }
        return result;
    }
})(JSONExt = exports.JSONExt || (exports.JSONExt = {}));
