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
  }

  /**
   * Render Plotly into this widget's node.
   */
  renderModel(model: IRenderMime.IMimeModel): Promise<void> {
    const { data, layout, frames, config } = model.data[this._mimeType] as
      | any
      | IPlotlySpec;
    // const metadata = model.metadata[this._mimeType] as any || {};
    return Plotly.react(this.node, data, layout, config).then(plot => {
      this.update();
      if (frames) {
        Plotly.addFrames(this.node, frames).then(() => {
          Plotly.animate(this.node);
        });
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
    if (this.isVisible) {
      Plotly.redraw(this.node).then(() => {
        Plotly.Plots.resize(this.node);
      });
    }
  }

  private _mimeType: string;
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