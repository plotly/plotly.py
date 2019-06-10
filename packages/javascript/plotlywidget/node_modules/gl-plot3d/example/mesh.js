'use strict'

var createScene = require('../scene')
var createMesh = require('gl-mesh3d')
var bunny = require('bunny')

var scene = createScene()
var mesh = createMesh({
  gl:         scene.gl,
  cells:      bunny.cells,
  positions:  bunny.positions,
  colormap:   'jet'
})

scene.add(mesh)
