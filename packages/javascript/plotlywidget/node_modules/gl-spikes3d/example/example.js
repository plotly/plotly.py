"use strict"

var shell = require("gl-now")({ clearColor: [0,0,0,0], tickRate: 5 })
var camera = require("game-shell-orbit-camera")(shell)
var mat4 = require("gl-matrix").mat4
var createAxes = require("gl-axes3d")
var createSpikes = require("../spikes")

//Bounds on function to plot
var bounds = [[-1,-1,-1], [1,1,1]]

//camera.lookAt([-15,20,-15], [0,0,0], [0, 1, 0])
camera.lookAt([2, 2, 2], [0,0,0], [0,1,0])

//State variables
var axes, spikes

shell.on("gl-init", function() {
  var gl = shell.gl

  axes = createAxes(gl, {
    bounds: bounds,
    tickSpacing: [0.1,0.1,0.1],
    textSize: 0.05
  })

  spikes = createSpikes(gl, {
    bounds:   bounds,
    colors:   [[1,0,0,1], [0,1,0,1], [0,0,1,1]],
    position: [0,0,0]
  })
})

shell.on("gl-render", function() {
  var gl = shell.gl
  gl.enable(gl.DEPTH_TEST)

  //Compute camera parameters
  var cameraParameters = {
    view: camera.view(),
    projection: mat4.perspective(
        mat4.create(),
        Math.PI/4.0,
        shell.width/shell.height,
        0.1,
        1000.0)
  }


  var t = 0.001*Date.now()
  spikes.position = [Math.cos(t), Math.sin(t), Math.cos(2*t+0.1)]

  //Draw objects
  axes.draw(cameraParameters)
  spikes.draw(cameraParameters)
})
