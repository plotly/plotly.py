'use strict'

module.exports = textGet

var vectorizeText = require('vectorize-text')

var globals = window || process.global || {}
var __TEXT_CACHE  = globals.__TEXT_CACHE || {}
globals.__TEXT_CACHE = {}

function unwrap(mesh) {
  var cells     = mesh.cells
  var positions = mesh.positions
  var data      = new Float32Array(cells.length * 6)
  var ptr       = 0
  var shapeX    = 0
  for(var i=0; i<cells.length; ++i) {
    var tri = cells[i]
    for(var j=0; j<3; ++j) {
      var point = positions[tri[j]]
      data[ptr++] = point[0]
      data[ptr++] = point[1] + 1.4
      shapeX      = Math.max(point[0], shapeX)
    }
  }
  return {
    data:  data,
    shape: shapeX
  }
}

function textGet(font, text, opts) {
  var opts = opts || {}
  var fontcache = __TEXT_CACHE[font]
  if(!fontcache) {
    fontcache = __TEXT_CACHE[font] = {
      ' ': {
        data:   new Float32Array(0),
        shape: 0.2
      }
    }
  }
  var mesh = fontcache[text]
  if(!mesh) {
    if(text.length <= 1 || !/\d/.test(text)) {
      mesh = fontcache[text] = unwrap(vectorizeText(text, {
        triangles:     true,
        font:          font,
        textAlign:     opts.textAlign || 'left',
        textBaseline:  'alphabetic',
        styletags: {
            breaklines: true,
                 bolds: true,
               italics: true,
            subscripts: true,
          superscripts: true
        }
      }))
    } else {
      var parts = text.split(/(\d|\s)/)
      var buffer = new Array(parts.length)
      var bufferSize = 0
      var shapeX = 0
      for(var i=0; i<parts.length; ++i) {
        buffer[i] = textGet(font, parts[i])
        bufferSize += buffer[i].data.length
        shapeX += buffer[i].shape
        if(i>0) {
          shapeX += 0.02
        }
      }

      var data = new Float32Array(bufferSize)
      var ptr     = 0
      var xOffset = -0.5 * shapeX
      for(var i=0; i<buffer.length; ++i) {
        var bdata = buffer[i].data
        for(var j=0; j<bdata.length; j+=2) {
          data[ptr++] = bdata[j] + xOffset
          data[ptr++] = bdata[j+1]
        }
        xOffset += buffer[i].shape + 0.02
      }

      mesh = fontcache[text] = {
        data:  data,
        shape: shapeX
      }
    }
  }

   return mesh
}
