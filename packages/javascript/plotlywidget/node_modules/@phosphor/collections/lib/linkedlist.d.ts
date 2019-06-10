import { IIterable, IIterator, IRetroable, IterableOrArrayLike } from '@phosphor/algorithm';
/**
 * A generic doubly-linked list.
 */
export declare class LinkedList<T> implements IIterable<T>, IRetroable<T> {
    /**
     * Construct a new linked list.
     */
    constructor();
    /**
     * Whether the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    readonly isEmpty: boolean;
    /**
     * The length of the list.
     *
     * #### Complexity
     * Constant.
     */
    readonly length: number;
    /**
     * The first value in the list.
     *
     * This is `undefined` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    readonly first: T | undefined;
    /**
     * The last value in the list.
     *
     * This is `undefined` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    readonly last: T | undefined;
    /**
     * The first node in the list.
     *
     * This is `null` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    readonly firstNode: LinkedList.INode<T> | null;
    /**
     * The last node in the list.
     *
     * This is `null` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    readonly lastNode: LinkedList.INode<T> | null;
    /**
     * Create an iterator over the values in the list.
     *
     * @returns A new iterator starting with the first value.
     *
     * #### Complexity
     * Constant.
     */
    iter(): IIterator<T>;
    /**
     * Create a reverse iterator over the values in the list.
     *
     * @returns A new iterator starting with the last value.
     *
     * #### Complexity
     * Constant.
     */
    retro(): IIterator<T>;
    /**
     * Create an iterator over the nodes in the list.
     *
     * @returns A new iterator starting with the first node.
     *
     * #### Complexity
     * Constant.
     */
    nodes(): IIterator<LinkedList.INode<T>>;
    /**
     * Create a reverse iterator over the nodes in the list.
     *
     * @returns A new iterator starting with the last node.
     *
     * #### Complexity
     * Constant.
     */
    retroNodes(): IIterator<LinkedList.INode<T>>;
    /**
     * Add a value to the beginning of the list.
     *
     * @param value - The value to add to the beginning of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Complexity
     * Constant.
     */
    addFirst(value: T): LinkedList.INode<T>;
    /**
     * Add a value to the end of the list.
     *
     * @param value - The value to add to the end of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Complexity
     * Constant.
     */
    addLast(value: T): LinkedList.INode<T>;
    /**
     * Insert a value before a specific node in the list.
     *
     * @param value - The value to insert before the reference node.
     *
     * @param ref - The reference node of interest. If this is `null`,
     *   the value will be added to the beginning of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Notes
     * The reference node must be owned by the list.
     *
     * #### Complexity
     * Constant.
     */
    insertBefore(value: T, ref: LinkedList.INode<T> | null): LinkedList.INode<T>;
    /**
     * Insert a value after a specific node in the list.
     *
     * @param value - The value to insert after the reference node.
     *
     * @param ref - The reference node of interest. If this is `null`,
     *   the value will be added to the end of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Notes
     * The reference node must be owned by the list.
     *
     * #### Complexity
     * Constant.
     */
    insertAfter(value: T, ref: LinkedList.INode<T> | null): LinkedList.INode<T>;
    /**
     * Remove and return the value at the beginning of the list.
     *
     * @returns The removed value, or `undefined` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    removeFirst(): T | undefined;
    /**
     * Remove and return the value at the end of the list.
     *
     * @returns The removed value, or `undefined` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    removeLast(): T | undefined;
    /**
     * Remove a specific node from the list.
     *
     * @param node - The node to remove from the list.
     *
     * #### Complexity
     * Constant.
     *
     * #### Notes
     * The node must be owned by the list.
     */
    removeNode(node: LinkedList.INode<T>): void;
    /**
     * Remove all values from the list.
     *
     * #### Complexity
     * Linear.
     */
    clear(): void;
    private _first;
    private _last;
    private _length;
}
/**
 * The namespace for the `LinkedList` class statics.
 */
export declare namespace LinkedList {
    /**
     * An object which represents a node in a linked list.
     *
     * #### Notes
     * User code will not create linked list nodes directly. Nodes
     * are created automatically when values are added to a list.
     */
    interface INode<T> {
        /**
         * The linked list which created and owns the node.
         *
         * This will be `null` when the node is removed from the list.
         */
        readonly list: LinkedList<T> | null;
        /**
         * The next node in the list.
         *
         * This will be `null` when the node is the last node in the list
         * or when the node is removed from the list.
         */
        readonly next: INode<T> | null;
        /**
         * The previous node in the list.
         *
         * This will be `null` when the node is the first node in the list
         * or when the node is removed from the list.
         */
        readonly prev: INode<T> | null;
        /**
         * The user value stored in the node.
         */
        readonly value: T;
    }
    /**
     * Create a linked list from an iterable of values.
     *
     * @param values - The iterable or array-like object of interest.
     *
     * @returns A new linked list initialized with the given values.
     */
    function from<T>(values: IterableOrArrayLike<T>): LinkedList<T>;
    /**
     * A forward iterator for values in a linked list.
     */
    class ForwardValueIterator<T> implements IIterator<T> {
        /**
         * Construct a forward value iterator.
         *
         * @param node - The first node in the list.
         */
        constructor(node: INode<T> | null);
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
        private _node;
    }
    /**
     * A reverse iterator for values in a linked list.
     */
    class RetroValueIterator<T> implements IIterator<T> {
        /**
         * Construct a retro value iterator.
         *
         * @param node - The last node in the list.
         */
        constructor(node: INode<T> | null);
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
        private _node;
    }
    /**
     * A forward iterator for nodes in a linked list.
     */
    class ForwardNodeIterator<T> implements IIterator<INode<T>> {
        /**
         * Construct a forward node iterator.
         *
         * @param node - The first node in the list.
         */
        constructor(node: INode<T> | null);
        /**
         * Get an iterator over the object's values.
         *
         * @returns An iterator which yields the object's values.
         */
        iter(): IIterator<INode<T>>;
        /**
         * Create an independent clone of the iterator.
         *
         * @returns A new independent clone of the iterator.
         */
        clone(): IIterator<INode<T>>;
        /**
         * Get the next value from the iterator.
         *
         * @returns The next value from the iterator, or `undefined`.
         */
        next(): INode<T> | undefined;
        private _node;
    }
    /**
     * A reverse iterator for nodes in a linked list.
     */
    class RetroNodeIterator<T> implements IIterator<INode<T>> {
        /**
         * Construct a retro node iterator.
         *
         * @param node - The last node in the list.
         */
        constructor(node: INode<T> | null);
        /**
         * Get an iterator over the object's values.
         *
         * @returns An iterator which yields the object's values.
         */
        iter(): IIterator<INode<T>>;
        /**
         * Create an independent clone of the iterator.
         *
         * @returns A new independent clone of the iterator.
         */
        clone(): IIterator<INode<T>>;
        /**
         * Get the next value from the iterator.
         *
         * @returns The next value from the iterator, or `undefined`.
         */
        next(): INode<T> | undefined;
        private _node;
    }
}
