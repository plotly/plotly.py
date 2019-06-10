'use strict';

var extend = require('extend-shallow');
var engines = require('./engines');
var utils = require('./utils');

module.exports = function(options) {
  var opts = extend({}, options);

  // ensure that delimiters are an array
  opts.delimiters = utils.arrayify(opts.delims || opts.delimiters || '---');
  if (opts.delimiters.length === 1) {
    opts.delimiters.push(opts.delimiters[0]);
  }

  opts.language = (opts.language || opts.lang || 'yaml').toLowerCase();
  opts.engines = extend({}, engines, opts.parsers, opts.engines);
  return opts;
};
