import { IIterator, IterableOrArrayLike } from './iter';
/**
 * Take a fixed number of items from an iterable.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param count - The number of items to take from the iterable.
 *
 * @returns An iterator which yields the specified number of items
 *   from the source iterable.
 *
 * #### Notes
 * The returned iterator will exhaust early if the source iterable
 * contains an insufficient number of items.
 */
export declare function take<T>(object: IterableOrArrayLike<T>, count: number): IIterator<T>;
/**
 * An iterator which takes a fixed number of items from a source.
 */
export declare class TakeIterator<T> implements IIterator<T> {
    /**
     * Construct a new take iterator.
     *
     * @param source - The iterator of interest.
     *
     * @param count - The number of items to take from the source.
     */
    constructor(source: IIterator<T>, count: number);
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
    private _count;
    private _source;
}
