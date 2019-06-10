"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var random_1 = require("./random");
/**
 * The namespace for UUID related functionality.
 */
var UUID;
(function (UUID) {
    /**
     * A function which generates UUID v4 identifiers.
     *
     * @returns A new UUID v4 string.
     *
     * #### Notes
     * This implementation complies with RFC 4122.
     *
     * This uses `Random.getRandomValues()` for random bytes, which in
     * turn will use the underlying `crypto` module of the platform if
     * it is available. The fallback for randomness is `Math.random`.
     */
    UUID.uuid4 = (function () {
        // Create a 16 byte array to hold the random values.
        var bytes = new Uint8Array(16);
        // Create a look up table from bytes to hex strings.
        var lut = new Array(256);
        // Pad the single character hex digits with a leading zero.
        for (var i = 0; i < 16; ++i) {
            lut[i] = '0' + i.toString(16);
        }
        // Populate the rest of the hex digits.
        for (var i = 16; i < 256; ++i) {
            lut[i] = i.toString(16);
        }
        // Return a function which generates the UUID.
        return function uuid4() {
            // Get a new batch of random values.
            random_1.Random.getRandomValues(bytes);
            // Set the UUID version number to 4.
            bytes[6] = 0x40 | (bytes[6] & 0x0F);
            // Set the clock sequence bit to the RFC spec.
            bytes[8] = 0x80 | (bytes[8] & 0x3F);
            // Assemble the UUID string.
            return (lut[bytes[0]] +
                lut[bytes[1]] +
                lut[bytes[2]] +
                lut[bytes[3]] +
                '-' +
                lut[bytes[4]] +
                lut[bytes[5]] +
                '-' +
                lut[bytes[6]] +
                lut[bytes[7]] +
                '-' +
                lut[bytes[8]] +
                lut[bytes[9]] +
                '-' +
                lut[bytes[10]] +
                lut[bytes[11]] +
                lut[bytes[12]] +
                lut[bytes[13]] +
                lut[bytes[14]] +
                lut[bytes[15]]);
        };
    })();
})(UUID = exports.UUID || (exports.UUID = {}));
