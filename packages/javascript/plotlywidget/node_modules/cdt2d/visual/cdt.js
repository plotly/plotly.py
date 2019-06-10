'use strict'

var orient = require('robust-orientation')
var vec2 = require('vec2')
var segment2 = require('segment2')
var mouseChange = require('mouse-change')
var segCrosses = require('robust-segment-intersect')
var fit = require('canvas-fit')
var createTriangulation = require('../cdt2d')

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

var points = []
var edges = []
var options = {
  delaunay: true,
  interior: true,
  exterior: true,
  infinity: false
}

for(var i=0; i<4; ++i) {
  for(var j=0; j<4; ++j) {
    points.push([0.25 + i/6,0.25 + j/6])
  }
}
for(var i=0; i<3; ++i) {
  edges.push([i, i+1])
  edges.push([i+12, i+13])
  edges.push([4*i, 4*i+4])
  edges.push([4*i+3, 4*i+7])
}
edges.push([5,6], [9,10], [5,9], [6,10])

var cells = createTriangulation(points, edges, options)

Object.keys(options).forEach(function(name) {
  var container = document.createElement('p')

  var checkBox = document.createElement('input')
  checkBox.type = 'checkbox'
  checkBox.name = name
  checkBox.checked = options[name]
  checkBox.id = 'check_' + name

  var label = document.createElement('label')
  label.htmlFor = checkBox.id
  label.appendChild(document.createTextNode(name))

  checkBox.addEventListener('change', function() {
    options[name] = !!checkBox.checked
    cells = createTriangulation(points, edges, options)
  })

  container.appendChild(checkBox)
  container.appendChild(label)

  optionDiv.appendChild(container)
})

var resetButton = document.createElement('input')
resetButton.type = 'button'
resetButton.value = 'reset'
resetButton.addEventListener('click', function() {
  points.length = edges.length = 0
  cells = createTriangulation(points, edges, options)
})
var resetP = document.createElement('p')
resetP.appendChild(resetButton)
optionDiv.appendChild(resetP)

var description = document.createElement('p')
description.innerHTML = 'click to add/remove points<br>drag to add constraints<br><a href="https://github.com/mikolalysenko/cdt2d">Project page</a>'
optionDiv.appendChild(description)

function edgeDistance(a, b, c) {
  var p = vec2(c[0], c[1])
  return segment2(vec2(a[0], a[1]), vec2(b[0], b[1])).closestPointTo(p).distance(p)
}

function isValidEdge(a, b) {
  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    if(e[0] < 0 || e[1] < 0) {
      continue
    }
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
  for(var i=0; i<points.length; ++i) {
    var p = points[i]
    if(p === a || p === b) {
      continue
    }
    if(segCrosses(a, b, p, p)) {
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
      cells = createTriangulation(points, edges, options)
      highlightEdge = -1
    } else if(highlightPoint < 0) {
      points.push([lx, ly])
      cells = createTriangulation(points, edges, options)
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
        cells = createTriangulation(points, edges, options)
      } else if(highlightPoint >= 0) {
        if(isValidEdge(points[startPoint], points[highlightPoint])) {
          edges.push([startPoint, highlightPoint])
          cells = createTriangulation(points, edges, options)
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

var CW_ARROW = '⟳'
var CCW_ARROW = '⟲'

function drawSpiral(a, b, c) {
  var w = canvas.width
  var h = canvas.height
  var s = Math.min(w, h)
  var x = s * ((a[0] + b[0] + c[0]) / 3.0 - 0.5) + w/2
  var y = s * ((a[1] + b[1] + c[1]) / 3.0 - 0.5) + h/2
  var size = Math.ceil(s*0.025)
  context.font = size + 'px Verdana'
  if(orient(a, b, c) > 0) {
    context.fillText(CW_ARROW, x-0.5*size, y+0.25*size)
  } else {
    context.fillText(CCW_ARROW, x-0.5*size, y+0.25*size)
  }
}

function length(v) {
  return Math.sqrt(Math.pow(v[0], 2) + Math.pow(v[1], 2))
}

function scale(v, s) {
  return [v[0]*s, v[1]*s]
}

function sum(u, v) {
  return [u[0]+v[0], u[1]+v[1]]
}

function bisector(a, b, c) {
  var ab = [a[0] - b[0], a[1] - b[1]]
  var cb = [c[0] - b[0], c[1] - b[1]]
  var d = sum(scale(ab, length(cb)), scale(cb, length(ab)))
  var l = length(d)
  if(l > 1e-6) {
    return scale(d, 1.0 / l)
  }
  return scale([ ab[1], -ab[0] ], 1.0 / length(ab))
}

function draw() {
  requestAnimationFrame(draw)

  var w = canvas.width
  var h = canvas.height
  context.fillStyle = '#fff'
  context.fillRect(0, 0, w, h)

  var neighbors = new Array(points.length)
  for(var i=0; i<points.length; ++i) {
    neighbors[i] = [-1,-1]
  }

  for(var i=0; i<cells.length; ++i) {
    var f = cells[i]
    if(f[0] < 0 || f[1] < 0 || f[2] < 0) {
      for(var j=0; j<3; ++j) {
        if(f[j] < 0) {
          var x = f[(j+1)%3]
          var y = f[(j+2)%3]
          neighbors[x][0] = y
          neighbors[y][1] = x
        }
      }
      continue
    }
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

  for(var i=0; i<points.length; ++i) {
    var ray = neighbors[i]
    if(ray[0] < 0 || ray[1] < 0) {
      continue
    }
    var a = points[ray[0]]
    var b = points[i]
    var c = points[ray[1]]
    context.strokeStyle = '#000'
    line(b, sum(scale(bisector(a, b, c), -1000), b))
  }

  for(var i=0; i<edges.length; ++i) {
    var e = edges[i]
    var a = points[e[0]]
    var b = points[e[1]]
    context.strokeStyle = '#0f0'
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
    circle(p[0], p[1], 3)
  }
}

draw()
