'use strict'

var tape = require('tape')
var rv = require('../index')
var equal = require('../equals')
var mul = require('../mul')
var rat = require('big-rat')

tape('multiply wholes', function(t) {
  var a = rv([5])
  var b = rv([3])
  var e = rv([15])

  var r = mul(a, b)

  t.ok(equal(r, e), '3 * 5 is 15')
  t.end()
})

tape('multiply fraction (positive)', function(t) {
  var a = rv([rat(1, 2)])
  var b = rv([3])
  var e = rv([rat(15, 10)])

  var r = mul(a, b)

  t.ok(equal(r, e), '3 * 1/2 is 15/10')
  t.end()
})

tape('multiply fraction (negative)', function(t) {
  var a = rv([rat(1, 2)])
  var b = rv([-3])
  var e = rv([rat(-15, 10)])

  var r = mul(a, b);

  t.ok(equal(r, e), '-3 * 1/2 is -15/10')
  t.end()
})
