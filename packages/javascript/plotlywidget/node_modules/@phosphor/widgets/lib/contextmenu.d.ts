import { CommandRegistry } from '@phosphor/commands';
import { IDisposable } from '@phosphor/disposable';
import { Menu } from './menu';
/**
 * An object which implements a universal context menu.
 *
 * #### Notes
 * The items shown in the context menu are determined by CSS selector
 * matching against the DOM hierarchy at the site of the mouse click.
 * This is similar in concept to how keyboard shortcuts are matched
 * in the command registry.
 */
export declare class ContextMenu {
    /**
     * Construct a new context menu.
     *
     * @param options - The options for initializing the menu.
     */
    constructor(options: ContextMenu.IOptions);
    /**
     * The menu widget which displays the matched context items.
     */
    readonly menu: Menu;
    /**
     * Add an item to the context menu.
     *
     * @param options - The options for creating the item.
     *
     * @returns A disposable which will remove the item from the menu.
     */
    addItem(options: ContextMenu.IItemOptions): IDisposable;
    /**
     * Open the context menu in response to a `'contextmenu'` event.
     *
     * @param event - The `'contextmenu'` event of interest.
     *
     * @returns `true` if the menu was opened, or `false` if no items
     *   matched the event and the menu was not opened.
     *
     * #### Notes
     * This method will populate the context menu with items which match
     * the propagation path of the event, then open the menu at the mouse
     * position indicated by the event.
     */
    open(event: MouseEvent): boolean;
    private _idTick;
    private _items;
}
/**
 * The namespace for the `ContextMenu` class statics.
 */
export declare namespace ContextMenu {
    /**
     * An options object for initializing a context menu.
     */
    interface IOptions {
        /**
         * The command registry to use with the context menu.
         */
        commands: CommandRegistry;
        /**
         * A custom renderer for use with the context menu.
         */
        renderer?: Menu.IRenderer;
    }
    /**
     * An options object for creating a context menu item.
     */
    interface IItemOptions extends Menu.IItemOptions {
        /**
         * The CSS selector for the context menu item.
         *
         * The context menu item will only be displayed in the context menu
         * when the selector matches a node on the propagation path of the
         * contextmenu event. This allows the menu item to be restricted to
         * user-defined contexts.
         *
         * The selector must not contain commas.
         */
        selector: string;
        /**
         * The rank for the item.
         *
         * The rank is used as a tie-breaker when ordering context menu
         * items for display. Items are sorted in the following order:
         *   1. Depth in the DOM tree (deeper is better)
         *   2. Selector specificity (higher is better)
         *   3. Rank (lower is better)
         *   4. Insertion order
         *
         * The default rank is `Infinity`.
         */
        rank?: number;
    }
}
