'use strict'

module.exports = barycentric

var solve = require('robust-linear-solve')

function reduce(x) {
  var r = 0
  for(var i=0; i<x.length; ++i) {
    r += x[i]
  }
  return r
}

function barycentric(simplex, point) {
  var d = point.length
  var A = new Array(d+1)
  for(var i=0; i<d; ++i) {
    var row = new Array(d+1)
    for(var j=0; j<=d; ++j) {
      row[j] = simplex[j][i]
    }
    A[i] = row
  }
  A[d] = new Array(d+1)
  for(var i=0; i<=d; ++i) {
    A[d][i] = 1
  }

  var b = new Array(d+1)
  for(var i=0; i<d; ++i) {
    b[i] = point[i]
  }
  b[d] = 1.0

  var x = solve(A, b)
  var w = reduce(x[d+1])
  
  if(w === 0) {
    w = 1.0
  }
  var y = new Array(d+1)
  for(var i=0; i<=d; ++i) {
    y[i] = reduce(x[i]) / w
  }
  return y
}