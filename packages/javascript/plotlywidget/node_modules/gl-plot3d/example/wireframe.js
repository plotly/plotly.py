'use strict'

require('enable-mobile')
var createScene = require('../scene')
var createMesh = require('gl-mesh3d')
var bunny = require('bunny')
var sc = require('simplicial-complex')

var scene = createScene()
var mesh = createMesh({
  gl:         scene.gl,
  cells:      sc.skeleton(bunny.cells, 1),
  positions:  bunny.positions,
  colormap:   'jet'
})

scene.add(mesh)
