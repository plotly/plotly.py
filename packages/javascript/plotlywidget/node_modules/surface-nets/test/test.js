"use strict"

var tape = require("tape")
var surfaceNets = require("../surfacenets")
var ndarray = require("ndarray")
var fill = require("ndarray-fill")

tape("sphere-test", function(t) {
  var shape = []
  var size = 1
  var fact = 1
  var funcs = [
    function(x) {
      return Math.pow(x-8,2)
    },
    function(x,y) {
      return Math.pow(x-8,2) + Math.pow(y-8,2)
    },
    function(x,y,z) {
      return Math.pow(x-8,2) + Math.pow(y-8,2) + Math.pow(z-8,2)
    },
    function(x,y,z,w) {
      return Math.pow(x-8,2) + Math.pow(y-8,2) + Math.pow(z-8,2) + Math.pow(w-8,2)
    }
  ]
  for(var d=1; d<=4; ++d) {
    shape.push(16)
    size *= 16
    fact *= d

    var x = ndarray(new Float32Array(size), shape)
    fill(x, funcs[d-1])
    var surf = surfaceNets(x, 36)
    for(var k=0; k<surf.positions.length; ++k) {
      var p = surf.positions[k]
      var u = 0.0
      for(var j=0; j<d; ++j) {
        u += Math.pow(p[j]-8,2)
      }
      t.ok(Math.abs(u-36) <= 1.2, "test: " + d + "d - " + u)
    }
  }
  t.end()
})