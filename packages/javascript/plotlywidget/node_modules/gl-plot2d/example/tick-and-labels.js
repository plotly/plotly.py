var fit = require('canvas-fit')
var mouseWheel = require('mouse-wheel')
var mouseChange = require('mouse-change')
var gaussRandom = require('gauss-random')
var createScatter = require('gl-scatter2d')
var createSelectBox = require('gl-select-box')
var createSpikes = require('gl-spikes2d')
var createPlot = require('../plot')

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas, null, +window.devicePixelRatio), false)

var gl = canvas.getContext('webgl')

var POINT_COUNT = 1e4

var dataBox = [-10,-10,10,10]
var viewBox = [300,200,1100,600]

function makeTicks(lo, hi) {
  var result = []
  for(var i=lo; i<=hi; ++i) {
    result.push({
      x: i,
      text: i + ''
    })
  }
  return result
}

var options = {
  gl:             gl,
  pixelRatio:     +window.devicePixelRatio,

  dataBox:        dataBox,
  viewBox:        viewBox,

  title:          'a bunch of points, with style',
  titleEnable:    true,
  titleCenter:    [450,650],
  titleAngle:     0,
  titleColor:     [0.3,0.3,0.3,1],
  titleFont:      'sans-serif',
  titleSize:      22,

  borderColor:      [1,0,0,1],
  backgroundColor:  [0,1,0,1],
  borderLineEnable: [true,true,false,false],
  borderLineWidth:  [4,3,1,1],
  borderLineColor:  [[1,1,0,1], [0,1,1,1], [0,0,0,0], [0,0,0,0]],

  labels:         ['some independent variable','some dependent variable'],
  labelEnable:    [true,true,false,false],
  labelAngle:     [0,Math.PI/2,0,3.0*Math.PI/2],
  labelPad:       [30,30,0,0],
  labelSize:      [18,18],
  labelFont:      ['sans-serif', 'sans-serif'],
  labelColor:     [[1,1,0,1], [0,1,1,1], [0,0,0,0], [0,0,0,0]],

  ticks:          [ makeTicks(-20,20), makeTicks(-20,20) ],
  tickEnable:     [true,true,true,true],
  tickPad:        [15,20,0,0],
  tickAngle:      [0,0,0,0],
  tickColor:      [[1,1,0,1], [0,1,1,1], [0,0,0,0], [0,0,0,0]],
  tickMarkWidth:  [2,5,2,5],
  tickMarkLength: [4,4,4,4],
  tickMarkColor:  [[1,1,0,1], [0,1,1,1], [0,0,0,0], [0,0,0,0]],

  gridLineEnable: [true,true],
  gridLineColor:  [[0,0,0,0.5], [0,0,0,0.5]],
  gridLineWidth:  [1.5,1.5],

  zeroLineEnable: [false,true],
  zeroLineWidth:  [0,3],
  zeroLineColor:  [[1,1,0,0.5], [1,0,1,0.5]]
}

var plot = createPlot(options)

var selectBox = createSelectBox(plot, {
  innerFill: false,
  outerFill: true
})
selectBox.enabled = false

var spikes = createSpikes(plot)

var positions = new Float32Array(2 * POINT_COUNT)
for(var i=0; i<2*POINT_COUNT; ++i) {
  positions[i] = gaussRandom()
}

var scatter = createScatter(plot, {
  positions: positions,
  size: 7,
  color: [0.3,0.5,0.8,1]
})

var lastX = 0, lastY = 0
var boxStart = [0,0]
var boxEnd   = [0,0]
var boxEnabled = false

mouseChange(function(buttons, x, y, mods) {
  var pixelRatio = plot.pixelRatio;

  y = window.innerHeight - y
  x *= pixelRatio
  y *= pixelRatio

  if(buttons & 1) {
    if(mods.shift) {
      var dataX = (x - viewBox[0]) / (viewBox[2]-viewBox[0]) * (dataBox[2] - dataBox[0]) + dataBox[0]
      var dataY = (y - viewBox[1]) / (viewBox[3]-viewBox[1]) * (dataBox[3] - dataBox[1]) + dataBox[1]
      if(!boxEnabled) {
        boxStart[0] = dataX
        boxStart[1] = dataY
      }
      boxEnd[0] = dataX
      boxEnd[1] = dataY
      boxEnabled = true
      spikes.update()
    } else {
      var dx = (lastX - x) * (dataBox[2] - dataBox[0]) / (viewBox[2]-viewBox[0])
      var dy = (lastY - y) * (dataBox[3] - dataBox[1]) / (viewBox[3]-viewBox[1])

      dataBox[0] += dx
      dataBox[1] += dy
      dataBox[2] += dx
      dataBox[3] += dy

      plot.setDataBox(dataBox)
      spikes.update()
    }
  } else {
    var result = plot.pick(x/pixelRatio, y/pixelRatio)
    if(result) {
      spikes.update({center: result.dataCoord})
    } else {
      spikes.update()
    }
  }

  if(boxEnabled) {
    selectBox.enabled = true
    selectBox.selectBox = [
      Math.min(boxStart[0], boxEnd[0]),
      Math.min(boxStart[1], boxEnd[1]),
      Math.max(boxStart[0], boxEnd[0]),
      Math.max(boxStart[1], boxEnd[1])
    ]
    plot.setDirty()
    if(!((buttons&1) && mods.shift)) {
      selectBox.enabled = false
      dataBox = [
        Math.min(boxStart[0], boxEnd[0]),
        Math.min(boxStart[1], boxEnd[1]),
        Math.max(boxStart[0], boxEnd[0]),
        Math.max(boxStart[1], boxEnd[1])
      ]
      plot.setDataBox(dataBox)
      boxEnabled = false
    }
  }

  lastX = x
  lastY = y
})

mouseWheel(function(dx, dy, dz) {
  var scale = Math.exp(0.1 * dy / gl.drawingBufferHeight)

  var cx = (lastX - viewBox[0]) / (viewBox[2] - viewBox[0]) * (dataBox[2] - dataBox[0]) + dataBox[0]
  var cy = (viewBox[1] - lastY) / (viewBox[3] - viewBox[1]) * (dataBox[3] - dataBox[1]) + dataBox[3]

  dataBox[0] = (dataBox[0] - cx) * scale + cx
  dataBox[1] = (dataBox[1] - cy) * scale + cy
  dataBox[2] = (dataBox[2] - cx) * scale + cx
  dataBox[3] = (dataBox[3] - cy) * scale + cy

  plot.setDataBox(dataBox)

  return true
})

function render() {
  requestAnimationFrame(render)
  plot.draw()
}

render()
