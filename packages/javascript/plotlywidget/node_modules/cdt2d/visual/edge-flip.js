'use strict'

var orient = require('robust-orientation')
var vec2 = require('vec2')
var segment2 = require('segment2')
var mouseChange = require('mouse-change')
var fit = require('canvas-fit')
var delaunay = require('delaunay-triangulate')
var createTriangulation = require('../lib/triangulation')

//Create canvas and context
var canvas = document.createElement('canvas')
var context = canvas.getContext('2d')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas), false)

var points = []
for(var i=0; i<40; ++i) {
  points.push([Math.random(), Math.random()])
}

var triangulation = createTriangulation(points.length)
delaunay(points).forEach(function(cell) {
    triangulation.addTriangle(cell[0], cell[1], cell[2])
})

var closestEdge = null

function distance(a, b, c) {
  var p = vec2(c[0], c[1])
  return segment2(vec2(a[0], a[1]), vec2(b[0], b[1])).closestPointTo(p).distance(p)
}

var lastButtons = 0
mouseChange(canvas, function(buttons, x, y) {
  if(!lastButtons && buttons && closestEdge) {
    triangulation.flip(closestEdge[0], closestEdge[1])
  }

  var edges = triangulation.edges()
  var p = [x / canvas.width, y / canvas.height]
  var closestDistance = 0.1
  closestEdge = null
  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    var d2 = distance(a, b, p)
    if(d2 < closestDistance && orient(a, b, p) > 0) {
      closestDistance = d2
      closestEdge = e
    }
  }
})

function line(x0, y0, x1, y1) {
  var w = canvas.width
  var h = canvas.height
  context.beginPath()
  context.moveTo(w*x0, h*y0)
  context.lineTo(w*x1, h*y1)
  context.stroke()
}

function circle(x, y, r) {
  var w = canvas.width
  var h = canvas.height
  context.beginPath()
  context.moveTo(w*x, y*h)
  context.arc(w*x, h*y, r, 0.0, 2.0*Math.PI)
  context.fill()
}

var CW_ARROW = '⟳'
var CCW_ARROW = '⟲'

function drawSpiral(a, b, c) {
  var w = canvas.width
  var h = canvas.height
  var x = w * (a[0] + b[0] + c[0]) / 3.0
  var y = h * (a[1] + b[1] + c[1]) / 3.0
  context.font = Math.ceil(Math.min(w, h)*0.025) + 'px Verdana'
  if(orient(a, b, c) > 0) {
    context.fillText(CW_ARROW, x, y)
  } else {
    context.fillText(CCW_ARROW, x, y)
  }
}

function draw() {
  requestAnimationFrame(draw)

  var w = canvas.width
  var h = canvas.height
  context.fillStyle = '#fff'
  context.fillRect(0, 0, w, h)

  var edges = triangulation.edges()
  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    if( closestEdge &&
       ((e[0] === closestEdge[0] && e[1] === closestEdge[1]) ||
        (e[1] === closestEdge[0] && e[0] === closestEdge[1]))) {
      context.strokeStyle = '#f00'
    } else {
      context.strokeStyle = '#000'
    }
    line(a[0], a[1], b[0], b[1])
  }

  var ca = -1, cb = -1, cs = -1, ct = -1

  if(closestEdge) {
    ca = closestEdge[0]
    cb = closestEdge[1]
    cs = triangulation.opposite(ca, cb)
    ct = triangulation.opposite(cb, ca)
  }

  var s0 = [ca, cb, cs].sort().join()
  var s1 = [ca, cb, ct].sort().join()

  var cells = triangulation.cells()
  for(var i=0; i<cells.length; ++i) {
    var f = cells[i]
    var a = points[f[0]]
    var b = points[f[1]]
    var c = points[f[2]]
    var fs = f.slice().sort().join()
    if(fs === s0) {
      context.fillStyle = '#0f0'
    } else if(fs === s1) {
      context.fillStyle = '#00f'
    } else {
      context.fillStyle = '#000'
    }
    drawSpiral(a, b, c)
  }

  for(var i=0; i<points.length; ++i) {
    var p = points[i]
    if(i === ca || i === cb) {
      context.fillStyle = '#f00'
    } else if(i === cs) {
      context.fillStyle = '#0f0'
    } else if(i === ct) {
      context.fillStyle = '#00f'
    } else {
      context.fillStyle = '#000'
    }
    circle(p[0], p[1], 3)
  }
}
draw()
