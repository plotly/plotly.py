var fit = require('canvas-fit')
var mouseWheel = require('mouse-wheel')
var mouseChange = require('mouse-change')
var gaussRandom = require('gauss-random')
var createLine = require('gl-line2d')
var createPlot = require('../plot')

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas, null, +window.devicePixelRatio), false)

var gl = canvas.getContext('webgl')

var POINT_COUNT = 10

var aspect = gl.drawingBufferWidth / gl.drawingBufferHeight
var dataBox = [-10,-10/aspect,10,10/aspect]

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
  dataBox:        dataBox,
  title:          '1 million points',
  ticks:          [ makeTicks(-20,20), makeTicks(-20,20) ],
  labels:         ['x', 'y'],
  pixelRatio:     +window.devicePixelRatio
}

var plot = createPlot(options)

var positions = new Float32Array(2 * POINT_COUNT)
for(var i=0; i<2*POINT_COUNT; i+=2) {
  positions[i]   = (i/POINT_COUNT)*20.0-20.0
  positions[i+1] = gaussRandom()
}

positions[11] = 1e10

var line = createLine(plot, {
  positions: positions,
  /*
  fill: [false, true, false, false],
  fillColor: [
    [0,0,1,0.5],
    [0,0,1,0.5],
    [0,0,1,0.5],
    [0,0,1,0.5]],
  */
  //positions: [-10,2,3,-3,2,10],
  width: 10
})

plot.addObject(line)

var lastX = 0, lastY = 0
mouseChange(function(buttons, x, y) {
  y = window.innerHeight - y
  x *= plot.pixelRatio
  y *= plot.pixelRatio

  if(buttons & 1) {
    var dx = (lastX - x) * (dataBox[2]-dataBox[0]) / (plot.viewBox[2]-plot.viewBox[0])
    var dy = (lastY - y) * (dataBox[3]-dataBox[1]) / (plot.viewBox[3]-plot.viewBox[1])

    dataBox[0] += dx
    dataBox[1] += dy
    dataBox[2] += dx
    dataBox[3] += dy

    plot.setDataBox(dataBox)
  } else {
    var result = plot.pick(x/plot.pixelRatio, y/plot.pixelRatio)
    /*
    if(result) {
      plot.setSpike(result.dataCoord[0], result.dataCoord[1])
    } else {
      plot.setSpike()
    }
    */
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

  return true
})

function render() {
  requestAnimationFrame(render)
  plot.draw()
}

render()
