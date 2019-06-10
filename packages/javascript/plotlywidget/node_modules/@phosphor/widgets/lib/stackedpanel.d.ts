import { ISignal } from '@phosphor/signaling';
import { Panel } from './panel';
import { StackedLayout } from './stackedlayout';
import { Widget } from './widget';
/**
 * A panel where visible widgets are stacked atop one another.
 *
 * #### Notes
 * This class provides a convenience wrapper around a [[StackedLayout]].
 */
export declare class StackedPanel extends Panel {
    /**
     * Construct a new stacked panel.
     *
     * @param options - The options for initializing the panel.
     */
    constructor(options?: StackedPanel.IOptions);
    /**
     * A signal emitted when a widget is removed from a stacked panel.
     */
    readonly widgetRemoved: ISignal<this, Widget>;
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    protected onChildAdded(msg: Widget.ChildMessage): void;
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    protected onChildRemoved(msg: Widget.ChildMessage): void;
    private _widgetRemoved;
}
/**
 * The namespace for the `StackedPanel` class statics.
 */
export declare namespace StackedPanel {
    /**
     * An options object for creating a stacked panel.
     */
    interface IOptions {
        /**
         * The stacked layout to use for the stacked panel.
         *
         * The default is a new `StackedLayout`.
         */
        layout?: StackedLayout;
    }
}
