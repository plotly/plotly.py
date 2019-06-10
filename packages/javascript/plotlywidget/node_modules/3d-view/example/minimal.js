'use strict'

var now            = require('right-now')
var bunny          = require('bunny')
var perspective    = require('gl-mat4/perspective')
var fit            = require('canvas-fit')
var createContext  = require('gl-context')
var createAxes     = require('gl-axes')
var createMesh     = require('gl-simplicial-complex')
var createCamera   = require('../view')

//Set up WebGL
var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas), false)
var gl = createContext(canvas, {}, render)

//Create objects for rendering
var bounds = [[-10,-10,-10], [10,10,10]]
var mesh = createMesh(gl, {
    cells: bunny.cells,
    positions: bunny.positions,
    colormap: 'jet'
  })
var axes = createAxes(gl, {
    bounds: bounds,
    tickSpacing: [1,1,1],
    textSize: 0.05
  })

//Set up camera
var projectionMatrix = new Array(16)
var camera = createCamera({
  center:  [
    0.5*(bounds[0][0]+bounds[1][0]),
    0.5*(bounds[0][1]+bounds[1][1]),
    0.5*(bounds[0][2]+bounds[1][2]) ],
  eye: [0, 0, bounds[1][2]],
  distanceLimits: [1, 1000]
})

//Create mode drop down
var modeSelect = document.createElement('select')
camera.modes.forEach(function(mode) {
  modeSelect.add(new Option(mode, mode))
})
modeSelect.style.position = 'absolute'
modeSelect.style.left = '10px'
modeSelect.style.top = '10px'
modeSelect.style['z-index'] = 10
document.body.appendChild(modeSelect)


//Hook event listeners
var lastX = 0, lastY = 0

document.oncontextmenu = function(e) { 
  e.preventDefault()
  e.stopPropagation()
  return false 
}

modeSelect.addEventListener('change', function(ev) {
  camera.setMode(modeSelect.value)
})

canvas.addEventListener('mousemove', function(ev) {
  var dx =  (ev.clientX - lastX) / gl.drawingBufferWidth
  var dy = -(ev.clientY - lastY) / gl.drawingBufferHeight
  if(ev.which === 1) {
    if(ev.shiftKey) {
      //zoom
      camera.rotate(now(), 0, 0, dx)
    } else {
      //rotate
      camera.rotate(now(), dx, dy)
    }
  } else if(ev.which === 3) {
    //pan
    camera.pan(now(), dx, dy)
  }
  lastX = ev.clientX
  lastY = ev.clientY
})

canvas.addEventListener('wheel', function(e) {
  camera.pan(now(), 0, 0, e.deltaY)
})

//Redraw frame
function render() {

  //Update camera parameters
  var t = now()
  camera.idle(t - 20)
  camera.flush(t - 100)

  //Compute parameters
  camera.recalcMatrix(t - 25)
  var cameraParams = {
    view: camera.computedMatrix,
    projection: perspective(
      [],
      Math.PI/4.0,
      gl.drawingBufferWidth/gl.drawingBufferHeight,
      0.1,
      1000.0)
  }

  //Draw everything
  gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight)
  gl.enable(gl.DEPTH_TEST)
  axes.draw(cameraParams)
  mesh.draw(cameraParams)
}