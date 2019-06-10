/**
 * An object which represents an abstract keyboard layout.
 */
export interface IKeyboardLayout {
    /**
     * The human readable name of the layout.
     *
     * This value is used primarily for display and debugging purposes.
     */
    readonly name: string;
    /**
     * Get an array of all key values supported by the layout.
     *
     * @returns A new array of the supported key values.
     *
     * #### Notes
     * This can be useful for authoring tools and debugging, when it's
     * necessary to know which keys are available for shortcut use.
     */
    keys(): string[];
    /**
     * Test whether the given key is a valid value for the layout.
     *
     * @param key - The user provided key to test for validity.
     *
     * @returns `true` if the key is valid, `false` otherwise.
     */
    isValidKey(key: string): boolean;
    /**
     * Get the key for a `'keydown'` event.
     *
     * @param event - The event object for a `'keydown'` event.
     *
     * @returns The associated key value, or an empty string if the event
     *   does not represent a valid primary key.
     */
    keyForKeydownEvent(event: KeyboardEvent): string;
}
/**
 * Get the global application keyboard layout instance.
 *
 * @returns The keyboard layout for use by the application.
 *
 * #### Notes
 * The default keyboard layout is US-English.
 */
export declare function getKeyboardLayout(): IKeyboardLayout;
/**
 * Set the global application keyboard layout instance.
 *
 * @param - The keyboard layout for use by the application.
 *
 * #### Notes
 * The keyboard layout should typically be set on application startup
 * to a layout which is appropriate for the user's system.
 */
export declare function setKeyboardLayout(layout: IKeyboardLayout): void;
/**
 * A concrete implementation of [[IKeyboardLayout]] based on keycodes.
 *
 * The `keyCode` property of a `'keydown'` event is a browser and OS
 * specific representation of the physical key (not character) which
 * was pressed on a keyboard. While not the most convenient API, it
 * is currently the only one which works reliably on all browsers.
 *
 * This class accepts a user-defined mapping of keycode to key, which
 * allows for reliable shortcuts tailored to the user's system.
 */
export declare class KeycodeLayout implements IKeyboardLayout {
    /**
     * Construct a new keycode layout.
     *
     * @param name - The human readable name for the layout.
     *
     * @param codes - A mapping of keycode to key value.
     */
    constructor(name: string, codes: KeycodeLayout.CodeMap);
    /**
     * The human readable name of the layout.
     */
    readonly name: string;
    /**
     * Get an array of the key values supported by the layout.
     *
     * @returns A new array of the supported key values.
     */
    keys(): string[];
    /**
     * Test whether the given key is a valid value for the layout.
     *
     * @param key - The user provided key to test for validity.
     *
     * @returns `true` if the key is valid, `false` otherwise.
     */
    isValidKey(key: string): boolean;
    /**
     * Get the key for a `'keydown'` event.
     *
     * @param event - The event object for a `'keydown'` event.
     *
     * @returns The associated key value, or an empty string if
     *   the event does not represent a valid primary key.
     */
    keyForKeydownEvent(event: KeyboardEvent): string;
    private _keys;
    private _codes;
}
/**
 * The namespace for the `KeycodeLayout` class statics.
 */
export declare namespace KeycodeLayout {
    /**
     * A type alias for a keycode map.
     */
    type CodeMap = {
        readonly [code: number]: string;
    };
    /**
     * A type alias for a key set.
     */
    type KeySet = {
        readonly [key: string]: boolean;
    };
    /**
     * Extract the set of keys from a code map.
     *
     * @param code - The code map of interest.
     *
     * @returns A set of the keys in the code map.
     */
    function extractKeys(codes: CodeMap): KeySet;
}
/**
 * A keycode-based keyboard layout for US English keyboards.
 *
 * This layout is valid for the following OS/Browser combinations.
 *
 * - Windows
 *   - Chrome
 *   - Firefox
 *   - IE
 *
 * - OSX
 *   - Chrome
 *   - Firefox
 *   - Safari
 *
 * - Linux
 *   - Chrome
 *   - Firefox
 *
 * Other combinations may also work, but are untested.
 */
export declare const EN_US: IKeyboardLayout;
