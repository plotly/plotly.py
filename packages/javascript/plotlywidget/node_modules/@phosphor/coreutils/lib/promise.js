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
 * A class which wraps a promise into a delegate object.
 *
 * #### Notes
 * This class is useful when the logic to resolve or reject a promise
 * cannot be defined at the point where the promise is created.
 */
var PromiseDelegate = (function () {
    /**
     * Construct a new promise delegate.
     */
    function PromiseDelegate() {
        var _this = this;
        this.promise = new Promise(function (resolve, reject) {
            _this._resolve = resolve;
            _this._reject = reject;
        });
    }
    /**
     * Resolve the wrapped promise with the given value.
     *
     * @param value - The value to use for resolving the promise.
     */
    PromiseDelegate.prototype.resolve = function (value) {
        var resolve = this._resolve;
        resolve(value);
    };
    /**
     * Reject the wrapped promise with the given value.
     *
     * @reason - The reason for rejecting the promise.
     */
    PromiseDelegate.prototype.reject = function (reason) {
        var reject = this._reject;
        reject(reason);
    };
    return PromiseDelegate;
}());
exports.PromiseDelegate = PromiseDelegate;
