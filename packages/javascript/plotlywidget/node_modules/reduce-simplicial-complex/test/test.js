'use strict'

var tape = require('tape')
var compareComplex = require('oriented-simplicial-complex-compare')
var reduce = require('../reduce')

tape('reduceCells', function(t) {

  var cells = [
    [1, 2, 3],
    [2, 1, 3],
    [3, 2, 1],
    [4, 5, 6],
    [7, 8]
  ]

  t.equals(compareComplex(reduce(cells), [
    [3,2,1],
    [4,5,6],
    [7,8]
  ]), 0)

  t.end()
})
