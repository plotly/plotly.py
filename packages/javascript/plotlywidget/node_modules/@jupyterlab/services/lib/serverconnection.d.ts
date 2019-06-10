/**
 * The namespace for ServerConnection functions.
 *
 * #### Notes
 * This is only intended to manage communication with the Jupyter server.
 *
 * The default values can be used in a JupyterLab or Jupyter Notebook context.
 *
 * We use `token` authentication if available, falling back on an XSRF
 * cookie if one has been provided on the `document`.
 *
 * A content type of `'application/json'` is added when using authentication
 * and there is no body data to allow the server to prevent malicious forms.
 */
export declare namespace ServerConnection {
    /**
     * A Jupyter server settings object.
     * Note that all of the settings are optional when passed to
     * [[makeSettings]].  The default settings are given in [[defaultSettings]].
     */
    interface ISettings {
        /**
         * The base url of the server.
         */
        readonly baseUrl: string;
        /**
         * The page url of the JupyterLab application.
         */
        readonly pageUrl: string;
        /**
         * The base ws url of the server.
         */
        readonly wsUrl: string;
        /**
         * The default request init options.
         */
        readonly init: RequestInit;
        /**
         * The authentication token for requests.  Use an empty string to disable.
         */
        readonly token: string;
        /**
         * The `fetch` method to use.
         */
        readonly fetch: (input: RequestInfo, init?: RequestInit) => Promise<Response>;
        /**
         * The `Request` object constructor.
         */
        readonly Request: typeof Request;
        /**
         * The `Headers` object constructor.
         */
        readonly Headers: typeof Headers;
        /**
         * The `WebSocket` object constructor.
         */
        readonly WebSocket: typeof WebSocket;
    }
    /**
     * Create a settings object given a subset of options.
     *
     * @param options - An optional partial set of options.
     *
     * @returns The full settings object.
     */
    function makeSettings(options?: Partial<ISettings>): ISettings;
    /**
     * Make an request to the notebook server.
     *
     * @param url - The url for the request.
     *
     * @param init - The initialization options for the request.
     *
     * @param settings - The server settings to apply to the request.
     *
     * @returns a Promise that resolves with the response.
     *
     * @throws If the url of the request is not a notebook server url.
     *
     * #### Notes
     * The `url` must start with `settings.baseUrl`.  The `init` settings are
     * merged with `settings.init`, with `init` taking precedence.
     * The headers in the two objects are not merged.
     * If there is no body data, we set the content type to `application/json`
     * because it is required by the Notebook server.
     */
    function makeRequest(url: string, init: RequestInit, settings: ISettings): Promise<Response>;
    /**
     * A wrapped error for a fetch response.
     */
    class ResponseError extends Error {
        /**
         * Create a new response error.
         */
        constructor(response: Response, message?: string);
        /**
         * The response associated with the error.
         */
        response: Response;
    }
    /**
     * A wrapped error for a network error.
     */
    class NetworkError extends TypeError {
        /**
         * Create a new network error.
         */
        constructor(original: TypeError);
    }
    /**
     * The default settings.
     */
    const defaultSettings: ServerConnection.ISettings;
}
