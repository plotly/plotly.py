'use strict'

var createShader = require('gl-shader')
var createBuffer = require('gl-buffer')

var pool = require('typedarray-pool')

var SHADERS = require('./lib/shader')

module.exports = createPointcloud2D

function Pointcloud2D(plot, offsetBuffer, pickBuffer, shader, pickShader) {
  this.plot           = plot
  this.offsetBuffer   = offsetBuffer
  this.pickBuffer     = pickBuffer
  this.shader         = shader
  this.pickShader     = pickShader
  this.sizeMin        = 0.5
  this.sizeMinCap     = 2
  this.sizeMax        = 20
  this.areaRatio      = 1.0
  this.pointCount     = 0
  this.color          = [1, 0, 0, 1]
  this.borderColor    = [0, 0, 0, 1]
  this.blend          = false
  this.pickOffset     = 0
  this.points         = null
}

var proto = Pointcloud2D.prototype

proto.dispose = function() {
  this.shader.dispose()
  this.pickShader.dispose()
  this.offsetBuffer.dispose()
  this.pickBuffer.dispose()
  this.plot.removeObject(this)
}

proto.update = function(options) {

  var i

  options = options || {}

  function dflt(opt, value) {
    if(opt in options) {
      return options[opt]
    }
    return value
  }

  this.sizeMin      = dflt('sizeMin', 0.5)
  // this.sizeMinCap      = dflt('sizeMinCap', 2)
  this.sizeMax      = dflt('sizeMax', 20)
  this.color        = dflt('color', [1, 0, 0, 1]).slice()
  this.areaRatio    = dflt('areaRatio', 1)
  this.borderColor  = dflt('borderColor', [0, 0, 0, 1]).slice()
  this.blend        = dflt('blend', false)

  //Update point data

  // Attempt straight-through processing (STP) to avoid allocation and copy
  // TODO eventually abstract out STP logic, maybe into `pool` or a layer above
  var pointCount = options.positions.length >>> 1
  var dataStraightThrough = options.positions instanceof Float32Array
  var idStraightThrough = options.idToIndex instanceof Int32Array && options.idToIndex.length >= pointCount // permit larger to help reuse

  var data          = options.positions
  var packed        = dataStraightThrough ? data : pool.mallocFloat32(data.length)
  var packedId      = idStraightThrough ? options.idToIndex : pool.mallocInt32(pointCount)

  if(!dataStraightThrough) {
    packed.set(data)
  }

  if(!idStraightThrough) {
    packed.set(data)
    for(i = 0; i < pointCount; i++) {
      packedId[i] = i
    }
  }

  this.points       = data

  this.offsetBuffer.update(packed)
  this.pickBuffer.update(packedId)

  if(!dataStraightThrough) {
    pool.free(packed)
  }

  if(!idStraightThrough) {
    pool.free(packedId)
  }

  this.pointCount = pointCount
  this.pickOffset = 0
}

function count(points, dataBox) {
  var visiblePointCountEstimate = 0
  var length = points.length >>> 1
  var i
  for(i = 0; i < length; i++) {
    var x = points[i * 2]
    var y = points[i * 2 + 1]
    if(x >= dataBox[0] && x <= dataBox[2] && y >= dataBox[1] && y <= dataBox[3])
      visiblePointCountEstimate++
  }
  return visiblePointCountEstimate
}

proto.unifiedDraw = (function() {
  var MATRIX = [1, 0, 0,
                0, 1, 0,
                0, 0, 1]
  var PICK_VEC4 = [0, 0, 0, 0]
return function(pickOffset) {
  var pick = pickOffset !== void(0)

  var shader        = pick ? this.pickShader : this.shader
  var gl            = this.plot.gl
  var dataBox       = this.plot.dataBox

  if(this.pointCount === 0) {
    return pickOffset
  }

  var dataX   = dataBox[2] - dataBox[0]
  var dataY   = dataBox[3] - dataBox[1]

  var visiblePointCountEstimate = count(this.points, dataBox)
  var basicPointSize =  this.plot.pickPixelRatio * Math.max(Math.min(this.sizeMinCap, this.sizeMin), Math.min(this.sizeMax, this.sizeMax / Math.pow(visiblePointCountEstimate, 0.33333)))

  MATRIX[0] = 2.0 / dataX
  MATRIX[4] = 2.0 / dataY
  MATRIX[6] = -2.0 * dataBox[0] / dataX - 1.0
  MATRIX[7] = -2.0 * dataBox[1] / dataY - 1.0

  this.offsetBuffer.bind()

  shader.bind()
  shader.attributes.position.pointer()
  shader.uniforms.matrix      = MATRIX
  shader.uniforms.color       = this.color
  shader.uniforms.borderColor = this.borderColor
  shader.uniforms.pointCloud = basicPointSize < 5
  shader.uniforms.pointSize = basicPointSize
  shader.uniforms.centerFraction = Math.min(1, Math.max(0, Math.sqrt(1 - this.areaRatio)))

  if(pick) {

    PICK_VEC4[0] = ( pickOffset        & 0xff)
    PICK_VEC4[1] = ((pickOffset >> 8)  & 0xff)
    PICK_VEC4[2] = ((pickOffset >> 16) & 0xff)
    PICK_VEC4[3] = ((pickOffset >> 24) & 0xff)

    this.pickBuffer.bind()
    shader.attributes.pickId.pointer(gl.UNSIGNED_BYTE)
    shader.uniforms.pickOffset = PICK_VEC4
    this.pickOffset = pickOffset
  }

  // Worth switching these off, but we can't make assumptions about other
  // renderers, so let's restore it after each draw
  var blend = gl.getParameter(gl.BLEND)
  var dither = gl.getParameter(gl.DITHER)

  if(blend && !this.blend)
    gl.disable(gl.BLEND)
  if(dither)
    gl.disable(gl.DITHER)

  gl.drawArrays(gl.POINTS, 0, this.pointCount)

  if(blend && !this.blend)
    gl.enable(gl.BLEND)
  if(dither)
    gl.enable(gl.DITHER)

  return pickOffset + this.pointCount
}
})()

proto.draw = proto.unifiedDraw
proto.drawPick = proto.unifiedDraw

proto.pick = function(x, y, value) {
  var pickOffset = this.pickOffset
  var pointCount = this.pointCount
  if(value < pickOffset || value >= pickOffset + pointCount) {
    return null
  }
  var pointId = value - pickOffset
  var points = this.points
  return {
    object: this,
    pointId: pointId,
    dataCoord: [points[2 * pointId], points[2 * pointId + 1] ]
  }
}

function createPointcloud2D(plot, options) {
  var gl = plot.gl
  var buffer = createBuffer(gl)
  var pickBuffer = createBuffer(gl)
  var shader = createShader(gl, SHADERS.pointVertex, SHADERS.pointFragment)
  var pickShader = createShader(gl, SHADERS.pickVertex, SHADERS.pickFragment)

  var result = new Pointcloud2D(plot, buffer, pickBuffer, shader, pickShader)
  result.update(options)

  //Register with plot
  plot.addObject(result)

  return result
}
