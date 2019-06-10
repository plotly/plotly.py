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
 * An object which stores MIME data for general application use.
 *
 * #### Notes
 * This class does not attempt to enforce "correctness" of MIME types
 * and their associated data. Since this class is designed to transfer
 * arbitrary data and objects within the same application, it assumes
 * that the user provides correct and accurate data.
 */
var MimeData = (function () {
    function MimeData() {
        this._types = [];
        this._values = [];
    }
    /**
     * Get an array of the MIME types contained within the dataset.
     *
     * @returns A new array of the MIME types, in order of insertion.
     */
    MimeData.prototype.types = function () {
        return this._types.slice();
    };
    /**
     * Test whether the dataset has an entry for the given type.
     *
     * @param mime - The MIME type of interest.
     *
     * @returns `true` if the dataset contains a value for the given
     *   MIME type, `false` otherwise.
     */
    MimeData.prototype.hasData = function (mime) {
        return this._types.indexOf(mime) !== -1;
    };
    /**
     * Get the data value for the given MIME type.
     *
     * @param mime - The MIME type of interest.
     *
     * @returns The value for the given MIME type, or `undefined` if
     *   the dataset does not contain a value for the type.
     */
    MimeData.prototype.getData = function (mime) {
        var i = this._types.indexOf(mime);
        return i !== -1 ? this._values[i] : undefined;
    };
    /**
     * Set the data value for the given MIME type.
     *
     * @param mime - The MIME type of interest.
     *
     * @param data - The data value for the given MIME type.
     *
     * #### Notes
     * This will overwrite any previous entry for the MIME type.
     */
    MimeData.prototype.setData = function (mime, data) {
        this.clearData(mime);
        this._types.push(mime);
        this._values.push(data);
    };
    /**
     * Remove the data entry for the given MIME type.
     *
     * @param mime - The MIME type of interest.
     *
     * #### Notes
     * This is a no-op if there is no entry for the given MIME type.
     */
    MimeData.prototype.clearData = function (mime) {
        var i = this._types.indexOf(mime);
        if (i !== -1) {
            this._types.splice(i, 1);
            this._values.splice(i, 1);
        }
    };
    /**
     * Remove all data entries from the dataset.
     */
    MimeData.prototype.clear = function () {
        this._types.length = 0;
        this._values.length = 0;
    };
    return MimeData;
}());
exports.MimeData = MimeData;
