'use strict'

var glslify = require('glslify')

var FRAGMENT = glslify('./shaders/fragment.glsl')

module.exports = {
  lineVert: glslify('./shaders/line-vertex.glsl'),
  lineFrag: FRAGMENT,
  textVert: glslify('./shaders/text-vertex.glsl'),
  textFrag: FRAGMENT,
  gridVert: glslify('./shaders/grid-vertex.glsl'),
  gridFrag: FRAGMENT,
  boxVert:  glslify('./shaders/box-vertex.glsl'),
  tickVert: glslify('./shaders/tick-vertex.glsl')
}
