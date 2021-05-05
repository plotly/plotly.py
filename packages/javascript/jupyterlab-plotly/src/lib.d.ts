import { Data, Layout } from "plotly.js";
import { Layout } from "plotly.js/dist/plotly";

declare module "plotly.js/dist/plotly" {
  export * from "plotly.js";
  export type Frame = { [key: string]: any };
  export function addFrames(root: Plotly.Root, frames: Frame[]): Promise<void>;
  export function animate(root: Plotly.Root): void;

  type PlotlyEvent =
    | "plotly_webglcontextlost"
    | "plotly_restyle"
    | "plotly_relayout"
    | "plotly_update"
    | "plotly_click"
    | "plotly_hover"
    | "plotly_unhover"
    | "plotly_selected"
    | "plotly_deselect"
    | "plotly_doubleclick";

  export interface PlotlyHTMLElement extends HTMLElement {
    _fullData: Data;
    _fullLayout: Layout;
    data: Data;
    layout: Layout;
    on(event: PlotlyEvent, callback: (update: any) => void): void;
  }
}
