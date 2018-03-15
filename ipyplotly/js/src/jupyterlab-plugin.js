var ipyplotly = require('./index');
var base = require('@jupyter-widgets/base');

/**
 * The widget manager provider.
 */
module.exports = {
  id: 'ipyplotly',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipyplotly',
          version: ipyplotly.version,
          exports: ipyplotly
      });
    },
  autoStart: true
};
