'use strict'

var mouseChange = require('mouse-change')
var alphaShape = require('./alpha')
var fit = require('canvas-fit')

var alphaContainer = document.createElement('div')
alphaContainer.style.top = '0'
alphaContainer.style.left = '0'
alphaContainer.style.position = 'absolute'
alphaContainer.style['z-index'] = 10
alphaContainer.style.color = '#fff'

var alphaLabel = document.createElement('p')
alphaContainer.appendChild(alphaLabel)

var alphaSlider = document.createElement('input')
alphaSlider.type = 'range'
alphaSlider.minValue = 0
alphaSlider.maxValue = 100
alphaSlider.value = 1.0
alphaContainer.appendChild(alphaSlider)

document.body.appendChild(alphaContainer)

var canvas = document.body.appendChild(document.createElement('canvas'))
window.addEventListener('resize', fit(canvas))
var context = canvas.getContext('2d')

var points = []

var pbuttons = 0
mouseChange(function(buttons, x, y) {
  if(buttons&1 && (~pbuttons)&1) {
    points.push([x/canvas.width, y/canvas.height])
  }
  pbuttons = buttons
})

function render() {
  requestAnimationFrame(render)

  alphaLabel.innerHTML = 'alpha = ' + alphaSlider.value

  var alphaHull = alphaShape(+alphaSlider.value, points)
  var w = canvas.width
  var h = canvas.height

  context.fillStyle = '#000'
  context.fillRect(0, 0, canvas.width, canvas.height)

  context.strokeStyle = '#f00'
  for(var i=0; i<alphaHull.length; ++i) {
    var cell = alphaHull[i]
    for(var j=0; j<cell.length; ++j) {
      var p = points[cell[j]]
      var q = points[cell [(j+1)%cell.length]]
      context.beginPath()
      context.moveTo(w * p[0], h * p[1])
      context.lineTo(w * q[0], h * q[1])
      context.stroke()
    }
  }

  context.fillStyle = '#0f0'
  for(var i=0; i<points.length; ++i) {
    var p = points[i]
    context.fillRect(p[0]*w, p[1]*h, 5, 5)
  }
}

render()