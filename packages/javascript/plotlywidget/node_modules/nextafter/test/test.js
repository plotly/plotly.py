"use strict"

var tape = require("tape")
var nextafter = require("../nextafter")

tape("nextafter", function(t) {

  t.equals(nextafter(0,0), 0)
  t.equals(nextafter(1, Infinity), 1.0 + Math.pow(2, -52))
  t.equals(nextafter(1, 0), 1.0-Math.pow(2,-53))
  t.equals(nextafter(-1,-Infinity), -(1.0 + Math.pow(2, -52)))
  t.equals(nextafter(-1, 0), -1.0 + Math.pow(2, -53))
  t.equals(nextafter(1-Math.pow(2,-53), 2), 1)

  t.end()
})