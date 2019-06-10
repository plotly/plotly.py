import { IterableOrArrayLike } from '@phosphor/algorithm';
/**
 * An object which implements the disposable pattern.
 */
export interface IDisposable {
    /**
     * Test whether the object has been disposed.
     *
     * #### Notes
     * This property is always safe to access.
     */
    readonly isDisposed: boolean;
    /**
     * Dispose of the resources held by the object.
     *
     * #### Notes
     * If the object's `dispose` method is called more than once, all
     * calls made after the first will be a no-op.
     *
     * #### Undefined Behavior
     * It is undefined behavior to use any functionality of the object
     * after it has been disposed unless otherwise explicitly noted.
     */
    dispose(): void;
}
/**
 * A disposable object which delegates to a callback function.
 */
export declare class DisposableDelegate implements IDisposable {
    /**
     * Construct a new disposable delegate.
     *
     * @param fn - The callback function to invoke on dispose.
     */
    constructor(fn: () => void);
    /**
     * Test whether the delegate has been disposed.
     */
    readonly isDisposed: boolean;
    /**
     * Dispose of the delegate and invoke the callback function.
     */
    dispose(): void;
    private _fn;
}
/**
 * An object which manages a collection of disposable items.
 */
export declare class DisposableSet implements IDisposable {
    /**
     * Construct a new disposable set.
     */
    constructor();
    /**
     * Test whether the set has been disposed.
     */
    readonly isDisposed: boolean;
    /**
     * Dispose of the set and the items it contains.
     *
     * #### Notes
     * Items are disposed in the order they are added to the set.
     */
    dispose(): void;
    /**
     * Test whether the set contains a specific item.
     *
     * @param item - The item of interest.
     *
     * @returns `true` if the set contains the item, `false` otherwise.
     */
    contains(item: IDisposable): boolean;
    /**
     * Add a disposable item to the set.
     *
     * @param item - The item to add to the set.
     *
     * #### Notes
     * If the item is already contained in the set, this is a no-op.
     */
    add(item: IDisposable): void;
    /**
     * Remove a disposable item from the set.
     *
     * @param item - The item to remove from the set.
     *
     * #### Notes
     * If the item is not contained in the set, this is a no-op.
     */
    remove(item: IDisposable): void;
    /**
     * Remove all items from the set.
     */
    clear(): void;
    private _disposed;
    private _items;
}
/**
 * The namespace for the `DisposableSet` class statics.
 */
export declare namespace DisposableSet {
    /**
     * Create a disposable set from an iterable of items.
     *
     * @param items - The iterable or array-like object of interest.
     *
     * @returns A new disposable initialized with the given items.
     */
    function from(items: IterableOrArrayLike<IDisposable>): DisposableSet;
}
