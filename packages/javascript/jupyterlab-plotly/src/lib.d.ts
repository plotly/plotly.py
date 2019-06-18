declare module 'plotly.js/dist/plotly' {
  export * from 'plotly.js';
  export type Frame = { [key: string]: any };
  export function addFrames(root: Plotly.Root, frames: Frame[]): Promise<void>;
  export function animate(root: Plotly.Root): void;

  export interface PlotlyHTMLElement extends HTMLElement {
    on(event: 'plotly_webglcontextlost', callback: () => void): void;
  }
}