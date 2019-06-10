'use strict'

var glslify = require('glslify')
var createShader = require('gl-shader')

var vertSrc = glslify('./vertex.glsl')
var fragSrc = glslify('./fragment.glsl')

module.exports = function(gl) {
  return createShader(gl, vertSrc, fragSrc, null, [
    {name: 'position', type: 'vec3'},
    {name: 'color', type: 'vec4'},
    {name: 'offset', type: 'vec3'}
  ])
}
