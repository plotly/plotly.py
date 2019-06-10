'use strict'

module.exports = createBackgroundCube

var createBuffer = require('gl-buffer')
var createVAO    = require('gl-vao')
var createShader = require('./shaders').bg

function BackgroundCube(gl, buffer, vao, shader) {
  this.gl = gl
  this.buffer = buffer
  this.vao = vao
  this.shader = shader
}

var proto = BackgroundCube.prototype

proto.draw = function(model, view, projection, bounds, enable, colors) {
  var needsBG = false
  for(var i=0; i<3; ++i) {
    needsBG = needsBG || enable[i]
  }
  if(!needsBG) {
    return
  }

  var gl = this.gl

  gl.enable(gl.POLYGON_OFFSET_FILL)
  gl.polygonOffset(1, 2)

  this.shader.bind()
  this.shader.uniforms = {
    model: model,
    view: view,
    projection: projection,
    bounds: bounds,
    enable: enable,
    colors: colors
  }
  this.vao.bind()
  this.vao.draw(this.gl.TRIANGLES, 36)
  this.vao.unbind()

  gl.disable(gl.POLYGON_OFFSET_FILL)
}

proto.dispose = function() {
  this.vao.dispose()
  this.buffer.dispose()
  this.shader.dispose()
}

function createBackgroundCube(gl) {
  //Create cube vertices
  var vertices = []
  var indices  = []
  var ptr = 0
  for(var d=0; d<3; ++d) {
    var u = (d+1) % 3
    var v = (d+2) % 3
    var x = [0,0,0]
    var c = [0,0,0]
    for(var s=-1; s<=1; s+=2) {
      indices.push(ptr,   ptr+2, ptr+1,
                   ptr+1, ptr+2, ptr+3)
      x[d] = s
      c[d] = s
      for(var i=-1; i<=1; i+=2) {
        x[u] = i
        for(var j=-1; j<=1; j+=2) {
          x[v] = j
          vertices.push(x[0], x[1], x[2],
                        c[0], c[1], c[2])
          ptr += 1
        }
      }
      //Swap u and v
      var tt = u
      u = v
      v = tt
    }
  }

  //Allocate buffer and vertex array
  var buffer = createBuffer(gl, new Float32Array(vertices))
  var elements = createBuffer(gl, new Uint16Array(indices), gl.ELEMENT_ARRAY_BUFFER)
  var vao = createVAO(gl, [
      {
        buffer: buffer,
        type: gl.FLOAT,
        size: 3,
        offset: 0,
        stride: 24
      },
      {
        buffer: buffer,
        type: gl.FLOAT,
        size: 3,
        offset: 12,
        stride: 24
      }
    ], elements)

  //Create shader object
  var shader = createShader(gl)
  shader.attributes.position.location = 0
  shader.attributes.normal.location = 1

  return new BackgroundCube(gl, buffer, vao, shader)
}
