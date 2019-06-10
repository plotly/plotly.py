'use strict'

var createBuffer = require('gl-buffer')
var createVAO = require('gl-vao')
var createShader = require('./shaders/index')

module.exports = createSpikes

var identity = [1,0,0,0,
                0,1,0,0,
                0,0,1,0,
                0,0,0,1]

function AxisSpikes(gl, buffer, vao, shader) {
  this.gl         = gl
  this.buffer     = buffer
  this.vao        = vao
  this.shader     = shader
  this.pixelRatio = 1
  this.bounds     = [[-1000,-1000,-1000], [1000,1000,1000]]
  this.position   = [0,0,0]
  this.lineWidth  = [2,2,2]
  this.colors     = [[0,0,0,1], [0,0,0,1], [0,0,0,1]]
  this.enabled    = [true,true,true]
  this.drawSides  = [true,true,true]
  this.axes       = null
}

var proto = AxisSpikes.prototype

var OUTER_FACE = [0,0,0]
var INNER_FACE = [0,0,0]

var SHAPE = [0,0]

proto.isTransparent = function() {
  return false
}

proto.drawTransparent = function(camera) {}

proto.draw = function(camera) {
  var gl = this.gl
  var vao = this.vao
  var shader = this.shader

  vao.bind()
  shader.bind()

  var model      = camera.model || identity
  var view       = camera.view || identity
  var projection = camera.projection || identity

  var axis
  if(this.axes) {
    axis = this.axes.lastCubeProps.axis
  }

  var outerFace = OUTER_FACE
  var innerFace = INNER_FACE
  for(var i=0; i<3; ++i) {
    if(axis && axis[i] < 0) {
      outerFace[i] = this.bounds[0][i]
      innerFace[i] = this.bounds[1][i]
    } else {
      outerFace[i] = this.bounds[1][i]
      innerFace[i] = this.bounds[0][i]
    }
  }

  SHAPE[0] = gl.drawingBufferWidth
  SHAPE[1] = gl.drawingBufferHeight

  shader.uniforms.model       = model
  shader.uniforms.view        = view
  shader.uniforms.projection  = projection
  shader.uniforms.coordinates = [this.position, outerFace, innerFace]
  shader.uniforms.colors      = this.colors
  shader.uniforms.screenShape = SHAPE

  for(var i=0; i<3; ++i) {
    shader.uniforms.lineWidth = this.lineWidth[i] * this.pixelRatio
    if(this.enabled[i]) {
      vao.draw(gl.TRIANGLES, 6, 6*i)
      if(this.drawSides[i]) {
        vao.draw(gl.TRIANGLES, 12, 18+12*i)
      }
    }
  }

  vao.unbind()
}

proto.update = function(options) {
  if(!options) {
    return
  }
  if("bounds" in options) {
    this.bounds = options.bounds
  }
  if("position" in options) {
    this.position = options.position
  }
  if("lineWidth" in options) {
    this.lineWidth = options.lineWidth
  }
  if("colors" in options) {
    this.colors = options.colors
  }
  if("enabled" in options) {
    this.enabled = options.enabled
  }
  if("drawSides" in options) {
    this.drawSides = options.drawSides
  }
}

proto.dispose = function() {
  this.vao.dispose()
  this.buffer.dispose()
  this.shader.dispose()
}



function createSpikes(gl, options) {
  //Create buffers
  var data = [ ]

  function line(x,y,z,i,l,h) {
    var row = [x,y,z,  0,0,0,  1]
    row[i+3] = 1
    row[i] = l
    data.push.apply(data, row)
    row[6] = -1
    data.push.apply(data, row)
    row[i] = h
    data.push.apply(data, row)
    data.push.apply(data, row)
    row[6] = 1
    data.push.apply(data, row)
    row[i] = l
    data.push.apply(data, row)
  }

  line(0,0,0, 0, 0, 1)
  line(0,0,0, 1, 0, 1)
  line(0,0,0, 2, 0, 1)

  line(1,0,0,  1,  -1,1)
  line(1,0,0,  2,  -1,1)

  line(0,1,0,  0,  -1,1)
  line(0,1,0,  2,  -1,1)

  line(0,0,1,  0,  -1,1)
  line(0,0,1,  1,  -1,1)

  var buffer = createBuffer(gl, data)
  var vao = createVAO(gl, [{
    type: gl.FLOAT,
    buffer: buffer,
    size: 3,
    offset: 0,
    stride: 28
  }, {
    type: gl.FLOAT,
    buffer: buffer,
    size: 3,
    offset: 12,
    stride: 28
  }, {
    type: gl.FLOAT,
    buffer: buffer,
    size: 1,
    offset: 24,
    stride: 28
  }])

  //Create shader
  var shader = createShader(gl)
  shader.attributes.position.location = 0
  shader.attributes.color.location = 1
  shader.attributes.weight.location = 2

  //Create spike object
  var spikes = new AxisSpikes(gl, buffer, vao, shader)

  //Set parameters
  spikes.update(options)

  //Return resulting object
  return spikes
}
