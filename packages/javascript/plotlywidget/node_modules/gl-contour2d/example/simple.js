var fit = require('canvas-fit')
var mouseWheel = require('mouse-wheel')
var mouseChange = require('mouse-change')
var createContour = require('../contour')
var createSelectBox = require('gl-select-box')
var createSpikes = require('gl-spikes2d')
var createPlot = require('gl-plot2d')

var canvas = document.createElement('canvas')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas, null, +window.devicePixelRatio), false) // not working well at the moment

var gl = canvas.getContext('webgl')

var aspect = gl.drawingBufferWidth / gl.drawingBufferHeight

// visible data box
var initialVisibleTickItemRangeX = [-10, 10] // initially show at most 10 ticks to the left and 10 to the right
var initialVisibleTickItemRangeY = [-6, 6] // initially show at most 6 ticks up and 6 ticks down
var tickItemRange = aspect > 1 ? initialVisibleTickItemRangeX : initialVisibleTickItemRangeY // make sure it fits
console.log(tickItemRange)
var initialDataBox = [
  tickItemRange[0], tickItemRange[0] / aspect,
  tickItemRange[1], tickItemRange[1] / aspect
]
var dataBox = initialDataBox.slice() // will be mutated by mouse interactions

// left closed, right open range function
function range(start, end, specifiedIncrement) {
  var increment = specifiedIncrement || 1
  var result = []
  for(var n = start; n < end; n += increment)
    result.push(n)
  return result
}

function makeTick(i) {
  return {
    x: i,
    text: i.toString()
  }
}

var options = {
  gl:             gl,
  dataBox:        dataBox,
  title:          '100 million points',
  ticks:          [range(-20, 20).map(makeTick), range(-20, 20).map(makeTick)],
  labels:         ['x', 'y'],
  pixelRatio:     +window.devicePixelRatio,
  tickMarkWidth:  [2, 2, 2, 2],
  tickMarkLength: [6, 6, 6, 6]
}

var plot = createPlot(options)

var selectBox = createSelectBox(plot, {
  innerFill: false,
  outerFill: true
})
selectBox.enabled = false

var spikes = createSpikes(plot)

// making and populating the data grid

var xRange = range(-6, 7)
var yRange = range(-5, 6)

var z = new Array(xRange.length * yRange.length)

for(var i = 0; i < xRange.length; i++)
  for(var j = 0; j < yRange.length; j++)
    z[i * yRange.length + j] = Math.pow(xRange[i], 2) / (4 * 4) + Math.pow(yRange[j], 2) / (3 * 3)


// creating the plot

console.time('createContour')

var heatmap = createContour(plot, {
  x:           xRange,
  y:           yRange,
  z:           z,
  shape:       [xRange.length, yRange.length], // it doesn't calculate shape out even if x and y optionals are passed
  levels:      [0.1, 0.5, 1, 1.5],
  lineWidth:   4,
  levelColors: [
    1, 0, 0, 1,
    0, 1, 0, 1,
    0, 0, 1, 1,
    0, 0, 0, 1
  ],
  fillColors:  [
    1, 0, 0, .3,
    0, 1, 0, .3,
    0, 0, 1, .3,
    0, 0, 0, .5,
    0, 0, 0, .2
  ]
})

console.timeEnd('createContour')

// adding interactions (optional)

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

  return true
})


function render() {
  requestAnimationFrame(render)
  plot.draw()
}

render()
