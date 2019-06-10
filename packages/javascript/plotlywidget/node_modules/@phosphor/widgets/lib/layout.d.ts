import { IIterable, IIterator } from '@phosphor/algorithm';
import { IDisposable } from '@phosphor/disposable';
import { Message } from '@phosphor/messaging';
import { Widget } from './widget';
/**
 * An abstract base class for creating Phosphor layouts.
 *
 * #### Notes
 * A layout is used to add widgets to a parent and to arrange those
 * widgets within the parent's DOM node.
 *
 * This class implements the base functionality which is required of
 * nearly all layouts. It must be subclassed in order to be useful.
 *
 * Notably, this class does not define a uniform interface for adding
 * widgets to the layout. A subclass should define that API in a way
 * which is meaningful for its intended use.
 */
export declare abstract class Layout implements IIterable<Widget>, IDisposable {
    /**
     * Construct a new layout.
     *
     * @param options - The options for initializing the layout.
     */
    constructor(options?: Layout.IOptions);
    /**
     * Dispose of the resources held by the layout.
     *
     * #### Notes
     * This should be reimplemented to clear and dispose of the widgets.
     *
     * All reimplementations should call the superclass method.
     *
     * This method is called automatically when the parent is disposed.
     */
    dispose(): void;
    /**
     * Test whether the layout is disposed.
     */
    readonly isDisposed: boolean;
    /**
     * Get the parent widget of the layout.
     */
    /**
     * Set the parent widget of the layout.
     *
     * #### Notes
     * This is set automatically when installing the layout on the parent
     * widget. The parent widget should not be set directly by user code.
     */
    parent: Widget | null;
    /**
     * Get the fit policy for the layout.
     *
     * #### Notes
     * The fit policy controls the computed size constraints which are
     * applied to the parent widget by the layout.
     *
     * Some layout implementations may ignore the fit policy.
     */
    /**
     * Set the fit policy for the layout.
     *
     * #### Notes
     * The fit policy controls the computed size constraints which are
     * applied to the parent widget by the layout.
     *
     * Some layout implementations may ignore the fit policy.
     *
     * Changing the fit policy will clear the current size constraint
     * for the parent widget and then re-fit the parent.
     */
    fitPolicy: Layout.FitPolicy;
    /**
     * Create an iterator over the widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     *
     * #### Notes
     * This abstract method must be implemented by a subclass.
     */
    abstract iter(): IIterator<Widget>;
    /**
     * Remove a widget from the layout.
     *
     * @param widget - The widget to remove from the layout.
     *
     * #### Notes
     * A widget is automatically removed from the layout when its `parent`
     * is set to `null`. This method should only be invoked directly when
     * removing a widget from a layout which has yet to be installed on a
     * parent widget.
     *
     * This method should *not* modify the widget's `parent`.
     */
    abstract removeWidget(widget: Widget): void;
    /**
     * Process a message sent to the parent widget.
     *
     * @param msg - The message sent to the parent widget.
     *
     * #### Notes
     * This method is called by the parent widget to process a message.
     *
     * Subclasses may reimplement this method as needed.
     */
    processParentMessage(msg: Message): void;
    /**
     * Perform layout initialization which requires the parent widget.
     *
     * #### Notes
     * This method is invoked immediately after the layout is installed
     * on the parent widget.
     *
     * The default implementation reparents all of the widgets to the
     * layout parent widget.
     *
     * Subclasses should reimplement this method and attach the child
     * widget nodes to the parent widget's node.
     */
    protected init(): void;
    /**
     * A message handler invoked on a `'resize'` message.
     *
     * #### Notes
     * The layout should ensure that its widgets are resized according
     * to the specified layout space, and that they are sent a `'resize'`
     * message if appropriate.
     *
     * The default implementation of this method sends an `UnknownSize`
     * resize message to all widgets.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onResize(msg: Widget.ResizeMessage): void;
    /**
     * A message handler invoked on an `'update-request'` message.
     *
     * #### Notes
     * The layout should ensure that its widgets are resized according
     * to the available layout space, and that they are sent a `'resize'`
     * message if appropriate.
     *
     * The default implementation of this method sends an `UnknownSize`
     * resize message to all widgets.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'before-attach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onBeforeAttach(msg: Message): void;
    /**
     * A message handler invoked on an `'after-attach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onAfterAttach(msg: Message): void;
    /**
     * A message handler invoked on a `'before-detach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onBeforeDetach(msg: Message): void;
    /**
     * A message handler invoked on an `'after-detach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onAfterDetach(msg: Message): void;
    /**
     * A message handler invoked on a `'before-show'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onBeforeShow(msg: Message): void;
    /**
     * A message handler invoked on an `'after-show'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onAfterShow(msg: Message): void;
    /**
     * A message handler invoked on a `'before-hide'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onBeforeHide(msg: Message): void;
    /**
     * A message handler invoked on an `'after-hide'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    protected onAfterHide(msg: Message): void;
    /**
     * A message handler invoked on a `'child-removed'` message.
     *
     * #### Notes
     * This will remove the child widget from the layout.
     *
     * Subclasses should **not** typically reimplement this method.
     */
    protected onChildRemoved(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'fit-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onFitRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'child-shown'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onChildShown(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'child-hidden'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    protected onChildHidden(msg: Widget.ChildMessage): void;
    private _disposed;
    private _fitPolicy;
    private _parent;
}
/**
 * The namespace for the `Layout` class statics.
 */
export declare namespace Layout {
    /**
     * A type alias for the layout fit policy.
     *
     * #### Notes
     * The fit policy controls the computed size constraints which are
     * applied to the parent widget by the layout.
     *
     * Some layout implementations may ignore the fit policy.
     */
    type FitPolicy = ('set-no-constraint' | 'set-min-size');
    /**
     * An options object for initializing a layout.
     */
    interface IOptions {
        /**
         * The fit policy for the for layout.
         *
         * The default is `'set-min-size'`.
         */
        fitPolicy?: FitPolicy;
    }
    /**
     * A type alias for the horizontal alignment of a widget.
     */
    type HorizontalAlignment = 'left' | 'center' | 'right';
    /**
     * A type alias for the vertical alignment of a widget.
     */
    type VerticalAlignment = 'top' | 'center' | 'bottom';
    /**
     * Get the horizontal alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The horizontal alignment for the widget.
     *
     * #### Notes
     * If the layout width allocated to a widget is larger than its max
     * width, the horizontal alignment controls how the widget is placed
     * within the extra horizontal space.
     *
     * If the allocated width is less than the widget's max width, the
     * horizontal alignment has no effect.
     *
     * Some layout implementations may ignore horizontal alignment.
     */
    function getHorizontalAlignment(widget: Widget): HorizontalAlignment;
    /**
     * Set the horizontal alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the horizontal alignment.
     *
     * #### Notes
     * If the layout width allocated to a widget is larger than its max
     * width, the horizontal alignment controls how the widget is placed
     * within the extra horizontal space.
     *
     * If the allocated width is less than the widget's max width, the
     * horizontal alignment has no effect.
     *
     * Some layout implementations may ignore horizontal alignment.
     *
     * Changing the horizontal alignment will post an `update-request`
     * message to widget's parent, provided the parent has a layout
     * installed.
     */
    function setHorizontalAlignment(widget: Widget, value: HorizontalAlignment): void;
    /**
     * Get the vertical alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The vertical alignment for the widget.
     *
     * #### Notes
     * If the layout height allocated to a widget is larger than its max
     * height, the vertical alignment controls how the widget is placed
     * within the extra vertical space.
     *
     * If the allocated height is less than the widget's max height, the
     * vertical alignment has no effect.
     *
     * Some layout implementations may ignore vertical alignment.
     */
    function getVerticalAlignment(widget: Widget): VerticalAlignment;
    /**
     * Set the vertical alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the vertical alignment.
     *
     * #### Notes
     * If the layout height allocated to a widget is larger than its max
     * height, the vertical alignment controls how the widget is placed
     * within the extra vertical space.
     *
     * If the allocated height is less than the widget's max height, the
     * vertical alignment has no effect.
     *
     * Some layout implementations may ignore vertical alignment.
     *
     * Changing the horizontal alignment will post an `update-request`
     * message to widget's parent, provided the parent has a layout
     * installed.
     */
    function setVerticalAlignment(widget: Widget, value: VerticalAlignment): void;
}
/**
 * An object which assists in the absolute layout of widgets.
 *
 * #### Notes
 * This class is useful when implementing a layout which arranges its
 * widgets using absolute positioning.
 *
 * This class is used by nearly all of the built-in Phosphor layouts.
 */
export declare class LayoutItem implements IDisposable {
    /**
     * Construct a new layout item.
     *
     * @param widget - The widget to be managed by the item.
     *
     * #### Notes
     * The widget will be set to absolute positioning.
     */
    constructor(widget: Widget);
    /**
     * Dispose of the the layout item.
     *
     * #### Notes
     * This will reset the positioning of the widget.
     */
    dispose(): void;
    /**
     * The widget managed by the layout item.
     */
    readonly widget: Widget;
    /**
     * The computed minimum width of the widget.
     *
     * #### Notes
     * This value can be updated by calling the `fit` method.
     */
    readonly minWidth: number;
    /**
     * The computed minimum height of the widget.
     *
     * #### Notes
     * This value can be updated by calling the `fit` method.
     */
    readonly minHeight: number;
    /**
     * The computed maximum width of the widget.
     *
     * #### Notes
     * This value can be updated by calling the `fit` method.
     */
    readonly maxWidth: number;
    /**
     * The computed maximum height of the widget.
     *
     * #### Notes
     * This value can be updated by calling the `fit` method.
     */
    readonly maxHeight: number;
    /**
     * Whether the layout item is disposed.
     */
    readonly isDisposed: boolean;
    /**
     * Whether the managed widget is hidden.
     */
    readonly isHidden: boolean;
    /**
     * Whether the managed widget is visible.
     */
    readonly isVisible: boolean;
    /**
     * Whether the managed widget is attached.
     */
    readonly isAttached: boolean;
    /**
     * Update the computed size limits of the managed widget.
     */
    fit(): void;
    /**
     * Update the position and size of the managed widget.
     *
     * @param left - The left edge position of the layout box.
     *
     * @param top - The top edge position of the layout box.
     *
     * @param width - The width of the layout box.
     *
     * @param height - The height of the layout box.
     */
    update(left: number, top: number, width: number, height: number): void;
    private _top;
    private _left;
    private _width;
    private _height;
    private _minWidth;
    private _minHeight;
    private _maxWidth;
    private _maxHeight;
    private _disposed;
}
