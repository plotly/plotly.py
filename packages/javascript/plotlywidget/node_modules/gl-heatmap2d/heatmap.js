'use strict'

module.exports = createHeatmap2D

var bsearch = require('binary-search-bounds')
var iota = require('iota-array')
var pool = require('typedarray-pool')
var createShader = require('gl-shader')
var createBuffer = require('gl-buffer')

var shaders = require('./lib/shaders')

function GLHeatmap2D (
  plot,
  shader,
  pickShader,
  positionBuffer,
  weightBuffer,
  colorBuffer,
  idBuffer) {
  this.plot = plot
  this.shader = shader
  this.pickShader = pickShader
  this.positionBuffer = positionBuffer
  this.weightBuffer = weightBuffer
  this.colorBuffer = colorBuffer
  this.idBuffer = idBuffer
  this.xData = []
  this.yData = []
  this.shape = [0, 0]
  this.bounds = [Infinity, Infinity, -Infinity, -Infinity]
  this.pickOffset = 0
}

var proto = GLHeatmap2D.prototype

var WEIGHTS = [
  0, 0,
  1, 0,
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

  return function () {
    var plot = this.plot
    var shader = this.shader
    var bounds = this.bounds
    var numVertices = this.numVertices

    if (numVertices <= 0) {
      return
    }

    var gl = plot.gl
    var dataBox = plot.dataBox

    var boundX = bounds[2] - bounds[0]
    var boundY = bounds[3] - bounds[1]
    var dataX = dataBox[2] - dataBox[0]
    var dataY = dataBox[3] - dataBox[1]

    MATRIX[0] = 2.0 * boundX / dataX
    MATRIX[4] = 2.0 * boundY / dataY
    MATRIX[6] = 2.0 * (bounds[0] - dataBox[0]) / dataX - 1.0
    MATRIX[7] = 2.0 * (bounds[1] - dataBox[1]) / dataY - 1.0

    shader.bind()

    var uniforms = shader.uniforms
    uniforms.viewTransform = MATRIX

    uniforms.shape = this.shape

    var attributes = shader.attributes
    this.positionBuffer.bind()
    attributes.position.pointer()

    this.weightBuffer.bind()
    attributes.weight.pointer(gl.UNSIGNED_BYTE, false)

    this.colorBuffer.bind()
    attributes.color.pointer(gl.UNSIGNED_BYTE, true)

    gl.drawArrays(gl.TRIANGLES, 0, numVertices)
  }
})()

proto.drawPick = (function () {
  var MATRIX = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ]

  var PICK_VECTOR = [0, 0, 0, 0]

  return function (pickOffset) {
    var plot = this.plot
    var shader = this.pickShader
    var bounds = this.bounds
    var numVertices = this.numVertices

    if (numVertices <= 0) {
      return
    }

    var gl = plot.gl
    var dataBox = plot.dataBox

    var boundX = bounds[2] - bounds[0]
    var boundY = bounds[3] - bounds[1]
    var dataX = dataBox[2] - dataBox[0]
    var dataY = dataBox[3] - dataBox[1]

    MATRIX[0] = 2.0 * boundX / dataX
    MATRIX[4] = 2.0 * boundY / dataY
    MATRIX[6] = 2.0 * (bounds[0] - dataBox[0]) / dataX - 1.0
    MATRIX[7] = 2.0 * (bounds[1] - dataBox[1]) / dataY - 1.0

    for (var i = 0; i < 4; ++i) {
      PICK_VECTOR[i] = (pickOffset >> (i * 8)) & 0xff
    }

    this.pickOffset = pickOffset

    shader.bind()

    var uniforms = shader.uniforms
    uniforms.viewTransform = MATRIX
    uniforms.pickOffset = PICK_VECTOR
    uniforms.shape = this.shape

    var attributes = shader.attributes
    this.positionBuffer.bind()
    attributes.position.pointer()

    this.weightBuffer.bind()
    attributes.weight.pointer(gl.UNSIGNED_BYTE, false)

    this.idBuffer.bind()
    attributes.pickId.pointer(gl.UNSIGNED_BYTE, false)

    gl.drawArrays(gl.TRIANGLES, 0, numVertices)

    return pickOffset + this.shape[0] * this.shape[1]
  }
})()

proto.pick = function (x, y, value) {
  var pickOffset = this.pickOffset
  var pointCount = this.shape[0] * this.shape[1]
  if (value < pickOffset || value >= pickOffset + pointCount) {
    return null
  }
  var pointId = value - pickOffset
  var xData = this.xData
  var yData = this.yData
  return {
    object: this,
    pointId: pointId,
    dataCoord: [
      xData[pointId % this.shape[0]],
      yData[(pointId / this.shape[0]) | 0]]
  }
}

proto.update = function (options) {
  options = options || {}

  var shape = options.shape || [0, 0]

  var x = options.x || iota(shape[0])
  var y = options.y || iota(shape[1])
  var z = options.z || new Float32Array(shape[0] * shape[1])

  this.xData = x
  this.yData = y

  var colorLevels = options.colorLevels || [0]
  var colorValues = options.colorValues || [0, 0, 0, 1]
  var colorCount = colorLevels.length

  var bounds = this.bounds
  var lox = bounds[0] = x[0]
  var loy = bounds[1] = y[0]
  var hix = bounds[2] = x[x.length - 1]
  var hiy = bounds[3] = y[y.length - 1]

  var xs = 1.0 / (hix - lox)
  var ys = 1.0 / (hiy - loy)

  var numX = shape[0]
  var numY = shape[1]

  this.shape = [numX, numY]

  var numVerts = (numX - 1) * (numY - 1) * (WEIGHTS.length >>> 1)

  this.numVertices = numVerts

  var colors = pool.mallocUint8(numVerts * 4)
  var positions = pool.mallocFloat32(numVerts * 2)
  var weights   = pool.mallocUint8 (numVerts * 2)
  var ids = pool.mallocUint32(numVerts)

  var ptr = 0

  for (var j = 0; j < numY - 1; ++j) {
    var yc0 = ys * (y[j] - loy)
    var yc1 = ys * (y[j + 1] - loy)
    for (var i = 0; i < numX - 1; ++i) {
      var xc0 = xs * (x[i] - lox)
      var xc1 = xs * (x[i + 1] - lox)

      for (var dd = 0; dd < WEIGHTS.length; dd += 2) {
        var dx = WEIGHTS[dd]
        var dy = WEIGHTS[dd + 1]
        var offset = (j + dy) * numX + (i + dx)
        var zc = z[offset]
        var colorIdx = bsearch.le(colorLevels, zc)
        var r, g, b, a
        if (colorIdx < 0) {
          r = colorValues[0]
          g = colorValues[1]
          b = colorValues[2]
          a = colorValues[3]
        } else if (colorIdx === colorCount - 1) {
          r = colorValues[4 * colorCount - 4]
          g = colorValues[4 * colorCount - 3]
          b = colorValues[4 * colorCount - 2]
          a = colorValues[4 * colorCount - 1]
        } else {
          var t = (zc - colorLevels[colorIdx]) /
            (colorLevels[colorIdx + 1] - colorLevels[colorIdx])
          var ti = 1.0 - t
          var i0 = 4 * colorIdx
          var i1 = 4 * (colorIdx + 1)
          r = ti * colorValues[i0] + t * colorValues[i1]
          g = ti * colorValues[i0 + 1] + t * colorValues[i1 + 1]
          b = ti * colorValues[i0 + 2] + t * colorValues[i1 + 2]
          a = ti * colorValues[i0 + 3] + t * colorValues[i1 + 3]
        }

        colors[4 * ptr] = 255 * r
        colors[4 * ptr + 1] = 255 * g
        colors[4 * ptr + 2] = 255 * b
        colors[4 * ptr + 3] = 255 * a

        positions[2*ptr] = xc0*.5 + xc1*.5;
        positions[2*ptr+1] = yc0*.5 + yc1*.5;

        weights[2*ptr] = dx;
        weights[2*ptr+1] = dy;

        ids[ptr] = j * numX + i

        ptr += 1
      }
    }
  }

  this.positionBuffer.update(positions)
  this.weightBuffer.update(weights)
  this.colorBuffer.update(colors)
  this.idBuffer.update(ids)

  pool.free(positions)
  pool.free(colors)
  pool.free(weights)
  pool.free(ids)
}

proto.dispose = function () {
  this.shader.dispose()
  this.pickShader.dispose()
  this.positionBuffer.dispose()
  this.weightBuffer.dispose()
  this.colorBuffer.dispose()
  this.idBuffer.dispose()
  this.plot.removeObject(this)
}

function createHeatmap2D (plot, options) {
  var gl = plot.gl

  var shader = createShader(gl, shaders.vertex, shaders.fragment)
  var pickShader = createShader(gl, shaders.pickVertex, shaders.pickFragment)

  var positionBuffer = createBuffer(gl)
  var weightBuffer   = createBuffer(gl)
  var colorBuffer = createBuffer(gl)
  var idBuffer = createBuffer(gl)

  var heatmap = new GLHeatmap2D(
    plot,
    shader,
    pickShader,
    positionBuffer,
    weightBuffer,
    colorBuffer,
    idBuffer)

  heatmap.update(options)
  plot.addObject(heatmap)

  return heatmap
}
