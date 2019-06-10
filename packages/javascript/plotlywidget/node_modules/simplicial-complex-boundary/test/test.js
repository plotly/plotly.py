'use strict'

var tape = require('tape')
var sccmp = require('oriented-simplicial-complex-compare')
var bnd = require('../boundary')

tape('boundary', function(t) {
  t.equals(sccmp(
      bnd([[0, 1, 2], [2, 1, 3]]),
      [[0, 1], [1, 3], [3, 2], [2, 0]]),
    0)
  t.end()
})
