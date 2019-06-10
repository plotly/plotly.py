'use strict'

var parseUnit = require('parse-unit')

module.exports = toPX

var PIXELS_PER_INCH = 96

var defaults = {
  'ch': 8,
  'ex': 7.15625,
  'em': 16,
  'rem': 16,
  'in': PIXELS_PER_INCH,
  'cm': PIXELS_PER_INCH / 2.54,
  'mm': PIXELS_PER_INCH / 25.4,
  'pt': PIXELS_PER_INCH / 72,
  'pc': PIXELS_PER_INCH / 6,
  'px': 1
}

function toPX(str) {
  if (!str) return null

  if (defaults[str]) return defaults[str]

  // detect number of units
  var parts = parseUnit(str)
  if (!isNaN(parts[0]) && parts[1]) {
    var px = toPX(parts[1])
    return typeof px === 'number' ? parts[0] * px : null
  }

  return null
}
