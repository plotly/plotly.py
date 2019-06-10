'use strict'

var bnabs = require('big-rat/abs')

module.exports = abs

function abs(v) {
  return v.map(bnabs)
}
