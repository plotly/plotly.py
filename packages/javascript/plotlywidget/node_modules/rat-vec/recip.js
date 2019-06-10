'use strict'

var bnrecip = require('big-rat/recip')

module.exports = recip

function recip(a) {
  return a.map(bnrecip)
}
