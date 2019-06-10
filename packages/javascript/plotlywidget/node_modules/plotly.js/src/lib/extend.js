/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isPlainObject = require('./is_plain_object.js');
var isArray = Array.isArray;

function primitivesLoopSplice(source, target) {
    var i, value;
    for(i = 0; i < source.length; i++) {
        value = source[i];
        if(value !== null && typeof(value) === 'object') {
            return false;
        }
        if(value !== void(0)) {
            target[i] = value;
        }
    }
    return true;
}

exports.extendFlat = function() {
    return _extend(arguments, false, false, false);
};

exports.extendDeep = function() {
    return _extend(arguments, true, false, false);
};

exports.extendDeepAll = function() {
    return _extend(arguments, true, true, false);
};

exports.extendDeepNoArrays = function() {
    return _extend(arguments, true, false, true);
};

/*
 * Inspired by https://github.com/justmoon/node-extend/blob/master/index.js
 * All credit to the jQuery authors for perfecting this amazing utility.
 *
 * API difference with jQuery version:
 * - No optional boolean (true -> deep extend) first argument,
 *   use `extendFlat` for first-level only extend and
 *   use `extendDeep` for a deep extend.
 *
 * Other differences with jQuery version:
 * - Uses a modern (and faster) isPlainObject routine.
 * - Expected to work with object {} and array [] arguments only.
 * - Does not check for circular structure.
 *   FYI: jQuery only does a check across one level.
 *   Warning: this might result in infinite loops.
 *
 */
function _extend(inputs, isDeep, keepAllKeys, noArrayCopies) {
    var target = inputs[0];
    var length = inputs.length;

    var input, key, src, copy, copyIsArray, clone, allPrimitives;

    // TODO does this do the right thing for typed arrays?

    if(length === 2 && isArray(target) && isArray(inputs[1]) && target.length === 0) {
        allPrimitives = primitivesLoopSplice(inputs[1], target);

        if(allPrimitives) {
            return target;
        } else {
            target.splice(0, target.length); // reset target and continue to next block
        }
    }

    for(var i = 1; i < length; i++) {
        input = inputs[i];

        for(key in input) {
            src = target[key];
            copy = input[key];

            if(noArrayCopies && isArray(copy)) {
                // Stop early and just transfer the array if array copies are disallowed:

                target[key] = copy;
            } else if(isDeep && copy && (isPlainObject(copy) || (copyIsArray = isArray(copy)))) {
                // recurse if we're merging plain objects or arrays

                if(copyIsArray) {
                    copyIsArray = false;
                    clone = src && isArray(src) ? src : [];
                } else {
                    clone = src && isPlainObject(src) ? src : {};
                }

                // never move original objects, clone them
                target[key] = _extend([clone, copy], isDeep, keepAllKeys, noArrayCopies);
            } else if(typeof copy !== 'undefined' || keepAllKeys) {
                // don't bring in undefined values, except for extendDeepAll

                target[key] = copy;
            }
        }
    }

    return target;
}
