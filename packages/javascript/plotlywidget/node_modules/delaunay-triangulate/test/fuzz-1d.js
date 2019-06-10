"use strict"

var tape = require("tape")
var dt = require("../triangulate")
var isDelaunay = require("./util/is-delaunay")

tape("fuzz-1d", function(t) {
  var points = new Array(40)
  for(var j=0; j<40; ++j) {
    points[j] = [ Math.random() ]
  }
  isDelaunay(t, dt(points), points)
  t.end()
})