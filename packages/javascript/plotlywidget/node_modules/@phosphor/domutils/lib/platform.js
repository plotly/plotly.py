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
 * The namespace for platform related utilities.
 */
var Platform;
(function (Platform) {
    /**
     * A flag indicating whether the platform is Mac.
     */
    Platform.IS_MAC = !!navigator.platform.match(/Mac/i);
    /**
     * A flag indicating whether the platform is Windows.
     */
    Platform.IS_WIN = !!navigator.platform.match(/Win/i);
    /**
     * A flag indicating whether the browser is IE.
     */
    Platform.IS_IE = /Trident/.test(navigator.userAgent);
    /**
     * A flag indicating whether the browser is Edge.
     */
    Platform.IS_EDGE = /Edge/.test(navigator.userAgent);
})(Platform = exports.Platform || (exports.Platform = {}));
