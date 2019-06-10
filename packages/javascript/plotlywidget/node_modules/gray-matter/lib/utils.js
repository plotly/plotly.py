'use strict';

var stripBom = require('strip-bom-string');
exports.typeOf = require('kind-of');

/**
 * Returns true if `val` is a buffer
 */

exports.isBuffer = function(val) {
  return exports.typeOf(val) === 'buffer';
};

/**
 * Returns true if `val` is an object
 */

exports.isObject = function(val) {
  return exports.typeOf(val) === 'object';
};

/**
 * Cast `input` to a buffer
 */

exports.toBuffer = function(input) {
  if (typeof input === 'string') {
    return new Buffer(input);
  }
  return input;
};

/**
 * Cast `val` to a string.
 */

exports.toString = function(input) {
  if (exports.isBuffer(input)) {
    return stripBom(String(input));
  }
  if (typeof input !== 'string') {
    throw new TypeError('expected input to be a string or buffer');
  }
  return stripBom(input);
};

/**
 * Cast `val` to an array.
 */

exports.arrayify = function(val) {
  return val ? (Array.isArray(val) ? val : [val]) : [];
};

/**
 * Returns true if `str` starts with `substr`.
 */

exports.startsWith = function(str, substr, len) {
  if (typeof len !== 'number') len = substr.length;
  return str.slice(0, len) === substr;
};
