'use strict'

module.exports = createContour2D

var iota = require('iota-array')
var createShader = require('gl-shader')
var createBuffer = require('gl-buffer')
var ndarray = require('ndarray')
var surfaceNets = require('surface-nets')
var cdt2d = require('cdt2d')
var cleanPSLG = require('clean-pslg')
var bsearch = require('binary-search-bounds')

var shaders = require('./lib/shaders')

function GLContour2D (
  plot,
  shader,
  fillShader,
  positionBuffer,
  colorBuffer,
  idBuffer,
  fillPositionBuffer,
  fillColorBuffer) {
  this.plot = plot
  this.shader = shader
  this.fillShader = fillShader
  this.positionBuffer = positionBuffer
  this.colorBuffer = colorBuffer
  this.idBuffer = idBuffer
  this.fillPositionBuffer = fillPositionBuffer
  this.fillColorBuffer = fillColorBuffer
  this.fillVerts = 0
  this.shape = [0, 0]
  this.bounds = [Infinity, Infinity, -Infinity, -Infinity]
  this.numVertices = 0
  this.lineWidth = 1
}

var proto = GLContour2D.prototype

var WEIGHTS = [
  1, 0,
  0, 0,
  0, 1,
  1, 0,
  1, 1,
  0, 1
]

proto.draw = (function () {
  var MATRIX = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ]

  var SCREEN_SHAPE = [0, 0]

  return function () {
    var plot = this.plot
    var shader = this.shader
    var fillShader = this.fillShader
    var bounds = this.bounds
    var numVertices = this.numVertices
    var fillVerts = this.fillVerts

    var uniforms, attributes

    var gl = plot.gl
    var viewBox = plot.viewBox
    var dataBox = plot.dataBox

    var boundX = bounds[2] - bounds[0]
    var boundY = bounds[3] - bounds[1]
    var dataX = dataBox[2] - dataBox[0]
    var dataY = dataBox[3] - dataBox[1]

    MATRIX[0] = 2.0 * boundX / dataX
    MATRIX[4] = 2.0 * boundY / dataY
    MATRIX[6] = 2.0 * (bounds[0] - dataBox[0]) / dataX - 1.0
    MATRIX[7] = 2.0 * (bounds[1] - dataBox[1]) / dataY - 1.0

    SCREEN_SHAPE[0] = viewBox[2] - viewBox[0]
    SCREEN_SHAPE[1] = viewBox[3] - viewBox[1]

    if (fillVerts > 0) {
      fillShader.bind()

      uniforms = fillShader.uniforms
      uniforms.viewTransform = MATRIX
      uniforms.screenShape = SCREEN_SHAPE

      attributes = shader.attributes
      this.fillPositionBuffer.bind()
      attributes.position.pointer()

      this.fillColorBuffer.bind()
      attributes.color.pointer(gl.UNSIGNED_BYTE, true)

      gl.drawArrays(gl.TRIANGLES, 0, fillVerts)
    }

    if (numVertices > 0) {
      shader.bind()

      var lineWidth = this.lineWidth * plot.pixelRatio

      uniforms = shader.uniforms
      uniforms.viewTransform = MATRIX
      uniforms.screenShape = SCREEN_SHAPE
      uniforms.lineWidth = lineWidth
      uniforms.pointSize = 1000

      attributes = shader.attributes

      // Draw lines
      this.positionBuffer.bind()
      attributes.position.pointer(gl.FLOAT, false, 16, 0)
      attributes.tangent.pointer(gl.FLOAT, false, 16, 8)

      this.colorBuffer.bind()
      attributes.color.pointer(gl.UNSIGNED_BYTE, true)

      gl.drawArrays(gl.TRIANGLES, 0, numVertices)

      // Draw end caps
      uniforms.lineWidth = 0
      uniforms.pointSize = lineWidth

      this.positionBuffer.bind()
      attributes.position.pointer(gl.FLOAT, false, 16 * 3, 0)
      attributes.tangent.pointer(gl.FLOAT, false, 16 * 3, 8)

      this.colorBuffer.bind()
      attributes.color.pointer(gl.UNSIGNED_BYTE, true, 4 * 3, 0)

      gl.drawArrays(gl.POINTS, 0, numVertices / 3)
    }
  }
})()

proto.drawPick = (function () {
  return function (pickOffset) {
    return pickOffset
  }
})()

proto.pick = function (x, y, value) {
  return null
}

function interpolate (array, point) {
  var idx = Math.floor(point)
  if (idx < 0) {
    return array[0]
  } else if (idx >= array.length - 1) {
    return array[array.length - 1]
  }
  var t = point - idx
  return (1.0 - t) * array[idx] + t * array[idx + 1]
}

proto.update = function (options) {
  options = options || {}

  var shape = options.shape || [0, 0]

  var x = options.x || iota(shape[0])
  var y = options.y || iota(shape[1])
  var z = options.z || new Float32Array(shape[0] * shape[1])

  var levels = options.levels || []
  var levelColors = options.levelColors || []

  var bounds = this.bounds
  var lox = bounds[0] = x[0]
  var loy = bounds[1] = y[0]
  var hix = bounds[2] = x[x.length - 1]
  var hiy = bounds[3] = y[y.length - 1]

  if (lox === hix) {
    bounds[2] += 1
    hix += 1
  }
  if (loy === hiy) {
    bounds[3] += 1
    hiy += 1
  }

  var xs = 1.0 / (hix - lox)
  var ys = 1.0 / (hiy - loy)

  this.lineWidth = options.lineWidth || 1

  var zarray = ndarray(z, shape)

  var positions = []
  var colors = []
  var ids = []

  var fillCells = []
  var fillPositions = [
    [0, 0],
    [shape[0] - 1, 0],
    [0, shape[1] - 1],
    [shape[0] - 1, shape[1] - 1]
  ]

  function intersect (level, x, a, b) {
    var d = (b - a)
    if (Math.abs(d) < 1e-6) {
      return x
    }
    return Math.floor(x) + Math.max(0.001, Math.min(0.999, (level - a) / d))
  }

  for (var i = 0; i < levels.length; ++i) {
    var level = levels[i]
    if (i > 0 && level === levels[i - 1]) {
      continue
    }
    var contour = surfaceNets(zarray, level)

    var c_r = (255 * levelColors[4 * i]) | 0
    var c_g = (255 * levelColors[4 * i + 1]) | 0
    var c_b = (255 * levelColors[4 * i + 2]) | 0
    var c_a = (255 * levelColors[4 * i + 3]) | 0

    var c_cells = contour.cells
    var c_positions = contour.positions

    // Fix boundaries
    var in_degree = Array(c_positions.length)
    for (var j = 0; j < in_degree.length; ++j) {
      in_degree[j] = 0
    }
    for (j = 0; j < c_cells.length; ++j) {
      var edge = c_cells[j]
      in_degree[edge[0]] += 1
      in_degree[edge[1]] += 1
    }

    for (j = 0; j < in_degree.length; ++j) {
      var deg = in_degree[j]
      if (deg === 0) {
        continue
      }
      var pp = c_positions[j]
      in_degree[j] = fillPositions.length
      fillPositions.push(pp)
      if (deg > 1) {
        continue
      }
      var ppx = pp[0]
      var ppy = pp[1]
      var z00 = zarray.get(Math.floor(ppx), Math.floor(ppy))
      var z01 = zarray.get(Math.floor(ppx), Math.ceil(ppy))
      var z10 = zarray.get(Math.ceil(ppx), Math.floor(ppy))
      var z11 = zarray.get(Math.ceil(ppx), Math.ceil(ppy))
      var intercept
      if (Math.floor(pp[0]) === 0 &&
          ((z00 <= level) !== (z01 < level))) {
        intercept = [0, intersect(level, pp[1], z00, z01)]
      } else if (Math.ceil(pp[0]) === shape[0] - 1 &&
          ((z10 <= level) !== (z11 < level))) {
        intercept = [shape[0] - 1, intersect(level, pp[1], z10, z11)]
      } else if (Math.floor(pp[1]) === 0 &&
          ((z00 <= level) !== (z10 < level))) {
        intercept = [intersect(level, pp[0], z00, z10), 0]
      } else if (Math.ceil(pp[1]) === shape[1] - 1 &&
          ((z01 <= level) !== (z11 < level))) {
        intercept = [intersect(level, pp[0], z01, z11), shape[1] - 1]
      }
      if (intercept) {
        c_cells.push([j, c_positions.length])
        in_degree.push(fillPositions.length)
        c_positions.push(intercept)
      }
    }

    for (j = 0; j < c_cells.length; ++j) {
      var e = c_cells[j]
      var a = c_positions[e[0]]
      var b = c_positions[e[1]]

      fillCells.push([in_degree[e[0]], in_degree[e[1]]])

      var pointId = Math.round(a[0]) + shape[0] * Math.round(a[1])

      var ax = interpolate(x, a[0])
      var ay = interpolate(y, a[1])
      var bx = interpolate(x, b[0])
      var by = interpolate(y, b[1])

      ax = xs * (ax - lox)
      ay = ys * (ay - loy)
      bx = xs * (bx - lox)
      by = ys * (by - loy)

      var dx = ax - bx
      var dy = ay - by

      for (var k = 0; k < WEIGHTS.length; k += 2) {
        var wx = WEIGHTS[k]
        var wix = 1.0 - wx
        var wy = 2.0 * WEIGHTS[k + 1] - 1.0

        positions.push(
          wix * ax + wx * bx, wix * ay + wx * by,
          wy * dx, wy * dy)
        colors.push(c_r, c_g, c_b, c_a)
        ids.push(pointId)
      }
    }
  }

  this.positionBuffer.update(new Float32Array(positions))
  this.colorBuffer.update(new Uint8Array(colors))
  this.idBuffer.update(new Uint32Array(ids))
  this.numVertices = ids.length

  var fillColors = options.fillColors
  var fillCellColors = []
  var fillCellPositions = []
  var fillVerts = 0

  if (fillColors) {
    cleanPSLG(fillPositions, fillCells)
    var fillMesh = cdt2d(fillPositions, fillCells, {
      delaunay: false
    })
    for (i = 0; i < fillMesh.length; ++i) {
      var cell = fillMesh[i]
      var cx = 0
      var cy = 0

      for (j = 0; j < 3; ++j) {
        var p = fillPositions[cell[j]]
        var px = interpolate(x, p[0])
        var py = interpolate(y, p[1])
        cx += p[0]
        cy += p[1]
        fillCellPositions.push(
          xs * (px - lox),
          ys * (py - loy))
      }

      // Compute centroid of triangle
      cx /= 3
      cy /= 3

      // Sample height field at triangle centroid
      var cxi = Math.floor(cx)
      var cyi = Math.floor(cy)
      var cxf = cx - cxi
      var cyf = cy - cyi

      var c00 = zarray.get(cxi, cyi)
      var c01 = zarray.get(cxi, cyi + 1)
      var c10 = zarray.get(cxi + 1, cyi)
      var c11 = zarray.get(cxi + 1, cyi + 1)

      var zlevel =
        (1 - cyf) * ((1 - cxf) * c00 + cxf * c10) +
        cyf * ((1 - cxf) * c01 + cxf * c11)

      // Color triangle using centroid data
      var l = bsearch.le(levels, zlevel) + 1
      var cr = (255 * fillColors[4 * l + 0]) | 0
      var cg = (255 * fillColors[4 * l + 1]) | 0
      var cb = (255 * fillColors[4 * l + 2]) | 0
      var ca = (255 * fillColors[4 * l + 3]) | 0

      fillCellColors.push(
        cr, cg, cb, ca,
        cr, cg, cb, ca,
        cr, cg, cb, ca)

      fillVerts += 3
    }

    this.fillPositionBuffer.update(new Float32Array(fillCellPositions))
    this.fillColorBuffer.update(new Uint8Array(fillCellColors))

    this.fillVerts = fillVerts
  }
}

proto.dispose = function () {
  this.plot.removeObject(this)
}

function createContour2D (plot, options) {
  var gl = plot.gl

  var shader = createShader(gl, shaders.vertex, shaders.fragment)
  var fillShader = createShader(gl, shaders.fillVertex, shaders.fragment)

  var positionBuffer = createBuffer(gl)
  var colorBuffer = createBuffer(gl)
  var idBuffer = createBuffer(gl)

  var fillPositionBuffer = createBuffer(gl)
  var fillColorBuffer = createBuffer(gl)

  var contours = new GLContour2D(
    plot,
    shader,
    fillShader,
    positionBuffer,
    colorBuffer,
    idBuffer,
    fillPositionBuffer,
    fillColorBuffer)

  contours.update(options)
  plot.addObject(contours)

  return contours
}
