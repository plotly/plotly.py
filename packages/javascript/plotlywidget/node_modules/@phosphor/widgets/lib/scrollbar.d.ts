import { Message } from '@phosphor/messaging';
import { ISignal } from '@phosphor/signaling';
import { Widget } from './widget';
/**
 * A widget which implements a canonical scroll bar.
 */
export declare class ScrollBar extends Widget {
    /**
     * Construct a new scroll bar.
     *
     * @param options - The options for initializing the scroll bar.
     */
    constructor(options?: ScrollBar.IOptions);
    /**
     * A signal emitted when the user moves the scroll thumb.
     *
     * #### Notes
     * The payload is the current value of the scroll bar.
     */
    readonly thumbMoved: ISignal<this, number>;
    /**
     * A signal emitted when the user clicks a step button.
     *
     * #### Notes
     * The payload is whether a decrease or increase is requested.
     */
    readonly stepRequested: ISignal<this, 'decrement' | 'increment'>;
    /**
     * A signal emitted when the user clicks the scroll track.
     *
     * #### Notes
     * The payload is whether a decrease or increase is requested.
     */
    readonly pageRequested: ISignal<this, 'decrement' | 'increment'>;
    /**
     * Get the orientation of the scroll bar.
     */
    /**
     * Set the orientation of the scroll bar.
     */
    orientation: ScrollBar.Orientation;
    /**
     * Get the current value of the scroll bar.
     */
    /**
     * Set the current value of the scroll bar.
     *
     * #### Notes
     * The value will be clamped to the range `[0, maximum]`.
     */
    value: number;
    /**
     * Get the page size of the scroll bar.
     *
     * #### Notes
     * The page size is the amount of visible content in the scrolled
     * region, expressed in data units. It determines the size of the
     * scroll bar thumb.
     */
    /**
     * Set the page size of the scroll bar.
     *
     * #### Notes
     * The page size will be clamped to the range `[0, Infinity]`.
     */
    page: number;
    /**
     * Get the maximum value of the scroll bar.
     */
    /**
     * Set the maximum value of the scroll bar.
     *
     * #### Notes
     * The max size will be clamped to the range `[0, Infinity]`.
     */
    maximum: number;
    /**
     * The scroll bar decrement button node.
     *
     * #### Notes
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly decrementNode: HTMLDivElement;
    /**
     * The scroll bar increment button node.
     *
     * #### Notes
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly incrementNode: HTMLDivElement;
    /**
     * The scroll bar track node.
     *
     * #### Notes
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly trackNode: HTMLDivElement;
    /**
     * The scroll bar thumb node.
     *
     * #### Notes
     * Modifying this node directly can lead to undefined behavior.
     */
    readonly thumbNode: HTMLDivElement;
    /**
     * Handle the DOM events for the scroll bar.
     *
     * @param event - The DOM event sent to the scroll bar.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the scroll bar's DOM node.
     *
     * This should not be called directly by user code.
     */
    handleEvent(event: Event): void;
    /**
     * A method invoked on a 'before-attach' message.
     */
    protected onBeforeAttach(msg: Message): void;
    /**
     * A method invoked on an 'after-detach' message.
     */
    protected onAfterDetach(msg: Message): void;
    /**
     * A method invoked on an 'update-request' message.
     */
    protected onUpdateRequest(msg: Message): void;
    /**
     * Handle the `'keydown'` event for the scroll bar.
     */
    private _evtKeyDown(event);
    /**
     * Handle the `'mousedown'` event for the scroll bar.
     */
    private _evtMouseDown(event);
    /**
     * Handle the `'mousemove'` event for the scroll bar.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseup'` event for the scroll bar.
     */
    private _evtMouseUp(event);
    /**
     * Release the mouse and restore the node states.
     */
    private _releaseMouse();
    /**
     * Move the thumb to the specified position.
     */
    private _moveThumb(value);
    /**
     * A timeout callback for repeating the mouse press.
     */
    private _onRepeat;
    private _value;
    private _page;
    private _maximum;
    private _repeatTimer;
    private _orientation;
    private _pressData;
    private _thumbMoved;
    private _stepRequested;
    private _pageRequested;
}
/**
 * The namespace for the `ScrollBar` class statics.
 */
export declare namespace ScrollBar {
    /**
     * A type alias for a scroll bar orientation.
     */
    type Orientation = 'horizontal' | 'vertical';
    /**
     * An options object for creating a scroll bar.
     */
    interface IOptions {
        /**
         * The orientation of the scroll bar.
         *
         * The default is `'vertical'`.
         */
        orientation?: Orientation;
        /**
         * The value for the scroll bar.
         *
         * The default is `0`.
         */
        value?: number;
        /**
         * The page size for the scroll bar.
         *
         * The default is `10`.
         */
        page?: number;
        /**
         * The maximum value for the scroll bar.
         *
         * The default is `100`.
         */
        maximum?: number;
    }
}
