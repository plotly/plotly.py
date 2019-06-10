'use strict'

var createScene = require('../scene')
var createScatter = require('gl-scatter3d')
var createErrorBars = require('gl-error3d')

var points = [ [0,0,0], [1,1,1], [-1, 2, -3] ]
var errors = [
  [[-0.5,-0.5,-0.5],[0.5,0.5,0.5]],
  [[-0.1,-1,-2],[0,0,0]],
  [[-0.1,-0.1,-0.1],[0.1,0.1,0.1]]
]

var scene = createScene()

var scatter = createScatter({
  gl:           scene.gl,
  position:     points,
  size:         20,
  orthographic: true,
  lineColor:    [0,0,0],
  color:        [0.7,0.8,0.4],
  lineWidth:    1
})
scene.add(scatter)


var errorBars = createErrorBars({
  gl:       scene.gl,
  position: points,
  error:    errors,
  color:    [0.9, 0.3, 0.3]
})

scene.add(errorBars)
