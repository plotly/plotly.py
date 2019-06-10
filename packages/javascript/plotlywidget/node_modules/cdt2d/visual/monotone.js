'use strict'

var orient = require('robust-orientation')
var vec2 = require('vec2')
var segment2 = require('segment2')
var mouseChange = require('mouse-change')
var segCrosses = require('robust-segment-intersect')
var fit = require('canvas-fit')
var createTriangulation = require('../lib/monotone')

//Create canvas and context
var canvas = document.createElement('canvas')
var context = canvas.getContext('2d')
document.body.appendChild(canvas)
window.addEventListener('resize', fit(canvas), false)

function edgeDistance(a, b, c) {
  var p = vec2(c[0], c[1])
  return segment2(vec2(a[0], a[1]), vec2(b[0], b[1])).closestPointTo(p).distance(p)
}

var points = []
var edges = []

for(var i=0; i<4; ++i) {
  for(var j=0; j<4; ++j) {
    points.push([0.25 + i/10,0.25 + j/10])
  }
}

var cells = createTriangulation(points, edges)

function isValidEdge(a, b) {
  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var p = points[e[0]]
    var q = points[e[1]]
    if( (p === a && q !== b) ||
        (p === b && q !== a) ||
        (q === a && p !== b) ||
        (q === b && p !== a)) {
      continue
    }
    if(segCrosses(a, b, p, q)) {
      return false
    }
  }
  return true
}

var lastButtons = 0,
  highlightPoint = -1,
  startPoint = -1,
  highlightEdge = -1,
  activeEdge = null
mouseChange(canvas, function(buttons, x, y) {
  var lx = x / canvas.width
  var ly = y / canvas.height
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
      cells = createTriangulation(points, edges)
      highlightEdge = -1
    } else if(highlightPoint < 0) {
      points.push([lx, ly])
      cells = createTriangulation(points, edges)
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
        cells = createTriangulation(points, edges)
      } else if(highlightPoint >= 0) {
        if(isValidEdge(points[startPoint], points[highlightPoint])) {
          edges.push([startPoint, highlightPoint])
          cells = createTriangulation(points, edges)
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
  var x0 = a[0]
  var y0 = a[1]
  var x1 = b[0]
  var y1 = b[1]
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

  for(var i=0; i<cells.length; ++i) {
    var f = cells[i]
    var a = points[f[0]]
    var b = points[f[1]]
    var c = points[f[2]]
    var fs = f.slice().sort().join()
    context.fillStyle = '#000'
    context.strokeStyle = '#000'
    line(a, b)
    line(b, c)
    line(c, a)
    drawSpiral(a, b, c)
  }

  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    context.strokeStyle = '#0f0'
    line(a, b)
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
    circle(p[0], p[1], 3)
  }
}

draw()
