'use strict'

var bnequal = require('big-rat/equals')

module.exports = equal

function equal(a, b) {
  var n = a.length
  for(var i=0; i<n; ++i) {
    if(!bnequal(a[i], b[i])) {
      return false
    }
  }
  return true
}
