"use strict"

var shell = require("gl-now")({tickRate:2})
var camera = require("game-shell-orbit-camera")(shell)
var mat4 = require("gl-matrix").mat4
var createSimplicialComplex = require("gl-simplicial-complex")
var sc = require("simplicial-complex")
var createAxes = require("gl-axes")
var dt = require("../triangulate")

camera.lookAt(
  [2.5, 2.5, 2.5],
  [0,0,0],
  [0,1,0])

var mesh, axes

var points = new Array(100)
for(var i=0; i<100; ++i) {
  var p = new Array(3)
  for(var j=0; j<3; ++j) {
    p[j] = 2.0 * Math.random() - 1.0
  }
  points[i] = p
}
var cells = dt(points)

shell.on("gl-init", function() {
  var gl = shell.gl
  gl.enable(gl.DEPTH_TEST)
  mesh = createSimplicialComplex(gl, {
    cells: sc.skeleton(cells, 1),
    positions: points,
    pointSize: 5,
    meshColor: [0,0,0]
  })

  axes = createAxes(shell.gl, {
    bounds: [[-1,-1,-1],[1,1,1]], 
    tickSpacing: [0.1,0.1,0.1],
    gridColor:[0.5,0.5,0.5]
  })
})

shell.on("tick", function() {
  if(shell.press("space")) {
    updateTriangulation()
  }
})

shell.on("gl-render", function() {
  var cameraParameters = {
    view: camera.view(),
    projection: mat4.perspective(mat4.create(),
          Math.PI/4.0,
          shell.width/shell.height,
          0.1,
          1000.0)
  }
  mesh.draw(cameraParameters)
  axes.draw(cameraParameters)
})