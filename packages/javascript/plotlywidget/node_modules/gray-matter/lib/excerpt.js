'use strict';

var defaults = require('./defaults');

module.exports = function(file, options) {
  var opts = defaults(options);

  if (file.data == null) {
    file.data = {};
  }

  if (typeof opts.excerpt === 'function') {
    return opts.excerpt(file, opts);
  }

  var sep = file.data.excerpt_separator || opts.excerpt_separator;
  if (sep == null && (opts.excerpt === false || opts.excerpt == null)) {
    return file;
  }

  var delimiter = sep || opts.delimiters[0];
  if (typeof opts.excerpt === 'string') {
    delimiter = opts.excerpt;
  }

  // if enabled, get the excerpt defined after front-matter
  var idx = file.content.indexOf(delimiter);
  if (idx !== -1) {
    file.excerpt = file.content.slice(0, idx);
  }

  return file;
};
