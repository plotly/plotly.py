'use strict'

var rat = require('big-rat')
var bnmul = require('big-rat/mul')
var recip = require('big-rat/recip')

module.exports = divs

function divs(a, s) {
  var sr = recip(rat(s))
  var n = a.length
  var r = new Array(n)
    for(var i=0; i<n; ++i) {
    r[i] = bnmul(a[i], sr)
  }
  return r
}
