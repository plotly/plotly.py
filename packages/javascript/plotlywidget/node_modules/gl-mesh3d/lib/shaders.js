var glslify       = require('glslify')

var triVertSrc = glslify('./triangle-vertex.glsl')
var triFragSrc = glslify('./triangle-fragment.glsl')
var edgeVertSrc = glslify('./edge-vertex.glsl')
var edgeFragSrc = glslify('./edge-fragment.glsl')
var pointVertSrc = glslify('./point-vertex.glsl')
var pointFragSrc = glslify('./point-fragment.glsl')
var pickVertSrc = glslify('./pick-vertex.glsl')
var pickFragSrc = glslify('./pick-fragment.glsl')
var pickPointVertSrc = glslify('./pick-point-vertex.glsl')
var contourVertSrc = glslify('./contour-vertex.glsl')
var contourFragSrc = glslify('./contour-fragment.glsl')

exports.meshShader = {
  vertex:   triVertSrc,
  fragment: triFragSrc,
  attributes: [
    {name: 'position', type: 'vec3'},
    {name: 'normal', type: 'vec3'},
    {name: 'color', type: 'vec4'},
    {name: 'uv', type: 'vec2'}
  ]
}
exports.wireShader = {
  vertex:   edgeVertSrc,
  fragment: edgeFragSrc,
  attributes: [
    {name: 'position', type: 'vec3'},
    {name: 'color', type: 'vec4'},
    {name: 'uv', type: 'vec2'}
  ]
}
exports.pointShader = {
  vertex:   pointVertSrc,
  fragment: pointFragSrc,
  attributes: [
    {name: 'position', type: 'vec3'},
    {name: 'color', type: 'vec4'},
    {name: 'uv', type: 'vec2'},
    {name: 'pointSize', type: 'float'}
  ]
}
exports.pickShader = {
  vertex:   pickVertSrc,
  fragment: pickFragSrc,
  attributes: [
    {name: 'position', type: 'vec3'},
    {name: 'id', type: 'vec4'}
  ]
}
exports.pointPickShader = {
  vertex:   pickPointVertSrc,
  fragment: pickFragSrc,
  attributes: [
    {name: 'position', type: 'vec3'},
    {name: 'pointSize', type: 'float'},
    {name: 'id', type: 'vec4'}
  ]
}
exports.contourShader = {
  vertex:   contourVertSrc,
  fragment: contourFragSrc,
  attributes: [
    {name: 'position', type: 'vec3'}
  ]
}
