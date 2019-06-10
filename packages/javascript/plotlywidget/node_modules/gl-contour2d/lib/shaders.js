'use strict'

var glslify = require('glslify')

module.exports = {
  fragment: glslify('./shaders/fragment.glsl'),
  vertex: glslify('./shaders/vertex.glsl'),
  fillVertex: glslify('./shaders/fill-vertex.glsl')
}
