'use strict';

var extend = require('extend-shallow');
var typeOf = require('kind-of');
var getEngine = require('./engine');
var defaults = require('./defaults');

module.exports = function(file, data, options) {
  if (data == null && options == null) {
    switch (typeOf(file)) {
      case 'object':
        data = file.data;
        options = {};
        break;
      case 'string':
        return file;
      default: {
        throw new TypeError('expected file to be a string or object');
      }
    }
  }

  var str = file.content;
  var opts = defaults(options);
  if (data == null) {
    if (!opts.data) {
      return file;
    }
    data = opts.data;
  }

  var language = file.language || opts.language;
  var engine = getEngine(language, opts);
  if (typeof engine.stringify !== 'function') {
    throw new TypeError('expected "' + language + '.stringify" to be a function');
  }

  data = extend({}, file.data, data);
  var open = opts.delimiters[0];
  var close = opts.delimiters[1];
  var matter = engine.stringify(data, options).trim();
  var buf = '';

  if (matter !== '{}') {
    buf = newline(open) + newline(matter) + newline(close);
  }

  if (typeof file.excerpt === 'string' && file.excerpt !== '') {
    if (str.indexOf(file.excerpt.trim()) === -1) {
      buf += newline(file.excerpt) + newline(close);
    }
  }

  return buf + newline(str);
};

function newline(str) {
  return str.slice(-1) !== '\n' ? str + '\n' : str;
}
