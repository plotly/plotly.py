'use strict'

var warp = require('ndarray-warp')
var invert = require('gl-matrix-invert')

module.exports = applyHomography

function applyHomography(dest, src, Xi) {
  var n = src.dimension
  var X = invert([], Xi)
  warp(dest, src, function(out_c, inp_c) {
    for(var i=0; i<n; ++i) {
      out_c[i] = X[(n+1)*n + i]
      for(var j=0; j<n; ++j) {
        out_c[i] += X[(n+1)*j+i] * inp_c[j]
      }
    }
    var w = X[(n+1)*(n+1)-1]
    for(var j=0; j<n; ++j) {
      w += X[(n+1)*j+n] * inp_c[j]
    }
    var wr = 1.0 / w
    for(var i=0; i<n; ++i) {
      out_c[i] *= wr
    }
    return out_c
  })
  return dest
}