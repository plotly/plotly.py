"use strict"

var simplify = require("../simplify")
var tape = require("tape")

tape("simplify-2d-complex", function(t) {

  t.same(simplify([[0,1]], [
    [0, 0],
    [1,0]
    ], 100),
  { positions: [[0,0], [1,0]],
    edges: [[0,1]]
  })

  t.same(simplify([[0,1], [1,2]], [
    [0, 0],
    [0.5, 0],
    [1,0]
    ], 100),
  { positions: [[0,0], [1,0]],
    edges: [[0,1]]
  })

  t.same(simplify([[0,1], [0,2], [0,3], [0,4]], [
    [0, 0],
    [-1, 0],
    [1,0],
    [0,-1],
    [0,1]
    ], 100),
  { positions: [[0, 0],
    [-1, 0],
    [1,0],
    [0,-1],
    [0,1]],
    edges: [[0,1], [0,2], [0,3], [0,4]]
  })


  t.same(simplify([[0,1], [0,2], [0,3], [0,4],[1,5], [2,6], [3,7], [4,8]], [
    [0, 0],
    [-1, 0],
    [1,0],
    [0,-1],
    [0,1],
    [-2, 0],
    [2,0],
    [0,-2],
    [0,2]
    ], 100),
  { positions: [[0, 0],
    [-2, 0],
    [2,0],
    [0,-2],
    [0,2]],
    edges: [[0,1], [0,2], [0,3], [0,4]]
  }, "non-manifold")

  t.same(simplify([[0,1], [1,2], [2,0]],
      [[0,0],
      [1,0],
      [0,1]],
      0.1
    ),{
    positions: [[0,0], [1,0], [0,1]],
    edges: [[0,1], [2,0], [1,2]]
  })

  t.same(simplify([[0,1], [1,2], [2,0]],
      [[0,0],
      [1,0],
      [0,1]],
      100000.0
    ),{
    positions: [],
    edges: []
  })

  //Test line simplification
  for(var j=0; j<100; ++j) {
    var theta = 2.0 * Math.PI * j / 100.0
    var dx = Math.cos(theta)
    var dy = Math.sin(theta)
    for(var k=0; k<5; ++k) {
      var w = k / 200.0
      var points = []
      var cells = []
      for(var i=0; i<100; ++i) {
        points.push([i*dx + w*Math.random(), i*dy + w*Math.random()])
        if(i > 0) {
          cells.push([i-1, i])
        }
      }
      t.same(simplify(cells, points, 1), {
        positions: [points[0], points[points.length-1]],
        edges: [[0,1]]
      }, "angle=" + theta + " var=" + w)
    }
  }

  //Test non-manifold simplification

  t.end()
})