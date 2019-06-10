'use strict'

var tape        = require('tape')
var triangulate = require('../tripolyline')

tape(function(t) {

  var points = []
  var loop   = []

  for(var i=0; i<10; ++i) {
    points.push([0,i])
  }
  for(var i=0; i<10; ++i) {
    points.push([i,10])
  }
  for(var i=10; i>0; --i) {
    points.push([10,i])
  }
  for(var i=10; i>0; --i) {
    points.push([i,0])
  }
    
  for(var i=0; i<points.length; ++i) {
    loop[i] = i
  }

  var faces = triangulate([loop], points)
  t.equals(faces.length, 38)

  t.end()
})