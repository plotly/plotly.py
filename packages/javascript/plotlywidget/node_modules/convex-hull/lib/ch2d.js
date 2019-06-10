'use strict'

module.exports = convexHull2D

var monotoneHull = require('monotone-convex-hull-2d')

function convexHull2D(points) {
  var hull = monotoneHull(points)
  var h = hull.length
  if(h <= 2) {
    return []
  }
  var edges = new Array(h)
  var a = hull[h-1]
  for(var i=0; i<h; ++i) {
    var b = hull[i]
    edges[i] = [a,b]
    a = b
  }
  return edges
}
