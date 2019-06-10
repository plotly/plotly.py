'use strict'

var glslify = require('glslify')

exports.boxVertex = glslify('./shaders/box-vertex.glsl')
exports.boxFragment = glslify('./shaders/box-fragment.glsl')
