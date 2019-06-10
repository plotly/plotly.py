/**
 * The namespace for random number related functionality.
 */
export declare namespace Random {
    /**
     * A function which generates random bytes.
     *
     * @param buffer - The `Uint8Array` to fill with random bytes.
     *
     * #### Notes
     * A cryptographically strong random number generator will be used if
     * available. Otherwise, `Math.random` will be used as a fallback for
     * randomness.
     *
     * The following RNGs are supported, listed in order of precedence:
     *   - `window.crypto.getRandomValues`
     *   - `window.msCrypto.getRandomValues`
     *   - `require('crypto').randomFillSync
     *   - `require('crypto').randomBytes
     *   - `Math.random`
     */
    const getRandomValues: (buffer: Uint8Array) => void;
}
