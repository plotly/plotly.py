import { IterableOrArrayLike } from './iter';
/**
 * Summarize all values in an iterable using a reducer function.
 *
 * @param object - The iterable or array-like object of interest.
 *
 * @param fn - The reducer function to invoke for each value.
 *
 * @param initial - The initial value to start accumulation.
 *
 * @returns The final accumulated value.
 *
 * #### Notes
 * The `reduce` function follows the conventions of `Array#reduce`.
 *
 * If the iterator is empty, an initial value is required. That value
 * will be used as the return value. If no initial value is provided,
 * an error will be thrown.
 *
 * If the iterator contains a single item and no initial value is
 * provided, the single item is used as the return value.
 *
 * Otherwise, the reducer is invoked for each element in the iterable.
 * If an initial value is not provided, the first element will be used
 * as the initial accumulated value.
 *
 * #### Complexity
 * Linear.
 *
 * #### Example
 * ```typescript
 * import { reduce } from '@phosphor/algorithm';
 *
 * let data = [1, 2, 3, 4, 5];
 *
 * let sum = reduce(data, (a, value) => a + value);  // 15
 * ```
 */
export declare function reduce<T>(object: IterableOrArrayLike<T>, fn: (accumulator: T, value: T, index: number) => T): T;
export declare function reduce<T, U>(object: IterableOrArrayLike<T>, fn: (accumulator: U, value: T, index: number) => U, initial: U): U;
