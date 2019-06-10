var shell = require("gl-now")({tickRate: 2})
var camera = require("game-shell-orbit-camera")(shell)
var createPoints = require("../pointcloud")
var createAxes = require("gl-axes")
var createSelect = require("gl-select")
var createSpikes = require("gl-spikes")
var mat4 = require("gl-matrix").mat4
 
var points, axes, select, spikes, target=null

var SCALE = 1

camera.lookAt(
  [2,2,2],
  [0.5,0.5,0.5],
  [0,1,0])
 
shell.on("gl-init", function() {
  var gl = shell.gl

  var initialData = {
    gl: gl,
    position: [ [0.9, 0, -0.8], [0, 0.6, -0.75], [0, 0, 0.4], [0.8,0.92,-0.4], [0.33,0,0.56], [0,0.11,0.8] ],
    glyph: [  "▼", "★", "■", "◆", "✚", "✖" ],
    color: [ [0,1,0], [0,0,1], [1,1,0], [1,0,1], [0,1,1], [0,0,0] ],
    size: 30,
    orthographic: true,
    lineColor: [0,0,0],
    lineWidth: 1,
    project: [true, true, true]
  }

  for(var i=0; i<100; ++i) {
    var theta = i / 100.0 * 2.0 * Math.PI
    var x = Math.cos(theta)
    var y = Math.sin(theta)
    initialData.position.push([ SCALE*x, SCALE*y, 0 ])
    initialData.glyph.push("●")
    initialData.color.push([1, 0, 0])
  }

  points = createPoints(initialData)

  axes = createAxes(gl, {
    bounds: [[-SCALE,-SCALE, -SCALE], [SCALE, SCALE, SCALE]],
    tickSpacing: [0.25*SCALE, 0.25*SCALE, 0.25*SCALE],
    textSize: 0.1,
    tickPad: 0.2,
    labelPad: 0.2,
    gridColor: [0.5,0.5,0.5]

  })

  points.axes = axes

  spikes = createSpikes(gl, {
    bounds: axes.bounds,
    colors: [[1,0,0,1], [0,1,0,1], [0,0,1,1]]
  })
  select = createSelect(gl, [shell.width, shell.height])
})


function updatePick(cameraParams) {
  //Update size of select buffer
  select.shape = [shell.width, shell.height]

  //Begin pass, look for points within 30 pixels of mouse
  select.begin(shell.mouse[0], shell.mouse[1], 30)

  //Draw point cloud pick buffer
  points.drawPick(cameraParams)

  //End pass, retrieve selection information
  var selected = select.end()

  //Look up point id in scatter plot, mark as highlighted
  target = points.pick(selected)
  if(target) {
    points.highlight(target.index, [Math.random(),Math.random(),Math.random()])
    spikes.position = target.position
    spikes.enabled = [true,true,true]
  } else {
    points.highlight()
    spikes.enabled = [false,false,false]
  }
}

 
shell.on("gl-render", function() {
  var gl = shell.gl

  var cameraParams = {
    view: camera.view(),
    projection: mat4.perspective(
        mat4.create(),
        Math.PI/4.0,
        shell.width/shell.height,
        0.1,
        1000.0),
    model: [1/SCALE, 0, 0, 0,
            0, 3/SCALE, 0, 0,
            0, 0, 1/SCALE, 0,
            0, 0, 0, 1]
  }

  gl.enable(gl.DEPTH_TEST)

  //Update point picking data
  updatePick(cameraParams)

  //Update camera
  points.axesProject = [true,true,true]
  points.axesBounds = axes.bounds
  points.clipBounds = axes.bounds
  points.draw(cameraParams)
  axes.draw(cameraParams)
  spikes.draw(cameraParams)
})