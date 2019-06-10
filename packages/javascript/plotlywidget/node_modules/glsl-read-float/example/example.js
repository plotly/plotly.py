"use strict"

var triangle     = require('a-big-triangle')
var glslify      = require('glslify')
var unpackFloat  = require("../index.js")

var canvas     = document.body.appendChild(document.createElement('canvas'))
var gl         = canvas.getContext('webgl')

var shader = glslify({
  vert: "\
attribute vec2 position;\
void main() {\
  gl_Position = vec4(position, 0, 1);\
}",
  frag: "\
#pragma glslify: packFloat = require(../index.glsl)\n\
uniform highp float f;\
void main() {\
  gl_FragColor = packFloat(f);\
}",
  inline: true
})(gl)

var FLOAT = new Float32Array(1)
var BYTE  = new Uint8Array(FLOAT.buffer)

function render(num) {
  //Convert to float
  FLOAT[0] = num

  //Draw shader
  shader.bind()
  shader.uniforms.f = FLOAT[0]
  triangle(gl)

  //Read back the float
  var buffer = new Uint8Array(4)
  gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, buffer)
  var unpacked = unpackFloat(buffer[0], buffer[1], buffer[2], buffer[3])

  FLOAT[0] = num
  console.log('in bits:', BYTE[3], BYTE[2], BYTE[1], BYTE[0])
  console.log('out bits: ', buffer[0], buffer[1], buffer[2], buffer[3])

  //Log output to console
  if(FLOAT[0] === unpacked) {
    console.log('ok')
  } else {
    console.log('fail, expected:', FLOAT[0], 'got:', unpacked)
  }
}

for(var i=-300; i<300; ++i) {
  render(i)
}
for(var j=0; j<100; ++j) {
  render(Math.random())
}
//Test edge cases
render(1.70141184e38)
render(-1.70141184e38)
render(1.17549435e-38)
render(-1.17549435e-38)
render(Infinity)
render(-Infinity)
