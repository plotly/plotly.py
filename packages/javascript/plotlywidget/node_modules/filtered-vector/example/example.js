'use strict'

var now = require('right-now')
var filterVector = require('../fvec')

var smoothPosition = filterVector([256, 256])
smoothPosition.bounds = [[0,0], [512,512]]


var canvas = document.createElement('canvas')
canvas.width = 512
canvas.height = 512
document.body.appendChild(canvas)

var context = canvas.getContext('2d')

canvas.addEventListener('mousemove', function(ev) {
  smoothPosition.push(now(), ev.x, ev.y)
})

function paint() {
  requestAnimationFrame(paint)
  var t = now() - 30
  smoothPosition.idle(t)
  context.fillStyle = 'rgba(0,0,0,1)'
  context.fillRect(0,0,512,512)
  
  context.strokeStyle = '#0f0'
  context.lineWidth = 1
  context.beginPath()
  var x = smoothPosition.curve(t)
  context.moveTo(x[0], x[1])
  for(var i=0; i<2000; ++i) {
    var y = smoothPosition.curve(Math.floor(t - i))
    context.lineTo(y[0], y[1])
  }
  context.stroke()
}
paint()