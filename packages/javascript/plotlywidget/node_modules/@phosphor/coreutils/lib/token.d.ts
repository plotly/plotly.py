/**
 * A runtime object which captures compile-time type information.
 *
 * #### Notes
 * A token captures the compile-time type of an interface or class in
 * an object which can be used at runtime in a type-safe fashion.
 */
export declare class Token<T> {
    /**
     * Construct a new token.
     *
     * @param name - A human readable name for the token.
     */
    constructor(name: string);
    /**
     * The human readable name for the token.
     *
     * #### Notes
     * This can be useful for debugging and logging.
     */
    readonly name: string;
    private _tokenStructuralPropertyT;
}
