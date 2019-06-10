import * as Backbone from 'backbone';
export declare class NativeView<T extends Backbone.Model> extends Backbone.View<T> {
    _removeElement(): void;
    _setElement(element: HTMLElement): void;
    _setAttributes(attrs: any): void;
    /**
     * Make an event delegation handler for the given `eventName` and `selector`
     * and attach it to `this.el`.
     * If selector is empty, the listener will be bound to `this.el`. If not, a
     * new handler that will recursively traverse up the event target's DOM
     * hierarchy looking for a node that matches the selector. If one is found,
     * the event's `delegateTarget` property is set to it and the return the
     * result of calling bound `listener` with the parameters given to the
     * handler.
     *
     * This does not properly handle selectors for things like focus and blur (see
     * https://github.com/jquery/jquery/blob/7d21f02b9ec9f655583e898350badf89165ed4d5/src/event.js#L442
     * for some similar exceptional cases).
     */
    delegate(eventName: any, selector: any, listener: any): any;
    undelegate(eventName: any, selector: any, listener: any): this;
    undelegateEvents(): this;
    private _domEvents;
}
