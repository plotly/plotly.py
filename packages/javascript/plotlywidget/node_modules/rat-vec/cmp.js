'use strict'

var bncmp = require('big-rat/cmp')

module.exports = cmp

function cmp(a, b) {
  var n = a.length
  var r = new Array(n)
    for(var i=0; i<n; ++i) {
    r[i] = bncmp(a[i], b[i])
  }
  return r
}
