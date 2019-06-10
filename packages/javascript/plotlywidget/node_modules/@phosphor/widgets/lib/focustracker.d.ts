import { IDisposable } from '@phosphor/disposable';
import { ISignal } from '@phosphor/signaling';
import { Widget } from './widget';
/**
 * A class which tracks focus among a set of widgets.
 *
 * This class is useful when code needs to keep track of the most
 * recently focused widget(s) among a set of related widgets.
 */
export declare class FocusTracker<T extends Widget> implements IDisposable {
    /**
     * Construct a new focus tracker.
     */
    constructor();
    /**
     * Dispose of the resources held by the tracker.
     */
    dispose(): void;
    /**
     * A signal emitted when the current widget has changed.
     */
    readonly currentChanged: ISignal<this, FocusTracker.IChangedArgs<T>>;
    /**
     * A signal emitted when the active widget has changed.
     */
    readonly activeChanged: ISignal<this, FocusTracker.IChangedArgs<T>>;
    /**
     * A flag indicating whether the tracker is disposed.
     */
    readonly isDisposed: boolean;
    /**
     * The current widget in the tracker.
     *
     * #### Notes
     * The current widget is the widget among the tracked widgets which
     * has the *descendant node* which has most recently been focused.
     *
     * The current widget will not be updated if the node loses focus. It
     * will only be updated when a different tracked widget gains focus.
     *
     * If the current widget is removed from the tracker, the previous
     * current widget will be restored.
     *
     * This behavior is intended to follow a user's conceptual model of
     * a semantically "current" widget, where the "last thing of type X"
     * to be interacted with is the "current instance of X", regardless
     * of whether that instance still has focus.
     */
    readonly currentWidget: T | null;
    /**
     * The active widget in the tracker.
     *
     * #### Notes
     * The active widget is the widget among the tracked widgets which
     * has the *descendant node* which is currently focused.
     */
    readonly activeWidget: T | null;
    /**
     * A read only array of the widgets being tracked.
     */
    readonly widgets: ReadonlyArray<T>;
    /**
     * Get the focus number for a particular widget in the tracker.
     *
     * @param widget - The widget of interest.
     *
     * @returns The focus number for the given widget, or `-1` if the
     *   widget has not had focus since being added to the tracker, or
     *   is not contained by the tracker.
     *
     * #### Notes
     * The focus number indicates the relative order in which the widgets
     * have gained focus. A widget with a larger number has gained focus
     * more recently than a widget with a smaller number.
     *
     * The `currentWidget` will always have the largest focus number.
     *
     * All widgets start with a focus number of `-1`, which indicates that
     * the widget has not been focused since being added to the tracker.
     */
    focusNumber(widget: T): number;
    /**
     * Test whether the focus tracker contains a given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns `true` if the widget is tracked, `false` otherwise.
     */
    has(widget: T): boolean;
    /**
     * Add a widget to the focus tracker.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * A widget will be automatically removed from the tracker if it
     * is disposed after being added.
     *
     * If the widget is already tracked, this is a no-op.
     */
    add(widget: T): void;
    /**
     * Remove a widget from the focus tracker.
     *
     * #### Notes
     * If the widget is the `currentWidget`, the previous current widget
     * will become the new `currentWidget`.
     *
     * A widget will be automatically removed from the tracker if it
     * is disposed after being added.
     *
     * If the widget is not tracked, this is a no-op.
     */
    remove(widget: T): void;
    /**
     * Handle the DOM events for the focus tracker.
     *
     * @param event - The DOM event sent to the panel.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the tracked nodes. It should
     * not be called directly by user code.
     */
    handleEvent(event: Event): void;
    /**
     * Set the current and active widgets for the tracker.
     */
    private _setWidgets(current, active);
    /**
     * Handle the `'focus'` event for a tracked widget.
     */
    private _evtFocus(event);
    /**
     * Handle the `'blur'` event for a tracked widget.
     */
    private _evtBlur(event);
    /**
     * Handle the `disposed` signal for a tracked widget.
     */
    private _onWidgetDisposed(sender);
    private _counter;
    private _widgets;
    private _activeWidget;
    private _currentWidget;
    private _numbers;
    private _nodes;
    private _activeChanged;
    private _currentChanged;
}
/**
 * The namespace for the `FocusTracker` class statics.
 */
export declare namespace FocusTracker {
    /**
     * An arguments object for the changed signals.
     */
    interface IChangedArgs<T extends Widget> {
        /**
         * The old value for the widget.
         */
        oldValue: T | null;
        /**
         * The new value for the widget.
         */
        newValue: T | null;
    }
}
