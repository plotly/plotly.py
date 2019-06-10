'use strict'

var bnadd = require('big-rat/add')

module.exports = add

function add (a, b) {
  var n = a.length
  var r = new Array(n)
  for (var i=0; i<n; ++i) {
    r[i] = bnadd(a[i], b[i])
  }
  return r
}
