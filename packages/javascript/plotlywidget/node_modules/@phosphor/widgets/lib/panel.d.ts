import { PanelLayout } from './panellayout';
import { Widget } from './widget';
/**
 * A simple and convenient panel widget class.
 *
 * #### Notes
 * This class is suitable as a base class for implementing a variety of
 * convenience panel widgets, but can also be used directly with CSS to
 * arrange a collection of widgets.
 *
 * This class provides a convenience wrapper around a [[PanelLayout]].
 */
export declare class Panel extends Widget {
    /**
     * Construct a new panel.
     *
     * @param options - The options for initializing the panel.
     */
    constructor(options?: Panel.IOptions);
    /**
     * A read-only array of the widgets in the panel.
     */
    readonly widgets: ReadonlyArray<Widget>;
    /**
     * Add a widget to the end of the panel.
     *
     * @param widget - The widget to add to the panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     */
    addWidget(widget: Widget): void;
    /**
     * Insert a widget at the specified index.
     *
     * @param index - The index at which to insert the widget.
     *
     * @param widget - The widget to insert into to the panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     */
    insertWidget(index: number, widget: Widget): void;
}
/**
 * The namespace for the `Panel` class statics.
 */
export declare namespace Panel {
    /**
     * An options object for creating a panel.
     */
    interface IOptions {
        /**
         * The panel layout to use for the panel.
         *
         * The default is a new `PanelLayout`.
         */
        layout?: PanelLayout;
    }
}
