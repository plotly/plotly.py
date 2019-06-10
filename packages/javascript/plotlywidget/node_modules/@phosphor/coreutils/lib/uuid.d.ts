/**
 * The namespace for UUID related functionality.
 */
export declare namespace UUID {
    /**
     * A function which generates UUID v4 identifiers.
     *
     * @returns A new UUID v4 string.
     *
     * #### Notes
     * This implementation complies with RFC 4122.
     *
     * This uses `Random.getRandomValues()` for random bytes, which in
     * turn will use the underlying `crypto` module of the platform if
     * it is available. The fallback for randomness is `Math.random`.
     */
    const uuid4: () => string;
}
