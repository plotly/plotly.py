import { Message } from '@phosphor/messaging';
import { PanelLayout } from './panellayout';
import { Widget } from './widget';
/**
 * A layout which arranges its widgets in a single row or column.
 */
export declare class BoxLayout extends PanelLayout {
    /**
     * Construct a new box layout.
     *
     * @param options - The options for initializing the layout.
     */
    constructor(options?: BoxLayout.IOptions);
    /**
     * Dispose of the resources held by the layout.
     */
    dispose(): void;
    /**
     * Get the layout direction for the box layout.
     */
    /**
     * Set the layout direction for the box layout.
     */
    direction: BoxLayout.Direction;
    /**
     * Get the content alignment for the box layout.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand to fill the
     * entire box layout.
     */
    /**
     * Set the content alignment for the box layout.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand to fill the
     * entire box layout.
     */
    alignment: BoxLayout.Alignment;
    /**
     * Get the inter-element spacing for the box layout.
     */
    /**
     * Set the inter-element spacing for the box layout.
     */
    spacing: number;
    /**
     * Perform layout initialization which requires the parent widget.
     */
    protected init(): void;
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param index - The current index of the widget in the layout.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    protected attachWidget(index: number, widget: Widget): void;
    /**
     * Move a widget in the parent's DOM node.
     *
     * @param fromIndex - The previous index of the widget in the layout.
     *
     * @param toIndex - The current index of the widget in the layout.
     *
     * @param widget - The widget to move in the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    protected moveWidget(fromIndex: number, toIndex: number, widget: Widget): void;
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param index - The previous index of the widget in the layout.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    protected detachWidget(index: number, widget: Widget): void;
    /**
     * A message handler invoked on a `'before-show'` message.
     */
    protected onBeforeShow(msg: Message): void;
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    protected onBeforeAttach(msg: Message): void;
    /**
     * A message handler invoked on a `'child-shown'` message.
     */
    protected onChildShown(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'child-hidden'` message.
     */
    protected onChildHidden(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'resize'` message.
     */
    protected onResize(msg: Widget.ResizeMessage): void;
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'fit-request'` message.
     */
    protected onFitRequest(msg: Message): void;
    /**
     * Fit the layout to the total size required by the widgets.
     */
    private _fit();
    /**
     * Update the layout position and size of the widgets.
     *
     * The parent offset dimensions should be `-1` if unknown.
     */
    private _update(offsetWidth, offsetHeight);
    private _fixed;
    private _spacing;
    private _dirty;
    private _sizers;
    private _items;
    private _box;
    private _alignment;
    private _direction;
}
/**
 * The namespace for the `BoxLayout` class statics.
 */
export declare namespace BoxLayout {
    /**
     * A type alias for a box layout direction.
     */
    type Direction = ('left-to-right' | 'right-to-left' | 'top-to-bottom' | 'bottom-to-top');
    /**
     * A type alias for a box layout alignment.
     */
    type Alignment = 'start' | 'center' | 'end' | 'justify';
    /**
     * An options object for initializing a box layout.
     */
    interface IOptions {
        /**
         * The direction of the layout.
         *
         * The default is `'top-to-bottom'`.
         */
        direction?: Direction;
        /**
         * The content alignment of the layout.
         *
         * The default is `'start'`.
         */
        alignment?: Alignment;
        /**
         * The spacing between items in the layout.
         *
         * The default is `4`.
         */
        spacing?: number;
    }
    /**
     * Get the box layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box layout stretch factor for the widget.
     */
    function getStretch(widget: Widget): number;
    /**
     * Set the box layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget: Widget, value: number): void;
    /**
     * Get the box layout size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box layout size basis for the widget.
     */
    function getSizeBasis(widget: Widget): number;
    /**
     * Set the box layout size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the size basis.
     */
    function setSizeBasis(widget: Widget, value: number): void;
}
