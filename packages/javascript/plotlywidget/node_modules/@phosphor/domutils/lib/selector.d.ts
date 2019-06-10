/**
 * The namespace for selector related utilities.
 */
export declare namespace Selector {
    /**
     * Calculate the specificity of a single CSS selector.
     *
     * @param selector - The CSS selector of interest.
     *
     * @returns The specificity of the selector.
     *
     * #### Undefined Behavior
     * The selector is invalid.
     *
     * #### Notes
     * This is based on https://www.w3.org/TR/css3-selectors/#specificity
     *
     * A larger number represents a more specific selector.
     *
     * The smallest possible specificity is `0`.
     *
     * The result is represented as a hex number `0x<aa><bb><cc>` where
     * each component is the count of the respective selector clause.
     *
     * If the selector contains commas, only the first clause is used.
     *
     * The computed result is cached, so subsequent calculations for the
     * same selector are extremely fast.
     */
    function calculateSpecificity(selector: string): number;
    /**
     * Test whether a selector is a valid CSS selector.
     *
     * @param selector - The CSS selector of interest.
     *
     * @returns `true` if the selector is valid, `false` otherwise.
     *
     * #### Notes
     * The computed result is cached, so subsequent tests for the same
     * selector are extremely fast.
     */
    function isValid(selector: string): boolean;
    /**
     * Test whether an element matches a CSS selector.
     *
     * @param element - The element of interest.
     *
     * @param selector - The valid CSS selector of interest.
     *
     * @returns `true` if the element is a match, `false` otherwise.
     *
     * #### Notes
     * This function uses the builtin browser capabilities when possible,
     * falling back onto a document query otherwise.
     */
    function matches(element: Element, selector: string): boolean;
}
