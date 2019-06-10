var extractContour = require('../contour')
var bunny = require('bunny')

//Solve for the curve z=0 on the surface of the bunny
var zvalues = bunny.positions.map(function(p) {
  return p[2]
})
var curve = extractContour(bunny.cells, zvalues, 0.0)

//Unpack edges and positions of curve
var curveEdges = curve.cells
var curvePositions = curve.vertexWeights.map(function(w,i) {
  var a = bunny.positions[curve.vertexIds[i][0]]
  var b = bunny.positions[curve.vertexIds[i][1]]

  return [
    w * a[0] + (1 - w) * b[0],
    w * a[1] + (1 - w) * b[1],
    w * a[2] + (1 - w) * b[2]
  ]
})

console.log({
  cells: curveEdges,
  positions: curvePositions
})