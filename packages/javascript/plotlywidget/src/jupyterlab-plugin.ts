import { IJupyterWidgetRegistry } from "@jupyter-widgets/base";

import { Application, IPlugin } from "@lumino/application";

import { Widget } from "@lumino/widgets";

import * as plotly from "./index";

import { MODULE_NAME, MODULE_VERSION } from "./version";

/**
 * Activate the widget extension.
 */
function activateWidgetExtension(
  app: Application<Widget>,
  registry: IJupyterWidgetRegistry
): void {
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: plotly,
  });
}

/**
 * The widget plugin.
 */
const widgetPlugin: IPlugin<Application<Widget>, void> = {
  id: "plotlywidget",
  requires: [IJupyterWidgetRegistry],
  activate: activateWidgetExtension,
  autoStart: true,
} as IPlugin<Application<Widget>, void>;

export default widgetPlugin;
