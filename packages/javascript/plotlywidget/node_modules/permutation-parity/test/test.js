"use strict"

var tape = require("tape")
var sgn = require("../permutation-sign")

tape("permutation-parity", function(t) {

  t.equals(sgn([0,1]), 1)
  t.equals(sgn([1,0]), -1)
  t.equals(sgn([0,0]), 0)

  t.end()
})