var createStreamTubes = require('../streamtube');
var wind = require('./dataset-wind');
var meshgrid = require('./meshgrid');

var createCamera = require('3d-view-controls')
var perspective  = require('gl-mat4/perspective')
var createAxes   = require('gl-axes3d')
var createSpikes = require('gl-spikes3d')
var createSelect = require('gl-select-static')
var getBounds    = require('bound-points')
var mouseChange  = require('mouse-change')
var createMesh   = createStreamTubes.createTubeMesh;
var vec3 = require('gl-vec3');

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', require('canvas-fit')(canvas))
var gl = canvas.getContext('webgl')

var pvecs = [];
for (var i=0; i<wind.positions.length; i++) {
  pvecs.push({position: wind.positions[i], vector: wind.vectors[i]});
}
var cmpZYX = function(a, b) {
  if (a.position[2] !== b.position[2]) return a.position[2] - b.position[2];
  if (a.position[1] !== b.position[1]) return a.position[1] - b.position[1];
  return a.position[0] - b.position[0];
};
pvecs.sort(cmpZYX);

var positions = pvecs.map(function(p) { return p.position; });
var vectors = pvecs.map(function(p) { return p.vector; });

var windBounds = getBounds(positions);


var startingPositions = meshgrid.toPoints(meshgrid(80, [20, 10, 50], [0, 5, 15])); // {start: 20, step: 10, end: 50}, {start:0, step: 5, end: 15});

var mg = [[],[],[]]
var mgi =[{},{},{}];
positions.forEach(function(p) {
  var x = p[0];
  var y = p[1];
  var z = p[2];
  if (!mgi[0][x]) { mgi[0][x] = true; mg[0].push(x); }
  if (!mgi[1][y]) { mgi[1][y] = true; mg[1].push(y); }
  if (!mgi[2][z]) { mgi[2][z] = true; mg[2].push(z); }
})

var bounds = meshgrid.getBounds(mg);

var camera = createCamera(canvas, {
  eye:    [0,0,50],
  center: [0.5*(bounds[0][0]+bounds[1][0]),
           0.5*(bounds[0][1]+bounds[1][1]),
           0.5*(bounds[0][2]+bounds[1][2])],
  zoomMax: 500
})

var streams = createStreamTubes({
  startingPositions: startingPositions,
  maxLength: 3000,
  tubeSize: 1,
  //absoluteTubeSize: 0.1,
  meshgrid: mg,
  vectors: vectors,
  colormap: 'portland'
}, bounds);

var mesh = createMesh(gl, streams);
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