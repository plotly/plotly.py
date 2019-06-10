"use strict"

var tape = require("tape")
var uniq = require("uniq")
var ch = require("../ich")

function createSphere(dimension, numBoundary, numInterior) {
  var points = []
  for(var i=0; i<numBoundary; ++i) {
    var point = new Array(dimension)
    var r2 = 0.0
    for(var j=0; j<dimension; ++j) {
      var v = Math.random()-0.5
      r2 += v*v
      point[j] = v
    }
    var r = Math.sqrt(r2)
    for(var j=0; j<dimension; ++j) {
      point[j] /= r
    }
    points.push(point)
  }
  for(var i=0; i<numInterior; ++i) {
    var point = new Array(dimension)
    for(var j=0; j<dimension; ++j) {
      point[j] = 0.5 * (Math.random() - 0.5)
    }
    points.push(point)
  }
  return points
}

function testSphere(t, dimension, numBoundary, numInterior) {
  var s = createSphere(dimension, numBoundary, numInterior)
  var hull = ch(s)
  var boundary = uniq(hull.reduce(function(f, c) {
    f.push.apply(f, c)
    return f
  }, []), function(a,b) { return a-b })
  t.equals(boundary.length, numBoundary, "sphere " + dimension + " boundary ok")
  for(var i=0; i<boundary.length; ++i) {
    t.equals(boundary[i], i, "boundary " + i)
  }
}

tape("sphere 2d", function(t) {
  for(var i=0; i<10; ++i) {
    testSphere(t, 2, 50, 50)
  }
  t.end()
})

tape("sphere 3d", function(t) {
  for(var i=0; i<10; ++i) {
    testSphere(t, 3, 100, 100)
  }
  t.end()
})

tape("sphere 4d", function(t) {
  for(var i=0; i<10; ++i) {
    testSphere(t, 4, 120, 120)
  }
  t.end()
})