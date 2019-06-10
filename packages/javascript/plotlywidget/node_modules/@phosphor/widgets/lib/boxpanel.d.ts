import { BoxLayout } from './boxlayout';
import { Panel } from './panel';
import { Widget } from './widget';
/**
 * A panel which arranges its widgets in a single row or column.
 *
 * #### Notes
 * This class provides a convenience wrapper around a [[BoxLayout]].
 */
export declare class BoxPanel extends Panel {
    /**
     * Construct a new box panel.
     *
     * @param options - The options for initializing the box panel.
     */
    constructor(options?: BoxPanel.IOptions);
    /**
     * Get the layout direction for the box panel.
     */
    /**
     * Set the layout direction for the box panel.
     */
    direction: BoxPanel.Direction;
    /**
     * Get the content alignment for the box panel.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand to fill the
     * entire box layout.
     */
    /**
     * Set the content alignment for the box panel.
     *
     * #### Notes
     * This is the alignment of the widgets in the layout direction.
     *
     * The alignment has no effect if the widgets can expand to fill the
     * entire box layout.
     */
    alignment: BoxPanel.Alignment;
    /**
     * Get the inter-element spacing for the box panel.
     */
    /**
     * Set the inter-element spacing for the box panel.
     */
    spacing: number;
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    protected onChildAdded(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    protected onChildRemoved(msg: Widget.ChildMessage): void;
}
/**
 * The namespace for the `BoxPanel` class statics.
 */
export declare namespace BoxPanel {
    /**
     * A type alias for a box panel direction.
     */
    type Direction = BoxLayout.Direction;
    /**
     * A type alias for a box panel alignment.
     */
    type Alignment = BoxLayout.Alignment;
    /**
     * An options object for initializing a box panel.
     */
    interface IOptions {
        /**
         * The layout direction of the panel.
         *
         * The default is `'top-to-bottom'`.
         */
        direction?: Direction;
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
         * The box layout to use for the box panel.
         *
         * If this is provided, the other options are ignored.
         *
         * The default is a new `BoxLayout`.
         */
        layout?: BoxLayout;
    }
    /**
     * Get the box panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box panel stretch factor for the widget.
     */
    function getStretch(widget: Widget): number;
    /**
     * Set the box panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget: Widget, value: number): void;
    /**
     * Get the box panel size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box panel size basis for the widget.
     */
    function getSizeBasis(widget: Widget): number;
    /**
     * Set the box panel size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the size basis.
     */
    function setSizeBasis(widget: Widget, value: number): void;
}
