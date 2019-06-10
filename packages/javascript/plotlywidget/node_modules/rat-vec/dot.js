'use strict'

var rat = require('big-rat')
var mul = require('big-rat/mul')
var add = require('big-rat/add')

module.exports = dot

function dot(a, b) {
  var s = rat(0)
  var n = a.length
  for(var i=0; i<n; ++i) {
    s = add(s, mul(a[i], b[i]))
  }
  return s
}
