"use strict"

var robustProduct = require("../product.js")
var tape = require("tape")

function pow2(n) {
  return Math.pow(2, n)
}

tape(function(t) {
  for(var i=-20; i<=20; ++i)
  for(var j=-20; j<=20; ++j) {
    t.same(robustProduct([i], [j]), [i*j])
  }
  t.same(robustProduct([pow2(-50), pow2(50)], [pow2(-50), pow2(50)]), [pow2(-100), pow2(1), pow2(100)])
  t.end()
})