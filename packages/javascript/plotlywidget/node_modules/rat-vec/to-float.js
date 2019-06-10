'use strict'

var bnToFloat = require('big-rat/to-float')

module.exports = toFloat

function toFloat(v) {
  return v.map(bnToFloat)
}
