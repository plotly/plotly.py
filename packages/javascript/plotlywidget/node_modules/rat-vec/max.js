'use strict'

var bnmax = require('big-rat/max')

module.exports = max

function max(a, b) {
  var n = a.length
  var r = new Array(n)
    for(var i=0; i<n; ++i) {
    r[i] = bnmax(a[i], b[i])
  }
  return r
}
