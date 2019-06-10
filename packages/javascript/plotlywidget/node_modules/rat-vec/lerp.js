'use strict'

var muls = require('./muls')
var add = require('./add')
var sub = require('./sub')

module.exports = lerp

function lerp(a, b, t) {
  return add(a, muls(sub(b, a), t));
}
