'use strict'

var compareCells = require('compare-cell')
var parity = require('cell-orientation')

module.exports = compareOrientedCells

function compareOrientedCells(a, b) {
  return compareCells(a, b) || parity(a) - parity(b)
}
