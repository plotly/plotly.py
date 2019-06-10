"use strict"

module.exports = axesProperties

var getPlanes   = require("extract-frustum-planes")
var splitPoly   = require("split-polygon")
var cubeParams  = require("./lib/cube.js")
var m4mul       = require("gl-mat4/multiply")
var m4transpose = require("gl-mat4/transpose")
var v4transformMat4 = require("gl-vec4/transformMat4")

var identity    = new Float32Array([
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1
  ])

var mvp         = new Float32Array(16)

function AxesRange3D(lo, hi, pixelsPerDataUnit) {
  this.lo = lo
  this.hi = hi
  this.pixelsPerDataUnit = pixelsPerDataUnit
}

var SCRATCH_P = [0,0,0,1]
var SCRATCH_Q = [0,0,0,1]

function gradient(result, M, v, width, height) {
  for(var i=0; i<3; ++i) {
    var p = SCRATCH_P
    var q = SCRATCH_Q
    for(var j=0; j<3; ++j) {
      q[j] = p[j] = v[j]
    }
    q[3] = p[3] = 1

    q[i] += 1
    v4transformMat4(q, q, M)
    if(q[3] < 0) {
      result[i] = Infinity
    }

    p[i] -= 1
    v4transformMat4(p, p, M)
    if(p[3] < 0) {
      result[i] = Infinity
    }

    var dx = (p[0]/p[3] - q[0]/q[3]) * width
    var dy = (p[1]/p[3] - q[1]/q[3]) * height

    result[i] = 0.25 * Math.sqrt(dx*dx + dy*dy)
  }
  return result
}

var RANGES = [
  new AxesRange3D(Infinity, -Infinity, Infinity),
  new AxesRange3D(Infinity, -Infinity, Infinity),
  new AxesRange3D(Infinity, -Infinity, Infinity)
]

var SCRATCH_X = [0,0,0]

function axesProperties(axes, camera, width, height, params) {
  var model       = camera.model || identity
  var view        = camera.view || identity
  var projection  = camera.projection || identity
  var isOrtho     = camera._ortho || false
  var bounds      = axes.bounds
  var params      = params || cubeParams(model, view, projection, bounds, isOrtho)
  var axis        = params.axis

  m4mul(mvp, view, model)
  m4mul(mvp, projection, mvp)

  //Calculate the following properties for each axis:
  //
  // * lo - start of visible range for each axis in tick coordinates
  // * hi - end of visible range for each axis in tick coordinates
  // * ticksPerPixel - pixel density of tick marks for the axis
  //
  var ranges = RANGES
  for(var i=0; i<3; ++i) {
    ranges[i].lo = Infinity
    ranges[i].hi = -Infinity
    ranges[i].pixelsPerDataUnit = Infinity
  }

  //Compute frustum planes, intersect with box
  var frustum = getPlanes(m4transpose(mvp, mvp))
  m4transpose(mvp, mvp)

  //Loop over vertices of viewable box
  for(var d=0; d<3; ++d) {
    var u = (d+1)%3
    var v = (d+2)%3
    var x = SCRATCH_X
i_loop:
    for(var i=0; i<2; ++i) {
      var poly = []

      if((axis[d] < 0) === !!i) {
        continue
      }

      x[d] = bounds[i][d]
      for(var j=0; j<2; ++j) {
        x[u] = bounds[j^i][u]
        for(var k=0; k<2; ++k) {
          x[v] = bounds[k^j^i][v]
          poly.push(x.slice())
        }
      }

      var Q = (isOrtho) ? 5 : 4
      for(var j=Q; j===Q; ++j) { // Note: using only near plane here (& for orthographic projection we use the far).
        if(poly.length === 0) {
          continue i_loop
        }
        poly = splitPoly.positive(poly, frustum[j])
      }

      //Loop over vertices of polygon to find extremal points
      for(var j=0; j<poly.length; ++j) {
        var v = poly[j]
        var grad = gradient(SCRATCH_X, mvp, v, width, height)
        for(var k=0; k<3; ++k) {
          ranges[k].lo = Math.min(ranges[k].lo, v[k])
          ranges[k].hi = Math.max(ranges[k].hi, v[k])
          if(k !== d) {
            ranges[k].pixelsPerDataUnit = Math.min(ranges[k].pixelsPerDataUnit, Math.abs(grad[k]))
          }
        }
      }
    }
  }

  return ranges
}
