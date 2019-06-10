'use strict'

var glslify = require('glslify')
var createShader = require('gl-shader')

var lineVert = glslify('./lineVert.glsl')
var lineFrag = glslify('./lineFrag.glsl')
exports.line = function(gl) {
  return createShader(gl, lineVert, lineFrag, null, [
    {name: 'position', type: 'vec3'}
  ])
}

var textVert = glslify('./textVert.glsl')
var textFrag = glslify('./textFrag.glsl')
exports.text = function(gl) {
  return createShader(gl, textVert, textFrag, null, [
    {name: 'position', type: 'vec3'}
  ])
}

var bgVert = glslify('./backgroundVert.glsl')
var bgFrag = glslify('./backgroundFrag.glsl')
exports.bg = function(gl) {
  return createShader(gl, bgVert, bgFrag, null, [
    {name: 'position', type: 'vec3'},
    {name: 'normal', type: 'vec3'}
  ])
}
