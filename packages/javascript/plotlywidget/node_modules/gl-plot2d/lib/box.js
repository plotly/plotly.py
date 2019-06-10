'use strict'

module.exports = createBoxes

var createBuffer = require('gl-buffer')
var createShader = require('gl-shader')

var shaders = require('./shaders')

function Boxes(plot, vbo, shader) {
  this.plot   = plot
  this.vbo    = vbo
  this.shader = shader
}

var proto = Boxes.prototype

proto.bind = function() {
  var shader = this.shader
  this.vbo.bind()
  this.shader.bind()
  shader.attributes.coord.pointer()
  shader.uniforms.screenBox = this.plot.screenBox
}

proto.drawBox = (function() {
  var lo = [0,0]
  var hi = [0,0]
  return function(loX, loY, hiX, hiY, color) {
    var plot       = this.plot
    var shader     = this.shader
    var gl         = plot.gl

    lo[0] = loX
    lo[1] = loY
    hi[0] = hiX
    hi[1] = hiY

    shader.uniforms.lo     = lo
    shader.uniforms.hi     = hi
    shader.uniforms.color  = color

    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4)
  }
}())

proto.dispose = function() {
  this.vbo.dispose()
  this.shader.dispose()
}

function createBoxes(plot) {
  var gl  = plot.gl
  var vbo = createBuffer(gl, [
    0,0,
    0,1,
    1,0,
    1,1])
  var shader  = createShader(gl, shaders.boxVert, shaders.lineFrag)
  return new Boxes(plot, vbo, shader)
}
