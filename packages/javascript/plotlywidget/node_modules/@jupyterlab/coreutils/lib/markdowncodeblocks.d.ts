/**
 * The namespace for code block functions which help
 * in extract code from markdown text
 */
export declare namespace MarkdownCodeBlocks {
    const CODE_BLOCK_MARKER = "```";
    class MarkdownCodeBlock {
        startLine: number;
        endLine: number;
        code: string;
        constructor(startLine: number);
    }
    /**
     * Check whether the given file extension is a markdown extension
     * @param extension - A file extension
     *
     * @returns true/false depending on whether this is a supported markdown extension
     */
    function isMarkdown(extension: string): boolean;
    /**
     * Construct all code snippets from current text
     * (this could be potentially optimized if we can cache and detect differences)
     * @param text - A string to parse codeblocks from
     *
     * @returns An array of MarkdownCodeBlocks.
     */
    function findMarkdownCodeBlocks(text: string): MarkdownCodeBlock[];
}
