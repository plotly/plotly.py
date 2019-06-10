var tape = require('tape')
var sccmp = require('oriented-simplicial-complex-compare')
var boundary = require('../boundary')

tape('boundary', function (t) {
  t.equals(
    sccmp(boundary([[0, 1, 2]]),
      [ [0, 1], [1, 2], [2, 0] ]), 0)

  t.end()
})
