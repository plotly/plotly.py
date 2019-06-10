"use strict"

var crosses = require("../segseg")
var tape = require("tape")

tape("segment-segment crossing", function(t) {

  t.ok(crosses([-1, 0], [1, 0], [0,-1], [0,1]), "general test")
  t.ok(!crosses([0.5, 0], [1, 0], [0,-1], [0,1]))
  t.ok(crosses([0, 0], [1, 0], [0,-1], [0,1]))
  t.ok(crosses([0, 0], [100000000000000020000, 1e-12], 
        [1,0], [1e20, 1e-11]))
  t.ok(!crosses([0, 0], [1e20, 1e-11], 
        [1,0], [100000000000000020000, 1e-12]))

  t.ok(!crosses(
    [0, 1],
    [0, 2],
    [0, -1],
    [0, -2]), "collinear, no intersect")

  t.ok(crosses(
    [0, 1],
    [0, 2],
    [0, 1.5],
    [0, -2]), "collinear, intersect")

  t.ok(crosses(
    [0, 1],
    [0, 2],
    [0, 1],
    [0, -2]), "collinear, endpoint touch")

  t.ok(crosses(
    [0, 1],
    [0, -1],
    [0, 0],
    [0, 1]), "endpoint touches")

  t.end()
})