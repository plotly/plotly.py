var glslify       = require('glslify')

var triVertSrc = glslify('./triangle-vertex.glsl')
var triFragSrc = glslify('./triangle-fragment.glsl')
var pickVertSrc = glslify('./pick-vertex.glsl')
var pickFragSrc = glslify('./pick-fragment.glsl')

exports.meshShader = {
  vertex:   triVertSrc,
  fragment: triFragSrc,
  attributes: [
    {name: 'position', type: 'vec4'},
    {name: 'normal', type: 'vec3'},
    {name: 'color', type: 'vec4'},
    {name: 'uv', type: 'vec2'},
    {name: 'vector', type: 'vec3'}
  ]
}
exports.pickShader = {
  vertex:   pickVertSrc,
  fragment: pickFragSrc,
  attributes: [
    {name: 'position', type: 'vec4'},
    {name: 'id', type: 'vec4'},
    {name: 'vector', type: 'vec3'}
  ]
}
