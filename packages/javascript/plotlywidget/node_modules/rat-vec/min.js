'use strict'

var bnmin = require('big-rat/min')

module.exports = min

function min(a, b) {
  var n = a.length
  var r = new Array(n)
    for(var i=0; i<n; ++i) {
    r[i] = bnmin(a[i], b[i])
  }
  return r
}
