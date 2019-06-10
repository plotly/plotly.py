"use strict"

module.exports = triangulateLoop

var cdt2d = require('cdt2d')

function triangulateLoop(loops, positions) {
  var edges = []
  for(var i=0; i<loops.length; ++i) {
    var loop = loops[i]
    for(var j=0; j<loop.length; ++j) {
      edges.push([loop[j], loop[(j+1)%loop.length]])
    }
  }
  return cdt2d(positions, edges, {
    delaunay: false,
    exterior: false
  })
}
