'use strict'

var tape = require('tape')
var rv = require('../index')
var equal = require('../equals')
var sub = require('../sub')

tape('subtract', function(t) {

  var a = rv([1.5])
  var b = rv([1.25])
  var e = rv([0.25])
  var r = sub(a, b)

  t.ok(equal(e, r), '1.5 - 1.25 = 0.25')
  t.end()
})

tape('subtract', function(t) {

  var a = rv([1.5])
  var b = rv([-1.25])
  var e = rv([2.75])
  var r = sub(a, b)

  t.ok(equal(e, r), '1.5 - -1.25 = 2.75')
  t.end()
})
