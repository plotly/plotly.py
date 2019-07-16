// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

import { Widget } from '@phosphor/widgets';

import { Message } from '@phosphor/messaging';

import { IRenderMime } from '@jupyterlab/rendermime-interfaces';

import Plotly from 'plotly.js/dist/plotly';

import '../style/index.css';

/**
 * The CSS class to add to the Plotly Widget.
 */
const CSS_CLASS = 'jp-RenderedPlotly';

/**
 * The CSS class for a Plotly icon.
 */
const CSS_ICON_CLASS = 'jp-MaterialIcon jp-PlotlyIcon';

/**
 * The MIME type for Plotly.
 * The version of this follows the major version of Plotly.
 */
export const MIME_TYPE = 'application/vnd.plotly.v1+json';

interface IPlotlySpec {
  data: Plotly.Data;
  layout: Plotly.Layout;
  frames?: Plotly.Frame[];
}

export class RenderedPlotly extends Widget implements IRenderMime.IRenderer {
  /**
   * Create a new widget for rendering Plotly.
   */
  constructor(options: IRenderMime.IRendererOptions) {
    super();
    this.addClass(CSS_CLASS);
    this._mimeType = options.mimeType;

    // Create image element
    this._img_el = <HTMLImageElement>(document.createElement("img"));
    this._img_el.className = 'plot-img';
    this.node.appendChild(this._img_el);

    // Install image hover callback
    this._img_el.addEventListener('mouseenter', event => {
      this.createGraph(this._model);
    })
  }

  /**
   * Render Plotly into this widget's node.
   */
  renderModel(model: IRenderMime.IMimeModel): Promise<void> {

    if (this.hasGraphElement()) {
      // We already have a graph, don't overwrite it
      return Promise.resolve();
    }

    // Save off reference to model so that we can regenerate the plot later
    this._model = model;

    // Check for PNG data in mime bundle
    const png_data = <string>model.data['image/png'];
    if(png_data !== undefined && png_data !== null) {
      // We have PNG data, use it
      this.updateImage(png_data);
      return Promise.resolve();
    } else {
      // Create a new graph
      return this.createGraph(model);
    }
  }

  private hasGraphElement() {
    // Check for the presence of the .plot-container element that plotly.js
    // places at the top of the figure structure
    return this.node.querySelector('.plot-container') !==  null
  }

  private updateImage(png_data: string) {
    this.hideGraph();
    this._img_el.src = "data:image/png;base64," + <string>png_data;
    this.showImage();
  }

  private hideGraph() {
    // Hide the graph if there is one
    let el = <HTMLDivElement>this.node.querySelector('.plot-container');
    if (el !== null && el !== undefined) {
      el.style.display = "none"
    }
  }

  private showGraph() {
    // Show the graph if there is one
    let el = <HTMLDivElement>this.node.querySelector('.plot-container');
    if (el !== null && el !== undefined) {
      el.style.display = "block"
    }
  }

  private hideImage() {
    // Hide the image element
    let el = <HTMLImageElement>this.node.querySelector('.plot-img');
    if (el !== null && el !== undefined) {
      el.style.display = "none"
    }
  }

  private showImage() {
    // Show the image element
    let el = <HTMLImageElement>this.node.querySelector('.plot-img');
    if (el !== null && el !== undefined) {
      el.style.display = "block"
    }
  }

  private createGraph(model: IRenderMime.IMimeModel) {
    const { data, layout, frames, config } = model.data[this._mimeType] as
      | any
      | IPlotlySpec;

    return Plotly.react(this.node, data, layout, config).then(plot => {
      this.showGraph();
      this.hideImage();
      this.update();
      if (frames) {
        Plotly.addFrames(this.node, frames);
      }
      if (this.node.offsetWidth > 0 && this.node.offsetHeight > 0) {
        Plotly.toImage(plot, {
          format: 'png',
          width: this.node.offsetWidth,
          height: this.node.offsetHeight
        }).then((url: string) => {
          const imageData = url.split(',')[1];
          if (model.data['image/png'] !== imageData) {
            model.setData({
              data: {
                ...model.data,
                'image/png': imageData
              }
            });
          }
        });
      }

      // Handle webgl context lost events
      (<Plotly.PlotlyHTMLElement>(this.node)).on('plotly_webglcontextlost', () => {
            const png_data = <string>model.data['image/png'];
            if(png_data !== undefined && png_data !== null) {
              // We have PNG data, use it
              this.updateImage(png_data);
              return Promise.resolve();
            }
          });
    });
  }

  /**
   * A message handler invoked on an `'after-show'` message.
   */
  protected onAfterShow(msg: Message): void {
    this.update();
  }

  /**
   * A message handler invoked on a `'resize'` message.
   */
  protected onResize(msg: Widget.ResizeMessage): void {
    this.update();
  }

  /**
   * A message handler invoked on an `'update-request'` message.
   */
  protected onUpdateRequest(msg: Message): void {
    if (this.isVisible && this.hasGraphElement()) {
      Plotly.redraw(this.node).then(() => {
        Plotly.Plots.resize(this.node);
      });
    }
  }

  private _mimeType: string;
  private _img_el: HTMLImageElement;
  private _model: IRenderMime.IMimeModel
}

/**
 * A mime renderer factory for Plotly data.
 */
export const rendererFactory: IRenderMime.IRendererFactory = {
  safe: true,
  mimeTypes: [MIME_TYPE],
  createRenderer: options => new RenderedPlotly(options)
};

const extensions: IRenderMime.IExtension | IRenderMime.IExtension[] = [
  {
    id: '@jupyterlab/plotly-extension:factory',
    rendererFactory,
    rank: 0,
    dataType: 'json',
    fileTypes: [
      {
        name: 'plotly',
        mimeTypes: [MIME_TYPE],
        extensions: ['.plotly', '.plotly.json'],
        iconClass: CSS_ICON_CLASS
      }
    ],
    documentWidgetFactoryOptions: {
      name: 'Plotly',
      primaryFileType: 'plotly',
      fileTypes: ['plotly', 'json'],
      defaultFor: ['plotly']
    }
  }
];

export default extensions;