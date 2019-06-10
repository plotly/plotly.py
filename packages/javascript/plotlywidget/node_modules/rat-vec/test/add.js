'use strict'

var tape = require('tape')
var rv = require('../index')
var equal = require('../equals')
var add = require('../add')
var float = require('../to-float');

tape('check addition', function(t) {
  t.ok(equal(
    add(
      rv([1,2]),
      rv([1,3])),
    rv([2,5])))

  t.end()
})

tape('create, add, and to float', function(t) {
  t.deepEqual(float(add(
    rv([1/2,1/4]),
    rv([1/2,1/8]))
  ), [1, 3/8])

  t.end()
})
