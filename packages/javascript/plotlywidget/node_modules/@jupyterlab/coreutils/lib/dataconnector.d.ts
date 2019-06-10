import { IDataConnector } from './interfaces';
/**
 * An abstract class that adheres to the data connector interface.
 *
 * #### Notes
 * The only abstract method in this class is the `fetch` method, which must be
 * reimplemented by all subclasses. The `remove` and `save` methods have a
 * default implementation that returns a promise that will always reject. This
 * class is a convenience superclass for connectors that only need to `fetch`.
 */
export declare abstract class DataConnector<T, U = T, V = string> implements IDataConnector<T, U, V> {
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
    abstract fetch(id: V): Promise<T | undefined>;
    /**
     * Remove a value using the data connector.
     *
     * @param id - The identifier for the data being removed.
     *
     * @returns A promise that is rejected if remove fails and succeeds otherwise.
     *
     * #### Notes
     * This method will always reject; subclasses should reimplement it if they
     * support a back-end that can remove resources.
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
     *
     * #### Notes
     * This method will always reject; subclasses should reimplement it if they
     * support a back-end that can save resources.
     */
    save(id: V, value: U): Promise<void>;
}
