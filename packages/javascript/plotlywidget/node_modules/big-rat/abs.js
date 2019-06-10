'use strict'

var sign = require('./sign')
var neg = require('./neg')

module.exports = abs

function abs(a) {
  if(sign(a) < 0) {
    return neg(a)
  }
  return a
}
