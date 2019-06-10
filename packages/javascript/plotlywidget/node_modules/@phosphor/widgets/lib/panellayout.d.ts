import { IIterator } from '@phosphor/algorithm';
import { Layout } from './layout';
import { Widget } from './widget';
/**
 * A concrete layout implementation suitable for many use cases.
 *
 * #### Notes
 * This class is suitable as a base class for implementing a variety of
 * layouts, but can also be used directly with standard CSS to layout a
 * collection of widgets.
 */
export declare class PanelLayout extends Layout {
    /**
     * Dispose of the resources held by the layout.
     *
     * #### Notes
     * This will clear and dispose all widgets in the layout.
     *
     * All reimplementations should call the superclass method.
     *
     * This method is called automatically when the parent is disposed.
     */
    dispose(): void;
    /**
     * A read-only array of the widgets in the layout.
     */
    readonly widgets: ReadonlyArray<Widget>;
    /**
     * Create an iterator over the widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     */
    iter(): IIterator<Widget>;
    /**
     * Add a widget to the end of the layout.
     *
     * @param widget - The widget to add to the layout.
     *
     * #### Notes
     * If the widget is already contained in the layout, it will be moved.
     */
    addWidget(widget: Widget): void;
    /**
     * Insert a widget into the layout at the specified index.
     *
     * @param index - The index at which to insert the widget.
     *
     * @param widget - The widget to insert into the layout.
     *
     * #### Notes
     * The index will be clamped to the bounds of the widgets.
     *
     * If the widget is already added to the layout, it will be moved.
     *
     * #### Undefined Behavior
     * An `index` which is non-integral.
     */
    insertWidget(index: number, widget: Widget): void;
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
     * Remove the widget at a given index from the layout.
     *
     * @param index - The index of the widget to remove.
     *
     * #### Notes
     * A widget is automatically removed from the layout when its `parent`
     * is set to `null`. This method should only be invoked directly when
     * removing a widget from a layout which has yet to be installed on a
     * parent widget.
     *
     * This method does *not* modify the widget's `parent`.
     *
     * #### Undefined Behavior
     * An `index` which is non-integral.
     */
    removeWidgetAt(index: number): void;
    /**
     * Perform layout initialization which requires the parent widget.
     */
    protected init(): void;
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param index - The current index of the widget in the layout.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This method is called automatically by the panel layout at the
     * appropriate time. It should not be called directly by user code.
     *
     * The default implementation adds the widgets's node to the parent's
     * node at the proper location, and sends the appropriate attach
     * messages to the widget if the parent is attached to the DOM.
     *
     * Subclasses may reimplement this method to control how the widget's
     * node is added to the parent's node.
     */
    protected attachWidget(index: number, widget: Widget): void;
    /**
     * Move a widget in the parent's DOM node.
     *
     * @param fromIndex - The previous index of the widget in the layout.
     *
     * @param toIndex - The current index of the widget in the layout.
     *
     * @param widget - The widget to move in the parent.
     *
     * #### Notes
     * This method is called automatically by the panel layout at the
     * appropriate time. It should not be called directly by user code.
     *
     * The default implementation moves the widget's node to the proper
     * location in the parent's node and sends the appropriate attach and
     * detach messages to the widget if the parent is attached to the DOM.
     *
     * Subclasses may reimplement this method to control how the widget's
     * node is moved in the parent's node.
     */
    protected moveWidget(fromIndex: number, toIndex: number, widget: Widget): void;
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param index - The previous index of the widget in the layout.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This method is called automatically by the panel layout at the
     * appropriate time. It should not be called directly by user code.
     *
     * The default implementation removes the widget's node from the
     * parent's node, and sends the appropriate detach messages to the
     * widget if the parent is attached to the DOM.
     *
     * Subclasses may reimplement this method to control how the widget's
     * node is removed from the parent's node.
     */
    protected detachWidget(index: number, widget: Widget): void;
    private _widgets;
}
