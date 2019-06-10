import { IIterator } from '@phosphor/algorithm';
import { Message } from '@phosphor/messaging';
import { ISignal } from '@phosphor/signaling';
import { DockLayout } from './docklayout';
import { TabBar } from './tabbar';
import { Widget } from './widget';
/**
 * A widget which provides a flexible docking area for widgets.
 */
export declare class DockPanel extends Widget {
    /**
     * Construct a new dock panel.
     *
     * @param options - The options for initializing the panel.
     */
    constructor(options?: DockPanel.IOptions);
    /**
     * Dispose of the resources held by the panel.
     */
    dispose(): void;
    /**
     * A signal emitted when the layout configuration is modified.
     *
     * #### Notes
     * This signal is emitted whenever the current layout configuration
     * may have changed.
     *
     * This signal is emitted asynchronously in a collapsed fashion, so
     * that multiple synchronous modifications results in only a single
     * emit of the signal.
     */
    readonly layoutModified: ISignal<this, void>;
    /**
     * The overlay used by the dock panel.
     */
    readonly overlay: DockPanel.IOverlay;
    /**
     * The renderer used by the dock panel.
     */
    readonly renderer: DockPanel.IRenderer;
    /**
     * Get the spacing between the widgets.
     */
    /**
     * Set the spacing between the widgets.
     */
    spacing: number;
    /**
     * Get the mode for the dock panel.
     */
    /**
     * Set the mode for the dock panel.
     *
     * #### Notes
     * Changing the mode is a destructive operation with respect to the
     * panel's layout configuration. If layout state must be preserved,
     * save the current layout config before changing the mode.
     */
    mode: DockPanel.Mode;
    /**
     * Whether the dock panel is empty.
     */
    readonly isEmpty: boolean;
    /**
     * Create an iterator over the user widgets in the panel.
     *
     * @returns A new iterator over the user widgets in the panel.
     *
     * #### Notes
     * This iterator does not include the generated tab bars.
     */
    widgets(): IIterator<Widget>;
    /**
     * Create an iterator over the selected widgets in the panel.
     *
     * @returns A new iterator over the selected user widgets.
     *
     * #### Notes
     * This iterator yields the widgets corresponding to the current tab
     * of each tab bar in the panel.
     */
    selectedWidgets(): IIterator<Widget>;
    /**
     * Create an iterator over the tab bars in the panel.
     *
     * @returns A new iterator over the tab bars in the panel.
     *
     * #### Notes
     * This iterator does not include the user widgets.
     */
    tabBars(): IIterator<TabBar<Widget>>;
    /**
     * Create an iterator over the handles in the panel.
     *
     * @returns A new iterator over the handles in the panel.
     */
    handles(): IIterator<HTMLDivElement>;
    /**
     * Select a specific widget in the dock panel.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * This will make the widget the current widget in its tab area.
     */
    selectWidget(widget: Widget): void;
    /**
     * Activate a specified widget in the dock panel.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * This will select and activate the given widget.
     */
    activateWidget(widget: Widget): void;
    /**
     * Save the current layout configuration of the dock panel.
     *
     * @returns A new config object for the current layout state.
     *
     * #### Notes
     * The return value can be provided to the `restoreLayout` method
     * in order to restore the layout to its current configuration.
     */
    saveLayout(): DockPanel.ILayoutConfig;
    /**
     * Restore the layout to a previously saved configuration.
     *
     * @param config - The layout configuration to restore.
     *
     * #### Notes
     * Widgets which currently belong to the layout but which are not
     * contained in the config will be unparented.
     *
     * The dock panel automatically reverts to `'multiple-document'`
     * mode when a layout config is restored.
     */
    restoreLayout(config: DockPanel.ILayoutConfig): void;
    /**
     * Add a widget to the dock panel.
     *
     * @param widget - The widget to add to the dock panel.
     *
     * @param options - The additional options for adding the widget.
     *
     * #### Notes
     * If the panel is in single document mode, the options are ignored
     * and the widget is always added as tab in the hidden tab bar.
     */
    addWidget(widget: Widget, options?: DockPanel.IAddOptions): void;
    /**
     * Process a message sent to the widget.
     *
     * @param msg - The message sent to the widget.
     */
    processMessage(msg: Message): void;
    /**
     * Handle the DOM events for the dock panel.
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
     * Handle the `'p-dragenter'` event for the dock panel.
     */
    private _evtDragEnter(event);
    /**
     * Handle the `'p-dragleave'` event for the dock panel.
     */
    private _evtDragLeave(event);
    /**
     * Handle the `'p-dragover'` event for the dock panel.
     */
    private _evtDragOver(event);
    /**
     * Handle the `'p-drop'` event for the dock panel.
     */
    private _evtDrop(event);
    /**
     * Handle the `'keydown'` event for the dock panel.
     */
    private _evtKeyDown(event);
    /**
     * Handle the `'mousedown'` event for the dock panel.
     */
    private _evtMouseDown(event);
    /**
     * Handle the `'mousemove'` event for the dock panel.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseup'` event for the dock panel.
     */
    private _evtMouseUp(event);
    /**
     * Release the mouse grab for the dock panel.
     */
    private _releaseMouse();
    /**
     * Show the overlay indicator at the given client position.
     *
     * Returns the drop zone at the specified client position.
     *
     * #### Notes
     * If the position is not over a valid zone, the overlay is hidden.
     */
    private _showOverlay(clientX, clientY);
    /**
     * Create a new tab bar for use by the panel.
     */
    private _createTabBar();
    /**
     * Create a new handle for use by the panel.
     */
    private _createHandle();
    /**
     * Handle the `tabMoved` signal from a tab bar.
     */
    private _onTabMoved();
    /**
     * Handle the `currentChanged` signal from a tab bar.
     */
    private _onCurrentChanged(sender, args);
    /**
     * Handle the `tabActivateRequested` signal from a tab bar.
     */
    private _onTabActivateRequested(sender, args);
    /**
     * Handle the `tabCloseRequested` signal from a tab bar.
     */
    private _onTabCloseRequested(sender, args);
    /**
     * Handle the `tabDetachRequested` signal from a tab bar.
     */
    private _onTabDetachRequested(sender, args);
    private _mode;
    private _drag;
    private _renderer;
    private _pressData;
    private _layoutModified;
}
/**
 * The namespace for the `DockPanel` class statics.
 */
export declare namespace DockPanel {
    /**
     * An options object for creating a dock panel.
     */
    interface IOptions {
        /**
         * The overlay to use with the dock panel.
         *
         * The default is a new `Overlay` instance.
         */
        overlay?: IOverlay;
        /**
         * The renderer to use for the dock panel.
         *
         * The default is a shared renderer instance.
         */
        renderer?: IRenderer;
        /**
         * The spacing between the items in the panel.
         *
         * The default is `4`.
         */
        spacing?: number;
        /**
         * The mode for the dock panel.
         *
         * The deafult is `'multiple-document'`.
         */
        mode?: DockPanel.Mode;
    }
    /**
     * A type alias for the supported dock panel modes.
     */
    type Mode = ('single-document' | 'multiple-document');
    /**
     * A type alias for a layout configuration object.
     */
    type ILayoutConfig = DockLayout.ILayoutConfig;
    /**
     * A type alias for the supported insertion modes.
     */
    type InsertMode = DockLayout.InsertMode;
    /**
     * A type alias for the add widget options.
     */
    type IAddOptions = DockLayout.IAddOptions;
    /**
     * An object which holds the geometry for overlay positioning.
     */
    interface IOverlayGeometry {
        /**
         * The distance between the overlay and parent top edges.
         */
        top: number;
        /**
         * The distance between the overlay and parent left edges.
         */
        left: number;
        /**
         * The distance between the overlay and parent right edges.
         */
        right: number;
        /**
         * The distance between the overlay and parent bottom edges.
         */
        bottom: number;
    }
    /**
     * An object which manages the overlay node for a dock panel.
     */
    interface IOverlay {
        /**
         * The DOM node for the overlay.
         */
        readonly node: HTMLDivElement;
        /**
         * Show the overlay using the given overlay geometry.
         *
         * @param geo - The desired geometry for the overlay.
         *
         * #### Notes
         * The given geometry values assume the node will use absolute
         * positioning.
         *
         * This is called on every mouse move event during a drag in order
         * to update the position of the overlay. It should be efficient.
         */
        show(geo: IOverlayGeometry): void;
        /**
         * Hide the overlay node.
         *
         * @param delay - The delay (in ms) before hiding the overlay.
         *   A delay value <= 0 should hide the overlay immediately.
         *
         * #### Notes
         * This is called whenever the overlay node should been hidden.
         */
        hide(delay: number): void;
    }
    /**
     * A concrete implementation of `IOverlay`.
     *
     * This is the default overlay implementation for a dock panel.
     */
    class Overlay implements IOverlay {
        /**
         * Construct a new overlay.
         */
        constructor();
        /**
         * The DOM node for the overlay.
         */
        readonly node: HTMLDivElement;
        /**
         * Show the overlay using the given overlay geometry.
         *
         * @param geo - The desired geometry for the overlay.
         */
        show(geo: IOverlayGeometry): void;
        /**
         * Hide the overlay node.
         *
         * @param delay - The delay (in ms) before hiding the overlay.
         *   A delay value <= 0 will hide the overlay immediately.
         */
        hide(delay: number): void;
        private _timer;
        private _hidden;
    }
    /**
     * A type alias for a dock panel renderer;
     */
    type IRenderer = DockLayout.IRenderer;
    /**
     * The default implementation of `IRenderer`.
     */
    class Renderer implements IRenderer {
        /**
         * Create a new tab bar for use with a dock panel.
         *
         * @returns A new tab bar for a dock panel.
         */
        createTabBar(): TabBar<Widget>;
        /**
         * Create a new handle node for use with a dock panel.
         *
         * @returns A new handle node for a dock panel.
         */
        createHandle(): HTMLDivElement;
    }
    /**
     * The default `Renderer` instance.
     */
    const defaultRenderer: Renderer;
}
