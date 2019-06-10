"use strict"

var tape = require("tape")
var extractPlanes = require("../extract-planes")

tape(function(t) {
  console.log(extractPlanes([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]))
  t.end()
})