'use strict'

var bnneg = require('big-rat/neg')

module.exports = neg

function neg(v) {
  return v.map(bnneg)
}
