import { ISignal } from '@phosphor/signaling';
import { StackedPanel } from './stackedpanel';
import { TabBar } from './tabbar';
import { Widget } from './widget';
/**
 * A widget which combines a `TabBar` and a `StackedPanel`.
 *
 * #### Notes
 * This is a simple panel which handles the common case of a tab bar
 * placed next to a content area. The selected tab controls the widget
 * which is shown in the content area.
 *
 * For use cases which require more control than is provided by this
 * panel, the `TabBar` widget may be used independently.
 */
export declare class TabPanel extends Widget {
    /**
     * Construct a new tab panel.
     *
     * @param options - The options for initializing the tab panel.
     */
    constructor(options?: TabPanel.IOptions);
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
    readonly currentChanged: ISignal<this, TabPanel.ICurrentChangedArgs>;
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
     * If the index is out of range, it will be set to `-1`.
     */
    currentIndex: number;
    /**
     * Get the currently selected widget.
     *
     * #### Notes
     * This will be `null` if there is no selected tab.
     */
    /**
     * Set the currently selected widget.
     *
     * #### Notes
     * If the widget is not in the panel, it will be set to `null`.
     */
    currentWidget: Widget | null;
    /**
     * Get the whether the tabs are movable by the user.
     *
     * #### Notes
     * Tabs can always be moved programmatically.
     */
    /**
     * Set the whether the tabs are movable by the user.
     *
     * #### Notes
     * Tabs can always be moved programmatically.
     */
    tabsMovable: boolean;
    /**
     * Get the tab placement for the tab panel.
     *
     * #### Notes
     * This controls the position of the tab bar relative to the content.
     */
    /**
     * Set the tab placement for the tab panel.
     *
     * #### Notes
     * This controls the position of the tab bar relative to the content.
     */
    tabPlacement: TabPanel.TabPlacement;
    /**
     * The tab bar used by the tab panel.
     *
     * #### Notes
     * Modifying the tab bar directly can lead to undefined behavior.
     */
    readonly tabBar: TabBar<Widget>;
    /**
     * The stacked panel used by the tab panel.
     *
     * #### Notes
     * Modifying the panel directly can lead to undefined behavior.
     */
    readonly stackedPanel: StackedPanel;
    /**
     * A read-only array of the widgets in the panel.
     */
    readonly widgets: ReadonlyArray<Widget>;
    /**
     * Add a widget to the end of the tab panel.
     *
     * @param widget - The widget to add to the tab panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     *
     * The widget's `title` is used to populate the tab.
     */
    addWidget(widget: Widget): void;
    /**
     * Insert a widget into the tab panel at a specified index.
     *
     * @param index - The index at which to insert the widget.
     *
     * @param widget - The widget to insert into to the tab panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     *
     * The widget's `title` is used to populate the tab.
     */
    insertWidget(index: number, widget: Widget): void;
    /**
     * Handle the `currentChanged` signal from the tab bar.
     */
    private _onCurrentChanged(sender, args);
    /**
     * Handle the `tabActivateRequested` signal from the tab bar.
     */
    private _onTabActivateRequested(sender, args);
    /**
     * Handle the `tabCloseRequested` signal from the tab bar.
     */
    private _onTabCloseRequested(sender, args);
    /**
     * Handle the `tabMoved` signal from the tab bar.
     */
    private _onTabMoved(sender, args);
    /**
     * Handle the `widgetRemoved` signal from the stacked panel.
     */
    private _onWidgetRemoved(sender, widget);
    private _tabPlacement;
    private _currentChanged;
}
/**
 * The namespace for the `TabPanel` class statics.
 */
export declare namespace TabPanel {
    /**
     * A type alias for tab placement in a tab bar.
     */
    type TabPlacement = ('top' | 'left' | 'right' | 'bottom');
    /**
     * An options object for initializing a tab panel.
     */
    interface IOptions {
        /**
         * Whether the tabs are movable by the user.
         *
         * The default is `false`.
         */
        tabsMovable?: boolean;
        /**
         * The placement of the tab bar relative to the content.
         *
         * The default is `'top'`.
         */
        tabPlacement?: TabPlacement;
        /**
         * The renderer for the panel's tab bar.
         *
         * The default is a shared renderer instance.
         */
        renderer?: TabBar.IRenderer<Widget>;
    }
    /**
     * The arguments object for the `currentChanged` signal.
     */
    interface ICurrentChangedArgs {
        /**
         * The previously selected index.
         */
        previousIndex: number;
        /**
         * The previously selected widget.
         */
        previousWidget: Widget | null;
        /**
         * The currently selected index.
         */
        currentIndex: number;
        /**
         * The currently selected widget.
         */
        currentWidget: Widget | null;
    }
}
