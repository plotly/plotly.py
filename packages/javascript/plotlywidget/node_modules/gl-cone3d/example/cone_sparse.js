var createCamera = require('3d-view-controls')
var getBounds    = require('bound-points')
var perspective  = require('gl-mat4/perspective')
var createAxes   = require('gl-axes3d')
var createSpikes = require('gl-spikes3d')
var createSelect = require('gl-select-static')
var getBounds    = require('bound-points')
var mouseChange  = require('mouse-change')
var createConePlot = require('../cone')
var createMesh = createConePlot.createConeMesh;

var bounds = []

var wind = require('./dataset-wind')


var meshgrid = [
  [0, 15, 30, 35, 40, 55, 70],
  [0, 15, 30, 35, 40, 45, 50],
  [0, 1, 2, 3, 30, 31, 50]
];

var getPoint = function(x,y,z) {
  return [Math.cos(y) * Math.sin(z), Math.sin(x), Math.cos(x)*Math.cos(z)];
};

var data = [];
for (var z=0; z<meshgrid[2].length; z++) {
  for (var y=0; y<meshgrid[1].length; y++) {
    for (var x=0; x<meshgrid[0].length; x++) {
      data[z*meshgrid[1].length*meshgrid[0].length + y*meshgrid[0].length + x] = getPoint(meshgrid[0][x], meshgrid[1][y], meshgrid[2][z]);
    }
  }
}

var positions = [];
for (var z=0; z<=50; z+=5) {
  for (var y=0; y<=50; y+=5) {
    for (var x=0; x<=70; x+=7) {
      positions.push([x,y,z]);
    }
  }
}

var conePlot = createConePlot({
  positions: positions,
  meshgrid: meshgrid,
  vectors: data,
  coneSize: 1,
  colormap: 'portland'
}, bounds)

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', require('canvas-fit')(canvas))
var gl = canvas.getContext('webgl')

var camera = createCamera(canvas, {
  eye:    [100,100,100],
  center: [0.5*(bounds[0][0]+bounds[1][0]),
           0.5*(bounds[0][1]+bounds[1][1]),
           0.5*(bounds[0][2]+bounds[1][2])],
  zoomMax: 500,
  mode: 'turntable'
})


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

function render() {
  requestAnimationFrame(render)

  gl.enable(gl.DEPTH_TEST)

  var needsUpdate = camera.tick()
  var cameraParams = {
    projection: perspective([], Math.PI/4, canvas.width/canvas.height, 0.1, 300),
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
