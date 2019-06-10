import { IIterator, IterableOrArrayLike } from './iter';
/**
 * Chain together several iterables.
 *
 * @param objects - The iterable or array-like objects of interest.
 *
 * @returns An iterator which yields the values of the iterables
 *   in the order in which they are supplied.
 *
 * #### Example
 * ```typescript
 * import { chain, toArray } from '@phosphor/algorithm';
 *
 * let data1 = [1, 2, 3];
 * let data2 = [4, 5, 6];
 *
 * let stream = chain(data1, data2);
 *
 * toArray(stream);  // [1, 2, 3, 4, 5, 6]
 * ```
 */
export declare function chain<T>(...objects: IterableOrArrayLike<T>[]): IIterator<T>;
/**
 * An iterator which chains together several iterators.
 */
export declare class ChainIterator<T> implements IIterator<T> {
    /**
     * Construct a new chain iterator.
     *
     * @param source - The iterator of iterators of interest.
     */
    constructor(source: IIterator<IIterator<T>>);
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    iter(): IIterator<T>;
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    clone(): IIterator<T>;
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    next(): T | undefined;
    private _source;
    private _active;
    private _cloned;
}
