'use strict'

module.exports = createTable

var chull = require('convex-hull')

function constructVertex(d, a, b) {
  var x = new Array(d)
  for(var i=0; i<d; ++i) {
    x[i] = 0.0
    if(i === a) {
      x[i] += 0.5
    }
    if(i === b) {
      x[i] += 0.5
    }
  }
  return x
}

function constructCell(dimension, mask) {
  if(mask === 0 || mask === (1<<(dimension+1))-1) {
    return []
  }
  var points = []
  var index  = []
  for(var i=0; i<=dimension; ++i) {
    if(mask & (1<<i)) {
      points.push(constructVertex(dimension, i-1, i-1))
      index.push(null)
      for(var j=0; j<=dimension; ++j) {
        if(~mask & (1<<j)) {
          points.push(constructVertex(dimension, i-1, j-1))
          index.push([i,j])
        }
      }
    }
  }
  
  //Preprocess points so first d+1 points are linearly independent
  var hull = chull(points)
  var faces = []
i_loop:
  for(var i=0; i<hull.length; ++i) {
    var face = hull[i]
    var nface = []
    for(var j=0; j<face.length; ++j) {
      if(!index[face[j]]) {
        continue i_loop
      }
      nface.push(index[face[j]].slice())
    }
    faces.push(nface)
  }
  return faces
}

function createTable(dimension) {
  var numCells = 1<<(dimension+1)
  var result = new Array(numCells)
  for(var i=0; i<numCells; ++i) {
    result[i] = constructCell(dimension, i)
  }
  return result
}