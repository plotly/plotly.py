"use strict"

var uniq = require("uniq")

module.exports = generateTestPoints

function generateTestPoints(segments) {
  var x = [-1e20, 1e20]
  var y = [-1e20, 1e20]
  for(var i=0; i<segments.length; ++i) {
    var s = segments[i]
    x.push(s[0][0], s[1][0], 0.5 * (s[0][0] + s[1][0]), s[0][0]+1e-6, s[0][0]-1e-6, s[1][0]+1e-6, s[1][0]-1e-6)
    y.push(s[0][1], s[1][1], 0.5 * (s[0][1] + s[1][1]), s[0][1]+1e-6, s[0][1]-1e-6, s[1][1]+1e-6, s[1][1]-1e-6)
  }
  uniq(x, function(a,b) { return a-b })
  uniq(y, function(a,b) { return a-b })
  var points = []
  for(var i=0; i<x.length; ++i) {
    for(var j=0; j<y.length; ++j) {
      points.push([x[i], y[j]])
    }
  }
  return points
}