"use strict"

var tape = require("tape")
var zc = require("../zc")
var ndarray = require("ndarray")

tape("zero-crossings", function(t) {

  t.same(zc(ndarray([-1,1])), [0.5])
  t.same(zc(ndarray([0, -0.25])), [0])
  t.same(zc(ndarray([-0.25, 0])), [1])

  t.end()
})