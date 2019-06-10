/**
 * The namespace for date functions.
 */
export declare namespace Time {
    /**
     * Convert a timestring to a human readable string (e.g. 'two minutes ago').
     *
     * @param value - The date timestring or date object.
     *
     * @returns A formatted date.
     */
    function formatHuman(value: string | Date): string;
    /**
     * Convert a timestring to a date format.
     *
     * @param value - The date timestring or date object.
     *
     * @param format - The format string.
     *
     * @returns A formatted date.
     */
    function format(value: string | Date, format?: string): string;
}
