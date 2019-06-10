"use strict"

var tape = require("tape")
var compare = require("./util/normalize").compare
var triangulate = require("../triangulate")

tape("delaunay-2d", function(t) {
  var points = [
    [0, 1],
    [1, 0],
    [1, 1],
    [0, 0],
    [0.5, 0.5]
  ]

  compare(t, triangulate(points), [
      [4,0,3],
      [4,2,0],
      [4,2,1],
      [4,3,1]
    ], "simple 2d")

  compare(t, triangulate(points, true), [
      [4,0,3],
      [4,2,0],
      [4,2,1],
      [4,3,1],
      [-1,3,0],
      [-1,0,2],
      [-1,1,2],
      [-1,1,3]
    ], "2d + point at infinity")

  points.push([0.5, 0.5])
  compare(t, triangulate(points), [
      [4,0,3],
      [4,2,0],
      [4,2,1],
      [4,3,1]
    ], "2d + repeated point")

  t.end()
})