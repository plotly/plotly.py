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

var POINT_COUNT = 1e7

var aspect = gl.drawingBufferWidth / gl.drawingBufferHeight
var dataBox = [-10,-10/aspect,10,10/aspect]

function makeTicks(lo, hi, step, precision) {
  var result = []
  for(var i=lo, f=0; i<=hi; i+=step, f+=1) {

    var text = ''
    if(precision >= 0) {
      text = Math.round(lo + f*step) + ''
    } else {
      var len = Math.abs(precision)
      var num = (lo + f*step)
      var text = Math.abs(Math.round(num/step)) + ''
      while(text.length <= len) {
        text = '0' + text
      }
      text = text.substr(0, text.length - len) + '.' +
             text.substr(text.length - len)
      if(num < 0) {
        text = '-' + text
      }
    }

    result.push({
      x: i,
      text: text
    })
  }
  return result
}

var options = {
  gl:             gl,
  dataBox:        dataBox,
  title:          '10 million points',
  ticks:          [ makeTicks(-100,100,1,0), makeTicks(-100,100,1,0) ],
  labels:         ['x', 'y'],
  pixelRatio:     +window.devicePixelRatio,
  tickMarkWidth:  [2,2,2,2],
  tickMarkLength: [6,6,6,6],
  tickPad:        [20,20,20,20],
  borderLineEnable: [false, false, false, false]
}

var plot = createPlot(options)

var lastXTickMarks = [0,0,0,0], lastYTickMarks = [0,0,0,0]
var lastInputTime = Date.now()

function computeTickSpan(lo, hi, tickMarks) {
  var dist = hi - lo
  var digits = Math.log10(hi - lo) - 0.5
  var precision = Math.floor(digits)
  var step = Math.pow(10, precision)


  if(precision === tickMarks[0] &&
     tickMarks[2] <= lo &&
     hi <= tickMarks[3]) {
    return false
  }

  tickMarks[0] = precision
  tickMarks[1] = step
  tickMarks[2] = Math.floor(lo / (16*step)) * step * 16
  tickMarks[3] = Math.ceil(hi  / (16*step) + 1) * step * 16

  return true
}

function updateTicks() {
  var needXUpdate = computeTickSpan(dataBox[0], dataBox[2], lastXTickMarks)
  var needYUpdate = computeTickSpan(dataBox[1], dataBox[3], lastYTickMarks)

  if(needXUpdate || needYUpdate) {

    var precision = Math.min(lastXTickMarks[0], lastYTickMarks[0])
    var step      = Math.min(lastXTickMarks[1], lastYTickMarks[1])

    options.ticks[0] = makeTicks(lastXTickMarks[2], lastXTickMarks[3], step, precision)
    options.ticks[1] = makeTicks(lastYTickMarks[2], lastYTickMarks[3], step, precision)
    options.dataBox = dataBox

    plot.update(options)
  }
}

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
  color: [0.3,0.5,0.8,0.6]
})

var lastX = 0, lastY = 0
var boxStart = [0,0]
var boxEnd   = [0,0]
var boxEnabled = false
mouseChange(function(buttons, x, y, mods) {
  y = window.innerHeight - y
  x *= plot.pixelRatio
  y *= plot.pixelRatio

  if(buttons & 1) {
    if(mods.shift) {
      var dataX = (x - plot.viewBox[0]) / (plot.viewBox[2]-plot.viewBox[0]) * (dataBox[2] - dataBox[0]) + dataBox[0]
      var dataY = (y - plot.viewBox[1]) / (plot.viewBox[3]-plot.viewBox[1]) * (dataBox[3] - dataBox[1]) + dataBox[1]
      if(!boxEnabled) {
        boxStart[0] = dataX
        boxStart[1] = dataY
      }
      boxEnd[0] = dataX
      boxEnd[1] = dataY
      boxEnabled = true
      spikes.update()
    } else {
      var dx = (lastX - x) * (dataBox[2] - dataBox[0]) / (plot.viewBox[2]-plot.viewBox[0])
      var dy = (lastY - y) * (dataBox[3] - dataBox[1]) / (plot.viewBox[3] - plot.viewBox[1])

      dataBox[0] += dx
      dataBox[1] += dy
      dataBox[2] += dx
      dataBox[3] += dy

      plot.setDataBox(dataBox)
      spikes.update()
      lastInputTime = Date.now()
    }
  } else {
    var result = plot.pick(x/plot.pixelRatio, y/plot.pixelRatio)
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
      updateTicks()
    }
  }

  lastX = x
  lastY = y
})

mouseWheel(function(dx, dy, dz) {
  var scale = Math.exp(0.1 * dy / gl.drawingBufferHeight)

  var cx = (lastX - plot.viewBox[0]) / (plot.viewBox[2] - plot.viewBox[0]) * (dataBox[2] - dataBox[0]) + dataBox[0]
  var cy = (plot.viewBox[1] - lastY) / (plot.viewBox[3] - plot.viewBox[1]) * (dataBox[3] - dataBox[1]) + dataBox[3]

  dataBox[0] = (dataBox[0] - cx) * scale + cx
  dataBox[1] = (dataBox[1] - cy) * scale + cy
  dataBox[2] = (dataBox[2] - cx) * scale + cx
  dataBox[3] = (dataBox[3] - cy) * scale + cy

  plot.setDataBox(dataBox)

  lastInputTime = Date.now()

  return true
})

function render() {
  requestAnimationFrame(render)
  plot.draw()

  //if(Date.now() - lastInputTime > 500) {
    updateTicks()
  //}
}

render()
