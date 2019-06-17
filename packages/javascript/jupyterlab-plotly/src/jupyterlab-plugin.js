var plotly = require('./index');
var base = require('@jupyter-widgets/base');

/**
 * The widget manager provider.
 */
module.exports = {
  id: 'jupyterlab-plotly',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'plotlywidget',
          version: plotly.version,
          exports: plotly
      });
    },
  autoStart: true
};
