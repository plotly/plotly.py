var raf = require('raf')
var fit = require('./')

var canvas = document.createElement('canvas')
var ctx = canvas.getContext('2d')
var resize = fit(canvas)

window.addEventListener('resize', resize, false)
document.body.appendChild(canvas)

raf(canvas).on('data', function() {
  ctx.fillStyle = '#f00'
  ctx.fillRect(0, 0, canvas.width, canvas.height)
})
