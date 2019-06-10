'use strict'

var bnmul = require('big-rat/mul')

module.exports = mul

function mul(a, b) {
  var n = a.length
  var r = new Array(n)
    for(var i=0; i<n; ++i) {
    r[i] = bnmul(a[i], b[i])
  }
  return r
}
