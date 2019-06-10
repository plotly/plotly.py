'use strict'

var createScene = require('../scene')
var createScatter = require('gl-scatter3d')
var bunny = require('bunny')

var scene = createScene()
var scatter = createScatter({
  gl:           scene.gl,
  position:     bunny.positions,
  size:         10,
  glyph:        '★',
  orthographic: true,
  lineColor:    [0,0,0],
  color:        [1,0,0],
  lineWidth:    1
})

scene.add(scatter)
