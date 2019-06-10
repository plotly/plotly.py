'use strict'

var tape = require('tape')
var crad = require('../crad')

tape('fuzz', function(t) {

  for(var d=2; d<5; ++d) {
    for(var i=0; i<100; ++i) {
      var radius = Math.random()
      var points = []
      for(var j=0; j<=d; ++j) {
        var p = new Array(d)
        var pl = 0.0
        for(var k=0; k<d; ++k) {
          p[k] = Math.random() - 0.5
          pl += Math.pow(p[k], 2)
        }
        pl = radius/Math.sqrt(pl)
        for(var k=0; k<d; ++k) {
          p[k] *= pl
        }
        points.push(p)
      }
      t.ok(Math.abs(crad(points) - radius) < 1e-4, 'radius ok d=' + d)
    }
  }

  t.end()
})