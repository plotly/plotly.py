"use strict"

var tape = require("tape")
var e2a = require("../e2a")

tape("edges-to-adjacency-list", function(t) {
  t.same(e2a([
      [0,1],
      [1,2],
      [2,3]
    ]), [
    [1],
    [0,2],
    [1,3],
    [2]
  ])
  t.end()
})