var glslify       = require('glslify')
var createShader  = require('gl-shader')

var vertSrc = glslify('../shaders/vertex.glsl')
var forwardFrag = glslify('../shaders/fragment.glsl')
var pickFrag = glslify('../shaders/pick.glsl')

var ATTRIBUTES = [
  {name: 'position', type: 'vec3'},
  {name: 'nextPosition', type: 'vec3'},
  {name: 'arcLength', type: 'float'},
  {name: 'lineWidth', type: 'float'},
  {name: 'color', type: 'vec4'}
]

exports.createShader = function(gl) {
  return createShader(gl, vertSrc, forwardFrag, null, ATTRIBUTES)
}

exports.createPickShader = function(gl) {
  return createShader(gl, vertSrc, pickFrag, null, ATTRIBUTES)
}
