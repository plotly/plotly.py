/**
 * A message which can be delivered to a message handler.
 *
 * #### Notes
 * This class may be subclassed to create complex message types.
 */
export declare class Message {
    /**
     * Construct a new message.
     *
     * @param type - The type of the message.
     */
    constructor(type: string);
    /**
     * The type of the message.
     *
     * #### Notes
     * The `type` of a message should be related directly to its actual
     * runtime type. This means that `type` can and will be used to cast
     * the message to the relevant derived `Message` subtype.
     */
    readonly type: string;
    /**
     * Test whether the message is conflatable.
     *
     * #### Notes
     * Message conflation is an advanced topic. Most message types will
     * not make use of this feature.
     *
     * If a conflatable message is posted to a handler while another
     * conflatable message of the same `type` has already been posted
     * to the handler, the `conflate()` method of the existing message
     * will be invoked. If that method returns `true`, the new message
     * will not be enqueued. This allows messages to be compressed, so
     * that only a single instance of the message type is processed per
     * cycle, no matter how many times messages of that type are posted.
     *
     * Custom message types may reimplement this property.
     *
     * The default implementation is always `false`.
     */
    readonly isConflatable: boolean;
    /**
     * Conflate this message with another message of the same `type`.
     *
     * @param other - A conflatable message of the same `type`.
     *
     * @returns `true` if the message was successfully conflated, or
     *   `false` otherwise.
     *
     * #### Notes
     * Message conflation is an advanced topic. Most message types will
     * not make use of this feature.
     *
     * This method is called automatically by the message loop when the
     * given message is posted to the handler paired with this message.
     * This message will already be enqueued and conflatable, and the
     * given message will have the same `type` and also be conflatable.
     *
     * This method should merge the state of the other message into this
     * message as needed so that when this message is finally delivered
     * to the handler, it receives the most up-to-date information.
     *
     * If this method returns `true`, it signals that the other message
     * was successfully conflated and that message will not be enqueued.
     *
     * If this method returns `false`, the other message will be enqueued
     * for normal delivery.
     *
     * Custom message types may reimplement this method.
     *
     * The default implementation always returns `false`.
     */
    conflate(other: Message): boolean;
}
/**
 * A convenience message class which conflates automatically.
 *
 * #### Notes
 * Message conflation is an advanced topic. Most user code will not
 * make use of this class.
 *
 * This message class is useful for creating message instances which
 * should be conflated, but which have no state other than `type`.
 *
 * If conflation of stateful messages is required, a custom `Message`
 * subclass should be created.
 */
export declare class ConflatableMessage extends Message {
    /**
     * Test whether the message is conflatable.
     *
     * #### Notes
     * This property is always `true`.
     */
    readonly isConflatable: boolean;
    /**
     * Conflate this message with another message of the same `type`.
     *
     * #### Notes
     * This method always returns `true`.
     */
    conflate(other: ConflatableMessage): boolean;
}
/**
 * An object which handles messages.
 *
 * #### Notes
 * A message handler is a simple way of defining a type which can act
 * upon on a large variety of external input without requiring a large
 * abstract API surface. This is particularly useful in the context of
 * widget frameworks where the number of distinct message types can be
 * unbounded.
 */
export interface IMessageHandler {
    /**
     * Process a message sent to the handler.
     *
     * @param msg - The message to be processed.
     */
    processMessage(msg: Message): void;
}
/**
 * An object which intercepts messages sent to a message handler.
 *
 * #### Notes
 * A message hook is useful for intercepting or spying on messages
 * sent to message handlers which were either not created by the
 * consumer, or when subclassing the handler is not feasible.
 *
 * If `messageHook` returns `false`, no other message hooks will be
 * invoked and the message will not be delivered to the handler.
 *
 * If all installed message hooks return `true`, the message will
 * be delivered to the handler for processing.
 *
 * **See also:** [[installMessageHook]] and [[removeMessageHook]]
 */
export interface IMessageHook {
    /**
     * Intercept a message sent to a message handler.
     *
     * @param handler - The target handler of the message.
     *
     * @param msg - The message to be sent to the handler.
     *
     * @returns `true` if the message should continue to be processed
     *   as normal, or `false` if processing should cease immediately.
     */
    messageHook(handler: IMessageHandler, msg: Message): boolean;
}
/**
 * A type alias for message hook object or function.
 *
 * #### Notes
 * The signature and semantics of a message hook function are the same
 * as the `messageHook` method of [[IMessageHook]].
 */
export declare type MessageHook = IMessageHook | ((handler: IMessageHandler, msg: Message) => boolean);
/**
 * The namespace for the global singleton message loop.
 */
export declare namespace MessageLoop {
    /**
     * Send a message to a message handler to process immediately.
     *
     * @param handler - The handler which should process the message.
     *
     * @param msg - The message to deliver to the handler.
     *
     * #### Notes
     * The message will first be sent through any installed message hooks
     * for the handler. If the message passes all hooks, it will then be
     * delivered to the `processMessage` method of the handler.
     *
     * The message will not be conflated with pending posted messages.
     *
     * Exceptions in hooks and handlers will be caught and logged.
     */
    function sendMessage(handler: IMessageHandler, msg: Message): void;
    /**
     * Post a message to a message handler to process in the future.
     *
     * @param handler - The handler which should process the message.
     *
     * @param msg - The message to post to the handler.
     *
     * #### Notes
     * The message will be conflated with the pending posted messages for
     * the handler, if possible. If the message is not conflated, it will
     * be queued for normal delivery on the next cycle of the event loop.
     *
     * Exceptions in hooks and handlers will be caught and logged.
     */
    function postMessage(handler: IMessageHandler, msg: Message): void;
    /**
     * Install a message hook for a message handler.
     *
     * @param handler - The message handler of interest.
     *
     * @param hook - The message hook to install.
     *
     * #### Notes
     * A message hook is invoked before a message is delivered to the
     * handler. If the hook returns `false`, no other hooks will be
     * invoked and the message will not be delivered to the handler.
     *
     * The most recently installed message hook is executed first.
     *
     * If the hook is already installed, this is a no-op.
     */
    function installMessageHook(handler: IMessageHandler, hook: MessageHook): void;
    /**
     * Remove an installed message hook for a message handler.
     *
     * @param handler - The message handler of interest.
     *
     * @param hook - The message hook to remove.
     *
     * #### Notes
     * It is safe to call this function while the hook is executing.
     *
     * If the hook is not installed, this is a no-op.
     */
    function removeMessageHook(handler: IMessageHandler, hook: MessageHook): void;
    /**
     * Clear all message data associated with a message handler.
     *
     * @param handler - The message handler of interest.
     *
     * #### Notes
     * This will clear all posted messages and hooks for the handler.
     */
    function clearData(handler: IMessageHandler): void;
    /**
     * Process the pending posted messages in the queue immediately.
     *
     * #### Notes
     * This function is useful when posted messages must be processed
     * immediately, instead of on the next animation frame.
     *
     * This function should normally not be needed, but it may be
     * required to work around certain browser idiosyncrasies.
     *
     * Recursing into this function is a no-op.
     */
    function flush(): void;
    /**
     * A type alias for the exception handler function.
     */
    type ExceptionHandler = (err: Error) => void;
    /**
     * Get the message loop exception handler.
     *
     * @returns The current exception handler.
     *
     * #### Notes
     * The default exception handler is `console.error`.
     */
    function getExceptionHandler(): ExceptionHandler;
    /**
     * Set the message loop exception handler.
     *
     * @param handler - The function to use as the exception handler.
     *
     * @returns The old exception handler.
     *
     * #### Notes
     * The exception handler is invoked when a message handler or a
     * message hook throws an exception.
     */
    function setExceptionHandler(handler: ExceptionHandler): ExceptionHandler;
}
