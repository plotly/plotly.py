import { Message } from '@phosphor/messaging';
import { Panel } from './panel';
import { SplitLayout } from './splitlayout';
import { Widget } from './widget';
/**
 * A panel which arranges its widgets into resizable sections.
 *
 * #### Notes
 * This class provides a convenience wrapper around a [[SplitLayout]].
 */
export declare class SplitPanel extends Panel {
    /**
     * Construct a new split panel.
     *
     * @param options - The options for initializing the split panel.
     */
    constructor(options?: SplitPanel.IOptions);
    /**
     * Dispose of the resources held by the panel.
     */
    dispose(): void;
    /**
     * Get the layout orientation for the split panel.
     */
    /**
     * Set the layout orientation for the split panel.
     */
    orientation: SplitPanel.Orientation;
    /**
     * Get the content alignment for the split panel.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand to fill the
     * entire split panel.
     */
    /**
     * Set the content alignment for the split panel.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand to fill the
     * entire split panel.
     */
    alignment: SplitPanel.Alignment;
    /**
     * Get the inter-element spacing for the split panel.
     */
    /**
     * Set the inter-element spacing for the split panel.
     */
    spacing: number;
    /**
     * The renderer used by the split panel.
     */
    readonly renderer: SplitPanel.IRenderer;
    /**
     * A read-only array of the split handles in the panel.
     */
    readonly handles: ReadonlyArray<HTMLDivElement>;
    /**
     * Get the relative sizes of the widgets in the panel.
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
     * Set the relative sizes for the widgets in the panel.
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
     * Handle the DOM events for the split panel.
     *
     * @param event - The DOM event sent to the panel.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the panel's DOM node. It should
     * not be called directly by user code.
     */
    handleEvent(event: Event): void;
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    protected onBeforeAttach(msg: Message): void;
    /**
     * A message handler invoked on an `'after-detach'` message.
     */
    protected onAfterDetach(msg: Message): void;
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    protected onChildAdded(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    protected onChildRemoved(msg: Widget.ChildMessage): void;
    /**
     * Handle the `'keydown'` event for the split panel.
     */
    private _evtKeyDown(event);
    /**
     * Handle the `'mousedown'` event for the split panel.
     */
    private _evtMouseDown(event);
    /**
     * Handle the `'mousemove'` event for the split panel.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseup'` event for the split panel.
     */
    private _evtMouseUp(event);
    /**
     * Release the mouse grab for the split panel.
     */
    private _releaseMouse();
    private _pressData;
}
/**
 * The namespace for the `SplitPanel` class statics.
 */
export declare namespace SplitPanel {
    /**
     * A type alias for a split panel orientation.
     */
    type Orientation = SplitLayout.Orientation;
    /**
     * A type alias for a split panel alignment.
     */
    type Alignment = SplitLayout.Alignment;
    /**
     * A type alias for a split panel renderer.
     */
    type IRenderer = SplitLayout.IRenderer;
    /**
     * An options object for initializing a split panel.
     */
    interface IOptions {
        /**
         * The renderer to use for the split panel.
         *
         * The default is a shared renderer instance.
         */
        renderer?: IRenderer;
        /**
         * The layout orientation of the panel.
         *
         * The default is `'horizontal'`.
         */
        orientation?: Orientation;
        /**
         * The content alignment of the panel.
         *
         * The default is `'start'`.
         */
        alignment?: Alignment;
        /**
         * The spacing between items in the panel.
         *
         * The default is `4`.
         */
        spacing?: number;
        /**
         * The split layout to use for the split panel.
         *
         * If this is provided, the other options are ignored.
         *
         * The default is a new `SplitLayout`.
         */
        layout?: SplitLayout;
    }
    /**
     * The default implementation of `IRenderer`.
     */
    class Renderer implements IRenderer {
        /**
         * Create a new handle for use with a split panel.
         *
         * @returns A new handle element for a split panel.
         */
        createHandle(): HTMLDivElement;
    }
    /**
     * The default `Renderer` instance.
     */
    const defaultRenderer: Renderer;
    /**
     * Get the split panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The split panel stretch factor for the widget.
     */
    function getStretch(widget: Widget): number;
    /**
     * Set the split panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget: Widget, value: number): void;
}
