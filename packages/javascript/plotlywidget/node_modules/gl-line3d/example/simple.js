"use strict"

var shell = require("gl-now")({ clearColor: [0,0,0,0] })
var camera = require("game-shell-orbit-camera")(shell)
var createSelect = require("gl-select")
var createAxes = require("gl-axes")
var createSpikes = require("gl-spikes")
var createLines = require("../lines")

var mat4 = require("gl-matrix").mat4

//State variables
var  axes, lines, select, spikes

var pickPoint = null

//Set up camera
camera.lookAt(
  [10, 0, 0], 
  [ 0, 0, 0], 
  [ 0, 1, 0])

shell.on("gl-init", function() {
  var gl = shell.gl

  //Create the line plot
  var polyline = []
  for(var i=0; i<100; ++i) {
    var theta = (i / 100.0) * Math.PI
    polyline.push([
        Math.cos(3*theta),
        Math.sin(3*theta),
        (i/50) - 1.0
      ])
  }

  lines = createLines({
    gl: gl,
    position: polyline,
    color: [1,0,0],
    dashes: [0.5,0.5],
    dashScale: 100
  })

  //Create axes object
  axes = createAxes(gl, {
    bounds: [[-1,-1,-1],[ 1, 1, 1]]
  })

  //Create selection buffer
  select = createSelect(gl, [shell.width, shell.height])

  //Create spike ball
  spikes = createSpikes(gl, {bounds: [[-1,-1,-1], [1,1,1]]})
})

function drawPick(cameraParameters) {
  select.shape = [shell.width, shell.height]
  select.begin(shell.mouse[0], shell.mouse[1], 30)
  lines.drawPick(cameraParameters)
  var selected = select.end()
  pickPoint = lines.pick(selected)
}


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

  drawPick(cameraParameters)

  axes.draw(cameraParameters)
  lines.draw(cameraParameters)

  if(pickPoint) {
    spikes.position = pickPoint.position
    spikes.draw(cameraParameters)
  }
})