var createCamera = require('3d-view-controls')
var getBounds    = require('bound-points')
var bunny        = require('bunny')
var perspective  = require('gl-mat4/perspective')
var createAxes   = require('gl-axes3d')
var createSpikes = require('gl-spikes3d')
var createSelect = require('gl-select-static')
var getBounds    = require('bound-points')
var mouseChange  = require('mouse-change')
var createMesh   = require('../mesh')

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', require('canvas-fit')(canvas))
var gl = canvas.getContext('webgl')

var bounds = getBounds(bunny.positions)
var camera = createCamera(canvas, {
  eye:    [0,0,50],
  center: [-0.5*(bounds[0][0]+bounds[1][0]),
           -0.5*(bounds[0][1]+bounds[1][1]),
           -0.5*(bounds[0][2]+bounds[1][2])],
  zoomMax: 500
})
var mesh = createMesh(gl, {
  cells:      bunny.cells,
  positions:  bunny.positions,
  meshColor:  [1, 0, 0]
})
var select = createSelect(gl, [canvas.width, canvas.height])
var axes = createAxes(gl, { bounds: bounds })
var spikes = createSpikes(gl, {
  bounds: bounds
})
var spikeChanged = false

mouseChange(canvas, function(buttons, x, y) {
  var pickData = select.query(x, canvas.height - y, 10)
  var pickResult = mesh.pick(pickData)
  if(pickResult) {
    spikes.update({
      position: pickResult.position,
      enabled: [true, true, true]
    })
    spikeChanged = true
  } else {
    spikeChanged = spikes.enabled[0]
    spikes.update({
      enabled: [false, false, false]
    })
  }
})

function render() {
  requestAnimationFrame(render)

  gl.enable(gl.DEPTH_TEST)

  var needsUpdate = camera.tick()
  var cameraParams = {
    projection: perspective([], Math.PI/4, canvas.width/canvas.height, 0.01, 1000),
    view: camera.matrix
  }

  if(needsUpdate || spikeChanged) {
    gl.bindFramebuffer(gl.FRAMEBUFFER, null)
    gl.viewport(0, 0, canvas.width, canvas.height)
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)
    axes.draw(cameraParams)
    spikes.draw(cameraParams)
    mesh.draw(cameraParams)
    spikeChanged = false
  }

  if(needsUpdate) {
    select.shape = [canvas.width, canvas.height]
    select.begin()
    mesh.drawPick(cameraParams)
    select.end()
  }
}
render()
