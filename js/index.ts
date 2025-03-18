import { IRenderMime } from '@jupyterlab/rendermime-interfaces';
import { Widget } from '@lumino/widgets';
import Plotly from "plotly.js";

/**
* The default mime type for the extension.
*/
const MIME_TYPE = 'plotly/vnd';


/**
* The CSS class to add to the Plotly Widget.
*/
const CSS_CLASS = "jp-RenderedPlotly";

/**
* The CSS class for a Plotly icon.
*/
const CSS_ICON_CLASS = "jp-MaterialIcon jp-PlotlyIcon";

/**
* A widget for rendering mp4.
*/
export class PlotlyMimeRenderer extends Widget implements IRenderMime.IRenderer {
    private _data: any;
    private _config: any;
    private _plotly_layout: any;
    /**
    * Construct a new output widget.
    */
    constructor(options: any) {
        super();
        this.addClass(CSS_CLASS);
        this._data = options.data;
        this._config = options.config;
        this._plotly_layout = options.layout;
    }
    
    /**
    * Render plotly into this widget's node.
    */
    renderModel(model: IRenderMime.IMimeModel): Promise<void> {
        return new Promise<void>((resolve, reject) => {
            Plotly.react(this.node, this._data, this._plotly_layout, this._config)
        });
    }
}

/**
* A mime renderer factory for mp4 data.
*/
export const rendererFactory: IRenderMime.IRendererFactory = {
    safe: true,
    mimeTypes: [MIME_TYPE],
    createRenderer: options => new PlotlyMimeRenderer(options)
};

/**
* Extension definition.
*/
const extension: IRenderMime.IExtension = {
    id: "@jupyterlab/plotly-extension:factory",
    rendererFactory,
    rank: 0,
    dataType: "json",
    fileTypes: [
        {
            name: "plotly",
            mimeTypes: [MIME_TYPE],
            extensions: [".plotly", ".plotly.json"],
            iconClass: CSS_ICON_CLASS,
        },
    ],
    documentWidgetFactoryOptions: {
        name: "Plotly",
        primaryFileType: "plotly",
        fileTypes: ["plotly", "json"],
        defaultFor: ["plotly"],
    },
}

export default extension;