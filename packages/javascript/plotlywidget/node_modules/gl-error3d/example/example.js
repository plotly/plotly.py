var shell = require("gl-now")({ clearColor: [0,0,0,0] })
var camera = require("game-shell-orbit-camera")(shell)
var createAxes = require("gl-axes3d")
var createErrorBars = require('../errorbars')
var mat4 = require("gl-matrix").mat4


var bounds = [[-5,-5,-5], [5,5,5]]

var errorbars, axes

shell.on("gl-init", function() {
  var gl = shell.gl

  camera.lookAt(bounds[1], [0,0,0], [0, 1, 0])

  axes = createAxes(gl, {
    bounds: bounds
  })

  errorbars = createErrorBars({
    gl: gl,
    position: [
      [0,0,0],
      [0,2,0],
      [-2,-3,0]
    ],

    error: [
      [[-0.5,-0.5,-0.1], [0.5,0.5,0.5]],
      [[0,0,0], [0.5,0.5,0.5]],
      [[-0.5,-0.5,0], [0,0,0]]
    ],

    color: [
      [1,0,0],
      [0,1,0],
      [0,0,1]
    ]
  })
})

shell.on("gl-render", function() {
  var gl = shell.gl
  gl.enable(gl.DEPTH_TEST)

  var cameraParameters = {
    view: camera.view(),
    projection: mat4.perspective(
        mat4.create(),
        Math.PI/4.0,
        shell.width/shell.height,
        0.1,
        1000.0)
  }

  axes.draw(cameraParameters)

  errorbars.draw(cameraParameters)
})
