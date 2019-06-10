'use strict'

module.exports    = createLines

var createBuffer  = require('gl-buffer')
var createVAO     = require('gl-vao')
var createShader  = require('./shaders').line

var MAJOR_AXIS = [0,0,0]
var MINOR_AXIS = [0,0,0]
var SCREEN_AXIS = [0,0,0]
var OFFSET_VEC = [0,0,0]
var SHAPE = [1,1]

function zeroVec(a) {
  a[0] = a[1] = a[2] = 0
  return a
}

function copyVec(a,b) {
  a[0] = b[0]
  a[1] = b[1]
  a[2] = b[2]
  return a
}

function Lines(gl, vertBuffer, vao, shader, tickCount, tickOffset, gridCount, gridOffset) {
  this.gl         = gl
  this.vertBuffer = vertBuffer
  this.vao        = vao
  this.shader     = shader
  this.tickCount  = tickCount
  this.tickOffset = tickOffset
  this.gridCount  = gridCount
  this.gridOffset = gridOffset
}

var proto = Lines.prototype

proto.bind = function(model, view, projection) {
  this.shader.bind()
  this.shader.uniforms.model = model
  this.shader.uniforms.view = view
  this.shader.uniforms.projection = projection

  SHAPE[0] = this.gl.drawingBufferWidth
  SHAPE[1] = this.gl.drawingBufferHeight

  this.shader.uniforms.screenShape = SHAPE
  this.vao.bind()
}

proto.unbind = function() {
  this.vao.unbind()
}

proto.drawAxisLine = function(j, bounds, offset, color, lineWidth) {
  var minorAxis = zeroVec(MINOR_AXIS)
  this.shader.uniforms.majorAxis = MINOR_AXIS

  minorAxis[j] = bounds[1][j] - bounds[0][j]
  this.shader.uniforms.minorAxis = minorAxis

  var noffset = copyVec(OFFSET_VEC, offset)
  noffset[j] += bounds[0][j]
  this.shader.uniforms.offset = noffset

  this.shader.uniforms.lineWidth = lineWidth

  this.shader.uniforms.color = color

  var screenAxis = zeroVec(SCREEN_AXIS)
  screenAxis[(j+2)%3] = 1
  this.shader.uniforms.screenAxis = screenAxis
  this.vao.draw(this.gl.TRIANGLES, 6)

  var screenAxis = zeroVec(SCREEN_AXIS)
  screenAxis[(j+1)%3] = 1
  this.shader.uniforms.screenAxis = screenAxis
  this.vao.draw(this.gl.TRIANGLES, 6)
}

proto.drawAxisTicks = function(j, offset, minorAxis, color, lineWidth) {
  if(!this.tickCount[j]) {
    return
  }

  var majorAxis = zeroVec(MAJOR_AXIS)
  majorAxis[j]  = 1
  this.shader.uniforms.majorAxis = majorAxis
  this.shader.uniforms.offset    = offset
  this.shader.uniforms.minorAxis = minorAxis
  this.shader.uniforms.color     = color
  this.shader.uniforms.lineWidth = lineWidth

  var screenAxis = zeroVec(SCREEN_AXIS)
  screenAxis[j] = 1
  this.shader.uniforms.screenAxis = screenAxis
  this.vao.draw(this.gl.TRIANGLES, this.tickCount[j], this.tickOffset[j])
}


proto.drawGrid = function(i, j, bounds, offset, color, lineWidth) {
  if(!this.gridCount[i]) {
    return
  }

  var minorAxis = zeroVec(MINOR_AXIS)
  minorAxis[j]  = bounds[1][j] - bounds[0][j]
  this.shader.uniforms.minorAxis = minorAxis

  var noffset = copyVec(OFFSET_VEC, offset)
  noffset[j] += bounds[0][j]
  this.shader.uniforms.offset = noffset

  var majorAxis = zeroVec(MAJOR_AXIS)
  majorAxis[i]  = 1
  this.shader.uniforms.majorAxis = majorAxis

  var screenAxis = zeroVec(SCREEN_AXIS)
  screenAxis[i] = 1
  this.shader.uniforms.screenAxis = screenAxis
  this.shader.uniforms.lineWidth = lineWidth

  this.shader.uniforms.color = color
  this.vao.draw(this.gl.TRIANGLES, this.gridCount[i], this.gridOffset[i])
}

proto.drawZero = function(j, i, bounds, offset, color, lineWidth) {
  var minorAxis = zeroVec(MINOR_AXIS)
  this.shader.uniforms.majorAxis = minorAxis

  minorAxis[j] = bounds[1][j] - bounds[0][j]
  this.shader.uniforms.minorAxis = minorAxis

  var noffset = copyVec(OFFSET_VEC, offset)
  noffset[j] += bounds[0][j]
  this.shader.uniforms.offset = noffset

  var screenAxis = zeroVec(SCREEN_AXIS)
  screenAxis[i] = 1
  this.shader.uniforms.screenAxis = screenAxis
  this.shader.uniforms.lineWidth = lineWidth

  this.shader.uniforms.color = color
  this.vao.draw(this.gl.TRIANGLES, 6)
}

proto.dispose = function() {
  this.vao.dispose()
  this.vertBuffer.dispose()
  this.shader.dispose()
}

function createLines(gl, bounds, ticks) {
  var vertices    = []
  var tickOffset  = [0,0,0]
  var tickCount   = [0,0,0]

  //Create grid lines for each axis/direction
  var gridOffset = [0,0,0]
  var gridCount  = [0,0,0]

  //Add zero line
  vertices.push(
    0,0,1,   0,1,1,   0,0,-1,
    0,0,-1,  0,1,1,   0,1,-1)

  for(var i=0; i<3; ++i) {
    //Axis tick marks
    var start = ((vertices.length / 3)|0)
    for(var j=0; j<ticks[i].length; ++j) {
      var x = +ticks[i][j].x
      vertices.push(
        x,0,1,   x,1,1,   x,0,-1,
        x,0,-1,  x,1,1,   x,1,-1)
    }
    var end = ((vertices.length / 3)|0)
    tickOffset[i] = start
    tickCount[i]  = end - start

    //Grid lines
    var start = ((vertices.length / 3)|0)
    for(var k=0; k<ticks[i].length; ++k) {
      var x = +ticks[i][k].x
      vertices.push(
        x,0,1,   x,1,1,   x,0,-1,
        x,0,-1,  x,1,1,   x,1,-1)
    }
    var end = ((vertices.length / 3)|0)
    gridOffset[i] = start
    gridCount[i]  = end - start
  }

  //Create cube VAO
  var vertBuf = createBuffer(gl, new Float32Array(vertices))
  var vao = createVAO(gl, [
    { "buffer": vertBuf,
      "type": gl.FLOAT,
      "size": 3,
      "stride": 0,
      "offset": 0
    }
  ])
  var shader = createShader(gl)
  shader.attributes.position.location = 0
  return new Lines(gl, vertBuf, vao, shader, tickCount, tickOffset, gridCount, gridOffset)
}
