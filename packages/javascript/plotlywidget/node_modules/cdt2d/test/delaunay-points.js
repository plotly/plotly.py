'use strict'

var tape = require('tape')
var delaunay = require('delaunay-triangulate')
var gaussRandom = require('gauss-random')
var cdt = require('../cdt2d')

function compareLex(a, b) {
  for(var i=0; i<3; ++i) {
    var d = a[i] - b[i]
    if(d) {
      return d
    }
  }
  return 0
}

function normalizeCell(c) {
  if(c[0] < Math.min(c[1], c[2])) {
    return c
  }
  if(c[1] < Math.min(c[0], c[2])) {
    return [c[1], c[2], c[0]]
  }
  return [c[2], c[0], c[1]]
}

function flipCell(c) {
  return [c[1], c[0], c[2]]
}

function verifyDT(tape, points) {
  var expectedCells = delaunay(points)
  var actualCells = cdt(points)

  //Canonicalize cells
  actualCells = actualCells.map(normalizeCell).sort(compareLex)
  expectedCells = expectedCells.map(flipCell).map(normalizeCell).sort(compareLex)

  if(actualCells.length !== expectedCells.length) {
    tape.error('dt returned incorrect number of cells')
    return
  }
  for(var i=0; i<actualCells.length; ++i) {
    tape.equals(actualCells[i].join(), expectedCells[i].join(), 'cells match')
  }
}

tape('delaunay triangulation - grid', function(t) {

  function grid(nx, ny) {
    var points = []
    for(var i=0; i<nx; ++i) {
      for(var j=0; j<ny; ++j) {
        points.push([i, j])
      }
    }
    verifyDT(t, points)
  }

  grid(1, 1)
  grid(2, 2)
  grid(3, 3)
  grid(10, 10)
  grid(2, 10)
  grid(10, 2)
  grid(1, 10)
  grid(10, 1)
  grid(3, 10)
  grid(10, 3)

  t.end()
})


tape('delaunay triangulation - random points', function(t) {

  function testRandom(count, dist) {
    var points = []
    for(var i=0; i<count; ++i) {
      points.push([ dist(), dist() ])
    }
    verifyDT(t, points)
  }

  for(var i=0; i<10; ++i) {
    testRandom(100, Math.random.bind(Math))
  }

  for(var i=0; i<10; ++i) {
    testRandom(100, gaussRandom)
  }

  t.end()
})
