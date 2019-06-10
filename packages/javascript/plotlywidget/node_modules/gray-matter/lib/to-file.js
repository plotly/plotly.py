'use strict';

var typeOf = require('kind-of');
var stringify = require('./stringify');
var utils = require('./utils');

/**
 * Normalize the given value to ensure an object is returned
 * with the expected properties.
 */

module.exports = function(file) {
  if (typeOf(file) !== 'object') {
    file = { content: file };
  }

  if (typeOf(file.data) !== 'object') {
    file.data = {};
  }

  if (file.content == null) {
    file.content = file.contents;
  }

  var orig = utils.toBuffer(file.content);
  Object.defineProperty(file, 'orig', {
    configurable: true,
    enumerable: false,
    writable: true,
    value: orig
  });

  Object.defineProperty(file, 'matter', {
    configurable: true,
    enumerable: false,
    writable: true,
    value: file.matter || ''
  });

  Object.defineProperty(file, 'language', {
    configurable: true,
    enumerable: false,
    writable: true,
    value: file.language || ''
  });

  Object.defineProperty(file, 'stringify', {
    configurable: true,
    enumerable: false,
    writable: true,
    value: function(data, options) {
      if (options && options.language) {
        file.language = options.language;
      }
      return stringify(file, data, options);
    }
  });

  file.content = utils.toString(file.content);
  file.excerpt = '';
  return file;
};
