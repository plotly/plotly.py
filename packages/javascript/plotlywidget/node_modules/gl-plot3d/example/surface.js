'use strict'

var createScene = require('../scene')
var createSurface = require('gl-surface3d')
var ndarray = require('ndarray')

var scene = createScene()

//Create parameters for a torus
var size = 64
var coords = [
  ndarray(new Float32Array(4*(size+1)*(size+1)), [2*size+1,2*size+1]),
  ndarray(new Float32Array(4*(size+1)*(size+1)), [2*size+1,2*size+1]),
  ndarray(new Float32Array(4*(size+1)*(size+1)), [2*size+1,2*size+1])
]
for(var i=0; i<=2*size; ++i) {
  var theta = Math.PI * (i - size) / size
  for(var j=0; j<=2*size; ++j) {
    var phi = Math.PI * (j - size) / size
    coords[0].set(i, j, (50.0 + 20.0 * Math.cos(theta)) * Math.cos(phi))
    coords[1].set(i, j, (50.0 + 20.0 * Math.cos(theta)) * Math.sin(phi))
    coords[2].set(i, j, 20.0 * Math.sin(theta))
  }
}

var contourLevels = [[0], [0], [0]]

var surface = createSurface({
  gl:  scene.gl,
  levels: [ contourLevels, contourLevels, contourLevels ],
  lineWidth: 3,
  contourTint: 1,
  coords: coords,
  contourProject: [
    [true,false,false], 
    [false,true,false], 
    [false,false,true] ],
  showContour: true
})

scene.add(surface)