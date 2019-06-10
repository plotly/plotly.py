"use strict";
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * The namespace for string-specific algorithms.
 */
var StringExt;
(function (StringExt) {
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
    function findIndices(source, query, start) {
        if (start === void 0) { start = 0; }
        var indices = new Array(query.length);
        for (var i = 0, j = start, n = query.length; i < n; ++i, ++j) {
            j = source.indexOf(query[i], j);
            if (j === -1) {
                return null;
            }
            indices[i] = j;
        }
        return indices;
    }
    StringExt.findIndices = findIndices;
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
    function matchSumOfSquares(source, query, start) {
        if (start === void 0) { start = 0; }
        var indices = findIndices(source, query, start);
        if (!indices) {
            return null;
        }
        var score = 0;
        for (var i = 0, n = indices.length; i < n; ++i) {
            var j = indices[i] - start;
            score += j * j;
        }
        return { score: score, indices: indices };
    }
    StringExt.matchSumOfSquares = matchSumOfSquares;
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
    function matchSumOfDeltas(source, query, start) {
        if (start === void 0) { start = 0; }
        var indices = findIndices(source, query, start);
        if (!indices) {
            return null;
        }
        var score = 0;
        var last = start - 1;
        for (var i = 0, n = indices.length; i < n; ++i) {
            var j = indices[i];
            score += j - last - 1;
            last = j;
        }
        return { score: score, indices: indices };
    }
    StringExt.matchSumOfDeltas = matchSumOfDeltas;
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
    function highlight(source, indices, fn) {
        // Set up the result array.
        var result = [];
        // Set up the counter variables.
        var k = 0;
        var last = 0;
        var n = indices.length;
        // Iterator over each index.
        while (k < n) {
            // Set up the chunk indices.
            var i = indices[k];
            var j = indices[k];
            // Advance the right chunk index until it's non-contiguous.
            while (++k < n && indices[k] === j + 1) {
                j++;
            }
            // Extract the unmatched text.
            if (last < i) {
                result.push(source.slice(last, i));
            }
            // Extract and highlight the matched text.
            if (i < j + 1) {
                result.push(fn(source.slice(i, j + 1)));
            }
            // Update the last visited index.
            last = j + 1;
        }
        // Extract any remaining unmatched text.
        if (last < source.length) {
            result.push(source.slice(last));
        }
        // Return the highlighted result.
        return result;
    }
    StringExt.highlight = highlight;
})(StringExt = exports.StringExt || (exports.StringExt = {}));
