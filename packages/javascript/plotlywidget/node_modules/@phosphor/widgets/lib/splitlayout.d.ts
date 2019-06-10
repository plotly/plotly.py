import { Message } from '@phosphor/messaging';
import { PanelLayout } from './panellayout';
import { Widget } from './widget';
/**
 * A layout which arranges its widgets into resizable sections.
 */
export declare class SplitLayout extends PanelLayout {
    /**
     * Construct a new split layout.
     *
     * @param options - The options for initializing the layout.
     */
    constructor(options: SplitLayout.IOptions);
    /**
     * Dispose of the resources held by the layout.
     */
    dispose(): void;
    /**
     * The renderer used by the split layout.
     */
    readonly renderer: SplitLayout.IRenderer;
    /**
     * Get the layout orientation for the split layout.
     */
    /**
     * Set the layout orientation for the split layout.
     */
    orientation: SplitLayout.Orientation;
    /**
     * Get the content alignment for the split layout.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand  to fill the
     * entire split layout.
     */
    /**
     * Set the content alignment for the split layout.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand  to fill the
     * entire split layout.
     */
    alignment: SplitLayout.Alignment;
    /**
     * Get the inter-element spacing for the split layout.
     */
    /**
     * Set the inter-element spacing for the split layout.
     */
    spacing: number;
    /**
     * A read-only array of the split handles in the layout.
     */
    readonly handles: ReadonlyArray<HTMLDivElement>;
    /**
     * Get the relative sizes of the widgets in the layout.
     *
     * @returns A new array of the relative sizes of the widgets.
     *
     * #### Notes
     * The returned sizes reflect the sizes of the widgets normalized
     * relative to their siblings.
     *
     * This method **does not** measure the DOM nodes.
     */
    relativeSizes(): number[];
    /**
     * Set the relative sizes for the widgets in the layout.
     *
     * @param sizes - The relative sizes for the widgets in the panel.
     *
     * #### Notes
     * Extra values are ignored, too few will yield an undefined layout.
     *
     * The actual geometry of the DOM nodes is updated asynchronously.
     */
    setRelativeSizes(sizes: number[]): void;
    /**
     * Move the offset position of a split handle.
     *
     * @param index - The index of the handle of the interest.
     *
     * @param position - The desired offset position of the handle.
     *
     * #### Notes
     * The position is relative to the offset parent.
     *
     * This will move the handle as close as possible to the desired
     * position. The sibling widgets will be adjusted as necessary.
     */
    moveHandle(index: number, position: number): void;
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
    private _hasNormedSizes;
    private _sizers;
    private _items;
    private _handles;
    private _box;
    private _alignment;
    private _orientation;
}
/**
 * The namespace for the `SplitLayout` class statics.
 */
export declare namespace SplitLayout {
    /**
     * A type alias for a split layout orientation.
     */
    type Orientation = 'horizontal' | 'vertical';
    /**
     * A type alias for a split layout alignment.
     */
    type Alignment = 'start' | 'center' | 'end' | 'justify';
    /**
     * An options object for initializing a split layout.
     */
    interface IOptions {
        /**
         * The renderer to use for the split layout.
         */
        renderer: IRenderer;
        /**
         * The orientation of the layout.
         *
         * The default is `'horizontal'`.
         */
        orientation?: Orientation;
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
     * A renderer for use with a split layout.
     */
    interface IRenderer {
        /**
         * Create a new handle for use with a split layout.
         *
         * @returns A new handle element.
         */
        createHandle(): HTMLDivElement;
    }
    /**
     * Get the split layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The split layout stretch factor for the widget.
     */
    function getStretch(widget: Widget): number;
    /**
     * Set the split layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget: Widget, value: number): void;
}
