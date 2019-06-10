/**
 * The namespace for string-specific algorithms.
 */
export declare namespace StringExt {
    /**
     * Find the indices of characters in a source text.
     *
     * @param source - The source text which should be searched.
     *
     * @param query - The characters to locate in the source text.
     *
     * @param start - The index to start the search.
     *
     * @returns The matched indices, or `null` if there is no match.
     *
     * #### Complexity
     * Linear on `sourceText`.
     *
     * #### Notes
     * In order for there to be a match, all of the characters in `query`
     * **must** appear in `source` in the order given by `query`.
     *
     * Characters are matched using strict `===` equality.
     */
    function findIndices(source: string, query: string, start?: number): number[] | null;
    /**
     * The result of a string match function.
     */
    interface IMatchResult {
        /**
         * A score which indicates the strength of the match.
         *
         * The documentation of a given match function should specify
         * whether a lower or higher score is a stronger match.
         */
        score: number;
        /**
         * The indices of the matched characters in the source text.
         *
         * The indices will appear in increasing order.
         */
        indices: number[];
    }
    /**
     * A string matcher which uses a sum-of-squares algorithm.
     *
     * @param source - The source text which should be searched.
     *
     * @param query - The characters to locate in the source text.
     *
     * @param start - The index to start the search.
     *
     * @returns The match result, or `null` if there is no match.
     *   A lower `score` represents a stronger match.
     *
     * #### Complexity
     * Linear on `sourceText`.
     *
     * #### Notes
     * This scoring algorithm uses a sum-of-squares approach to determine
     * the score. In order for there to be a match, all of the characters
     * in `query` **must** appear in `source` in order. The index of each
     * matching character is squared and added to the score. This means
     * that early and consecutive character matches are preferred, while
     * late matches are heavily penalized.
     */
    function matchSumOfSquares(source: string, query: string, start?: number): IMatchResult | null;
    /**
     * A string matcher which uses a sum-of-deltas algorithm.
     *
     * @param source - The source text which should be searched.
     *
     * @param query - The characters to locate in the source text.
     *
     * @param start - The index to start the search.
     *
     * @returns The match result, or `null` if there is no match.
     *   A lower `score` represents a stronger match.
     *
     * #### Complexity
     * Linear on `sourceText`.
     *
     * #### Notes
     * This scoring algorithm uses a sum-of-deltas approach to determine
     * the score. In order for there to be a match, all of the characters
     * in `query` **must** appear in `source` in order. The delta between
     * the indices are summed to create the score. This means that groups
     * of matched characters are preferred, while fragmented matches are
     * penalized.
     */
    function matchSumOfDeltas(source: string, query: string, start?: number): IMatchResult | null;
    /**
     * Highlight the matched characters of a source text.
     *
     * @param source - The text which should be highlighted.
     *
     * @param indices - The indices of the matched characters. They must
     *   appear in increasing order and must be in bounds of the source.
     *
     * @param fn - The function to apply to the matched chunks.
     *
     * @returns An array of unmatched and highlighted chunks.
     */
    function highlight<T>(source: string, indices: ReadonlyArray<number>, fn: (chunk: string) => T): Array<string | T>;
}
