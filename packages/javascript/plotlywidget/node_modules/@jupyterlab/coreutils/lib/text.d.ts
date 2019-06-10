/**
 * The namespace for text-related functions.
 */
export declare namespace Text {
    /**
     * Convert a javascript string index into a unicode character offset
     *
     * @param jsIdx - The javascript string index (counting surrogate pairs)
     *
     * @param text - The text in which the offset is calculated
     *
     * @returns The unicode character offset
     */
    function jsIndexToCharIndex(jsIdx: number, text: string): number;
    /**
     * Convert a unicode character offset to a javascript string index.
     *
     * @param charIdx - The index in unicode characters
     *
     * @param text - The text in which the offset is calculated
     *
     * @returns The js-native index
     */
    function charIndexToJsIndex(charIdx: number, text: string): number;
}
