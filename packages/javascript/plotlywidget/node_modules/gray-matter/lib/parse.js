'use strict';

var getEngine = require('./engine');
var defaults = require('./defaults');

module.exports = function(language, str, options) {
  var opts = defaults(options);
  var engine = getEngine(language, opts);
  if (typeof engine.parse !== 'function') {
    throw new TypeError('expected "' + language + '.parse" to be a function');
  }
  return engine.parse(str, opts);
};
