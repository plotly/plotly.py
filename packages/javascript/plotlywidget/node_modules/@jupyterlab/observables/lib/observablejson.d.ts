import { JSONObject, JSONValue } from '@phosphor/coreutils';
import { Message } from '@phosphor/messaging';
import { IObservableMap, ObservableMap } from './observablemap';
/**
 * An observable JSON value.
 */
export interface IObservableJSON extends IObservableMap<JSONValue> {
    /**
     * Serialize the model to JSON.
     */
    toJSON(): JSONObject;
}
/**
 * The namespace for IObservableJSON related interfaces.
 */
export declare namespace IObservableJSON {
    /**
     * A type alias for observable JSON changed args.
     */
    type IChangedArgs = IObservableMap.IChangedArgs<JSONValue>;
}
/**
 * A concrete Observable map for JSON data.
 */
export declare class ObservableJSON extends ObservableMap<JSONValue> {
    /**
     * Construct a new observable JSON object.
     */
    constructor(options?: ObservableJSON.IOptions);
    /**
     * Serialize the model to JSON.
     */
    toJSON(): JSONObject;
}
/**
 * The namespace for ObservableJSON static data.
 */
export declare namespace ObservableJSON {
    /**
     * The options use to initialize an observable JSON object.
     */
    interface IOptions {
        /**
         * The optional intitial value for the object.
         */
        values?: JSONObject;
    }
    /**
     * An observable JSON change message.
     */
    class ChangeMessage extends Message {
        /**
         * Create a new metadata changed message.
         */
        constructor(args: IObservableJSON.IChangedArgs);
        /**
         * The arguments of the change.
         */
        readonly args: IObservableJSON.IChangedArgs;
    }
}
