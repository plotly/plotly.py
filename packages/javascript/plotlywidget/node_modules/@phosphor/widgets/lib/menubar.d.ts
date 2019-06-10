import { Message } from '@phosphor/messaging';
import { ElementDataset, VirtualElement, h } from '@phosphor/virtualdom';
import { Menu } from './menu';
import { Title } from './title';
import { Widget } from './widget';
/**
 * A widget which displays menus as a canonical menu bar.
 */
export declare class MenuBar extends Widget {
    /**
     * Construct a new menu bar.
     *
     * @param options - The options for initializing the menu bar.
     */
    constructor(options?: MenuBar.IOptions);
    /**
     * Dispose of the resources held by the widget.
     */
    dispose(): void;
    /**
     * The renderer used by the menu bar.
     */
    readonly renderer: MenuBar.IRenderer;
    /**
     * The child menu of the menu bar.
     *
     * #### Notes
     * This will be `null` if the menu bar does not have an open menu.
     */
    readonly childMenu: Menu | null;
    /**
     * Get the menu bar content node.
     *
     * #### Notes
     * This is the node which holds the menu title nodes.
     *
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly contentNode: HTMLUListElement;
    /**
     * Get the currently active menu.
     */
    /**
     * Set the currently active menu.
     *
     * #### Notes
     * If the menu does not exist, the menu will be set to `null`.
     */
    activeMenu: Menu | null;
    /**
     * Get the index of the currently active menu.
     *
     * #### Notes
     * This will be `-1` if no menu is active.
     */
    /**
     * Set the index of the currently active menu.
     *
     * #### Notes
     * If the menu cannot be activated, the index will be set to `-1`.
     */
    activeIndex: number;
    /**
     * A read-only array of the menus in the menu bar.
     */
    readonly menus: ReadonlyArray<Menu>;
    /**
     * Open the active menu and activate its first menu item.
     *
     * #### Notes
     * If there is no active menu, this is a no-op.
     */
    openActiveMenu(): void;
    /**
     * Add a menu to the end of the menu bar.
     *
     * @param menu - The menu to add to the menu bar.
     *
     * #### Notes
     * If the menu is already added to the menu bar, it will be moved.
     */
    addMenu(menu: Menu): void;
    /**
     * Insert a menu into the menu bar at the specified index.
     *
     * @param index - The index at which to insert the menu.
     *
     * @param menu - The menu to insert into the menu bar.
     *
     * #### Notes
     * The index will be clamped to the bounds of the menus.
     *
     * If the menu is already added to the menu bar, it will be moved.
     */
    insertMenu(index: number, menu: Menu): void;
    /**
     * Remove a menu from the menu bar.
     *
     * @param menu - The menu to remove from the menu bar.
     *
     * #### Notes
     * This is a no-op if the menu is not in the menu bar.
     */
    removeMenu(menu: Menu): void;
    /**
     * Remove the menu at a given index from the menu bar.
     *
     * @param index - The index of the menu to remove.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    removeMenuAt(index: number): void;
    /**
     * Remove all menus from the menu bar.
     */
    clearMenus(): void;
    /**
     * Handle the DOM events for the menu bar.
     *
     * @param event - The DOM event sent to the menu bar.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the menu bar's DOM nodes. It
     * should not be called directly by user code.
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
     * A message handler invoked on an `'activate-request'` message.
     */
    protected onActivateRequest(msg: Message): void;
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * Handle the `'keydown'` event for the menu bar.
     */
    private _evtKeyDown(event);
    /**
     * Handle the `'mousedown'` event for the menu bar.
     */
    private _evtMouseDown(event);
    /**
     * Handle the `'mousemove'` event for the menu bar.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseleave'` event for the menu bar.
     */
    private _evtMouseLeave(event);
    /**
     * Open the child menu at the active index immediately.
     *
     * If a different child menu is already open, it will be closed,
     * even if there is no active menu.
     */
    private _openChildMenu();
    /**
     * Close the child menu immediately.
     *
     * This is a no-op if a child menu is not open.
     */
    private _closeChildMenu();
    /**
     * Handle the `aboutToClose` signal of a menu.
     */
    private _onMenuAboutToClose(sender);
    /**
     * Handle the `menuRequested` signal of a child menu.
     */
    private _onMenuMenuRequested(sender, args);
    /**
     * Handle the `changed` signal of a title object.
     */
    private _onTitleChanged();
    private _activeIndex;
    private _menus;
    private _childMenu;
}
/**
 * The namespace for the `MenuBar` class statics.
 */
export declare namespace MenuBar {
    /**
     * An options object for creating a menu bar.
     */
    interface IOptions {
        /**
         * A custom renderer for creating menu bar content.
         *
         * The default is a shared renderer instance.
         */
        renderer?: IRenderer;
    }
    /**
     * An object which holds the data to render a menu bar item.
     */
    interface IRenderData {
        /**
         * The title to be rendered.
         */
        readonly title: Title<Widget>;
        /**
         * Whether the item is the active item.
         */
        readonly active: boolean;
    }
    /**
     * A renderer for use with a menu bar.
     */
    interface IRenderer {
        /**
         * Render the virtual element for a menu bar item.
         *
         * @param data - The data to use for rendering the item.
         *
         * @returns A virtual element representing the item.
         */
        renderItem(data: IRenderData): VirtualElement;
    }
    /**
     * The default implementation of `IRenderer`.
     *
     * #### Notes
     * Subclasses are free to reimplement rendering methods as needed.
     */
    class Renderer implements IRenderer {
        /**
         * Construct a new renderer.
         */
        constructor();
        /**
         * Render the virtual element for a menu bar item.
         *
         * @param data - The data to use for rendering the item.
         *
         * @returns A virtual element representing the item.
         */
        renderItem(data: IRenderData): VirtualElement;
        /**
         * Render the icon element for a menu bar item.
         *
         * @param data - The data to use for rendering the icon.
         *
         * @returns A virtual element representing the item icon.
         */
        renderIcon(data: IRenderData): VirtualElement;
        /**
         * Render the label element for a menu item.
         *
         * @param data - The data to use for rendering the label.
         *
         * @returns A virtual element representing the item label.
         */
        renderLabel(data: IRenderData): VirtualElement;
        /**
         * Create the class name for the menu bar item.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the menu item.
         */
        createItemClass(data: IRenderData): string;
        /**
         * Create the dataset for a menu bar item.
         *
         * @param data - The data to use for the item.
         *
         * @returns The dataset for the menu bar item.
         */
        createItemDataset(data: IRenderData): ElementDataset;
        /**
         * Create the class name for the menu bar item icon.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the item icon.
         */
        createIconClass(data: IRenderData): string;
        /**
         * Create the render content for the label node.
         *
         * @param data - The data to use for the label content.
         *
         * @returns The content to add to the label node.
         */
        formatLabel(data: IRenderData): h.Child;
    }
    /**
     * The default `Renderer` instance.
     */
    const defaultRenderer: Renderer;
}
