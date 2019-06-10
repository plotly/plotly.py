'use strict'

var bndiv = require('big-rat/div')

module.exports = div

function div(a, b) {
  var n = a.length
  var r = new Array(n)
    for(var i=0; i<n; ++i) {
    r[i] = bndiv(a[i], b[i])
  }
  return r
}
