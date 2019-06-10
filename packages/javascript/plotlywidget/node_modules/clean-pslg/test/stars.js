'use strict'

var tape = require('tape')
var cleanPSLG = require('../clean-pslg')
var checkPSLG = require('./check-graph')

tape('stars', function(t) {

  for(var n=0; n<10; ++n) {
    var points = []
    var edges = []
    for(var i=0; i<10; ++i) {
      var x = Math.random() * 0.8 - 0.4
      var y = Math.random() * 0.8 - 0.4
      points.push([0.5+x,0.5+y], [0.5-x,0.5-y])
      edges.push([2*i, 2*i+1])
    }
    cleanPSLG(points, edges)
    checkPSLG(t, points, edges)
  }

  t.end()
})
