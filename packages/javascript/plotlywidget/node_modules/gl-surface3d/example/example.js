"use strict"

var shell = require("gl-now")({ clearColor: [0,0,0,0] })
var camera = require("game-shell-orbit-camera")(shell)
var createSurface = require("../surface.js")
var createAxes = require("gl-axes3d")
var createSpikes = require("gl-spikes3d")
var ndarray = require("ndarray")
var fill = require("ndarray-fill")
var diric = require("dirichlet")
var glm = require("gl-matrix")
var createSelect = require("gl-select-static")
var mat4 = glm.mat4

var surface, spikes, axes, select, target = null

var size = 128

shell.on("gl-init", function() {
  var gl = shell.gl
  gl.enable(gl.DEPTH_TEST)

  //Set up camera
  camera.lookAt(
    [-size, -size, 1.5*size],      //Eye position
    [0,0,0], //Eye target
    [0, 0, 1])      //Up direction

  //Create field
  var field = ndarray(new Float32Array(4*(size+1)*(size+1)), [2*size+1,2*size+1])

  /*
  fill(field, function(x,y) {
    return 0.5 * size * diric(10, 5.0*(x-size)/size) * diric(10, 5.0*(y-size)/size)
  })
  */

  var coords = [
    ndarray(new Float32Array(4*(size+1)*(size+1)), [2*size+1,2*size+1]),
    ndarray(new Float32Array(4*(size+1)*(size+1)), [2*size+1,2*size+1]),
    field
  ]

  var x = coords[0]
  var y = coords[1]
  var z = field

  for(var i=0; i<=2*size; ++i) {
    var theta = Math.PI * (i - size) / size
    for(var j=0; j<=2*size; ++j) {
      var phi = Math.PI * (j - size) / size

      x.set(i, j, (50.0 + 20.0 * Math.cos(theta)) * Math.cos(phi))
      y.set(i, j, (50.0 + 20.0 * Math.cos(theta)) * Math.sin(phi))
      z.set(i, j, 20.0 * Math.sin(theta))
    }
  }


  var contourLevels = []
  for(var i=-5; i<=5; ++i) {
    contourLevels.push(20*(i+0.3)/6.0)
  }


  surface = createSurface({
    gl: gl,
    field: field,
    //levels: [contourLevels,contourLevels,contourLevels],
    lineWidth: 3,
    contourTint: 1,
    coords: coords,
    contourProject: [[true,false,false], [true,false,false], [true,false,false]],
    vertexColor: false
    //surfaceProject: [true, true, true]
    //showContour: false
    //showSurface: false
  })

  axes = createAxes(gl, {
    bounds: [[-96,-96,-32],[96,96,32]],
    tickSpacing: [0.125*size, 0.125*size, 0.125*size],
    textSize: size / 32.0,
    gridColor: [0.8,0.8,0.8],
    tickPad: 8,
    labelPad: 12
  })

  spikes = createSpikes(gl, {
    bounds: axes.bounds
  })

  select = createSelect(gl, [shell.width, shell.height])
})

function drawPick(cameraParams) {
  select.shape = [shell.width, shell.height]
  select.begin(shell.mouse[0], shell.mouse[1], 30)
  surface.drawPick(cameraParams)
  target = surface.pick(select.end())
}

shell.on("gl-render", function() {
  var cameraParams = {
    view: camera.view(),
    projection:  mat4.perspective(
      new Array(16), Math.PI/4.0, shell.width/shell.height, 0.1, 10000.0)
  }

  drawPick(cameraParams)

  surface.axesBounds = axes.bounds
  surface.draw(cameraParams)
  axes.draw(cameraParams)

  if(target) {
    spikes.position = target.position
    spikes.draw(cameraParams)
    surface.highlightLevel = target.level
    surface.dynamic(target.position)
  } else {
    surface.highlightLevel = -1
  }
})
