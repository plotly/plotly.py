/**
 * The namespace for element related utilities.
 */
export declare namespace ElementExt {
    /**
     * An object which holds the border and padding data for an element.
     */
    interface IBoxSizing {
        /**
         * The top border width, in pixels.
         */
        borderTop: number;
        /**
         * The left border width, in pixels.
         */
        borderLeft: number;
        /**
         * The right border width, in pixels.
         */
        borderRight: number;
        /**
         * The bottom border width, in pixels.
         */
        borderBottom: number;
        /**
         * The top padding width, in pixels.
         */
        paddingTop: number;
        /**
         * The left padding width, in pixels.
         */
        paddingLeft: number;
        /**
         * The right padding width, in pixels.
         */
        paddingRight: number;
        /**
         * The bottom padding width, in pixels.
         */
        paddingBottom: number;
        /**
         * The sum of horizontal border and padding.
         */
        horizontalSum: number;
        /**
         * The sum of vertical border and padding.
         */
        verticalSum: number;
    }
    /**
     * Compute the box sizing for an element.
     *
     * @param element - The element of interest.
     *
     * @returns The box sizing data for the specified element.
     */
    function boxSizing(element: Element): IBoxSizing;
    /**
     * An object which holds the min and max size data for an element.
     */
    interface ISizeLimits {
        /**
         * The minimum width, in pixels.
         */
        minWidth: number;
        /**
         * The minimum height, in pixels.
         */
        minHeight: number;
        /**
         * The maximum width, in pixels.
         */
        maxWidth: number;
        /**
         * The maximum height, in pixels.
         */
        maxHeight: number;
    }
    /**
     * Compute the size limits for an element.
     *
     * @param element - The element of interest.
     *
     * @returns The size limit data for the specified element.
     */
    function sizeLimits(element: Element): ISizeLimits;
    /**
     * Test whether a client position lies within an element.
     *
     * @param element - The DOM element of interest.
     *
     * @param clientX - The client X coordinate of interest.
     *
     * @param clientY - The client Y coordinate of interest.
     *
     * @returns Whether the point is within the given element.
     */
    function hitTest(element: Element, clientX: number, clientY: number): boolean;
    /**
     * Vertically scroll an element into view if needed.
     *
     * @param area - The scroll area element.
     *
     * @param element - The element of interest.
     *
     * #### Notes
     * This follows the "nearest" behavior of the native `scrollIntoView`
     * method, which is not supported by all browsers.
     * https://drafts.csswg.org/cssom-view/#element-scrolling-members
     *
     * If the element fully covers the visible area or is fully contained
     * within the visible area, no scrolling will take place. Otherwise,
     * the nearest edges of the area and element are aligned.
     */
    function scrollIntoViewIfNeeded(area: Element, element: Element): void;
}
