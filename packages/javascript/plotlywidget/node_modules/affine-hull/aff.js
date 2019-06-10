'use strict'

module.exports = affineHull

var orient = require('robust-orientation')

function linearlyIndependent(points, d) {
  var nhull = new Array(d+1)
  for(var i=0; i<points.length; ++i) {
    nhull[i] = points[i]
  }
  for(var i=0; i<=points.length; ++i) {
    for(var j=points.length; j<=d; ++j) {
      var x = new Array(d)
      for(var k=0; k<d; ++k) {
        x[k] = Math.pow(j+1-i, k)
      }
      nhull[j] = x
    }
    var o = orient.apply(void 0, nhull)
    if(o) {
      return true
    }
  }
  return false
}

function affineHull(points) {
  var n = points.length
  if(n === 0) {
    return []
  }
  if(n === 1) {
    return [0]
  }
  var d = points[0].length
  var frame = [ points[0] ]
  var index = [ 0 ]
  for(var i=1; i<n; ++i) {
    frame.push(points[i])
    if(!linearlyIndependent(frame, d)) {
      frame.pop()
      continue
    }
    index.push(i)
    if(index.length === d+1) {
      return index
    }
  }
  return index
}