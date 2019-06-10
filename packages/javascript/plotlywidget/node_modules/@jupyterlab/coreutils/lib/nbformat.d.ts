import { JSONObject } from '@phosphor/coreutils';
/**
 * A namespace for nbformat interfaces.
 */
export declare namespace nbformat {
    /**
     * The major version of the notebook format.
     */
    const MAJOR_VERSION: number;
    /**
     * The minor version of the notebook format.
     */
    const MINOR_VERSION: number;
    /**
     * The kernelspec metadata.
     */
    interface IKernelspecMetadata extends JSONObject {
        name: string;
        display_name: string;
    }
    /**
     * The language info metatda
     */
    interface ILanguageInfoMetadata extends JSONObject {
        name: string;
        codemirror_mode?: string | JSONObject;
        file_extension?: string;
        mimetype?: string;
        pygments_lexer?: string;
    }
    /**
     * The default metadata for the notebook.
     */
    interface INotebookMetadata extends JSONObject {
        kernelspec?: IKernelspecMetadata;
        language_info?: ILanguageInfoMetadata;
        orig_nbformat: number;
    }
    /**
     * The notebook content.
     */
    interface INotebookContent extends JSONObject {
        metadata: INotebookMetadata;
        nbformat_minor: number;
        nbformat: number;
        cells: ICell[];
    }
    /**
     * A multiline string.
     */
    type MultilineString = string | string[];
    /**
     * A mime-type keyed dictionary of data.
     */
    interface IMimeBundle extends JSONObject {
        [key: string]: MultilineString | JSONObject;
    }
    /**
     * Media attachments (e.g. inline images).
     */
    interface IAttachments {
        [key: string]: IMimeBundle;
    }
    /**
     * The code cell's prompt number. Will be null if the cell has not been run.
     */
    type ExecutionCount = number | null;
    /**
     * Cell output metadata.
     */
    type OutputMetadata = JSONObject;
    /**
     * Validate a mime type/value pair.
     *
     * @param type - The mimetype name.
     *
     * @param value - The value associated with the type.
     *
     * @returns Whether the type/value pair are valid.
     */
    function validateMimeValue(type: string, value: MultilineString | JSONObject): boolean;
    /**
     * A type which describes the type of cell.
     */
    type CellType = 'code' | 'markdown' | 'raw';
    /**
     * Cell-level metadata.
     */
    interface IBaseCellMetadata extends JSONObject {
        /**
         * Whether the cell is trusted.
         *
         * #### Notes
         * This is not strictly part of the nbformat spec, but it is added by
         * the contents manager.
         *
         * See https://jupyter-notebook.readthedocs.io/en/latest/security.html.
         */
        trusted: boolean;
        /**
         * The cell's name. If present, must be a non-empty string.
         */
        name: string;
        /**
         * The cell's tags. Tags must be unique, and must not contain commas.
         */
        tags: string[];
    }
    /**
     * The base cell interface.
     */
    interface IBaseCell extends JSONObject {
        /**
         * String identifying the type of cell.
         */
        cell_type: string;
        /**
         * Contents of the cell, represented as an array of lines.
         */
        source: MultilineString;
        /**
         * Cell-level metadata.
         */
        metadata: Partial<ICellMetadata>;
    }
    /**
     * Metadata for the raw cell.
     */
    interface IRawCellMetadata extends IBaseCellMetadata {
        /**
         * Raw cell metadata format for nbconvert.
         */
        format: string;
    }
    /**
     * A raw cell.
     */
    interface IRawCell extends IBaseCell {
        /**
         * String identifying the type of cell.
         */
        cell_type: 'raw';
        /**
         * Cell-level metadata.
         */
        metadata: Partial<IRawCellMetadata>;
        /**
         * Cell attachments.
         */
        attachments?: IAttachments;
    }
    /**
     * A markdown cell.
     */
    interface IMarkdownCell extends IBaseCell {
        /**
         * String identifying the type of cell.
         */
        cell_type: 'markdown';
        /**
         * Cell attachments.
         */
        attachments?: IAttachments;
    }
    /**
     * Metadata for a code cell.
     */
    interface ICodeCellMetadata extends IBaseCellMetadata {
        /**
         * Whether the cell is collapsed/expanded.
         */
        collapsed: boolean;
        /**
         * Whether the cell's output is scrolled, unscrolled, or autoscrolled.
         */
        scrolled: boolean | 'auto';
    }
    /**
     * A code cell.
     */
    interface ICodeCell extends IBaseCell {
        /**
         * String identifying the type of cell.
         */
        cell_type: 'code';
        /**
         * Cell-level metadata.
         */
        metadata: Partial<ICodeCellMetadata>;
        /**
         * Execution, display, or stream outputs.
         */
        outputs: IOutput[];
        /**
         * The code cell's prompt number. Will be null if the cell has not been run.
         */
        execution_count: ExecutionCount;
    }
    /**
     * An unrecognized cell.
     */
    interface IUnrecognizedCell extends IBaseCell {
    }
    /**
     * A cell union type.
     */
    type ICell = IRawCell | IMarkdownCell | ICodeCell | IUnrecognizedCell;
    /**
     * Test whether a cell is a raw cell.
     */
    function isRaw(cell: ICell): cell is IRawCell;
    /**
     * Test whether a cell is a markdown cell.
     */
    function isMarkdown(cell: ICell): cell is IMarkdownCell;
    /**
     * Test whether a cell is a code cell.
     */
    function isCode(cell: ICell): cell is ICodeCell;
    /**
     * A union metadata type.
     */
    type ICellMetadata = IBaseCellMetadata | IRawCellMetadata | ICodeCellMetadata;
    /**
     * The valid output types.
     */
    type OutputType = 'execute_result' | 'display_data' | 'stream' | 'error' | 'update_display_data';
    /**
     * The base output type.
     */
    interface IBaseOutput extends JSONObject {
        /**
         * Type of cell output.
         */
        output_type: string;
    }
    /**
     * Result of executing a code cell.
     */
    interface IExecuteResult extends IBaseOutput {
        /**
         * Type of cell output.
         */
        output_type: 'execute_result';
        /**
         * A result's prompt number.
         */
        execution_count: ExecutionCount;
        /**
         * A mime-type keyed dictionary of data.
         */
        data: IMimeBundle;
        /**
         * Cell output metadata.
         */
        metadata: OutputMetadata;
    }
    /**
     * Data displayed as a result of code cell execution.
     */
    interface IDisplayData extends IBaseOutput {
        /**
         * Type of cell output.
         */
        output_type: 'display_data';
        /**
         * A mime-type keyed dictionary of data.
         */
        data: IMimeBundle;
        /**
         * Cell output metadata.
         */
        metadata: OutputMetadata;
    }
    /**
     * Data displayed as an update to existing display data.
     */
    interface IDisplayUpdate extends IBaseOutput {
        /**
         * Type of cell output.
         */
        output_type: 'update_display_data';
        /**
         * A mime-type keyed dictionary of data.
         */
        data: IMimeBundle;
        /**
         * Cell output metadata.
         */
        metadata: OutputMetadata;
    }
    /**
     * Stream output from a code cell.
     */
    interface IStream extends IBaseOutput {
        /**
         * Type of cell output.
         */
        output_type: 'stream';
        /**
         * The name of the stream.
         */
        name: StreamType;
        /**
         * The stream's text output.
         */
        text: MultilineString;
    }
    /**
     * An alias for a stream type.
     */
    type StreamType = 'stdout' | 'stderr';
    /**
     * Output of an error that occurred during code cell execution.
     */
    interface IError extends IBaseOutput {
        /**
         * Type of cell output.
         */
        output_type: 'error';
        /**
         * The name of the error.
         */
        ename: string;
        /**
         * The value, or message, of the error.
         */
        evalue: string;
        /**
         * The error's traceback.
         */
        traceback: string[];
    }
    /**
     * Unrecognized output.
     */
    interface IUnrecognizedOutput extends IBaseOutput {
    }
    /**
     * Test whether an output is an execute result.
     */
    function isExecuteResult(output: IOutput): output is IExecuteResult;
    /**
     * Test whether an output is from display data.
     */
    function isDisplayData(output: IOutput): output is IDisplayData;
    /**
     * Test whether an output is from updated display data.
     */
    function isDisplayUpdate(output: IOutput): output is IDisplayUpdate;
    /**
     * Test whether an output is from a stream.
     */
    function isStream(output: IOutput): output is IStream;
    /**
     * Test whether an output is from a stream.
     */
    function isError(output: IOutput): output is IError;
    /**
     * An output union type.
     */
    type IOutput = IUnrecognizedOutput | IExecuteResult | IDisplayData | IStream | IError;
}
