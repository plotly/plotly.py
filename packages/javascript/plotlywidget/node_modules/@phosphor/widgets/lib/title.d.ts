import { ISignal } from '@phosphor/signaling';
/**
 * An object which holds data related to an object's title.
 *
 * #### Notes
 * A title object is intended to hold the data necessary to display a
 * header for a particular object. A common example is the `TabPanel`,
 * which uses the widget title to populate the tab for a child widget.
 */
export declare class Title<T> {
    /**
     * Construct a new title.
     *
     * @param options - The options for initializing the title.
     */
    constructor(options: Title.IOptions<T>);
    /**
     * A signal emitted when the state of the title changes.
     */
    readonly changed: ISignal<this, void>;
    /**
     * The object which owns the title.
     */
    readonly owner: T;
    /**
     * Get the label for the title.
     *
     * #### Notes
     * The default value is an empty string.
     */
    /**
     * Set the label for the title.
     */
    label: string;
    /**
     * Get the mnemonic index for the title.
     *
     * #### Notes
     * The default value is `-1`.
     */
    /**
     * Set the mnemonic index for the title.
     */
    mnemonic: number;
    /**
     * @deprecated Use `iconClass` instead.
     */
    /**
     * @deprecated Use `iconClass` instead.
     */
    icon: string;
    /**
     * Get the icon class name for the title.
     *
     * #### Notes
     * The default value is an empty string.
     */
    /**
     * Set the icon class name for the title.
     *
     * #### Notes
     * Multiple class names can be separated with whitespace.
     */
    iconClass: string;
    /**
     * Get the icon label for the title.
     *
     * #### Notes
     * The default value is an empty string.
     */
    /**
     * Set the icon label for the title.
     *
     * #### Notes
     * Multiple class names can be separated with whitespace.
     */
    iconLabel: string;
    /**
     * Get the caption for the title.
     *
     * #### Notes
     * The default value is an empty string.
     */
    /**
     * Set the caption for the title.
     */
    caption: string;
    /**
     * Get the extra class name for the title.
     *
     * #### Notes
     * The default value is an empty string.
     */
    /**
     * Set the extra class name for the title.
     *
     * #### Notes
     * Multiple class names can be separated with whitespace.
     */
    className: string;
    /**
     * Get the closable state for the title.
     *
     * #### Notes
     * The default value is `false`.
     */
    /**
     * Set the closable state for the title.
     *
     * #### Notes
     * This controls the presence of a close icon when applicable.
     */
    closable: boolean;
    /**
     * Get the dataset for the title.
     *
     * #### Notes
     * The default value is an empty dataset.
     */
    /**
     * Set the dataset for the title.
     *
     * #### Notes
     * This controls the data attributes when applicable.
     */
    dataset: Title.Dataset;
    private _label;
    private _caption;
    private _mnemonic;
    private _iconClass;
    private _iconLabel;
    private _className;
    private _closable;
    private _dataset;
    private _changed;
}
/**
 * The namespace for the `Title` class statics.
 */
export declare namespace Title {
    /**
     * A type alias for a simple immutable string dataset.
     */
    type Dataset = {
        readonly [key: string]: string;
    };
    /**
     * An options object for initializing a title.
     */
    interface IOptions<T> {
        /**
         * The object which owns the title.
         */
        owner: T;
        /**
         * The label for the title.
         */
        label?: string;
        /**
         * The mnemonic index for the title.
         */
        mnemonic?: number;
        /**
         * @deprecated Use `iconClass` instead.
         */
        icon?: string;
        /**
         * The icon class name for the title.
         */
        iconClass?: string;
        /**
         * The icon label for the title.
         */
        iconLabel?: string;
        /**
         * The caption for the title.
         */
        caption?: string;
        /**
         * The extra class name for the title.
         */
        className?: string;
        /**
         * The closable state for the title.
         */
        closable?: boolean;
        /**
         * The dataset for the title.
         */
        dataset?: Dataset;
    }
}
