/**
 * A type alias for a JSON primitive.
 */
export declare type JSONPrimitive = boolean | number | string | null;
/**
 * A type alias for a JSON value.
 */
export declare type JSONValue = JSONPrimitive | JSONObject | JSONArray;
/**
 * A type definition for a JSON object.
 */
export interface JSONObject {
    [key: string]: JSONValue;
}
/**
 * A type definition for a JSON array.
 */
export interface JSONArray extends Array<JSONValue> {
}
/**
 * A type definition for a readonly JSON object.
 */
export interface ReadonlyJSONObject {
    readonly [key: string]: ReadonlyJSONValue;
}
/**
 * A type definition for a readonly JSON array.
 */
export interface ReadonlyJSONArray extends ReadonlyArray<ReadonlyJSONValue> {
}
/**
 * A type alias for a readonly JSON value.
 */
export declare type ReadonlyJSONValue = JSONPrimitive | ReadonlyJSONObject | ReadonlyJSONArray;
/**
 * The namespace for JSON-specific functions.
 */
export declare namespace JSONExt {
    /**
     * A shared frozen empty JSONObject
     */
    const emptyObject: ReadonlyJSONObject;
    /**
     * A shared frozen empty JSONArray
     */
    const emptyArray: ReadonlyJSONArray;
    /**
     * Test whether a JSON value is a primitive.
     *
     * @param value - The JSON value of interest.
     *
     * @returns `true` if the value is a primitive,`false` otherwise.
     */
    function isPrimitive(value: ReadonlyJSONValue): value is JSONPrimitive;
    /**
     * Test whether a JSON value is an array.
     *
     * @param value - The JSON value of interest.
     *
     * @returns `true` if the value is a an array, `false` otherwise.
     */
    function isArray(value: JSONValue): value is JSONArray;
    function isArray(value: ReadonlyJSONValue): value is ReadonlyJSONArray;
    /**
     * Test whether a JSON value is an object.
     *
     * @param value - The JSON value of interest.
     *
     * @returns `true` if the value is a an object, `false` otherwise.
     */
    function isObject(value: JSONValue): value is JSONObject;
    function isObject(value: ReadonlyJSONValue): value is ReadonlyJSONObject;
    /**
     * Compare two JSON values for deep equality.
     *
     * @param first - The first JSON value of interest.
     *
     * @param second - The second JSON value of interest.
     *
     * @returns `true` if the values are equivalent, `false` otherwise.
     */
    function deepEqual(first: ReadonlyJSONValue, second: ReadonlyJSONValue): boolean;
    /**
     * Create a deep copy of a JSON value.
     *
     * @param value - The JSON value to copy.
     *
     * @returns A deep copy of the given JSON value.
     */
    function deepCopy<T extends ReadonlyJSONValue>(value: T): T;
}
