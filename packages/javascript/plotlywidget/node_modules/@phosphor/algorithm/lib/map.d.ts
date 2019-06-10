import { IIterator, IterableOrArrayLike } from './iter';
/**
 * Transform the values of an iterable with a mapping function.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The mapping function to invoke for each value.
 *
 * @returns An iterator which yields the transformed values.
 *
 * #### Example
 * ```typescript
 * import { map, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3];
 *
 * let stream = map(data, value => value * 2);
 *
 * toArray(stream);  // [2, 4, 6]
 * ```
 */
export declare function map<T, U>(object: IterableOrArrayLike<T>, fn: (value: T, index: number) => U): IIterator<U>;
/**
 * An iterator which transforms values using a mapping function.
 */
export declare class MapIterator<T, U> implements IIterator<U> {
    /**
     * Construct a new map iterator.
     *
     * @param source - The iterator of values of interest.
     *
     * @param fn - The mapping function to invoke for each value.
     */
    constructor(source: IIterator<T>, fn: (value: T, index: number) => U);
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    iter(): IIterator<U>;
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    clone(): IIterator<U>;
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    next(): U | undefined;
    private _index;
    private _source;
    private _fn;
}
