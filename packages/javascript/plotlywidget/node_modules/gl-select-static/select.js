'use strict'

module.exports = createSelectBuffer

var createFBO = require('gl-fbo')
var pool      = require('typedarray-pool')
var ndarray   = require('ndarray')
var cwise     = require('cwise')
var nextPow2  = require('bit-twiddle').nextPow2

var selectRange = cwise({
  args: [
      'array',
      {'offset': [0,0,1], 'array':0},
      {'offset': [0,0,2], 'array':0},
      {'offset': [0,0,3], 'array':0},
      'scalar',
      'scalar',
      'index'],
  pre: function() {
    this.closestD2 = 1e8
    this.closestX = -1
    this.closestY = -1
  },
  body: function(r, g, b, a, x, y, idx) {
    if(r < 255 || g < 255 || b < 255 || a < 255) {
      var dx = x - idx[0]
      var dy = y - idx[1]
      var d2 = dx*dx + dy*dy
      if(d2 < this.closestD2) {
        this.closestD2 = d2
        this.closestX = idx[0]
        this.closestY = idx[1]
      }
    }
  },
  post: function() {
    return [this.closestX, this.closestY, this.closestD2]
  }
})

function SelectResult(x, y, id, value, distance) {
  this.coord = [x, y]
  this.id = id
  this.value = value
  this.distance = distance
}

function SelectBuffer(gl, fbo, buffer) {
  this.gl     = gl
  this.fbo    = fbo
  this.buffer = buffer
  this._readTimeout = null
  var self = this

  this._readCallback = function() {
    if(!self.gl) {
      return
    }
    fbo.bind()
    gl.readPixels(0,0,fbo.shape[0],fbo.shape[1],gl.RGBA,gl.UNSIGNED_BYTE,self.buffer)
    self._readTimeout = null
  }
}

var proto = SelectBuffer.prototype

Object.defineProperty(proto, 'shape', {
  get: function() {
    if(!this.gl) {
      return [0,0]
    }
    return this.fbo.shape.slice()
  },
  set: function(v) {
    if(!this.gl) {
      return
    }
    this.fbo.shape = v
    var c = this.fbo.shape[0]
    var r = this.fbo.shape[1]
    if(r*c*4 > this.buffer.length) {
      pool.free(this.buffer)
      var buffer = this.buffer = pool.mallocUint8(nextPow2(r*c*4))
      for(var i=0; i<r*c*4; ++i) {
        buffer[i] = 0xff
      }
    }
    return v
  }
})

proto.begin = function() {
  var gl = this.gl
  var shape = this.shape
  if(!gl) {
    return
  }

  this.fbo.bind()
  gl.clearColor(1,1,1,1)
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)
}

proto.end = function() {
  var gl = this.gl
  if(!gl) {
    return
  }
  gl.bindFramebuffer(gl.FRAMEBUFFER, null)
  if(!this._readTimeout) {
    clearTimeout(this._readTimeout)
  }
  this._readTimeout = setTimeout(this._readCallback, 1)
}

proto.query = function(x, y, radius) {
  if(!this.gl) {
    return null
  }

  var shape = this.fbo.shape.slice()

  x = x|0
  y = y|0
  if(typeof radius !== 'number') {
    radius = 1.0
  }

  var x0 = Math.min(Math.max(x - radius, 0), shape[0])|0
  var x1 = Math.min(Math.max(x + radius, 0), shape[0])|0
  var y0 = Math.min(Math.max(y - radius, 0), shape[1])|0
  var y1 = Math.min(Math.max(y + radius, 0), shape[1])|0

  if(x1 <= x0 || y1 <= y0) {
    return null
  }

  var dims   = [x1-x0,y1-y0]
  var region = ndarray(
    this.buffer,
    [dims[0], dims[1], 4],
    [4, shape[0]*4, 1],
    4*(x0 + shape[0]*y0));

  var closest = selectRange(region.hi(dims[0],dims[1],1), radius, radius)
  var dx = closest[0]
  var dy = closest[1]
  if(dx < 0 || Math.pow(this.radius, 2) < closest[2]) {
    return null
  }

  var c0 = region.get(dx, dy, 0)
  var c1 = region.get(dx, dy, 1)
  var c2 = region.get(dx, dy, 2)
  var c3 = region.get(dx, dy, 3)

  return new SelectResult(
     (dx + x0)|0,
     (dy + y0)|0,
     c0,
     [c1, c2, c3],
     Math.sqrt(closest[2]))
}

proto.dispose = function() {
  if(!this.gl) {
    return
  }
  this.fbo.dispose()
  pool.free(this.buffer)
  this.gl = null
  if(this._readTimeout) {
    clearTimeout(this._readTimeout)
  }
}

function createSelectBuffer(gl, shape) {
  var fbo = createFBO(gl, shape)
  var buffer = pool.mallocUint8(shape[0]*shape[1]*4)
  return new SelectBuffer(gl, fbo, buffer)
}
