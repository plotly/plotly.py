import { CommandRegistry } from '@phosphor/commands';
import { ReadonlyJSONObject } from '@phosphor/coreutils';
import { Message } from '@phosphor/messaging';
import { ISignal } from '@phosphor/signaling';
import { ElementDataset, VirtualElement, h } from '@phosphor/virtualdom';
import { Widget } from './widget';
/**
 * A widget which displays items as a canonical menu.
 */
export declare class Menu extends Widget {
    /**
     * Construct a new menu.
     *
     * @param options - The options for initializing the menu.
     */
    constructor(options: Menu.IOptions);
    /**
     * Dispose of the resources held by the menu.
     */
    dispose(): void;
    /**
     * A signal emitted just before the menu is closed.
     *
     * #### Notes
     * This signal is emitted when the menu receives a `'close-request'`
     * message, just before it removes itself from the DOM.
     *
     * This signal is not emitted if the menu is already detached from
     * the DOM when it receives the `'close-request'` message.
     */
    readonly aboutToClose: ISignal<this, void>;
    /**
     * A signal emitted when a new menu is requested by the user.
     *
     * #### Notes
     * This signal is emitted whenever the user presses the right or left
     * arrow keys, and a submenu cannot be opened or closed in response.
     *
     * This signal is useful when implementing menu bars in order to open
     * the next or previous menu in response to a user key press.
     *
     * This signal is only emitted for the root menu in a hierarchy.
     */
    readonly menuRequested: ISignal<this, 'next' | 'previous'>;
    /**
     * The command registry used by the menu.
     */
    readonly commands: CommandRegistry;
    /**
     * The renderer used by the menu.
     */
    readonly renderer: Menu.IRenderer;
    /**
     * The parent menu of the menu.
     *
     * #### Notes
     * This is `null` unless the menu is an open submenu.
     */
    readonly parentMenu: Menu | null;
    /**
     * The child menu of the menu.
     *
     * #### Notes
     * This is `null` unless the menu has an open submenu.
     */
    readonly childMenu: Menu | null;
    /**
     * The root menu of the menu hierarchy.
     */
    readonly rootMenu: Menu;
    /**
     * The leaf menu of the menu hierarchy.
     */
    readonly leafMenu: Menu;
    /**
     * The menu content node.
     *
     * #### Notes
     * This is the node which holds the menu item nodes.
     *
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly contentNode: HTMLUListElement;
    /**
     * Get the currently active menu item.
     */
    /**
     * Set the currently active menu item.
     *
     * #### Notes
     * If the item cannot be activated, the item will be set to `null`.
     */
    activeItem: Menu.IItem | null;
    /**
     * Get the index of the currently active menu item.
     *
     * #### Notes
     * This will be `-1` if no menu item is active.
     */
    /**
     * Set the index of the currently active menu item.
     *
     * #### Notes
     * If the item cannot be activated, the index will be set to `-1`.
     */
    activeIndex: number;
    /**
     * A read-only array of the menu items in the menu.
     */
    readonly items: ReadonlyArray<Menu.IItem>;
    /**
     * Activate the next selectable item in the menu.
     *
     * #### Notes
     * If no item is selectable, the index will be set to `-1`.
     */
    activateNextItem(): void;
    /**
     * Activate the previous selectable item in the menu.
     *
     * #### Notes
     * If no item is selectable, the index will be set to `-1`.
     */
    activatePreviousItem(): void;
    /**
     * Trigger the active menu item.
     *
     * #### Notes
     * If the active item is a submenu, it will be opened and the first
     * item will be activated.
     *
     * If the active item is a command, the command will be executed.
     *
     * If the menu is not attached, this is a no-op.
     *
     * If there is no active item, this is a no-op.
     */
    triggerActiveItem(): void;
    /**
     * Add a menu item to the end of the menu.
     *
     * @param options - The options for creating the menu item.
     *
     * @returns The menu item added to the menu.
     */
    addItem(options: Menu.IItemOptions): Menu.IItem;
    /**
     * Insert a menu item into the menu at the specified index.
     *
     * @param index - The index at which to insert the item.
     *
     * @param options - The options for creating the menu item.
     *
     * @returns The menu item added to the menu.
     *
     * #### Notes
     * The index will be clamped to the bounds of the items.
     */
    insertItem(index: number, options: Menu.IItemOptions): Menu.IItem;
    /**
     * Remove an item from the menu.
     *
     * @param item - The item to remove from the menu.
     *
     * #### Notes
     * This is a no-op if the item is not in the menu.
     */
    removeItem(item: Menu.IItem): void;
    /**
     * Remove the item at a given index from the menu.
     *
     * @param index - The index of the item to remove.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    removeItemAt(index: number): void;
    /**
     * Remove all menu items from the menu.
     */
    clearItems(): void;
    /**
     * Open the menu at the specified location.
     *
     * @param x - The client X coordinate of the menu location.
     *
     * @param y - The client Y coordinate of the menu location.
     *
     * @param options - The additional options for opening the menu.
     *
     * #### Notes
     * The menu will be opened at the given location unless it will not
     * fully fit on the screen. If it will not fit, it will be adjusted
     * to fit naturally on the screen.
     *
     * This is a no-op if the menu is already attached to the DOM.
     */
    open(x: number, y: number, options?: Menu.IOpenOptions): void;
    /**
     * Handle the DOM events for the menu.
     *
     * @param event - The DOM event sent to the menu.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the menu's DOM nodes. It should
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
     * A message handler invoked on an `'activate-request'` message.
     */
    protected onActivateRequest(msg: Message): void;
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * A message handler invoked on a `'close-request'` message.
     */
    protected onCloseRequest(msg: Message): void;
    /**
     * Handle the `'keydown'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    private _evtKeyDown(event);
    /**
     * Handle the `'mouseup'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    private _evtMouseUp(event);
    /**
     * Handle the `'mousemove'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseenter'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    private _evtMouseEnter(event);
    /**
     * Handle the `'mouseleave'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the menu node.
     */
    private _evtMouseLeave(event);
    /**
     * Handle the `'mousedown'` event for the menu.
     *
     * #### Notes
     * This listener is attached to the document node.
     */
    private _evtMouseDown(event);
    /**
     * Open the child menu at the active index immediately.
     *
     * If a different child menu is already open, it will be closed,
     * even if the active item is not a valid submenu.
     */
    private _openChildMenu(activateFirst?);
    /**
     * Close the child menu immediately.
     *
     * This is a no-op if a child menu is not open.
     */
    private _closeChildMenu();
    /**
     * Start the open timer, unless it is already pending.
     */
    private _startOpenTimer();
    /**
     * Start the close timer, unless it is already pending.
     */
    private _startCloseTimer();
    /**
     * Cancel the open timer, if the timer is pending.
     */
    private _cancelOpenTimer();
    /**
     * Cancel the close timer, if the timer is pending.
     */
    private _cancelCloseTimer();
    private _childIndex;
    private _activeIndex;
    private _openTimerID;
    private _closeTimerID;
    private _items;
    private _childMenu;
    private _parentMenu;
    private _aboutToClose;
    private _menuRequested;
}
/**
 * The namespace for the `Menu` class statics.
 */
export declare namespace Menu {
    /**
     * An options object for creating a menu.
     */
    interface IOptions {
        /**
         * The command registry for use with the menu.
         */
        commands: CommandRegistry;
        /**
         * A custom renderer for use with the menu.
         *
         * The default is a shared renderer instance.
         */
        renderer?: IRenderer;
    }
    /**
     * An options object for the `open` method on a menu.
     */
    interface IOpenOptions {
        /**
         * Whether to force the X position of the menu.
         *
         * Setting to `true` will disable the logic which repositions the
         * X coordinate of the menu if it will not fit entirely on screen.
         *
         * The default is `false`.
         */
        forceX?: boolean;
        /**
         * Whether to force the Y position of the menu.
         *
         * Setting to `true` will disable the logic which repositions the
         * Y coordinate of the menu if it will not fit entirely on screen.
         *
         * The default is `false`.
         */
        forceY?: boolean;
    }
    /**
     * A type alias for a menu item type.
     */
    type ItemType = 'command' | 'submenu' | 'separator';
    /**
     * An options object for creating a menu item.
     */
    interface IItemOptions {
        /**
         * The type of the menu item.
         *
         * The default value is `'command'`.
         */
        type?: ItemType;
        /**
         * The command to execute when the item is triggered.
         *
         * The default value is an empty string.
         */
        command?: string;
        /**
         * The arguments for the command.
         *
         * The default value is an empty object.
         */
        args?: ReadonlyJSONObject;
        /**
         * The submenu for a `'submenu'` type item.
         *
         * The default value is `null`.
         */
        submenu?: Menu | null;
    }
    /**
     * An object which represents a menu item.
     *
     * #### Notes
     * Item objects are created automatically by a menu.
     */
    interface IItem {
        /**
         * The type of the menu item.
         */
        readonly type: ItemType;
        /**
         * The command to execute when the item is triggered.
         */
        readonly command: string;
        /**
         * The arguments for the command.
         */
        readonly args: ReadonlyJSONObject;
        /**
         * The submenu for a `'submenu'` type item.
         */
        readonly submenu: Menu | null;
        /**
         * The display label for the menu item.
         */
        readonly label: string;
        /**
         * The mnemonic index for the menu item.
         */
        readonly mnemonic: number;
        /**
         * @deprecated Use `iconClass` instead.
         */
        readonly icon: string;
        /**
         * The icon class for the menu item.
         */
        readonly iconClass: string;
        /**
         * The icon label for the menu item.
         */
        readonly iconLabel: string;
        /**
         * The display caption for the menu item.
         */
        readonly caption: string;
        /**
         * The extra class name for the menu item.
         */
        readonly className: string;
        /**
         * The dataset for the menu item.
         */
        readonly dataset: CommandRegistry.Dataset;
        /**
         * Whether the menu item is enabled.
         */
        readonly isEnabled: boolean;
        /**
         * Whether the menu item is toggled.
         */
        readonly isToggled: boolean;
        /**
         * Whether the menu item is visible.
         */
        readonly isVisible: boolean;
        /**
         * The key binding for the menu item.
         */
        readonly keyBinding: CommandRegistry.IKeyBinding | null;
    }
    /**
     * An object which holds the data to render a menu item.
     */
    interface IRenderData {
        /**
         * The item to be rendered.
         */
        readonly item: IItem;
        /**
         * Whether the item is the active item.
         */
        readonly active: boolean;
        /**
         * Whether the item should be collapsed.
         */
        readonly collapsed: boolean;
    }
    /**
     * A renderer for use with a menu.
     */
    interface IRenderer {
        /**
         * Render the virtual element for a menu item.
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
         * Render the virtual element for a menu item.
         *
         * @param data - The data to use for rendering the item.
         *
         * @returns A virtual element representing the item.
         */
        renderItem(data: IRenderData): VirtualElement;
        /**
         * Render the icon element for a menu item.
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
         * Render the shortcut element for a menu item.
         *
         * @param data - The data to use for rendering the shortcut.
         *
         * @returns A virtual element representing the item shortcut.
         */
        renderShortcut(data: IRenderData): VirtualElement;
        /**
         * Render the submenu icon element for a menu item.
         *
         * @param data - The data to use for rendering the submenu icon.
         *
         * @returns A virtual element representing the submenu icon.
         */
        renderSubmenu(data: IRenderData): VirtualElement;
        /**
         * Create the class name for the menu item.
         *
         * @param data - The data to use for the class name.
         *
         * @returns The full class name for the menu item.
         */
        createItemClass(data: IRenderData): string;
        /**
         * Create the dataset for the menu item.
         *
         * @param data - The data to use for creating the dataset.
         *
         * @returns The dataset for the menu item.
         */
        createItemDataset(data: IRenderData): ElementDataset;
        /**
         * Create the class name for the menu item icon.
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
        /**
         * Create the render content for the shortcut node.
         *
         * @param data - The data to use for the shortcut content.
         *
         * @returns The content to add to the shortcut node.
         */
        formatShortcut(data: IRenderData): h.Child;
    }
    /**
     * The default `Renderer` instance.
     */
    const defaultRenderer: Renderer;
}
