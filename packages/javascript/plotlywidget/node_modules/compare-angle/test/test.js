"use strict"

var tape = require("tape")
var compareAngle = require("../cmpangle")
var sgn = require("signum")

tape("compare-angle", function(t) {
  var pts = [
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0]
  ]
  var a = [2,0]
  var b = [0,0]

  //det M[i] must be > 0
  var M = [
    [1, 0, 0, 1],
    [2, 0, 0, 0.5],
    [0, 1, -1, 0]
  ]
  var X = [ [0,0], [10, 10], [-3, 1] ]

  function xform(i, p) {
    var m = M[i]
    var x = X[i]
    return [
      x[0] + m[0]*p[0] + m[1]*p[1],
      x[1] + m[2]*p[0] + m[3]*p[1]
    ]
  }

  for(var i=0; i<M.length; ++i) {
    var ai = xform(i, a)
    var bi = xform(i, b)
    for(var j=0; j<pts.length; ++j) {
      var ci = xform(i, pts[j])
      for(var k=0; k<pts.length; ++k) {
        var di = xform(i, pts[k])
        t.equals(compareAngle(ai, bi, ci, di), sgn(j - k), "angle:" + ai + " " + bi + " " + ci + " " + di)
      }
    }
  }

  t.end()
})