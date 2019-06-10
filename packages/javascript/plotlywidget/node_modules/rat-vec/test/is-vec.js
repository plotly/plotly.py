'use strict'

var vec = require('../index')
var isVec = require('../is-vec')
var tape = require('tape')

tape('is-vector', function(t) {

  var x = [1,2,3]

  t.ok(!isVec(x))
  t.ok(isVec(vec(x)))
  t.ok(!isVec(null))
  t.ok(isVec([]))

  t.end()
})
