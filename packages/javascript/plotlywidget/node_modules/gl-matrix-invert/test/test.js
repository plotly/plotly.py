'use strict'

var tape = require('tape')
var invert = require('../invert')

tape('gl-matrix-invert', function(t) {


  t.same(invert([], [1, 0, 1, 1]), [1, 0, -1, 1])


  t.end()
})