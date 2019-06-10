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
 * A class which attaches a value to an external object.
 *
 * #### Notes
 * Attached properties are used to extend the state of an object with
 * semantic data from an unrelated class. They also encapsulate value
 * creation, coercion, and notification.
 *
 * Because attached property values are stored in a hash table, which
 * in turn is stored in a WeakMap keyed on the owner object, there is
 * non-trivial storage overhead involved in their use. The pattern is
 * therefore best used for the storage of rare data.
 */
var AttachedProperty = (function () {
    /**
     * Construct a new attached property.
     *
     * @param options - The options for initializing the property.
     */
    function AttachedProperty(options) {
        this._pid = Private.nextPID();
        this.name = options.name;
        this._create = options.create;
        this._coerce = options.coerce || null;
        this._compare = options.compare || null;
        this._changed = options.changed || null;
    }
    /**
     * Get the current value of the property for a given owner.
     *
     * @param owner - The property owner of interest.
     *
     * @returns The current value of the property.
     *
     * #### Notes
     * If the value has not yet been set, the default value will be
     * computed and assigned as the current value of the property.
     */
    AttachedProperty.prototype.get = function (owner) {
        var value;
        var map = Private.ensureMap(owner);
        if (this._pid in map) {
            value = map[this._pid];
        }
        else {
            value = map[this._pid] = this._createValue(owner);
        }
        return value;
    };
    /**
     * Set the current value of the property for a given owner.
     *
     * @param owner - The property owner of interest.
     *
     * @param value - The value for the property.
     *
     * #### Notes
     * If the value has not yet been set, the default value will be
     * computed and used as the previous value for the comparison.
     */
    AttachedProperty.prototype.set = function (owner, value) {
        var oldValue;
        var map = Private.ensureMap(owner);
        if (this._pid in map) {
            oldValue = map[this._pid];
        }
        else {
            oldValue = map[this._pid] = this._createValue(owner);
        }
        var newValue = this._coerceValue(owner, value);
        this._maybeNotify(owner, oldValue, map[this._pid] = newValue);
    };
    /**
     * Explicitly coerce the current property value for a given owner.
     *
     * @param owner - The property owner of interest.
     *
     * #### Notes
     * If the value has not yet been set, the default value will be
     * computed and used as the previous value for the comparison.
     */
    AttachedProperty.prototype.coerce = function (owner) {
        var oldValue;
        var map = Private.ensureMap(owner);
        if (this._pid in map) {
            oldValue = map[this._pid];
        }
        else {
            oldValue = map[this._pid] = this._createValue(owner);
        }
        var newValue = this._coerceValue(owner, oldValue);
        this._maybeNotify(owner, oldValue, map[this._pid] = newValue);
    };
    /**
     * Get or create the default value for the given owner.
     */
    AttachedProperty.prototype._createValue = function (owner) {
        var create = this._create;
        return create(owner);
    };
    /**
     * Coerce the value for the given owner.
     */
    AttachedProperty.prototype._coerceValue = function (owner, value) {
        var coerce = this._coerce;
        return coerce ? coerce(owner, value) : value;
    };
    /**
     * Compare the old value and new value for equality.
     */
    AttachedProperty.prototype._compareValue = function (oldValue, newValue) {
        var compare = this._compare;
        return compare ? compare(oldValue, newValue) : oldValue === newValue;
    };
    /**
     * Run the change notification if the given values are different.
     */
    AttachedProperty.prototype._maybeNotify = function (owner, oldValue, newValue) {
        var changed = this._changed;
        if (changed && !this._compareValue(oldValue, newValue)) {
            changed(owner, oldValue, newValue);
        }
    };
    return AttachedProperty;
}());
exports.AttachedProperty = AttachedProperty;
/**
 * The namespace for the `AttachedProperty` class statics.
 */
(function (AttachedProperty) {
    /**
     * Clear the stored property data for the given owner.
     *
     * @param owner - The property owner of interest.
     *
     * #### Notes
     * This will clear all property values for the owner, but it will
     * **not** run the change notification for any of the properties.
     */
    function clearData(owner) {
        Private.ownerData.delete(owner);
    }
    AttachedProperty.clearData = clearData;
})(AttachedProperty = exports.AttachedProperty || (exports.AttachedProperty = {}));
exports.AttachedProperty = AttachedProperty;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * A weak mapping of property owner to property map.
     */
    Private.ownerData = new WeakMap();
    /**
     * A function which computes successive unique property ids.
     */
    Private.nextPID = (function () {
        var id = 0;
        return function () {
            var rand = Math.random();
            var stem = ("" + rand).slice(2);
            return "pid-" + stem + "-" + id++;
        };
    })();
    /**
     * Lookup the data map for the property owner.
     *
     * This will create the map if one does not already exist.
     */
    function ensureMap(owner) {
        var map = Private.ownerData.get(owner);
        if (map) {
            return map;
        }
        map = Object.create(null);
        Private.ownerData.set(owner, map);
        return map;
    }
    Private.ensureMap = ensureMap;
})(Private || (Private = {}));
