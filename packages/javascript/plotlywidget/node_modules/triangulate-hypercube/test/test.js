"use strict"

var tape = require("tape")
var triangulate = require("../triangulate-cube")

tape("triangulate-hypercube", function(t) {
  console.log(triangulate(0))
  console.log(triangulate(1))
  console.log(triangulate(2))
  console.log(triangulate(3))
  
  t.end()
})