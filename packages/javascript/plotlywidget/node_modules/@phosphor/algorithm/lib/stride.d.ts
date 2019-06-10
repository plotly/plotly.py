import { IIterator, IterableOrArrayLike } from './iter';
/**
 * Iterate over an iterable using a stepped increment.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param step - The distance to step on each iteration. A value
 *   of less than `1` will behave the same as a value of `1`.
 *
 * @returns An iterator which traverses the iterable step-wise.
 *
 * #### Example
 * ```typescript
 * import { stride, toArray } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3, 4, 5, 6];
 *
 * let stream = stride(data, 2);
 *
 * toArray(stream);  // [1, 3, 5];
 * ```
 */
export declare function stride<T>(object: IterableOrArrayLike<T>, step: number): IIterator<T>;
/**
 * An iterator which traverses a source iterator step-wise.
 */
export declare class StrideIterator<T> implements IIterator<T> {
    /**
     * Construct a new stride iterator.
     *
     * @param source - The iterator of values of interest.
     *
     * @param step - The distance to step on each iteration. A value
     *   of less than `1` will behave the same as a value of `1`.
     */
    constructor(source: IIterator<T>, step: number);
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
    private _step;
}
