import { IIterator } from '@phosphor/algorithm';
import { Message } from '@phosphor/messaging';
import { Layout } from './layout';
import { Widget } from './widget';
/**
 * A layout which arranges its widgets in a grid.
 */
export declare class GridLayout extends Layout {
    /**
     * Construct a new grid layout.
     *
     * @param options - The options for initializing the layout.
     */
    constructor(options?: GridLayout.IOptions);
    /**
     * Dispose of the resources held by the layout.
     */
    dispose(): void;
    /**
     * Get the number of rows in the layout.
     */
    /**
     * Set the number of rows in the layout.
     *
     * #### Notes
     * The minimum row count is `1`.
     */
    rowCount: number;
    /**
     * Get the number of columns in the layout.
     */
    /**
     * Set the number of columns in the layout.
     *
     * #### Notes
     * The minimum column count is `1`.
     */
    columnCount: number;
    /**
     * Get the row spacing for the layout.
     */
    /**
     * Set the row spacing for the layout.
     */
    rowSpacing: number;
    /**
     * Get the column spacing for the layout.
     */
    /**
     * Set the col spacing for the layout.
     */
    columnSpacing: number;
    /**
     * Get the stretch factor for a specific row.
     *
     * @param index - The row index of interest.
     *
     * @returns The stretch factor for the row.
     *
     * #### Notes
     * This returns `-1` if the index is out of range.
     */
    rowStretch(index: number): number;
    /**
     * Set the stretch factor for a specific row.
     *
     * @param index - The row index of interest.
     *
     * @param value - The stretch factor for the row.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    setRowStretch(index: number, value: number): void;
    /**
     * Get the stretch factor for a specific column.
     *
     * @param index - The column index of interest.
     *
     * @returns The stretch factor for the column.
     *
     * #### Notes
     * This returns `-1` if the index is out of range.
     */
    columnStretch(index: number): number;
    /**
     * Set the stretch factor for a specific column.
     *
     * @param index - The column index of interest.
     *
     * @param value - The stretch factor for the column.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    setColumnStretch(index: number, value: number): void;
    /**
     * Create an iterator over the widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     */
    iter(): IIterator<Widget>;
    /**
     * Add a widget to the grid layout.
     *
     * @param widget - The widget to add to the layout.
     *
     * #### Notes
     * If the widget is already contained in the layout, this is no-op.
     */
    addWidget(widget: Widget): void;
    /**
     * Remove a widget from the grid layout.
     *
     * @param widget - The widget to remove from the layout.
     *
     * #### Notes
     * A widget is automatically removed from the layout when its `parent`
     * is set to `null`. This method should only be invoked directly when
     * removing a widget from a layout which has yet to be installed on a
     * parent widget.
     *
     * This method does *not* modify the widget's `parent`.
     */
    removeWidget(widget: Widget): void;
    /**
     * Perform layout initialization which requires the parent widget.
     */
    protected init(): void;
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param widget - The widget to attach to the parent.
     */
    protected attachWidget(widget: Widget): void;
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param widget - The widget to detach from the parent.
     */
    protected detachWidget(widget: Widget): void;
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
    private _dirty;
    private _rowSpacing;
    private _columnSpacing;
    private _items;
    private _rowStarts;
    private _columnStarts;
    private _rowSizers;
    private _columnSizers;
    private _box;
}
/**
 * The namespace for the `GridLayout` class statics.
 */
export declare namespace GridLayout {
    /**
     * An options object for initializing a grid layout.
     */
    interface IOptions extends Layout.IOptions {
        /**
         * The initial row count for the layout.
         *
         * The default is `1`.
         */
        rowCount?: number;
        /**
         * The initial column count for the layout.
         *
         * The default is `1`.
         */
        columnCount?: number;
        /**
         * The spacing between rows in the layout.
         *
         * The default is `4`.
         */
        rowSpacing?: number;
        /**
         * The spacing between columns in the layout.
         *
         * The default is `4`.
         */
        columnSpacing?: number;
    }
    /**
     * An object which holds the cell configuration for a widget.
     */
    interface ICellConfig {
        /**
         * The row index for the widget.
         */
        readonly row: number;
        /**
         * The column index for the widget.
         */
        readonly column: number;
        /**
         * The row span for the widget.
         */
        readonly rowSpan: number;
        /**
         * The column span for the widget.
         */
        readonly columnSpan: number;
    }
    /**
     * Get the cell config for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The cell config for the widget.
     */
    function getCellConfig(widget: Widget): ICellConfig;
    /**
     * Set the cell config for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the cell config.
     */
    function setCellConfig(widget: Widget, value: Partial<ICellConfig>): void;
}
