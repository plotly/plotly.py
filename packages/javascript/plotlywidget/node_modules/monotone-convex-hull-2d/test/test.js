'use strict'

var tape = require('tape')
var hull = require('../index')

tape('convex-hull-2d', function(t) {

  var res = hull([[0,0],[1,1],[1,0],[0.5,0.5],[0.7,0.1]])
  t.deepEqual(res, [ 0, 1, 2 ])

  var h = [[0,0], [1,0], [1,1], [0,1]]
  t.deepEqual(hull(h), [0,3,2,1])

  var h = [[0,0], [1,1], [1,0], [0,1]]
  t.deepEqual(hull(h), [0,3,1,2])

  for(var i=0; i<1000; ++i) {
    h.push([Math.random(), Math.random()])
    h.push([0,Math.random()])
    h.push([Math.random(),0])
    h.push([Math.random(),1])
    h.push([1,Math.random()])
  }
  t.deepEqual(hull(h), [0,3,1,2])

  //Degenerate cases
  t.deepEqual(hull([[0,0]]), [0])
  t.deepEqual(hull([]), [])
  t.deepEqual(hull([[0,0], [1,1]]), [0,1])
  t.deepEqual(hull([[0,0], [0,0]]), [0])


  t.end()
})