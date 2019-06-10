'use strict'

var orient = require('robust-orientation')
var vec2 = require('vec2')
var segment2 = require('segment2')
var mouseChange = require('mouse-change')
var segCrosses = require('robust-segment-intersect')
var fit = require('canvas-fit')
var cleanupPSLG = require('../clean-pslg')

//Create canvas and context
var canvas = document.createElement('canvas')
var context = canvas.getContext('2d')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas), false)

var optionDiv = document.createElement('div')
optionDiv.style.position = 'absolute'
optionDiv.style.left = '5px'
optionDiv.style.top = '5px'
optionDiv.style['z-index'] = '10'
document.body.appendChild(optionDiv)

var points      = []
var edges       = []
var cleanPoints = []
var cleanEdges  = []

function dataChanged() {
  cleanPoints = points.map(function(p) { return [p[0], p[1]] })
  cleanEdges = edges.map(function(e) { return [e[0], e[1]] })
  cleanupPSLG(cleanPoints, cleanEdges)
}

for(var i=0; i<10; ++i) {
  var x = Math.random() * 0.8 - 0.4
  var y = Math.random() * 0.8 - 0.4
  points.push([0.5+x,0.5+y], [0.5-x,0.5-y])
  edges.push([2*i, 2*i+1])
}

dataChanged()

var resetButton = document.createElement('input')
resetButton.type = 'button'
resetButton.value = 'reset'
resetButton.addEventListener('click', function() {
  points.length = edges.length = 0
  dataChanged()
})
var resetP = document.createElement('p')
resetP.appendChild(resetButton)
optionDiv.appendChild(resetP)

var description = document.createElement('p')
description.innerHTML = 'click to add/remove points<br>drag to add edges<br><a href="https://github.com/mikolalysenko/clean-pslg">Project page</a>'
optionDiv.appendChild(description)

function edgeDistance(a, b, c) {
  var p = vec2(c[0], c[1])
  return segment2(vec2(a[0], a[1]), vec2(b[0], b[1])).closestPointTo(p).distance(p)
}

function isValidEdge(a, b) {
  return true
}

var lastButtons = 0,
  highlightPoint = -1,
  startPoint = -1,
  highlightEdge = -1,
  activeEdge = null
mouseChange(canvas, function(buttons, x, y) {
  var s = Math.min(canvas.width, canvas.height)
  var lx = (x - canvas.width/2) / s + 0.5
  var ly = (y - canvas.height/2) / s + 0.5
  var closestDist = 0.0125
  highlightPoint = -1
  highlightEdge = -1
  for(var i=0; i<points.length; ++i) {
    var p = points[i]
    var d2 = Math.sqrt(Math.pow(lx - p[0], 2) + Math.pow(ly - p[1], 2))
    if(d2 < closestDist) {
      highlightPoint = i
      closestDist = d2
    }
  }

  if(highlightPoint < 0) {
    for(var i=0; i<edges.length; ++i) {
      var e = edges[i]
      if(e[0] < 0 || e[1] < 0) {
        continue
      }
      var d2 = edgeDistance(points[e[0]], points[e[1]], [lx, ly])
      if(d2 < closestDist) {
        highlightEdge = i
        closestDist = d2
      }
    }
  }

  if(!lastButtons && !!buttons) {
    if(highlightEdge >= 0) {
      edges.splice(highlightEdge, 1)
      dataChanged()
      highlightEdge = -1
    } else if(highlightPoint < 0) {
      points.push([lx, ly])
      dataChanged()
    } else {
      startPoint = highlightPoint
      activeEdge = [ points[highlightPoint], [lx, ly] ]
    }
  } else if(!!lastButtons && !buttons) {
    if(startPoint >= 0) {
      if(highlightPoint === startPoint) {
        points.splice(highlightPoint, 1)
        var nedges = []
discard_edge:
        for(var i=0; i<edges.length; ++i) {
          var e = edges[i]
          for(var j=0; j<2; ++j) {
            if(e[j] > highlightPoint) {
              e[j] -= 1
            } else if(e[j] === highlightPoint) {
              continue discard_edge
            }
          }
          nedges.push(e)
        }
        edges = nedges
        highlightPoint = -1
        dataChanged()
      } else if(highlightPoint >= 0) {
        if(isValidEdge(points[startPoint], points[highlightPoint])) {
          edges.push([startPoint, highlightPoint])
          dataChanged()
        }
      }
      startPoint = -1
      activeEdge = null
    }
  } else if(!!buttons) {
    if(activeEdge) {
      activeEdge[1] = [lx, ly]
    }
  }
  lastButtons = buttons
})

function line(a, b) {
  var x0 = a[0]-0.5
  var y0 = a[1]-0.5
  var x1 = b[0]-0.5
  var y1 = b[1]-0.5
  var w = canvas.width
  var h = canvas.height
  var s = Math.min(w, h)
  context.beginPath()
  context.moveTo(s*x0 + w/2, s*y0 + h/2)
  context.lineTo(s*x1 + w/2, s*y1 + h/2)
  context.stroke()
}

function circle(x, y, r) {
  var w = canvas.width
  var h = canvas.height
  var s = Math.min(w, h)
  context.beginPath()
  context.moveTo(s*x, s*y)
  context.arc(s*(x-0.5) + w/2, s*(y-0.5) + h/2, r, 0.0, 2.0*Math.PI)
  context.fill()
}

var EDGE_PALETTE = [
  'rgba(255,0,0,0.25)',
  'rgba(0,255,0,0.25)',
  'rgba(0,0,255,0.25)',
  'rgba(255,255,0,0.25)',
  'rgba(255,0,255,0.25)',
  'rgba(0,255,255,0.25)'
]

function draw() {
  requestAnimationFrame(draw)

  var w = canvas.width
  var h = canvas.height
  context.fillStyle = '#fff'
  context.fillRect(0, 0, w, h)

  for(var i=0; i<cleanPoints.length; ++i) {
    var p = cleanPoints[i]
    context.fillStyle = 'rgba(0, 0, 255, 0.25)'
    circle(p[0], p[1], 5)
  }

  for(var i=0; i<cleanEdges.length; ++i) {
    var e = cleanEdges[i]
    var a = cleanPoints[e[0]]
    var b = cleanPoints[e[1]]
    context.strokeStyle = EDGE_PALETTE[i%EDGE_PALETTE.length]
    context.lineWidth = 4
    line(a, b)
  }

  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    context.strokeStyle = '#000'
    context.lineWidth = 1
    line(a, b)
  }

  if(window.NEEDS_FLIP) {
    for(var i=0; i<window.NEEDS_FLIP.length; i+=2) {
      var a = window.NEEDS_FLIP[i]
      var b = window.NEEDS_FLIP[i+1]
      context.strokeStyle = '#00f'
      line(points[a], points[b])
    }
  }


  if(!!activeEdge) {
    context.strokeStyle = '#f00'
    line(activeEdge[0], activeEdge[1])
  } else if(highlightEdge >= 0) {
    var e = edges[highlightEdge]
    context.strokeStyle = '#f00'
    line(points[e[0]], points[e[1]])
  }


  for(var i=0; i<points.length; ++i) {
    var p = points[i]
    if(i === highlightPoint || i === startPoint) {
      context.fillStyle = '#f00'
    } else {
      context.fillStyle = '#000'
    }
    circle(p[0], p[1], 2)
  }
}

draw()
