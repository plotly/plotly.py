"use strict"

var tape = require("tape")
var compare = require("./util/normalize").compare
var triangulate = require("../triangulate")

tape("edge-cases", function(t) {
  
  //Test triangulation with no points
  t.same(triangulate([]), [], "empty triangulation")
  t.same(triangulate([], true), [], "empty triangulation + infinity")

  t.same(triangulate([[0]]), [], "triangulation with 1 point")
  t.same(triangulate([[0]], true), [[-1,0]], "triangulation with 1 point + infinity")

  t.same(triangulate([[0,0]]), [], "one point in 2D")
  t.same(triangulate([[0,0]], true), [], "one point in 2D")
  
  t.same(triangulate([[0,0,0]]), [], "one point in 3D")
  t.same(triangulate([[0,0,0]], true), [], "one point in 3D")

  //Generate cuboids
  for(var d=1; d<=4; ++d) {
    var verts = []
    for(var i=0; i<(1<<d); ++i) {
      var p = new Array(d)
      for(var j=0; j<d; ++j) {
        if(i & (1<<j)) {
          p[j] = 1
        } else {
          p[j] = -1
        }
      }
      verts.push(p)
    }

    var h = triangulate(verts)
    t.ok(h.length > 0, "make sure no crash on hypercube, d=" + d)

    if(d > 1) {
      var line = []
      for(var i=0; i<10; ++i) {
        var p = new Array(i)
        for(var j=0; j<d; ++j) {
          p[j] = i
        }
        line.push(p)
      }
      t.same(triangulate(line), [], "test collinear, d=" + d)
    }
  }

  t.end()
})