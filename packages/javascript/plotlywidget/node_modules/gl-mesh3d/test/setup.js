'use strict'

var ndarray = require('ndarray')

function setupGL() {
  var canvas = document.createElement('canvas')
  canvas.width = canvas.height = 512
  return canvas.getContext('webgl')
}

exports.setup = setup

function readPixels(gl) {
  var pixels = new Uint8Array(512*512*4)
  gl.readPixels(0, 0, 512, 512, gl.RGBA, gl.UNSIGNED_BYTE, pixels)
  return ndarray(pixels, [512,512,4])
}
exports.readPixels = readPixels