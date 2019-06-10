"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var signaling_1 = require("@phosphor/signaling");
/**
 * An object which holds data related to an object's title.
 *
 * #### Notes
 * A title object is intended to hold the data necessary to display a
 * header for a particular object. A common example is the `TabPanel`,
 * which uses the widget title to populate the tab for a child widget.
 */
var Title = (function () {
    /**
     * Construct a new title.
     *
     * @param options - The options for initializing the title.
     */
    function Title(options) {
        this._label = '';
        this._caption = '';
        this._mnemonic = -1;
        this._iconClass = '';
        this._iconLabel = '';
        this._className = '';
        this._closable = false;
        this._changed = new signaling_1.Signal(this);
        this.owner = options.owner;
        if (options.label !== undefined) {
            this._label = options.label;
        }
        if (options.mnemonic !== undefined) {
            this._mnemonic = options.mnemonic;
        }
        if (options.icon !== undefined) {
            this._iconClass = options.icon;
        }
        if (options.iconClass !== undefined) {
            this._iconClass = options.iconClass;
        }
        if (options.iconLabel !== undefined) {
            this._iconLabel = options.iconLabel;
        }
        if (options.caption !== undefined) {
            this._caption = options.caption;
        }
        if (options.className !== undefined) {
            this._className = options.className;
        }
        if (options.closable !== undefined) {
            this._closable = options.closable;
        }
        this._dataset = options.dataset || {};
    }
    Object.defineProperty(Title.prototype, "changed", {
        /**
         * A signal emitted when the state of the title changes.
         */
        get: function () {
            return this._changed;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "label", {
        /**
         * Get the label for the title.
         *
         * #### Notes
         * The default value is an empty string.
         */
        get: function () {
            return this._label;
        },
        /**
         * Set the label for the title.
         */
        set: function (value) {
            if (this._label === value) {
                return;
            }
            this._label = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "mnemonic", {
        /**
         * Get the mnemonic index for the title.
         *
         * #### Notes
         * The default value is `-1`.
         */
        get: function () {
            return this._mnemonic;
        },
        /**
         * Set the mnemonic index for the title.
         */
        set: function (value) {
            if (this._mnemonic === value) {
                return;
            }
            this._mnemonic = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "icon", {
        /**
         * @deprecated Use `iconClass` instead.
         */
        get: function () {
            return this.iconClass;
        },
        /**
         * @deprecated Use `iconClass` instead.
         */
        set: function (value) {
            this.iconClass = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "iconClass", {
        /**
         * Get the icon class name for the title.
         *
         * #### Notes
         * The default value is an empty string.
         */
        get: function () {
            return this._iconClass;
        },
        /**
         * Set the icon class name for the title.
         *
         * #### Notes
         * Multiple class names can be separated with whitespace.
         */
        set: function (value) {
            if (this._iconClass === value) {
                return;
            }
            this._iconClass = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "iconLabel", {
        /**
         * Get the icon label for the title.
         *
         * #### Notes
         * The default value is an empty string.
         */
        get: function () {
            return this._iconLabel;
        },
        /**
         * Set the icon label for the title.
         *
         * #### Notes
         * Multiple class names can be separated with whitespace.
         */
        set: function (value) {
            if (this._iconLabel === value) {
                return;
            }
            this._iconLabel = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "caption", {
        /**
         * Get the caption for the title.
         *
         * #### Notes
         * The default value is an empty string.
         */
        get: function () {
            return this._caption;
        },
        /**
         * Set the caption for the title.
         */
        set: function (value) {
            if (this._caption === value) {
                return;
            }
            this._caption = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "className", {
        /**
         * Get the extra class name for the title.
         *
         * #### Notes
         * The default value is an empty string.
         */
        get: function () {
            return this._className;
        },
        /**
         * Set the extra class name for the title.
         *
         * #### Notes
         * Multiple class names can be separated with whitespace.
         */
        set: function (value) {
            if (this._className === value) {
                return;
            }
            this._className = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "closable", {
        /**
         * Get the closable state for the title.
         *
         * #### Notes
         * The default value is `false`.
         */
        get: function () {
            return this._closable;
        },
        /**
         * Set the closable state for the title.
         *
         * #### Notes
         * This controls the presence of a close icon when applicable.
         */
        set: function (value) {
            if (this._closable === value) {
                return;
            }
            this._closable = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Title.prototype, "dataset", {
        /**
         * Get the dataset for the title.
         *
         * #### Notes
         * The default value is an empty dataset.
         */
        get: function () {
            return this._dataset;
        },
        /**
         * Set the dataset for the title.
         *
         * #### Notes
         * This controls the data attributes when applicable.
         */
        set: function (value) {
            if (this._dataset === value) {
                return;
            }
            this._dataset = value;
            this._changed.emit(undefined);
        },
        enumerable: true,
        configurable: true
    });
    return Title;
}());
exports.Title = Title;
