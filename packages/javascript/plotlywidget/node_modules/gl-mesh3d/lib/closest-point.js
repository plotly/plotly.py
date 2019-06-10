'use strict'

var barycentric            = require('barycentric')
var closestPointToTriangle = require('polytope-closest-point/lib/closest_point_2d.js')

module.exports = closestPointToPickLocation

function xformMatrix(m, v) {
  var out = [0,0,0,0]
  for(var i=0; i<4; ++i) {
    for(var j=0; j<4; ++j) {
      out[j] += m[4*i + j] * v[i]
    }
  }
  return out
}

function projectVertex(v, model, view, projection, resolution) {
  var p = xformMatrix(projection,
            xformMatrix(view,
              xformMatrix(model, [v[0], v[1], v[2], 1])))
  for(var i=0; i<3; ++i) {
    p[i] /= p[3]
  }
  return [ 0.5 * resolution[0] * (1.0+p[0]), 0.5 * resolution[1] * (1.0-p[1]) ]
}

function barycentricCoord(simplex, point) {
  if(simplex.length === 2) {
    var d0 = 0.0
    var d1 = 0.0
    for(var i=0; i<2; ++i) {
      d0 += Math.pow(point[i] - simplex[0][i], 2)
      d1 += Math.pow(point[i] - simplex[1][i], 2)
    }
    d0 = Math.sqrt(d0)
    d1 = Math.sqrt(d1)
    if(d0+d1 < 1e-6) {
      return [1,0]
    }
    return [d1/(d0+d1),d0/(d1+d0)]
  } else if(simplex.length === 3) {
    var closestPoint = [0,0]
    closestPointToTriangle(simplex[0], simplex[1], simplex[2], point, closestPoint)
    return barycentric(simplex, closestPoint)
  }
  return []
}

function interpolate(simplex, weights) {
  var result = [0,0,0]
  for(var i=0; i<simplex.length; ++i) {
    var p = simplex[i]
    var w = weights[i]
    for(var j=0; j<3; ++j) {
      result[j] += w * p[j]
    }
  }
  return result
}

function closestPointToPickLocation(simplex, pixelCoord, model, view, projection, resolution) {
  if(simplex.length === 1) {
    return [0, simplex[0].slice()]
  }
  var simplex2D = new Array(simplex.length)
  for(var i=0; i<simplex.length; ++i) {
    simplex2D[i] = projectVertex(simplex[i], model, view, projection, resolution);
  }

  var closestIndex = 0
  var closestDist  = Infinity
  for(var i=0; i<simplex2D.length; ++i) {
    var d2 = 0.0
    for(var j=0; j<2; ++j) {
      d2 += Math.pow(simplex2D[i][j] - pixelCoord[j], 2)
    }
    if(d2 < closestDist) {
      closestDist  = d2
      closestIndex = i
    }
  }

  var weights = barycentricCoord(simplex2D, pixelCoord)
  var s = 0.0
  for(var i=0; i<3; ++i) {
    if(weights[i] < -0.001 ||
       weights[i] > 1.0001) {
      return null
    }
    s += weights[i]
  }
  if(Math.abs(s - 1.0) > 0.001) {
    return null
  }
  return [closestIndex, interpolate(simplex, weights), weights]
}