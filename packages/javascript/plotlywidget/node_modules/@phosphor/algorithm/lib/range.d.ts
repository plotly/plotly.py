import { IIterator } from './iter';
/**
 * Create an iterator of evenly spaced values.
 *
 * @param start - The starting value for the range, inclusive.
 *
 * @param stop - The stopping value for the range, exclusive.
 *
 * @param step - The distance between each value.
 *
 * @returns An iterator which produces evenly spaced values.
 *
 * #### Notes
 * In the single argument form of `range(stop)`, `start` defaults to
 * `0` and `step` defaults to `1`.
 *
 * In the two argument form of `range(start, stop)`, `step` defaults
 * to `1`.
 */
export declare function range(start: number, stop?: number, step?: number): IIterator<number>;
/**
 * An iterator which produces a range of evenly spaced values.
 */
export declare class RangeIterator implements IIterator<number> {
    /**
     * Construct a new range iterator.
     *
     * @param start - The starting value for the range, inclusive.
     *
     * @param stop - The stopping value for the range, exclusive.
     *
     * @param step - The distance between each value.
     */
    constructor(start: number, stop: number, step: number);
    /**
     * Get an iterator over the object's values.
     *
     * @returns An iterator which yields the object's values.
     */
    iter(): IIterator<number>;
    /**
     * Create an independent clone of the iterator.
     *
     * @returns A new independent clone of the iterator.
     */
    clone(): IIterator<number>;
    /**
     * Get the next value from the iterator.
     *
     * @returns The next value from the iterator, or `undefined`.
     */
    next(): number | undefined;
    private _index;
    private _length;
    private _start;
    private _stop;
    private _step;
}
