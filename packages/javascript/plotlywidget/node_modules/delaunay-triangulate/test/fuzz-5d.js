"use strict"

var tape = require("tape")
var dt = require("../triangulate")
var isDelaunay = require("./util/is-delaunay")

tape("fuzz-5d", function(t) {
  var points = new Array(10)
  for(var j=0; j<10; ++j) {
    points[j] = [ Math.random(), Math.random(), Math.random(), Math.random() ]
  }
  isDelaunay(t, dt(points), points)
  t.end()
})