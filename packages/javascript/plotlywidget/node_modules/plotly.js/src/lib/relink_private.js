/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var isArrayOrTypedArray = require('./array').isArrayOrTypedArray;
var isPlainObject = require('./is_plain_object');

/**
 * Relink private _keys and keys with a function value from one container
 * to the new container.
 * Relink means copying if object is pass-by-value and adding a reference
 * if object is pass-by-ref.
 * This prevents deepCopying massive structures like a webgl context.
 */
module.exports = function relinkPrivateKeys(toContainer, fromContainer) {
    for(var k in fromContainer) {
        var fromVal = fromContainer[k];
        var toVal = toContainer[k];

        if(toVal === fromVal) {
            continue;
        }
        if(k.charAt(0) === '_' || typeof fromVal === 'function') {
            // if it already exists at this point, it's something
            // that we recreate each time around, so ignore it
            if(k in toContainer) continue;

            toContainer[k] = fromVal;
        } else if(isArrayOrTypedArray(fromVal) && isArrayOrTypedArray(toVal) && isPlainObject(fromVal[0])) {
            // filter out data_array items that can contain user objects
            // most of the time the toVal === fromVal check will catch these early
            // but if the user makes new ones we also don't want to recurse in.
            if(k === 'customdata' || k === 'ids') continue;

            // recurse into arrays containers
            var minLen = Math.min(fromVal.length, toVal.length);
            for(var j = 0; j < minLen; j++) {
                if((toVal[j] !== fromVal[j]) && isPlainObject(fromVal[j]) && isPlainObject(toVal[j])) {
                    relinkPrivateKeys(toVal[j], fromVal[j]);
                }
            }
        } else if(isPlainObject(fromVal) && isPlainObject(toVal)) {
            // recurse into objects, but only if they still exist
            relinkPrivateKeys(toVal, fromVal);

            if(!Object.keys(toVal).length) delete toContainer[k];
        }
    }
};
