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
export declare class AttachedProperty<T, U> {
    /**
     * Construct a new attached property.
     *
     * @param options - The options for initializing the property.
     */
    constructor(options: AttachedProperty.IOptions<T, U>);
    /**
     * The human readable name for the property.
     */
    readonly name: string;
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
    get(owner: T): U;
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
    set(owner: T, value: U): void;
    /**
     * Explicitly coerce the current property value for a given owner.
     *
     * @param owner - The property owner of interest.
     *
     * #### Notes
     * If the value has not yet been set, the default value will be
     * computed and used as the previous value for the comparison.
     */
    coerce(owner: T): void;
    /**
     * Get or create the default value for the given owner.
     */
    private _createValue(owner);
    /**
     * Coerce the value for the given owner.
     */
    private _coerceValue(owner, value);
    /**
     * Compare the old value and new value for equality.
     */
    private _compareValue(oldValue, newValue);
    /**
     * Run the change notification if the given values are different.
     */
    private _maybeNotify(owner, oldValue, newValue);
    private _pid;
    private _create;
    private _coerce;
    private _compare;
    private _changed;
}
/**
 * The namespace for the `AttachedProperty` class statics.
 */
export declare namespace AttachedProperty {
    /**
     * The options object used to initialize an attached property.
     */
    interface IOptions<T, U> {
        /**
         * The human readable name for the property.
         *
         * #### Notes
         * By convention, this should be the same as the name used to define
         * the public accessor for the property value.
         *
         * This **does not** have an effect on the property lookup behavior.
         * Multiple properties may share the same name without conflict.
         */
        name: string;
        /**
         * A factory function used to create the default property value.
         *
         * #### Notes
         * This will be called whenever the property value is required,
         * but has not yet been set for a given owner.
         */
        create: (owner: T) => U;
        /**
         * A function used to coerce a supplied value into the final value.
         *
         * #### Notes
         * This will be called whenever the property value is changed, or
         * when the property is explicitly coerced. The return value will
         * be used as the final value of the property.
         *
         * This will **not** be called for the initial default value.
         */
        coerce?: (owner: T, value: U) => U;
        /**
         * A function used to compare two values for equality.
         *
         * #### Notes
         * This is called to determine if the property value has changed.
         * It should return `true` if the given values are equivalent, or
         * `false` if they are different.
         *
         * If this is not provided, it defaults to the `===` operator.
         */
        compare?: (oldValue: U, newValue: U) => boolean;
        /**
         * A function called when the property value has changed.
         *
         * #### Notes
         * This will be invoked when the property value is changed and the
         * comparator indicates that the old value is not equal to the new
         * value.
         *
         * This will **not** be called for the initial default value.
         */
        changed?: (owner: T, oldValue: U, newValue: U) => void;
    }
    /**
     * Clear the stored property data for the given owner.
     *
     * @param owner - The property owner of interest.
     *
     * #### Notes
     * This will clear all property values for the owner, but it will
     * **not** run the change notification for any of the properties.
     */
    function clearData(owner: any): void;
}
