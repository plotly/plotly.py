import { IIterator } from '@phosphor/algorithm';
import { Message } from '@phosphor/messaging';
import { Layout } from './layout';
import { TabBar } from './tabbar';
import { Widget } from './widget';
/**
 * A layout which provides a flexible docking arrangement.
 *
 * #### Notes
 * The consumer of this layout is repsonsible for handling all signals
 * from the generated tab bars and managing the visibility of widgets
 * and tab bars as needed.
 */
export declare class DockLayout extends Layout {
    /**
     * Construct a new dock layout.
     *
     * @param options - The options for initializing the layout.
     */
    constructor(options: DockLayout.IOptions);
    /**
     * Dispose of the resources held by the layout.
     *
     * #### Notes
     * This will clear and dispose all widgets in the layout.
     */
    dispose(): void;
    /**
     * The renderer used by the dock layout.
     */
    readonly renderer: DockLayout.IRenderer;
    /**
     * Get the inter-element spacing for the dock layout.
     */
    /**
     * Set the inter-element spacing for the dock layout.
     */
    spacing: number;
    /**
     * Whether the dock layout is empty.
     */
    readonly isEmpty: boolean;
    /**
     * Create an iterator over all widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     *
     * #### Notes
     * This iterator includes the generated tab bars.
     */
    iter(): IIterator<Widget>;
    /**
     * Create an iterator over the user widgets in the layout.
     *
     * @returns A new iterator over the user widgets in the layout.
     *
     * #### Notes
     * This iterator does not include the generated tab bars.
     */
    widgets(): IIterator<Widget>;
    /**
     * Create an iterator over the selected widgets in the layout.
     *
     * @returns A new iterator over the selected user widgets.
     *
     * #### Notes
     * This iterator yields the widgets corresponding to the current tab
     * of each tab bar in the layout.
     */
    selectedWidgets(): IIterator<Widget>;
    /**
     * Create an iterator over the tab bars in the layout.
     *
     * @returns A new iterator over the tab bars in the layout.
     *
     * #### Notes
     * This iterator does not include the user widgets.
     */
    tabBars(): IIterator<TabBar<Widget>>;
    /**
     * Create an iterator over the handles in the layout.
     *
     * @returns A new iterator over the handles in the layout.
     */
    handles(): IIterator<HTMLDivElement>;
    /**
     * Move a handle to the given offset position.
     *
     * @param handle - The handle to move.
     *
     * @param offsetX - The desired offset X position of the handle.
     *
     * @param offsetY - The desired offset Y position of the handle.
     *
     * #### Notes
     * If the given handle is not contained in the layout, this is no-op.
     *
     * The handle will be moved as close as possible to the desired
     * position without violating any of the layout constraints.
     *
     * Only one of the coordinates is used depending on the orientation
     * of the handle. This method accepts both coordinates to make it
     * easy to invoke from a mouse move event without needing to know
     * the handle orientation.
     */
    moveHandle(handle: HTMLDivElement, offsetX: number, offsetY: number): void;
    /**
     * Save the current configuration of the dock layout.
     *
     * @returns A new config object for the current layout state.
     *
     * #### Notes
     * The return value can be provided to the `restoreLayout` method
     * in order to restore the layout to its current configuration.
     */
    saveLayout(): DockLayout.ILayoutConfig;
    /**
     * Restore the layout to a previously saved configuration.
     *
     * @param config - The layout configuration to restore.
     *
     * #### Notes
     * Widgets which currently belong to the layout but which are not
     * contained in the config will be unparented.
     */
    restoreLayout(config: DockLayout.ILayoutConfig): void;
    /**
     * Add a widget to the dock layout.
     *
     * @param widget - The widget to add to the dock layout.
     *
     * @param options - The additional options for adding the widget.
     *
     * #### Notes
     * The widget will be moved if it is already contained in the layout.
     *
     * An error will be thrown if the reference widget is invalid.
     */
    addWidget(widget: Widget, options?: DockLayout.IAddOptions): void;
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
     * This method does *not* modify the widget's `parent`.
     */
    removeWidget(widget: Widget): void;
    /**
     * Find the tab area which contains the given client position.
     *
     * @param clientX - The client X position of interest.
     *
     * @param clientY - The client Y position of interest.
     *
     * @returns The geometry of the tab area at the given position, or
     *   `null` if there is no tab area at the given position.
     */
    hitTestTabAreas(clientX: number, clientY: number): DockLayout.ITabAreaGeometry | null;
    /**
     * Perform layout initialization which requires the parent widget.
     */
    protected init(): void;
    /**
     * Attach the widget to the layout parent widget.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This is a no-op if the widget is already attached.
     */
    protected attachWidget(widget: Widget): void;
    /**
     * Detach the widget from the layout parent widget.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This is a no-op if the widget is not attached.
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
     * Remove the specified widget from the layout structure.
     *
     * #### Notes
     * This is a no-op if the widget is not in the layout tree.
     *
     * This does not detach the widget from the parent node.
     */
    private _removeWidget(widget);
    /**
     * Insert a widget next to an existing tab.
     *
     * #### Notes
     * This does not attach the widget to the parent widget.
     */
    private _insertTab(widget, ref, refNode, after);
    /**
     * Insert a widget as a new split area.
     *
     * #### Notes
     * This does not attach the widget to the parent widget.
     */
    private _insertSplit(widget, ref, refNode, orientation, after);
    /**
     * Ensure the root is a split node with the given orientation.
     */
    private _splitRoot(orientation);
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
    /**
     * Create a new tab bar for use by the dock layout.
     *
     * #### Notes
     * The tab bar will be attached to the parent if it exists.
     */
    private _createTabBar();
    /**
     * Create a new handle for the dock layout.
     *
     * #### Notes
     * The handle will be attached to the parent if it exists.
     */
    private _createHandle();
    private _spacing;
    private _dirty;
    private _root;
    private _box;
    private _items;
}
/**
 * The namespace for the `DockLayout` class statics.
 */
export declare namespace DockLayout {
    /**
     * An options object for creating a dock layout.
     */
    interface IOptions {
        /**
         * The renderer to use for the dock layout.
         */
        renderer: IRenderer;
        /**
         * The spacing between items in the layout.
         *
         * The default is `4`.
         */
        spacing?: number;
    }
    /**
     * A renderer for use with a dock layout.
     */
    interface IRenderer {
        /**
         * Create a new tab bar for use with a dock layout.
         *
         * @returns A new tab bar for a dock layout.
         */
        createTabBar(): TabBar<Widget>;
        /**
         * Create a new handle node for use with a dock layout.
         *
         * @returns A new handle node for a dock layout.
         */
        createHandle(): HTMLDivElement;
    }
    /**
     * A type alias for the supported insertion modes.
     *
     * An insert mode is used to specify how a widget should be added
     * to the dock layout relative to a reference widget.
     */
    type InsertMode = ('split-top' | 'split-left' | 'split-right' | 'split-bottom' | 'tab-before' | 'tab-after');
    /**
     * An options object for adding a widget to the dock layout.
     */
    interface IAddOptions {
        /**
         * The insertion mode for adding the widget.
         *
         * The default is `'tab-after'`.
         */
        mode?: InsertMode;
        /**
         * The reference widget for the insert location.
         *
         * The default is `null`.
         */
        ref?: Widget | null;
    }
    /**
     * A layout config object for a tab area.
     */
    interface ITabAreaConfig {
        /**
         * The discriminated type of the config object.
         */
        type: 'tab-area';
        /**
         * The widgets contained in the tab area.
         */
        widgets: Widget[];
        /**
         * The index of the selected tab.
         */
        currentIndex: number;
    }
    /**
     * A layout config object for a split area.
     */
    interface ISplitAreaConfig {
        /**
         * The discriminated type of the config object.
         */
        type: 'split-area';
        /**
         * The orientation of the split area.
         */
        orientation: 'horizontal' | 'vertical';
        /**
         * The children in the split area.
         */
        children: AreaConfig[];
        /**
         * The relative sizes of the children.
         */
        sizes: number[];
    }
    /**
     * A type alias for a general area config.
     */
    type AreaConfig = ITabAreaConfig | ISplitAreaConfig;
    /**
     * A dock layout configuration object.
     */
    interface ILayoutConfig {
        /**
         * The layout config for the main dock area.
         */
        main: AreaConfig | null;
    }
    /**
     * An object which represents the geometry of a tab area.
     */
    interface ITabAreaGeometry {
        /**
         * The tab bar for the tab area.
         */
        tabBar: TabBar<Widget>;
        /**
         * The local X position of the hit test in the dock area.
         *
         * #### Notes
         * This is the distance from the left edge of the layout parent
         * widget, to the local X coordinate of the hit test query.
         */
        x: number;
        /**
         * The local Y position of the hit test in the dock area.
         *
         * #### Notes
         * This is the distance from the top edge of the layout parent
         * widget, to the local Y coordinate of the hit test query.
         */
        y: number;
        /**
         * The local coordinate of the top edge of the tab area.
         *
         * #### Notes
         * This is the distance from the top edge of the layout parent
         * widget, to the top edge of the tab area.
         */
        top: number;
        /**
         * The local coordinate of the left edge of the tab area.
         *
         * #### Notes
         * This is the distance from the left edge of the layout parent
         * widget, to the left edge of the tab area.
         */
        left: number;
        /**
         * The local coordinate of the right edge of the tab area.
         *
         * #### Notes
         * This is the distance from the right edge of the layout parent
         * widget, to the right edge of the tab area.
         */
        right: number;
        /**
         * The local coordinate of the bottom edge of the tab area.
         *
         * #### Notes
         * This is the distance from the bottom edge of the layout parent
         * widget, to the bottom edge of the tab area.
         */
        bottom: number;
        /**
         * The width of the tab area.
         *
         * #### Notes
         * This is total width allocated for the tab area.
         */
        width: number;
        /**
         * The height of the tab area.
         *
         * #### Notes
         * This is total height allocated for the tab area.
         */
        height: number;
    }
}
