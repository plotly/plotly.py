"use strict"

var tape = require("tape")
var ch = require("../ich")
var sameCells = require("./util/normalize").compare

function bowlHull(t, points, msg) {
  var tagged = points.map(function(p, i) {
    return [ p, i ]
  })
  var lifted = points.map(function(p) {
    return [ p, p*p ]
  })

  tagged.sort(function(a,b) {
    return a[0] - b[0]
  })

  var expectedCells = []
  for(var i=1; i<tagged.length; ++i) {
    expectedCells.push([tagged[i-1][1], tagged[i][1]])
  }
  expectedCells.push([tagged[tagged.length-1][1], tagged[0][1]])

  var hull = ch(lifted)
  sameCells(t, hull, expectedCells, msg)
}

tape("parabola", function(t) {

  //In order list
  var list = []
  for(var i=-10; i<=10; ++i) {
    list.push(i)
  }
  bowlHull(t, list, "ordered list")

  //Random cells
  for(var j=0; j<10; ++j) {
    var points = []
    for(var i=0; i<100; ++i) {
      points.push(Math.random())
    }
    bowlHull(t, points, "random")
  }

  t.end()
})