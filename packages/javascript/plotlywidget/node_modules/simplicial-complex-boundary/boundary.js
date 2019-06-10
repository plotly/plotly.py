'use strict'

module.exports = boundary

var bnd = require('boundary-cells')
var reduce = require('reduce-simplicial-complex')

function boundary(cells) {
  return reduce(bnd(cells))
}
