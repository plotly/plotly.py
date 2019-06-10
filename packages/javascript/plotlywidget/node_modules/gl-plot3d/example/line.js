'use strict'

var createScene = require('../scene')
var createLine = require('gl-line3d')

var scene = createScene()

var points = []
for(var t = 0; t< 1000; ++t) {
  var theta = Math.PI * t / 200.0
  points.push([Math.cos(theta), 0.002 * t, Math.sin(theta)])
}

var linePlot = createLine({
  gl:        scene.gl,
  position:  points,
  lineWidth: 5,
  color:     [1,0,0]
})

scene.add(linePlot)
