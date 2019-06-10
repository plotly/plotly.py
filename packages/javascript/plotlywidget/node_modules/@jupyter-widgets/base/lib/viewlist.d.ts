/**
 * - create_view and remove_view are default functions called when adding or removing views
 * - create_view takes a model and an index and returns a view or a promise for a view for that model
 * - remove_view takes a view and destroys it (including calling `view.remove()`)
 * - each time the update() function is called with a new list, the create and remove
 *   callbacks will be called in an order so that if you append the views created in the
 *   create callback and remove the views in the remove callback, you will duplicate
 *   the order of the list.
 * - the remove callback defaults to just removing the view (e.g., pass in null for the second parameter)
 * - the context defaults to the created ViewList.  If you pass another context, the create and remove
 *   will be called in that context.
 */
export declare class ViewList<T> {
    constructor(create_view: (model: any, index: any) => T | Promise<T>, remove_view: (view: T) => void, context: any);
    initialize(create_view: (model: any, index: any) => T | Promise<T>, remove_view: (view: T) => void, context: any): void;
    /**
     * the create_view, remove_view, and context arguments override the defaults
     * specified when the list is created.
     * after this function, the .views attribute is a list of promises for views
     * if you want to perform some action on the list of views, do something like
     * `Promise.all(myviewlist.views).then(function(views) {...});`
     */
    update(new_models: any, create_view?: (model: any, index: any) => T | Promise<T>, remove_view?: (view: T) => void, context?: any): Promise<T[]>;
    /**
     * removes every view in the list; convenience function for `.update([])`
     * that should be faster
     * returns a promise that resolves after this removal is done
     */
    remove(): Promise<void>;
    /**
     * Dispose this viewlist.
     *
     * A synchronous function which just deletes references to child views. This
     * function does not call .remove() on child views because that is
     * asynchronous. Use this in cases where child views will be removed in
     * another way.
     */
    dispose(): void;
    _handler_context: any;
    _models: any[];
    views: Promise<T>[];
    _create_view: (model: any, index: any) => T | Promise<T>;
    _remove_view: (view: T) => void;
}
