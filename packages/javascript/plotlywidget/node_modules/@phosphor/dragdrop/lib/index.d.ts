import { MimeData } from '@phosphor/coreutils';
import { IDisposable } from '@phosphor/disposable';
/**
 * A type alias which defines the possible independent drop actions.
 */
export declare type DropAction = 'none' | 'copy' | 'link' | 'move';
/**
 * A type alias which defines the possible supported drop actions.
 */
export declare type SupportedActions = DropAction | 'copy-link' | 'copy-move' | 'link-move' | 'all';
/**
 * A custom event type used for drag-drop operations.
 *
 * #### Notes
 * In order to receive `'p-dragover'`, `'p-dragleave'`, or `'p-drop'`
 * events, a drop target must cancel the `'p-dragenter'` event by
 * calling the event's `preventDefault()` method.
 */
export interface IDragEvent extends MouseEvent {
    /**
     * The drop action supported or taken by the drop target.
     *
     * #### Notes
     * At the start of each event, this value will be `'none'`. During a
     * `'p-dragover'` event, the drop target must set this value to one
     * of the supported actions, or the drop event will not occur.
     *
     * When handling the drop event, the drop target should set this
     * to the action which was *actually* taken. This value will be
     * reported back to the drag initiator.
     */
    dropAction: DropAction;
    /**
     * The drop action proposed by the drag initiator.
     *
     * #### Notes
     * This is the action which is *preferred* by the drag initiator. The
     * drop target is not required to perform this action, but should if
     * it all possible.
     */
    readonly proposedAction: DropAction;
    /**
     * The drop actions supported by the drag initiator.
     *
     * #### Notes
     * If the `dropAction` is not set to one of the supported actions
     * during the `'p-dragover'` event, the drop event will not occur.
     */
    readonly supportedActions: SupportedActions;
    /**
     * The mime data associated with the event.
     *
     * #### Notes
     * This is mime data provided by the drag initiator. Drop targets
     * should use this data to determine if they can handle the drop.
     */
    readonly mimeData: MimeData;
    /**
     * The source object of the drag, as provided by the drag initiator.
     *
     * #### Notes
     * For advanced applications, the drag initiator may wish to expose
     * a source object to the drop targets. That will be provided here
     * if given by the drag initiator, otherwise it will be `null`.
     */
    readonly source: any;
}
/**
 * An object which manages a drag-drop operation.
 *
 * A drag object dispatches four different events to drop targets:
 *
 * - `'p-dragenter'` - Dispatched when the mouse enters the target
 *   element. This event must be canceled in order to receive any
 *   of the other events.
 *
 * - `'p-dragover'` - Dispatched when the mouse moves over the drop
 *   target. It must cancel the event and set the `dropAction` to one
 *   of the supported actions in order to receive drop events.
 *
 * - `'p-dragleave'` - Dispatched when the mouse leaves the target
 *   element. This includes moving the mouse into child elements.
 *
 * - `'p-drop'`- Dispatched when the mouse is released over the target
 *   element when the target indicates an appropriate drop action. If
 *   the event is canceled, the indicated drop action is returned to
 *   the initiator through the resolved promise.
 *
 * A drag operation can be terminated at any time by pressing `Escape`
 * or by disposing the drag object.
 *
 * A drag object has the ability to automatically scroll a scrollable
 * element when the mouse is hovered near one of its edges. To enable
 * this, add the `data-p-dragscroll` attribute to any element which
 * the drag object should consider for scrolling.
 *
 * #### Notes
 * This class is designed to be used when dragging and dropping custom
 * data *within* a single application. It is *not* a replacement for
 * the native drag-drop API. Instead, it provides an API which allows
 * drag operations to be initiated programmatically and enables the
 * transfer of arbitrary non-string objects; features which are not
 * possible with the native drag-drop API.
 */
export declare class Drag implements IDisposable {
    /**
     * Construct a new drag object.
     *
     * @param options - The options for initializing the drag.
     */
    constructor(options: Drag.IOptions);
    /**
     * Dispose of the resources held by the drag object.
     *
     * #### Notes
     * This will cancel the drag operation if it is active.
     */
    dispose(): void;
    /**
     * The mime data for the drag object.
     */
    readonly mimeData: MimeData;
    /**
     * The drag image element for the drag object.
     */
    readonly dragImage: HTMLElement | null;
    /**
     * The proposed drop action for the drag object.
     */
    readonly proposedAction: DropAction;
    /**
     * The supported drop actions for the drag object.
     */
    readonly supportedActions: SupportedActions;
    /**
     * Get the drag source for the drag object.
     */
    readonly source: any;
    /**
     * Test whether the drag object is disposed.
     */
    readonly isDisposed: boolean;
    /**
     * Start the drag operation at the specified client position.
     *
     * @param clientX - The client X position for the drag start.
     *
     * @param clientY - The client Y position for the drag start.
     *
     * @returns A promise which resolves to the result of the drag.
     *
     * #### Notes
     * If the drag has already been started, the promise created by the
     * first call to `start` is returned.
     *
     * If the drag operation has ended, or if the drag object has been
     * disposed, the returned promise will resolve to `'none'`.
     *
     * The drag object will be automatically disposed when drag operation
     * completes. This means `Drag` objects are for single-use only.
     *
     * This method assumes the left mouse button is already held down.
     */
    start(clientX: number, clientY: number): Promise<DropAction>;
    /**
     * Handle the DOM events for the drag operation.
     *
     * @param event - The DOM event sent to the drag object.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the document. It should not be
     * called directly by user code.
     */
    handleEvent(event: Event): void;
    /**
     * Handle the `'mousemove'` event for the drag object.
     */
    private _evtMouseMove(event);
    /**
     * Handle the `'mouseup'` event for the drag object.
     */
    private _evtMouseUp(event);
    /**
     * Handle the `'keydown'` event for the drag object.
     */
    private _evtKeyDown(event);
    /**
     * Add the document event listeners for the drag object.
     */
    private _addListeners();
    /**
     * Remove the document event listeners for the drag object.
     */
    private _removeListeners();
    /**
     * Update the drag scroll element under the mouse.
     */
    private _updateDragScroll(event);
    /**
     * Update the current target node using the given mouse event.
     */
    private _updateCurrentTarget(event);
    /**
     * Attach the drag image element at the specified location.
     *
     * This is a no-op if there is no drag image element.
     */
    private _attachDragImage(clientX, clientY);
    /**
     * Move the drag image element to the specified location.
     *
     * This is a no-op if there is no drag image element.
     */
    private _moveDragImage(clientX, clientY);
    /**
     * Detach the drag image element from the DOM.
     *
     * This is a no-op if there is no drag image element.
     */
    private _detachDragImage();
    /**
     * Set the internal drop action state and update the drag cursor.
     */
    private _setDropAction(action);
    /**
     * Finalize the drag operation and resolve the drag promise.
     */
    private _finalize(action);
    /**
     * The scroll loop handler function.
     */
    private _onScrollFrame;
    private _disposed;
    private _dropAction;
    private _override;
    private _currentTarget;
    private _currentElement;
    private _promise;
    private _scrollTarget;
    private _resolve;
}
/**
 * The namespace for the `Drag` class statics.
 */
export declare namespace Drag {
    /**
     * An options object for initializing a `Drag` object.
     */
    interface IOptions {
        /**
         * The populated mime data for the drag operation.
         */
        mimeData: MimeData;
        /**
         * An optional drag image which follows the mouse cursor.
         *
         * #### Notes
         * The drag image can be any DOM element. It is not limited to
         * image or canvas elements as with the native drag-drop APIs.
         *
         * If provided, this will be positioned at the mouse cursor on each
         * mouse move event. A CSS transform can be used to offset the node
         * from its specified position.
         *
         * The drag image will automatically have the `p-mod-drag-image`
         * class name added.
         *
         * The default value is `null`.
         */
        dragImage?: HTMLElement;
        /**
         * The optional proposed drop action for the drag operation.
         *
         * #### Notes
         * This can be provided as a hint to the drop targets as to which
         * drop action is preferred.
         *
         * The default value is `'copy'`.
         */
        proposedAction?: DropAction;
        /**
         * The drop actions supported by the drag initiator.
         *
         * #### Notes
         * A drop target must indicate that it intends to perform one of the
         * supported actions in order to receive a drop event. However, it is
         * not required to *actually* perform that action when handling the
         * drop event. Therefore, the initiator must be prepared to handle
         * any drop action performed by a drop target.
         *
         * The default value is `'all'`.
         */
        supportedActions?: SupportedActions;
        /**
         * An optional object which indicates the source of the drag.
         *
         * #### Notes
         * For advanced applications, the drag initiator may wish to expose
         * a source object to the drop targets. That object can be specified
         * here and will be carried along with the drag events.
         *
         * The default value is `null`.
         */
        source?: any;
    }
    /**
     * Override the cursor icon for the entire document.
     *
     * @param cursor - The string representing the cursor style.
     *
     * @returns A disposable which will clear the override when disposed.
     *
     * #### Notes
     * The most recent call to `overrideCursor` takes precedence.
     * Disposing an old override has no effect on the current override.
     *
     * This utility function is used by the `Drag` class to override the
     * mouse cursor during a drag-drop operation, but it can also be used
     * by other classes to fix the cursor icon during normal mouse drags.
     *
     * #### Example
     * ```typescript
     * import { Drag } from '@phosphor/dragdrop';
     *
     * // Force the cursor to be 'wait' for the entire document.
     * let override = Drag.overrideCursor('wait');
     *
     * // Clear the override by disposing the return value.
     * override.dispose();
     * ```
     */
    function overrideCursor(cursor: string): IDisposable;
}
