"use strict"

var tape = require("tape")
var createExtractor = require("../contour.js")
var pack = require("ndarray-pack")


tape("test-vectorize", function(t) {

  var verts = []
  var cells = []
  var testVectorizer = createExtractor({
    order: [1, 0],
    vertex: function(x, y) {
      verts.push([x,y])
    },
    phase: function(s) {
      console.log(s)
      return s
    },
    cell: function(i, j, p0, p1) {
      cells.push([i,j,p0,p1])
    }
  })
  console.log(verts, cells)

  testVectorizer(pack(
    [ [0,1,0,0],
      [0,1,1,1],
      [1,1,1,0],
      [0,0,1,0] ] ))
  t.end()
})