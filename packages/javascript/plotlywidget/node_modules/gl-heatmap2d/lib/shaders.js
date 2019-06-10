'use strict'

var glslify = require('glslify')

module.exports = {
  fragment:     glslify('./shaders/fragment.glsl'),
  vertex:       glslify('./shaders/vertex.glsl'),
  pickFragment: glslify('./shaders/pick-fragment.glsl'),
  pickVertex:   glslify('./shaders/pick-vertex.glsl')
}
