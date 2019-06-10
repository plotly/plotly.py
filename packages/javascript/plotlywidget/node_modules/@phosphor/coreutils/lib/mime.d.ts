/**
 * An object which stores MIME data for general application use.
 *
 * #### Notes
 * This class does not attempt to enforce "correctness" of MIME types
 * and their associated data. Since this class is designed to transfer
 * arbitrary data and objects within the same application, it assumes
 * that the user provides correct and accurate data.
 */
export declare class MimeData {
    /**
     * Get an array of the MIME types contained within the dataset.
     *
     * @returns A new array of the MIME types, in order of insertion.
     */
    types(): string[];
    /**
     * Test whether the dataset has an entry for the given type.
     *
     * @param mime - The MIME type of interest.
     *
     * @returns `true` if the dataset contains a value for the given
     *   MIME type, `false` otherwise.
     */
    hasData(mime: string): boolean;
    /**
     * Get the data value for the given MIME type.
     *
     * @param mime - The MIME type of interest.
     *
     * @returns The value for the given MIME type, or `undefined` if
     *   the dataset does not contain a value for the type.
     */
    getData(mime: string): any | undefined;
    /**
     * Set the data value for the given MIME type.
     *
     * @param mime - The MIME type of interest.
     *
     * @param data - The data value for the given MIME type.
     *
     * #### Notes
     * This will overwrite any previous entry for the MIME type.
     */
    setData(mime: string, data: any): void;
    /**
     * Remove the data entry for the given MIME type.
     *
     * @param mime - The MIME type of interest.
     *
     * #### Notes
     * This is a no-op if there is no entry for the given MIME type.
     */
    clearData(mime: string): void;
    /**
     * Remove all data entries from the dataset.
     */
    clear(): void;
    private _types;
    private _values;
}
