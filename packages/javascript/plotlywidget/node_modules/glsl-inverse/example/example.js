var glslify       = require('glslify')
var drawTriangle  = require('a-big-triangle')
var invert        = require('gl-matrix-invert')

var canvas = document.createElement('canvas')
var gl = canvas.getContext('webgl')

var shader = glslify({
  vert: '\
attribute vec2 position;\
void main() {\
  gl_Position = vec4(position,0.0,1.0);\
}',
  frag: '\
precision highp float;\n\
#pragma glslify: frob = require(glsl-frobenius)\n\
#pragma glslify: inverse = require(../index.glsl)\n\
uniform float m0,t0;\
uniform mat2  m1,t1;\
uniform mat3  m2,t2;\
uniform mat4  m3,t3;\
void main() {\
  gl_FragColor = 100.0 * vec4(\
    frob(inverse(m0)-t0),\
    frob(inverse(m1)-t1),\
    frob(inverse(m2)-t2),\
    frob(inverse(m3)-t3));\
}',
  inline: true
})(gl)

function runTest(m0, m1, m2, m3) {
  shader.bind()
  shader.uniforms = {
    t0: 1.0/m0,
    t1: invert(new Array(4), m1),
    t2: invert(new Array(9), m2),
    t3: invert(new Array(16), m3),
    m0: m0,
    m1: m1,
    m2: m2,
    m3: m3
  }
  drawTriangle(gl)

  var result = new Uint8Array(4)
  gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, result)

  if(result[0] > 0 ||
     result[1] > 0 ||
     result[2] > 0 ||
     result[3] > 0) {
    console.log('fail', result[0], result[1], result[2], result[3])
  } else {
    console.log('ok')
  }
}


function randFloat() {
  return (Math.random() - 0.5) * Math.pow(2, 20*(Math.random()-0.5))
}
function randArray(n) {
  var r = new Array(n)
  for(var i=0; i<n; ++i) {
    r[i] = randFloat()
  }
  return r
}

for(var i=0; i<100; ++i) {
  runTest(randFloat(), randArray(4), randArray(9), randArray(16))
}