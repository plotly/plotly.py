"use strict"

var tape = require("tape")
var sgn = require("../sgn")

tape("signum", function(t) {
  t.equals(sgn(-0.00001), -1)
  t.equals(sgn(0), 0)
  t.equals(sgn(Infinity), 1)

  t.end()
})