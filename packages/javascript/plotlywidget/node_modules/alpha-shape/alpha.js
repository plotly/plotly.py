module.exports = alphaShape

var ac = require('alpha-complex')
var bnd = require('simplicial-complex-boundary')

function alphaShape(alpha, points) {
  return bnd(ac(alpha, points))
}