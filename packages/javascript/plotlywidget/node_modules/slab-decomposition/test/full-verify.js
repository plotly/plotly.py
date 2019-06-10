"use strict"

module.exports = verifyFull

var orient = require("robust-orientation")
var createSlabs = require("../slabs.js")
var rayBrutal = require("./bruteforce-ray")
var invariant = require("./invariant")
var genPoints = require("./generate-test-points")

function verifyFull(t, segments) {
  function perm(rotate, flipX, flipY) {
    var signX = flipX ? -1 : 1
    var signY = flipY ? -1 : 1
    var parity = (flipX|0) ^ (flipY|0)
    var result = new Array(segments.length)
    for(var i=0; i<segments.length; ++i) {
      var s = new Array(2)
      for(var j=0; j<2; ++j) {
        var p = segments[i][j]
        if(rotate) {
          s[j^parity] = [ signX * p[1], signY * p[0] ]
        } else {
          s[j^parity] = [ signX * p[0], signY * p[1] ]
        }
      }
      result[i] = s
    }
    return result
  }

  function doTest(a, b, c) {
    var s = perm(a, b, c)
    var str = (a|0) + "" + (b|0) + "" + (c|0)
    var slabs = createSlabs(s)
    invariant(t, slabs)
    var points = genPoints(s)
    for(var i=0; i<points.length; ++i) {
      var expected = rayBrutal(s, points[i])
      var computed = slabs.castUp(points[i])
      if(expected>=0 && orient(s[expected][0], s[expected][1], points[i]) === 0) {
        if(computed < 0) {
          t.fail("castRay(" + points[i].join() + "): expected surface hit, got nothing - seg = (" + s[expected].join(")-(") + ")")
        } else {
          t.equals(orient(s[computed][0], s[computed][1], points[i]), 0, "castRay(" + points[i].join() + "): expect on surface")
        }
      } else if(expected < 0) {
        t.equals(computed, -1, "castRay(" + points[i].join() + ") - " + str + "-miss expected")
      } else {
        var x = s[computed]
        var y = s[expected]
        if(points[i][0] === x[0][0] && x[0][0] === y[0][0] && x[0][1] === x[0][1]) {
          t.ok(true, "end points match")
        } else {
          t.equals(computed, expected, "castRay(" + points[i].join() + ") - " + str)
        }
      }
    }
  }

  doTest(false, false, false)
  doTest(false, false, true)
  doTest(false, true, true)
  doTest(false, true, true)
  doTest(true, false, false)
  doTest(true, false, true)
  doTest(true, true, false)
  doTest(true, true, true)
}