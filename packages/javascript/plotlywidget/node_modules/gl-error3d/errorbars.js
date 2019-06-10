'use strict'

module.exports = createErrorBars

var createBuffer  = require('gl-buffer')
var createVAO     = require('gl-vao')
var createShader  = require('./shaders/index')

var IDENTITY = [1,0,0,0,
                0,1,0,0,
                0,0,1,0,
                0,0,0,1]

function ErrorBars(gl, buffer, vao, shader) {
  this.gl           = gl
  this.shader       = shader
  this.buffer       = buffer
  this.vao          = vao
  this.pixelRatio   = 1
  this.bounds       = [[ Infinity, Infinity, Infinity], [-Infinity,-Infinity,-Infinity]]
  this.clipBounds   = [[-Infinity,-Infinity,-Infinity], [ Infinity, Infinity, Infinity]]
  this.lineWidth    = [1,1,1]
  this.capSize      = [10,10,10]
  this.lineCount    = [0,0,0]
  this.lineOffset   = [0,0,0]
  this.opacity      = 1
  this.hasAlpha     = false
}

var proto = ErrorBars.prototype

proto.isOpaque = function() {
  return !this.hasAlpha
}

proto.isTransparent = function() {
  return this.hasAlpha
}

proto.drawTransparent = proto.draw = function(cameraParams) {
  var gl = this.gl
  var uniforms        = this.shader.uniforms

  this.shader.bind()
  var view       = uniforms.view       = cameraParams.view       || IDENTITY
  var projection = uniforms.projection = cameraParams.projection || IDENTITY
  uniforms.model      = cameraParams.model      || IDENTITY
  uniforms.clipBounds = this.clipBounds
  uniforms.opacity    = this.opacity


  var cx = view[12]
  var cy = view[13]
  var cz = view[14]
  var cw = view[15]

  var isOrtho = cameraParams._ortho || false
  var orthoFix = (isOrtho) ? 2 : 1 // double up padding for orthographic ticks & labels
  var pixelScaleF = orthoFix * this.pixelRatio * (projection[3]*cx + projection[7]*cy + projection[11]*cz + projection[15]*cw) / gl.drawingBufferHeight

  this.vao.bind()
  for(var i=0; i<3; ++i) {
    gl.lineWidth(this.lineWidth[i] * this.pixelRatio)
    uniforms.capSize = this.capSize[i] * pixelScaleF
    if (this.lineCount[i]) {
      gl.drawArrays(gl.LINES, this.lineOffset[i], this.lineCount[i])
    }
  }
  this.vao.unbind()
}

function updateBounds(bounds, point) {
  for(var i=0; i<3; ++i) {
    bounds[0][i] = Math.min(bounds[0][i], point[i])
    bounds[1][i] = Math.max(bounds[1][i], point[i])
  }
}

var FACE_TABLE = (function(){
  var table = new Array(3)
  for(var d=0; d<3; ++d) {
    var row = []
    for(var j=1; j<=2; ++j) {
      for(var s=-1; s<=1; s+=2) {
        var u = (j+d) % 3
        var y = [0,0,0]
        y[u] = s
        row.push(y)
      }
    }
    table[d] = row
  }
  return table
})()


function emitFace(verts, x, c, d) {
  var offsets = FACE_TABLE[d]
  for(var i=0; i<offsets.length; ++i) {
    var o = offsets[i]
    verts.push(x[0], x[1], x[2],
               c[0], c[1], c[2], c[3],
               o[0], o[1], o[2])
  }
  return offsets.length
}

proto.update = function(options) {
  options = options || {}

  if('lineWidth' in options) {
    this.lineWidth = options.lineWidth
    if(!Array.isArray(this.lineWidth)) {
      this.lineWidth = [this.lineWidth, this.lineWidth, this.lineWidth]
    }
  }
  if('capSize' in options) {
    this.capSize = options.capSize
    if(!Array.isArray(this.capSize)) {
      this.capSize = [this.capSize, this.capSize, this.capSize]
    }
  }

  this.hasAlpha = false // default to no transparent draw
  if('opacity' in options) {
    this.opacity = +options.opacity
    if(this.opacity < 1) {
      this.hasAlpha = true;
    }
  }

  var color    = options.color || [[0,0,0],[0,0,0],[0,0,0]]
  var position = options.position
  var error    = options.error
  if(!Array.isArray(color[0])) {
    color = [color,color,color]
  }

  if(position && error) {

    var verts       = []
    var n           = position.length
    var vertexCount = 0
    this.bounds     = [[ Infinity, Infinity, Infinity],
                       [-Infinity,-Infinity,-Infinity]]
    this.lineCount  = [0,0,0]

    //Build geometry for lines
    for(var j=0; j<3; ++j) {
      this.lineOffset[j] = vertexCount

i_loop:
      for(var i=0; i<n; ++i) {
        var p = position[i]

        for(var k=0; k<3; ++k) {
          if(isNaN(p[k]) || !isFinite(p[k])) {
            continue i_loop
          }
        }

        var e = error[i]
        var c = color[j]
        if(Array.isArray(c[0])) {
          c = color[i]
        }
        if(c.length === 3) {
          c = [c[0], c[1], c[2], 1]
        } else if(c.length === 4) {
          c = [c[0], c[1], c[2], c[3]]
          if(!this.hasAlpha && c[3] < 1) this.hasAlpha = true
        }

        if(isNaN(e[0][j]) || isNaN(e[1][j])) {
          continue
        }
        if(e[0][j] < 0) {
          var x = p.slice()
          x[j] += e[0][j]
          verts.push(p[0], p[1], p[2],
                     c[0], c[1], c[2], c[3],
                        0,    0,    0,
                     x[0], x[1], x[2],
                     c[0], c[1], c[2], c[3],
                        0,    0,    0)
          updateBounds(this.bounds, x)
          vertexCount += 2 + emitFace(verts, x, c, j)
        }
        if(e[1][j] > 0) {
          var x = p.slice()
          x[j] += e[1][j]
          verts.push(p[0], p[1], p[2],
                     c[0], c[1], c[2], c[3],
                        0,    0,    0,
                     x[0], x[1], x[2],
                     c[0], c[1], c[2], c[3],
                        0,    0,    0)
          updateBounds(this.bounds, x)
          vertexCount += 2 + emitFace(verts, x, c, j)
        }
      }
      this.lineCount[j] = vertexCount - this.lineOffset[j]
    }
    this.buffer.update(verts)
  }
}

proto.dispose = function() {
  this.shader.dispose()
  this.buffer.dispose()
  this.vao.dispose()
}

function createErrorBars(options) {
  var gl = options.gl
  var buffer = createBuffer(gl)
  var vao = createVAO(gl, [
      {
        buffer: buffer,
        type:   gl.FLOAT,
        size:   3,
        offset: 0,
        stride: 40
      },
      {
        buffer: buffer,
        type:   gl.FLOAT,
        size:   4,
        offset: 12,
        stride: 40
      },
      {
        buffer: buffer,
        type:   gl.FLOAT,
        size:   3,
        offset: 28,
        stride: 40
      }
    ])

  var shader = createShader(gl)
  shader.attributes.position.location = 0
  shader.attributes.color.location    = 1
  shader.attributes.offset.location   = 2

  var result = new ErrorBars(gl, buffer, vao, shader)
  result.update(options)
  return result
}
