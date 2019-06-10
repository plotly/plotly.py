/**
 * A class which wraps a promise into a delegate object.
 *
 * #### Notes
 * This class is useful when the logic to resolve or reject a promise
 * cannot be defined at the point where the promise is created.
 */
export declare class PromiseDelegate<T> {
    /**
     * Construct a new promise delegate.
     */
    constructor();
    /**
     * The promise wrapped by the delegate.
     */
    readonly promise: Promise<T>;
    /**
     * Resolve the wrapped promise with the given value.
     *
     * @param value - The value to use for resolving the promise.
     */
    resolve(value: T | PromiseLike<T>): void;
    /**
     * Reject the wrapped promise with the given value.
     *
     * @reason - The reason for rejecting the promise.
     */
    reject(reason: any): void;
    private _resolve;
    private _reject;
}
