/**
 * A generic interface for change emitter payloads.
 */
export interface IChangedArgs<T> {
    /**
     * The name of the changed attribute.
     */
    name: string;
    /**
     * The old value of the changed attribute.
     */
    oldValue: T;
    /**
     * The new value of the changed attribute.
     */
    newValue: T;
}
/**
 * The description of a general purpose data connector.
 */
export interface IDataConnector<T, U = T, V = string> {
    /**
     * Retrieve an item from the data connector.
     *
     * @param id - The identifier used to retrieve an item.
     *
     * @returns A promise that bears a data payload if available.
     *
     * #### Notes
     * The promise returned by this method may be rejected if an error occurs in
     * retrieving the data. Nonexistence of an `id` will succeed with `undefined`.
     */
    fetch(id: V): Promise<T | undefined>;
    /**
     * Remove a value using the data connector.
     *
     * @param id - The identifier for the data being removed.
     *
     * @returns A promise that is rejected if remove fails and succeeds otherwise.
     */
    remove(id: V): Promise<void>;
    /**
     * Save a value using the data connector.
     *
     * @param id - The identifier for the data being saved.
     *
     * @param value - The data being saved.
     *
     * @returns A promise that is rejected if saving fails and succeeds otherwise.
     */
    save(id: V, value: U): Promise<void>;
}
