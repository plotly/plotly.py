import { IIterator, IterableOrArrayLike } from './iter';
/**
 * Iterate several iterables in lockstep.
 *
 * @param objects - The iterable or array-like objects of interest.
 *
 * @returns An iterator which yields successive tuples of values where
 *   each value is taken in turn from the provided iterables. It will
 *   be as long as the shortest provided iterable.
 *
 * #### Example
 * ```typescript
 * import { zip, toArray } from '@phosphor/algorithm';
 *
 * let data1 = [1, 2, 3];
 * let data2 = [4, 5, 6];
 *
 * let stream = zip(data1, data2);
 *
 * toArray(stream);  // [[1, 4], [2, 5], [3, 6]]
 * ```
 */
export declare function zip<T>(...objects: IterableOrArrayLike<T>[]): IIterator<T[]>;
/**
 * An iterator which iterates several sources in lockstep.
 */
export declare class ZipIterator<T> implements IIterator<T[]> {
    /**
     * Construct a new zip iterator.
     *
     * @param source - The iterators of interest.
     */
    constructor(source: IIterator<T>[]);
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    iter(): IIterator<T[]>;
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    clone(): IIterator<T[]>;
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    next(): T[] | undefined;
    private _source;
}
