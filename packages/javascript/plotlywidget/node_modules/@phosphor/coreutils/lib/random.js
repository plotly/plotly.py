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
 * The namespace for random number related functionality.
 */
var Random;
(function (Random) {
    /**
     * A function which generates random bytes.
     *
     * @param buffer - The `Uint8Array` to fill with random bytes.
     *
     * #### Notes
     * A cryptographically strong random number generator will be used if
     * available. Otherwise, `Math.random` will be used as a fallback for
     * randomness.
     *
     * The following RNGs are supported, listed in order of precedence:
     *   - `window.crypto.getRandomValues`
     *   - `window.msCrypto.getRandomValues`
     *   - `require('crypto').randomFillSync
     *   - `require('crypto').randomBytes
     *   - `Math.random`
     */
    Random.getRandomValues = (function () {
        // Look up the crypto module if available.
        var crypto = ((typeof window !== 'undefined' && (window.crypto || window.msCrypto)) ||
            (typeof require !== 'undefined' && require('crypto')) || null);
        // Modern browsers and IE 11
        if (crypto && typeof crypto.getRandomValues === 'function') {
            return function getRandomValues(buffer) {
                return crypto.getRandomValues(buffer);
            };
        }
        // Node 7+
        if (crypto && typeof crypto.randomFillSync === 'function') {
            return function getRandomValues(buffer) {
                return crypto.randomFillSync(buffer);
            };
        }
        // Node 0.10+
        if (crypto && typeof crypto.randomBytes === 'function') {
            return function getRandomValues(buffer) {
                var bytes = crypto.randomBytes(buffer.length);
                for (var i = 0, n = bytes.length; i < n; ++i) {
                    buffer[i] = bytes[i];
                }
            };
        }
        // Fallback
        return function getRandomValues(buffer) {
            var value = 0;
            for (var i = 0, n = buffer.length; i < n; ++i) {
                if (i % 4 === 0) {
                    value = Math.random() * 0xFFFFFFFF >>> 0;
                }
                buffer[i] = value & 0xFF;
                value >>>= 8;
            }
        };
    })();
})(Random = exports.Random || (exports.Random = {}));
