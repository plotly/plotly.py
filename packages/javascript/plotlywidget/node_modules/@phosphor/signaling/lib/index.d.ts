/**
 * A type alias for a slot function.
 *
 * @param sender - The object emitting the signal.
 *
 * @param args - The args object emitted with the signal.
 *
 * #### Notes
 * A slot is invoked when a signal to which it is connected is emitted.
 */
export declare type Slot<T, U> = (sender: T, args: U) => void;
/**
 * An object used for type-safe inter-object communication.
 *
 * #### Notes
 * Signals provide a type-safe implementation of the publish-subscribe
 * pattern. An object (publisher) declares which signals it will emit,
 * and consumers connect callbacks (subscribers) to those signals. The
 * subscribers are invoked whenever the publisher emits the signal.
 */
export interface ISignal<T, U> {
    /**
     * Connect a slot to the signal.
     *
     * @param slot - The slot to invoke when the signal is emitted.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection succeeds, `false` otherwise.
     *
     * #### Notes
     * Slots are invoked in the order in which they are connected.
     *
     * Signal connections are unique. If a connection already exists for
     * the given `slot` and `thisArg`, this method returns `false`.
     *
     * A newly connected slot will not be invoked until the next time the
     * signal is emitted, even if the slot is connected while the signal
     * is dispatching.
     */
    connect(slot: Slot<T, U>, thisArg?: any): boolean;
    /**
     * Disconnect a slot from the signal.
     *
     * @param slot - The slot to disconnect from the signal.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection is removed, `false` otherwise.
     *
     * #### Notes
     * If no connection exists for the given `slot` and `thisArg`, this
     * method returns `false`.
     *
     * A disconnected slot will no longer be invoked, even if the slot
     * is disconnected while the signal is dispatching.
     */
    disconnect(slot: Slot<T, U>, thisArg?: any): boolean;
}
/**
 * A concrete implementation of `ISignal`.
 *
 * #### Example
 * ```typescript
 * import { ISignal, Signal } from '@phosphor/signaling';
 *
 * class SomeClass {
 *
 *   constructor(name: string) {
 *     this.name = name;
 *   }
 *
 *   readonly name: string;
 *
 *   get valueChanged: ISignal<this, number> {
 *     return this._valueChanged;
 *   }
 *
 *   get value(): number {
 *     return this._value;
 *   }
 *
 *   set value(value: number) {
 *     if (value === this._value) {
 *       return;
 *     }
 *     this._value = value;
 *     this._valueChanged.emit(value);
 *   }
 *
 *   private _value = 0;
 *   private _valueChanged = new Signal<this, number>(this);
 * }
 *
 * function logger(sender: SomeClass, value: number): void {
 *   console.log(sender.name, value);
 * }
 *
 * let m1 = new SomeClass('foo');
 * let m2 = new SomeClass('bar');
 *
 * m1.valueChanged.connect(logger);
 * m2.valueChanged.connect(logger);
 *
 * m1.value = 42;  // logs: foo 42
 * m2.value = 17;  // logs: bar 17
 * ```
 */
export declare class Signal<T, U> implements ISignal<T, U> {
    /**
     * Construct a new signal.
     *
     * @param sender - The sender which owns the signal.
     */
    constructor(sender: T);
    /**
     * The sender which owns the signal.
     */
    readonly sender: T;
    /**
     * Connect a slot to the signal.
     *
     * @param slot - The slot to invoke when the signal is emitted.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection succeeds, `false` otherwise.
     */
    connect(slot: Slot<T, U>, thisArg?: any): boolean;
    /**
     * Disconnect a slot from the signal.
     *
     * @param slot - The slot to disconnect from the signal.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection is removed, `false` otherwise.
     */
    disconnect(slot: Slot<T, U>, thisArg?: any): boolean;
    /**
     * Emit the signal and invoke the connected slots.
     *
     * @param args - The args to pass to the connected slots.
     *
     * #### Notes
     * Slots are invoked synchronously in connection order.
     *
     * Exceptions thrown by connected slots will be caught and logged.
     */
    emit(args: U): void;
}
/**
 * The namespace for the `Signal` class statics.
 */
export declare namespace Signal {
    /**
     * Remove all connections between a sender and receiver.
     *
     * @param sender - The sender object of interest.
     *
     * @param receiver - The receiver object of interest.
     *
     * #### Notes
     * If a `thisArg` is provided when connecting a signal, that object
     * is considered the receiver. Otherwise, the `slot` is considered
     * the receiver.
     */
    function disconnectBetween(sender: any, receiver: any): void;
    /**
     * Remove all connections where the given object is the sender.
     *
     * @param sender - The sender object of interest.
     */
    function disconnectSender(sender: any): void;
    /**
     * Remove all connections where the given object is the receiver.
     *
     * @param receiver - The receiver object of interest.
     *
     * #### Notes
     * If a `thisArg` is provided when connecting a signal, that object
     * is considered the receiver. Otherwise, the `slot` is considered
     * the receiver.
     */
    function disconnectReceiver(receiver: any): void;
    /**
     * Remove all connections where an object is the sender or receiver.
     *
     * @param object - The object of interest.
     *
     * #### Notes
     * If a `thisArg` is provided when connecting a signal, that object
     * is considered the receiver. Otherwise, the `slot` is considered
     * the receiver.
     */
    function disconnectAll(object: any): void;
    /**
     * Clear all signal data associated with the given object.
     *
     * @param object - The object for which the data should be cleared.
     *
     * #### Notes
     * This removes all signal connections and any other signal data
     * associated with the object.
     */
    function clearData(object: any): void;
    /**
     * A type alias for the exception handler function.
     */
    type ExceptionHandler = (err: Error) => void;
    /**
     * Get the signal exception handler.
     *
     * @returns The current exception handler.
     *
     * #### Notes
     * The default exception handler is `console.error`.
     */
    function getExceptionHandler(): ExceptionHandler;
    /**
     * Set the signal exception handler.
     *
     * @param handler - The function to use as the exception handler.
     *
     * @returns The old exception handler.
     *
     * #### Notes
     * The exception handler is invoked when a slot throws an exception.
     */
    function setExceptionHandler(handler: ExceptionHandler): ExceptionHandler;
}
