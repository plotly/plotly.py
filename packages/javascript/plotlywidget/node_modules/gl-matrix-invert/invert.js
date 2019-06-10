'use strict'

module.exports = invert

var invert2 = require('gl-mat2/invert')
var invert3 = require('gl-mat3/invert')
var invert4 = require('gl-mat4/invert')

function invert(out, M) {
  switch(M.length) {
    case 0:
    break
    case 1:
      out[0] = 1.0 / M[0]
    break
    case 4:
      invert2(out, M)
    break
    case 9:
      invert3(out, M)
    break
    case 16:
      invert4(out, M)
    break
    default:
      throw new Error('currently supports matrices up to 4x4')
    break
  }
  return out
}