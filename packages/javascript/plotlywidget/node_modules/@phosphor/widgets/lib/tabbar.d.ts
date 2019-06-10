import { Message } from '@phosphor/messaging';
import { ISignal } from '@phosphor/signaling';
import { ElementDataset, ElementInlineStyle, VirtualElement } from '@phosphor/virtualdom';
import { Title } from './title';
import { Widget } from './widget';
/**
 * A widget which displays titles as a single row or column of tabs.
 *
 * #### Notes
 * If CSS transforms are used to rotate nodes for vertically oriented
 * text, then tab dragging will not work correctly. The `tabsMovable`
 * property should be set to `false` when rotating nodes from CSS.
 */
export declare class TabBar<T> extends Widget {
    /**
     * Construct a new tab bar.
     *
     * @param options - The options for initializing the tab bar.
     */
    constructor(options?: TabBar.IOptions<T>);
    /**
     * Dispose of the resources held by the widget.
     */
    dispose(): void;
    /**
     * A signal emitted when the current tab is changed.
     *
     * #### Notes
     * This signal is emitted when the currently selected tab is changed
     * either through user or programmatic interaction.
     *
     * Notably, this signal is not emitted when the index of the current
     * tab changes due to tabs being inserted, removed, or moved. It is
     * only emitted when the actual current tab node is changed.
     */
    readonly currentChanged: ISignal<this, TabBar.ICurrentChangedArgs<T>>;
    /**
     * A signal emitted when a tab is moved by the user.
     *
     * #### Notes
     * This signal is emitted when a tab is moved by user interaction.
     *
     * This signal is not emitted when a tab is moved programmatically.
     */
    readonly tabMoved: ISignal<this, TabBar.ITabMovedArgs<T>>;
    /**
     * A signal emitted when a tab is clicked by the user.
     *
     * #### Notes
     * If the clicked tab is not the current tab, the clicked tab will be
     * made current and the `currentChanged` signal will be emitted first.
     *
     * This signal is emitted even if the clicked tab is the current tab.
     */
    readonly tabActivateRequested: ISignal<this, TabBar.ITabActivateRequestedArgs<T>>;
    /**
     * A signal emitted when a tab close icon is clicked.
     *
     * #### Notes
     * This signal is not emitted unless the tab title is `closable`.
     */
    readonly tabCloseRequested: ISignal<this, TabBar.ITabCloseRequestedArgs<T>>;
    /**
     * A signal emitted when a tab is dragged beyond the detach threshold.
     *
     * #### Notes
     * This signal is emitted when the user drags a tab with the mouse,
     * and mouse is dragged beyond the detach threshold.
     *
     * The consumer of the signal should call `releaseMouse` and remove
     * the tab in order to complete the detach.
     *
     * This signal is only emitted once per drag cycle.
     */
    readonly tabDetachRequested: ISignal<this, TabBar.ITabDetachRequestedArgs<T>>;
    /**
     * The renderer used by the tab bar.
     */
    readonly renderer: TabBar.IRenderer<T>;
    /**
     * Whether the tabs are movable by the user.
     *
     * #### Notes
     * Tabs can always be moved programmatically.
     */
    tabsMovable: boolean;
    /**
     * Whether a tab can be deselected by the user.
     *
     * #### Notes
     * Tabs can be always be deselected programmatically.
     */
    allowDeselect: boolean;
    /**
     * The selection behavior when inserting a tab.
     */
    insertBehavior: TabBar.InsertBehavior;
    /**
     * The selection behavior when removing a tab.
     */
    removeBehavior: TabBar.RemoveBehavior;
    /**
     * Get the currently selected title.
     *
     * #### Notes
     * This will be `null` if no tab is selected.
     */
    /**
     * Set the currently selected title.
     *
     * #### Notes
     * If the title does not exist, the title will be set to `null`.
     */
    currentTitle: Title<T> | null;
    /**
     * Get the index of the currently selected tab.
     *
     * #### Notes
     * This will be `-1` if no tab is selected.
     */
    /**
     * Set the index of the currently selected tab.
     *
     * #### Notes
     * If the value is out of range, the index will be set to `-1`.
     */
    currentIndex: number;
    /**
     * Get the orientation of the tab bar.
     *
     * #### Notes
     * This controls whether the tabs are arranged in a row or column.
     */
    /**
     * Set the orientation of the tab bar.
     *
     * #### Notes
     * This controls whether the tabs are arranged in a row or column.
     */
    orientation: TabBar.Orientation;
    /**
     * A read-only array of the titles in the tab bar.
     */
    readonly titles: ReadonlyArray<Title<T>>;
    /**
     * The tab bar content node.
     *
     * #### Notes
     * This is the node which holds the tab nodes.
     *
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly contentNode: HTMLUListElement;
    /**
     * Add a tab to the end of the tab bar.
     *
     * @param value - The title which holds the data for the tab,
     *   or an options object to convert to a title.
     *
     * @returns The title object added to the tab bar.
     *
     * #### Notes
     * If the title is already added to the tab bar, it will be moved.
     */
    addTab(value: Title<T> | Title.IOptions<T>): Title<T>;
    /**
     * Insert a tab into the tab bar at the specified index.
     *
     * @param index - The index at which to insert the tab.
     *
     * @param value - The title which holds the data for the tab,
     *   or an options object to convert to a title.
     *
     * @returns The title object added to the tab bar.
     *
     * #### Notes
     * The index will be clamped to the bounds of the tabs.
     *
     * If the title is already added to the tab bar, it will be moved.
     */
    insertTab(index: number, value: Title<T> | Title.IOptions<T>): Title<T>;
    /**
     * Remove a tab from the tab bar.
     *
     * @param title - The title for the tab to remove.
     *
     * #### Notes
     * This is a no-op if the title is not in the tab bar.
     */
    removeTab(title: Title<T>): void;
    /**
     * Remove the tab at a given index from the tab bar.
     *
     * @param index - The index of the tab to remove.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    removeTabAt(index: number): void;
    /**
     * Remove all tabs from the tab bar.
     */
    clearTabs(): void;
    /**
     * Release the mouse and restore the non-dragged tab positions.
     *
     * #### Notes
     * This will cause the tab bar to stop handling mouse events and to
     * restore the tabs to their non-dragged positions.
     */
    releaseMouse(): void;
    /**
     * Handle the DOM events for the tab bar.
     *
     * @param event - The DOM event sent to the tab bar.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the tab bar's DOM node.
     *
     * This should not be called directly by user code.
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
     * A message handler invoked on an `'update-request'` message.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * Handle the `'keydown'` event for the tab bar.
     */
    private _evtKeyDown(event);
    /**
     * Handle the `'mousedown'` event for the tab bar.
     */
    private _evtMouseDown(event);
    /**
     * Handle the `'mousemove'` event for the tab bar.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseup'` event for the document.
     */
    private _evtMouseUp(event);
    /**
     * Release the mouse and restore the non-dragged tab positions.
     */
    private _releaseMouse();
    /**
     * Adjust the current index for a tab insert operation.
     *
     * This method accounts for the tab bar's insertion behavior when
     * adjusting the current index and emitting the changed signal.
     */
    private _adjustCurrentForInsert(i, title);
    /**
     * Adjust the current index for a tab move operation.
     *
     * This method will not cause the actual current tab to change.
     * It silently adjusts the index to account for the given move.
     */
    private _adjustCurrentForMove(i, j);
    /**
     * Adjust the current index for a tab remove operation.
     *
     * This method accounts for the tab bar's remove behavior when
     * adjusting the current index and emitting the changed signal.
     */
    private _adjustCurrentForRemove(i, title);
    /**
     * Handle the `changed` signal of a title object.
     */
    private _onTitleChanged(sender);
    private _currentIndex;
    private _titles;
    private _orientation;
    private _previousTitle;
    private _dragData;
    private _tabMoved;
    private _currentChanged;
    private _tabCloseRequested;
    private _tabDetachRequested;
    private _tabActivateRequested;
}
/**
 * The namespace for the `TabBar` class statics.
 */
export declare namespace TabBar {
    /**
     * A type alias for a tab bar orientation.
     */
    type Orientation = ('horizontal' | 'vertical');
    /**
     * A type alias for the selection behavior on tab insert.
     */
    type InsertBehavior = ('none' | 'select-tab' | 'select-tab-if-needed');
    /**
     * A type alias for the selection behavior on tab remove.
     */
    type RemoveBehavior = ('none' | 'select-tab-after' | 'select-tab-before' | 'select-previous-tab');
    /**
     * An options object for creating a tab bar.
     */
    interface IOptions<T> {
        /**
         * The layout orientation of the tab bar.
         *
         * The default is `horizontal`.
         */
        orientation?: TabBar.Orientation;
        /**
         * Whether the tabs are movable by the user.
         *
         * The default is `false`.
         */
        tabsMovable?: boolean;
        /**
         * Whether a tab can be deselected by the user.
         *
         * The default is `false`.
         */
        allowDeselect?: boolean;
        /**
         * The selection behavior when inserting a tab.
         *
         * The default is `'select-tab-if-needed'`.
         */
        insertBehavior?: TabBar.InsertBehavior;
        /**
         * The selection behavior when removing a tab.
         *
         * The default is `'select-tab-after'`.
         */
        removeBehavior?: TabBar.RemoveBehavior;
        /**
         * A renderer to use with the tab bar.
         *
         * The default is a shared renderer instance.
         */
        renderer?: IRenderer<T>;
    }
    /**
     * The arguments object for the `currentChanged` signal.
     */
    interface ICurrentChangedArgs<T> {
        /**
         * The previously selected index.
         */
        readonly previousIndex: number;
        /**
         * The previously selected title.
         */
        readonly previousTitle: Title<T> | null;
        /**
         * The currently selected index.
         */
        readonly currentIndex: number;
        /**
         * The currently selected title.
         */
        readonly currentTitle: Title<T> | null;
    }
    /**
     * The arguments object for the `tabMoved` signal.
     */
    interface ITabMovedArgs<T> {
        /**
         * The previous index of the tab.
         */
        readonly fromIndex: number;
        /**
         * The current index of the tab.
         */
        readonly toIndex: number;
        /**
         * The title for the tab.
         */
        readonly title: Title<T>;
    }
    /**
     * The arguments object for the `tabActivateRequested` signal.
     */
    interface ITabActivateRequestedArgs<T> {
        /**
         * The index of the tab to activate.
         */
        readonly index: number;
        /**
         * The title for the tab.
         */
        readonly title: Title<T>;
    }
    /**
     * The arguments object for the `tabCloseRequested` signal.
     */
    interface ITabCloseRequestedArgs<T> {
        /**
         * The index of the tab to close.
         */
        readonly index: number;
        /**
         * The title for the tab.
         */
        readonly title: Title<T>;
    }
    /**
     * The arguments object for the `tabDetachRequested` signal.
     */
    interface ITabDetachRequestedArgs<T> {
        /**
         * The index of the tab to detach.
         */
        readonly index: number;
        /**
         * The title for the tab.
         */
        readonly title: Title<T>;
        /**
         * The node representing the tab.
         */
        readonly tab: HTMLElement;
        /**
         * The current client X position of the mouse.
         */
        readonly clientX: number;
        /**
         * The current client Y position of the mouse.
         */
        readonly clientY: number;
    }
    /**
     * An object which holds the data to render a tab.
     */
    interface IRenderData<T> {
        /**
         * The title associated with the tab.
         */
        readonly title: Title<T>;
        /**
         * Whether the tab is the current tab.
         */
        readonly current: boolean;
        /**
         * The z-index for the tab.
         */
        readonly zIndex: number;
    }
    /**
     * A renderer for use with a tab bar.
     */
    interface IRenderer<T> {
        /**
         * A selector which matches the close icon node in a tab.
         */
        readonly closeIconSelector: string;
        /**
         * Render the virtual element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab.
         */
        renderTab(data: IRenderData<T>): VirtualElement;
    }
    /**
     * The default implementation of `IRenderer`.
     *
     * #### Notes
     * Subclasses are free to reimplement rendering methods as needed.
     */
    class Renderer implements IRenderer<any> {
        /**
         * Construct a new renderer.
         */
        constructor();
        /**
         * A selector which matches the close icon node in a tab.
         */
        readonly closeIconSelector: string;
        /**
         * Render the virtual element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab.
         */
        renderTab(data: IRenderData<any>): VirtualElement;
        /**
         * Render the icon element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab icon.
         */
        renderIcon(data: IRenderData<any>): VirtualElement;
        /**
         * Render the label element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab label.
         */
        renderLabel(data: IRenderData<any>): VirtualElement;
        /**
         * Render the close icon element for a tab.
         *
         * @param data - The data to use for rendering the tab.
         *
         * @returns A virtual element representing the tab close icon.
         */
        renderCloseIcon(data: IRenderData<any>): VirtualElement;
        /**
         * Create a unique render key for the tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The unique render key for the tab.
         *
         * #### Notes
         * This method caches the key against the tab title the first time
         * the key is generated. This enables efficient rendering of moved
         * tabs and avoids subtle hover style artifacts.
         */
        createTabKey(data: IRenderData<any>): string;
        /**
         * Create the inline style object for a tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The inline style data for the tab.
         */
        createTabStyle(data: IRenderData<any>): ElementInlineStyle;
        /**
         * Create the class name for the tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The full class name for the tab.
         */
        createTabClass(data: IRenderData<any>): string;
        /**
         * Create the dataset for a tab.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The dataset for the tab.
         */
        createTabDataset(data: IRenderData<any>): ElementDataset;
        /**
         * Create the class name for the tab icon.
         *
         * @param data - The data to use for the tab.
         *
         * @returns The full class name for the tab icon.
         */
        createIconClass(data: IRenderData<any>): string;
        private _tabID;
        private _tabKeys;
    }
    /**
     * The default `Renderer` instance.
     */
    const defaultRenderer: Renderer;
}
