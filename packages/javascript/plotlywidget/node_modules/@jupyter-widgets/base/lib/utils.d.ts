/**
 * Find all strings in the first argument that are not in the second.
 */
export declare function difference(a: string[], b: string[]): string[];
/**
 * Compare two objects deeply to see if they are equal.
 */
export declare function isEqual(a: any, b: any): boolean;
/**
 * A polyfill for Object.assign
 *
 * This is from code that Typescript 2.4 generates for a polyfill.
 */
export declare let assign: any;
/**
 * Generate a UUID
 *
 * http://www.ietf.org/rfc/rfc4122.txt
 */
export declare function uuid(): string;
/**
 * Wrappable Error class
 *
 * The Error class doesn't actually act on `this`.  Instead it always
 * returns a new instance of Error.  Here we capture that instance so we
 * can apply it's properties to `this`.
 */
export declare class WrappedError extends Error {
    constructor(message: any, error: any);
    error_stack: any[];
}
/**
 * Resolve a promiseful dictionary.
 * Returns a single Promise.
 */
export declare function resolvePromisesDict(d: any): Promise<any>;
/**
 * Creates a wrappable Promise rejection function.
 *
 * Creates a function that logs an error message before rethrowing
 * the original error that caused the promise to reject.
 */
export declare function reject(message: any, log: any): (error: any) => never;
/**
 * Takes an object 'state' and fills in buffer[i] at 'path' buffer_paths[i]
 * where buffer_paths[i] is a list indicating where in the object buffer[i] should
 * be placed
 * Example: state = {a: 1, b: {}, c: [0, null]}
 * buffers = [array1, array2]
 * buffer_paths = [['b', 'data'], ['c', 1]]
 * Will lead to {a: 1, b: {data: array1}, c: [0, array2]}
 */
export declare function put_buffers(state: any, buffer_paths: (string | number)[][], buffers: DataView[]): void;
/**
 * The inverse of put_buffers, return an objects with the new state where all buffers(ArrayBuffer)
 * are removed. If a buffer is a member of an object, that object is cloned, and the key removed. If a buffer
 * is an element of an array, that array is cloned, and the element is set to null.
 * See put_buffers for the meaning of buffer_paths
 * Returns an object with the new state (.state) an array with paths to the buffers (.buffer_paths),
 * and the buffers associated to those paths (.buffers).
 */
export declare function remove_buffers(state: any): {
    state: any;
    buffers: ArrayBuffer[];
    buffer_paths: (string | number)[][];
};
/**
 * Convert an ArrayBuffer to a hex string.
 */
export declare function bufferToHex(buffer: ArrayBuffer): string;
/**
 * Convert a hex string to an ArrayBuffer.
 */
export declare function hexToBuffer(hex: string): ArrayBuffer;
/**
 * Convert an ArrayBuffer to a base64 string.
 */
export declare function bufferToBase64(buffer: ArrayBuffer): string;
/**
 * Convert a base64 string to an ArrayBuffer.
 */
export declare function base64ToBuffer(base64: string): ArrayBuffer;
