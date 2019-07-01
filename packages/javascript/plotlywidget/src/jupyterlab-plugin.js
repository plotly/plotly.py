var plotly = require('./index');
var base = require('@jupyter-widgets/base');

/**
 * The widget manager provider.
 */
module.exports = {
  id: 'plotlywidget',
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
