'use strict'

var tape = require('tape')
var equal = require('../equals')
var makeVec = require('../index')

tape('equality test', function(t) {

  function eq(a, b) {
    return equal(makeVec(a), makeVec(b))
  }

  t.ok(!eq([1,3], [2,6]))
  t.ok(eq([1,1], [1,1]))
  t.ok(!eq([0,1], [1,1]))

  t.end()
})
