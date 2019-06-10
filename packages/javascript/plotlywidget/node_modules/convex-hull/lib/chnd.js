'use strict'

module.exports = convexHullnD

var ich = require('incremental-convex-hull')
var aff = require('affine-hull')

function permute(points, front) {
  var n = points.length
  var npoints = new Array(n)
  for(var i=0; i<front.length; ++i) {
    npoints[i] = points[front[i]]
  }
  var ptr = front.length
  for(var i=0; i<n; ++i) {
    if(front.indexOf(i) < 0) {
      npoints[ptr++] = points[i]
    }
  }
  return npoints
}

function invPermute(cells, front) {
  var nc = cells.length
  var nf = front.length
  for(var i=0; i<nc; ++i) {
    var c = cells[i]
    for(var j=0; j<c.length; ++j) {
      var x = c[j]
      if(x < nf) {
        c[j] = front[x]
      } else {
        x = x - nf
        for(var k=0; k<nf; ++k) {
          if(x >= front[k]) {
            x += 1
          }
        }
        c[j] = x
      }
    }
  }
  return cells
}

function convexHullnD(points, d) {
  try {
    return ich(points, true)
  } catch(e) {
    //If point set is degenerate, try to find a basis and rerun it
    var ah = aff(points)
    if(ah.length <= d) {
      //No basis, no try
      return []
    }
    var npoints = permute(points, ah)
    var nhull   = ich(npoints, true)
    return invPermute(nhull, ah)
  }
}