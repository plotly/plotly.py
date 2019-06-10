import { IIterator, IterableOrArrayLike } from './iter';
/**
 * Filter an iterable for values which pass a test.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The predicate function to invoke for each value.
 *
 * @returns An iterator which yields the values which pass the test.
 *
 * #### Example
 * ```typescript
 * import { filter, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3, 4, 5, 6];
 *
 * let stream = filter(data, value => value % 2 === 0);
 *
 * toArray(stream);  // [2, 4, 6]
 * ```
 */
export declare function filter<T>(object: IterableOrArrayLike<T>, fn: (value: T, index: number) => boolean): IIterator<T>;
/**
 * An iterator which yields values which pass a test.
 */
export declare class FilterIterator<T> implements IIterator<T> {
    /**
     * Construct a new filter iterator.
     *
     * @param source - The iterator of values of interest.
     *
     * @param fn - The predicate function to invoke for each value.
     */
    constructor(source: IIterator<T>, fn: (value: T, index: number) => boolean);
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
    private _index;
    private _source;
    private _fn;
}
