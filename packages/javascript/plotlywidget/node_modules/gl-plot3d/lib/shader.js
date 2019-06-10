var glslify      = require('glslify')
var createShader = require('gl-shader')

var vertSrc = glslify('./vertex.glsl')
var fragSrc = glslify('./composite.glsl')

module.exports = function(gl) {
  return createShader(gl, vertSrc, fragSrc, null, [ { name: 'position', type: 'vec2'}])
}
