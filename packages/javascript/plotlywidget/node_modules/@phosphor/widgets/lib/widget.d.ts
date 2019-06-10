import { IIterator } from '@phosphor/algorithm';
import { IDisposable } from '@phosphor/disposable';
import { ConflatableMessage, IMessageHandler, Message } from '@phosphor/messaging';
import { ISignal } from '@phosphor/signaling';
import { Layout } from './layout';
import { Title } from './title';
/**
 * The base class of the Phosphor widget hierarchy.
 *
 * #### Notes
 * This class will typically be subclassed in order to create a useful
 * widget. However, it can be used directly to host externally created
 * content.
 */
export declare class Widget implements IDisposable, IMessageHandler {
    /**
     * Construct a new widget.
     *
     * @param options - The options for initializing the widget.
     */
    constructor(options?: Widget.IOptions);
    /**
     * Dispose of the widget and its descendant widgets.
     *
     * #### Notes
     * It is unsafe to use the widget after it has been disposed.
     *
     * All calls made to this method after the first are a no-op.
     */
    dispose(): void;
    /**
     * A signal emitted when the widget is disposed.
     */
    readonly disposed: ISignal<this, void>;
    /**
     * Get the DOM node owned by the widget.
     */
    readonly node: HTMLElement;
    /**
     * Test whether the widget has been disposed.
     */
    readonly isDisposed: boolean;
    /**
     * Test whether the widget's node is attached to the DOM.
     */
    readonly isAttached: boolean;
    /**
     * Test whether the widget is explicitly hidden.
     */
    readonly isHidden: boolean;
    /**
     * Test whether the widget is visible.
     *
     * #### Notes
     * A widget is visible when it is attached to the DOM, is not
     * explicitly hidden, and has no explicitly hidden ancestors.
     */
    readonly isVisible: boolean;
    /**
     * The title object for the widget.
     *
     * #### Notes
     * The title object is used by some container widgets when displaying
     * the widget alongside some title, such as a tab panel or side bar.
     *
     * Since not all widgets will use the title, it is created on demand.
     *
     * The `owner` property of the title is set to this widget.
     */
    readonly title: Title<Widget>;
    /**
     * Get the id of the widget's DOM node.
     */
    /**
     * Set the id of the widget's DOM node.
     */
    id: string;
    /**
     * The dataset for the widget's DOM node.
     */
    readonly dataset: DOMStringMap;
    /**
     * Get the parent of the widget.
     */
    /**
     * Set the parent of the widget.
     *
     * #### Notes
     * Children are typically added to a widget by using a layout, which
     * means user code will not normally set the parent widget directly.
     *
     * The widget will be automatically removed from its old parent.
     *
     * This is a no-op if there is no effective parent change.
     */
    parent: Widget | null;
    /**
     * Get the layout for the widget.
     */
    /**
     * Set the layout for the widget.
     *
     * #### Notes
     * The layout is single-use only. It cannot be changed after the
     * first assignment.
     *
     * The layout is disposed automatically when the widget is disposed.
     */
    layout: Layout | null;
    /**
     * Create an iterator over the widget's children.
     *
     * @returns A new iterator over the children of the widget.
     *
     * #### Notes
     * The widget must have a populated layout in order to have children.
     *
     * If a layout is not installed, the returned iterator will be empty.
     */
    children(): IIterator<Widget>;
    /**
     * Test whether a widget is a descendant of this widget.
     *
     * @param widget - The descendant widget of interest.
     *
     * @returns `true` if the widget is a descendant, `false` otherwise.
     */
    contains(widget: Widget): boolean;
    /**
     * Test whether the widget's DOM node has the given class name.
     *
     * @param name - The class name of interest.
     *
     * @returns `true` if the node has the class, `false` otherwise.
     */
    hasClass(name: string): boolean;
    /**
     * Add a class name to the widget's DOM node.
     *
     * @param name - The class name to add to the node.
     *
     * #### Notes
     * If the class name is already added to the node, this is a no-op.
     *
     * The class name must not contain whitespace.
     */
    addClass(name: string): void;
    /**
     * Remove a class name from the widget's DOM node.
     *
     * @param name - The class name to remove from the node.
     *
     * #### Notes
     * If the class name is not yet added to the node, this is a no-op.
     *
     * The class name must not contain whitespace.
     */
    removeClass(name: string): void;
    /**
     * Toggle a class name on the widget's DOM node.
     *
     * @param name - The class name to toggle on the node.
     *
     * @param force - Whether to force add the class (`true`) or force
     *   remove the class (`false`). If not provided, the presence of
     *   the class will be toggled from its current state.
     *
     * @returns `true` if the class is now present, `false` otherwise.
     *
     * #### Notes
     * The class name must not contain whitespace.
     */
    toggleClass(name: string, force?: boolean): boolean;
    /**
     * Post an `'update-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for posting the message.
     */
    update(): void;
    /**
     * Post a `'fit-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for posting the message.
     */
    fit(): void;
    /**
     * Post an `'activate-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for posting the message.
     */
    activate(): void;
    /**
     * Send a `'close-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for sending the message.
     */
    close(): void;
    /**
     * Show the widget and make it visible to its parent widget.
     *
     * #### Notes
     * This causes the [[isHidden]] property to be `false`.
     *
     * If the widget is not explicitly hidden, this is a no-op.
     */
    show(): void;
    /**
     * Hide the widget and make it hidden to its parent widget.
     *
     * #### Notes
     * This causes the [[isHidden]] property to be `true`.
     *
     * If the widget is explicitly hidden, this is a no-op.
     */
    hide(): void;
    /**
     * Show or hide the widget according to a boolean value.
     *
     * @param hidden - `true` to hide the widget, or `false` to show it.
     *
     * #### Notes
     * This is a convenience method for `hide()` and `show()`.
     */
    setHidden(hidden: boolean): void;
    /**
     * Test whether the given widget flag is set.
     *
     * #### Notes
     * This will not typically be called directly by user code.
     */
    testFlag(flag: Widget.Flag): boolean;
    /**
     * Set the given widget flag.
     *
     * #### Notes
     * This will not typically be called directly by user code.
     */
    setFlag(flag: Widget.Flag): void;
    /**
     * Clear the given widget flag.
     *
     * #### Notes
     * This will not typically be called directly by user code.
     */
    clearFlag(flag: Widget.Flag): void;
    /**
     * Process a message sent to the widget.
     *
     * @param msg - The message sent to the widget.
     *
     * #### Notes
     * Subclasses may reimplement this method as needed.
     */
    processMessage(msg: Message): void;
    /**
     * Invoke the message processing routine of the widget's layout.
     *
     * @param msg - The message to dispatch to the layout.
     *
     * #### Notes
     * This is a no-op if the widget does not have a layout.
     *
     * This will not typically be called directly by user code.
     */
    protected notifyLayout(msg: Message): void;
    /**
     * A message handler invoked on a `'close-request'` message.
     *
     * #### Notes
     * The default implementation unparents or detaches the widget.
     */
    protected onCloseRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'resize'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onResize(msg: Widget.ResizeMessage): void;
    /**
     * A message handler invoked on an `'update-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'fit-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onFitRequest(msg: Message): void;
    /**
     * A message handler invoked on an `'activate-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onActivateRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'before-show'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onBeforeShow(msg: Message): void;
    /**
     * A message handler invoked on an `'after-show'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onAfterShow(msg: Message): void;
    /**
     * A message handler invoked on a `'before-hide'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onBeforeHide(msg: Message): void;
    /**
     * A message handler invoked on an `'after-hide'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onAfterHide(msg: Message): void;
    /**
     * A message handler invoked on a `'before-attach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onBeforeAttach(msg: Message): void;
    /**
     * A message handler invoked on an `'after-attach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onAfterAttach(msg: Message): void;
    /**
     * A message handler invoked on a `'before-detach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onBeforeDetach(msg: Message): void;
    /**
     * A message handler invoked on an `'after-detach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onAfterDetach(msg: Message): void;
    /**
     * A message handler invoked on a `'child-added'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onChildAdded(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'child-removed'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onChildRemoved(msg: Widget.ChildMessage): void;
    private _flags;
    private _layout;
    private _parent;
    private _disposed;
}
/**
 * The namespace for the `Widget` class statics.
 */
export declare namespace Widget {
    /**
     * An options object for initializing a widget.
     */
    interface IOptions {
        /**
         * The optional node to use for the widget.
         *
         * If a node is provided, the widget will assume full ownership
         * and control of the node, as if it had created the node itself.
         *
         * The default is a new `<div>`.
         */
        node?: HTMLElement;
    }
    /**
     * An enum of widget bit flags.
     */
    enum Flag {
        /**
         * The widget has been disposed.
         */
        IsDisposed = 1,
        /**
         * The widget is attached to the DOM.
         */
        IsAttached = 2,
        /**
         * The widget is hidden.
         */
        IsHidden = 4,
        /**
         * The widget is visible.
         */
        IsVisible = 8,
        /**
         * A layout cannot be set on the widget.
         */
        DisallowLayout = 16,
    }
    /**
     * A collection of stateless messages related to widgets.
     */
    namespace Msg {
        /**
         * A singleton `'before-show'` message.
         *
         * #### Notes
         * This message is sent to a widget before it becomes visible.
         *
         * This message is **not** sent when the widget is being attached.
         */
        const BeforeShow: Message;
        /**
         * A singleton `'after-show'` message.
         *
         * #### Notes
         * This message is sent to a widget after it becomes visible.
         *
         * This message is **not** sent when the widget is being attached.
         */
        const AfterShow: Message;
        /**
         * A singleton `'before-hide'` message.
         *
         * #### Notes
         * This message is sent to a widget before it becomes not-visible.
         *
         * This message is **not** sent when the widget is being detached.
         */
        const BeforeHide: Message;
        /**
         * A singleton `'after-hide'` message.
         *
         * #### Notes
         * This message is sent to a widget after it becomes not-visible.
         *
         * This message is **not** sent when the widget is being detached.
         */
        const AfterHide: Message;
        /**
         * A singleton `'before-attach'` message.
         *
         * #### Notes
         * This message is sent to a widget before it is attached.
         */
        const BeforeAttach: Message;
        /**
         * A singleton `'after-attach'` message.
         *
         * #### Notes
         * This message is sent to a widget after it is attached.
         */
        const AfterAttach: Message;
        /**
         * A singleton `'before-detach'` message.
         *
         * #### Notes
         * This message is sent to a widget before it is detached.
         */
        const BeforeDetach: Message;
        /**
         * A singleton `'after-detach'` message.
         *
         * #### Notes
         * This message is sent to a widget after it is detached.
         */
        const AfterDetach: Message;
        /**
         * A singleton `'parent-changed'` message.
         *
         * #### Notes
         * This message is sent to a widget when its parent has changed.
         */
        const ParentChanged: Message;
        /**
         * A singleton conflatable `'update-request'` message.
         *
         * #### Notes
         * This message can be dispatched to supporting widgets in order to
         * update their content based on the current widget state. Not all
         * widgets will respond to messages of this type.
         *
         * For widgets with a layout, this message will inform the layout to
         * update the position and size of its child widgets.
         */
        const UpdateRequest: ConflatableMessage;
        /**
         * A singleton conflatable `'fit-request'` message.
         *
         * #### Notes
         * For widgets with a layout, this message will inform the layout to
         * recalculate its size constraints to fit the space requirements of
         * its child widgets, and to update their position and size. Not all
         * layouts will respond to messages of this type.
         */
        const FitRequest: ConflatableMessage;
        /**
         * A singleton conflatable `'activate-request'` message.
         *
         * #### Notes
         * This message should be dispatched to a widget when it should
         * perform the actions necessary to activate the widget, which
         * may include focusing its node or descendant node.
         */
        const ActivateRequest: ConflatableMessage;
        /**
         * A singleton conflatable `'close-request'` message.
         *
         * #### Notes
         * This message should be dispatched to a widget when it should close
         * and remove itself from the widget hierarchy.
         */
        const CloseRequest: ConflatableMessage;
    }
    /**
     * A message class for child related messages.
     */
    class ChildMessage extends Message {
        /**
         * Construct a new child message.
         *
         * @param type - The message type.
         *
         * @param child - The child widget for the message.
         */
        constructor(type: string, child: Widget);
        /**
         * The child widget for the message.
         */
        readonly child: Widget;
    }
    /**
     * A message class for `'resize'` messages.
     */
    class ResizeMessage extends Message {
        /**
         * Construct a new resize message.
         *
         * @param width - The **offset width** of the widget, or `-1` if
         *   the width is not known.
         *
         * @param height - The **offset height** of the widget, or `-1` if
         *   the height is not known.
         */
        constructor(width: number, height: number);
        /**
         * The offset width of the widget.
         *
         * #### Notes
         * This will be `-1` if the width is unknown.
         */
        readonly width: number;
        /**
         * The offset height of the widget.
         *
         * #### Notes
         * This will be `-1` if the height is unknown.
         */
        readonly height: number;
    }
    /**
     * The namespace for the `ResizeMessage` class statics.
     */
    namespace ResizeMessage {
        /**
         * A singleton `'resize'` message with an unknown size.
         */
        const UnknownSize: ResizeMessage;
    }
    /**
     * Attach a widget to a host DOM node.
     *
     * @param widget - The widget of interest.
     *
     * @param host - The DOM node to use as the widget's host.
     *
     * @param ref - The child of `host` to use as the reference element.
     *   If this is provided, the widget will be inserted before this
     *   node in the host. The default is `null`, which will cause the
     *   widget to be added as the last child of the host.
     *
     * #### Notes
     * This will throw an error if the widget is not a root widget, if
     * the widget is already attached, or if the host is not attached
     * to the DOM.
     */
    function attach(widget: Widget, host: HTMLElement, ref?: HTMLElement | null): void;
    /**
     * Detach the widget from its host DOM node.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * This will throw an error if the widget is not a root widget,
     * or if the widget is not attached to the DOM.
     */
    function detach(widget: Widget): void;
}
