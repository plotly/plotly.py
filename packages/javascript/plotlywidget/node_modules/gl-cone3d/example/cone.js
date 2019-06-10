var createCamera = require('3d-view-controls')
var getBounds    = require('bound-points')
var perspective  = require('gl-mat4/perspective')
var createAxes   = require('gl-axes3d')
var createSpikes = require('gl-spikes3d')
var createSelect = require('gl-select-static')
var getBounds    = require('bound-points')
var mouseChange  = require('mouse-change')
var createConePlot = require('../cone')
var createShader = require('gl-shader')
var mat4 = require('gl-mat4')

var createMesh = createConePlot.createConeMesh;

var shaders = require('../lib/shaders')

var bounds = []

var wind = require('./dataset-wind')

var conePlot = createConePlot({
  positions: wind.positions,
  vectors: wind.vectors,
  colormap: 'portland'
}, bounds)

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', require('canvas-fit')(canvas))
var gl = canvas.getContext('webgl')

var camera = createCamera(canvas, {
  eye:    bounds[0],
  center: [0.5*(bounds[0][0]+bounds[1][0]),
           0.5*(bounds[0][1]+bounds[1][1]),
           0.5*(bounds[0][2]+bounds[1][2])],
  zoomMax: 500,
  mode: 'turntable'
})

conePlot.colormap = 'portland'

var mesh = createMesh(gl, conePlot)

var select = createSelect(gl, [canvas.width, canvas.height])
var tickSpacing = 5;
var ticks = bounds[0].map(function(v,i) {
  var arr = [];
  var firstTick = Math.ceil(bounds[0][i] / tickSpacing) * tickSpacing;
  var lastTick = Math.floor(bounds[1][i] / tickSpacing) * tickSpacing;
  for (var tick = firstTick; tick <= lastTick; tick += tickSpacing) {
    if (tick === -0) tick = 0;
    arr.push({x: tick, text: tick.toString()});
  }
  return arr;
});
var axes = createAxes(gl, { bounds: bounds, ticks: ticks })
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

var modelMat = mat4.create();

var vectorScale = mesh.vectorScale;

function render() {
  requestAnimationFrame(render)

  gl.enable(gl.DEPTH_TEST)

  mat4.identity(modelMat);
  mat4.translate(modelMat, modelMat, [100, 40, 8]);
  mat4.scale(modelMat, modelMat, [2*Math.cos(Date.now()/4000), 2*Math.sin(Date.now()/5000), 4*Math.sin(Date.now()/7400)])
  mat4.rotate(modelMat, modelMat, Date.now()/10000, [Math.cos(Date.now()/24000), Math.sin(Date.now()/15000), Math.cos(Date.now()/19000)])
  mat4.translate(modelMat, modelMat, [-100, -40, -8]);

  var needsUpdate = camera.tick()
  var cameraParams = {
    projection: perspective([], Math.PI/4, canvas.width/canvas.height, 1, 300),
    view: camera.matrix,
    model: modelMat
  }

  // mesh.vectorScale = vectorScale * Math.abs(Math.sin(Date.now()/500))*4;

  if(true || needsUpdate || spikeChanged) {
    gl.bindFramebuffer(gl.FRAMEBUFFER, null)
    gl.viewport(0, 0, canvas.width, canvas.height)
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)
    axes.draw(cameraParams)
    spikes.draw(cameraParams)
    mesh.draw(cameraParams)
    spikeChanged = false
  }

  if(true || needsUpdate) {
    select.shape = [canvas.width, canvas.height]
    select.begin()
    mesh.drawPick(cameraParams)
    select.end()
  }
}
render()
