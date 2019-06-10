'use strict'

module.exports = createLinePlot

var createBuffer = require('gl-buffer')
var createVAO = require('gl-vao')
var createTexture = require('gl-texture2d')
var unpackFloat = require('glsl-read-float')
var bsearch = require('binary-search-bounds')
var ndarray = require('ndarray')
var shaders = require('./lib/shaders')

var createShader = shaders.createShader
var createPickShader = shaders.createPickShader

var identity = [1, 0, 0, 0,
  0, 1, 0, 0,
  0, 0, 1, 0,
  0, 0, 0, 1]

function distance (a, b) {
  var s = 0.0
  for (var i = 0; i < 3; ++i) {
    var d = a[i] - b[i]
    s += d * d
  }
  return Math.sqrt(s)
}

function filterClipBounds (bounds) {
  var result = [[-1e6, -1e6, -1e6], [1e6, 1e6, 1e6]]
  for (var i = 0; i < 3; ++i) {
    result[0][i] = Math.max(bounds[0][i], result[0][i])
    result[1][i] = Math.min(bounds[1][i], result[1][i])
  }
  return result
}

function PickResult (tau, position, index, dataCoordinate) {
  this.arcLength = tau
  this.position = position
  this.index = index
  this.dataCoordinate = dataCoordinate
}

function LinePlot (gl, shader, pickShader, buffer, vao, texture) {
  this.gl = gl
  this.shader = shader
  this.pickShader = pickShader
  this.buffer = buffer
  this.vao = vao
  this.clipBounds = [
    [ -Infinity, -Infinity, -Infinity ],
    [ Infinity, Infinity, Infinity ]]
  this.points = []
  this.arcLength = []
  this.vertexCount = 0
  this.bounds = [[0, 0, 0], [0, 0, 0]]
  this.pickId = 0
  this.lineWidth = 1
  this.texture = texture
  this.dashScale = 1
  this.opacity = 1
  this.hasAlpha = false
  this.dirty = true
  this.pixelRatio = 1
}

var proto = LinePlot.prototype

proto.isTransparent = function () {
  return this.hasAlpha
}

proto.isOpaque = function () {
  return !this.hasAlpha
}

proto.pickSlots = 1

proto.setPickBase = function (id) {
  this.pickId = id
}

proto.drawTransparent = proto.draw = function (camera) {
  if (!this.vertexCount) return
  var gl = this.gl
  var shader = this.shader
  var vao = this.vao
  shader.bind()
  shader.uniforms = {
    model: camera.model || identity,
    view: camera.view || identity,
    projection: camera.projection || identity,
    clipBounds: filterClipBounds(this.clipBounds),
    dashTexture: this.texture.bind(),
    dashScale: this.dashScale / this.arcLength[this.arcLength.length - 1],
    opacity: this.opacity,
    screenShape: [gl.drawingBufferWidth, gl.drawingBufferHeight],
    pixelRatio: this.pixelRatio
  }
  vao.bind()
  vao.draw(gl.TRIANGLE_STRIP, this.vertexCount)
  vao.unbind()
}

proto.drawPick = function (camera) {
  if (!this.vertexCount) return
  var gl = this.gl
  var shader = this.pickShader
  var vao = this.vao
  shader.bind()
  shader.uniforms = {
    model: camera.model || identity,
    view: camera.view || identity,
    projection: camera.projection || identity,
    pickId: this.pickId,
    clipBounds: filterClipBounds(this.clipBounds),
    screenShape: [gl.drawingBufferWidth, gl.drawingBufferHeight],
    pixelRatio: this.pixelRatio
  }
  vao.bind()
  vao.draw(gl.TRIANGLE_STRIP, this.vertexCount)
  vao.unbind()
}

proto.update = function (options) {
  var i, j

  this.dirty = true

  var connectGaps = !!options.connectGaps

  if ('dashScale' in options) {
    this.dashScale = options.dashScale
  }

  this.hasAlpha = false // default to no transparent draw
  if ('opacity' in options) {
    this.opacity = +options.opacity
    if(this.opacity < 1) {
      this.hasAlpha = true;
    }
  }

  // Recalculate buffer data
  var buffer = []
  var arcLengthArray = []
  var pointArray = []
  var arcLength = 0.0
  var vertexCount = 0
  var bounds = [
    [ Infinity, Infinity, Infinity ],
    [ -Infinity, -Infinity, -Infinity ]]

  var positions = options.position || options.positions
  if (positions) {

    // Default color
    var colors = options.color || options.colors || [0, 0, 0, 1]

    var lineWidth = options.lineWidth || 1

    var hadGap = false

    fill_loop:
    for (i = 1; i < positions.length; ++i) {
      var a = positions[i - 1]
      var b = positions[i]

      arcLengthArray.push(arcLength)
      pointArray.push(a.slice())

      for (j = 0; j < 3; ++j) {
        if (isNaN(a[j]) || isNaN(b[j]) ||
          !isFinite(a[j]) || !isFinite(b[j])) {

          if (!connectGaps && buffer.length > 0) {
            for (var k = 0; k < 24; ++k) {
              buffer.push(buffer[buffer.length - 12])
            }
            vertexCount += 2
            hadGap = true
          }

          continue fill_loop
        }
        bounds[0][j] = Math.min(bounds[0][j], a[j], b[j])
        bounds[1][j] = Math.max(bounds[1][j], a[j], b[j])
      }

      var acolor, bcolor
      if (Array.isArray(colors[0])) {
        acolor = (colors.length > i - 1) ? colors[i - 1] :             // using index value
                 (colors.length > 0)     ? colors[colors.length - 1] : // using last item
                                           [0, 0, 0, 1];               // using black

        bcolor = (colors.length > i) ? colors[i] :                 // using index value
                 (colors.length > 0) ? colors[colors.length - 1] : // using last item
                                       [0, 0, 0, 1];               // using black
      } else {
        acolor = bcolor = colors
      }

      if (acolor.length === 3) {
        acolor = [acolor[0], acolor[1], acolor[2], 1]
      }
      if (bcolor.length === 3) {
        bcolor = [bcolor[0], bcolor[1], bcolor[2], 1]
      }

      if(!this.hasAlpha && acolor[3] < 1) this.hasAlpha = true

      var w0
      if (Array.isArray(lineWidth)) {
        w0 = (lineWidth.length > i - 1) ? lineWidth[i - 1] :                // using index value
             (lineWidth.length > 0)     ? lineWidth[lineWidth.length - 1] : // using last item
                                          [0, 0, 0, 1];                     // using black
      } else {
        w0 = lineWidth
      }

      var t0 = arcLength
      arcLength += distance(a, b)

      if (hadGap) {
        for (j = 0; j < 2; ++j) {
          buffer.push(
            a[0], a[1], a[2], b[0], b[1], b[2], t0, w0, acolor[0], acolor[1], acolor[2], acolor[3])
        }
        vertexCount += 2
        hadGap = false
      }

      buffer.push(
        a[0], a[1], a[2], b[0], b[1], b[2], t0, w0, acolor[0], acolor[1], acolor[2], acolor[3],
        a[0], a[1], a[2], b[0], b[1], b[2], t0, -w0, acolor[0], acolor[1], acolor[2], acolor[3],
        b[0], b[1], b[2], a[0], a[1], a[2], arcLength, -w0, bcolor[0], bcolor[1], bcolor[2], bcolor[3],
        b[0], b[1], b[2], a[0], a[1], a[2], arcLength, w0, bcolor[0], bcolor[1], bcolor[2], bcolor[3])

      vertexCount += 4
    }
  }
  this.buffer.update(buffer)

  arcLengthArray.push(arcLength)
  pointArray.push(positions[positions.length - 1].slice())

  this.bounds = bounds

  this.vertexCount = vertexCount

  this.points = pointArray
  this.arcLength = arcLengthArray

  if ('dashes' in options) {
    var dashArray = options.dashes

    // Calculate prefix sum
    var prefixSum = dashArray.slice()
    prefixSum.unshift(0)
    for (i = 1; i < prefixSum.length; ++i) {
      prefixSum[i] = prefixSum[i - 1] + prefixSum[i]
    }

    var dashTexture = ndarray(new Array(256 * 4), [256, 1, 4])
    for (i = 0; i < 256; ++i) {
      for (j = 0; j < 4; ++j) {
        dashTexture.set(i, 0, j, 0)
      }
      if (bsearch.le(prefixSum, prefixSum[prefixSum.length - 1] * i / 255.0) & 1) {
        dashTexture.set(i, 0, 0, 0)
      } else {
        dashTexture.set(i, 0, 0, 255)
      }
    }

    this.texture.setPixels(dashTexture)
  }
}

proto.dispose = function () {
  this.shader.dispose()
  this.vao.dispose()
  this.buffer.dispose()
}

proto.pick = function (selection) {
  if (!selection) {
    return null
  }
  if (selection.id !== this.pickId) {
    return null
  }
  var tau = unpackFloat(
    selection.value[0],
    selection.value[1],
    selection.value[2],
    0)
  var index = bsearch.le(this.arcLength, tau)
  if (index < 0) {
    return null
  }
  if (index === this.arcLength.length - 1) {
    return new PickResult(
      this.arcLength[this.arcLength.length - 1],
      this.points[this.points.length - 1].slice(),
      index)
  }
  var a = this.points[index]
  var b = this.points[Math.min(index + 1, this.points.length - 1)]
  var t = (tau - this.arcLength[index]) / (this.arcLength[index + 1] - this.arcLength[index])
  var ti = 1.0 - t
  var x = [0, 0, 0]
  for (var i = 0; i < 3; ++i) {
    x[i] = ti * a[i] + t * b[i]
  }
  var dataIndex = Math.min((t < 0.5) ? index : (index + 1), this.points.length - 1)
  return new PickResult(
    tau,
    x,
    dataIndex,
    this.points[dataIndex])
}

function createLinePlot (options) {
  var gl = options.gl || (options.scene && options.scene.gl)

  var shader = createShader(gl)
  shader.attributes.position.location = 0
  shader.attributes.nextPosition.location = 1
  shader.attributes.arcLength.location = 2
  shader.attributes.lineWidth.location = 3
  shader.attributes.color.location = 4

  var pickShader = createPickShader(gl)
  pickShader.attributes.position.location = 0
  pickShader.attributes.nextPosition.location = 1
  pickShader.attributes.arcLength.location = 2
  pickShader.attributes.lineWidth.location = 3
  pickShader.attributes.color.location = 4

  var buffer = createBuffer(gl)
  var vao = createVAO(gl, [
    {
      'buffer': buffer,
      'size': 3,
      'offset': 0,
      'stride': 48
    },
    {
      'buffer': buffer,
      'size': 3,
      'offset': 12,
      'stride': 48
    },
    {
      'buffer': buffer,
      'size': 1,
      'offset': 24,
      'stride': 48
    },
    {
      'buffer': buffer,
      'size': 1,
      'offset': 28,
      'stride': 48
    },
    {
      'buffer': buffer,
      'size': 4,
      'offset': 32,
      'stride': 48
    }
  ])

  // Create texture for dash pattern
  var defaultTexture = ndarray(new Array(256 * 4), [256, 1, 4])
  for (var i = 0; i < 256 * 4; ++i) {
    defaultTexture.data[i] = 255
  }
  var texture = createTexture(gl, defaultTexture)
  texture.wrap = gl.REPEAT

  var linePlot = new LinePlot(gl, shader, pickShader, buffer, vao, texture)
  linePlot.update(options)
  return linePlot
}
