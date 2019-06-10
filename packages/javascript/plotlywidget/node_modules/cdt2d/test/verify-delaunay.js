'use strict'

var cdt = require('../cdt2d')
var verifyTriangulation = require('./verify-triangulation')

function verifyDelaunay(tape, points, edges) {
  var triangles = cdt(points, edges)

  //First verify triangulation is consistent
  verifyTriangulation(tape, points, edges, triangles)

  
}
