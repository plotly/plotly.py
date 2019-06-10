'use strict'

var tape = require('tape')
var cleanPSLG = require('../clean-pslg')
var checkPSLG = require('./check-graph')

tape('collinear', function(t) {

  for(var n=0; n<10; ++n) {
    var points = []
    var edges = []
    for(var i=0; i<10; ++i) {
      var x0 = Math.random()
      var x1 = Math.random()
      points.push([x0, 0], [x1, 0])
      edges.push([2*i, 2*i+1])
    }
    cleanPSLG(points, edges)
    console.log(points.length, edges.length)
    console.log(points, edges)
    checkPSLG(t, points, edges)
  }

  t.end()
})
